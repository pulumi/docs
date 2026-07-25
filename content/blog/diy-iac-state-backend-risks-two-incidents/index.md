---
title: "Two Real-World Incidents That Expose the Risk of a DIY State Backend"
date: 2026-07-25
meta_desc: "A leaked IAM key in S3 and an out-of-order Terraform merge both trace back to one root cause: a self-managed state backend. Here's what a managed backend changes."
feature_image: feature.png
authors:
    - alex-leventer
tags:
    - infrastructure-as-code
    - security
    - pulumi-cloud
    - state
    - platform-engineering
category: general
schema_type: auto
faq_schema: true
social:
    twitter: |
        Two incidents. One root cause: a self-managed state backend.

        A leaked IAM key in an S3-hosted tfstate file opened a second AWS account. An out-of-order merge deleted two of three production Kubernetes clusters. Here's the common thread, and what closes the gap.
    linkedin: |
        Two real-world incidents. One root cause: a self-managed infrastructure-as-code state backend.

        We walk through a credential leak that pivoted an attacker into a second AWS account, and a state race condition that deleted two of three production Kubernetes clusters, then show what a managed backend changes about both.
    bluesky: |
        A leaked IAM key in S3. An out-of-order Terraform merge. Two incidents, one root cause: DIY state management.
---

Two publicly documented infrastructure-as-code incidents, a cloud intrusion and a mass cluster deletion, trace back to the same root cause: a self-managed state backend. Neither is a knock on any one tool. Plaintext credentials in object storage and unprotected concurrent writes are risks inherent to running your own state backend, whether that state file is written by Terraform or by Pulumi in a self-managed configuration. A managed backend, like Pulumi Cloud, is purpose-built to close both gaps.

## Incident one: how a single plaintext state file opened two AWS accounts

In 2023, the [Sysdig Threat Research Team documented an intrusion](https://www.sysdig.com/blog/cloud-breach-terraform-data-theft) it named SCARLETEEL, discovered in a single customer's environment. The attack chain ran through infrastructure, not application code:

1. The attacker exploited a public-facing service running in a self-managed Kubernetes cluster to gain initial access to a worker node.
2. From that node, they queried the [IMDSv1 instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) to retrieve the node's IAM role credentials.
3. With those credentials, they enumerated the AWS account's resources, including S3 buckets, and found a `terraform.tfstate` file stored in plaintext.
4. That state file contained a second, more privileged set of IAM access keys in plaintext, which the attacker used to pivot into a **second AWS account**.
5. Once inside, the attacker disabled CloudTrail logging to cover their tracks before continuing to explore the environment.

**Root cause**: this was not a Terraform vulnerability. Terraform's [own state documentation](https://developer.hashicorp.com/terraform/language/state/sensitive-data) has long warned that state files "can contain sensitive data" in plaintext and that "care should be taken" to limit access. The exposure came from where and how the state was stored: an S3 bucket subject to whatever object-storage ACLs the team configured, holding secrets in cleartext with no engine-level enforcement of encryption. A Pulumi project on a self-managed backend, an S3 bucket, a local file, or any object store you administer yourself, carries the identical exposure. The risk lives in the DIY backend model, not in a specific IaC language or syntax.

## Incident two: how shared state deleted two of three production clusters

In a [2019 KubeCon EU keynote](https://www.youtube.com/watch?v=ix0Tw8uinWs), Spotify infrastructure engineer David Xia described how the company deleted most of its production Kubernetes clusters, twice, during a migration. The proximate cause in the more severe incident:

- Two pull requests, both touching the same shared Terraform state for the cluster fleet, were merged out of order.
- The resulting `terraform apply` attempted to recreate a cluster and hit a permissions mismatch between what the state expected and what existed.
- The apply's failure mode was destructive rather than inert: **two of Spotify's three production Kubernetes clusters were deleted**.
- Restoring service took **three hours and fifteen minutes**, made slower because the automation scripts involved were not resumable, so failed steps had to be worked around or rerun from scratch.
- Critically, Spotify reported **no end-user impact**, because the team had deliberately engineered redundancy across clusters as a hedge against exactly this class of failure.

**Root cause**: this is a general property of self-managed, serialized state protocols, not a Terraform-specific defect. Whenever two changes race to mutate the same state file without an enforced lock, the outcome depends on merge order and timing rather than intent. Any DIY-backend IaC tool, again including Pulumi run against a self-managed backend, is exposed to the same class of failure absent an external locking mechanism the team builds and maintains themselves.

## The common thread: the DIY state backend

Both incidents map cleanly onto the same underlying gaps in how a self-managed backend handles state:

| Risk surface | Self-managed backend (e.g. raw S3, local file) | What it takes to close the gap yourself |
| --- | --- | --- |
| Secret handling | Secrets, including IAM keys, stored in plaintext by default | Manually configure bucket encryption, apply strict IAM policies, and hope no credential is ever written to state without being caught |
| Concurrency and locking | No enforced lock between competing writers; behavior depends on merge order | Stand up and maintain a separate distributed lock service (e.g. DynamoDB for Terraform's S3 backend) |
| Recoverability | A destructive apply is final; recovery depends on backups and runbooks you built | Maintain your own state backup and restore process, tested under pressure |
| Auditability | Access and mutation history exists only if you built logging on top of the object store | Instrument CloudTrail (or equivalent), and don't let anyone disable it |

Neither Spotify nor the SCARLETEEL victim organization did anything unusual. They ran infrastructure as code the way most teams do: state in an object store, changes shipped through pull requests, and standard IAM roles. The gaps above are what a self-managed backend leaves for the team to solve alone.

## How a managed backend closes these gaps

[Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/) is a managed backend built specifically to remove these risks from the team's plate, whether the underlying program is written in Pulumi's language SDKs or, since Pulumi's native HCL and Terraform state backend support, in HCL against Terraform-compatible state:

| Incident risk | Pulumi Cloud defense |
| --- | --- |
| Plaintext secrets in state (SCARLETEEL) | [State is encrypted at rest and in transit by default](https://www.pulumi.com/docs/iac/concepts/state-and-backends/), with engine-level [transitive secret tainting](https://www.pulumi.com/blog/pulumi-state-taint/) that marks any value derived from a secret as sensitive, so it can't leak downstream unnoticed |
| Long-lived plaintext IAM keys (SCARLETEEL) | [Pulumi ESC](https://www.pulumi.com/docs/esc/) issues short-lived, dynamic credentials via OIDC federation, so there is no durable IAM access key sitting in state or in a config file for an attacker to find |
| Out-of-order concurrent writes (Spotify) | Automatic stack locking prevents two operations from mutating the same stack's state at once, removing the race condition that let two merges collide |
| Slow, non-resumable recovery (Spotify) | A [transactional, journaling state backend](https://www.pulumi.com/docs/iac/concepts/state-and-backends/), reported up to 20x faster than file-based alternatives, plus built-in deleted-stack restoration, so a destructive operation is a recoverable event rather than a three-hour incident |

A team does not have to rewrite its infrastructure code to get these protections. Teams already on Pulumi get them by pointing their stacks at Pulumi Cloud instead of a self-managed backend. Teams currently on Terraform can [migrate existing state to Pulumi](https://www.pulumi.com/blog/converting-full-terraform-states-to-pulumi/) or, with Pulumi's native Terraform state backend support, connect Pulumi Cloud directly to their existing Terraform-managed state without a rewrite at all.

## What the downtime and breach math says

Neither incident's owning company disclosed a specific dollar figure, but industry benchmarks make clear why leadership treats state-backend risk as a business problem, not just an engineering one. [IBM's Cost of a Data Breach Report 2025](https://www.ibm.com/reports/data-breach) put the global average cost of a data breach at **$4.44 million**, the first year-over-year decline in five years, but still a number few organizations can absorb repeatedly. On the availability side, [ITIC's 2024 Hourly Cost of Downtime survey](https://itic-corp.com/itic-2024-hourly-cost-of-downtime-report/) found that more than **90% of mid-size and large enterprises** report an hourly downtime cost exceeding **$300,000**, with 41% reporting figures between $1 million and over $5 million per hour. A three-hour recovery window, of the kind Spotify navigated without customer impact only because of infrastructure they had deliberately over-provisioned, is exactly the scenario those figures describe for teams without that redundancy already in place.

## Frequently asked questions

### Is this a Terraform-specific problem?

No. Both incidents stem from properties of self-managed, file-based state backends: plaintext secret storage and unenforced concurrent writes. Any infrastructure-as-code tool, including Pulumi, carries the same exposure when it is pointed at a self-managed backend such as a raw S3 bucket or local file rather than a managed backend with encryption and locking built in.

### What is a state backend in infrastructure as code?

A state backend is where an infrastructure-as-code tool stores the record of what it has deployed, so it can compare desired configuration against actual resources on the next run. Self-managed backends (local files, raw object storage buckets) put the team fully in charge of that record's encryption, locking, and recoverability. Managed backends, like [Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/), build those protections in.

### How does Pulumi Cloud prevent the credential leak that happened in the SCARLETEEL incident?

Pulumi Cloud [encrypts state at rest and in transit by default](https://www.pulumi.com/docs/iac/concepts/state-and-backends/) and applies [transitive secret tainting](https://www.pulumi.com/blog/pulumi-state-taint/) so any value derived from a secret is automatically treated as sensitive. Combined with [Pulumi ESC](https://www.pulumi.com/docs/esc/) issuing short-lived, OIDC-based credentials instead of long-lived IAM keys, there is no durable plaintext key sitting in state for an attacker to extract.

### How does Pulumi Cloud prevent the kind of out-of-order state conflict that hit Spotify?

Pulumi Cloud applies automatic stack locking, so two operations can't mutate the same stack's state concurrently. That removes the race condition where merge order determines the outcome of a state mutation, which is what led to Spotify's cluster recreation hitting a permissions mismatch.

### Can I get these protections without rewriting our existing Terraform infrastructure?

Yes. Pulumi now supports HCL and Terraform-compatible state backends natively, so teams can connect Pulumi Cloud to existing Terraform-managed infrastructure, or [migrate state into Pulumi](https://www.pulumi.com/blog/converting-full-terraform-states-to-pulumi/) directly, without rewriting infrastructure code from scratch.

### What should a team do first if they're on a self-managed backend today?

Start by auditing whether any secrets, including cloud provider credentials, exist in plaintext anywhere in the current state file or its backing storage. From there, moving to a managed backend such as Pulumi Cloud addresses encryption, locking, and recoverability in one step, rather than requiring the team to build and maintain each protection separately.

Self-managed state backends put the burden of encryption, locking, and recovery entirely on the team running them, and both of these incidents show what happens when that burden goes unmet. [Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/) builds those protections into the backend itself. [Get started with Pulumi Cloud](https://app.pulumi.com/signup) to see how a managed backend changes the risk profile of your own infrastructure as code.
