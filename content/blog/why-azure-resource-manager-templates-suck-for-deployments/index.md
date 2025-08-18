---
title: "Why ARM Sucks for Azure Deployments (and What to Do About It)"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-08-21T01:41:10Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: ARM slowing you down? Ditch the JSON pain and deploy Azure like a pro with Pulumi + C#. Faster, cleaner, and actually developer-friendly.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - azure
    - arm-templates
    - azure-resource-manager


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Azure Resource Manager (ARM) templates were supposed to make cloud infrastructure easy to automate. Instead, for many teams, they’ve become a sprawling mess of brittle JSON, manual scripts, and hours of wasted time.

If you’ve ever tried to scale your Azure infrastructure with ARM, you’ve probably hit some of these pain points:

- Templates that started simple… and now span thousands of lines  
- Manual configuration stitched together with bespoke deployment logic  
- Lack of support for key services like Databricks  
- Slow, error-prone deployments that require multiple manual steps  
- No reuse, no testing, and no relief

ARM wasn’t built for the complexity of modern Azure workloads. If you're already familiar with general-purpose languages, there’s a better path: Pulumi.

<!--more-->

## What Real Azure Teams Are Struggling With

From Reddit threads to customer calls, here’s what we keep hearing:

**"Our ARM templates have grown very complex and unwieldy."**

When everything is defined in JSON, there’s no concept of modularity. You end up with copy/pasted blocks, unreadable logic, and maintenance nightmares.

**"We rely on bespoke code to deploy Databricks, which isn't supported in ARM."**

If the tooling can’t deploy what you need, you're forced to write scripts and wire them in manually. That’s not DevOps—it’s duct tape.

**"Configuration management is all manual and custom."**

No secrets management, no config validation, no reusable environments, just fragile, homegrown scripts that break in subtle ways.

**"Our deployments are long and difficult. It all has to run sequentially."**

Because there's no dependency graph, no abstraction, and limited orchestration, deployments are slow and hard to parallelize.

---

## Pulumi: The Obvious Upgrade for .NET and Azure

Pulumi solves these problems at their root. It lets you define your Azure infrastructure using C#, the same language you're already using to build your applications. With Pulumi, you get:

✅ Familiar programming languages  
✅ Type safety and compile-time validation  
✅ Full IDE support (IntelliSense, refactoring, debugging)  
✅ Built-in support for Databricks, Kubernetes, and more  
✅ Automated config and secrets management  
✅ Easy testing, reuse, and CI/CD integration

Here’s a simple example: creating a Storage Account:

### ⛔ ARM Template (JSON)

```json
{
  "type": "Microsoft.Storage/storageAccounts",
  "apiVersion": "2021-09-01",
  "name": "[parameters('storageAccountName')]",
  "location": "[resourceGroup().location]",
  "sku": { "name": "Standard_LRS" },
  "kind": "StorageV2",
  "properties": {}
}
```

### ✅ Azure with Pulumi in C#

```csharp
using Pulumi;
using Pulumi.AzureNative.Storage;

class MyStack : Stack
{
    public MyStack()
    {
        var storageAccount = new StorageAccount("sa", new StorageAccountArgs
        {
            ResourceGroupName = "my-rg",
            Sku = new SkuArgs { Name = SkuName.Standard_LRS },
            Kind = Kind.StorageV2
        });
    }
}
```

It’s clean. It’s familiar. And it works seamlessly with your .NET tooling.

## Why It Just Works for .NET Teams

If you're a Microsoft shop, Pulumi is a natural fit:

- Use C# across both infrastructure and application layers
- Share libraries and logic between services
- Test infrastructure the same way you test code
- Integrate with Azure DevOps and GitHub Actions
- Manage secrets, environments, and policies as code

Pulumi supports all the Azure services ARM does (and more), while giving you flexibility and control ARM never could.

## Summary
ARM templates weren’t designed to scale with the complexity of today’s cloud environments. They’re static, verbose, hard to test, and increasingly brittle.

Pulumi gives you the tools to manage Azure the way you manage software—modular, testable, scalable, and secure.

If you’re already building with .NET, you’re 90% of the way there.

Why suffer through another slow, error-prone ARM deployment?

Level up your Azure infrastructure with Pulumi.
