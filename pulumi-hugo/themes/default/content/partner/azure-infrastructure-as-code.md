---
title: Azure Infrastructure as Code
layout: azure
url: /azure/azure-infrastructure-as-code

meta_desc: Azure Infrastructure as Code means you can model and manage Azure resources using programming languages such as C#/F#, Python, TypeScript/JavaScript, and Go.

hero:
    title: Improve your cloud application knowledge with your existing programming skills
    description: |
        If you’re a developer building on Microsoft Azure, then you’ve probably encountered challenges deploying cloud applications. With over 200 services, it can be difficult to know where to start.

        What if you could radically simplify building on Azure by using your existing programming knowledge, software tools, and software engineering principles? Enter [Infrastructure as Code](/what-is/what-is-infrastructure-as-code/).
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

customer_logos:
  title: Powering top engineering teams
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - sans
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro

detail_sections:
  - title: Azure Infrastructure as Code makes developing on the cloud easier
    description: |
        The Pulumi Azure provider covers 100% of the resources available in Azure
        Resource Manager giving you the full power of Azure at your fingertips. Every
        property of each resource is always represented in the SDKs.
    items:
        - title: Everything in one place
          icon: cloud-with-nodes
          icon_color: violet
          description: |
            Azure Infrastructure as Code means you can model and manage Azure resources using programming languages such as C#/F#, Python, TypeScript/JavaScript, and Go.

        - title: Use existing tooling
          icon: lightning
          icon_color: yellow
          description: |
            Azure infrastructure becomes application code. You can author code in IDEs and validate it with standard test frameworks. You can also find and use existing libraries in package managers.

        - title: Automation
          icon: rocketship
          icon_color: salmon
          description: |
            You can deploy your Azure infrastructure with a CLI or through your CI/CD process. When changes are needed, simply update your code, check your code into Git and run an update.

  - title: Pulumi is your window to the cloud
    description: |
        Pulumi’s [Cloud Engineering Platform](/azure/) enables you to manage Azure infrastructure as code using your favorite languages and tools. It’s open source and backed by a vibrant community.
    items:
        - title: Learn cloud concepts faster through coding
          icon: cycle
          icon_color: blue
          description: Leverage Pulumi’s programmable cloud interface with code auto-completion, smart configuration defaults, type & error checking, and reusable packages with best practices.

        - title: Complete coverage of the Azure platform
          icon: clipboard
          icon_color: purple
          description: The [Pulumi Azure Native Provider SDK](/docs/intro/cloud-providers/azure/) covers 100% of the resources available in Azure Resource Manager and gives you same-day access to newly released Azure features.

        - title: Use engineering practices with infrastructure
          icon: nodes
          icon_color: salmon
          description: Adopt infrastructure as code automation, combined with tried and true software engineering practices—including modularity, testing, and CI/CD—to do more with less.

        - title: Use familiar tools and services
          icon: code
          icon_color: yellow
          description: Pulumi supports IDEs like Visual Studio and VS Code, package managers like NuGet Gallery, common test frameworks, and developer tools like GitHub and Azure DevOps.

resources:
    azure:
        title: Become a super effective Azure developer today
        description: |
            Are you ready to level up your cloud skills with Azure Infrastructure as Code? Get started with Pulumi today by following our five-part series on [top 5 things Azure developers should know](/blog/top-5-things-for-azure-devs-intro/).
        items:
            - "[Azure Virtual Machines](/blog/top-5-things-for-azure-devs-vm/)"
            - "[Serverless](/blog/top-5-things-for-azure-devs-serverless/)"
            - "[Static websites](/blog/top-5-things-for-azure-devs-static-websites/)"
            - "[Kubernetes infrastructure](/blog/top-5-things-for-azure-devs-kubernetes-infrastructure/) and [Kubernetes applications](/blog/top-5-things-for-azure-devs-kubernetes-apps/)"
            - "[DevOps integration](/blog/top-5-things-for-azure-devs-devops/)"

    other:
        title: Other resources
        items:
            - "[Watch a workshop](/resources/getting-started-with-azure-native/)"
            - "[Convert an existing ARM template](/arm2pulumi/)"
---
