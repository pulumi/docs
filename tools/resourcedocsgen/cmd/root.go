package cmd

import (
	"encoding/json"
	"io/ioutil"

	"github.com/pkg/errors"

	"github.com/spf13/cobra"

	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"
	"github.com/pulumi/pulumi/sdk/v3/go/common/util/logging"
)

var (
	schemaFile  string
	version     string
	mainSpec    *pschema.PackageSpec
	logToStderr bool
	verbose     int
)

func RootCmd() *cobra.Command {
	rootCmd := &cobra.Command{
		Use:   "resourcedocsgen",
		Short: "Generate Pulumi resource docs",
		Long: "A tool to generate resource docs and package metadata for Pulumi provider and component packages. " +
			"This tool relies a Pulumi package's schema spec. " +
			"This tool will not generate the schema.",
		PersistentPreRunE: func(cmd *cobra.Command, args []string) error {
			logging.InitLogging(logToStderr, verbose, false)

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
	}
	rootCmd.PersistentFlags().StringVarP(&schemaFile, "schemaFile", "s", "", "Path to the schema.json file")
	rootCmd.PersistentFlags().StringVar(&version, "version", "", "The version of the package")
	rootCmd.PersistentFlags().BoolVar(&logToStderr, "logtostderr", false, "Log to stderr instead of to files")
	rootCmd.PersistentFlags().IntVarP(&verbose, "verbose", "v", 0, "Enable verbose logging (e.g., v=3); anything >3 is very verbose")

	rootCmd.MarkPersistentFlagRequired("schemaFile")
	rootCmd.MarkPersistentFlagRequired("version")

	rootCmd.AddCommand(resourceDocsCmd())
	rootCmd.AddCommand(packageMetadataCmd())

	return rootCmd
}
