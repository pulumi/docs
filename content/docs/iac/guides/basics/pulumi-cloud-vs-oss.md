---
title_tag: "Pulumi Cloud vs. OSS | Pulumi Guides"
meta_desc: Compare open source Pulumi with Pulumi Cloud across state backends, access management, secrets and configuration, policy enforcement, and workflows.
title: Pulumi Cloud vs. OSS
h1: Pulumi Cloud vs. Open Source Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi Cloud vs. OSS
        parent: iac-guides-basics
        weight: 70
aliases:
  - /docs/deployments/get-started/what-is-it/
  - /docs/pulumi-cloud/get-started/what-is-it/
---

This guide explains how Pulumi Cloud relates to open source Pulumi. It clarifies which capabilities are open source and which require Pulumi Cloud, and it breaks down the differences across each major area of the platform so you can decide which option fits your team.

## Open source Pulumi and Pulumi Cloud

Pulumi's infrastructure as code (IaC) tool is [open source](https://github.com/pulumi). It includes the CLI, the deployment engine, the language SDKs, and the resource providers, and it is how many people first adopt Pulumi. Open source Pulumi can store state in a "DIY" backend—object storage such as AWS S3, Azure Blob Storage, or Google Cloud Storage, a PostgreSQL database, or your local filesystem.

Pulumi Cloud is a managed service for storing state, managing access, and collaborating on cloud infrastructure. It is a single platform: the IaC state backend, role-based access control, secrets and configuration management, cloud resource inventory, policy enforcement, an AI agent, and managed workflows are all part of one product. Pulumi Cloud is the default backend for open source Pulumi, and it is available both as a hosted service (SaaS) and as a [self-hosted](/docs/pulumi-cloud/self-hosted/) edition you can run in your own environment.

{{% notes "info" %}}
Just as Git is fully open source and you can host, secure, and manage repositories yourself, you can also host your own Pulumi projects and stacks. However, many teams use Git with a service like GitHub for its security, reliability, and collaboration features. A similar dynamic exists with open source Pulumi and Pulumi Cloud.
{{% /notes %}}

## Comparison

The following table summarizes how open source Pulumi and Pulumi Cloud compare across the platform's major capabilities.

| Capability | Open source Pulumi | Pulumi Cloud |
| --- | --- | --- |
| State backend | DIY object storage, PostgreSQL, or local filesystem | Managed, transactional state backend; can also store Terraform state |
| Deployment history | Per-stack checkpoint history in the backend | Full organization-wide deployment history |
| Access control | Managed yourself (for example, cloud IAM on the state bucket) | Built-in RBAC with SAML/SSO integration |
| Secrets encryption | Passphrase or self-managed KMS keys | Managed encryption by default; can also use a separate encryption service |
| Secrets and configuration management | Per-stack config files only | Per-stack config files, plus centrally managed, reusable Pulumi ESC environments |
| Policy as code | Policy packs kept on disk and passed as CLI arguments | Centrally managed enforcement, plus custom and pre-built policy packs |
| Cloud resource inventory | Not included | Pulumi Insights discovers resources not managed by Pulumi |
| Drift detection | Run `pulumi refresh` manually | Scheduled drift detection and remediation |
| AI assistance | Pulumi CLI and editor integrations | Pulumi Neo AI agent integrated across the platform |
| Ephemeral environments | Not included | Review Stacks and TTL Stacks |
| Managed deployments | Bring your own automation | Pulumi Deployments managed service |
| REST API and webhooks | Not included | Documented REST API and webhooks |
| Compliance | Not applicable | Annual SOC 2 Type II audits; exportable audit trail |
| Support | Community support; commercial support available | Community support; support plans available for enterprise customers |

The sections below describe each area in more detail.

## Pulumi Cloud as an IaC backend

Pulumi stores [state](/docs/iac/concepts/state-and-backends/)—the metadata it uses to manage your cloud resources—in a backend. Open source Pulumi supports two classes of backend:

- **DIY backend**: a storage endpoint you manage yourself, such as AWS S3, Azure Blob Storage, Google Cloud Storage, an S3-compatible server, a PostgreSQL database, or your local filesystem. DIY backends are open source and free to use. See [Using a DIY backend](/docs/iac/guides/basics/using-a-diy-backend/) for setup instructions.
- **Pulumi Cloud**: a managed backend, available as a hosted service or self-hosted.

DIY backends include built-in state locking, checkpoint history, project-scoped stacks, and support for several secrets encryption providers. However, they leave operational concerns to you, including securing access to the storage backend, backup and disaster recovery, monitoring availability, and managing team access.

The Pulumi Cloud backend exposes a transactional REST API rather than a blob storage protocol. This allows it to record state incrementally and recover cleanly from partial failures—such as a network interruption during an update—where a blob storage backend has a coarser-grained protocol. Pulumi Cloud also handles the operational concerns above on your behalf. In addition to Pulumi state, Pulumi Cloud can store and manage Terraform state.

## Access management

Open source Pulumi leaves access control to you. With a DIY backend, your options are the access controls of the underlying storage: your cloud provider's IAM for an object store, or ordinary file permissions for a local or shared filesystem. That access is expressed in terms of storage operations—reads and writes to files. At that level you cannot distinguish one Pulumi operation from another: a routine `pulumi up` and a `pulumi destroy` both look like writes to the same state file, so you cannot grant someone permission to update infrastructure without also allowing them to delete it.

Pulumi Cloud provides a [role-based access control model](/docs/administration/organizations-teams/teams/) expressed in terms of Pulumi concepts and operations—stacks, projects, and the actions performed on them. It integrates with identity providers such as Microsoft Entra ID, Google Workspace, Okta, and any SAML/SSO provider, and supports [access tokens](/docs/administration/access-identity/access-tokens/) with fine-grained permissions for automation, including auditing and revocation.

## Secrets and configuration management

Both open source Pulumi and Pulumi Cloud support per-stack [configuration and secrets](/docs/iac/concepts/secrets/): each stack has its own configuration values stored in its `Pulumi.<stack-name>.yaml` file, and secret values are encrypted with the stack's chosen encryption provider—a passphrase, AWS KMS, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault. With open source Pulumi, these per-stack files are the only option, so configuration and secrets are scoped to a single stack and cannot be shared except by duplicating them.

Pulumi Cloud supports the same per-stack config files and adds Pulumi ESC (Environments, Secrets, and Configuration), which is available only with Pulumi Cloud. ESC provides centrally managed, composable, versioned environments. An environment groups configuration and secrets that change together and can be reused across many stacks and projects—as well as by tools beyond Pulumi IaC. This makes it easier to apply Don't Repeat Yourself (DRY) practices and to roll out configuration changes deliberately across related projects.

## Cloud resource inventory

With open source Pulumi, you can inspect the resources Pulumi manages by reading state—for example, with `pulumi stack` and `pulumi stack export`—but only one stack's state at a time, and only for resources Pulumi created. There is no built-in view of resources across stacks or of resources outside Pulumi's state.

Pulumi Cloud adds [Pulumi Insights](/docs/insights/), which scans your connected cloud accounts to build a searchable inventory of resources—including resources that were not created or managed by Pulumi. This helps you find unmanaged or orphaned resources and understand what exists across your cloud accounts. This capability is available only with Pulumi Cloud.

## Policy enforcement

Both open source Pulumi and Pulumi Cloud support policy as code. With open source Pulumi, you write your own policy packs and run them locally or in CI: the policy packs must be present on disk, and you supply them as command-line arguments on each run. Open source policy evaluation is limited to the resources defined in the Pulumi program being run.

Pulumi Cloud manages policy enforcement centrally. Policies are configured once for the organization and applied automatically to every update, so individual users do not need the policy packs locally. In addition to custom policy packs, Pulumi Cloud offers pre-built policy packs for common security, compliance, and cost rules. Policies apply both to infrastructure as code—blocking violations before they are deployed—and to existing cloud resources, including resources that were not created or managed by Pulumi. Pulumi Cloud evaluates policies against the resources discovered by [cloud resource inventory](#cloud-resource-inventory) with Pulumi Insights, so you can find and remediate violations across your cloud accounts regardless of how the resources were provisioned. Pulumi Cloud can also detect [drift](/docs/deployments/deployments/drift/) on a schedule, alerting you—or remediating automatically—when deployed infrastructure diverges from its declared state.

## AI assistance

Open source Pulumi includes AI integrations in the Pulumi CLI and the Pulumi VS Code extension to assist with local development.

Pulumi Cloud includes an AI agent, [Pulumi Neo](/docs/ai/), that works across the platform. It can help debug deployment failures, write infrastructure as code, automate infrastructure tasks, and answer questions about your environment—such as which versions of a dependency are deployed or which resources are unused.

## Workflows

With open source Pulumi, you run Pulumi operations yourself—from a local machine or from automation you set up, such as a CI job or a script using the [Automation API](/docs/iac/automation-api/). There is no built-in mechanism for emitting events when something changes; reacting to deployments or resource changes is something you would wire up yourself.

Pulumi Cloud includes a managed [deployment service](/docs/deployments/deployments/) that runs Pulumi operations remotely rather than from a local machine—for example, in response to Git pushes or on demand. It can also send [webhooks](/docs/deployments/webhooks/) for events such as deployments, resource updates, and policy violations, which you can use to trigger custom, event-driven workflows.

## Cost considerations

The two options trade off direct cost against operational cost. DIY backends have no licensing or subscription cost—object storage is inexpensive, and the DIY backends are open source. In exchange, you take on the work of operating them: securing access, backups and disaster recovery, monitoring availability, and managing team access. Capabilities such as RBAC, resource inventory, and centralized policy enforcement either have to be built and maintained internally or go without.

Pulumi Cloud has a free tier and paid plans. It moves the operational work of running a state backend—and the capabilities described above—to a managed service, in exchange for a subscription cost. Which tradeoff makes sense depends on the size of your team, your compliance and collaboration requirements, and how much engineering time you want to spend operating infrastructure tooling.

## Next steps

For the technical details of how Pulumi manages state with either option, see [State and backends](/docs/iac/concepts/state-and-backends/) and [Using a DIY backend](/docs/iac/guides/basics/using-a-diy-backend/). A complete list of Pulumi Cloud's features is available on the [pricing page](/pricing#compare).
