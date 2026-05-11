---
title: "Neo Can Now Query Your Cloud Infrastructure Directly"
allow_long_title: true
date: 2026-05-12
draft: true
meta_desc: "Connect Neo to the AWS, Google Cloud, Azure, and Kubernetes CLIs using credentials managed by Pulumi ESC."
authors:
    - neo-team
tags:
    - ai
    - ai-agents
    - features
    - pulumi-neo
    - esc

social:
    twitter: |
        Neo can now run aws, gcloud, az, and kubectl directly, using short-lived credentials from Pulumi ESC.

        Ask Neo to list your S3 buckets, check a firewall rule, or inspect a Kubernetes deployment. It calls the CLI, not an API wrapper.
    linkedin: |
        Neo can now run aws, gcloud, az, and kubectl using short-lived credentials from Pulumi ESC. No long-lived secrets stored in Pulumi Cloud.

        When we launched Neo's Integration Catalog recently, third-party integrations brought context from Datadog, Linear, PagerDuty, and others into Neo's tasks. CLI integrations add the cloud providers themselves. Here's how it works.
    bluesky: |
        Neo can now run aws, gcloud, az, and kubectl using credentials from Pulumi ESC.

        Ask it to check your S3 buckets or inspect a Kubernetes deployment and it calls the CLI directly.
---

CLI integrations let [Neo](/docs/ai/) run `aws`, `gcloud`, `az`, and `kubectl` using credentials managed by [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration). When we [launched the Integration Catalog](/blog/neo-integration-catalog/), third-party integrations brought context from Datadog, Linear, PagerDuty, and others into Neo's tasks. CLI integrations add the cloud providers themselves, so Neo can query your infrastructure directly.

<!--more-->

## Neo in action

> **You:** Which S3 buckets in `production-aws` don't have versioning enabled?
>
> **Neo:** I found 43 S3 buckets. 7 don't have versioning enabled:
>
> - `legacy-uploads-2023` (us-east-1)
> - `temp-processing-queue` (us-east-1)
> - `marketing-assets-archive` (us-west-2)
> - ...

Neo ran `aws s3api list-buckets` followed by `get-bucket-versioning` for each bucket, using the credentials from the ESC environment linked to `production-aws`. You didn't need to paste secrets or switch terminals.

## How it works

An admin connects a CLI integration by pointing it at an ESC environment that emits the credentials the CLI expects. When Neo needs to run a command, ESC opens the environment, materializes short-lived credentials, and passes them to the CLI. Once the command finishes, ESC tears the environment back down. Pulumi Cloud never stores cloud credentials for CLI integrations; ESC owns the secret lifecycle end-to-end.

You can connect multiple instances of the same CLI, each pointing at a different ESC environment. Name them after what they represent (`production-aws`, `staging-aws`) and Neo uses the name to decide which one to reach for.

## Credential setup

The recommended path for AWS, Google Cloud, and Azure is OpenID Connect (OIDC) through ESC's login providers (`aws-login`, `gcp-login`, `azure-login`). OIDC lets ESC request temporary credentials from your cloud provider at task time without storing any long-lived secrets. Pulumi Cloud has a [Login Provider Setup wizard](/docs/ai/integrations/cli/#recommended-credential-setup) that automates the trust setup and writes the ESC environment for you.

For Kubernetes, ESC can pull the kubeconfig from a Pulumi stack output (so Neo always connects to the cluster Pulumi just deployed) or accept a static kubeconfig for clusters managed outside Pulumi.

See the [CLI integrations docs](/docs/ai/integrations/cli/) for the full setup guide, including the supported environment variables for each CLI.

## Get started

- [Connect your first CLI integration](/docs/ai/integrations/cli/) in Neo Settings
- [Set up an ESC environment](/docs/esc/) with OIDC credentials for your cloud provider
- [Read the Integration Catalog post](/blog/neo-integration-catalog/) for the third-party side of the story
