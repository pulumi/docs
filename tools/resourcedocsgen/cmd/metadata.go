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
	"confluent":     pkg.PackageCategoryInfrastructure,
	"consul":        pkg.PackageCategoryInfrastructure,
	"datadog":       pkg.PackageCategoryMonitoring,
	"digitalocean":  pkg.PackageCategoryCloud,
	"dnsimple":      pkg.PackageCategoryNetwork,
	"docker":        pkg.PackageCategoryInfrastructure,
	"eks":           pkg.PackageCategoryCloud,
	"equinix-metal": pkg.PackageCategoryCloud,
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
	"libvirt":       pkg.PackageCategoryUtility,
	"linode":        pkg.PackageCategoryCloud,
	"mailgun":       pkg.PackageCategoryInfrastructure,
	"minio":         pkg.PackageCategoryInfrastructure,
	"mongodbatlas":  pkg.PackageCategoryDatabase,
	"mysql":         pkg.PackageCategoryDatabase,
	"newrelic":      pkg.PackageCategoryMonitoring,
	"nomad":         pkg.PackageCategoryInfrastructure,
	"ns1":           pkg.PackageCategoryNetwork,
	"okta":          pkg.PackageCategoryInfrastructure,
	"openstack":     pkg.PackageCategoryCloud,
	"opsgenie":      pkg.PackageCategoryInfrastructure,
	"pagerduty":     pkg.PackageCategoryInfrastructure,
	"postgresql":    pkg.PackageCategoryDatabase,
	"rabbitmq":      pkg.PackageCategoryInfrastructure,
	"rancher2":      pkg.PackageCategoryInfrastructure,
	"random":        pkg.PackageCategoryUtility,
	"rke":           pkg.PackageCategoryInfrastructure,
	"signalfx":      pkg.PackageCategoryMonitoring,
	"snowflake":     pkg.PackageCategoryInfrastructure,
	"splunk":        pkg.PackageCategoryInfrastructure,
	"spotinst":      pkg.PackageCategoryInfrastructure,
	"sumologic":     pkg.PackageCategoryMonitoring,
	"tls":           pkg.PackageCategoryUtility,
	"vault":         pkg.PackageCategoryInfrastructure,
	"venafi":        pkg.PackageCategoryInfrastructure,
	"vsphere":       pkg.PackageCategoryCloud,
	"wavefront":     pkg.PackageCategoryMonitoring,
	"yandex":        pkg.PackageCategoryCloud,
}

// TODO[pulumi/pulumi#7813]: Remove this lookup once display name is available in
// the Pulumi schema.
//
// NOTE: For the time being this lookup map and the one used by the docs
// generator in `pulumi/pulumi` must be kept up-to-date.
//
// titleLookup is a map pf package name to the desired display name
// for display in the TOC menu under API Reference.
var titleLookup = map[string]string{
	"aiven":         "Aiven",
	"akamai":        "Akamai",
	"alicloud":      "Alibaba Cloud",
	"auth0":         "Auth0",
	"aws":           "AWS Classic",
	"aws-native":    "AWS Native",
	"azure":         "Azure Classic",
	"azure-native":  "Azure Native",
	"azuread":       "Azure Active Directory",
	"azuredevops":   "Azure DevOps",
	"azuresel":      "Azure",
	"civo":          "Civo",
	"cloudamqp":     "CloudAMQP",
	"cloudflare":    "Cloudflare",
	"cloudinit":     "cloud-init",
	"confluent":     "Confluent Cloud",
	"consul":        "Consul",
	"datadog":       "Datadog",
	"digitalocean":  "DigitalOcean",
	"dnsimple":      "DNSimple",
	"docker":        "Docker",
	"eks":           "Amazon EKS",
	"equinix-metal": "Equinix Metal",
	"f5bigip":       "f5 BIG-IP",
	"fastly":        "Fastly",
	"gcp":           "Google Cloud Classic",
	"google-native": "Google Cloud Native",
	"github":        "GitHub",
	"gitlab":        "GitLab",
	"hcloud":        "Hetzner Cloud",
	"kafka":         "Kafka",
	"keycloak":      "Keycloak",
	"kong":          "Kong",
	"kubernetes":    "Kubernetes",
	"libvirt":       "libvirt",
	"linode":        "Linode",
	"mailgun":       "Mailgun",
	"minio":         "MinIO",
	"mongodbatlas":  "MongoDB Atlas",
	"mysql":         "MySQL",
	"newrelic":      "New Relic",
	"nomad":         "Nomad",
	"ns1":           "NS1",
	"okta":          "Okta",
	"openstack":     "OpenStack",
	"opsgenie":      "Opsgenie",
	"packet":        "Packet",
	"pagerduty":     "PagerDuty",
	"postgresql":    "PostgreSQL",
	"rabbitmq":      "RabbitMQ",
	"rancher2":      "Rancher 2",
	"random":        "random",
	"rke":           "Rancher RKE",
	"signalfx":      "SignalFx",
	"snowflake":     "Snowflake",
	"splunk":        "Splunk",
	"spotinst":      "Spotinst",
	"sumologic":     "Sumo Logic",
	"tls":           "TLS",
	"vault":         "Vault",
	"venafi":        "Venafi",
	"vsphere":       "vSphere",
	"wavefront":     "Wavefront",
	"yandex":        "Yandex",
}

func packageMetadataCmd() *cobra.Command {
	var metadataOutDir string
	var featured bool

	cmd := &cobra.Command{
		Use:   "metadata <metadataOutDir> [featured]",
		Short: "Generate package metadata only",
		RunE: func(cmd *cobra.Command, args []string) error {
			status := pkg.PackageStatusGA
			if strings.HasPrefix(version, "v0.") {
				status = pkg.PackageStatusPublicPreview
			}

			category := pkg.PackageCategoryCloud
			if c, ok := categoryLookup[mainSpec.Name]; ok {
				category = c
			}

			title := mainSpec.Name
			if v, ok := titleLookup[mainSpec.Name]; ok {
				title = v
			}
			pm := pkg.PackageMeta{
				Name:          mainSpec.Name,
				UpdatedOn:     time.Now().Unix(),
				Publisher:     "Pulumi",
				Title:         title,
				Description:   mainSpec.Description,
				Category:      category,
				PackageStatus: status,
				Featured:      featured,
				Native:        mainSpec.Attribution == "",
				Version:       version,
				LogoURL:       mainSpec.LogoURL,
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
