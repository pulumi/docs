package cmd

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"strings"

	"github.com/pkg/errors"

	"github.com/spf13/cobra"

	"github.com/ghodss/yaml"

	"github.com/golang/glog"

	"github.com/pulumi/docs/tools/resourcedocsgen/pkg"
	docsgen "github.com/pulumi/pulumi/pkg/v3/codegen/docs"
	"github.com/pulumi/pulumi/pkg/v3/codegen/dotnet"
	go_gen "github.com/pulumi/pulumi/pkg/v3/codegen/go"
	"github.com/pulumi/pulumi/pkg/v3/codegen/nodejs"
	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tools"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/contract"
)

const (
	tool                        = "Pulumi Docs Generator"
	registryRepo                = "https://github.com/pulumi/registry"
	defaultSchemaFilePathFormat = "/provider/cmd/pulumi-resource-%s/schema.json"
)

var mainSpec *pschema.PackageSpec

func getRegistryPackagesPath(repoPath string) string {
	return filepath.Join(repoPath, "themes", "default", "data", "registry", "packages")
}

func getPulumiPackageFromSchema(docsOutDir, overlaysSchemaFile string) (*pschema.Package, error) {
	if overlaysSchemaFile != "" {
		overlaySpec := &pschema.PackageSpec{}
		overlaysSchema, err := ioutil.ReadFile(overlaysSchemaFile)
		if err != nil {
			return nil, errors.Wrap(err, "reading overlay schema file from path")
		}
		if err := json.Unmarshal(overlaysSchema, overlaySpec); err != nil {
			return nil, errors.Wrap(err, "unmarshalling overlay schema into a PackageSpec")
		}

		if err := mergeOverlaySchemaSpec(mainSpec, overlaySpec); err != nil {
			return nil, errors.Wrap(err, "merging the overlay schema spec with the main spec")
		}
	}

	// Delete existing docs before generating new ones.
	if err := os.RemoveAll(docsOutDir); err != nil {
		return nil, errors.Wrapf(err, "deleting provider directory %v", docsOutDir)
	}

	pulPkg, err := pschema.ImportSpec(*mainSpec, nil)
	if err != nil {
		return nil, errors.Wrapf(err, "error importing package spec: %v", err)
	}

	docsgen.Initialize(tool, pulPkg)

	return pulPkg, nil
}

func getRepoSlug(repoURL string) (string, error) {
	u, err := url.Parse(repoURL)
	if err != nil {
		return "", errors.Wrapf(err, "parsing repo url %s", repoURL)
	}

	return u.Path, nil
}

func genResourceDocsForPackageFromRegistryMetadata(metadata pkg.PackageMeta, docsOutDir, packageTreeJSONOutDir string) error {
	glog.Infoln("Generating docs for", metadata.Name)
	if metadata.RepoURL == "" {
		return errors.Errorf("metadata for package %q does not contain the repo_url", metadata.Name)
	}

	schemaFilePath := fmt.Sprintf(defaultSchemaFilePathFormat, metadata.Name)
	if metadata.SchemaFilePath != "" {
		schemaFilePath = metadata.SchemaFilePath
	}

	// Make sure the schema file path does not have a leading slash.
	// We'll add in the URL format below. It's easier to read that way.
	schemaFilePath = strings.TrimPrefix(schemaFilePath, "/")

	repoSlug, err := getRepoSlug(metadata.RepoURL)

	glog.Infoln("Reading remote schema file from VCS")
	// TODO: Support raw URLs for other VCS too.
	schemaFileURL := fmt.Sprintf("https://raw.githubusercontent.com/%s/%s/%s", repoSlug, metadata.Version, schemaFilePath)
	resp, err := http.Get(schemaFileURL)
	if err != nil {
		return errors.Wrapf(err, "reading schema file from VCS %s", schemaFileURL)
	}

	schemaBytes, err := io.ReadAll(resp.Body)
	if err != nil {
		return errors.Wrapf(err, "reading response body from %s", schemaFileURL)
	}

	// The source schema can be in YAML format. If that's the case
	// convert it to JSON first.
	if strings.HasSuffix(schemaFilePath, ".yaml") {
		schemaBytes, err = yaml.YAMLToJSON(schemaBytes)
		if err != nil {
			return errors.Wrap(err, "reading YAML schema")
		}
	}

	mainSpec = &pschema.PackageSpec{}
	if err := json.Unmarshal(schemaBytes, mainSpec); err != nil {
		return errors.Wrap(err, "unmarshalling schema into a PackageSpec")
	}

	// TODO: check the overlays folder for the current package to see if it
	// has any overlays.
	pulPkg, err := getPulumiPackageFromSchema(docsOutDir, "")
	if err != nil {
		return errors.Wrap(err, "generating package from schema file")
	}

	glog.Infoln("Running docs generator now")
	if err := generateDocsFromSchema(docsOutDir, pulPkg); err != nil {
		return errors.Wrap(err, "generating docs from schema")
	}

	glog.Infoln("Generating the package tree JSON file")
	if err := generatePackageTree(packageTreeJSONOutDir, pulPkg.Name); err != nil {
		return errors.Wrap(err, "generating package tree")
	}

	return nil
}

func genResourceDocsForAllRegistryPackages(registryRepoPath, baseDocsOutDir, basePackageTreeJSONOutDir string) error {
	registryPackagesPath := getRegistryPackagesPath(registryRepoPath)
	metadataFiles, err := os.ReadDir(registryPackagesPath)
	if err != nil {
		return errors.Wrap(err, "reading the registry packages dir")
	}

	for _, f := range metadataFiles {
		glog.Infoln("Processing metadata file", f.Name())
		metadataFilePath := filepath.Join(registryPackagesPath, f.Name())

		b, err := os.ReadFile(metadataFilePath)
		if err != nil {
			return errors.Wrapf(err, "reading the metadata file %s", metadataFilePath)
		}

		var metadata pkg.PackageMeta
		if err := yaml.Unmarshal(b, &metadata); err != nil {
			return errors.Wrapf(err, "unmarshalling the metadata file %s", metadataFilePath)
		}

		docsOutDir := filepath.Join(baseDocsOutDir, metadata.Name, "api-docs")
		err = genResourceDocsForPackageFromRegistryMetadata(metadata, docsOutDir, basePackageTreeJSONOutDir)
		if err != nil {
			return errors.Wrapf(err, "generating resource docs using metadata file info %s", f.Name())
		}
	}

	return nil
}

func genResourceDocsFromRegistry() *cobra.Command {
	var baseDocsOutDir string
	var basePackageTreeJSONOutDir string

	cmd := &cobra.Command{
		Use:   "registry [pkgName]",
		Short: "Generate resource docs for a package from the registry",
		Long: "Generate resource docs for all packages in the registry or specific packages. " +
			"Pass a package name in the registry as an optional arg to generate docs only for that package.",
		RunE: func(cmd *cobra.Command, args []string) error {
			tempDir, err := ioutil.TempDir("", "")
			if err != nil {
				return errors.Wrap(err, "creating temp dir for registry repo")
			}

			defer os.RemoveAll(tempDir)

			branch := "praneetloke/regen-metadata"
			glog.Infoln("Cloning the registry repo @", branch)
			gitCmd := exec.Command("git", "clone", "-b", branch, registryRepo, tempDir)
			gitCmd.Stdout = os.Stdout
			if err := gitCmd.Run(); err != nil {
				return errors.Wrap(err, "cloning the registry repo")
			}

			glog.Infoln("Cloned the repo successfully!")

			if len(args) > 0 {
				glog.Infoln("Generating docs for a single package:", args[0])
				registryPackagesPath := getRegistryPackagesPath(tempDir)
				pkgName := args[0]
				metadataFilePath := filepath.Join(registryPackagesPath, fmt.Sprintf("%s.yaml", pkgName))
				b, err := os.ReadFile(metadataFilePath)
				if err != nil {
					return errors.Wrapf(err, "reading the metadata file %s", metadataFilePath)
				}

				var metadata pkg.PackageMeta
				if err := yaml.Unmarshal(b, &metadata); err != nil {
					return errors.Wrapf(err, "unmarshalling the metadata file %s", metadataFilePath)
				}

				docsOutDir := filepath.Join(baseDocsOutDir, metadata.Name, "api-docs")

				err = genResourceDocsForPackageFromRegistryMetadata(metadata, docsOutDir, basePackageTreeJSONOutDir)
				if err != nil {
					return errors.Wrapf(err, "generating docs for package %q from registry metadata", pkgName)
				}
			} else {
				glog.Infoln("Generating docs for all packages in the registry...")
				err := genResourceDocsForAllRegistryPackages(tempDir, baseDocsOutDir, basePackageTreeJSONOutDir)
				if err != nil {
					return errors.Wrap(err, "generating docs for all packages from registry metadata")
				}
			}

			glog.Infoln("Done!")
			return nil
		},
	}

	cmd.Flags().StringVar(&baseDocsOutDir, "baseDocsOutDir", "../../content/registry/packages", "The directory path to where the docs will be written to")
	cmd.Flags().StringVar(&basePackageTreeJSONOutDir, "basePackageTreeJSONOutDir", "../../static/registry/packages/navs", "The directory path to write the package tree JSON file to")

	return cmd
}

func resourceDocsCmd() *cobra.Command {
	var schemaFile string
	var version string
	var docsOutDir string
	var overlaysSchemaFile string
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

			pulPkg, err := getPulumiPackageFromSchema(docsOutDir, overlaysSchemaFile)
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
	cmd.Flags().StringVar(&overlaysSchemaFile, "overlaysSchemaFile", "", "(Optional) Overlays that should be merged with the main schema")

	cmd.MarkFlagRequired("docsOutDir")
	cmd.MarkFlagRequired("packageTreeJSONOutDir")
	cmd.MarkFlagRequired("schemaFile")
	cmd.MarkFlagRequired("version")

	cmd.AddCommand(genResourceDocsFromRegistry())

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
		if err := emitFile(outDir, f, contents); err != nil {
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
	if err := emitFile(outDir, filename, b); err != nil {
		return errors.Wrap(err, "writing the package tree")
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
