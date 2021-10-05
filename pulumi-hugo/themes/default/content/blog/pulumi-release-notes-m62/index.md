---
title: "Oct. 6 releases: AWS Native Provider, more refresh options"
date: 2021-10-06T08:00:00-07:00
draft: false
meta_desc: "New AWS Native Provider built on the AWS Cloud Control API, support for the newest AWS and Azure features, and more control over when stacks are refreshed"
meta_image: meta.png
authors:
    - alex-mullans
tags:
    - features
---

It's been a busy few weeks at Pulumi, including for some of our community contributors! Read on to see what's new.

- New and updated cloud providers
  - [AWS Native Provider, powered by the AWS Cloud Control API]({{< relref "/blog/pulumi-release-notes-m62#aws-native-provider-powered-by-the-aws-cloud-control-api" >}})
  - [Using AWS Graviton2 processors in AWS Lambda functions]({{< relref "/blog/pulumi-release-notes-m62#using-aws-graviton2-processors-in-aws-lambda-functions" >}})
  - [New resources in the Azure Native provider]({{< relref "/blog/pulumi-release-notes-m62#new-resources-in-the-azure-native-provider" >}})
- Pulumi CLI and core technologies
  - [New project configuration option to refresh before all write operations]({{< relref "/blog/pulumi-release-notes-m62#new-project-configuration-option-to-refresh-before-all-write-operations" >}})

<!--more-->

## New and updated cloud providers

### AWS Native Provider, powered by the AWS Cloud Control API

Last week, we announced the release of the new [AWS Native]({{< relref "/docs/intro/cloud-providers/aws-native" >}}) provider for Pulumi, which is now available in preview. AWS is the most-used cloud provider across the Pulumi ecosystem, and with the new AWS Native provider, we are focused on delivering the best possible support for the AWS platform to all Pulumi users. The AWS Native provider offers same-day support for all new AWS features and releases covered by the newly released AWS Cloud Control API, which typically supports new AWS features on the day of launch.

This release also includes a new tool for migrating existing CloudFormation templates into Pulumi programs in your favorite language, powered by the new AWS Native provider and AWS Cloud Control API, as well as the ability to deploy any 3rd party resources in the CloudFormation Registry, including resources from Atlassian, Datadog, Densify, Dynatrace, Fortinet, New Relic, and Spot by NetApp.

Learn more in the [Announcing AWS Native]({{< relref "/blog/announcing-aws-native" >}}) blog post

### Using AWS Graviton2 processors in AWS Lambda functions

Last week, AWS launched the ability to use Graviton2 processors with AWS Lambda functions. Using Graviton2 processors gives you access to the improved price performance of that architecture. Pulumi's AWS Classic provider shipped with same-day support for this new functionality.

Learn more in the [AWS Lambda functions blog post]({{< relref "/blog/aws-lambda-functions-powered-by-graviton2" >}})

### New resources in the Azure Native provider

We shipped new versions of the Azure Native provider (1.29.0 through 1.34.0) that collectively added [14 new resources](https://github.com/pulumi/pulumi-azure-native/blob/master/CHANGELOG.md#1340-2021-09-30) across services like Azure SQL, Azure API Management, and more that you can now manage with the Azure Native provider.

## Pulumi CLI and core technologies

In this milestone, we shipped Pulumi versions [3.13.0](https://github.com/pulumi/pulumi/releases/tag/v3.13.0) through [3.13.2](https://github.com/pulumi/pulumi/releases/tag/v3.13.2). The full list of changes in each version is available in the [changelog](https://github.com/pulumi/pulumi/releases); read on to learn about some of the biggest changes.

### New project configuration option to refresh before all write operations

Some Pulumi users have told us that they want to configure the behavior of their project such that a stack is always refreshed before any write operation (`preview`/`up`/`destroy`). This can help you detect and catch drift in your infrastructure, which can be introduced if someone makes changes to your infrastructure outside of the Pulumi program (e.g. in the cloud provider console).

Now, you can add the following option to your `Pulumi.yaml` project configuration file to always run a `pulumi refresh` before any write operation:

```yaml
options:
  refresh: always
```

<script id="asciicast-2BQoAe9gx9E07gBiM9h9A1cra" src="https://asciinema.org/a/2BQoAe9gx9E07gBiM9h9A1cra.js" async></script>

[Learn more in this GitHub issue](https://github.com/pulumi/pulumi/issues/8058)

### Output property enhancements

To make Pulumi Component Package previews more useful and to improve parallelism of operations like destroy, we’ve expanded the definition of the Output property type to include dependencies, as well as its resolved value, and support to serialize the outputs.

Thanks [@BenjaminSchiborr](https://github.com/BenjaminSchiborr) for their contribution in improving error messages related to these enhancements!
