---
title: What Is Terraform State?
meta_desc: "Terraform state maps your configuration to real cloud resources so Terraform knows what it manages. Learn how the state file, backends, and locking work."
type: what-is
date: 2026-07-21T12:18:00-07:00
page_title: "What Is Terraform State?"
authors: ["alex-leventer"]
---

**Terraform state is the record Terraform keeps of the real-world infrastructure it manages: a mapping between the resources declared in your configuration and the actual objects that exist in your cloud provider, along with their metadata and dependency relationships.** Terraform stores this record in a state file (by default `terraform.tfstate`), and it consults that file on every operation to decide what to create, update, or destroy.

Without state, Terraform would have no memory of what it had already provisioned. Each run would be blind: it could describe the infrastructure you want, but it could not tell the difference between a resource that needs to be created and one that already exists. State is what makes Terraform's plan-and-apply model work, and understanding it is essential to using Terraform safely on a team.

In this article, we'll cover the key questions about Terraform state:

* What is Terraform state?
* What is the Terraform state file (terraform.tfstate)?
* Why does Terraform need state?
* What are Terraform state backends?
* What is state locking?
* How do you manage and inspect Terraform state?
* What are the security and operational risks of state?
* How does Pulumi manage state differently?
* Frequently asked questions about Terraform state

## What is Terraform state?

Terraform state is a snapshot of the infrastructure Terraform manages, stored as structured data that Terraform reads and writes on every operation. It serves three core purposes.

**Mapping configuration to real resources.** Your `.tf` files declare resources with logical names like `aws_instance.web`. The cloud provider knows those same resources by opaque identifiers like `i-0abc123def456`. State is the lookup table that connects the two, so Terraform knows that the `aws_instance.web` block in your code corresponds to a specific running EC2 instance.

**Tracking metadata and dependencies.** State records attributes that only exist after a resource is created (generated IDs, computed IP addresses, ARNs) and the dependency ordering between resources. This lets Terraform destroy resources in the correct reverse order and resolve references between them without re-querying the entire cloud environment.

**Improving performance.** For large configurations, querying every resource's live status from the provider API on each run would be slow. State acts as a cache of the last-known values, so Terraform can plan changes quickly and only reconcile against the provider when needed.

## What is the Terraform state file (terraform.tfstate)?

The Terraform state file is where that snapshot lives. By default it is a single JSON file named `terraform.tfstate`, written to your working directory the first time you run `terraform apply`.

The file contains a version number, the Terraform version that wrote it, a serial counter that increments on each change, a unique lineage identifier, and a list of managed resources with their provider, type, name, and the full set of attributes for each instance. When a previous state exists, Terraform may also keep a `terraform.tfstate.backup` file alongside it.

You should treat `terraform.tfstate` as sensitive and machine-owned. It is JSON, so it is technically readable and editable, but hand-editing it is a common way to corrupt state. Terraform provides dedicated commands (covered below) for the rare cases where you need to change what state records. The state file should never be committed to version control, both because it changes on every apply and because it can contain secrets in plaintext.

## Why does Terraform need state?

Terraform is declarative: you describe the desired end state, and Terraform figures out how to get there. To do that, it has to answer one question on every run: "What already exists?"

Some infrastructure tools answer that question by querying the provider live every time and reconciling against reality. Terraform instead maintains its own record. This is a deliberate design choice with real trade-offs. The state file gives Terraform a fast, complete picture of what it manages, including the mapping between logical names and provider IDs that many cloud APIs cannot reconstruct on their own (there is no reliable way to ask AWS "which instance did Terraform mean by `web`?"). It also lets Terraform detect [infrastructure drift](/what-is/what-is-infrastructure-drift/) by comparing the recorded state against the live environment during a refresh.

The cost of that design is that the state file becomes a critical, stateful artifact you have to store, secure, share, and protect from corruption. Nearly every operational concern in this article flows from that one fact.

## What are Terraform state backends?

A backend determines where Terraform stores state and how operations interact with it. There are two broad categories.

**Local backend.** The default. State is a `terraform.tfstate` file on your local disk. This is fine for a solo experiment, but it breaks down the moment a second person needs to run Terraform: there is no shared source of truth, no locking, and a real risk of two people applying conflicting changes or losing the file entirely.

**Remote backends.** State is stored in a shared, remote location so a team can collaborate safely. Remote backends typically add locking and, in some cases, encryption in transit and at rest. Common options include cloud object storage and managed services.

| Backend | Where state lives | Locking mechanism | Notes |
|---|---|---|---|
| Local | `terraform.tfstate` on disk | None | Default; single-user only |
| Amazon S3 | S3 bucket | S3 native lock file (`use_lockfile`) or DynamoDB | DynamoDB-based locking is deprecated in favor of native S3 locking |
| Azure Blob Storage | Azure storage container | Blob lease | Supports encryption at rest via the storage account |
| Google Cloud Storage (GCS) | GCS bucket | Native GCS locking | Supports encryption at rest via the bucket |
| HCP Terraform | HashiCorp-managed | Automatic | Formerly Terraform Cloud; adds runs, RBAC, and a UI |

Configuring a remote backend is a small block in your Terraform configuration. An S3 backend with native locking looks like this:

```hcl
terraform {
  backend "s3" {
    bucket       = "my-terraform-state"
    key          = "prod/network/terraform.tfstate"
    region       = "us-west-2"
    encrypt      = true
    use_lockfile = true
  }
}
```

## What is state locking?

State locking prevents two Terraform operations from writing to the same state at the same time. If two engineers (or two CI jobs) ran `terraform apply` against the same state simultaneously, they could interleave writes and corrupt the file, or make conflicting changes based on stale data.

When a backend supports locking, Terraform acquires a lock before any operation that could write state and releases it when finished. If someone else holds the lock, Terraform waits or fails with a clear message rather than proceeding. The lock is stored differently depending on the backend: HCP Terraform locks automatically, GCS and Azure Blob use native mechanisms, and the S3 backend now supports a native lock file through the `use_lockfile` argument (using S3 conditional writes), which is replacing the older pattern of a separate DynamoDB lock table.

If a run is interrupted and leaves a stale lock behind, `terraform force-unlock <LOCK_ID>` releases it. Use it carefully: forcing a lock while another operation is genuinely running reintroduces the corruption risk locking exists to prevent.

## How do you manage and inspect Terraform state?

Terraform ships a set of subcommands under `terraform state` for inspecting and modifying what state records, plus related commands for importing and refreshing. The most common ones:

* **`terraform state list`** shows every resource address currently tracked in state. It's the starting point for understanding what Terraform manages.
* **`terraform state show <address>`** prints the recorded attributes of a single resource, such as `terraform state show aws_instance.web`.
* **`terraform state mv <source> <destination>`** renames a resource in state or moves it (for example, into a module) without destroying and recreating it. This tells Terraform "the thing I used to call X is now called Y," so it updates the mapping instead of planning a replacement.
* **`terraform state rm <address>`** removes a resource from state without destroying the real infrastructure. Terraform simply stops managing it. This is how you hand a resource off to another configuration or stop tracking something.
* **`terraform state pull`** and **`terraform state push`** download the raw state from the backend and upload a modified version, respectively. `push` is a low-level, high-risk operation reserved for recovery scenarios.
* **`terraform import <address> <id>`** brings an existing, unmanaged cloud resource under Terraform management by writing it into state under the given address. (Newer Terraform versions also support declarative `import` blocks.)
* **`terraform refresh`** reconciles state with the live infrastructure, updating recorded attributes to match reality. In current Terraform this behavior is folded into `terraform plan -refresh-only`, which lets you review drift before writing it to state.

Because `state mv` and `state rm` change what Terraform believes it owns, they are among the sharpest tools in the kit: powerful for refactoring, but capable of orphaning or destroying resources if pointed at the wrong address. Always run a plan afterward to confirm the result.

## What are the security and operational risks of state?

State is powerful precisely because it holds a complete picture of your infrastructure, and that same completeness creates risk.

**Secrets stored in plaintext.** This is the most important security fact about Terraform state. When a resource has a sensitive attribute (a database password, a private key, an access token, a generated secret), that value is written into the state file as-is. Terraform's `sensitive` flag redacts values from CLI output, but it does *not* encrypt them in the state file itself. Anyone who can read the state file can read those secrets. Historically, core Terraform did not encrypt state at rest on its own; protecting it depended on the backend (an encrypted S3 bucket, for example) rather than on Terraform. OpenTofu, the open-source fork of Terraform, added native client-side state encryption in its 1.7 release (2024), encrypting state before it reaches any backend, which addresses this gap for OpenTofu users.

**Drift.** State records what Terraform last knew, not what is true right now. When someone changes a resource outside Terraform (a console click, another tool, a manual fix), the live environment drifts from state. Terraform can detect drift on a refresh, but until it does, plans are made against stale information. See [what is infrastructure drift](/what-is/what-is-infrastructure-drift/) for a fuller treatment.

**Corruption and loss.** Because state is a single critical file, losing it or corrupting it is a serious incident. A lost state file means Terraform no longer knows what it manages, and rebuilding the mapping by importing every resource by hand is slow and error-prone. Interrupted writes, unsynced local files, and careless `state push` operations are all ways state gets corrupted. Remote backends with versioning and locking are the primary defense.

These risks are all manageable, and remote backends with encryption, versioning, and locking address most of them. But they are inherent to the design: state is a valuable, sensitive, stateful artifact that a team has to actively protect.

## How does Pulumi manage state differently?

Pulumi also uses state, and for the same fundamental reason: an [infrastructure as code](/what-is/what-is-infrastructure-as-code/) tool needs a record of what it manages to map declarations to real resources. What differs is the model around that state.

**A fully managed backend by default.** With [Pulumi Cloud](/docs/iac/concepts/state-and-backends/), state is stored, versioned, and locked for you. There is no bucket to provision, no lock table to configure, and no state file to guard on your laptop. Concurrency locking is handled automatically, so two engineers can't clobber each other's updates. Pulumi Cloud is free for individuals.

**Secrets encrypted by default, not stored in plaintext.** This is the sharpest difference. Pulumi treats [secrets](/docs/iac/concepts/secrets/) as first-class: values marked secret are encrypted before they are ever written to state, using a per-stack encryption key (managed by Pulumi Cloud, or your own key in AWS KMS, Azure Key Vault, GCP KMS, or HashiCorp Vault). The encrypted ciphertext is what lands in state, so a reader of the state file cannot recover the secret. Rather than relying on the storage layer to protect plaintext, Pulumi encrypts the sensitive values themselves.

**Self-managed backends when you want them.** Teams that prefer to own their storage can point Pulumi at object storage instead: Amazon S3, Azure Blob Storage, Google Cloud Storage, or the local filesystem. The secret-encryption model carries over, so sensitive values stay encrypted regardless of where the state file lives.

| Dimension | Terraform state | Pulumi state |
|---|---|---|
| Default location | Local `terraform.tfstate` file | Pulumi Cloud managed backend |
| Secrets in state | Plaintext (unless the backend encrypts at rest; OpenTofu adds client-side encryption) | Encrypted per-secret before write, by default |
| Locking | Depends on backend; configured manually | Automatic on the managed backend |
| Self-managed option | S3, Azure Blob, GCS, etc. | S3, Azure Blob, GCS, or local filesystem |
| Managed SaaS option | HCP Terraform | Pulumi Cloud |

The result is a different set of defaults for the same job. Terraform gives you a state file and a wide choice of backends to store it in, and expects you to secure it; Pulumi manages the backend and encrypts secrets out of the box, while still letting you self-host if you prefer. Neither model is universally right, and teams migrating between the two can compare the mechanics in the [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/) guide and the [terminology mapping](/docs/iac/comparisons/terraform/#terraform-terms-and-command-equivalents).

## Frequently asked questions about Terraform state

### What is Terraform state?

Terraform state is Terraform's record of the infrastructure it manages: a mapping between the resources you declare in configuration and the real objects that exist in your cloud provider, together with their metadata and dependencies. Terraform reads state on every run to decide what to create, update, or destroy, and to detect drift from the live environment.

### What is a Terraform state file?

The Terraform state file is the file that stores that record, named `terraform.tfstate` by default and formatted as JSON. It holds a serial counter, a lineage ID, and the full attribute set of every managed resource. It should be treated as sensitive (it can contain secrets) and should never be committed to version control.

### What does terraform state mv do?

`terraform state mv` renames or relocates a resource within state without destroying and recreating the underlying infrastructure. If you rename a resource in your code or move it into a module, `state mv` updates the state mapping so Terraform recognizes the existing resource under its new address instead of planning a replacement. Run a plan afterward to confirm the move produced no unexpected changes.

### What does terraform state rm do?

`terraform state rm` removes a resource from Terraform state without touching the real infrastructure. Terraform stops managing the resource, but the actual cloud object continues to exist. It's used to hand a resource off to another configuration or to stop tracking something. Because it changes what Terraform owns, point it carefully and verify with a plan.

### Where is Terraform state stored?

By default, state is stored in a local `terraform.tfstate` file in your working directory. For team use, it's stored in a remote backend such as an Amazon S3 bucket, Azure Blob Storage, Google Cloud Storage, or HCP Terraform. Remote backends add shared access and locking so multiple people can work safely against the same state.

### How do you secure Terraform state?

Store state in a remote backend with encryption at rest and in transit, restrict access with least-privilege IAM, enable versioning so you can recover from corruption, and enable locking to prevent concurrent writes. Keep the state file out of version control. Note that Terraform's `sensitive` flag redacts CLI output but does not encrypt values in the state file itself; OpenTofu adds native client-side state encryption, and Pulumi encrypts secret values before they are written to state. See [secrets management](/what-is/what-is-secrets-management/) for broader practices.

### What is the difference between Terraform state and Pulumi state?

Both tools keep state to map declarations to real resources, but the defaults differ. Terraform writes state to a local file by default and can store secrets in plaintext unless the backend encrypts them, and locking depends on the backend you configure. Pulumi defaults to a fully managed, locked backend (Pulumi Cloud), encrypts secret values before writing them to state, and also supports self-managed object-storage backends. The [Pulumi vs. Terraform comparison](/docs/iac/comparisons/terraform/) covers the differences in depth.

### Can Terraform manage resources it didn't create?

Yes. `terraform import` (or a declarative `import` block in newer versions) brings an existing, unmanaged cloud resource into Terraform state under a specified address, after which Terraform manages it normally. Pulumi offers an equivalent workflow through [importing existing resources](/docs/iac/guides/migration/import/).

## Learn more

Pulumi manages state for you: Pulumi Cloud stores, versions, and locks state automatically, and encrypts secret values before they ever reach the state file, so sensitive data is never sitting in plaintext. You can also self-host state in S3, Azure Blob, GCS, or the local filesystem while keeping the same encryption model. [Read about state and backends](/docs/iac/concepts/state-and-backends/) to see how it works.

Related reading:

* [State and backends](/docs/iac/concepts/state-and-backends/)
* [Secrets handling](/docs/iac/concepts/secrets/)
* [Importing existing resources](/docs/iac/guides/migration/import/)
* [Pulumi vs. Terraform](/docs/iac/comparisons/terraform/)
* [Terraform-to-Pulumi terminology](/docs/iac/comparisons/terraform/#terraform-terms-and-command-equivalents)
* [What is infrastructure as code?](/what-is/what-is-infrastructure-as-code/)
* [What is a Terraform module?](/what-is/what-is-a-terraform-module/)
* [What is Terragrunt?](/what-is/what-is-terragrunt/)
* [What is infrastructure drift?](/what-is/what-is-infrastructure-drift/)
* [What is secrets management?](/what-is/what-is-secrets-management/)
</content>
</invoke>
