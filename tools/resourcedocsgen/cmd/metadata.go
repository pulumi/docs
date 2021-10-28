package cmd

import (
	"fmt"
	"strings"
	"time"

	"github.com/golang/glog"

	"github.com/pkg/errors"

	"github.com/spf13/cobra"

	"gopkg.in/yaml.v2"

	pschema "github.com/pulumi/pulumi/pkg/v3/codegen/schema"

	"github.com/pulumi/docs/tools/resourcedocsgen/pkg"
)

const defaultPackageCategory = pkg.PackageCategoryCloud

var categoryNameMap = map[string]pkg.PackageCategory{
	"cloud":          pkg.PackageCategoryCloud,
	"database":       pkg.PackageCategoryDatabase,
	"infrastructure": pkg.PackageCategoryInfrastructure,
	"monitoring":     pkg.PackageCategoryMonitoring,
	"network":        pkg.PackageCategoryNetwork,
	"utility":        pkg.PackageCategoryUtility,
	"vcs":            pkg.PackageCategoryVCS,
}

var categoryLookup = map[string]pkg.PackageCategory{
	"aiven":                               pkg.PackageCategoryInfrastructure,
	"akamai":                              pkg.PackageCategoryNetwork,
	"alicloud":                            pkg.PackageCategoryCloud,
	"auth0":                               pkg.PackageCategoryInfrastructure,
	"aws":                                 pkg.PackageCategoryCloud,
	"aws-apigateway":                      pkg.PackageCategoryCloud,
	"aws-miniflux":                        pkg.PackageCategoryCloud,
	"aws-native":                          pkg.PackageCategoryCloud,
	"aws-quickstart-aurora-mysql":         pkg.PackageCategoryCloud,
	"aws-quickstart-aurora-postgresql":    pkg.PackageCategoryCloud,
	"aws-quickstart-redshift":             pkg.PackageCategoryCloud,
	"aws-serverless":                      pkg.PackageCategoryCloud,
	"aws-quickstart-vpc":                  pkg.PackageCategoryCloud,
	"aws-s3-replicated-bucket":            pkg.PackageCategoryCloud,
	"azure":                               pkg.PackageCategoryCloud,
	"azure-native":                        pkg.PackageCategoryCloud,
	"azure-quickstart-acr-geo-replicated": pkg.PackageCategoryCloud,
	"azure-quickstart-aks":                pkg.PackageCategoryCloud,
	"azure-quickstart-compute":            pkg.PackageCategoryCloud,
	"azure-quickstart-sql":                pkg.PackageCategoryCloud,
	"azuread":                             pkg.PackageCategoryInfrastructure,
	"azuredevops":                         pkg.PackageCategoryInfrastructure,
	"civo":                                pkg.PackageCategoryCloud,
	"cloudamqp":                           pkg.PackageCategoryCloud,
	"cloudflare":                          pkg.PackageCategoryNetwork,
	"cloudinit":                           pkg.PackageCategoryUtility,
	"confluent":                           pkg.PackageCategoryInfrastructure,
	"consul":                              pkg.PackageCategoryInfrastructure,
	"coredns-helm":                        pkg.PackageCategoryNetwork,
	"datadog":                             pkg.PackageCategoryMonitoring,
	"digitalocean":                        pkg.PackageCategoryCloud,
	"dnsimple":                            pkg.PackageCategoryNetwork,
	"docker":                              pkg.PackageCategoryInfrastructure,
	"docker-buildkit":                     pkg.PackageCategoryInfrastructure,
	"eks":                                 pkg.PackageCategoryCloud,
	"equinix-metal":                       pkg.PackageCategoryCloud,
	"f5bigip":                             pkg.PackageCategoryNetwork,
	"fastly":                              pkg.PackageCategoryCloud,
	"gcp":                                 pkg.PackageCategoryCloud,
	"gcp-cloudrun-multi-region":           pkg.PackageCategoryCloud,
	"gcp-project-scaffold":                pkg.PackageCategoryCloud,
	"google-native":                       pkg.PackageCategoryCloud,
	"github":                              pkg.PackageCategoryVCS,
	"github-serverless-webhook":           pkg.PackageCategoryVCS,
	"gitlab":                              pkg.PackageCategoryVCS,
	"hcloud":                              pkg.PackageCategoryCloud,
	"istio-helm":                          pkg.PackageCategoryInfrastructure,
	"jaeger-helm":                         pkg.PackageCategoryMonitoring,
	"kafka":                               pkg.PackageCategoryInfrastructure,
	"keycloak":                            pkg.PackageCategoryInfrastructure,
	"kong":                                pkg.PackageCategoryInfrastructure,
	"kubernetes":                          pkg.PackageCategoryCloud,
	"libvirt":                             pkg.PackageCategoryUtility,
	"linode":                              pkg.PackageCategoryCloud,
	"mailgun":                             pkg.PackageCategoryInfrastructure,
	"minio":                               pkg.PackageCategoryInfrastructure,
	"mongodbatlas":                        pkg.PackageCategoryDatabase,
	"mysql":                               pkg.PackageCategoryDatabase,
	"newrelic":                            pkg.PackageCategoryMonitoring,
	"nginx-ingress-controller-helm":       pkg.PackageCategoryNetwork,
	"nomad":                               pkg.PackageCategoryInfrastructure,
	"ns1":                                 pkg.PackageCategoryNetwork,
	"okta":                                pkg.PackageCategoryInfrastructure,
	"onelogin":                            pkg.PackageCategoryInfrastructure,
	"openstack":                           pkg.PackageCategoryCloud,
	"opsgenie":                            pkg.PackageCategoryInfrastructure,
	"pagerduty":                           pkg.PackageCategoryInfrastructure,
	"postgresql":                          pkg.PackageCategoryDatabase,
	"prometheus-helm":                     pkg.PackageCategoryMonitoring,
	"rabbitmq":                            pkg.PackageCategoryInfrastructure,
	"rancher2":                            pkg.PackageCategoryInfrastructure,
	"random":                              pkg.PackageCategoryUtility,
	"rke":                                 pkg.PackageCategoryInfrastructure,
	"shipa":                               pkg.PackageCategoryCloud,
	"signalfx":                            pkg.PackageCategoryMonitoring,
	"snowflake":                           pkg.PackageCategoryInfrastructure,
	"splunk":                              pkg.PackageCategoryInfrastructure,
	"spotinst":                            pkg.PackageCategoryInfrastructure,
	"sumologic":                           pkg.PackageCategoryMonitoring,
	"tls":                                 pkg.PackageCategoryUtility,
	"vault":                               pkg.PackageCategoryInfrastructure,
	"venafi":                              pkg.PackageCategoryInfrastructure,
	"vsphere":                             pkg.PackageCategoryCloud,
	"wavefront":                           pkg.PackageCategoryMonitoring,
	"yandex":                              pkg.PackageCategoryCloud,
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
	"aiven":                               "Aiven",
	"akamai":                              "Akamai",
	"alicloud":                            "Alibaba Cloud",
	"auth0":                               "Auth0",
	"aws":                                 "AWS Classic",
	"aws-apigateway":                      "AWS API Gateway",
	"aws-miniflux":                        "Miniflux",
	"aws-native":                          "AWS Native",
	"aws-quickstart-aurora-mysql":         "AWS QuickStart Aurora MySQL",
	"aws-quickstart-aurora-postgresql":    "AWS QuickStart Aurora PostgreSQL",
	"aws-quickstart-redshift":             "AWS QuickStart Redshift",
	"aws-serverless":                      "AWS Serverless",
	"aws-quickstart-vpc":                  "AWS QuickStart VPC",
	"aws-s3-replicated-bucket":            "AWS S3 Replicated Bucket",
	"azure":                               "Azure Classic",
	"azure-native":                        "Azure Native",
	"azure-quickstart-acr-geo-replicated": "Azure QuickStart ACR Geo Replicated",
	"azure-quickstart-aks":                "Azure QuickStart AKS",
	"azure-quickstart-compute":            "Azure QuickStart Compute",
	"azure-quickstart-sql":                "Azure QuickStart SQL",
	"azuread":                             "Azure Active Directory",
	"azuredevops":                         "Azure DevOps",
	"azuresel":                            "Azure",
	"civo":                                "Civo",
	"cloudamqp":                           "CloudAMQP",
	"cloudflare":                          "Cloudflare",
	"cloudinit":                           "cloud-init",
	"confluent":                           "Confluent Cloud",
	"consul":                              "Consul",
	"coredns-helm":                        "CoreDNS (Helm)",
	"datadog":                             "Datadog",
	"digitalocean":                        "DigitalOcean",
	"dnsimple":                            "DNSimple",
	"docker":                              "Docker",
	"docker-buildkit":                     "Docker BuildKit",
	"eks":                                 "Amazon EKS",
	"equinix-metal":                       "Equinix Metal",
	"f5bigip":                             "f5 BIG-IP",
	"fastly":                              "Fastly",
	"gcp":                                 "Google Cloud Classic",
	"gcp-cloudrun-multi-region":           "Google Cloud Run Multi-Region",
	"gcp-project-scaffold":                "Google Project Scaffolding",
	"google-native":                       "Google Cloud Native",
	"github":                              "GitHub",
	"github-serverless-webhook":           "GitHub Serverless Webhook",
	"gitlab":                              "GitLab",
	"hcloud":                              "Hetzner Cloud",
	"istio-helm":                          "Istio (Helm)",
	"jaeger-helm":                         "Jaeger (Helm)",
	"kafka":                               "Kafka",
	"keycloak":                            "Keycloak",
	"kong":                                "Kong",
	"kubernetes":                          "Kubernetes",
	"libvirt":                             "libvirt",
	"linode":                              "Linode",
	"mailgun":                             "Mailgun",
	"minio":                               "MinIO",
	"mongodbatlas":                        "MongoDB Atlas",
	"mysql":                               "MySQL",
	"newrelic":                            "New Relic",
	"nginx-ingress-controller-helm":       "NGINX Ingress Controller (Helm)",
	"nomad":                               "Nomad",
	"ns1":                                 "NS1",
	"okta":                                "Okta",
	"openstack":                           "OpenStack",
	"opsgenie":                            "Opsgenie",
	"packet":                              "Packet",
	"pagerduty":                           "PagerDuty",
	"postgresql":                          "PostgreSQL",
	"prometheus-helm":                     "Prometheus (Helm)",
	"rabbitmq":                            "RabbitMQ",
	"rancher2":                            "Rancher 2",
	"random":                              "random",
	"rke":                                 "Rancher RKE",
	"shipa":                               "Shipa",
	"signalfx":                            "SignalFx",
	"snowflake":                           "Snowflake",
	"splunk":                              "Splunk",
	"spotinst":                            "Spotinst",
	"sumologic":                           "Sumo Logic",
	"tls":                                 "TLS",
	"vault":                               "Vault",
	"venafi":                              "Venafi",
	"vsphere":                             "vSphere",
	"wavefront":                           "Wavefront",
	"yandex":                              "Yandex",
}

func packageMetadataCmd() *cobra.Command {
	var metadataOutDir string
	var categoryStr string
	var component bool
	var featured bool
	var publisher string
	var title string
	var updatedOn int64

	cmd := &cobra.Command{
		Use:   "metadata <metadataOutDir> [featured]",
		Short: "Generate package metadata from Pulumi schema",
		RunE: func(cmd *cobra.Command, args []string) error {
			status := pkg.PackageStatusGA
			if strings.HasPrefix(version, "v0.") {
				status = pkg.PackageStatusPublicPreview
			}

			category, err := getPackageCategory(mainSpec, categoryStr)
			if err != nil {
				return errors.Wrap(err, "getting category")
			}

			// If the title was not overridden, then try to determine
			// the title from the schema.
			if title == "" {
				// If the schema for this package does not have the
				// displayName, then use its package name.
				if mainSpec.DisplayName == "" {
					title = mainSpec.Name
					// Eventually all of Pulumi's own packages will have the displayName
					// set in their schema but for the time being until they are updated
					// with that info, let's lookup the proper title from the lookup map.
					if v, ok := titleLookup[mainSpec.Name]; ok {
						title = v
					}
				} else {
					title = mainSpec.DisplayName
				}
			}

			native := isNative(mainSpec.Keywords)

			if !component {
				component = isComponent(mainSpec.Keywords)
			}

			if native && component {
				msg := fmt.Sprintf("package %q cannot be tagged as both native and component. only one is applicable", mainSpec.Name)
				return errors.New(msg)
			}

			if publisher == "" && mainSpec.Publisher != "" {
				publisher = mainSpec.Publisher
			} else if publisher == "" {
				publisher = "Pulumi"
			}

			pm := pkg.PackageMeta{
				Name:          mainSpec.Name,
				UpdatedOn:     updatedOn,
				Publisher:     publisher,
				Title:         title,
				Description:   mainSpec.Description,
				Category:      category,
				PackageStatus: status,
				Component:     component,
				Featured:      featured,
				Native:        native,
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
	cmd.Flags().StringVar(&categoryStr, "category", "", fmt.Sprintf("The category for the package. Value must match one of the keys in the map: %v", categoryNameMap))
	cmd.Flags().BoolVar(&featured, "featured", false, "Whether or not this package should be marked as featured in its metadata")
	cmd.Flags().StringVar(&publisher, "publisher", "", "The publisher's display name to be shown in the package")
	cmd.Flags().StringVar(&title, "title", "", "The display name of the package. If ommitted, the name of the package will be used")
	cmd.Flags().Int64Var(&updatedOn, "updatedOn", time.Now().Unix(), "The timestamp (epoch) to use for when the package was last updated")
	cmd.Flags().BoolVar(&component, "component", false, "Whether or not this package is a component and not a provider")

	cmd.MarkFlagRequired("metadataOutDir")

	return cmd
}

func getPackageCategory(mainSpec *pschema.PackageSpec, categoryOverrideStr string) (pkg.PackageCategory, error) {
	var category pkg.PackageCategory
	var err error

	// If a category override was passed-in, use that instead of what's in the schema.
	if categoryOverrideStr != "" {
		glog.V(2).Infof("Using category override name %s\n", categoryOverrideStr)
		if n, ok := categoryNameMap[categoryOverrideStr]; !ok {
			return "", errors.New(fmt.Sprintf("invalid override for category name %s", categoryOverrideStr))
		} else {
			category = n
		}
	} else if c, ok := categoryLookup[mainSpec.Name]; ok {
		glog.V(2).Infoln("Using the category for this package from the lookup map")
		// TODO: This condition can be removed when all packages under the `pulumi` org
		// have a proper category tag in their schema.
		category = c
	}

	if category != "" {
		return category, nil
	}

	glog.V(2).Infoln("Looking-up category from the keywords in the schema")
	category, err = getCategoryFromKeywords(mainSpec.Keywords)
	if err != nil {
		return "", errors.Wrap(err, "getting the category from keywords")
	}

	return category, nil
}

// getCategoryFromKeywords searches for a tag in the provided keywords slice
// with a prefix of category/. Returns the converted category type if such a tag
// is found. Otherwise, returns PackageCategoryCloud always as the default.
func getCategoryFromKeywords(keywords []string) (pkg.PackageCategory, error) {
	categoryTag := getTagWithPrefixFromKeywords(keywords, "category/")
	if categoryTag == nil {
		return defaultPackageCategory, nil
	}

	categoryName := strings.Replace(*categoryTag, "category/", "", -1)
	var category pkg.PackageCategory
	if n, ok := categoryNameMap[categoryName]; !ok {
		return defaultPackageCategory, errors.New(fmt.Sprintf("invalid category tag %s", *categoryTag))
	} else {
		category = n
	}

	return category, nil
}

func isComponent(keywords []string) bool {
	return getTagFromKeywords(keywords, "kind/component") != nil
}

func isNative(keywords []string) bool {
	return getTagFromKeywords(keywords, "kind/native") != nil
}

func getTagWithPrefixFromKeywords(keywords []string, tagPrefix string) *string {
	for _, k := range keywords {
		if strings.HasPrefix(k, tagPrefix) {
			return &k
		}
	}

	glog.V(2).Infof("A tag with the prefix %q was not found in the package's keywords", tagPrefix)
	return nil
}

func getTagFromKeywords(keywords []string, tag string) *string {
	for _, k := range keywords {
		if k == tag {
			return &k
		}
	}

	glog.V(2).Infof("The tag %q was not found in the package's keywords", tag)
	return nil
}
