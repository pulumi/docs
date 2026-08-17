---
title_tag: "Get Started with pulumi do | Pulumi CLI"
meta_desc: "Get started with pulumi do: create, query, update, and delete cloud resources directly from the Pulumi CLI without writing a program."
title: Get Started with pulumi do
h1: Get started with pulumi do
menu:
    iac:
        name: Get Started
        parent: iac-cli-do
        identifier: iac-cli-do-get-started
        weight: 1
---

{{% notes type="info" %}}
`pulumi do` is in **research preview**. The command interface may change based on feedback.
{{% /notes %}}

The `pulumi do` command gives you direct create, read, update, delete, and query access to cloud resources from the terminal. It works with every Pulumi provider, so covers thousands of resource types across every cloud.

This guide takes you from zero to your first resource operations, and shows you what you can do with `pulumi do`.

## Prerequisites

1. [Install the Pulumi CLI](/docs/install/), version 3.257.0 or later. Because `pulumi do` is in research preview and evolving quickly, we recommend the latest version.
1. Credentials for a cloud provider. The examples use AWS, but any [Pulumi provider](/registry/) works the same way.

## Create your first resource

`pulumi do` picks up provider credentials the same way the provider itself does — from standard environment variables and credential files (for AWS, for example, `AWS_PROFILE`, `AWS_REGION`, or `~/.aws/credentials`). You can also pass explicit provider configuration in a file with `--provider-file`.

Create an S3 bucket, giving it a name:

```bash
$ pulumi do aws:s3:Bucket create my-bucket
```

The provider plugin is installed automatically on first use. The CLI shows you the planned changes and asks for confirmation (which can be skipped by passing `--yes`), then creates the bucket:

```
 +  aws:s3:Bucket my-bucket created
Outputs:
    arn   : "arn:aws:s3:::my-bucket-f998a37"
    bucket: "my-bucket-f998a37"
    id    : "my-bucket-f998a37"
    ...

Created my-bucket (snippet c7901139-b263-4572-9a57-6e393c2eae2c)
```

Note that the bucket name uses the same provider defaults and [auto-naming](/docs/iac/concepts/resources/names/#autonaming) rules as a full Pulumi program.

By default, `pulumi do` runs in stateful mode: the bucket is recorded as a snippet in the state file, and its lifecycle is tracked. You can bypass this tracking by passing the `--stateless` flag.

## Add an object to the bucket

A bucket wouldn't be useful without anything to put into it. Create a bucket object in the bucket.

The object needs to reference the bucket you just created. `pulumi do` auto-assigns every tracked resource an identifier, derived from its name with hyphens converted to underscores — so `my-bucket` becomes `my_bucket`. To check the identifiers Pulumi assigned, run `pulumi do show-resources`:

```bash
$ pulumi do show-resources

NAME       URN
my_bucket  urn:pulumi:default::default-global-project::aws:s3/bucket:Bucket::my-bucket
```

You can also supply your own identifiers by passing a JSON file that maps identifiers to resource URNs with `--resources-file`; its entries take precedence over the auto-assigned ones.

Inputs can be passed to `pulumi do` either via `--<input>` flags for scalar inputs, or through a YAML formatted file that's passed with `--input-file`. Inside an input file, reference another resource by its identifier with `${...}`. The following example passes the bucket reference through the YAML file, while passing the content through an `--<input>` flag:

```yaml
# object.yaml
bucket: ${my_bucket}
```

```bash
$ pulumi do aws:s3:BucketObject create my-object --input-file object.yaml --content "Hello from pulumi do" --yes
```

```
 +  aws:s3:BucketObject my-object created
Outputs:
    arn        : "arn:aws:s3:::my-bucket-f998a37/my-object"
    contentType: "application/octet-stream"
    etag       : "a7008c67f9dcdd81b4d0bde99ebf21c2"
    id         : "my-bucket-f998a37/my-object"
    ...

Created my-object (snippet 08de6783-0957-415d-98f8-e304399a1d09)
```

## Read, update, and delete

Read the current state of any resource by its cloud provider ID, which is shown in the `id` output when the resource is created.

```bash
$ pulumi do aws:s3:Bucket read my-bucket-f998a37
$ pulumi do aws:s3:BucketObject read my-bucket-f998a37/my-object
```

Update a resource with `patch`, which reads the current state, merges your changes, and shows you a diff to confirm. For example, to tag the bucket:

```yaml
# tags.yaml
tags:
    environment: dev
```

```bash
$ pulumi do aws:s3:Bucket patch my-bucket --input-file tags.yaml
```

And when you're done, delete both resources by the names you gave them. The object first, because a bucket must be empty before it can be deleted:

```bash
$ pulumi do aws:s3:BucketObject delete my-object --yes
$ pulumi do aws:s3:Bucket delete my-bucket --yes
```

## Explore a provider from the terminal

Every `pulumi do` command addresses a resource or function by its [type token](/docs/iac/concepts/resources/names/#types) in the form `<package:module:type>`. For example, `aws:s3:Bucket` is the `Bucket` resource in the `s3` module of the `aws` package. For single-module packages, you can omit the module segment.

You don't need to know the token up front. Pass a partial token and `pulumi do` lists what's available at that level:

```bash
$ pulumi do aws:s3

Functions and resources for the s3 module.

Functions:
  aws:s3:getBucket
  aws:s3:getBucketObject
  ...

Resources:
  aws:s3:AccessPoint
  aws:s3:Bucket
  ...
```

`--help` works at every level of the command tree, generated from the provider's schema. On a resource, it shows the available operations plus every input and output with its type and documentation:

```bash
$ pulumi do aws:s3:Bucket --help
```

## Query the cloud with provider functions

Providers also expose read-only functions for querying cloud APIs. You can invoke them directly by name, with inputs as flags or with an optional `--input-file`:

```bash
$ pulumi do aws:ec2:getVpc --default

{
  "arn": "arn:aws:ec2:us-west-2:123456789012:vpc/vpc-d7b311af",
  "cidrBlock": "172.31.0.0/16",
  "enableDnsHostnames": true,
  "id": "vpc-d7b311af",
  ...
}
```

`--default` isn't a `pulumi do` flag — it's the `default` input of `getVpc`, passed with the same `--<input>` form used for resource inputs. When passed as CLI inputs in this way, Boolean values like this one are interpreted as `true`. 

## Use it in scripts

Pass `--output json` to get machine-readable output for resource operations, which lets you compose `pulumi do` with tools like `jq`:

```bash
$ pulumi do aws:s3:Bucket create --stateless --yes --output json | jq -r '.id'
bucket-9f7f27f

$ pulumi do aws:s3:Bucket delete bucket-9f7f27f --stateless --yes
```

Keeping this same command shape and output format across all Pulumi providers makes `pulumi do` work especially well for coding agents, too. See [Pulumi CLI for agents](/docs/ai/cli-for-agents/) to learn more.

## Next steps

1. Read the [direct resource operations reference](/docs/iac/cli/direct-resource-operations/) for the full command syntax, flags, and provider configuration options.
1. Browse the [Pulumi Registry](/registry/) to see the providers and resources you can operate on.
1. When a one-off resource grows into real infrastructure, graduate to [Pulumi IaC](/docs/iac/get-started/) for state tracking, dependency management, and repeatable deployments.
