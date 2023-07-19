package docs

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"os"
	"strings"

	"github.com/ghodss/yaml"
	"github.com/golang/glog"
	"github.com/hashicorp/hcl/v2"
	"github.com/pkg/errors"
	"github.com/pulumi/docs/tools/resourcedocsgen/pkg"
	"github.com/spf13/cobra"

	docsgen "github.com/pulumi/pulumi/pkg/v3/codegen/docs"
	"github.com/pulumi/pulumi/pkg/v3/codegen/dotnet"
	go_gen "github.com/pulumi/pulumi/pkg/v3/codegen/go"
	"github.com/pulumi/pulumi/pkg/v3/codegen/nodejs"
	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"
)

const (
	tool                        = "Pulumi Docs Generator"
	registryRepo                = "https://github.com/pulumi/registry"
	defaultSchemaFilePathFormat = "/provider/cmd/pulumi-resource-%s/schema.json"
)

var (
	// mainSpec represents a package's original schema. It's called "main" because a package
	// could have a hand-authored overlays schema spec in the overlays folder that could be
	// merged into it.
	mainSpec *pschema.PackageSpec
)

func getPulumiPackageFromSchema(docsOutDir string) (*pschema.Package, error) {

	// Delete existing docs before generating new ones.
	if err := os.RemoveAll(docsOutDir); err != nil {
		return nil, errors.Wrapf(err, "deleting provider directory %v", docsOutDir)
	}

	pulPkg, err := pschema.ImportSpec(*mainSpec, nil)
	if err != nil {
		if dErr, ok := err.(hcl.Diagnostics); ok {
			writer := hcl.NewDiagnosticTextWriter(os.Stderr, nil, 80, true)
			wErr := writer.WriteDiagnostics(dErr)
			if wErr != nil {
				err = wErr
			}
		}
		return nil, fmt.Errorf("importing package spec: %w", err)
	}

	// THIS IS A TEMPORARY HACK!!
	// temporarily hacking this tool to accommodate multiple versions of the azure-native package,
	// since both v1 and v2 are techically the same package (just different versons) so the
	// schema.json file will have `azure-native` as the package name. Without this, the files genned
	// will be overwritten by the second version of the package, since they will end up being written
	// to the same azure-native directory.
	if strings.Contains(docsOutDir, "azure-native-v2") {
		pulPkg.Name = "azure-native-v2"
	}

	if strings.Contains(docsOutDir, "azure-native-v1") {
		pulPkg.Name = "azure-native-v1"
	}

	docsgen.Initialize(tool, pulPkg)

	return pulPkg, nil
}

func ResourceDocsCmd() *cobra.Command {
	var schemaFile string
	var version string
	var docsOutDir string
	var packageTreeJSONOutDir string

	cmd := &cobra.Command{
		Use:   "docs",
		Short: "Generate resource docs from a Pulumi schema file",
		RunE: func(cmd *cobra.Command, args []string) error {
			schema, err := ioutil.ReadFile(schemaFile)
			if err != nil {
				return errors.Wrap(err, "reading schema file from path")
			}

			// The source schema can be in YAML format. If that's the case
			// convert it to JSON first.
			if strings.HasSuffix(schemaFile, ".yaml") {
				schema, err = yaml.YAMLToJSON(schema)
				if err != nil {
					return errors.Wrap(err, "reading YAML schema")
				}
			}

			mainSpec = &pschema.PackageSpec{}
			if err := json.Unmarshal(schema, mainSpec); err != nil {
				return errors.Wrap(err, "unmarshalling schema into a PackageSpec")
			}
			mainSpec.Version = version

			pulPkg, err := getPulumiPackageFromSchema(docsOutDir)
			if err != nil {
				return errors.Wrap(err, "generating package from schema file")
			}

			if err := generateDocsFromSchema(docsOutDir, pulPkg); err != nil {
				return errors.Wrap(err, "generating docs from schema")
			}

			if err := generatePackageTree(packageTreeJSONOutDir, pulPkg.Name); err != nil {
				return errors.Wrap(err, "generating package tree")
			}

			return nil
		},
	}

	cmd.Flags().StringVarP(&schemaFile, "schemaFile", "s", "", "Path to the schema.json file")
	cmd.Flags().StringVar(&version, "version", "", "The version of the package")
	cmd.Flags().StringVar(&docsOutDir, "docsOutDir", "", "The directory path to where the docs will be written to")
	cmd.Flags().StringVar(&packageTreeJSONOutDir, "packageTreeJSONOutDir", "", "The directory path to write the package tree JSON file to")

	cmd.MarkFlagRequired("docsOutDir")
	cmd.MarkFlagRequired("packageTreeJSONOutDir")
	cmd.MarkFlagRequired("schemaFile")
	cmd.MarkFlagRequired("version")

	cmd.AddCommand(resourceDocsFromRegistryCmd())

	return cmd
}

// mergeOverlaySchemaSpec merges the resources, types and language info from the overlay schema spec
// into the main package spec.
func mergeOverlaySchemaSpec(mainSpec *pschema.PackageSpec, overlaySpec *pschema.PackageSpec) error {
	// Merge the overlay schema spec into the main schema spec.
	for key, value := range overlaySpec.Types {
		if _, ok := mainSpec.Types[key]; ok {
			glog.Infoln(key, "was skipped because it was already in the main schema spec")
			continue
		}
		glog.Infoln(key, "adding overlay type")
		mainSpec.Types[key] = value
	}
	for key, value := range overlaySpec.Resources {
		if _, ok := mainSpec.Resources[key]; ok {
			glog.Infoln(key, "was skipped because it was already in the main schema spec")
			continue
		}
		glog.Infoln(key, "adding overlay resource")
		mainSpec.Resources[key] = value
	}
	for lang, overlayLanguageInfo := range overlaySpec.Language {
		switch lang {
		case "go":
			var mainSchemaPkgInfo go_gen.GoPackageInfo
			if err := json.Unmarshal(mainSpec.Language[lang], &mainSchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling Go package info from the main schema spec")
			}

			var overlaySchemaPkgInfo go_gen.GoPackageInfo
			if err := json.Unmarshal(overlayLanguageInfo, &overlaySchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling Go package info from the overlay schema spec")
			}

			for key, value := range overlaySchemaPkgInfo.ModuleToPackage {
				if _, ok := mainSchemaPkgInfo.ModuleToPackage[key]; ok {
					glog.Infoln("Go ModuleToPackage key", key, "was skipped because it was already in the main schema's language info")
					continue
				}
				mainSchemaPkgInfo.ModuleToPackage[key] = value
			}

			// Override the language info for Go in the main schema spec.
			b, err := json.Marshal(mainSchemaPkgInfo)
			if err != nil {
				return errors.Wrap(err, "error marshalling Go package info")
			}
			mainSpec.Language[lang] = b
		case "nodejs":
			var mainSchemaPkgInfo nodejs.NodePackageInfo
			if err := json.Unmarshal(mainSpec.Language[lang], &mainSchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling NodeJS package info from the main schema spec")
			}

			var overlaySchemaPkgInfo nodejs.NodePackageInfo
			if err := json.Unmarshal(overlayLanguageInfo, &overlaySchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling NodeJS package info from the overlay schema spec")
			}

			for key, value := range overlaySchemaPkgInfo.ModuleToPackage {
				if _, ok := mainSchemaPkgInfo.ModuleToPackage[key]; ok {
					glog.Infoln("NodeJS ModuleToPackage key", key, "was skipped because it was already in the main schema's language info")
					continue
				}
				mainSchemaPkgInfo.ModuleToPackage[key] = value
			}

			// Override the language info for NodeJS in the main schema spec.
			b, err := json.Marshal(mainSchemaPkgInfo)
			if err != nil {
				return errors.Wrap(err, "error marshalling NodeJS package info")
			}
			mainSpec.Language[lang] = b
		case "csharp":
			var mainSchemaPkgInfo dotnet.CSharpPackageInfo
			if err := json.Unmarshal(mainSpec.Language[lang], &mainSchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling C# package info from the main schema spec")
			}

			var overlaySchemaPkgInfo dotnet.CSharpPackageInfo
			if err := json.Unmarshal(overlayLanguageInfo, &overlaySchemaPkgInfo); err != nil {
				return errors.Wrap(err, "error un-marshalling C# package info from overlay schema spec")
			}

			for key, value := range overlaySchemaPkgInfo.Namespaces {
				if _, ok := mainSchemaPkgInfo.Namespaces[key]; ok {
					glog.Infoln("C# Namespaces key", key, "was skipped because it was already in the main schema's language info")
					continue
				}
				mainSchemaPkgInfo.Namespaces[key] = value
			}
			// Override the language info for C# in the main schema spec.
			b, err := json.Marshal(mainSchemaPkgInfo)
			if err != nil {
				return errors.Wrap(err, "error marshalling C# package info")
			}
			mainSpec.Language[lang] = b
		}
	}

	return nil
}

func generateDocsFromSchema(outDir string, pulPkg *pschema.Package) error {
	files, err := docsgen.GeneratePackage(tool, pulPkg)
	if err != nil {
		return errors.Wrap(err, "generating Pulumi package")
	}

	for f, contents := range files {
		if err := pkg.EmitFile(outDir, f, contents); err != nil {
			return errors.Wrapf(err, "emitting file %v", f)
		}
	}
	return nil
}

func generatePackageTree(outDir string, pkgName string) error {
	tree, err := docsgen.GeneratePackageTree()
	if err != nil {
		return errors.Wrap(err, "generating the package tree")
	}

	b, err := json.Marshal(tree)
	if err != nil {
		return errors.Wrap(err, "marshalling the package tree")
	}

	filename := fmt.Sprintf("%s.json", pkgName)
	if err := pkg.EmitFile(outDir, filename, b); err != nil {
		return errors.Wrap(err, "writing the package tree")
	}

	return nil
}
