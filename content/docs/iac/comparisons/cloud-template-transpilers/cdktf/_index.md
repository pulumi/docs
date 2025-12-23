---
title_tag: "Pulumi vs. CDKTF"
meta_desc: Pulumi and CDKTF share some similarities, but also key differences. Learn more about how Pulumi compares to CDKTF and how to migrate your projects to Pulumi.
title: Pulumi vs. CDK for Terraform (CDKTF)
h1: Pulumi vs. CDK for Terraform (CDKTF)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: CDK for Terraform (CDKTF)
        parent: iac-comparisons-transpilers
        weight: 4
---

<style>
    main table {
        font-size: 0.94em;
    }

    main table th,
    main table td {
        width: 33.3%;
    }
</style>

{{% notes type="info" %}}
As of December 2025, the CDKTF project has been [deprecated](/blog/cdktf-is-deprecated-whats-next-for-your-team/) and its [GitHub repository](https://github.com/hashicorp/terraform-cdk) has been archived.
{{% /notes %}}

## What is CDKTF?

CDK for Terraform (CDKTF) is a tool that allows you to define infrastructure using general-purpose programming languages like TypeScript, Python, Go, C#, and Java. Like [AWS CDK](/docs/iac/comparisons/cloud-template-transpilers/aws-cdk/), CDKTF is primarily a _transpiler_ — it converts your code into an intermediate format (specifically Terraform JSON) that is later deployed by the Terraform CLI.

## Pulumi vs. CDKTF: Similarities

In addition to supporting general-purpose languages, both CDKTF and Pulumi organize cloud resources into [_stacks_](/docs/iac/concepts/stacks/), encourage the use of higher-level abstractions (called _constructs_ in CDKTF, [_components_](/docs/iac/concepts/resources/components/) in Pulumi), and track [resource state](/docs/iac/concepts/state-and-backends/) similarly, with local, remote, and cloud-hosted options available. Both tools also support deploying to multiple clouds through open-source [resource providers](/docs/iac/concepts/resources/providers/).

Also, because many of Pulumi's most popular providers are derived from open-source Terraform provider schemas, their resource models are typically identical to CDKTF's. Compare, for example, the following declaration of an Amazon S3 bucket in CDKTF:

```typescript
import { S3Bucket } from '@cdktf/provider-aws/lib/s3-bucket';

const bucket = new S3Bucket(this, 'my-bucket', {
    bucket: 'my-example-bucket',
    versioning: { enabled: true },
    acl: 'private',
});
```

to the equivalent declaration in Pulumi:

```typescript
import * as aws from '@pulumi/aws';

const bucket = new aws.s3.Bucket('my-bucket', {
    bucket: 'my-example-bucket',
    versioning: { enabled: true },
    acl: 'private',
});
```

Moreover, Pulumi also supports referencing Terraform modules directly. To learn more, see [Using a Terraform Module in Pulumi](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/).

## Pulumi vs. CDKTF: Key differences

The main difference between CDKTF and Pulumi is in how the two tools deploy infrastructure. As mentioned, CDKTF transpiles your program code into Terraform JSON before passing it on to the Terraform CLI for deployment. By contrast, Pulumi uses [its own deployment engine](/docs/iac/concepts/how-pulumi-works/) to resolve the resource graph at runtime, and provisions cloud resources directly. This typically results in faster deployments and enables more flexible workflows.

## Feature comparisons

| Feature | Pulumi | CDKTF |
| ------- | ------ | ----- |
| [Language support](#language) | TypeScript, JavaScript, Python, Go, C#, F#, VB.NET, Java, and YAML | TypeScript, Python, Go, C#, Java |
| [Provider support](#providers) | Over 250 cloud and SaaS providers, with support for any Terraform provider | Terraform providers only |
| [Dynamic resource providers](#dynamic-providers) | Yes | No |
| [Terraform module integration](#terraform-modules) | Yes | Yes |
| [Modes of execution](#modes) | Pulumi CLI or embedded within application code | Terraform CLI only |
| [State management](#state) | Local, remote, and cloud-hosted options | Local, remote, and cloud-hosted options |
| [Secrets management](#secrets) | Built-in encryption for secrets in transit and at rest | No built-in support |

### Language support {#language}

While Pulumi and CDKTF both support writing infrastructure code with general-purpose languages, Pulumi supports additional languages that CDKTF does not, such as F#, VB.NET, and YAML.

### Provider support {#providers}

Both CDKTF and Pulumi support the full Terraform provider ecosystem, though in slightly different ways. Where CDKTF supports Terraform providers through project-specific SDKs built on demand, Pulumi supports them through native binaries and SDKs that are built in advance (from open-source Terraform provider schemas) and distributed through standard package managers. Hundreds of providers are listed on the [Pulumi Registry](/registry/), and Pulumi can also [generate typed SDKs on demand](/docs/iac/get-started/terraform/terraform-providers/) for any Terraform provider.

### Dynamic provider support {#dynamic-providers}

In addition to standard pre-built providers, Pulumi also supports [dynamic resource providers](/docs/iac/concepts/resources/dynamic-providers/), which allow you to extend the Pulumi resource model by building and distributing lightweight, custom providers of your own. CDKTF does not support this capability.

### Terraform module integration {#terraform-modules}

Like CDKTF, Pulumi allows you to reference Terraform modules directly in program code by generating language-specific SDKs on demand. See [Using a Terraform Module in Pulumi](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) for details.

### Modes of execution {#modes}

Unlike CDKTF, which provisions and manages exclusively through the Terraform CLI, Pulumi can be invoked in multiple ways, including programmatically. With the [Automation API](/docs/using-pulumi/automation-api/), you can import Pulumi into any program — native app, web service, custom CLI — and reference it as you would any other library, enabling much more dynamic and flexible IaC workflows.

### State management {#state}

Both CDKTF and Pulumi track deployment state similarly, with local, remote, and cloud-hosted [options available](/docs/iac/concepts/state-and-backends/).

### Secrets management {#secrets}

Pulumi has built-in support for [secrets management](/docs/iac/concepts/secrets/) that encrypts sensitive data in state files and protects secret values from exposure in CLI output. Beyond this foundational support, [Pulumi ESC](/docs/esc/) also offers additional capabilities, including centralized secrets management for teams, integration with third-party services, dynamic retrieval of cloud credentials with OpenID Connect, and more. CDKTF has no built-in support for secrets management.

## Migrating from CDKTF to Pulumi

For teams interested in migrating from CDKTF, Pulumi has several options, including automated tooling that can convert your CDKTF code to Pulumi and import your existing Terraform state. To learn more, see [Migrating from CDKTF to Pulumi](/docs/iac/guides/migration/migrating-to-pulumi/from-terraform/).

{{< get-started >}}
