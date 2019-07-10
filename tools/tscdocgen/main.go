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
	"sort"
	"strings"
	"unicode"

	"github.com/pkg/errors"
)

func main() {
	// Grab the args.
	flag.Parse()
	args := flag.Args()
	if len(args) < 3 {
		fmt.Fprintf(os.Stderr, "error: usage: %s <src-dir> <doc-file> <out-dir> <git-hash>\n", os.Args[0])
		os.Exit(1)
	}

	// Load and parse the document.
	doc, err := loadAndParseDoc(args[1])
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: reading and parsing docs file: %v\n", err)
		os.Exit(1)
	}

	// Assuming that succeeded, simply emit the Markdown docs now.
	if err = emitMarkdownDocs(args[0], doc, args[2], args[3]); err != nil {
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

	node.IndexSignatures = filterOutInternalNodeArray(node.IndexSignatures)
	node.Children = filterOutInternalNodeArray(node.Children)
	node.TypeParameter = filterOutInternalNodeArray(node.TypeParameter)
	node.Parameters = filterOutInternalNodeArray(node.Parameters)
	node.Signatures = filterOutInternalNodeArray(node.Signatures)
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
		if hasInternalTag(val) {
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

func hasInternalTag(node *typeDocNode) bool {
	for _, tag := range node.Comment.Tags {
		if tag.Tag == "internal" {
			return true
		}
	}

	return false
}

// gitHubBaseURLs is a *hackhackhack* hard-coded list of URLs for our packages.
// TODO(joe): base this off the package.json file.
var gitHubBaseURLs = map[string]string{
	"@pulumi/pulumi":       "https://github.com/pulumi/pulumi/blob/{githash}/sdk/nodejs",
	"@pulumi/aws":          "https://github.com/pulumi/pulumi-aws/blob/{githash}/sdk/nodejs",
	"@pulumi/awsx":         "https://github.com/pulumi/pulumi-awsx/blob/{githash}/nodejs/awsx",
	"@pulumi/azure":        "https://github.com/pulumi/pulumi-azure/blob/{githash}/sdk/nodejs",
	"@pulumi/azuread":      "https://github.com/pulumi/pulumi-azuread/blob/{githash}/sdk/nodejs",
	"@pulumi/cloud":        "https://github.com/pulumi/pulumi-cloud/blob/{githash}/api",
	"@pulumi/cloudflare":   "https://github.com/pulumi/pulumi-cloudflare/blob/{githash}/sdk/nodejs",
	"@pulumi/datadog":      "https://github.com/pulumi/pulumi-datadog/blob/{githash}/sdk/nodejs",
	"@pulumi/digitalocean": "https://github.com/pulumi/pulumi-digitalocean/blob/{githash}/sdk/nodejs",
	"@pulumi/dnsimple":     "https://github.com/pulumi/pulumi-dnsimple/blob/{githash}/sdk/nodejs",
	"@pulumi/docker":       "https://github.com/pulumi/pulumi-docker/blob/{githash}/sdk/nodejs",
	"@pulumi/eks":          "https://github.com/pulumi/pulumi-eks/blob/{githash}/nodejs/eks",
	"@pulumi/f5bigip":      "https://github.com/pulumi/pulumi-f5bigip/blob/{githash}/sdk/nodejs",
	"@pulumi/gcp":          "https://github.com/pulumi/pulumi-gcp/blob/{githash}/sdk/nodejs",
	"@pulumi/gitlab":       "https://github.com/pulumi/pulumi-gitlab/blob/{githash}/sdk/nodejs",
	"@pulumi/kubernetes":   "https://github.com/pulumi/pulumi-kubernetes/blob/{githash}/sdk/nodejs",
	"@pulumi/linode":       "https://github.com/pulumi/pulumi-linode/blob/{githash}/sdk/nodejs",
	"@pulumi/mysql":        "https://github.com/pulumi/pulumi-mysql/blob/{githash}/sdk/nodejs",
	"@pulumi/newrelic":     "https://github.com/pulumi/pulumi-newrelic/blob/{githash}/sdk/nodejs",
	"@pulumi/openstack":    "https://github.com/pulumi/pulumi-openstack/blob/{githash}/sdk/nodejs",
	"@pulumi/packet":       "https://github.com/pulumi/pulumi-packet/blob/{githash}/sdk/nodejs",
	"@pulumi/random":       "https://github.com/pulumi/pulumi-random/blob/{githash}/sdk/nodejs",
	"@pulumi/terraform":    "https://github.com/pulumi/pulumi-terraform/blob/{githash}/sdk/nodejs",
	"@pulumi/tls":    		"https://github.com/pulumi/pulumi-tls/blob/{githash}/sdk/nodejs",
	"@pulumi/vsphere":      "https://github.com/pulumi/pulumi-vsphere/blob/{githash}/sdk/nodejs",
}

// emitMarkdownDocs takes as input a full Typedoc AST, transforms it into Markdown suitable for our documentation
// website, and emits those files into the target directory.  If the target doesn't exist, it will be created.
func emitMarkdownDocs(srcdir string, doc *typeDocNode, outdir, githash string) error {
	// First, gather up the entries by module.  Note that we are doing something dubious here to make our docs
	// easier to use and navigate than the default ones that Typedoc generates.  We are assuming an idiomatic module
	// structure with top-level index-style exports for each submodule.  In the general case, this isn't always true,
	// and we may generate (a) incorrect documentation by showing something that isn't truly exported and (b) omit
	// important details about the specific inner modules that truly contain the members in question.  I'm sure we'll
	// want to revisit this and make the logic here more sophisticated and general purpose someday.
	pkg := doc.Name
	repoURL := strings.Replace(gitHubBaseURLs[pkg], "{githash}", githash, -1)
	e := newEmitter(pkg, srcdir, repoURL, outdir)

	// The kubernetes package requires some special handling since the structure differs from
	// the tf-generated providers.
	k8s := false
	if pkg == "@pulumi/kubernetes" {
		k8s = true
	}
	root, err := e.gatherModules(doc, rootModule, k8s)
	if err != nil {
		return err
	}
	e.augmentNode(doc, nil)
	return e.emitMarkdownModule(rootModule, root, true)
}

type emitter struct {
	pkg     string // the NPM package name.
	srcdir  string // the source directory for docs, etc.
	repoURL string // the base repo URL for this package's code.
	outdir  string // where to store the output files.
}

func newEmitter(pkg, srcdir, repoURL, outdir string) *emitter {
	return &emitter{
		pkg:     pkg,
		srcdir:  srcdir,
		repoURL: repoURL,
		outdir:  outdir,
	}
}

// augmentNode recurses throughout a tree AST, adding information that we'll need when translating it to Markdown.
func (e *emitter) augmentNode(node *typeDocNode, parent *typeDocNode) {
	// Add some labels.
	node.AnchorName = node.Name
	if parent != nil && (parent.Kind == typeDocClassNode || parent.Kind == typeDocInterfaceNode) {
		node.AnchorName = fmt.Sprintf("%s-%s", parent.Name, node.AnchorName)
	}
	node.Label = createLabel(node, parent)
	node.CodeDetails = createCodeDetails(node)
	node.RepoURL = getRepoURL(e.repoURL, node, parent)

	// If this extends or implements other types, render them.
	if len(node.ExtendedTypes) > 0 {
		node.Extends = "<span class='kd'>extends</span> "
		for i, ext := range node.ExtendedTypes {
			if i > 0 {
				node.Extends += ", "
			}
			node.Extends += createTypeLabel(ext, 0)
		}
	}
	if len(node.ImplementedTypes) > 0 {
		node.Implements = "<span class='kd'>implements</span> "
		for i, impl := range node.ImplementedTypes {
			if i > 0 {
				node.Implements += ", "
			}
			node.Implements += createTypeLabel(impl, 0)
		}
	}

	// Augment everything deeply.
	for _, child := range node.Children {
		e.augmentNode(child, node)
	}
	for _, sig := range node.Signatures {
		e.augmentNode(sig, node)
	}
	for _, param := range node.Parameters {
		e.augmentNode(param, node)
	}

	// Reorder children based on their labels.
	sort.Slice(node.Children, func(i, j int) bool {
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
func (e *emitter) emitMarkdownModule(name string, mod *module, root bool) error {
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
	var pkg string
	var pkgvar string
	var readme string
	var breadcrumbs []string

	if root {
		title = fmt.Sprintf("Package %s", e.pkg)
		pkg = e.pkg
		pkgvar = camelCase(e.pkg[strings.IndexRune(e.pkg, '/')+1:])
		readme = filepath.Join(e.srcdir, "README.md")
	} else {
		title = fmt.Sprintf("Module %s", name)
		readme = filepath.Join(e.srcdir, name, "README.md")

		// Create the breadcrumb links (in LIFO order).  First, add the current module name.
		var simplename string
		if slix := strings.IndexRune(name, '/'); slix != -1 {
			simplename = name[slix+1:]
		} else {
			simplename = name
		}
		breadcrumbs = append(breadcrumbs, simplename)

		// Now split the parent and walk it in reverse, prepending all of the parent links.
		parts := strings.Split(getModuleParentName(name), "/")
		crumbs := ".."
		for i := len(parts) - 1; i >= 0; i-- {
			name := parts[i]
			if i == 0 && name == rootModule {
				// we will add the root after this loop, no need to be redundant.
				break
			}

			breadcrumbs = append(
				[]string{fmt.Sprintf("<a href=\"%s/\">%s</a> &gt; ", crumbs, name)},
				breadcrumbs...)
			if crumbs != "" {
				crumbs += string(filepath.Separator)
			}
			crumbs += ".."
		}

		// Finally, add the link to the root module.
		breadcrumbs = append(
			[]string{fmt.Sprintf("<a href=\"%s/\">%s</a> &gt; ", crumbs, e.pkg)},
			breadcrumbs...)
	}

	// See if there is a README.md file and, if so, include it as the package's comment.
	pkgcomm, err := ioutil.ReadFile(readme)
	if err != nil && !os.IsNotExist(err) {
		return err
	}

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

		members = append(members, member)
	}

	// Ensure the files, members, and children (deeply throughout the tree) are sorted deterministically.
	sort.Strings(files)
	transitiveSortByLabels(members)

	// Get any submodules, make relative links, and ensure they are also sorted in a deterministic order.
	var modules []struct {
		Name string
		Link string
	}
	for modname := range mod.Modules {
		var link string
		prefix := name + "/"
		if nix := strings.Index(modname, prefix); nix != -1 {
			link = modname[len(prefix):]
		} else {
			link = modname
		}
		modules = append(modules, struct {
			Name string
			Link string
		}{
			Name: modname,
			Link: link,
		})
	}
	sort.Slice(modules, func(i, j int) bool {
		return modules[i].Name < modules[j].Name
	})

	// To generate the code, simply render the source Mustache template, using the right set of arguments.
	if err = indexTemplate.FRender(f, map[string]interface{}{
		"Title":          title,
		"Breadcrumbs":    breadcrumbs,
		"RepoURL":        e.repoURL,
		"Package":        pkg,
		"PackageComment": string(pkgcomm),
		"PackageVar":     pkgvar,
		"Files":          files,
		"Modules":        modules,
		"HasModules":     len(modules) > 0,
		"Members":        members,
		"HasMembers":     len(members) > 0,
	}); err != nil {
		return err
	}

	// Next up: generate all submodules underneath this one.
	for sub, module := range mod.Modules {
		if err = e.emitMarkdownModule(sub, module, false); err != nil {
			return err
		}
	}
	return nil
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

// transitiveSortByLabels sorts an array of nodes and their children, deeply.
func transitiveSortByLabels(nodes []*typeDocNode) {
	// First sort the nodes themselves.
	sort.SliceStable(nodes, labelSorter(nodes))

	// And now their children, deeply. Note that we use a stable sort because some children don't have labels.
	for _, node := range nodes {
		transitiveSortByLabels(node.Children)
	}
}

// gatherModules walks a Typedoc AST and turns it into a proper module structure, to ease Markdown emission.
func (e *emitter) gatherModules(doc *typeDocNode, parentModule string, k8s bool) (*module, error) {
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
		if k8s && modname == "tests" {
			continue
		}
		// k8s provider has common types files which are imported into multiple modules.
		// TODO(levi): Split the input/output types into the same directory structure, and remove this skip.
		if k8s && modname == "types" {
			continue
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
	for modname, mod := range mods {
		if modname != rootModule {
			parname := getModuleParentName(modname)
			par := mods[parname]
			if par == nil {
				par = newModule(parname)
				mods[parname] = par
			}
			par.Modules[modname] = mod
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
	return source.FileName != "" && source.FileName[0] != '/'
}

// getRepoURL returns a hyperlink to a given type node that is relative to a given repo.
func getRepoURL(baseURL string, node *typeDocNode, parent *typeDocNode) string {
	for _, source := range node.Sources {
		if isLocalSource(source) {
			return fmt.Sprintf("%s/%s#L%d", baseURL, source.FileName, source.Line)
		}
	}

	// If not relative, try returning a link to the parent, if any. This can happen if TypeDoc binds to,
	// say, something in the standard ES library due to naming overloads (like anything named `name`).
	if parent != nil {
		return getRepoURL(baseURL, parent, nil)
	}

	// If no parent, simply return a link to the repo itself.
	return baseURL
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

func createLabel(node *typeDocNode, parent *typeDocNode) string {
	switch node.Kind {
	// Create node kinds, we simply summarize.
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
	case typeDocExternalModuleNode, typeDocModuleNode:
		return "module"
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
		} else {
			return "let"
		}

	// For others, we will generate a full signature.
	case typeDocCallSigNode, typeDocConstructorSigNode:
		return createSignature(node, parent, false)

	// If we don't recognize this node, fail.
	default:
		log.Fatalf("unrecognized node kind: %v (%v)", node.Kind, node.Name)
		return ""
	}
}

func createSignature(node *typeDocNode, parent *typeDocNode, arrow bool) string {
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
		if paramType := createTypeLabel(param.Type, 0); paramType != "" {
			label += ": " + paramType
		}
	}
	label += ")"

	// Add a return type, if any.
	if node.Kind != typeDocConstructorSigNode {
		returnType := createTypeLabel(node.Type, 0)
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

func createCodeDetails(node *typeDocNode) string {
	switch node.Kind {
	case typeDocTypeAliasNode:
		// For type aliases, we won't have signatures, so we will create a detailed label.
		return fmt.Sprintf("<span class='kd'>type</span> %s = %s;", node.Name, createTypeLabel(node.Type, 0))
	case typeDocPropertyNode:
		label := createVisibilityLabel(node.Flags)
		label += node.Name
		if node.Flags.IsOptional {
			label += "?"
		}
		if proptyp := createTypeLabel(node.Type, 0); proptyp != "" {
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
		if vartyp := createTypeLabel(node.Type, 0); vartyp != "" {
			label += ": " + vartyp
		}
		if node.DefaultValue != nil {
			label += " = <span class='s2'>" + html.EscapeString(*node.DefaultValue) + "</span>"
		}
		return label + ";"
	default:
		return ""
	}
}

// typeHyperlink returns the hyperlink for help text associated with a given type, if available.
func typeHyperlink(t *typeDocType) string {
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
		if t.ID != 0 {
			// If this is a reference type in this package, link to it.
			// TODO: inter-module linking.
			return fmt.Sprintf("#%s", t.Name)
		} else {
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
				"ID", "Input", "Inputs", "InvokeOptions", "Output", "Outputs", "Resource", "ResourceOptions", "URN":
				return fmt.Sprintf(
					"/docs/reference/pkg/nodejs/pulumi/pulumi/#%s", t.Name)
			}

			// If this is a qualified name, see if it refers to the Pulumi SDK. If so, generate a link.
			elements := strings.Split(t.Name, ".")
			if len(elements) > 1 && elements[0] == "pulumi" {
				link := "/docs/reference/pkg/nodejs/pulumi/pulumi/"
				for i := 1; i < len(elements)-1; i++ {
					link += fmt.Sprintf("%s/", elements[i])
				}
				return link + fmt.Sprintf("#%s", elements[len(elements)-1])
			}
		}
	}

	return ""
}

func createTypeLabel(t *typeDocType, indent int) string {
	switch t.Type {
	case typeDocArrayType:
		return fmt.Sprintf("%s[]", createTypeLabel(t.ElementType, indent))
	case typeDocIntrinsicType, typeDocParameterType, typeDocReferenceType, typeDocUnknownType:
		// Add a hyperlink for the type if possible.
		var label string
		if hyperlink := typeHyperlink(t); hyperlink != "" {
			label += fmt.Sprintf("<a href='%s'>%s</a>", hyperlink, t.Name)
		} else {
			label += t.Name
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
				label += createTypeLabel(tyarg, indent)
			}
			label += "&gt;"
		}
		return label
	case typeDocReflectionType:
		// Either a type literal or a function type.
		decl := t.Declaration
		if len(decl.Signatures) > 0 {
			return createSignature(decl.Signatures[0], nil, true)
		} else if len(decl.Children) > 0 {
			label := "{\n"
			indent++
			for _, child := range decl.Children {
				label += fmt.Sprintf("%s%s: %s;\n",
					strings.Repeat(" ", indent*4), child.Name, createTypeLabel(child.Type, indent))
			}
			indent--
			return fmt.Sprintf("%s%s}", label, strings.Repeat(" ", indent*4))
		} else if len(decl.IndexSignatures) == 1 {
			index := decl.IndexSignatures[0]
			if len(index.Parameters) == 1 {
				return fmt.Sprintf("{[%s: %s]: %s}",
					index.Parameters[0].Name,
					createTypeLabel(index.Parameters[0].Type, indent),
					createTypeLabel(index.Type, indent))
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
			label += createTypeLabel(elem, indent)
		}
		return label + "]"
	case typeDocUnionType:
		var label string
		for i, inner := range t.Types {
			if i > 0 {
				label += " | "
			}
			label += createTypeLabel(inner, indent)
		}
		return label
	case typeDocIntersectionType:
		var label string
		for i, inner := range t.Types {
			if i > 0 {
				label += " &amp; "
			}
			label += createTypeLabel(inner, indent)
		}
		return label
	case typeDocTypeOperatorType:
		targetStr := createTypeLabel(t.Target, indent)
		return fmt.Sprintf("%s %s", t.Operator, targetStr)
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
	// RepoURL is a link to this member in the relevant Git repo.  It's augmented information.
	RepoURL string
	// Extends is a rendered type this type inherits from (or empty if none).
	Extends string
	// Implements is a rendered list of interfaces this type implements (if any, or empty if none).
	Implements string
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
}

type typeDocTypeType string

const (
	typeDocArrayType         typeDocTypeType = "array"
	typeDocIntrinsicType     typeDocTypeType = "intrinsic"
	typeDocIntersectionType  typeDocTypeType = "intersection"
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
