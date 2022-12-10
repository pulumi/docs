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
	"strings"

	"github.com/pkg/errors"
	"github.com/russross/blackfriday/v2"
)

var langAbbreviations = []string{"js", "ts", "go", "py", "cs", "fs", "java", "yaml"}

var langMap = map[string]string{
	"js":   "JavaScript",
	"ts":   "TypeScript",
	"go":   "Go",
	"py":   "Python",
	"cs":   "C#",
	"fs":   "F#",
	"yaml": "YAML",
	"java": "Java",
}

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
		h1 = strings.TrimSpace(h1)

		// Each tutorial directory follows a convention: <cloud>-<language>-<short-name>. Parse it.
		// Warn and ignore any that don't follow this convention (ideally we'd fix them).
		cloud := ""
		language := ""
		for _, langAbbreviation := range langAbbreviations {
			languageAbbreviationIndex := strings.Index(file.Name(), "-"+langAbbreviation+"-")
			languageFound := languageAbbreviationIndex >= 0

			if languageFound {
				cloud = file.Name()[0:languageAbbreviationIndex]
				language = langAbbreviation
				break
			}
		}

		if cloud == "" || language == "" {
			warn("malformed tutorial name; expected <cloud>-<language>-<short-name>, got '%s'", name)
			continue
		}

		// Add the language to the page title and meta descriptions to avoid duplicates.
		var title string
		var metaDescription string

		if val, ok := langMap[language]; ok {
			title = fmt.Sprintf("%s | %s", h1, val)
			metaDescription = fmt.Sprintf("%s How-to Guide using %s", h1, val)
		}

		// Great! We have a new tutorial. Append it and let's move on to the next one.
		tutorials = append(tutorials, tutorial{
			Name:  name,
			Title: title,
			H1:    h1,
			// LinkTitle is the display text for the breadcrumb control.
			LinkTitle:         h1,
			MetaDesc:          metaDescription,
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
	gitHubBaseURL            = "https://github.com/pulumi/examples"
	gitHubUserContentBaseURL = "https://raw.githubusercontent.com/pulumi/examples"
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
