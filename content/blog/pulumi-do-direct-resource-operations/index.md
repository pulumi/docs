---
title: "Introducing pulumi do: Direct Resource Operations for Any Cloud"
date: 2026-05-22
draft: false
meta_desc: "The new pulumi do command lets you create, read, update, and delete any cloud resource across the full Pulumi ecosystem with a single, agent-friendly API."
meta_image: meta.png
feature_image: feature.png
authors:
    - fraser-waters
    - pat-gavlin
    - arun-loganathan
    - christian-nunciato
tags:
    - features
    - pulumi-cli
    - ai-agents
    - product-launches
schema_type: auto

social:
    twitter:
    linkedin:
    bluesky:
---

Infrastructure as code is the right model for production systems. State tracking, drift detection, and repeatable deployments all matter when you're managing real workloads.

But sometimes, you also need a quick, one-off interaction with the cloud: create a bucket or a database, look up a VPC, delete a stray resource.

Today we're introducing `pulumi do`, a new command for direct resource operations. With `pulumi do`, you can create, read, update, delete, and query any cloud resource from the terminal with a single command, across thousands of Pulumi-supported providers — no project, code, or state required.

<!--more-->

## The problem: Sometimes IaC is more than you need

When you're managing production workloads, IaC is the proven solution. Code lets you declare complex systems, state tracking catches drift before it becomes a problem, dependency graphs sequence changes safely, and policy keeps everything in bounds. That full lifecycle, especially with the backing of a platform like Pulumi Cloud, is exactly what you want to build systems that scale.

But when you (or your coding agent) need an ad-hoc Postgres database, the simplest path with IaC still takes several steps: make a directory, create a project, configure your credentials, write the code, preview, deploy. It works, but it's not always necessary for what should be a simple operation. `pulumi do` collapses all of those steps into one, using the same Pulumi providers, resource model, and ecosystem that powers the core Pulumi platform.

Resource creation is also only part of the problem. As Joe laid out in [The Agentic Infrastructure Era](/blog/the-agentic-infrastructure-era/), the real challenge for AI agents isn't with code or CLI commands, it's with everything else: getting a cloud account, resolving credentials, wiring configuration across multiple services. [Agent accounts](/docs/administration/organizations-teams/agent-accounts/), also [released this week](/releases/agentic-infrastructure-era/), simplify this by letting an agent provision its own ephemeral Pulumi Cloud account, and [Pulumi ESC](/docs/esc/) takes care of consolidating credentials across providers. Together, with `pulumi do`, agents can now go from zero to deployed infrastructure without requiring a human in the loop — and when that one-off resource needs to grow into a more permanent system, there's a clear graduation path back to full Pulumi IaC.

## What it looks like

As an example, say you wanted to provision an S3 bucket. With the AWS CLI, you'd need to assemble an `aws s3api create-bucket` invocation with the right set of command-line flags, region constraints, a globally unique name, and so on. With `pulumi do`, it's just this:

```bash
$ pulumi do aws:s3:Bucket create
```

That might not look all that different on the surface — but because you're using the Pulumi engine and resource model, you can provide a minimal set of input properties, take advantage of provider-defined defaults, and use Pulumi's [auto-naming](/docs/iac/concepts/resources/names/) feature to give the bucket a unique name automatically:

```bash
$ pulumi do aws:s3:Bucket create

This will create aws:s3/bucket:Bucket with the following inputs:
{
  "bucket": "bucket-279ea56",
  "tagsAll": {}
}

Please confirm that this is what you'd like to do by typing `yes`:
```

Answer `yes` (or just pass `--yes`), and you're done. To delete the bucket:

```bash
$ pulumi do aws:s3:Bucket delete bucket-279ea56 --yes
```

Need to look up an existing resource? Use a [provider function](/docs/iac/concepts/functions/provider-functions/):

```bash
$ pulumi do aws:ec2:getVpc --default

{
  "arn": "arn:aws:ec2:us-west-2:663782525873:vpc/vpc-d7b311af",
  "cidrBlock": "172.31.0.0/16",
  "enableDnsHostnames": true,
  "enableDnsSupport": true,
  "enableNetworkAddressUsageMetrics": false,
  "id": "vpc-d7b311af",
  ...
}
```

Same CLI, same output contract, same provider ecosystem.

### The command shape

The `do` command accepts a Pulumi resource type, or [_type token_](/docs/iac/concepts/resources/names/#types), to determine the action to take. Type tokens have the form `<package:module:resource>`. For example, `aws:s3:Bucket` refers to the [Amazon S3 Bucket resource](/registry/packages/aws/api-docs/s3/bucket/) that belongs to the `s3` module of the `aws` package.

You can also provide a portion of the token to help you find what you're looking for without ever having to leave the terminal:

```bash
$ pulumi do aws:s3

Functions and resources for the s3 module.

Run 'pulumi do <module/resource/function> --help' for more details on usage.

Functions:
  aws:s3:getAccessPoint
  aws:s3:getAccountPublicAccessBlock
  aws:s3:getBucket
  aws:s3:getBucketObject
  ...

Resources:
  aws:s3:AccessPoint
  aws:s3:AccountPublicAccessBlock
  aws:s3:AnalyticsConfiguration
  aws:s3:Bucket
  ...

$ pulumi do aws:s3:Bucket read bucket-d20976f

{
  "arn": "arn:aws:s3:::bucket-d20976f",
  "bucket": "bucket-d20976f",
  "bucketDomainName": "bucket-d20976f.s3.amazonaws.com",
  "bucketNamespace": "global",
  ...
}
```

The package, module, and resource/function segments all come directly from the Pulumi provider schema, so `--help` works at every level of the tree. Pass a package name, optional module, and optional function or resource type, and `do` returns the appropriate level of detail.

You can also provide the input properties of a resource in a YAML or JSON file with the `--input` option. To create a container service in Google Cloud Run for example:

```yaml
# service.yaml
location: us-central1
deletionProtection: false
template:
  containers:
    - image: us-docker.pkg.dev/cloudrun/container/hello
```

```bash
$ pulumi do gcp:cloudrunv2:Service create \
    --input yaml \
    --input-file service.yaml

This will create gcp:cloudrunv2/service:Service with the following inputs:
{
  "deletionProtection": false,
  "location": "us-central1",
  "name": "service-b8af752",
  "template": {
    "containers": [
      {
        "image": "us-docker.pkg.dev/cloudrun/container/hello"
      }
    ]
  }
}
```

The result:

```plain
{
  "createTime": "2026-05-22T23:00:22.415839Z",
  ...
  "urls": [
    "https://service-b8af752-921927215178.us-central1.run.app",
    "https://service-b8af752-ctnulmzwoa-uc.a.run.app"
  ]
}
```

### Resource operations

Most resources support the full set of CRUD operations — create, read, update, delete, and list — directly from the CLI. Each operation maps to a provider CRUD method using the same provider logic a full Pulumi program would use, and resources are addressable by their cloud provider IDs:

```bash
# Create a resource
$ pulumi do aws:s3:Bucket create --yes | jq -r ".name"
bucket-5919be3r

# Fetch it
$ pulumi do aws:s3:Bucket read bucket-4f5cb22 | jq -r ".hostedZoneId"
Z3BJ6K6RIION7M

# Update/patch it
$ pulumi do aws:s3:Bucket patch bucket-4f5cb22 --input yaml --input-file tags.yaml

$ pulumi do aws:s3:Bucket read bucket-4f5cb22 | jq ".tags"
{
  "key": "value"
}

# Delete it
$ pulumi do aws:s3:Bucket delete bucket-4f5cb22
```

### Provider configuration

Today, `pulumi do` resolves provider configuration — for example, applying your AWS credentials — using environment variables or credential files as supported by each individual Pulumi provider. See the [Pulumi Registry](/registry/) for provider-specific configuration details.

## Designed for humans and agents

We've designed `pulumi do` to serve humans and coding agents equally well, guided by three fundamental ideas:

- **Consistent command structure across every provider.** The `do <package:module:type> <operation>` pattern is the same for AWS, Azure, Google Cloud, Kubernetes, Cloudflare, Datadog, and every provider, including packages containing higher-level [component resources](/docs/iac/concepts/components/). Once an agent learns that pattern, it applies across the board.

- **Predictable output contract.** JSON on stdout, progress on stderr, consistent exit codes. An agent can parse the result programmatically without scraping human-formatted tables.

- **A single CLI command that works across every cloud.** Many cloud and SaaS providers don't have a full CLI at all. `pulumi do` generates commands from the provider schema, so if a Pulumi provider exists for it, the CLI just works. Neither humans nor agents need to install, learn, or even know about cloud provider-specific tooling.

## What's next

Resource operations and provider functions are the foundation. The `pulumi do` roadmap extends the same direct-operation model with credential management, state tracking, and a path to full IaC.

### Unified credentials with Pulumi ESC

One of the hardest parts of multi-cloud operations is credential management. Every provider has its own authentication scheme, environment variables, and session lifecycle. An agent working across AWS, Cloudflare, and Datadog today manages three separate credential mechanisms.

We're building [Pulumi ESC](/docs/esc/) integration into `pulumi do` so you can manage credentials in one place and resolve them everywhere. ESC handles credential resolution (including OIDC-based dynamic credential generation and short-lived tokens) across all of your providers. Name the credential set, reference it, and ESC does the rest, with rotation, RBAC, and audit built in.

### Cross-resource references

Real infrastructure has dependencies — subnets need VPCs, security group rules need their security groups, and so on. When you're building resources one at a time, those references need to flow between commands somehow.

A future version of `pulumi do` will let resource inputs reference outputs from previously created resources, allowing the CLI to resolve them automatically and preserve the dependency graph. Later, when the time comes to graduate to a full IaC program, the generated code contains proper resource references rather than hard-coded strings.

### Stateful mode and the graduation path

Today, `pulumi do` is stateless. Each command runs independently. A planned stateful mode will persist resource state across operations, enabling drift detection, lifecycle management, and a graduation path to full infrastructure as code.

Here's what we're planning:

1. **Zero setup.** Your first `pulumi do` implicitly creates a project and stack. No manual initialization.

1. **Accumulate resources.** Each operation stores resource state. After a few commands, you have a lightweight representation of your infrastructure.

1. **Eject to a full project.** When the time comes, generate a Pulumi project in your chosen language with all resources imported and dependency graphs intact.

1. **Connect to Pulumi Cloud.** Layer on governance, compliance, team collaboration, and deployment automation through [Pulumi Cloud](/product/). Resources created via `pulumi do` can be governed by [Pulumi Insights](/product/insights-governance/) from day one, even before you opt into full IaC.

This path works because `pulumi do` uses the same providers, resource types, and property schemas as every other `pulumi` operation. Provisioned cloud resources stay where they are as management capabilities are added as needed.

## Get started

`pulumi do` ships as a research preview in [Pulumi CLI v3.242.0](https://github.com/pulumi/pulumi/releases/tag/v3.242.0) and later. Install or update the CLI, install a provider plugin, and start running commands. The [documentation](/docs/iac/cli/direct-resource-operations/) has the full reference.

We can't wait to hear your feedback. [Give it a try today](/docs/install/), tell us what works (and what doesn't), and help shape the CLI that agents and humans both reach for first.

- [Documentation](/docs/iac/cli/direct-resource-operations/)
- [File a feature request](https://github.com/pulumi/pulumi/issues/new)
- [Pulumi Community Slack](https://slack.pulumi.com/) for discussion
