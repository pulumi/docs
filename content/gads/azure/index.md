---
title: "Azure Infrastructure"
meta_desc: Infrastructure as Code in any programming language. Enable your team to get code to any cloud productively, securely, and reliably.
layout: gads-template
block_external_search_index: true
aliases:
    - /azure-resource-manager
    - /azure-infrastructure

heading: "Tame Azure with Code"
subheading: |
    Pulumi is a free, open source infrastructure as code tool, and works best with Pulumi Cloud to make managing infrastructure secure, reliable, and hassle-free.

overview:
    title: Infrastructure as Code<br/>in any Programming Language
    description: |
        Pulumi Cloud is the smartest and easiest way to automate, secure, and manage everything you run in the cloud using programming languages you know and love.

key_features_above:
    items:
        - title: "Azure Infrastructure you can Write, Reuse, and Test"
          sub_title: "Turn Azure Best Practices into Reusable Code"
          description: |
            Write IaC in the languages you know, such as C#, TypeScript, Python, Go, Java, or YAML. Pulumi manages 100% of your Azure resources, from containers to serverless. Go further with **components**: modular, reusable building blocks that cut down copy-paste and simplify your architecture. Write once, deploy anywhere → Build your first component in minutes.
          ide:
            - title: C#
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.AzureNative.Storage;
                using Pulumi.AzureNative.Storage.Inputs;
                
                class MyStack : Stack
                {
                    public MyStack()
                    {
                      var config = new Config();
                      var resourceGroupNameParam = config.Require("resourceGroupNameParam");
                      var storagecreatedbyarm = new StorageAccount("mystorage", 
                      new StorageAccountArgs
                      {
                          AccountName = "mystorage",
                          Kind = "StorageV2",
                          Location = "westeurope",
                          ResourceGroupName = resourceGroupNameParam,
                          Sku = new SkuArgs
                          {
                              Name = "Standard_LRS",
                          },
                      });
                    }
                }
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
        
key_features:
    title: Key features
    items:
        - title: "Azure Resource Manager → Pulumi"
          sub_title: "Move from static JSON to reusable code"
          description: |
           Many Azure teams hit a wall with ARM templates. Pulumi provides a flexible, code-first alternative using your favorite language. Get full IDE support, CI/CD integration, reusable components, modern workflows, and testability. For .NET teams, Pulumi’s C# support delivers a far better experience than static JSON.
          ide:
            - title: C#
              language: csharp
              code: |
                using Pulumi;
                using AzureNative = Pulumi.AzureNative;
                
                class MyStack : Stack
                {
                    public MyStack()
                    {
                        var config = new Config();
                        var resourceGroupNameParam = config.Require("resourceGroupNameParam");
                        var storagecreatedbyarm = new AzureNative.Storage.StorageAccount("storagecreatedbyarm", new AzureNative.Storage.StorageAccountArgs
                        {
                            AccountName = "storagecreatedbyarm",
                            Kind = "StorageV2",
                            Location = "westeurope",
                            ResourceGroupName = resourceGroupNameParam,
                            Sku = new AzureNative.Storage.Inputs.SkuArgs
                            {
                                Name = "Standard_LRS",
                            },
                        });
                    }
                }
            - title: typescript
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as azure_native from "@pulumi/azure-native";
                
                const config = new pulumi.Config();
                const resourceGroupNameParam = config.require("resourceGroupNameParam");
                const storagecreatedbyarm = new azure_native.storage.StorageAccount("storagecreatedbyarm", {
                    accountName: "storagecreatedbyarm",
                    kind: "StorageV2",
                    location: "westeurope",
                    resourceGroupName: resourceGroupNameParam,
                    sku: {
                        name: "Standard_LRS",
                    },
                });
            - title: go
              language: go
              code: |
                package main
                
                import (
                	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/storage"
                	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
                	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
                )
                
                func main() {
                	pulumi.Run(func(ctx *pulumi.Context) error {
                		cfg := config.New(ctx, "")
                		resourceGroupNameParam := cfg.Require("resourceGroupNameParam")
                		_, err := storage.NewStorageAccount(ctx, "storagecreatedbyarm", &storage.StorageAccountArgs{
                			AccountName:       pulumi.String("storagecreatedbyarm"),
                			Kind:              pulumi.String("StorageV2"),
                			Location:          pulumi.String("westeurope"),
                			ResourceGroupName: pulumi.String(resourceGroupNameParam),
                			Sku: &storage.SkuArgs{
                				Name: pulumi.String("Standard_LRS"),
                			},
                		})
                		if err != nil {
                			return err
                		}
                		return nil
                	})
                }


            - title: python
              language: python
              code: |
                import pulumi
                import pulumi_azure_native as azure_native
                
                config = pulumi.Config()
                resource_group_name_param = config.require("resourceGroupNameParam")
                storagecreatedbyarm = azure_native.storage.StorageAccount("storagecreatedbyarm",
                    account_name="storagecreatedbyarm",
                    kind="StorageV2",
                    location="westeurope",
                    resource_group_name=resource_group_name_param,
                    sku=azure_native.storage.SkuArgs(
                        name="Standard_LRS",
                    ))
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: 100% API Coverage
                description: |
                    Full API coverage for Azure with same-day updates. Every property of each resource is always represented in the SDKs.
              - title: Policy as Code for Azure
                description: |
                    Set guardrails for resources to ensure best practices and security compliance are consistently followed, using [Pulumi Policies](/docs/insights/policy/).
              - title: Everything In One Place
                description: |
                    Full coverage for Azure services, including Azure Static Web Apps, Azure Logic Apps, Azure DevOps, Azure Blockchain Service, Azure API Management and more.

        - title: "Deliver infrastructure through software delivery pipelines"
          sub_title: "CI/CD Integrations"
          description: |
            Version, review, test, and deploy infrastructure code through the same tools and processes used for your application code.
          image: "/images/product/pulumi-cicd.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: Version and review
                description: |
                    Manage infrastructure code in Git and approve changes through pull requests.
              - title: Shift left
                description: |
                    Get rapid feedback on your code with fast [unit tests](/docs/iac/concepts/testing/unit/), and run [integration tests](/docs/iac/concepts/testing/integration/) against ephemeral infrastructure.
              - title: Continuous delivery
                description: |
                    [Integrate your CI/CD provider](/docs/iac/packages-and-automation/continuous-delivery/) with Pulumi or use GitOps to [manage Kubernetes clusters](/docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/).

stats:
    title: Open source. Enterprise-ready.
    description: |
        Pulumi's Infrastructure as Code CLI and SDK is an [open-source project](https://github.com/pulumi/) that's supported
        by an active community. We maintain a [public roadmap](https://github.com/orgs/pulumi/projects/44) and welcome feedback and contributions.
    community:
        number: "350,000+"
        description: engineers building with Pulumi
    company:
        number: "3,700+"
        description: companies in production
    integration:
        number: "1,000s"
        description: of cloud and service providers

key_features_below:
    items:
        - title: "The fastest and easiest way to use Pulumi IaC at scale"
          sub_title: "Pulumi Cloud"
          description: |
             A fully-managed service for Pulumi IaC plus so much more. Manage and store infrastructure state & secrets, collaborate within teams, view and search infrastructure, and manage security and compliance using Pulumi Cloud.
          image: "/images/product/pulumi-cloud-iac-stylized-01.png"
          button:
            text: "Try Pulumi Cloud for FREE"
            link: "https://app.pulumi.com/signup"
          features:
              - title: Pulumi IaC
                description: |
                    Utilize open-source IaC in C#, TypeScript, Python, Go, Java and YAML. Build and distribute reusable components for 170+ cloud & SaaS providers.
              - title: Pulumi ESC
                description: |
                    Centralized secrets management & orchestration. Tame secrets sprawl and configuration complexity securely across all your cloud infrastructure and applications.
              - title: Automate deployment workflows
                description: |
                    Orchestrate secure deployment workflows through GitHub or an API.
              - title: Search and analytics
                description: |
                    View resources from any cloud in one place. Search for resources across clouds with simple queries and filters.
              - title: Pulumi Automation API
                description: |
                    Build custom deployment and CI/CD workflows that integrate with Pulumi Developer Portal, custom portals, or CLIs.
              - title: Developer portals
                description: |
                    Create internal developer portals to distribute infrastructure templates using Pulumi or the Backstage-plugin.
              - title: Identity and access control
                description: |
                    Manage teams with SCIM, SAML SSO, GitHub, GitLab, or Atlassian. Set permissions and access tokens.
              - title: Policy enforcement
                description: |
                    Build policy packs from 150 policies or write your own. Leverage compliance-ready policies for any cloud to increase compliance posture and remediation policies to correct violations.
              - title: Audit logs
                description: |
                    Track and store user actions and change history with the option to export logs.

case_studies:
    title: Customers innovating with Pulumi Cloud
    items:
        - name: Atlassian
          link: /case-studies/atlassian/
          logo: atlassian
          description: |
            Developers reduced their time spent on maintenance by 50%.

        - name: Elkjop
          link: /case-studies/elkjop-nordic/
          logo: elkjop-nordic
          description: |
            Increased developers' agility and speed through platform engineering.

        - name: Starburst
          link: /blog/how-starburst-data-creates-infrastructure-automation-magic-with-code/
          logo: starburst
          description: |
            Increased velocity and speed, with deployments that are up to 3x faster.

        - name: BMW
          link: /case-studies/bmw/
          logo: bmw
          description: |
            Enabled developers to deploy across hybrid cloud environments.

        - name: Lemonade
          link: /case-studies/lemonade/
          logo: lemonade
          description: |
            Standardized infrastructure architectures with reusable components.

        - name: Snowflake
          link: /case-studies/snowflake/
          logo: snowflake
          description: |
            Built a multi-cloud, Kubernetes-based platform to standardize all deployments
---
