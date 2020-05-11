// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package main

import (
	"flag"
	"fmt"
	"io/ioutil"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"sort"
	"strings"

	"github.com/pkg/errors"
	"github.com/russross/blackfriday/v2"
)

// clouds contains an index of the clouds for which we want to publish tutorials.
var clouds = []string{"aws", "azure", "gcp", "kubernetes"}

func main() {
	// Parse and validate the args.
	flag.Parse()
	args := flag.Args()
	if len(args) < 2 {
		exitErr("usage: %s <tutorial-repo> <docs-root-dir>", os.Args[0])
	}
	repo := os.Args[1]
	docsRoot := os.Args[2]

	// Clone the tutorial repo at master/HEAD so the tool isn't dependent on the local filesystem.
	fmt.Printf("Gathering tutorials from %s...\n", repo)
	tmp, err := ioutil.TempDir("", "")
	if err != nil {
		exitErr("creating temp dir for tutorial repo: %v", err)
	}
	defer os.RemoveAll(tmp)
	cmd := exec.Command("git", "clone", repo, "--depth=1", tmp)
	cmd.Stdout = os.Stdout
	if err = cmd.Run(); err != nil {
		exitErr("cloning tutorial repo: %v", err)
	}

	// Now, for every directory in the tutorial repo, accumulate metadata.
	tuts, err := gatherTutorials(tmp)
	if err != nil {
		exitErr("gathering tutorials: %v", err)
	}
	fmt.Printf("\tGathered %d tutorials.\n", len(tuts))

	// Emit the shortcode indexes; one global index and another per-cloud index.
	shortcodesDir := filepath.Join(docsRoot, "shortcodes")
	fmt.Printf("Generating shortcode pages...\n")
	if err = emitGlobalIndexShortcode(shortcodesDir, tuts); err != nil {
		exitErr("emitting global index shortcode: %v", err)
	}
	for _, cloud := range clouds {
		if err = emitCloudIndexShortcode(shortcodesDir, cloud, tuts); err != nil {
			exitErr("emitting cloud %s index shortcode: %v", cloud, err)
		}
	}

	// And now finally create the actual tutorial pages, primarily by copying the tutorial READMEs.
	fmt.Printf("Generating template pages...\n")
	templatesDir := filepath.Join(docsRoot, "tutorials")
	if err = emitTutorialDocs(templatesDir, tuts); err != nil {
		exitErr("emitting templates: %v", err)
	}
}

type tutorial struct {
	Name              string
	Title             string
	H1                string
	LinkTitle         string
	MetaDesc          string
	Cloud             string
	Language          string
	Body              string
	URL               string
	GitHubURL         string
	PulumiTemplateURL string
}

func gatherTutorials(root string) ([]tutorial, error) {
	files, err := ioutil.ReadDir(root)
	if err != nil {
		return nil, errors.Wrapf(err, "reading tutorial repo")
	}

	// For all tutorials, gather up the metadata.
	var tutorials []tutorial
	for _, file := range files {
		name := file.Name()
		if !file.IsDir() || name[0] == '.' {
			continue
		}
		githubURL := fmt.Sprintf("%s/tree/master/%s", gitHubBaseURL, name)
		pulumiTemplateURL := ""

		// Each tutorial directory follows a convention: <cloud>-<language>-<short-name>. Parse it.
		// Warn and ignore any that don't follow this convention (ideally we'd fix them).
		var parts []string
		for i, rem := 0, file.Name(); i < 2; i++ {
			dashIx := strings.Index(rem, "-")
			if dashIx == -1 {
				break
			}
			parts = append(parts, rem[:dashIx])
			rem = rem[dashIx+1:]
		}
		if len(parts) != 2 || parts[0] == "" || parts[1] == "" {
			warn("malformed tutorial name; expected <cloud>-<language>-<short-name>, got '%s'", name)
			continue
		}

		// Now that we've got the cloud and language, parse the contents to get extra metadata.
		body, err := ioutil.ReadFile(filepath.Join(root, name, "README.md"))
		if err != nil {
			if os.IsNotExist(err) {
				warn("tutorial is missing a README: %s", name)
				continue
			}
			return nil, errors.Wrapf(err, "reading tutorial '%s' README", name)
		}
		md := blackfriday.New()
		top := md.Parse(body)

		// The first H1 is assumed to be the title.
		var h1 string
		top.Walk(func(node *blackfriday.Node, entering bool) blackfriday.WalkStatus {
			if node.Type == blackfriday.Link {
				destination := string(node.LinkData.Destination)
				if destination == "https://app.pulumi.com/new" {
					pulumiTemplateURL = githubURL
				} else if strings.HasPrefix(destination, "https://app.pulumi.com/new?template=") {
					pulumiTemplateURL = strings.TrimPrefix(destination, "https://app.pulumi.com/new?template=")
				}
			}
			if node.Type == blackfriday.Heading && node.HeadingData.Level == 1 {
				node.Walk(func(inner *blackfriday.Node, entering bool) blackfriday.WalkStatus {
					if inner.Type == blackfriday.Text {
						h1 += string(inner.Literal)
					}
					return blackfriday.GoToNext
				})
				return blackfriday.Terminate
			}
			return blackfriday.GoToNext
		})
		if h1 == "" {
			warn("tutorial is missing an H1 title: %s", name)
			continue
		}

		// Assign the parts of the tutorial name to variables.
		cloud := parts[0]
		language := parts[1]

		// Add the language to the page title to avoid duplicate titles.
		var title string
		langMap := map[string]string{
			"js": "JavaScript",
			"ts": "TypeScript",
			"go": "Go",
			"py": "Python",
			"cs": "C#",
		}
		if val, ok := langMap[language]; ok {
			title = fmt.Sprintf("%s | %s", h1, val)
		}

		// Great! We have a new tutorial. Append it and let's move on to the next one.
		tutorials = append(tutorials, tutorial{
			Name:  name,
			Title: title,
			H1:    h1,
			// LinkTitle is the display text for the breadcrumb control.
			LinkTitle:         h1,
			MetaDesc:          "",
			Cloud:             cloud,
			Language:          language,
			Body:              cleanMarkdownBody(name, string(body)),
			URL:               fmt.Sprintf("/docs/tutorials/%s/%s/", cloud, name),
			GitHubURL:         githubURL,
			PulumiTemplateURL: pulumiTemplateURL,
		})
	}

	return tutorials, nil
}

const (
	gitHubBaseURL                 = "https://github.com/pulumi/examples"
	gitHubUserContentBaseURL      = "https://raw.githubusercontent.com/pulumi/examples"
	tutorialsIndexShortcodePrefix = "tutorials-index"
)

var (
	markdownLinkURL = regexp.MustCompile(`(?mU)\[(.*)\]\((.*)\)`)
	imageLink       = regexp.MustCompile(`.*\.(?:png|gif|jpe?g)`)
)

func cleanMarkdownBody(name, body string) string {
	// HACK: for now, skip everything leading up to, and including, the H1. The reason is otherwise
	// Hugo will add an H1 (due to our template). And we want to ensure we can add the badge explicitly.
	h1ix := strings.Index(body, "# ")
	if h1ix == -1 {
		return body
	}
	body = body[h1ix:]
	nlix := strings.Index(body, "\n")
	if nlix == -1 {
		return body
	}
	tidied := body[nlix+1:]

	// Also rewrite any URLs that are local to this repo so they refer back to the GitHub repo content.
	var lix int
	var result string
	for _, loc := range markdownLinkURL.FindAllStringSubmatchIndex(tidied, -1) {
		// Locations:
		//    - 0:1 is start:end
		//    - 2:3 is the [...] part, i.e. text
		//    - 4:5 is the (...) part, i.e. URL
		result += tidied[lix:loc[0]]
		mdtext := tidied[loc[2]:loc[3]]
		mdurl := tidied[loc[4]:loc[5]]

		// If the URL contains a scheme, we have no reason to replace it.
		if !strings.Contains(mdurl, "://") && !strings.HasPrefix(mdurl, "../") {
			// Otherwise, we need to make it relative to the Git repo's contents.
			if strings.HasPrefix(mdurl, "./") {
				mdurl = mdurl[2:]
			}
			// If it's an image, we use the GitHub user content domain to the image actually displays.
			if imageLink.MatchString(mdurl) {
				mdurl = fmt.Sprintf("%s/master/%s/%s", gitHubUserContentBaseURL, name, mdurl)
			} else {
				mdurl = fmt.Sprintf("%s/blob/master/%s/%s", gitHubBaseURL, name, mdurl)
			}
		}
		result += fmt.Sprintf("[%s](%s)", mdtext, mdurl)

		lix = loc[1]
	}
	if lix < len(tidied) {
		result += tidied[lix:]
	}

	return result
}

func makeLangMap(tutorials []tutorial, include []string, exclude []string) (map[string][]tutorial, int) {
	// Split tutorials out into respective languages.
	tuts := map[string][]tutorial{
		"js": nil,
		"ts": nil,
		"py": nil,
	}
	var c int
	for _, tut := range tutorials {
		cloud := tut.Cloud
		lang := tut.Language
		if _, has := tuts[lang]; has {
			// Filter out any specific included or excluded clouds.
			if len(include) > 0 {
				var found bool
				for _, incl := range include {
					if incl == cloud {
						found = true
						break
					}
				}
				if !found {
					continue
				}
			}
			if len(exclude) > 0 {
				var found bool
				for _, excl := range exclude {
					if excl == cloud {
						found = true
						break
					}
				}
				if found {
					continue
				}
			}
			tuts[lang] = append(tuts[lang], tut)
			c++
		}
	}

	// Sort the tutorials: first by cloud then by title.
	for _, ts := range tuts {
		sort.Slice(ts, func(i, j int) bool {
			if ts[i].Cloud == ts[j].Cloud {
				if ts[i].Language == ts[j].Language {
					return ts[i].Title < ts[j].Title
				}
				return ts[i].Language < ts[j].Language
			}
			return ts[i].Cloud < ts[j].Cloud
		})
	}

	return tuts, c
}

func emitGlobalIndexShortcode(root string, tutorials []tutorial) error {
	// Open the global shortcode file.
	fn := tutorialsIndexShortcodePrefix + ".html"
	path := filepath.Join(root, fn)
	if err := os.MkdirAll(filepath.Dir(path), 0700); err != nil {
		return err
	}
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()

	// Get the full list of tutorials, by language, excluding some of them.
	tuts, c := makeLangMap(tutorials, clouds, nil)

	// Render the template using the tutorials data.
	if err = globalIndexTemplate.FRender(f, map[string]interface{}{
		"JavaScriptTutorials": tuts["js"],
		"TypeScriptTutorials": tuts["ts"],
		"PythonTutorials":     tuts["py"],
	}); err != nil {
		return err
	}
	fmt.Printf("\tEmitted global index: %s (%d tutorials).\n", fn, c)
	return nil
}

func emitCloudIndexShortcode(root, cloud string, tutorials []tutorial) error {
	// Open the cloud-specific shortcode file.
	fn := tutorialsIndexShortcodePrefix + "-" + cloud + ".html"
	path := filepath.Join(root, fn)
	if err := os.MkdirAll(filepath.Dir(path), 0700); err != nil {
		return err
	}
	f, err := os.Create(path)
	if err != nil {
		return err
	}
	defer f.Close()

	// Filter the tutorials down to just this cloud.
	tuts, c := makeLangMap(tutorials, []string{cloud}, nil)

	// Render the template using the tutorials data.
	if err = cloudIndexTemplate.FRender(f, map[string]interface{}{
		"JavaScriptTutorials": tuts["js"],
		"TypeScriptTutorials": tuts["ts"],
		"PythonTutorials":     tuts["py"],
	}); err != nil {
		return err
	}
	fmt.Printf("\tEmitted cloud index: %s (%d tutorials).\n", fn, c)
	return nil
}

func emitTutorialDocs(root string, tutorials []tutorial) error {
	// For each cloud, create a sub-directory, and then render the README bodies into the right content.
	for _, tut := range tutorials {
		// Open the file for writing and ensure the cloud directory exists.
		path := filepath.Join(root, tut.Cloud, tut.Name+".md")
		if err := os.MkdirAll(filepath.Dir(path), 0700); err != nil {
			return err
		}
		f, err := os.Create(path)
		if err != nil {
			return err
		}

		// Now render this specific tutorial file.
		err = tutorialTemplate.FRender(f, tut)

		// Close the file explicitly here so defer doesn't end up waiting until the end of the function.
		f.Close()

		// Now check the error after we're sure we closed the file.
		if err != nil {
			return err
		}
	}
	fmt.Printf("\tEmitted %d tutorial docs.\n", len(tutorials))
	return nil
}

func warn(msg string, a ...interface{}) {
	msg = fmt.Sprintf(msg, a...)
	fmt.Fprintf(os.Stderr, "warning: %s\n", msg)
}

func exitErr(msg string, a ...interface{}) {
	msg = fmt.Sprintf(msg, a...)
	fmt.Fprintf(os.Stderr, "error: %s\n", msg)
	os.Exit(1)
}
