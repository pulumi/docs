package cmd

import (
	"fmt"
	"strings"
	"time"

	"github.com/pkg/errors"

	"gopkg.in/yaml.v2"

	"github.com/spf13/cobra"

	"github.com/pulumi/docs/tools/resourcedocsgen/pkg"
)

func packageMetadataCmd() *cobra.Command {
	var metadataOutDir string
	var featured bool

	cmd := &cobra.Command{
		Use:   "metadata <metadataOutDir> [featured]",
		Short: "Generate package metadata only",
		RunE: func(cmd *cobra.Command, args []string) error {
			status := pkg.PackageStatusGA
			if strings.HasPrefix(mainSpec.Description, "v0.") {
				status = pkg.PackageStatusPublicPreview
			}

			pm := pkg.PackageMeta{
				Name:          mainSpec.Name,
				UpdatedOn:     time.Now().Unix(),
				Publisher:     "Pulumi",
				Title:         mainSpec.Name,
				Description:   mainSpec.Description,
				Category:      pkg.PackageCategoryCloud,
				PackageStatus: status,
				Featured:      featured,
				Native:        mainSpec.Attribution == "",
			}
			b, err := yaml.Marshal(pm)
			if err != nil {
				return errors.Wrap(err, "generating package metadata")
			}

			metadataFileName := fmt.Sprintf("%s.yaml", mainSpec.Name)
			if err := emitFile(metadataOutDir, metadataFileName, b); err != nil {
				return errors.Wrap(err, "writing metadata file")
			}

			return nil
		},
	}

	cmd.Flags().StringVar(&metadataOutDir, "metadataOutDir", "", "The directory path to where the docs will be written to")
	cmd.Flags().BoolVar(&featured, "featured", false, "Whether or not this package should be marked as featured in its metadata")

	cmd.MarkFlagRequired("metadataOutDir")

	return cmd
}
