---
title: Modern Infrastructure as Code for Microsoft Azure | Pulumi
layout: azure
url: /azure

meta_desc: Modern Infrastructure as Code on the Azure cloud with Pulumi gives you huge productivity gains and a unified programming model for developers and operators.

hero:
    title: Modern Infrastructure as Code for 100% of Microsoft Azure
    description: |
        Pulumi's [infrastructure as code](/what-is/what-is-infrastructure-as-code/) SDK
        helps create, deploy, and manage 100% of your Microsoft Azure infrastructure, including
        containers, serverless functions, and infrastructure using modern programming languages.
    cta_text: See what's new
    cta_url: "/blog/full-coverage-of-azure-resources-with-azure-native"
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as resources from "@pulumi/azure-native/resources";
                import * as storage from "@pulumi/azure-native/storage";

                const resourceGroup = new resources.ResourceGroup("resourceGroup");

                const storageAccount = new storage.StorageAccount("sa", {
                    resourceGroupName: resourceGroup.name,
                    sku: {
                        name: "Standard_LRS",
                    },
                    kind: "StorageV2",
                });
            - title: __main__.py
              language: python
              code: |
                from pulumi_azure_native import storage
                from pulumi_azure_native import resources

                resource_group = resources.ResourceGroup('resource_group')

                account = storage.StorageAccount('sa',
                    resource_group_name=resource_group.name,
                    sku=storage.SkuArgs(name='Standard_LRS'),
                    kind='StorageV2')
            - title: main.go
              language: go
              code: |
                package main

                import (
                    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
                    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
                    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                )

                func main() {
                    pulumi.Run(func(ctx *pulumi.Context) error {
                        resourceGroup, err := resources.NewResourceGroup(ctx, "resourceGroup", nil)
                        if err != nil {
                            return err
                        }

                        account, err := storage.NewStorageAccount(ctx, "sa", &storage.StorageAccountArgs{
                            ResourceGroupName: resourceGroup.Name,
                            Sku: &storage.SkuArgs{
                                Name: pulumi.String("Standard_LRS"),
                            },
                            Kind: pulumi.String("StorageV2"),
                        })

                        return err
                    })
                }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.AzureNative.Resources;
                using Pulumi.AzureNative.Storage;
                using Pulumi.AzureNative.Storage.Inputs;

                class MyStack : Stack
                {
                    public MyStack()
                    {
                        var resourceGroup = new ResourceGroup("resourceGroup");

                        var storageAccount = new StorageAccount("sa", new StorageAccountArgs
                        {
                            ResourceGroupName = resourceGroup.Name,
                            Sku = new SkuArgs { Name = "Standard_LRS" },
                            Kind = "StorageV2"
                        });
                    }
                }

azure_overview:
  title: Modern Infrastructure as Code on Azure
  list:
    - Define infrastructure in JavaScript, TypeScript, Python, Go, or any .NET language, including C#, F#, and VB.
    - Increase your productivity using the full ecosystem of dev tools such as IDE auto-completion, type & error checking, linting, refactoring, and test frameworks to validate all of your Azure resources.
    - Keep your cloud secure and in compliance by enforcing policies on every deployment.
    - Codify best practices and policies then share them with your team or community as self-service architectures.
  cta: Learn More
  cta_url: "/blog/full-coverage-of-azure-resources-with-azure-native"

arm2pulumi:
  title: ARM &rarr; Pulumi
  description: |
    Whether you're new to Microsoft Azure or already using it to manage your infrastructure, Pulumi makes getting started easy. If you're just starting out, you can write your infrastructure code using the Pulumi Azure SDK. Or if you're already managing resources with Azure, you can deploy an existing ARM template using Pulumi or you can rewrite the ARM template JSON in a programming language, either entirely, or one resource at a time.

    If you can deploy a resource with ARM templates, you can deploy it with the Pulumi Azure provider!

  cta: Learn More
  cta_url: "/docs/guides/adopting/from_azure"

detail_sections:
  - title: 100% API Coverage
    description: |
        The Pulumi Azure provider covers 100% of the resources available in Azure
        Resource Manager giving you the full power of Azure at your fingertips. Every
        property of each resource is always represented in the SDKs.
    cta: Learn More
    cta_url: "/blog/full-coverage-of-azure-resources-with-azure-native"
    items:
        - title: Everything In One Place
          icon: cloud-with-nodes
          icon_color: violet
          description: The SDKs include full coverage for Azure services, including Azure Static Web Apps, Azure Synapse Analytics, Azure Logic Apps, Azure Service Fabric, Azure Blockchain Service, Azure API Management, and dozens of other services.

        - title: Efficient Adoption
          icon: lightning
          icon_color: yellow
          description: There’s no need to rewrite your existing Azure configurations to get started with Pulumi. You can efficiently adopt existing Azure resources to deploy your application to yourself save time and effort.

        - title: Secrets Management
          icon: security
          icon_color: salmon
          description: Use Pulumi to ensure secret data is encrypted in transit, at rest, and physically anywhere it gets stored. Bring your own preferred cloud encryption provider or use Pulumi's native secrets provider.

        - title: Convenience Functions
          icon: pen
          icon_color: fuchsia
          description: The provider also contains functions to retrieve keys, secrets, and connection strings from all resources that expose them.

  - title: Always Up to Date
    description: |
        Pulumi's Microsoft Azure provider is designed to stay up-to-date with additions and changes
        to Azure APIs. The `azure-native` SDK is generated automatically from the Azure API
        specifications published by Microsoft, which means you'll always have access to the latest
        Azure features and improvements.
    cta: Learn More
    cta_url: "/blog/full-coverage-of-azure-resources-with-azure-native"
    items:
        - title: Auto Generated
          icon: cycle
          icon_color: blue
          description: An automated pipeline releases updated resources within hours after any current API specifications are merged. Auto generated means less manual implementation and fewer chances for bugs, meaning a high fidelity, high quality experience.

        - title: Familiar Concepts
          icon: collab
          icon_color: purple
          description: Azure Resource Manager API is structured around Resource Providers &mdash; high-level groups like `storage`, `compute`, or `web`. We map Resource Providers to top-level modules or namespaces in Pulumi SDKs.

        - title: API Versions
          icon: nodes
          icon_color: salmon
          description: Each resource provider defines one or more API versions, for example, `2015-05-01`, `2020-09-01`, or `2020-08-01-preview`. Every version of every ARM API is available in Pulumi SDKs, and each version has its own module or namespace.

        - title: All Languages
          icon: code
          icon_color: yellow
          description: The Pulumi Azure provider is available in all Pulumi languages, including JavaScript, TypeScript, Python, Go, and .NET Core. All SDKs are open source on GitHub and available as npm, NuGet, PyPI, and Go modules.

superpowers:
  - title: Multi Cloud
    cta: Learn more
    cta_url: "/docs/get-started/azure"
    icon_type: cloud
    description: |
        Pulumi allows you to use top programming languages across all public clouds with support
        for dozens of popular infrastructure service providers including private and hybrid clouds
        helping ensure any multi-cloud strategy is succesful one.

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
    headline: Need help with Azure?
    quote:
        title: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage Azure resources.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
