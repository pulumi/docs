---
title: "Two Real-World Incidents That Show the Risk of Managing Your Own State Backend"
date: 2026-07-25
meta_desc: "A leaked IAM key and an out-of-order merge both trace to one cause: a self-managed state backend. Here's what a managed backend changes."
feature_image: feature.png
authors:
    - pulumi-content-team
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

        A leaked IAM key in an S3-hosted tfstate file put a second AWS account's keys within reach. An out-of-order merge deleted two of three production Kubernetes clusters.
    linkedin: |
        Two real-world incidents. One root cause: a self-managed infrastructure-as-code state backend.

        We walk through a credential leak that exposed a second AWS account's keys, and a state race condition that deleted two of three production Kubernetes clusters, then show what a managed backend changes about both.
    bluesky: |
        A leaked IAM key in S3. An out-of-order Terraform merge.

        Two incidents, one root cause: DIY state management.
---

Two publicly documented infrastructure-as-code incidents, a cloud intrusion and a mass cluster deletion, trace back to the same root cause: managing your own state backend. Neither is a knock on any one tool, and it isn't a knock on Pulumi's own self-managed backends either. Pulumi already improves on this picture versus Terraform by encrypting values marked as secrets by default, on any backend, self-managed included. What neither Pulumi nor Terraform can do on a self-managed backend is protect everything outside that scope: encrypting the state file as a whole, enforcing a lock between concurrent writers, or guaranteeing a clean recovery path. That's the layer a managed backend, like Pulumi Cloud, is purpose-built to close.

## Incident one: how a single plaintext state file exposed a second AWS account's credentials

In 2023, the [Sysdig Threat Research Team documented an intrusion](https://www.sysdig.com/blog/cloud-breach-terraform-data-theft) it named SCARLETEEL, discovered in a single customer's environment. The attack chain ran through infrastructure, not application code:

1. The attacker exploited a public-facing service running in a self-managed Kubernetes cluster to gain initial access to a worker node.
2. From that node, they queried the [IMDSv1 instance metadata service](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) to retrieve the node's IAM role credentials.
3. While enumerating the account's resources, the attacker disabled CloudTrail logging to evade detection and found a `terraform.tfstate` file in S3 holding a second AWS account's IAM access keys, stored in plaintext.
4. The attacker attempted to use those keys to move into the second account, but every API request they made there failed: the credentials didn't carry the permissions needed to do anything with them.

**Root cause**: this was not a Terraform vulnerability. Terraform's [own state documentation](https://developer.hashicorp.com/terraform/language/state/sensitive-data) acknowledges that state files "contain detailed information about your infrastructure, including resource attributes and metadata that can contain sensitive values, such as initial database passwords or API tokens," and that by default Terraform "stores your state in a plaintext file," instructing teams to "treat your state file as sensitive data." The exposure came from where and how the state was stored: an S3 bucket subject to whatever object-storage ACLs the team configured, holding secrets in cleartext with no engine-level enforcement of encryption. A Pulumi project on a self-managed backend still leaves the state file's storage, the S3 bucket ACLs, the local filesystem, in the team's hands, so the same object-storage misconfiguration that exposed the SCARLETEEL state file applies. Pulumi does encrypt values explicitly marked as secrets by default, even on a self-managed backend, so it doesn't share Terraform's plaintext-secret default, but any credential written to state without being marked secret is still only as protected as the bucket around it. The risk lives in the DIY backend model's storage layer, not in a specific IaC language or syntax.

## Incident two: how shared state deleted two of three production clusters

In a [2019 KubeCon EU keynote](https://www.youtube.com/watch?v=ix0Tw8uinWs), Spotify infrastructure engineer David Xia described two separate incidents in which the company accidentally deleted production Kubernetes clusters: one caused by a mistaken click in the wrong browser tab, the other by two Terraform pull requests merged out of order. The Terraform incident, the more serious of the two:

- Two pull requests, both touching the same shared Terraform state for the cluster fleet, were merged out of order.
- The resulting `terraform apply` attempted to recreate a cluster and hit a permissions mismatch between what the state expected and what existed.
- The apply's failure mode was destructive rather than inert: **two of Spotify's three production Kubernetes clusters were deleted**.
- The incident ran roughly **nine hours, from 8 PM to 5 AM**, before Spotify finished restoring the clusters and their integrations.
- Critically, Spotify reported **no end-user impact**, because the team had deliberately engineered redundancy across clusters as a hedge against exactly this class of failure.

**Root cause**: this is a general property of self-managed, serialized state protocols, not a Terraform-specific defect. Whenever two changes race to mutate the same state file without an enforced lock, the outcome depends on merge order and timing rather than intent. Any DIY-backend IaC tool is exposed to this class of failure to the degree its locking is optional or must be stood up separately. Terraform's S3 backend historically required a separate lock service; Pulumi's self-managed backends enable a basic file-based lock by default, though a shared object store still depends on that store honoring the lock.

## The common thread: managing your own state backend

Both incidents map cleanly onto the same underlying gaps in how a self-managed backend handles state:

| Risk surface | Self-managed backend (e.g. raw S3, local file) | What it takes to close the gap yourself |
| --- | --- | --- |
| Secret handling | Secrets, including IAM keys, are only as protected as the bucket (Terraform stores state in plaintext by default; Pulumi encrypts secret-marked values, but anything not marked is in the clear) | Manually configure bucket encryption, apply strict IAM policies, and hope no credential is ever written to state without being caught |
| Concurrency and locking | No enforced lock between competing writers; behavior depends on merge order | Locking is opt-in and yours to enable (Terraform's S3 backend historically required a separate DynamoDB table; as of Terraform 1.10 it also supports native S3 lockfile locking via `use_lockfile`, with DynamoDB-based locking now deprecated) |
| Recoverability | A destructive apply is final; recovery depends on backups and runbooks you built | Maintain your own state backup and restore process, tested under pressure |
| Auditability | Access and mutation history exists only if you built logging on top of the object store | Instrument CloudTrail (or equivalent), and don't let anyone disable it |

Neither Spotify nor the SCARLETEEL victim organization did anything unusual. They ran infrastructure as code the way most teams do: state in an object store, changes shipped through pull requests, and standard IAM roles. The gaps above are what a self-managed backend leaves for the team to solve alone.

## How a managed backend closes these gaps

[Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/) is a managed backend built specifically to remove these risks from the team's plate, whether the underlying program is written in Pulumi's language SDKs or, since Pulumi's native HCL and Terraform state backend support, in HCL against Terraform-compatible state:

| Incident risk | Pulumi Cloud defense |
| --- | --- |
| Plaintext secrets in state (SCARLETEEL) | Pulumi's [transitive secret tainting](https://www.pulumi.com/blog/pulumi-state-taint/) marks any value derived from a secret as sensitive and encrypts it, an engine behavior available on any backend, self-managed included. Pulumi Cloud goes further and [encrypts the entire state file at rest and in transit by default](https://www.pulumi.com/docs/iac/concepts/state-and-backends/), so protection doesn't depend on which individual values a team remembered to mark secret |
| Long-lived plaintext IAM keys (SCARLETEEL) | [Pulumi ESC](https://www.pulumi.com/docs/esc/) issues short-lived, dynamic credentials via OIDC federation, so there is no durable IAM access key sitting in state or in a config file for an attacker to find |
| Out-of-order concurrent writes (Spotify) | Automatic stack locking prevents two operations from mutating the same stack's state at once, removing the race condition that let two merges collide |
| Slow, destructive recovery (Spotify) | A transactional, journaling state backend, with journaling alone [reported to speed up operations by up to 20x](https://www.pulumi.com/blog/journaling-ga/) over Pulumi Cloud's own prior full-snapshot behavior. [Deleted-stack restoration](https://www.pulumi.com/docs/iac/operations/stack-management/restoring-deleted-stacks/) (Enterprise and Business Critical, last 25 deleted stacks) brings back a stack's state file and update history, so a team recovering from a destructive operation is rebuilding from an intact source of truth rather than reconstructing one from scratch, though it does not re-create cloud resources a `destroy` already removed |

A team does not have to rewrite its infrastructure code to get these protections. Teams already on Pulumi get them by pointing their stacks at Pulumi Cloud instead of a self-managed backend. Teams currently on Terraform can [migrate existing state to Pulumi](https://www.pulumi.com/blog/converting-full-terraform-states-to-pulumi/) or, with Pulumi's native Terraform state backend support, connect Pulumi Cloud directly to their existing Terraform-managed state without a rewrite at all. For the fuller picture of what changes as a team scales past a self-managed backend, see [Why Choose Pulumi Cloud Over DIY Backends?](https://www.pulumi.com/blog/why-choose-pulumi-cloud-over-diy-backends/)

## What the downtime and breach math says

Neither incident's owning company disclosed a specific dollar figure, but industry benchmarks make clear why leadership treats state-backend risk as a business problem, not just an engineering one. [IBM's Cost of a Data Breach Report 2026](https://www.ibm.com/reports/data-breach) put the global average cost of a data breach at **$4.99 million**, a 12% year-over-year increase and a record high, driven in part by rising detection, escalation, and lost-business costs. On the availability side, [ITIC's 2024 Hourly Cost of Downtime survey](https://itic-corp.com/itic-2024-hourly-cost-of-downtime-report/) found that more than **90% of mid-size and large enterprises** report an hourly downtime cost exceeding **$300,000**, with 41% reporting figures between $1 million and over $5 million per hour. A nine-hour recovery window, of the kind Spotify navigated without customer impact only because of infrastructure they had deliberately over-provisioned, is exactly the scenario those figures describe for teams without that redundancy already in place.

## Frequently asked questions

### Is this a Terraform-specific problem?

No. Both incidents stem from properties of self-managed, file-based state backends: plaintext secret storage and unenforced concurrent writes. Pulumi encrypts values explicitly marked as secrets by default, even on a self-managed backend, but the underlying gap, no encryption or locking enforced at the storage layer by the platform itself, applies to any infrastructure-as-code tool run against a self-managed backend such as a raw S3 bucket or local file, Pulumi included.

### What is a state backend in infrastructure as code?

A state backend is where an infrastructure-as-code tool stores the record of what it has deployed, so it can compare desired configuration against actual resources on the next run. Self-managed backends (local files, raw object storage buckets) put the team fully in charge of that record's encryption, locking, and recoverability. Managed backends, like [Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/), build those protections in.

### How does Pulumi Cloud prevent the credential leak that happened in the SCARLETEEL incident?

Pulumi's [transitive secret tainting](https://www.pulumi.com/blog/pulumi-state-taint/) already treats any value derived from a secret as sensitive on any backend, self-managed included. Pulumi Cloud adds [default encryption of the entire state file at rest and in transit](https://www.pulumi.com/docs/iac/concepts/state-and-backends/), so protection isn't limited to the values a team remembered to mark secret. Combined with [Pulumi ESC](https://www.pulumi.com/docs/esc/) issuing short-lived, OIDC-based credentials instead of long-lived IAM keys, there is no durable plaintext key sitting in state for an attacker to extract.

### How does Pulumi Cloud prevent the kind of out-of-order state conflict that hit Spotify?

Pulumi Cloud applies automatic stack locking, so two operations can't mutate the same stack's state concurrently. That removes the race condition where merge order determines the outcome of a state mutation, which is what led to Spotify's cluster recreation hitting a permissions mismatch.

### Can I get these protections without rewriting our existing Terraform infrastructure?

Yes. Pulumi now supports HCL and Terraform-compatible state backends natively, so teams can connect Pulumi Cloud to existing Terraform-managed infrastructure, or [migrate state into Pulumi](https://www.pulumi.com/blog/converting-full-terraform-states-to-pulumi/) directly, without rewriting infrastructure code from scratch.

### What should a team do first if they're on a self-managed backend today?

Start by auditing whether any secrets, including cloud provider credentials, exist in plaintext anywhere in the current state file or its backing storage. From there, moving to a managed backend such as Pulumi Cloud addresses encryption, locking, and recoverability in one step, rather than requiring the team to build and maintain each protection separately.

Self-managed state backends put the burden of encryption, locking, and recovery entirely on the team running them, and both of these incidents show what happens when that burden goes unmet. [Pulumi Cloud](https://www.pulumi.com/docs/pulumi-cloud/) builds those protections into the backend itself. [Get started with Pulumi Cloud](https://app.pulumi.com/signup) to see how a managed backend changes the risk profile of your own infrastructure as code.
