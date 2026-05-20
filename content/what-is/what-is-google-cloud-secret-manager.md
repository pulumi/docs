---
title: What is Google Cloud Secret Manager?
meta_desc: "Google Cloud Secret Manager is a managed service for storing and accessing secrets in GCP. Learn its versioning, replication, IAM model, and how Pulumi ESC fits."
meta_image: /images/what-is/what-is-google-cloud-secret-manager-meta.png
type: what-is
page_title: "What is Google Cloud Secret Manager?"
authors: ["torian-crane"]
---

**Google Cloud Secret Manager is a fully managed Google Cloud Platform service for securely storing, versioning, and accessing API keys, passwords, certificates, and other sensitive data.** Secrets are encrypted at rest with Google-managed or customer-managed encryption keys (CMEK), access is controlled by Google Cloud IAM, and every API call is recorded in Cloud Audit Logs.

Secret Manager is the default secrets store for Google Cloud-centric workloads. It integrates natively with Cloud Run, Google Kubernetes Engine (GKE), Compute Engine, Cloud Build, and Cloud Functions, and it uses the same project-and-IAM model as the rest of Google Cloud. Unlike AWS Secrets Manager, it doesn't have a built-in rotation engine; rotation is implemented by the workload (often a Cloud Function on a Cloud Scheduler trigger). [Pulumi ESC](/product/esc/) integrates with Secret Manager as a [secrets provider](/docs/pulumi-cloud/esc/providers/gcp-secrets/), pulling Secret Manager values into Pulumi programs, CI jobs, and applications through a single audited interface.

In this article, we'll cover the key questions about Google Cloud Secret Manager:

* Why do teams use Google Cloud Secret Manager?
* What are the core features?
* How does secret versioning work?
* What replication policies are available?
* How does Secret Manager compare to other vaults?
* How does IAM and access control work?
* How does Secret Manager integrate with the rest of Google Cloud?
* How does pricing work?
* How does Pulumi ESC integrate with Google Cloud Secret Manager?
* Frequently asked questions about Google Cloud Secret Manager

## Why do teams use Google Cloud Secret Manager?

Three durable reasons.

### Native IAM and Cloud Audit Logs integration

Access is governed by Google Cloud IAM at the project, secret, or version level. Every read, write, and admin operation is logged to Cloud Audit Logs with the principal that performed it. Workload Identity Federation extends this model to identities outside Google Cloud (GitHub Actions, AWS, Azure, on-prem).

### Versioning and immutability by default

Each new secret value creates a new immutable *version*. Versions can be enabled, disabled, or destroyed, but existing version values never change. That makes rollback trivial and makes drift detection straightforward.

### Customer-managed encryption keys (CMEK)

Secret Manager supports CMEK using Cloud KMS keys, including keys backed by Cloud HSM (FIPS 140-2 Level 3). Organizations with strict cryptographic-control requirements can manage the encryption key themselves while still using the managed Secret Manager service.

## What are the core features?

| Feature | What it does |
|---|---|
| **Encryption at rest** | AES-256 with Google-managed keys or CMEK from Cloud KMS |
| **Encryption in transit** | TLS for all API calls |
| **IAM-based access control** | Project, secret, or version-level role bindings; Workload Identity Federation for external identities |
| **Versioning** | Each new secret value is an immutable version with an integer ID; latest alias resolves to the most recent enabled version |
| **Replication policies** | Automatic (Google-chosen Regions) or user-managed (you list the Regions) |
| **Audit logging** | Admin and (when enabled) data-access logs to Cloud Audit Logs |
| **CMEK support** | Customer-managed encryption keys via Cloud KMS, including Cloud HSM |
| **VPC Service Controls** | Restrict Secret Manager access to a defined perimeter |
| **Rotation hooks** | Notification topic on a configurable schedule; rotation logic runs in your code |

A secret in Secret Manager is a named container of one or more immutable versions, addressable by name (`projects/<project>/secrets/<name>/versions/<version>`).

## How does secret versioning work?

Every write creates a new version with a monotonically increasing integer ID. Versions are immutable; they can be enabled (readable), disabled (still stored, not readable), or destroyed (permanently deleted). Properties of the version model:

* **`latest` alias.** Reads of `secrets/<name>/versions/latest` resolve to the most recent enabled version.
* **Stable references.** Workloads that need deterministic rollback can pin to a specific version ID.
* **No mutation.** Updating a secret never modifies an existing version — it creates a new one.
* **Audit trail per version.** Each version's create, enable, disable, and destroy events are recorded.

A version is independent of its replication policy: replicated secrets distribute their versions across all chosen Regions; user-managed-replication secrets store each version in the listed Regions.

## What replication policies are available?

When you create a secret, you choose one of two replication policies. The choice is permanent for that secret.

| Policy | Behavior | Best for |
|---|---|---|
| **Automatic** | Google replicates the secret across multiple Regions of its choosing | General-purpose secrets, default for most workloads |
| **User-managed** | You explicitly list the Regions for replication | Workloads that need to control data residency or that depend on Regional CMEK keys |

Automatic replication is the simplest and is what most teams use. User-managed replication is necessary when data-residency requirements pin the data to specific countries or when the secret is encrypted with a Regional CMEK. Replication policies cannot be changed after secret creation.

## How does Secret Manager compare to other vaults?

| Capability | Google Cloud Secret Manager | [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/) | [Azure Key Vault](/what-is/what-is-azure-key-vault/) | [HashiCorp Vault](/what-is/what-is-hashicorp-vault/) |
|---|---|---|---|---|
| Hosting | Fully managed (GCP) | Fully managed (AWS) | Fully managed (Azure) | Self-hosted or HCP managed |
| Cloud scope | GCP-native | AWS-native | Azure-native | Multi-cloud, hybrid, on-prem |
| Built-in rotation | No; notification topic + your own code | Yes (RDS, Redshift, DocumentDB; Lambda for others) | Certificates (built-in); secrets via Functions | Yes (dynamic secrets engines) |
| Certificate storage | Use Certificate Manager separately | Limited (no managed lifecycle) | Yes (with auto-renewal) | Yes (PKI engine issues) |
| HSM option | Cloud HSM via CMEK (FIPS 140-2 Level 3) | KMS Custom Key Stores | Premium (multi-tenant), Managed HSM (single-tenant) | Vault Enterprise + HSM |
| Best fit | GCP-centric workloads | AWS-centric workloads | Azure-centric workloads | Multi-cloud |

For workloads on GCP, Secret Manager is almost always the right default. For multi-cloud or hybrid deployments, organizations frequently pair it with HashiCorp Vault and use [Pulumi ESC](/product/esc/) to compose both under a single interface.

## How does IAM and access control work?

Secret Manager uses standard Google Cloud IAM. The model has three useful scopes:

1. **Project-level binding.** "Anyone with `roles/secretmanager.secretAccessor` on this project can read every secret in it." Coarse, simple, the wrong default for production.
1. **Secret-level binding.** "Service account A has `roles/secretmanager.secretAccessor` on this specific secret." Recommended baseline.
1. **Version-level binding.** Same role applied to a specific version. Useful for migration or emergency rollback.

The standard predefined roles:

* `roles/secretmanager.viewer` — list and describe secrets, but not read values.
* `roles/secretmanager.secretAccessor` — read secret values.
* `roles/secretmanager.secretVersionAdder` — add new versions.
* `roles/secretmanager.secretVersionManager` — manage versions (enable, disable, destroy).
* `roles/secretmanager.admin` — full control.

Workload Identity Federation lets external identities (GitHub Actions, GitLab, AWS, Azure, on-prem) assume a Google service account via OIDC and access Secret Manager without long-lived service account keys.

## How does Secret Manager integrate with the rest of Google Cloud?

The integrations that make Secret Manager load-bearing in GCP architectures:

* **Cloud Run / Cloud Functions.** Reference a secret directly in the service configuration; the runtime mounts it as an environment variable or as a file in `/etc/secrets/`.
* **Google Kubernetes Engine.** The [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/) with the GCP provider mounts Secret Manager values into pod filesystems. Authentication uses GKE Workload Identity.
* **Cloud Build.** Pipelines fetch secrets at build time via `availableSecrets` blocks; secret payloads stay out of build logs.
* **Compute Engine.** VMs use their attached service account to call the Secret Manager API; pair with metadata server-backed authentication.
* **GitHub Actions and other external CI.** Workload Identity Federation issues short-lived service account credentials based on the CI system's OIDC token.
* **Cloud KMS / Cloud HSM.** CMEK and HSM-backed CMEK secure the secret payload encryption key.

## How does pricing work?

Google Cloud Secret Manager pricing has two components:

1. **Per active secret version, per location, per month.** Each enabled version in each Region counts.
1. **Per 10,000 access operations.** A small per-API-call charge applies for reads and other operations.

Always consult the [Secret Manager pricing page](https://cloud.google.com/secret-manager/pricing) for current rates. A modest free tier covers small workloads. Cloud KMS keys used for CMEK are billed separately under KMS pricing. The pricing model means cost scales with the number of versions and replication Regions; consolidating short-lived versions and disabling old ones reduces ongoing cost.

## How does Pulumi ESC integrate with Google Cloud Secret Manager?

[Pulumi ESC](/product/esc/) treats Secret Manager as one of many secret sources. The [GCP Secrets provider](/docs/pulumi-cloud/esc/providers/gcp-secrets/) reads secrets from Secret Manager into an ESC environment, which then brokers them to Pulumi programs, CI jobs, and applications.

Concrete patterns:

* **Dynamic GCP credentials via OIDC.** ESC mints short-lived Google Cloud credentials at the moment a consumer opens the environment, removing the need for long-lived service account keys anywhere. See the [gcp-login provider](/docs/pulumi-cloud/esc/providers/gcp-login/).
* **Compose with other vaults.** A single ESC environment can pull a CMEK key reference from GCP Secret Manager, a database credential from HashiCorp Vault, and an OIDC client secret from AWS Secrets Manager.
* **Broker secrets to non-GCP consumers.** Workloads running outside Google Cloud can read Secret Manager values through ESC without managing their own service account keys.
* **Audit trail unification.** ESC logs every environment open with identity and timestamp; Cloud Audit Logs still records the underlying Secret Manager API call. The two together produce a complete chain of custody.

The [gcp.secretmanager Pulumi resource](/registry/packages/gcp/api-docs/secretmanager/secret/) lets you define and manage Secret Manager resources as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about Google Cloud Secret Manager

### Does Google Cloud Secret Manager rotate secrets automatically?

Not natively. Secret Manager can publish a notification to a Pub/Sub topic on a rotation schedule, and your code (often a Cloud Function triggered by that topic) is responsible for generating the new credential, updating downstream systems, and writing the new version. For most workloads, this is a small amount of code; for managed-database credentials, Google publishes sample rotation functions.

### Is Google Cloud Secret Manager HIPAA-compliant?

Yes. Secret Manager is covered under Google Cloud's HIPAA Business Associate Agreement and is in scope for SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, FedRAMP High, and PCI DSS. See [Google Cloud's compliance documentation](https://cloud.google.com/security/compliance) for the current list.

### What are the size and rate limits?

A secret payload can be up to 65,536 bytes (64 KiB). Default access quotas are 90,000 access requests per minute per project; they can be raised via a quota request. Each project has a default limit on secrets (commonly 1,000,000) that can also be raised. Always check the [Secret Manager quotas docs](https://cloud.google.com/secret-manager/quotas) for current values.

### How is Secret Manager different from Cloud KMS?

Cloud KMS manages cryptographic keys used for encryption and signing. Secret Manager stores arbitrary secret payloads (and uses Cloud KMS under the hood to encrypt them). For an API key or database password, use Secret Manager. For a key used to encrypt application data, use Cloud KMS.

### How do I use Secret Manager from GitHub Actions?

Configure [Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation) between Google Cloud and GitHub Actions, then use the `google-github-actions/auth` action followed by `google-github-actions/get-secretmanager-secrets`. No long-lived service account JSON keys live in GitHub secrets.

### Can I migrate secrets from Secret Manager to HashiCorp Vault?

Yes, though it's a one-time export-and-import. List secrets via `gcloud secrets list`, fetch each value, and write into Vault's KV v2 engine. [Pulumi ESC](/product/esc/) often makes migration unnecessary by sitting above both and brokering whichever vault each secret happens to live in.

### What happens when I destroy a secret version?

The version moves to the `DESTROYED` state and its payload is deleted. The version's ID still exists for audit purposes, but the value is unrecoverable. Reads against a destroyed version return an error. Destruction is permanent — use `disable` instead if you may want to recover the value.

### How does Secret Manager work with GKE Workload Identity?

Map a Kubernetes service account to a Google service account that has `roles/secretmanager.secretAccessor`. Pods running with that KSA can then call the Secret Manager API without any long-lived credentials. The [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/) pairs well for projecting secrets into the pod filesystem.

### What is the difference between automatic and user-managed replication?

Automatic replication lets Google choose the Regions; it's the simplest option and works for most workloads. User-managed replication lets you list the Regions explicitly; it's required when you need data residency control or when you use a Regional CMEK key. Replication policy is permanent for the lifetime of the secret.

### Is data-access logging enabled by default?

No. Admin Activity logs are always on, but Data Access logs (which record `secretmanager.googleapis.com/AccessSecretVersion` calls) are off by default. Enable them in IAM & Admin > Audit Logs if you need a complete per-read audit trail. Data access logs add cost, so most teams enable them on production projects only.

## Learn more

Pulumi makes Google Cloud Secret Manager part of a coherent secrets program: [Pulumi ESC](/docs/pulumi-cloud/esc/) brokers Secret Manager values to Pulumi programs, CI jobs, and applications under a single audited interface, and the [Pulumi Google Cloud provider](/registry/packages/gcp/) lets you declare every secret, version, and IAM binding as code in TypeScript, Python, Go, C#, Java, or YAML.

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
