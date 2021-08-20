package cmd

import (
	"encoding/json"
	"io/ioutil"

	"github.com/pkg/errors"

	"github.com/spf13/cobra"

	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"
)

var (
	schemaFile string
	version    string
	mainSpec   *pschema.PackageSpec
)

func RootCmd() *cobra.Command {
	rootCmd := &cobra.Command{
		Use:   "resourcedocsgen",
		Short: "Generate Pulumi resource docs",
		Long: `A tool to generate resource docs and package metadata for Pulumi
                provider and component packages. This tool relies a Pulumi package's
				schema spec. This tool will not generate the schema.`,
		TraverseChildren: true,
		PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
			if schemaFile == "" {
				return nil
			}

			schema, err := ioutil.ReadFile(schemaFile)
			if err != nil {
				return errors.Wrap(err, "reading schema file from path")
			}

			mainSpec = &pschema.PackageSpec{}
			if err := json.Unmarshal(schema, mainSpec); err != nil {
				return errors.Wrap(err, "unmarshalling schema into a PackageSpec")
			}
			mainSpec.Version = version

			return nil
		},
		RunE: func(cmd *cobra.Command, args []string) error {
			if err := resourceDocsCmd().Execute(); err != nil {
				return errors.Wrap(err, "executing the resource docs command")
			}

			if err := packageMetadataCmd().Execute(); err != nil {
				return errors.Wrap(err, "executing the metadata command")
			}

			return nil
		},
	}
	rootCmd.PersistentFlags().StringVarP(&schemaFile, "schemaFile", "s", "", "Path to the schema.json file")
	rootCmd.PersistentFlags().StringVarP(&version, "version", "v", "", "The version of the package")

	rootCmd.MarkPersistentFlagRequired("schemaFile")
	rootCmd.MarkPersistentFlagRequired("version")

	rootCmd.AddCommand(resourceDocsCmd())
	rootCmd.AddCommand(packageMetadataCmd())

	return rootCmd
}
