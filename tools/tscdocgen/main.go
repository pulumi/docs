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
	"encoding/json"
	"flag"
	"fmt"
	"html"
	"io/ioutil"
	"log"
	"os"
	"path"
	"path/filepath"
	"regexp"
	"sort"
	"strings"
	"unicode"

	"github.com/pkg/errors"
)

func main() {
	// Grab the args.
	flag.Parse()
	args := flag.Args()
	if len(args) < 6 {
		fmt.Fprintf(os.Stderr, "error: usage: %s <src-dir> <pkg-name> <doc-file> <out-dir> <out-data-dir> <pkg-repo-dir> <git-hash>\n", os.Args[0])
		os.Exit(1)
	}

	// Load and parse the document.
	doc, err := loadAndParseDoc(args[2])
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: reading and parsing docs file: %v\n", err)
		os.Exit(1)
	}

	// Assuming that succeeded, simply emit the Markdown docs now.
	if err = emitMarkdownDocs(args[0], args[1], doc, args[3], args[4], args[5], args[6]); err != nil {
		fmt.Fprintf(os.Stderr, "error: emitting Markdown docs: %v\n", err)
		os.Exit(2)
	}
}

// loadAndParseDoc loads the given docs file -- expected to be in Typedoc JSON format -- and parses it into memory.
func loadAndParseDoc(filename string) (*typeDocNode, error) {
	// Read the file.
	b, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	// Parse it.
	var doc typeDocNode
	if err = json.Unmarshal(b, &doc); err != nil {
		return nil, err
	}

	filterOutInternalNode(&doc)

	return &doc, nil
}

func filterOutInternalNode(node *typeDocNode) *typeDocNode {
	if node == nil {
		return nil
	}

	if node.Kind == typeDocExternalModuleNode {
		// These modules were renamed.  We don't need the docs for their prior names.
		modname := getModuleParentName(node.Name)
		if modname == "\"applicationloadbalancing" ||
			modname == "\"elasticloadbalancing" ||
			modname == "\"elasticloadbalancingv2" {
			return nil
		}
	}

	// typedoc represents @internal on a method/function by placing the tag on the 'Signature' of
	// that item. So, look to see if we previously had any signatures, but then end up filtering
	// them all out.  If so, then we don't want to include this function at all.
	originalSigLength := len(node.Signatures)
	node.Signatures = filterOutInternalNodeArray(node.Signatures)
	if originalSigLength > 0 && len(node.Signatures) == 0 {
		return nil
	}

	node.IndexSignatures = filterOutInternalNodeArray(node.IndexSignatures)
	node.Children = filterOutInternalNodeArray(node.Children)
	node.TypeParameter = filterOutInternalNodeArray(node.TypeParameter)
	node.Parameters = filterOutInternalNodeArray(node.Parameters)
	node.ExtendedBy = filterOutInternalTypeArray(node.ExtendedBy)
	node.ExtendedTypes = filterOutInternalTypeArray(node.ExtendedTypes)
	node.ImplementedTypes = filterOutInternalTypeArray(node.ImplementedTypes)

	return node
}

func filterOutInternalNodeArray(arr []*typeDocNode) []*typeDocNode {
	if arr == nil {
		return nil
	}

	var result []*typeDocNode

	for _, val := range arr {
		if hasTag(val, "internal") {
			continue
		}

		val = filterOutInternalNode(val)
		if val != nil {
			result = append(result, val)
		}
	}

	return result
}

func filterOutInternalTypeArray(arr []*typeDocType) []*typeDocType {
	if arr == nil {
		return nil
	}

	var result []*typeDocType

	for _, val := range arr {
		val = filterOutInternalType(val)
		if val != nil {
			result = append(result, val)
		}
	}

	return result
}

func filterOutInternalType(t *typeDocType) *typeDocType {
	if t == nil {
		return nil
	}

	if t.Declaration != nil {
		t.Declaration = filterOutInternalNode(t.Declaration)
		if t.Declaration == nil {
			return nil
		}
	}

	t.Elements = filterOutInternalTypeArray(t.Elements)
	t.ElementType = filterOutInternalType(t.ElementType)
	t.TypeArguments = filterOutInternalTypeArray(t.TypeArguments)
	t.Types = filterOutInternalTypeArray(t.Types)
	t.Target = filterOutInternalType(t.Target)
	t.Declaration = filterOutInternalNode(t.Declaration)

	return t
}

func hasTag(node *typeDocNode, value string) bool {
	for _, tag := range node.Comment.Tags {
		if tag.Tag == value {
			return true
		}
	}

	return false
}

func getTag(node *typeDocNode, value string) (string, bool) {
	for _, tag := range node.Comment.Tags {
		if tag.Tag == value {
			return strings.TrimSpace(tag.Text), true
		}
	}

	return "", false
}

// emitMarkdownDocs takes as input a full Typedoc AST, transforms it into Markdown suitable for our documentation
// website, and emits those files into the target directory.  If the target doesn't exist, it will be created.
func emitMarkdownDocs(srcdir, pkgname string, doc *typeDocNode, outdir, outdatadir, pkgRepoDir, gitSha string) error {

	// First, gather up the entries by module.  Note that we are doing something dubious here to make our docs
	// easier to use and navigate than the default ones that Typedoc generates.  We are assuming an idiomatic module
	// structure with top-level index-style exports for each submodule.  In the general case, this isn't always true,
	// and we may generate (a) incorrect documentation by showing something that isn't truly exported and (b) omit
	// important details about the specific inner modules that truly contain the members in question.  I'm sure we'll
	// want to revisit this and make the logic here more sophisticated and general purpose someday.
	pkg := doc.Name

	repoURL := getRepoURL(pkgRepoDir, gitSha)

	// The kubernetes package requires some special handling since the structure differs from
	// the tf-generated providers.
	k8s := false
	if pkg == "@pulumi/kubernetes" {
		k8s = true
	}

	e := newEmitter(pkg, pkgname, srcdir, repoURL, outdir, outdatadir, pkgRepoDir, k8s)

	// Gather modules.
	root, err := e.gatherModules(doc, rootModule)
	if err != nil {
		return err
	}
	e.root = root

	// Emit the root module, which will emit its submodules recursively.
	return e.emitMarkdownModule(rootModule, root, gitSha, true)
}

type emitter struct {
	pkg        string  // the NPM package name.
	pkgname    string  // the simple name of the package.
	srcdir     string  // the source directory for docs, etc.
	repoURL    string  // the base repo URL for this package's code.
	outdir     string  // where to store the output files.
	outdatadir string  // where to store output data.
	pkgrepodir string  // the package repo directory.
	root       *module // the root module.
	k8s        bool    // whether this is the kubernetes module.
}

func newEmitter(pkg, pkgname, srcdir, repoURL, outdir, outdatadir, pkgRepoDir string, k8s bool) *emitter {
	return &emitter{
		pkg:        pkg,
		pkgname:    pkgname,
		srcdir:     srcdir,
		repoURL:    repoURL,
		outdir:     outdir,
		outdatadir: outdatadir,
		pkgrepodir: pkgRepoDir,
		k8s:        k8s,
	}
}

type moduleEmitter struct {
	e   *emitter // the current emitter.
	mod *module  // the current module being emitted.
}

func newModuleEmitter(e *emitter, mod *module) *moduleEmitter {
	return &moduleEmitter{
		e:   e,
		mod: mod,
	}
}

func getRepoURL(pkgRepoDir, gitSha string) string {
	repo := strings.Split(pkgRepoDir, "/")[0]
	dir := strings.TrimPrefix(pkgRepoDir, repo)
	dir = strings.TrimPrefix(dir, "/")
	return fmt.Sprintf("https://github.com/pulumi/%s/blob/%s/%s", repo, gitSha, dir)
}

var (
	h3RE = regexp.MustCompile(`(?m)^### `)
	h2RE = regexp.MustCompile(`(?m)^## `)
)

const (
	h4 = "#### "
	h5 = "##### "
)

// augmentNode recurses throughout a tree AST, adding information that we'll need when translating it to Markdown.
func (e *moduleEmitter) augmentNode(node *typeDocNode, parent *typeDocNode) {
	// Add some labels.
	node.AnchorName = node.Name
	if parent != nil && (parent.Kind == typeDocClassNode || parent.Kind == typeDocInterfaceNode) {
		node.AnchorName = fmt.Sprintf("%s-%s", parent.Name, node.AnchorName)
	}
	node.Label = e.createLabel(node, parent)
	node.CodeDetails = e.createCodeDetails(node)
	node.URLPath = e.getURLPath(node, parent)

	if isResource(node) {
		node.IsResource = true
	} else if isFunction(node) {
		node.IsFunction = true
	}

	node.DeprecatedMessage, node.IsDeprecated = getTag(node, "deprecated")

	// Convert <h3>'s to be <h5>'s, and <h2>'s to be <h4>'s.
	node.Comment.ShortText = h3RE.ReplaceAllString(node.Comment.ShortText, h5)
	node.Comment.Text = h3RE.ReplaceAllString(node.Comment.Text, h5)
	node.Comment.ShortText = h2RE.ReplaceAllString(node.Comment.ShortText, h4)
	node.Comment.Text = h2RE.ReplaceAllString(node.Comment.Text, h4)

	// In K8S docs, ShortText can contain placeholder references that look like HTML tags.
	// We need to replace those with the HTML-encoded characters.
	// For example, the text might contain references like this:
	// "<namespace>/<name>", where <namespace> is a placeholder for an actual namespace value,
	// and <name> is a placeholder for an actual name value.
	//
	// This is done specifically for K8S because other providers can contain valid use of the
	// > and < characters, which we don't want to escape.
	if e.e.k8s &&
		strings.Contains(node.Comment.ShortText, "<") &&
		strings.Contains(node.Comment.ShortText, ">") {
		// To avoid double-encoding strings that are already encoded, we make a targeted replacement
		// of the < and > characters alone.
		node.Comment.ShortText = strings.ReplaceAll(node.Comment.ShortText, "<", "&lt;")
		node.Comment.ShortText = strings.ReplaceAll(node.Comment.ShortText, ">", "&gt;")
	}

	// Augment everything deeply.
	for _, child := range node.Children {
		e.augmentNode(child, node)
	}
	for _, sig := range node.Signatures {
		e.augmentNode(sig, node)
	}
	if len(node.Signatures) > 20 {
		// To avoid places where we have 1000+ overloads from becoming unreadable, limit the lists
		// of overloads to 20, and show a note that there are more available instead of rendering
		// them all.
		node.Signatures = append(node.Signatures[:20], &typeDocNode{
			Label: fmt.Sprintf("+ %d additional overloads", len(node.Signatures)-20),
		})
	}
	for _, param := range node.Parameters {
		e.augmentNode(param, node)
	}

	// Reorder children based on their labels.
	sort.SliceStable(node.Children, func(i, j int) bool {
		return node.Children[i].Label < node.Children[j].Label
	})
}

// camelCase converts a string into camelCase starting with a lower case letter.
func camelCase(s string) string {
	buffer := make([]rune, 0, len(s))

	var prev rune
	for _, curr := range s {
		if curr != '-' {
			if prev == '-' {
				buffer = append(buffer, unicode.ToUpper(curr))
			} else {
				buffer = append(buffer, unicode.ToLower(curr))
			}
		}
		prev = curr
	}

	return string(buffer)
}

// emitMarkdownModule emits a single markdown module into the given directory.
func (e *emitter) emitMarkdownModule(name string, mod *module, gitSha string, root bool) error {
	// Open the file we're about to write into.  Each module gets one.
	filename := filepath.Join(e.outdir, getModuleFilename(name))
	if err := os.MkdirAll(filepath.Dir(filename), 0700); err != nil {
		return err
	}
	f, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer f.Close()

	// Populate a set of variables required during rendering.

	// First a title and some additional package header info, for the root module.
	var title string
	var titleTag string
	var linktitle string
	var pkg string
	var pkgvar string
	var readme string

	if root {
		title = fmt.Sprintf("Package %s", e.pkg)
		titleTag = fmt.Sprintf("Package %s", e.pkg)
		linktitle = e.pkg
		pkg = e.pkg
		pkgvar = camelCase(e.pkg[strings.IndexRune(e.pkg, '/')+1:])
		readme = filepath.Join(e.srcdir, "README.md")
	} else {
		title = fmt.Sprintf("Module %s", name)
		titleTag = fmt.Sprintf("%s | Package %s", title, e.pkg)
		readme = filepath.Join(e.srcdir, name, "README.md")
		linktitle = name
		if slix := strings.IndexRune(linktitle, '/'); slix != -1 {
			linktitle = linktitle[slix+1:]
		}
	}

	// See if there is a README.md file and, if so, include it as the package's comment.
	pkgcomm, err := ioutil.ReadFile(readme)
	if err != nil && !os.IsNotExist(err) {
		return err
	}

	modEmitter := newModuleEmitter(e, mod)

	// Now build an index of files and members.
	var files []string
	filesAdded := make(map[string]bool)
	var members []*typeDocNode
	for _, member := range mod.Exports {
		for _, source := range member.Sources {
			if isLocalSource(source) {
				if !filesAdded[source.FileName] {
					files = append(files, source.FileName)
					filesAdded[source.FileName] = true
				}
			}
		}

		modEmitter.augmentNode(member, nil)

		members = append(members, member)
	}

	// Ensure the files, members, and children (deeply throughout the tree) are sorted deterministically.
	sort.Strings(files)
	transitiveSortNodes(members, false /*sortByLabel*/)

	// Get any submodules, make relative links, and ensure they are also sorted in a deterministic order.
	var modules []struct {
		Name string
		Link string
	}
	for modname, module := range mod.Modules {
		if module.IsEmpty() {
			continue
		}

		var link string
		prefix := name + "/"
		if nix := strings.Index(modname, prefix); nix != -1 {
			link = modname[len(prefix):]
		} else {
			link = modname
		}

		// Hugo converts all paths to lowercase by default when publishing, so we make these links lowercase as well.
		link = strings.ToLower(link)

		// Ensure the link has a trailing slash to avoid the S3 302 redirect dance.
		if !strings.HasSuffix(link, "/") {
			link = link + "/"
		}

		modules = append(modules, struct {
			Name string
			Link string
		}{
			Name: modname,
			Link: link,
		})
	}
	sort.SliceStable(modules, func(i, j int) bool {
		return modules[i].Name < modules[j].Name
	})

	var namespaces []namespace
	namespaces, members = e.gatherNamespaces(members, "")

	// Split members between resources, data sources, and others...
	var resources []*typeDocNode
	var functions []*typeDocNode
	var others []*typeDocNode
	for _, member := range members {
		if member.IsResource {
			resources = append(resources, member)
		} else if member.IsFunction {
			functions = append(functions, member)
		} else {
			others = append(others, member)
		}
	}

	hasModules := len(modules) > 0
	hasMembers := len(members) > 0
	hasNamespaces := len(namespaces) > 0
	hasResources := len(resources) > 0
	hasFunctions := len(functions) > 0

	metaDescription := "Explore "
	if root {
		metaDescription += "members of the " + linktitle + " package."
	} else {
		metaDescription += "members of the " + linktitle + " module in the " + e.pkg + " package."
	}

	// To generate the code, simply render the source Mustache template, using the right set of arguments.
	if err = indexTemplate.FRender(f, map[string]interface{}{
		"Title":                   title,
		"TitleTag":                titleTag,
		"LinkTitle":               linktitle,
		"MetaDescription":         metaDescription,
		"GitSha":                  gitSha,
		"RepoURL":                 e.repoURL,
		"Package":                 pkg,
		"PackageName":             e.pkgname,
		"PackageComment":          string(pkgcomm),
		"PackageVar":              pkgvar,
		"Files":                   files,
		"Modules":                 modules,
		"HasModules":              hasModules,
		"Members":                 members,
		"HasMembers":              hasMembers,
		"Namespaces":              namespaces,
		"HasNamespaces":           hasNamespaces,
		"Resources":               resources,
		"HasResources":            hasResources,
		"Functions":               functions,
		"HasFunctions":            hasFunctions,
		"HasResourcesOrFunctions": hasResources || hasFunctions,
		"Others":                  others,
		"HasOthers":               len(others) > 0,
	}); err != nil {
		return err
	}

	// Next up: generate all submodules underneath this one.
	for sub, module := range mod.Modules {
		if module.IsEmpty() {
			continue
		}
		if err = e.emitMarkdownModule(sub, module, gitSha, false); err != nil {
			return err
		}
	}
	return nil
}

func (e *emitter) gatherNamespaces(nodes []*typeDocNode, prefix string) ([]namespace, []*typeDocNode) {
	var namespaces []namespace
	var members []*typeDocNode
	for _, node := range nodes {
		if node.Kind == typeDocModuleNode {
			name := fmt.Sprintf("%s%s", prefix, node.Name)
			ns, mems := e.gatherNamespaces(node.Children, fmt.Sprintf("%s.", name))
			if len(mems) > 0 {
				namespaces = append(namespaces, namespace{
					Name:    name,
					Members: mems,
				})
			}
			namespaces = append(namespaces, ns...)
		} else {
			members = append(members, node)
		}
	}

	return namespaces, members
}

type namespace struct {
	Name    string
	Members []*typeDocNode
}

var resourceBaseTypes = map[string]bool{
	"Resource":          true,
	"CustomResource":    true,
	"ProviderResource":  true,
	"ComponentResource": true,
}

// isResource returns true if the node is an exported class that extends a type named `Resource`, `CustomResource`,
// `ProviderResource`, or `ComponentResource`.
func isResource(node *typeDocNode) bool {
	if node.Kind != typeDocClassNode || !node.Flags.IsExported {
		return false
	}

	if node.Name == "Resource" {
		return true
	}

	if len(node.ExtendedTypes) == 0 {
		return false
	}

	for _, t := range node.ExtendedTypes {
		if t.Type == typeDocReferenceType && resourceBaseTypes[t.Name] {
			return true
		}
	}

	return false
}

// isFunction returns true if the node is an exported function with a name that starts with lowercase "get" and has
// a `pulumi.InvokeOptions` parameter.
func isFunction(node *typeDocNode) bool {
	if node.Kind != typeDocFunctionNode || !node.Flags.IsExported || !strings.HasPrefix(node.Name, "get") ||
		len(node.Signatures) != 1 || len(node.Signatures[0].Parameters) == 0 {
		return false
	}

	// If there's a `pulumi.InvokeOptions` parameter, consider it a data source.
	for _, p := range node.Signatures[0].Parameters {
		if p.Type != nil && p.Type.Type == typeDocReferenceType && p.Type.Name == "pulumi.InvokeOptions" {
			return true
		}
	}

	return false
}

// labelSorter sorts nodes with labels alphabetically.
func labelSorter(nodes []*typeDocNode) func(i, j int) bool {
	return func(i, j int) bool {
		if nodes[i].Label != nodes[j].Label {
			return nodes[i].Label < nodes[j].Label
		}
		return nodes[i].Name < nodes[j].Name
	}
}

// transitiveSortNodes sorts an array of nodes and their children, deeply.
func transitiveSortNodes(nodes []*typeDocNode, sortByLabel bool) {
	if sortByLabel {
		// Sort the nodes themeselves by label.
		sort.SliceStable(nodes, labelSorter(nodes))
	} else {
		// Sort the nodes themselves using a case-insensitive sort.
		sort.SliceStable(nodes, func(i, j int) bool {
			return strings.ToLower(nodes[i].Name) < strings.ToLower(nodes[j].Name)
		})
	}

	// And now their children, deeply. If the node type is a class or interface, sort by label,
	// so that constructors come first, all properties are grouped together, etc.
	for _, node := range nodes {
		sortByLabel := node.Kind == typeDocClassNode || node.Kind == typeDocInterfaceNode
		transitiveSortNodes(node.Children, sortByLabel)
	}
}

// gatherModules walks a Typedoc AST and turns it into a proper module structure, to ease Markdown emission.
func (e *emitter) gatherModules(doc *typeDocNode, parentModule string) (*module, error) {
	// First gather up all modules.  Since the AST nodes may appear in arbitrary order, we need to perform this
	// pass first, before we can build up a proper tree structure with parents/children.
	mods := make(map[string]*module)
	for _, modnode := range doc.Children {
		// Skip unexported children.
		if !modnode.Flags.IsExported {
			continue
		}

		// We expect all top-level children to be modules.  (This is why `--mode file` won't work.)
		if modnode.Kind != typeDocExternalModuleNode {
			return nil, errors.Errorf("expected a module, got %s (%s)", modnode.Kind, modnode.Name)
		}

		// Simplify the module name, because we assume a simplified index-based re-export structure.  This will
		// flatten out all inner submodules to their index, so that all children will aggregate naturally.
		modname := simplifyModuleName(modnode, parentModule)

		// Skip internal tests module in k8s provider.
		if e.k8s && modname == "tests" {
			continue
		}

		// For submodules of the "types" module used in many providers, keep it in fully expanded
		// form ("types/input" instead of "types").
		if modname == "types" {
			modname = strings.Trim(modnode.Name, `"`)
			// Also skip the "types/index" which will never contain anything
			if modname == "types/index" {
				continue
			}
		}

		// Lazy init the module if appropriate.
		mod := mods[modname]
		if mod == nil {
			mod = newModule(modname)
			mods[modname] = mod
		}

		// Add all exported children from this module to the export list.
		for _, child := range modnode.Children {
			// Skip unexported children.
			isModule := child.Kind == typeDocModuleNode
			if !isModule && !child.Flags.IsExported {
				continue
			}

			name := strings.Trim(child.Name, `"`)

			// If it begins with a "./", simplify it to just the parent name.
			if isModule && strings.Index(name, "./") == 0 {
				// If this is a module, we must explode it out into the top-level modules list.
				// This may very well conflict, so we'll need to merge the new members in if so.
				nss, err := e.gatherNamespaceModules(modname, child)
				if err != nil {
					return nil, err
				}

				for nsname, ns := range nss {
					if exist, has := mods[nsname]; has {

						if err := exist.Merge(ns); err != nil {
							return nil, err
						}
					} else {
						mods[nsname] = ns
					}
				}
			} else {
				// Else, register this child as an export.
				name := child.Name
				if exist, has := mod.Exports[name]; has {
					var err error
					if child, err = exist.Merge(child); err != nil {
						return nil, err
					}
				}
				mod.Exports[name] = child
			}
		}

	}

	// Now that we've done a first pass, construct the tree structure, and return the root node.
	root := mods[rootModule]
	if root == nil {
		root = newModule(rootModule)
		mods[rootModule] = root
	}

	// Copy the names to an array and then process until empty. This allows us to add new names while iterating.
	var modnames []string
	for modname := range mods {
		modnames = append(modnames, modname)
	}
	for len(modnames) > 0 {
		// Get an item to process (the last item) and remove it.
		lastIndex := len(modnames) - 1
		modname := modnames[lastIndex]
		modnames = modnames[:lastIndex]

		if modname != rootModule {
			parname := getModuleParentName(modname)
			par := mods[parname]
			if par == nil {
				par = newModule(parname)
				mods[parname] = par
				// Add to the array for further processing.
				modnames = append(modnames, parname)
			}
			par.Modules[modname] = mods[modname]
		}
	}

	return root, nil
}

// gatherNamespaceModules returns a flat list of namespaces, recursively extracted from the tree.  The list is
// flat so that we can easily merge any duplicate entries, as namespaces can be spread across many modules.
func (e *emitter) gatherNamespaceModules(name string, node *typeDocNode) (map[string]*module, error) {
	// Start with a single module, but be prepared to append more if we find them.
	ns := newModule(name)
	nss := map[string]*module{
		name: ns,
	}

	// Find any children modules.
	for _, child := range node.Children {
		if child.Kind == typeDocModuleNode {
			submods, err := e.gatherNamespaceModules(path.Join(name, child.Name), child)
			if err != nil {
				return nil, err
			}

			for subname, submod := range submods {
				if exist, has := nss[subname]; has {
					if err := exist.Merge(submod); err != nil {
						return nil, err
					}
				} else {
					nss[subname] = submod
				}
			}
		} else {
			cn := child.Name
			if exist, has := ns.Exports[cn]; has {
				var err error
				if child, err = exist.Merge(child); err != nil {
					return nil, err
				}
			}
			ns.Exports[cn] = child
		}
	}

	return nss, nil
}

// module is an aggregate structure conceptually mapping to an ES6 module.
type module struct {
	// Name is the name of this module.
	Name string
	// Exports is a map of names to the exported member's Typedoc AST node.
	Exports map[string]*typeDocNode
	// Modules is a map of names to nested ES6 modules re-exported as a name by this module.
	Modules map[string]*module
}

func newModule(name string) *module {
	return &module{
		Name:    name,
		Exports: make(map[string]*typeDocNode),
		Modules: make(map[string]*module),
	}
}

// IsEmpty returns true if the module does not have any exports, or all of its
// submodules are empty.
func (m *module) IsEmpty() bool {
	if len(m.Exports) > 0 {
		return false
	}
	for _, module := range m.Modules {
		if !module.IsEmpty() {
			return false
		}
	}
	return true
}

// Merge another module into this one, in place, by mutating it.
func (m *module) Merge(other *module) error {
	// Now clone the other module, resolving and merging conflicts, if any arise.
	for k, exp := range other.Exports {
		if exist, has := m.Exports[k]; has {
			var err error
			if exp, err = exist.Merge(exp); err != nil {
				return err
			}
		}
		m.Exports[k] = exp
	}
	for k, mod := range other.Modules {
		if exist, has := m.Modules[k]; has {
			if err := exist.Merge(mod); err != nil {
				return err
			}
		} else {
			m.Modules[k] = mod
		}
	}

	return nil
}

// rootModule is the special name of the root index module.
const rootModule = "index"

func getModuleURL(m, pkgname string) string {
	suffix := m + "/"
	if m == rootModule {
		suffix = ""
	}
	return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/%s/%s", pkgname, suffix)
}

func getModuleFilename(m string) string {
	// Each module gets its own subdirectory and _index.md.  The package root gets a bit more metadata at the top.
	if m == rootModule {
		return "_index.md"
	}
	return filepath.Join(strings.Replace(m, "/", string(filepath.Separator), -1), "_index.md")
}

func getModuleParentName(m string) string {
	if slix := strings.IndexRune(m, '/'); slix != -1 {
		return m[:slix]
	}
	return rootModule
}

// simplifyModuleName turns a module AST's name into a simplified module name.
func simplifyModuleName(modnode *typeDocNode, parentModule string) string {
	// Remove the quotes that will always surround the name.
	name := strings.Trim(modnode.Name, `"`)

	// If it begins with a "./", simplify it to just the parent name.
	if strings.Index(name, "./") == 0 {
		return parentModule
	}

	// If the name contains a "/", then it's a sub-module, and we choose to simplify to the parent name.
	if slix := strings.LastIndex(name, "/"); slix != -1 {
		return name[:slix]
	}

	// Otherwise, there is no sub-module component, and this will belong to the parent.
	return parentModule
}

// isLocalSource returns true if this source is local to this repo. This filters out references to types or
// members that might be defined elsewhere, to avoid generating bogus links.
func isLocalSource(source typeDocSource) bool {
	return source.FileName != "" && source.FileName[0] != '/' && !strings.HasPrefix(source.FileName, "node_modules/") &&
		!strings.HasPrefix(source.FileName, "docs/node_modules/")
}

// getURLPath returns a URL path to a given type node that is relative to a given repo.
func (e *moduleEmitter) getURLPath(node *typeDocNode, parent *typeDocNode) string {
	for _, source := range node.Sources {
		if isLocalSource(source) {
			fileName := strings.TrimPrefix(source.FileName, e.e.pkgrepodir+"/")
			return fmt.Sprintf("%s#L%d", fileName, source.Line)
		}
	}

	// If not relative, try returning a link to the parent, if any. This can happen if TypeDoc binds to,
	// say, something in the standard ES library due to naming overloads (like anything named `name`).
	if parent != nil {
		return e.getURLPath(parent, nil)
	}

	// If no parent, simply return a link to the repo itself.
	return ""
}

// Merge attempts to merge two different document nodes. Only certain kinds of nodes can be merged with
// one another (generally just interface kinds). If they are unmergable, an error is returned.
func (n *typeDocNode) Merge(o *typeDocNode) (*typeDocNode, error) {
	// Check that the node types are compatible, and also select the "primary" node that will drive the
	// resulting merged node's type, tie breaking, etc. TL;DR, we prefer classes over interfaces.
	var p *typeDocNode
	var s *typeDocNode
	if n.Kind == typeDocInterfaceNode && o.Kind == typeDocInterfaceNode {
		p, s = n, o // either is fine, since they are interfaces, so choose the existing one
	} else if n.Kind == typeDocClassNode && o.Kind == typeDocInterfaceNode {
		p, s = n, o // class wins
	} else if n.Kind == typeDocInterfaceNode && o.Kind == typeDocClassNode {
		p, s = o, n // class wins
	} else if n.Kind == typeDocInterfaceNode && o.Kind == typeDocVariableNode {
		p, s = n, o // interface wins
	} else if n.Kind == typeDocTypeAliasNode && o.Kind == typeDocVariableNode {
		p, s = n, o // alias wins
	} else if n.Kind == typeDocVariableNode && o.Kind == typeDocFunctionNode {
		p, s = o, n // function wins
	} else if n.Kind == typeDocFunctionNode && o.Kind == typeDocVariableNode {
		p, s = n, o // function wins
	} else if n.Kind == typeDocFunctionNode && o.Kind == typeDocFunctionNode {
		p, s = n, o // either is fine
	} else {
		return nil, errors.Errorf(
			"cannot merge two nodes with same name '%s'; incompatible types %s and %s", n.Name, n.Kind, o.Kind)
	}

	// Mutate the existing primary node. This is done rather than creating a copy, so that we don't
	// need to worry about patching up existing pointers from parents into children, and so forth.
	p.Children = append(p.Children, s.Children...)
	p.ImplementedTypes = append(p.ImplementedTypes, s.ImplementedTypes...)
	p.Sources = append(p.Sources, s.Sources...)
	p.IndexSignatures = append(p.IndexSignatures, s.IndexSignatures...)
	p.Signatures = append(p.Signatures, s.Signatures...)

	return p, nil
}

type typeDocNodeKind string

const (
	typeDocPackageNode        typeDocNodeKind = ""
	typeDocAccessorNode       typeDocNodeKind = "Accessor"
	typeDocCallSigNode        typeDocNodeKind = "Call signature"
	typeDocClassNode          typeDocNodeKind = "Class"
	typeDocConstructorNode    typeDocNodeKind = "Constructor"
	typeDocConstructorSigNode typeDocNodeKind = "Constructor signature"
	typeDocEnumNode           typeDocNodeKind = "Enumeration"
	typeDocEnumMemberNode     typeDocNodeKind = "Enumeration member"
	typeDocExternalModuleNode typeDocNodeKind = "External module"
	typeDocFunctionNode       typeDocNodeKind = "Function"
	typeDocInterfaceNode      typeDocNodeKind = "Interface"
	typeDocMethodNode         typeDocNodeKind = "Method"
	typeDocModuleNode         typeDocNodeKind = "Module"
	typeDocObjectLiteral      typeDocNodeKind = "Object literal"
	typeDocParameterNode      typeDocNodeKind = "Parameter"
	typeDocPropertyNode       typeDocNodeKind = "Property"
	typeDocTypeAliasNode      typeDocNodeKind = "Type alias"
	typeDocTypeLiteralNode    typeDocNodeKind = "Type literal"
	typeDocVariableNode       typeDocNodeKind = "Variable"
)

func (e *moduleEmitter) createLabel(node *typeDocNode, parent *typeDocNode) string {
	switch node.Kind {
	// Create node kinds, we simply summarize.
	case typeDocAccessorNode:
		return "accessor"
	case typeDocClassNode:
		return "class"
	case typeDocConstructorNode:
		return "" // blank, the name itself is "constructor"
	case typeDocEnumNode:
		return "enum"
	case typeDocFunctionNode:
		return "function"
	case typeDocInterfaceNode:
		return "interface"
	case typeDocMethodNode:
		return "method"
	case typeDocExternalModuleNode:
		return "module"
	case typeDocModuleNode:
		return "namespace"
	case typeDocPackageNode:
		return "package"
	case typeDocParameterNode:
		return "parameter"
	case typeDocPropertyNode:
		return "property"
	case typeDocTypeAliasNode:
		return "type"
	case typeDocEnumMemberNode:
		return "enum member"
	case typeDocVariableNode, typeDocObjectLiteral:
		if node.Flags.IsConst {
			return "const"
		}
		return "let"

	// For others, we will generate a full signature.
	case typeDocCallSigNode, typeDocConstructorSigNode:
		return e.createSignature(node, parent, false)

	// If we don't recognize this node, fail.
	default:
		log.Fatalf("unrecognized node kind: %v (%v)", node.Kind, node.Name)
		return ""
	}
}

func (e *moduleEmitter) createSignature(node *typeDocNode, parent *typeDocNode, arrow bool) string {
	var label string

	// If not an arrow function (anonymous), add the name/type params/etc.
	if !arrow {
		if parent != nil {
			label += createVisibilityLabel(parent.Flags)
		}

		if strings.Index(node.Name, "new ") == 0 {
			label += fmt.Sprintf("<span class='kd'>new</span> %s", node.Name[4:])
		} else {
			label += node.Name
		}

		// If there are generic type arguments, add them now.
		if len(node.TypeParameter) > 0 {
			label += "&lt;"
			for i, typaram := range node.TypeParameter {
				if i > 0 {
					label += ","
				}
				label += typaram.Name
			}
			label += "&gt;"
		}
	}

	// Add the parameters.
	label += "("
	for i, param := range node.Parameters {
		if i > 0 {
			label += ", "
		}
		label += param.Name
		if param.Flags.IsOptional {
			label += "?"
		}
		if paramType := e.createTypeLabel(param.Type, 0); paramType != "" {
			label += ": " + paramType
		}
	}
	label += ")"

	// Add a return type, if any.
	if node.Kind != typeDocConstructorSigNode {
		returnType := e.createTypeLabel(node.Type, 0)
		if returnType != "" {
			if arrow {
				label += " => " + returnType
			} else {
				label += ": " + returnType
			}
		} else if arrow {
			label += " => void"
		}
	}

	return label
}

func (e *moduleEmitter) createCodeDetails(node *typeDocNode) string {
	switch node.Kind {
	case typeDocTypeAliasNode:
		// For type aliases, we won't have signatures, so we will create a detailed label.
		return fmt.Sprintf("<span class='kd'>type</span> %s = %s;", node.Name, e.createTypeLabel(node.Type, 0))
	case typeDocPropertyNode:
		label := createVisibilityLabel(node.Flags)
		label += node.Name
		if node.Flags.IsOptional {
			label += "?"
		}
		if proptyp := e.createTypeLabel(node.Type, 0); proptyp != "" {
			label += ": " + proptyp
		}
		if node.DefaultValue != nil {
			label += " = " + html.EscapeString(*node.DefaultValue)
		}
		return label + ";"
	case typeDocVariableNode:
		var label string
		if node.Flags.IsConst {
			label += "<span class='kd'>const</span> "
		} else {
			label += "<span class='kd'>let</span> "
		}
		label += node.Name
		if vartyp := e.createTypeLabel(node.Type, 0); vartyp != "" {
			label += ": " + vartyp
		}
		if node.DefaultValue != nil {
			label += " = <span class='s2'>" + html.EscapeString(*node.DefaultValue) + "</span>"
		}
		return label + ";"

	case typeDocClassNode, typeDocInterfaceNode:
		label := fmt.Sprintf("<span class='kr'>%s</span> <span class='nx'>%s</span>",
			e.createLabel(node, nil), node.Name)

		// If this extends or implements other types, render them.
		if len(node.ExtendedTypes) > 0 {
			label += " <span class='kr'>extends</span> "
			for i, ext := range node.ExtendedTypes {
				if i > 0 {
					label += ", "
				}
				label += e.createTypeLabel(ext, 0)
			}
		}
		if len(node.ImplementedTypes) > 0 {
			label = " <span class='kr'>implements</span> "
			for i, impl := range node.ImplementedTypes {
				if i > 0 {
					label += ", "
				}
				label += e.createTypeLabel(impl, 0)
			}
		}
		return label

	case typeDocAccessorNode:
		label := createVisibilityLabel(node.Flags)
		if len(node.GetSignatures) > 0 {
			label += fmt.Sprintf("<span class='kd'>get</span> %s()", node.Name)
			if typ := e.createTypeLabel(node.GetSignatures[0].Type, 0); typ != "" {
				label += ": " + typ
			}
		} else {
			label += node.Name
		}
		return label + ";"

	default:
		return ""
	}
}

func (e *moduleEmitter) typeHyperlinkInModule(mod *module, t *typeDocType) string {
	// First look in each exported member.
	for _, member := range mod.Exports {
		if url := e.typeHyperlinkInNode(mod, member, t); url != "" {
			return url
		}
	}
	// Next look in each submodule.
	for _, subMod := range mod.Modules {
		if url := e.typeHyperlinkInModule(subMod, t); url != "" {
			return url
		}
	}
	return ""
}

func (e *moduleEmitter) typeHyperlinkInNode(mod *module, node *typeDocNode, t *typeDocType) string {
	// If we found the type, return the link.
	if node.ID == t.ID {
		return fmt.Sprintf("%s#%s", getModuleURL(mod.Name, e.e.pkgname), t.Name)
	}
	// Otherwise, deeply check the node's children.
	for _, n := range node.Children {
		if url := e.typeHyperlinkInNode(mod, n, t); url != "" {
			return url
		}
	}
	return ""
}

// @pulumi/awsx imports types within the same modules using the following.
// We'll use this mapping to map the local import to the actual top-level exported module.
var awsxImportModuleMap = map[string]string{
	"ecs.": "ecs",
	"mod.": "lb",
}

// typeHyperlink returns the hyperlink for help text associated with a given type, if available.
func (e *moduleEmitter) typeHyperlink(t *typeDocType) string {
	// Add a hyperlink for the type if possible.
	if t.Type == typeDocIntrinsicType {
		// If an intrinsic type, hyperlink to the standard JavaScript docs.
		switch t.Name {
		// Standard JavaScript types.
		case "boolean":
			return "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean"
		case "number":
			return "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number"
		case "object":
			return "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object"
		case "string":
			return "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String"
		case "undefined":
			return "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined"

		// TypeScript-specific types.
		case "any":
			return "https://www.typescriptlang.org/docs/handbook/basic-types.html#any"
		case "never":
			return "https://www.typescriptlang.org/docs/handbook/basic-types.html#never"
		case "void":
			return "https://www.typescriptlang.org/docs/handbook/basic-types.html#void"
		}
	} else if t.Type == typeDocReferenceType {
		// If this is a reference type in this package, link to it.
		if t.ID != 0 {
			// First look for it in this module.
			for _, member := range e.mod.Exports {
				if member.ID == t.ID {
					return fmt.Sprintf("#%s", t.Name)
				}
			}
			// Next look in other modules.
			url := e.typeHyperlinkInModule(e.e.root, t)
			if url == fmt.Sprintf("%s#%s", getModuleURL(e.mod.Name, e.e.pkgname), t.Name) {
				// If the URL ends up being the same as for the current module, just return the
				// anchor link directly.
				return fmt.Sprintf("#%s", t.Name)
			}
			return url
		}

		// For certain well-known types, we'll hard-code links to them.
		// TODO: it's unfortunate we need to do this, but TypeDoc doesn't encode inter-package references.
		switch t.Name {
		case "Array", "Error", "Map", "Promise", "Set":
			return fmt.Sprintf(
				"https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/%s", t.Name)
		case "Archive", "Asset", "AssetMap", "AssetArchive",
			"FileArchive", "FileAsset", "RemoteArchive", "RemoteAsset", "StringAsset":
			return fmt.Sprintf(
				"/docs/reference/pkg/nodejs/pulumi/pulumi/asset/#%s", t.Name)
		case "ComponentResource", "ComponentResourceOptions", "CustomResource", "CustomResourceOptions",
			"ID", "Input", "Inputs", "InvokeOptions", "Output", "OutputInstance", "Outputs", "Resource", "ResourceOptions", "URN",
			"ProviderResource":
			return fmt.Sprintf(
				"/docs/reference/pkg/nodejs/pulumi/pulumi/#%s", t.Name)
		}

		if e.e.pkgname == "awsx" {
			for prefix, module := range awsxImportModuleMap {
				if strings.HasPrefix(t.Name, prefix) {
					name := strings.TrimPrefix(t.Name, prefix)
					return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/awsx/%s/#%s", module, name)
				}
			}

			var mod string
			switch t.Name {
			case "Tags":
				return "/docs/reference/pkg/nodejs/pulumi/aws/#Tags"
			case "RestApiEndpointConfiguration", "StageAccessLogSettings":
				return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/aws/types/input/#%s", t.Name)
			case "Deployment", "RestApi", "Stage":
				mod = "apigateway"
			case "Group", "Policy":
				mod = "autoscaling"
			case "Stack":
				mod = "cloudformation"
			case "MetricAlarm":
				mod = "cloudwatch"
			case "Instance", "LaunchConfiguration", "Route", "RouteTable", "RouteTableAssociation", "SecurityGroup",
				"SecurityGroupRule", "Subnet", "Vpc":
				mod = "ec2"
			case "LifecyclePolicy", "Repository":
				mod = "ecr"
			case "Cluster", "HealthCheck", "HostEntry", "LinuxParameters", "LogConfiguration", "MountPoint",
				"PortMapping", "RepositoryCredentials", "ResourceRequirements", "Secret", "Service", "SystemControl",
				"TaskDefinition", "Ulimit", "VolumeFrom":
				mod = "ecs"
			case "InstanceProfile", "PolicyDocument", "Role":
				mod = "iam"
			case "Function":
				mod = "lambda"
			case "Listener", "LoadBalancer", "TargetGroup", "TargetGroupAttachment":
				mod = "lb"
			case "Bucket", "BucketArgs":
				mod = "s3"
			case "Topic":
				mod = "sns"
			}
			if mod != "" {
				return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/aws/%s/#%s", mod, t.Name)
			}
		} else if e.e.pkgname == "eks" {
			var mod string
			switch t.Name {
			case "FargateProfileSelector", "NodeGroupScalingConfig":
				return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/aws/types/input/#%s", t.Name)
			case "Stack":
				mod = "cloudformation"
			case "SecurityGroup", "SecurityGroupRule":
				mod = "ec2"
			case "Cluster", "NodeGroup", "NodeGroupArgs":
				mod = "eks"
			case "Role":
				mod = "iam"
			}
			if mod != "" {
				return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/aws/%s/#%s", mod, t.Name)
			}

			switch t.Name {
			case "ObjectMeta":
				return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/kubernetes/types/input/#%s", t.Name)
			case "Provider":
				return "/docs/reference/pkg/nodejs/pulumi/kubernetes/#Provider"
			case "StorageClass":
				mod = "storage/v1"
			}
			if mod != "" {
				return fmt.Sprintf("/docs/reference/pkg/nodejs/pulumi/kubernetes/%s/#%s", mod, t.Name)
			}
		}

		// If this is a qualified name, see if it refers to the Pulumi SDK. If so, generate a link.
		elements := strings.Split(t.Name, ".")
		var link string
		if len(elements) > 1 {
			if elements[0] == "pulumi" {
				link = "/docs/reference/pkg/nodejs/pulumi/pulumi/"
			} else if e.e.pkgname == "awsx" && elements[0] == "aws" {
				link = "/docs/reference/pkg/nodejs/pulumi/aws/"
			} else if e.e.pkgname == "awsx" && (elements[0] == "x" || elements[0] == "awsx") {
				link = "/docs/reference/pkg/nodejs/pulumi/awsx/"
			} else if elements[0] == "inputs" || elements[0] == "inputApi" {
				link = "/docs/reference/pkg/nodejs/pulumi/" + e.e.pkgname + "/types/input/"
				// Strip out everything except first and last element.  This is necessary given
				// the current structure of docs, but leads to losing precision on which member
				// we are really trying to link to, as there may be multiple instances of the
				// label on this page.  Eventually, we need to improve the doc generator to
				// separate out these individual sub-namespaces into their own pages or to
				// enrichen the link format to that we can link more precisely.
				elements = append(elements[:1], elements[len(elements)-1])
			} else if elements[0] == "outputs" || elements[0] == "outputApi" {
				link = "/docs/reference/pkg/nodejs/pulumi/" + e.e.pkgname + "/types/output/"
				// Strip out everything except first and last element.  This is necessary given
				// the current structure of docs, but leads to losing precision on which member
				// we are really trying to link to, as there may be multiple instances of the
				// label on this page.  Eventually, we need to improve the doc generator to
				// separate out these individual sub-namespaces into their own pages or to
				// enrichen the link format to that we can link more precisely.
				elements = append(elements[:1], elements[len(elements)-1])
			}
		}
		if link != "" {
			for i := 1; i < len(elements)-1; i++ {
				link += fmt.Sprintf("%s/", elements[i])
			}
			return link + fmt.Sprintf("#%s", elements[len(elements)-1])
		}
	}

	return ""
}

func (e *moduleEmitter) createTypeLabel(t *typeDocType, indent int) string {
	switch t.Type {
	case typeDocArrayType:
		return fmt.Sprintf("%s[]", e.createTypeLabel(t.ElementType, indent))
	case typeDocIntrinsicType, typeDocParameterType, typeDocReferenceType, typeDocUnknownType:
		// Add a hyperlink for the type if possible.
		var label string
		if hyperlink := e.typeHyperlink(t); hyperlink != "" {
			label += fmt.Sprintf("<a href='%s'>%s</a>", hyperlink, t.Name)
		} else {
			label += t.Name
		}

		// If it's a reference type named `__type`, it's an empty type literal.
		if t.Type == typeDocReferenceType && label == "__type" {
			label = "{ }"
		}

		if t.Type == typeDocIntrinsicType {
			label = fmt.Sprintf("<span class='kd'>%s</span>", label)
		}

		// If there are type args, add them now.
		if len(t.TypeArguments) > 0 {
			label += "&lt;"
			for i, tyarg := range t.TypeArguments {
				if i > 0 {
					label += ", "
				}
				label += e.createTypeLabel(tyarg, indent)
			}
			label += "&gt;"
		}
		return label
	case typeDocReflectionType:
		// Either a type literal or a function type.
		decl := t.Declaration
		if len(decl.Signatures) > 0 {
			return e.createSignature(decl.Signatures[0], nil, true)
		} else if len(decl.Children) > 0 {
			label := "{\n"
			indent++
			for _, child := range decl.Children {
				if child.Kind == typeDocFunctionNode && len(child.Signatures) > 0 {
					label += fmt.Sprintf("%s%s;\n",
						strings.Repeat(" ", indent*4), e.createSignature(child.Signatures[0], decl, false))
				} else {
					var childType string
					if child.Type != nil {
						childType = e.createTypeLabel(child.Type, indent)
					}
					name := child.Name
					if child.Flags.IsOptional {
						name += "?"
					}
					label += fmt.Sprintf("%s%s: %s;\n",
						strings.Repeat(" ", indent*4), name, childType)
				}
			}
			indent--
			return fmt.Sprintf("%s%s}", label, strings.Repeat(" ", indent*4))
		} else if len(decl.IndexSignatures) == 1 {
			index := decl.IndexSignatures[0]
			if len(index.Parameters) == 1 {
				return fmt.Sprintf("{[%s: %s]: %s}",
					index.Parameters[0].Name,
					e.createTypeLabel(index.Parameters[0].Type, indent),
					e.createTypeLabel(index.Type, indent))
			}
			return "{ ... }"
		} else {
			return "{ ... }"
		}
	case typeDocStringLiteralType:
		return fmt.Sprintf(`<span class='s2'>"%s"</span>`, t.Value)
	case typeDocTupleType:
		label := "["
		for i, elem := range t.Elements {
			if i >= 0 {
				label += ", "
			}
			label += e.createTypeLabel(elem, indent)
		}
		return label + "]"
	case typeDocUnionType:
		var label string
		for i, inner := range t.Types {
			if i > 0 {
				label += " | "
			}
			label += e.createTypeLabel(inner, indent)
		}
		return label
	case typeDocIntersectionType:
		var label string
		for i, inner := range t.Types {
			if i > 0 {
				label += " &amp; "
			}
			label += e.createTypeLabel(inner, indent)
		}
		return label
	case typeDocTypeOperatorType:
		targetStr := e.createTypeLabel(t.Target, indent)
		return fmt.Sprintf("%s %s", t.Operator, targetStr)
	case typeDocPredicateType:
		if t.TargetType != nil && t.TargetType.Type == typeDocReferenceType {
			targetStr := e.createTypeLabel(t.TargetType, indent)
			return fmt.Sprintf("%s is %s", t.Name, targetStr)
		}
		// Otherwise, fall back to returning boolean.
		return e.createTypeLabel(&typeDocType{Type: typeDocIntrinsicType, Name: "boolean"}, indent)
	default:
		log.Fatalf("unrecognized type node type: %v\n", t.Type)
		return ""
	}
}

func createVisibilityLabel(flags typeDocFlags) string {
	var label string
	if flags.IsPublic {
		label += "public "
	} else if flags.IsPrivate {
		label += "private "
	} else if flags.IsProtected {
		label += "protected "
	}
	if flags.IsStatic {
		label += "static "
	}
	return fmt.Sprintf("<span class='kd'>%s</span>", label)
}

// typeDoc represents a JSON serialized structure that has been output from the `typedoc` program.  I'm sure we are
// unintentionally sensitive to particular flags, so for reference, we are generally parsing things of the form
//
//     $ tsdoc --json docs.json --mode modules --includeDeclarations
//
// In particular, passing --mode file will not lead to the correct behavior, due to the way we use module structure.
type typeDocNode struct {
	ID int `json:"id,omitempty"`
	// Name is the package name that this documentation refers to.
	Name string `json:"name,omitempty"`
	// KindString is the string-based kind of this node.
	Kind typeDocNodeKind `json:"kindString,omitempty"`
	// Flags contains a bunch of flags pertaining to this node.
	Flags typeDocFlags `json:"flags,omitempty"`
	// Type is the type of this member, when appropriate.
	Type *typeDocType `json:"type,omitempty"`
	// Comment is a JSDoc comment extracted via Typedoc.
	Comment typeDocComment `json:"comment,omitempty"`
	// DefaultValue is an optional default value for this entry (or nil if none).
	DefaultValue *string `json:"defaultValue,omitempty"`
	// GetSignatures is a list of get signature nodes for this node, when an Accessor.
	GetSignatures []*typeDocNode `json:"getSignature,omitempty"`
	// IndexSignature is used to represent indexed types (e.g., `{[key: string]: any}`).
	IndexSignatures []*typeDocNode `json:"indexSignature,omitempty"`
	// Children is a list of one or more child members of this node.
	Children []*typeDocNode `json:"children,omitempty"`
	// TypeParameter includes all the type parameters for this node.
	TypeParameter []*typeDocNode `json:"typeParameter,omitempty"`
	// Parameters is a list of parameter nodes for this node, when a Call signature.
	Parameters []*typeDocNode `json:"parameters,omitempty"`
	// Signatures is a list of signature nodes for this node, when a Method.
	Signatures []*typeDocNode `json:"signatures,omitempty"`
	// ExtendedBy is a cross-reference to all the other artifacts that extend this one.
	ExtendedBy []*typeDocType `json:"extendedBy,omitempty"`
	// ExtendedTypes is a list of other types extended by this one.
	ExtendedTypes []*typeDocType `json:"extendedTypes,omitempty"`
	// ImplementedTypes is a list of other types implemented by this one.
	ImplementedTypes []*typeDocType `json:"implementedTypes,omitempty"`
	// Sources represents the source files from which this node came.
	Sources []typeDocSource `json:"sources,omitempty"`

	// AnchorName is the qualified name of a member, for purposes of generating anchors.
	AnchorName string
	// Label is not stored in the file, it's a label generated by doing a pass over the AST. For members, this is
	// simply the node's "kind" to print in the docs (`class`, `function`, etc), and for signatures it's a more
	// detailed expansion of the full signature (including the name).
	Label string
	// CodeDetails is used when a code-styled header is available to print before the details of a member.
	CodeDetails string
	// URLPath is the path to this member in the relevant Git repi.  It's augmented information.
	URLPath string
	// IsResource is true if the node represents a Pulumi resource.
	IsResource bool
	// IsFunction is true if the node represents a Pulumi function.
	IsFunction bool
	// IsDeprecated is true if the node has "deprecated" comment tag.
	IsDeprecated bool
	// The text fo the deprecated comment tag.
	DeprecatedMessage string
}

type typeDocFlags struct {
	IsConst     bool `json:"isConst,omitempty"`
	IsOptional  bool `json:"isOptional,omitempty"`
	IsPublic    bool `json:"isPublic,omitempty"`
	IsProtected bool `json:"isProtected,omitempty"`
	IsPrivate   bool `json:"isPrivate,omitempty"`
	IsExported  bool `json:"isExported,omitempty"`
	IsStatic    bool `json:"isStatic,omitempty"`
}

type typeDocType struct {
	// Id is a reference identifier for intra-package type references.
	ID int `json:"id,omitempty"`
	// Type is the type of the type.
	Type typeDocTypeType `json:"type,omitempty"`
	// Name is the name of the type.
	Name string `json:"name,omitempty"`
	// Elements contains the element type for tuples.
	Elements []*typeDocType `json:"elements,omitempty"`
	// ElementType contains the element type for arrays.
	ElementType *typeDocType `json:"elementType,omitempty"`
	// TypeArguments is an optional list of instantiated type args.
	TypeArguments []*typeDocType `json:"typeArguments,omitempty"`
	// Types contains the constituent parts of complex types, like unions.
	Types []*typeDocType `json:"types,omitempty"`
	// Value is the actual value for literal types.
	Value string `json:"value,omitempty"`
	// Declaration is used for reflection-style type literals.
	Declaration *typeDocNode `json:"declaration,omitempty"`
	// Operator is the type operator used, if this is a type operator reference
	Operator string `json:"operator,omitempty"`
	// Target is the target of the type operator, if this is a type operator reference
	Target *typeDocType `json:"target,omitempty"`
	// TargetType is the target type of a predicate, if this is a predicate.
	TargetType *typeDocType `json:"targetType,omitempty"`
}

type typeDocTypeType string

const (
	typeDocArrayType         typeDocTypeType = "array"
	typeDocIntrinsicType     typeDocTypeType = "intrinsic"
	typeDocIntersectionType  typeDocTypeType = "intersection"
	typeDocPredicateType     typeDocTypeType = "predicate"
	typeDocParameterType     typeDocTypeType = "typeParameter"
	typeDocReferenceType     typeDocTypeType = "reference"
	typeDocReflectionType    typeDocTypeType = "reflection"
	typeDocStringLiteralType typeDocTypeType = "stringLiteral"
	typeDocTupleType         typeDocTypeType = "tuple"
	typeDocUnionType         typeDocTypeType = "union"
	typeDocUnknownType       typeDocTypeType = "unknown"
	typeDocTypeOperatorType  typeDocTypeType = "typeOperator"
)

type typeDocComment struct {
	// ShortText is the brief JSDoc comment attached to the artifact in question.
	ShortText string `json:"shortText,omitempty"`
	// Text is a more detailed JSDoc comment attached to the artifact in question.
	Text string       `json:"text,omitempty"`
	Tags []typeDocTag `json:"tags,omitempty"`
}

type typeDocTag struct {
	Tag  string `json:"tag,omitempty"`
	Text string `json:"text,omitempty"`
}

type typeDocSource struct {
	// FileName is the file containing the definition for this artifact.
	FileName string `json:"fileName,omitempty"`
	// Line is the line at which this artifact definition begins.
	Line int `json:"line,omitempty"`
	// Character is the character on the line at which this artifact definition begins.
	Character int `json:"character,omitempty"`
}
