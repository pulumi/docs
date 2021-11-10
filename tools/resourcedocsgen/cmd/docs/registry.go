package docs

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"net/url"
	"os"
	"os/exec"
	"path/filepath"
	"strings"

	"github.com/spf13/cobra"

	"github.com/ghodss/yaml"

	"github.com/golang/glog"

	"github.com/pkg/errors"

	"github.com/pulumi/docs/tools/resourcedocsgen/pkg"
	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"
)

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

	pulPkg, err := getPulumiPackageFromSchema(docsOutDir)
	if err != nil {
		return errors.Wrap(err, "generating package from schema file")
	}

	glog.Infoln("Running docs generator...")
	if err := generateDocsFromSchema(docsOutDir, pulPkg); err != nil {
		return errors.Wrap(err, "generating docs from schema")
	}

	glog.Infoln("Generating the package tree JSON file...")
	if err := generatePackageTree(packageTreeJSONOutDir, pulPkg.Name); err != nil {
		return errors.Wrap(err, "generating package tree")
	}

	return nil
}

func getRegistryPackagesPath(repoPath string) string {
	return filepath.Join(repoPath, "themes", "default", "data", "registry", "packages")
}

func genResourceDocsForAllRegistryPackages(registryRepoPath, baseDocsOutDir, basePackageTreeJSONOutDir string) error {
	registryPackagesPath := getRegistryPackagesPath(registryRepoPath)
	metadataFiles, err := os.ReadDir(registryPackagesPath)
	if err != nil {
		return errors.Wrap(err, "reading the registry packages dir")
	}

	for _, f := range metadataFiles {
		glog.Infof("=== starting %s ===\n", f.Name())
		glog.Infoln("Processing metadata file")
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

		glog.Infof("=== completed %s ===", f.Name())
	}

	return nil
}

func resourceDocsFromRegistryCmd() *cobra.Command {
	var branch string
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
	cmd.Flags().StringVarP(&branch, "branch", "b", "master", "The branch at which the registry repo will be checked out.")
	cmd.Flags().StringVar(&basePackageTreeJSONOutDir, "basePackageTreeJSONOutDir", "../../static/registry/packages/navs", "The directory path to write the package tree JSON file to")

	return cmd
}
