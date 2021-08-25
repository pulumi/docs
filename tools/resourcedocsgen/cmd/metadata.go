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

var categoryLookup = map[string]pkg.PackageCategory{
	"aiven":         pkg.PackageCategoryInfrastructure,
	"akamai":        pkg.PackageCategoryNetwork,
	"alicloud":      pkg.PackageCategoryCloud,
	"auth0":         pkg.PackageCategoryInfrastructure,
	"aws":           pkg.PackageCategoryCloud,
	"azure":         pkg.PackageCategoryCloud,
	"azure-native":  pkg.PackageCategoryCloud,
	"azuread":       pkg.PackageCategoryInfrastructure,
	"azuredevops":   pkg.PackageCategoryInfrastructure,
	"civo":          pkg.PackageCategoryCloud,
	"cloudamqp":     pkg.PackageCategoryCloud,
	"cloudflare":    pkg.PackageCategoryNetwork,
	"cloudinit":     pkg.PackageCategoryUtility,
	"consul":        pkg.PackageCategoryInfrastructure,
	"datadog":       pkg.PackageCategoryMonitoring,
	"digitalocean":  pkg.PackageCategoryCloud,
	"dnsimple":      pkg.PackageCategoryNetwork,
	"docker":        pkg.PackageCategoryInfrastructure,
	"eks":           pkg.PackageCategoryCloud,
	"f5bigip":       pkg.PackageCategoryNetwork,
	"fastly":        pkg.PackageCategoryCloud,
	"gcp":           pkg.PackageCategoryCloud,
	"google-native": pkg.PackageCategoryCloud,
	"github":        pkg.PackageCategoryVCS,
	"gitlab":        pkg.PackageCategoryVCS,
	"hcloud":        pkg.PackageCategoryCloud,
	"kafka":         pkg.PackageCategoryInfrastructure,
	"keycloak":      pkg.PackageCategoryInfrastructure,
	"kong":          pkg.PackageCategoryInfrastructure,
	"kubernetes":    pkg.PackageCategoryCloud,
	"linode":        pkg.PackageCategoryCloud,
	"mailgun":       pkg.PackageCategoryInfrastructure,
	"mongodbatlas":  pkg.PackageCategoryDatabase,
	"mysql":         pkg.PackageCategoryDatabase,
	"newrelic":      pkg.PackageCategoryMonitoring,
	"ns1":           pkg.PackageCategoryNetwork,
	"okta":          pkg.PackageCategoryInfrastructure,
	"openstack":     pkg.PackageCategoryCloud,
	"opsgenie":      pkg.PackageCategoryInfrastructure,
	"pagerduty":     pkg.PackageCategoryInfrastructure,
	"postgresql":    pkg.PackageCategoryDatabase,
	"rabbitmq":      pkg.PackageCategoryInfrastructure,
	"rancher2":      pkg.PackageCategoryInfrastructure,
	"random":        pkg.PackageCategoryUtility,
	"signalfx":      pkg.PackageCategoryMonitoring,
	"spotinst":      pkg.PackageCategoryInfrastructure,
	"tls":           pkg.PackageCategoryUtility,
	"vault":         pkg.PackageCategoryInfrastructure,
	"venafi":        pkg.PackageCategoryInfrastructure,
	"vsphere":       pkg.PackageCategoryCloud,
	"wavefront":     pkg.PackageCategoryMonitoring,
	"equinix-metal": pkg.PackageCategoryCloud,
	"splunk":        pkg.PackageCategoryInfrastructure,
	"yandex":        pkg.PackageCategoryCloud,
	"rke":           pkg.PackageCategoryInfrastructure,
	"sumologic":     pkg.PackageCategoryMonitoring,
}

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

			category := pkg.PackageCategoryCloud
			if c, ok := categoryLookup[mainSpec.Name]; ok {
				category = c
			}

			pm := pkg.PackageMeta{
				Name:          mainSpec.Name,
				UpdatedOn:     time.Now().Unix(),
				Publisher:     "Pulumi",
				Title:         mainSpec.Name,
				Description:   mainSpec.Description,
				Category:      category,
				PackageStatus: status,
				Featured:      featured,
				Native:        mainSpec.Attribution == "",
				Version:       version,
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
