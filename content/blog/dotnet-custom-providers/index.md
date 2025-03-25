---
title: "Preview of .NET resource providers"
authors: ["fraser-waters"]
tags: ["pulumi-news", ".net", "c#", "packages", "features", "native-providers"]
meta_desc: "Today we are releasing preview support for writing Pulumi providers in
  any .NET language, including C#, F#, and VB.NET."
date: "2023-01-18"

meta_image: "meta.png"
search:
  keywords:
    - preview
    - dotnet
    - including
    - net
    - providers
    - vb
    - resource
---

Today we are pleased to announce the Preview of .NET support for custom resource providers. This means you can build custom providers using your favorite .NET language, including C#, F#, and VB.NET.

<!--more-->

This is a first look preview release of the provider interface for .NET. It has minimal documentation but is feature complete. We hope to gather early feedback to refine the API and quickly bring this to a production quality release.

You will need to use version [3.52.0](https://github.com/pulumi/pulumi-dotnet/releases/tag/v3.52.0) to access the new APIs. You can install this in your project with:

```
dotnet add package Pulumi --version 3.52.0
```

You can see an example of using the new provider interface in the [dotnet integration tests directory](https://github.com/pulumi/pulumi-dotnet/tree/main/integration_tests/testprovider). This has replaced the old test provider that was written in Go.

Please [view the provider interface](https://github.com/pulumi/pulumi-dotnet/blob/main/sdk/Pulumi/Provider/Provider.cs) and raise issues and discussions on [GitHub](https://github.com/pulumi/pulumi-dotnet) or our [Community Slack](https://slack.pulumi.com) in the `#dotnet` channel &mdash; we can’t wait to hear what you think!
