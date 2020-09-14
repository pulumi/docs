---
title: Cloud Engineering on Azure
layout: azure
url: /azure

meta_desc: Cloud Engineering on the Azure cloud with Pulumi for huge productivity gains and a unified programming model for developers and operators.

hero:
    title: Cloud Engineering on Azure
    description: |
        Pulumi's infrastructure as code SDK helps create, deploy, and manage Microsoft Azure containers, serverless functions, and infrastructure using real programming languages.
    cta_text: See What's New
    cta_url: "/blog/new-kubernetes-superpowers"
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as azure from "@pulumi/azure";

                // Create a resource group
                const exampleResourceGroup = new azure.core.ResourceGroup("exampleResourceGroup", {
                    location: "West Europe"
                });

                // Create a virtual network within the resource group
                const exampleVirtualNetwork = new azure.network.VirtualNetwork("exampleVirtualNetwork", {
                    resourceGroupName: exampleResourceGroup.name,
                    location: exampleResourceGroup.location,
                    addressSpaces: ["10.0.0.0/16"],
                });
            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_azure as azure

                # Create a resource group
                example_resource_group = azure.core.ResourceGroup("exampleResourceGroup", location="West Europe")

                # Create a virtual network within the resource group
                example_virtual_network = azure.network.VirtualNetwork("exampleVirtualNetwork",
                    resource_group_name=example_resource_group.name,
                    location=example_resource_group.location,
                    address_spaces=["10.0.0.0/16"])
            - title: main.go
              language: go
              code: |
                    package main

                    import (
                        "github.com/pulumi/pulumi-azure/sdk/v3/go/azure/core"
                        "github.com/pulumi/pulumi-azure/sdk/v3/go/azure/network"
                        "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                    )

                    func main() {
                        pulumi.Run(func(ctx *pulumi.Context) error {
                            exampleResourceGroup, err := core.NewResourceGroup(ctx, "exampleResourceGroup", &core.ResourceGroupArgs{
                                Location: pulumi.String("West Europe"),
                            })
                            if err != nil {
                                return err
                            }
                            _, err = network.NewVirtualNetwork(ctx, "exampleVirtualNetwork", &network.VirtualNetworkArgs{
                                ResourceGroupName: exampleResourceGroup.Name,
                                Location:          exampleResourceGroup.Location,
                                AddressSpaces: pulumi.StringArray{
                                    pulumi.String("10.0.0.0/16"),
                                },
                            })
                            if err != nil {
                                return err
                            }
                            return nil
                        })
                    }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Azure = Pulumi.Azure;

                class MyStack : Stack
                {
                    public MyStack()
                    {
                        // Create a resource group
                        var exampleResourceGroup = new Azure.Core.ResourceGroup("exampleResourceGroup", new Azure.Core.ResourceGroupArgs
                        {
                            Location = "West Europe",
                        });
                        // Create a virtual network within the resource group
                        var exampleVirtualNetwork = new Azure.Network.VirtualNetwork("exampleVirtualNetwork", new Azure.Network.VirtualNetworkArgs
                        {
                            ResourceGroupName = exampleResourceGroup.Name,
                            Location = exampleResourceGroup.Location,
                            AddressSpaces =
                            {
                                "10.0.0.0/16",
                            },
                        });
                    }

                }

azure_overview:
  title: Cloud Engineering on Azure
  list:
    - Define infrastructure in JavaScript, TypeScript, Python, Go, or any .NET language, including C#, F#, and VB.
    - Increase your productivity using the full ecosystem of dev tools such as IDE auto-completion, type & error checking, linting, refactoring, and test frameworks to validate all your Azure resources.
    - Keep your cloud clean and secure by enforcing policies on every deployment.
    - Codify best practices and policies then share them with your team or community as self-service architectures.
  cta: Learn More
  cta_url: "/blog/new-kubernetes-superpowers"

detail_sections:
  - title: 100% API Coverage
    description: |
        The Pulumi Azure provider covers 100% of the resources available in Azure
        Resource Manager.
    cta: Learn More
    cta_url: "/blog/new-kubernetes-superpowers"
    items:
        - title: Everything In One Place
          description: The SDKs include full coverage for Azure services, includinglike Azure Static Web Apps, Azure Synapse Analytics, Azure Logic Apps, Azure Service Fabric, Azure Blockchain Service, Azure API Management, and dozens of other services.
          icon: fa-tools

        - title: Efficient Adoption
          description: There’s no need to rewrite your existing Azure configurations to get started with Pulumi. You can efficiently adopt existing Azure resources to deploy your application to save time and effort.
          icon: fa-book

        - title: Secrets Management
          description: Use Pulumi to ensure secret data is encrypted in transit, at rest, and physically anywhere it gets stored. Bring your own preferred cloud encryption provider or use Pulumi's native secrets provider.
          icon: fa-key

        - title: Convenience Functions
          description: The provider also contains functions to retrieve keys, secrets, and connection strings from all resources that expose them.
          icon: fa-people-carry

  - title: Always Up To Date
    description: |
        The provider is designed to be always up to date with additions and changes
        to Azure APIs.
    cta: Learn More
    cta_url: "/docs/guides/crosswalk/kubernetes"
    items:
        - title: Auto Generated
          description: We generate Pulumi SDKs for `azurerm` automatically from Azure API specifications published by Microsoft. An automated pipeline releases updated resources within hours after any current API specifications are merged.
          icon: fa-sun

        - title: Familiar Concepts
          description: Azure Resource Manager API is structured around Resource Providers &mdash; high-level groups like "storage", "compute", or "web". We map Resource Providers to top-level modules or namespaces in Pulumi SDKs.
          icon: fa-users

        - title: API Versions
          description: Each resource provider defines one or more API versions, for example, "2015-05-01", "2020-09-01", or "2020-08-01-preview". Every version of every ARM API is available in Pulumi SDKs, and each version has its own module or namespace.
          icon: fa-chalkboard-teacher

        - title: All Languages
          description: The Pulumi Azure provider is available in all Pulumi languages. The SDKs are open source on GitHub and available in NPM, NuGet, PyPI, and Go Modules.
          icon: fa-pager

superpowers:
  - title: Multi Cloud
    cta: Learn more
    cta_url: "/docs/get-started/azure"
    icon_type: cloud
    description: |
        Pulumi gives you the power to work seamlessly with other cloud
        providers helping ensure any multi cloud strategy is a successful one.

  - title: Reduce Provisioning Time
    cta: Learn more
    cta_url: "/docs/get-started/azure"
    icon_type: provisioning
    description: |
        With Pulumi you are able to take advantage of the features of programming languages,
        helping you reduce boilerplate code and ultimately ship Azure infrastructure and
        applications faster with greater consistency.

  - title: Automate Delivery
    cta: Learn more
    cta_url: "/docs/guides/continuous-delivery"
    icon_type: delivery
    description: |
        You can integrate Pulumi directly with your favorite CI/CD and SCM systems to
        continuously deliver Azure infrastructure and applications. Improve the velocity
        and visibility into your deployments from simple to complex global environments.

  - title: Smart Architecture
    cta: Learn more
    cta_url: "/docs/intro/concepts"
    icon_type: architecture
    description: |
        YAML and templated DSLs force you to write the same boilerplate code over and over.
        Pulumi’s Azure libraries allows you to codify those patterns and best practices so
        you can stop reinventing the wheel and start inventing the platforms of the future.

  - title: Be Proactive, Not Reactive
    cta: Learn more
    cta_url: "/docs/guides/crossguard"
    icon_type: policy
    description: |
        When you enable Pulumi's Policy as Code feature, you instantly gain the power to
        prevent mistakes from being deployed. Enforce security, compliance, cost controls,
        and best practices using policies defined in modern languages.

  - title: Reduce Deployment Complexity
    cta: Learn more
    cta_url: "/docs/guides/testing"
    icon_type: testing
    description: |
        Deploying untested code can lead to some unexpected results. Pulumi lets you take advantage
        of common tools, frameworks, and techniques to unit, integration, and property test your
        Azure infrastructure. Ensure your infrastructure is correct before and after deployment.

contact_us_form:
    section_id: contact-us
    hubspot_form_id: 826f708b-53a9-4abc-9cb9-950f47362b72
    headline: Need help with cloud-native infrastructure as code on Azure?
    quote:
        title: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage Azure resources.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
