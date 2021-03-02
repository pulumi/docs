---
title: "Automate Your Infrastructure with Automation API and C#"
date: tbd
meta_desc: "tbd"
meta_image: automation_api.png
authors:
- joshua-studt
tags:
- Automation API
- C#
- csharp
- dotnet
- .NET
---

Currently available in public preview, Pulumi's Automation API enables you to programmatically call upon the Pulumi engine to provision your infrastructure. Today, we are excited to announce C# support for the API, so .NET developers can do just that. Read more about the Automation API [here.](https://www.pulumi.com/blog/automation-api/)

## Using Automation API in .NET

The `Pulumi.Automation` [NuGet package](https://github.com/pulumi/pulumi/tree/master/sdk/dotnet/Pulumi.Automation) exposes a `LocalWorkspace` that empowers you to create and manage [Stacks]({{< relref "/docs/intro/concepts/stack" >}}) as well a `WorkspaceStack` so you can perform infrastructure updates, refresh, previews, and destroy.