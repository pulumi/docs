---
title: "Importing a GCP Project into Pulumi with Neo"
date: 2026-04-20
draft: false
meta_desc: "Neo imports an existing Google Cloud project into Pulumi and opens a pull request with the generated program."
meta_image: meta.png
feature_image: feature.png
authors:
    - neo-team
tags:
    - neo
    - gcp
    - ai
schema_type: auto

social:
    twitter: |
        Bringing an existing Google Cloud project under Pulumi has meant listing every resource, looking up types and IDs, and running pulumi import.

        Now, just hand the project to Neo, and review the pull request.
    linkedin: |
        Most teams on Google Cloud carry at least one project that grew outside of code. Resources accumulated through the Console or gcloud scripts.

        Bringing such a project under Pulumi has meant listing every resource, looking up types and IDs, and running pulumi import. For a busy project, that was days of work.

        Now, just hand the project to Neo, and review the pull request.
    bluesky: |
        Bringing an existing Google Cloud project under Pulumi has meant listing every resource, looking up types and IDs, and running pulumi import.

        Now, just hand the project to Neo, and review the pull request.
---

Most teams on [GCP](/docs/clouds/gcp/) carry projects that grew outside of code. Resources accumulated through the Console or `gcloud` scripts. Bringing that project under Pulumi has meant listing every resource, looking up types and IDs, and running [`pulumi import`](/docs/iac/adopting-pulumi/import/). Neo does it as a conversation.

<!--more-->

## Before you start

Neo needs a [Pulumi ESC](/docs/esc/) environment with GCP credentials that can reach the resources to import. Use an [OIDC login](/docs/esc/guides/configuring-oidc/gcp/) to the target project. Reuse an existing ESC environment if your org has one; otherwise create one before running the prompt.

## Importing with Neo

An import starts from a Neo prompt in [Pulumi Cloud](/docs/pulumi-cloud/). You name the project, name the target stack, and describe the scope to pull in.

> Import the Google Cloud project `acme-prod-42` into a new Pulumi stack `acme/gcp-prod/main`. Use TypeScript. Include Compute Engine instances, VPC networks and subnets, Cloud Storage buckets, Cloud SQL instances, and project-level IAM bindings. Skip default service accounts and default networks.

Start the task in [Plan Mode](/blog/neo-plan-mode/). Neo enumerates the project's resources, examines stack state and dependencies, and produces a plan for your review before generating any code. The plan covers which resource types to pull in, how to group them, what to name them, and any clarification it needs. Refine the plan through conversation: drop a resource type, rename a logical name, correct a missing dependency. On approval, execution picks up where discovery left off.

## The preview

After approval, Neo runs `pulumi import`. The preview:

```text
Previewing import (acme/gcp-prod/main)

     Type                                Name                Plan
 +   pulumi:pulumi:Stack                 gcp-prod-main       create
 =   gcp:compute:Network                 vpc-main            import
 =   gcp:compute:Subnetwork              subnet-us-central1  import
 =   gcp:compute:Instance                api-server-1        import
 =   gcp:compute:Instance                api-server-2        import
 =   gcp:storage:Bucket                  acme-artifacts      import
 =   gcp:sql:DatabaseInstance            orders-primary      import
 =   gcp:projects:IAMBinding             roles-editor        import
```

The import itself changes nothing in GCP. Neo reads the live resources with your permissions, writes them into Pulumi state, generates the program, and opens a pull request.

## Getting started

{{< neo-card title="Import a GCP project" prompt="I want to import existing GCP resources" >}}

Related reading:

- [Tasks](/docs/ai/tasks/)
- [Plan Mode](/blog/neo-plan-mode/)
- [Read-Only Mode](/blog/neo-read-only-mode/)
