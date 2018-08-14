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
	"io/ioutil"
	"log"
	"os"
	"path"
	"path/filepath"
	"sort"
	"strings"
	"unicode"
)

func main() {
	// Grab the args.
	flag.Parse()
	args := flag.Args()
	if len(args) < 2 {
		fmt.Fprintf(os.Stderr, "error: usage: %s <doc-file> <out-dir>\n", os.Args[0])
		os.Exit(1)
	}

	// Load and parse the document.
	doc, err := loadAndParseDoc(args[0])
	if err != nil {
		fmt.Fprintf(os.Stderr, "error: reading and parsing docs file: %v\n", err)
		os.Exit(1)
	}

	// Assuming that succeeded, simply emit the Markdown docs now.
	if err = emitMarkdownDocs(doc, args[1]); err != nil {
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

	return &doc, nil
}

// gitHubBaseURLs is a *hackhackhack* hard-coded list of URLs for our packages.
// TODO(joe): base this off the package.json file.
var gitHubBaseURLs = map[string]string{
	"@pulumi/pulumi":         "https://github.com/pulumi/pulumi/blob/master/sdk/nodejs",
	"@pulumi/aws":            "https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs",
	"@pulumi/aws-infra":      "https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs",
	"@pulumi/aws-serverless": "https://github.com/pulumi/pulumi-aws-serverless/blob/master/nodejs",
	"@pulumi/azure":          "https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs",
	"@pulumi/kubernetes":     "https://github.com/pulumi/pulumi-kubernetes/blob/master/sdk/nodejs",
	"@pulumi/gcp":            "https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs",
	"@pulumi/cloud":          "https://github.com/pulumi/pulumi-cloud/blob/master/api",
	"@pulumi/cloud-aws":      "https://github.com/pulumi/pulumi-cloud/blob/master/aws",
}

// emitMarkdownDocs takes as input a full Typedoc AST, transforms it into Markdown suitable for our documentation
// website, and emits those files into the target directory.  If the target doesn't exist, it will be created.
func emitMarkdownDocs(doc *typeDocNode, outdir string) error {
	// First, gather up the entries by module.  Note that we are doing something dubious here to make our docs
	// easier to use and navigate than the default ones that Typedoc generates.  We are assuming an idiomatic module
	// structure with top-level index-style exports for each submodule.  In the general case, this isn't always true,
	// and we may generate (a) incorrect documentation by showing something that isn't truly exported and (b) omit
	// important details about the specific inner modules that truly contain the members in question.  I'm sure we'll
	// want to revisit this and make the logic here more sophisticated and general purpose someday.
	pkg := doc.Name
	repoURL := gitHubBaseURLs[pkg]
	e := newEmitter(pkg, repoURL, outdir)
	e.augmentNode(doc, nil)
	root := e.gatherModules(doc)
	return e.emitMarkdownModule(rootModule, root, true)
}

type emitter struct {
	pkg     string // the NPM package name.
	repoURL string // the base repo URL for this package's code.
	outdir  string // where to store the output files.
}

func newEmitter(pkg, repoURL, outdir string) *emitter {
	return &emitter{
		pkg:     pkg,
		repoURL: repoURL,
		outdir:  outdir,
	}
}

// augmentNode recurses throughout a tree AST, adding information that we'll need when translating it to Markdown.
func (e *emitter) augmentNode(node *typeDocNode, parent *typeDocNode) {
	// Add some labels.
	node.Label = createLabel(node, parent)
	node.DetailedLabel = createDetailedLabel(node)
	node.RepoURL = getRepoURL(e.repoURL, node)

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
	var breadcrumbs []string
	if root {
		title = fmt.Sprintf("Package %s", e.pkg)
		pkg = e.pkg
		pkgvar = camelCase(e.pkg[strings.IndexRune(e.pkg, '/')+1:])
	} else {
		title = fmt.Sprintf("Module %s", name)

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
				[]string{fmt.Sprintf("<a href=\"%s/index.html\">%s</a> &gt; ", crumbs, name)},
				breadcrumbs...)
			if crumbs != "" {
				crumbs += string(filepath.Separator)
			}
			crumbs += ".."
		}

		// Finally, add the link to the root module.
		breadcrumbs = append(
			[]string{fmt.Sprintf("<a href=\"%s/index.html\">%s</a> &gt; ", crumbs, e.pkg)},
			breadcrumbs...)
	}

	// Now build an index of files and members.
	var files []string
	filesAdded := make(map[string]bool)
	var members []*typeDocNode
	for _, member := range mod.Exports {
		for _, source := range member.Sources {
			if source.FileName != "" {
				if !filesAdded[source.FileName] {
					files = append(files, source.FileName)
					filesAdded[source.FileName] = true
				}
			}
		}
		members = append(members, member)
	}
	sort.Strings(files)
	sort.Slice(members, func(i, j int) bool {
		return members[i].Label < members[j].Label
	})

	// Get any submodules, make relative links, and ensure they are sorted in a deterministic order.
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
		"Title":       title,
		"Breadcrumbs": breadcrumbs,
		"RepoURL":     e.repoURL,
		"Package":     pkg,
		"PackageVar":  pkgvar,
		"Files":       files,
		"Modules":     modules,
		"HasModules":  len(modules) > 0,
		"Members":     members,
		"HasMembers":  len(members) > 0,
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

// gatherModules walks a Typedoc AST and turns it into a proper module structure, to ease Markdown emission.
func (e *emitter) gatherModules(doc *typeDocNode) *module {
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
			fmt.Fprintf(os.Stderr, "warning: expected a module, got %s (%s)\n", modnode.Kind, modnode.Name)
			continue
		}

		// Simplify the module name, because we assume a simplified index-based re-export structure.  This will
		// flatten out all inner submodules to their index, so that all children will aggregate naturally.
		modname := simplifyModuleName(modnode)

		// Lazy init the module if appropriate.
		mod := mods[modname]
		if mod == nil {
			mod = newModule()
			mods[modname] = mod
		}

		// Add all exported children from this module to the export list.
		for _, child := range modnode.Children {
			// Skip unexported children.
			if !child.Flags.IsExported {
				continue
			}

			if child.Kind == typeDocModuleNode {
				// If this is a module (namespace), we must explode it out into the top-level modules list.
				// This may very well conflict, so we'll need to merge the new members in if so.
				nss := e.gatherNamespaceModules(path.Join(child.Name), child)
				for nsname, ns := range nss {
					if exist, has := mods[nsname]; has {
						exist.Merge(ns)
					} else {
						mods[nsname] = ns
					}
				}
			} else {
				// Else, register this child as an export.
				name := child.Name
				if mod.Exports[name] != nil {
					fmt.Fprintf(os.Stderr, "warning: duplicate child %s for module %s\n", name, modname)
					continue
				}
				mod.Exports[name] = child
			}
		}

	}

	// Now that we've done a first pass, construct the tree structure, and return the root node.
	root := mods[rootModule]
	if root == nil {
		root = newModule()
		mods[rootModule] = root
	}
	for modname, mod := range mods {
		if modname != rootModule {
			parname := getModuleParentName(modname)
			par := mods[parname]
			if par == nil {
				par = newModule()
				mods[parname] = par
			}
			par.Modules[modname] = mod
		}
	}
	return root
}

// gatherNamespaceModules returns a flat list of namespaces, recursively extracted from the tree.  The list is
// flat so that we can easily merge any duplicate entries, as namespaces can be spread across many modules.
func (e *emitter) gatherNamespaceModules(name string, node *typeDocNode) map[string]*module {
	// Start with a single module, but be prepared to append more if we find them.
	ns := newModule()
	nss := map[string]*module{
		name: ns,
	}

	// Find any children modules.
	for _, child := range node.Children {
		if child.Kind == typeDocModuleNode {
			submods := e.gatherNamespaceModules(path.Join(name, child.Name), child)
			for subname, submod := range submods {
				if exist, has := nss[subname]; has {
					exist.Merge(submod)
				} else {
					nss[subname] = submod
				}
			}
		} else {
			cn := child.Name
			if ns.Exports[cn] != nil {
				fmt.Fprintf(os.Stderr, "warning: duplicate child %s for namespace %s\n", cn, name)
				continue
			}
			ns.Exports[cn] = child
		}
	}

	return nss
}

// module is an aggregate structure conceptually mapping to an ES6 module.
type module struct {
	// Exports is a map of names to the exported member's Typedoc AST node.
	Exports map[string]*typeDocNode
	// Modules is a map of names to nested ES6 modules re-exported as a name by this module.
	Modules map[string]*module
}

func newModule() *module {
	return &module{
		Exports: make(map[string]*typeDocNode),
		Modules: make(map[string]*module),
	}
}

// Merge another module into this one, in place, by mutating it.
func (m *module) Merge(other *module) {
	for k, exp := range other.Exports {
		if _, has := m.Exports[k]; has {
			//fmt.Fprintf(os.Stderr, "warning: duplicate module member %s\n", k)
		}
		m.Exports[k] = exp
	}
	for k, mod := range other.Modules {
		if exist, has := m.Modules[k]; has {
			exist.Merge(mod)
		} else {
			m.Modules[k] = mod
		}
	}
}

// rootModule is the special name of the root index module.
const rootModule = "index"

func getModuleFilename(m string) string {
	// Each module gets its own subdirectory and index.md.  The package root gets a bit more metadata at the top.
	if m == rootModule {
		return "index.md"
	}
	return filepath.Join(strings.Replace(m, "/", string(filepath.Separator), -1), "index.md")
}

func getModuleParentName(m string) string {
	if slix := strings.IndexRune(m, '/'); slix != -1 {
		return m[:slix]
	}
	return rootModule
}

// simplifyModuleName turns a module AST's name into a simplified module name.
func simplifyModuleName(modnode *typeDocNode) string {
	name := strings.Trim(modnode.Name, "\"")
	if slix := strings.IndexRune(name, '/'); slix != -1 {
		return name[:slix]
	}
	return rootModule
}

func getRepoURL(baseURL string, node *typeDocNode) string {
	if len(node.Sources) > 0 && node.Sources[0].FileName != "" {
		return fmt.Sprintf("%s/%s#L%d", baseURL, node.Sources[0].FileName, node.Sources[0].Line)
	}
	return baseURL
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
	Type typeDocType `json:"type,omitempty"`
	// Comment is a JSDoc comment extracted via Typedoc.
	Comment typeDocComment `json:"comment,omitempty"`
	// DefaultValue is an optional default value for this entry (or nil if none).
	DefaultValue *string `json:"defaultValue,omitempty"`
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
	ExtendedTypes []*typeDocType `json:"extendedBy,omitempty"`
	// Sources represents the source files from which this node came.
	Sources []typeDocSource `json:"sources,omitempty"`

	// Label is not stored in the file, it's a label generated by doing a pass over the AST.
	Label string
	// DetailedLabel is used for cases where a member has details beyond the simple label used as a header.
	DetailedLabel string
	// RepoURL is a link to this member in the relevant Git repo.  It's augmented information.
	RepoURL string
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
		return fmt.Sprintf("class %s", node.Name)
	case typeDocConstructorNode:
		return fmt.Sprintf("constructor")
	case typeDocEnumNode:
		return fmt.Sprintf("enum %s", node.Name)
	case typeDocFunctionNode:
		return fmt.Sprintf("function %s", node.Name)
	case typeDocInterfaceNode:
		return fmt.Sprintf("interface %s", node.Name)
	case typeDocMethodNode:
		return fmt.Sprintf("method %s", node.Name)
	case typeDocExternalModuleNode, typeDocModuleNode:
		return fmt.Sprintf("module %s", node.Name)
	case typeDocPackageNode:
		return fmt.Sprintf("package %s", node.Name)
	case typeDocParameterNode:
		return fmt.Sprintf("parameter %s", node.Name)
	case typeDocPropertyNode:
		return fmt.Sprintf("property %s", node.Name)
	case typeDocTypeAliasNode:
		return fmt.Sprintf("type %s", node.Name)
	case typeDocEnumMemberNode:
		return fmt.Sprintf("enum member %s", node.Name)
	case typeDocVariableNode, typeDocObjectLiteral:
		if node.Flags.IsConst {
			return fmt.Sprintf("const %s", node.Name)
		} else {
			return fmt.Sprintf("let %s", node.Name)
		}

	// For others, we will generate a full signature.
	case typeDocCallSigNode, typeDocConstructorSigNode:
		var label string

		if parent != nil {
			label += createVisibilityLabel(parent.Flags)
		}

		label += node.Name

		// If there are generic type arguments, add them now.
		if len(node.TypeParameter) > 0 {
			label += "<"
			for i, typaram := range node.TypeParameter {
				if i > 0 {
					label += ","
				}
				label += typaram.Name
			}
			label += ">"
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
			if paramType := createTypeLabel(param.Type); paramType != "" {
				label += ": " + paramType
			}
		}
		label += ")"

		// Add a return type, if any.
		if node.Kind != typeDocConstructorSigNode {
			if returnType := createTypeLabel(node.Type); returnType != "" {
				label += ": " + returnType
			}
		}

		return label

	// If we don't recognize this node, fail.
	default:
		log.Fatalf("unrecognized node kind: %v (%v)", node.Kind, node.Name)
		return ""
	}
}

func createDetailedLabel(node *typeDocNode) string {
	switch node.Kind {
	case typeDocTypeAliasNode:
		// For type aliases, we won't have signatures, so we will create a detailed label.
		return fmt.Sprintf("type %s = %s;", node.Name, createTypeLabel(node.Type))
	case typeDocPropertyNode:
		label := createVisibilityLabel(node.Flags)
		label += node.Name
		if node.Flags.IsOptional {
			label += "?"
		}
		if proptyp := createTypeLabel(node.Type); proptyp != "" {
			label += ": " + proptyp
		}
		if node.DefaultValue != nil {
			label += " = " + *node.DefaultValue
		}
		return label + ";"
	case typeDocVariableNode:
		var label string
		if node.Flags.IsConst {
			label += "const "
		} else {
			label += "let "
		}
		label += node.Name
		if vartyp := createTypeLabel(node.Type); vartyp != "" {
			label += ": " + vartyp
		}
		if node.DefaultValue != nil {
			label += " = " + *node.DefaultValue
		}
		return label + ";"
	default:
		return ""
	}
}

func createTypeLabel(t typeDocType) string {
	// TODO: hyperlink the types.
	switch t.Type {
	case typeDocArrayType:
		return fmt.Sprintf("%s[]", createTypeLabel(*t.ElementType))
	case typeDocIntrinsicType, typeDocParameterType, typeDocReferenceType, typeDocUnknownType:
		label := t.Name
		if len(t.TypeArguments) > 0 {
			label += "<"
			for i, tyarg := range t.TypeArguments {
				if i > 0 {
					label += ", "
				}
				label += createTypeLabel(tyarg)
			}
			label += ">"
		}
		return label
	case typeDocReflectionType:
		// TODO: expand out type literals.
		return "{ ... }"
	case typeDocStringLiteralType:
		return t.Value
	case typeDocTupleType:
		label := "["
		for i, elem := range t.Elements {
			if i >= 0 {
				label += ", "
			}
			label += createTypeLabel(elem)
		}
		return label + "]"
	case typeDocUnionType:
		var label string
		for i, inner := range t.Types {
			if i > 0 {
				label += " | "
			}
			label += createTypeLabel(inner)
		}
		return label
	case typeDocTypeOperatorType:
		targetStr := createTypeLabel(*t.Target)
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
	return label
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
	// Type is the type of the type.
	Type typeDocTypeType `json:"type,omitempty"`
	// Name is the name of the type.
	Name string `json:"name,omitempty"`
	// Elements contains the element type for tuples.
	Elements []typeDocType `json:"elements,omitempty"`
	// ElementType contains the element type for arrays.
	ElementType *typeDocType `json:"elementType,omitempty"`
	// TypeArguments is an optional list of instantiated type args.
	TypeArguments []typeDocType `json:"typeArguments,omitempty"`
	// Types contains the constituent parts of complex types, like unions.
	Types []typeDocType `json:"types,omitempty"`
	// Value is the actual value for literal types.
	Value string `json:"value,omitempty"`
	// Operator is the type operator used, if this is a type operator reference
	Operator string `json:"operator,omitempty"`
	// Target is the target of the type operator, if this is a type operator reference
	Target *typeDocType `json:"target,omitempty"`
}

type typeDocTypeType string

const (
	typeDocArrayType         typeDocTypeType = "array"
	typeDocIntrinsicType     typeDocTypeType = "intrinsic"
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
