package cmd

import (
	"encoding/json"
	"io/ioutil"
	"os"
	"path"

	"github.com/golang/glog"

	"github.com/pkg/errors"

	"github.com/spf13/cobra"

	docsgen "github.com/pulumi/pulumi/pkg/v3/codegen/docs"
	"github.com/pulumi/pulumi/pkg/v3/codegen/dotnet"
	go_gen "github.com/pulumi/pulumi/pkg/v3/codegen/go"
	"github.com/pulumi/pulumi/pkg/v3/codegen/nodejs"
	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tools"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
)

var docsOutDir string
var overlaysSchemaFile string

func resourceDocsCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "docs",
		Short: "Generate resource docs from a Pulumi schema file",
		RunE: func(cmd *cobra.Command, args []string) error {
			defer glog.Flush()

			if overlaysSchemaFile != "" {
				overlaySpec := &pschema.PackageSpec{}
				overlaysSchema, err := ioutil.ReadFile(overlaysSchemaFile)
				if err != nil {
					return errors.Wrap(err, "reading overlay schema file from path")
				}
				if err := json.Unmarshal(overlaysSchema, overlaySpec); err != nil {
					return errors.Wrap(err, "unmarshalling overlay schema into a PackageSpec")
				}

				if err := mergeOverlaySchemaSpec(mainSpec, overlaySpec); err != nil {
					return errors.Wrap(err, "merging the overlay schema spec with the main spec")
				}
			}

			// Delete existing docs before generating new ones.
			if err := os.RemoveAll(docsOutDir); err != nil {
				return errors.Wrapf(err, "deleting provider directory %v", docsOutDir)
			}

			if err := generateDocsFromSchema(docsOutDir, mainSpec); err != nil {
				return errors.Wrap(err, "generating docs from schema")
			}

			return nil
		},
	}

	cmd.LocalFlags().StringVarP(&docsOutDir, "docsOutDir", "d", "", "The directory path to where the docs will be written to")
	cmd.LocalFlags().StringVarP(&overlaysSchemaFile, "overlaysSchemaFile", "o", "", "The optional overlays that should be merged with the main schema")

	cmd.MarkFlagRequired("docsOutDir")

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
		mainSpec.Types[key] = value
	}
	for key, value := range overlaySpec.Resources {
		if _, ok := mainSpec.Resources[key]; ok {
			glog.Infoln(key, "was skipped because it was already in the main schema spec")
			continue
		}
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

func generateDocsFromSchema(outDir string, spec *pschema.PackageSpec) error {
	pulPkg, err := pschema.ImportSpec(*spec, nil)
	if err != nil {
		return errors.Wrapf(err, "error importing package spec: %v", err)
	}

	files, err := docsgen.GeneratePackage("Pulumi Docs Generator", pulPkg)
	if err != nil {
		return errors.Wrap(err, "generating Pulumi package")
	}

	for f, contents := range files {
		if err := emitFile(outDir, f, contents); err != nil {
			return errors.Wrapf(err, "emitting file %v", f)
		}
	}
	return nil
}

func emitFile(outDir, relPath string, contents []byte) error {
	p := path.Join(outDir, relPath)
	if err := tools.EnsureDir(path.Dir(p)); err != nil {
		return errors.Wrap(err, "creating directory")
	}

	f, err := os.Create(p)
	if err != nil {
		return errors.Wrap(err, "creating file")
	}
	defer contract.IgnoreClose(f)

	_, err = f.Write(contents)
	return err
}
