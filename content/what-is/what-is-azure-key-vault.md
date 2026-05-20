---
title: What is Azure Key Vault?
meta_desc: "Azure Key Vault is a managed service for storing keys, secrets, and certificates. Learn the Standard, Premium, and Managed HSM tiers, RBAC, and how Pulumi ESC fits."
meta_image: /images/what-is/what-is-azure-key-vault-meta.png
type: what-is
page_title: "What is Azure Key Vault?"
authors: ["torian-crane"]
---

**Azure Key Vault is a Microsoft Azure managed service for securely storing and tightly controlling access to cryptographic keys, secrets (passwords, API keys, connection strings), and X.509 certificates.** Access is governed by Microsoft Entra ID identity and either Azure RBAC or Key Vault access policies; usage is audited through Azure Monitor and Microsoft Defender for Cloud.

Key Vault is the default secrets store for Azure-centric workloads because it integrates natively with everything else in Azure — Managed Identity, App Service, Azure Kubernetes Service (AKS), Azure DevOps, Azure Functions, and the Microsoft Entra identity model. It comes in three packagings (Standard, Premium, and Managed HSM) that differ in cryptographic backing and FIPS validation level. [Pulumi ESC](/product/esc/) integrates with Key Vault as a [secrets provider](/docs/pulumi-cloud/esc/providers/azure-secrets/), pulling Key Vault values into Pulumi programs, CI jobs, and applications through a single audited interface.

In this article, we'll cover the key questions about Azure Key Vault:

* Why do teams use Azure Key Vault?
* What does Azure Key Vault actually store?
* What are the Standard, Premium, and Managed HSM tiers?
* How do RBAC and access policies differ?
* How does Azure Key Vault compare to other vaults?
* How does authentication work?
* How does Key Vault integrate with the rest of Azure?
* How does pricing work?
* How does Pulumi ESC integrate with Azure Key Vault?
* Frequently asked questions about Azure Key Vault

## Why do teams use Azure Key Vault?

Three durable reasons.

### Native Microsoft Entra ID and Managed Identity integration

A workload running on App Service, Azure Functions, AKS, or a VM can authenticate to Key Vault as itself using a Managed Identity — no client secret, no certificate to rotate, no key buried in configuration. Identity-based access is the substrate the rest of Azure security depends on.

### FIPS 140-2 validated HSM tier

Azure Key Vault Premium stores keys in a multi-tenant FIPS 140-2 Level 2 HSM. Azure Key Vault Managed HSM is a single-tenant FIPS 140-2 Level 3 HSM. For workloads that need validated cryptographic boundaries, Managed HSM is the Azure-native answer.

### One service for keys, secrets, and certificates

A single vault holds three related-but-distinct asset types: cryptographic keys, secret values, and certificates (with their private keys). The certificate-management features (auto-renewal, lifecycle policies, integration with public CAs like DigiCert) are particularly hard to replicate in a generic secrets store.

## What does Azure Key Vault actually store?

A Key Vault holds three classes of asset:

* **Keys.** Asymmetric (RSA, EC) and symmetric (AES, with Managed HSM) cryptographic keys. Operations include encrypt, decrypt, sign, verify, wrap, and unwrap. Keys can be HSM-backed or software-backed depending on tier.
* **Secrets.** Arbitrary byte strings (up to 25 KB) with versioning, enabled/disabled state, and optional expiration. Used for passwords, API keys, connection strings, OIDC client secrets, and similar.
* **Certificates.** X.509 certificates with their private keys, including lifecycle management (auto-renewal with a configured issuer, periodic notifications) and integration with public CAs like DigiCert and GlobalSign for managed certificate issuance.

All three are scoped to a vault, addressed by URL, and accessed through the same RBAC or access-policy model.

## What are the Standard, Premium, and Managed HSM tiers?

Azure Key Vault is offered in three SKUs:

| Tier | Cryptographic backing | FIPS validation | Tenancy | Best for |
|---|---|---|---|---|
| **Standard** | Software-protected | Module: FIPS 140-2 Level 1 | Multi-tenant | General-purpose secrets, certificates, and software-protected keys |
| **Premium** | HSM-protected (multi-tenant nCipher HSMs) | FIPS 140-2 Level 2 | Multi-tenant | Workloads that need HSM-backed keys without a dedicated HSM |
| **Managed HSM** | HSM-protected (single-tenant) | FIPS 140-2 Level 3 | Single-tenant pool of three HSMs | Workloads with strict cryptographic-boundary or sovereignty requirements |

Standard and Premium share the same control plane; Managed HSM is a separate service with its own data plane API and a different cost model. Most organizations start with Standard and move to Premium or Managed HSM only when an explicit compliance requirement demands it.

## How do RBAC and access policies differ?

Azure Key Vault supports two authorization models. Choose one per vault.

| Aspect | Azure RBAC | Access policies |
|---|---|---|
| Identity model | Microsoft Entra ID + Azure RBAC role assignments | Per-vault list of identities and permissions |
| Granularity | Per role; scoped to vault, key, secret, or certificate | Per identity; coarse vault-level grant per operation type |
| Permissions style | Role definitions (built-in or custom) | List of allowed operations per identity |
| Cross-subscription use | First-class | Limited (must add the identity directly) |
| Auditability | Surfaces in standard Azure activity logs and access reviews | Surfaces in standard Azure activity logs |
| Recommendation | **Microsoft-recommended default** | Legacy model, still supported |

Microsoft recommends RBAC for new vaults because it inherits the rest of Azure's role-assignment, conditional-access, and access-review tooling. Access policies remain supported for backward compatibility.

## How does Azure Key Vault compare to other vaults?

| Capability | Azure Key Vault | [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/) | [HashiCorp Vault](/what-is/what-is-hashicorp-vault/) | [Google Cloud Secret Manager](/what-is/what-is-google-cloud-secret-manager/) |
|---|---|---|---|---|
| Hosting | Fully managed (Azure) | Fully managed (AWS) | Self-hosted or HCP managed | Fully managed (GCP) |
| Cloud scope | Azure-native | AWS-native | Multi-cloud, hybrid, on-prem | GCP-native |
| Stores certificates | Yes, with auto-renewal | Limited (no managed lifecycle) | Yes (PKI engine issues, not stores) | No (use Certificate Manager separately) |
| HSM option | Premium (multi-tenant), Managed HSM (single-tenant FIPS 140-2 L3) | KMS Custom Key Stores | Vault Enterprise + HSM | Cloud HSM via CMEK |
| Built-in rotation | Certificates (built-in); secrets via Functions or Event Grid | Yes (RDS, Redshift, DocumentDB; Lambda for others) | Yes (dynamic secrets engines) | Not built-in |
| Best fit | Azure-centric workloads | AWS-centric workloads | Multi-cloud | GCP-centric workloads |

For workloads on Azure, Key Vault is almost always the right default. For multi-cloud or hybrid deployments, organizations frequently pair it with HashiCorp Vault and use [Pulumi ESC](/product/esc/) to compose both under a single interface.

## How does authentication work?

Every Key Vault operation requires a Microsoft Entra ID identity. The common patterns:

* **Managed Identity.** A system-assigned or user-assigned identity attached to an Azure resource (VM, App Service, Function, AKS pod via Workload Identity). No secret to manage; Azure handles token acquisition.
* **Service principal.** An Entra ID application identity with either a client secret or a certificate. Used for workloads that can't use Managed Identity.
* **Workload Identity Federation.** External identities (GitHub Actions, GitLab, AWS, GCP, custom OIDC) federated to an Entra ID app registration via OIDC. Removes the need for long-lived client secrets in external systems.
* **User identity.** Developers and administrators authenticate directly through `az login`, Visual Studio, or the Azure portal.

Once authenticated, the identity's RBAC role assignments or access policies determine what it can do. Tokens are short-lived; the Azure SDKs handle refresh transparently.

## How does Key Vault integrate with the rest of Azure?

A short list of the integrations that make Key Vault load-bearing in Azure architectures:

* **App Service / Functions.** Reference a Key Vault secret directly in an application setting via `@Microsoft.KeyVault(SecretUri=...)`; the runtime fetches it at startup using the resource's Managed Identity.
* **Azure Kubernetes Service.** The [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/) plus the Azure Key Vault provider mount Key Vault secrets into pod filesystems. Workload Identity provides the AKS-to-Key-Vault auth.
* **Azure DevOps and GitHub Actions.** Pipelines pull secrets from Key Vault at run time using a service connection or OIDC federation, removing the need to store long-lived credentials in the pipeline.
* **Azure SQL, Cosmos DB, Storage, Service Bus.** Customer-managed keys (CMK) for encryption-at-rest reference a key in Key Vault.
* **Microsoft Defender for Cloud.** Surfaces misconfigurations (public access, missing logging, weak access policies) and recommends fixes.

## How does pricing work?

Pricing differs by tier:

1. **Standard.** Per-operation pricing on secrets, keys, and certificates. There is no per-vault charge — you pay for what you call.
1. **Premium.** Per-operation pricing for secrets and certificates; per-key-per-month plus per-operation pricing for HSM-protected keys.
1. **Managed HSM.** Per-instance, per-hour pricing for the HSM pool (one or more pools of three HSMs), plus per-key-per-month and per-operation charges.

Always consult the [Azure Key Vault pricing page](https://azure.microsoft.com/en-us/pricing/details/key-vault/) for current rates; some Region- and tier-specific differences apply. The cost model means that vaults with very high read volume should cache secrets in memory between calls.

## How does Pulumi ESC integrate with Azure Key Vault?

[Pulumi ESC](/product/esc/) treats Azure Key Vault as one of many secret sources. The [Azure Secrets provider](/docs/pulumi-cloud/esc/providers/azure-secrets/) reads secrets from Key Vault into an ESC environment, which then brokers them to Pulumi programs, CI jobs, and applications.

Concrete patterns:

* **Dynamic Azure credentials via OIDC.** ESC mints short-lived Azure credentials at the moment a consumer opens the environment, removing the need for long-lived client secrets anywhere. See the [azure-login provider](/docs/pulumi-cloud/esc/providers/azure-login/).
* **Compose with other vaults.** A single ESC environment can pull a connection string from Azure Key Vault, a database credential from HashiCorp Vault, and an OIDC client secret from AWS Secrets Manager.
* **Broker secrets to non-Azure consumers.** Workloads running outside Azure can read Key Vault secrets through ESC without managing their own Entra ID app registration and client secret.
* **Audit trail unification.** ESC logs every environment open with identity and timestamp; Key Vault still records the underlying API call in Azure Monitor. The two together produce a complete chain of custody.

The [azure-native.keyvault Pulumi resource](/registry/packages/azure-native/api-docs/keyvault/secret/) lets you define and manage Key Vault resources as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about Azure Key Vault

### What is the difference between Azure Key Vault Standard and Premium?

Standard stores keys in software (FIPS 140-2 Level 1); Premium stores them in a multi-tenant HSM (FIPS 140-2 Level 2). Secrets and certificates behave the same on both tiers. Pick Premium when an explicit compliance requirement demands HSM-backed keys.

### What is Azure Key Vault Managed HSM?

Managed HSM is a separate single-tenant service that provides a dedicated, FIPS 140-2 Level 3 HSM pool of three HSMs. It has its own control and data planes, its own RBAC model, and per-instance hourly pricing. It's the choice for sovereign-cryptography and strict-boundary workloads.

### Should I use Azure RBAC or access policies?

Azure RBAC. Microsoft recommends it for new vaults because it inherits the rest of Azure's role assignment, conditional access, and access review tooling. Access policies are still supported but are the older model.

### Can I rotate secrets automatically in Azure Key Vault?

For *certificates*, yes — Key Vault renews automatically with a configured issuer. For *secrets*, there's no built-in scheduler; the standard pattern is an Azure Function on a timer or an Event Grid event that runs custom rotation logic and writes a new version. For database passwords specifically, Microsoft also publishes sample rotation Functions.

### How is Azure Key Vault different from Azure Managed HSM?

Key Vault is a multi-tenant service with software-backed and HSM-backed keys (Standard and Premium). Managed HSM is a separate single-tenant service backed exclusively by FIPS 140-2 Level 3 HSMs. Most organizations use Key Vault Standard or Premium and only adopt Managed HSM when validated boundaries are required.

### Is Azure Key Vault HIPAA-compliant?

Azure Key Vault is in scope for Microsoft's HIPAA Business Associate Agreement and the Azure HITRUST CSF certification. It's also in scope for SOC 1, SOC 2, ISO 27001, ISO 27018, FedRAMP High, PCI DSS, and several other Azure compliance offerings. See the [Azure compliance documentation](https://learn.microsoft.com/en-us/azure/compliance/) for the current list.

### How does Key Vault work with AKS?

Most teams use the [Secrets Store CSI Driver](https://secrets-store-csi-driver.sigs.k8s.io/) with the Azure Key Vault provider. The driver mounts Key Vault secrets into the pod filesystem at startup; authentication uses AKS Workload Identity (or, on older clusters, AAD Pod Identity).

### How do I share a secret across Azure subscriptions?

The vault is in one subscription, but Microsoft Entra ID identities from any subscription (or tenant) can be granted RBAC access to it. Cross-tenant access requires guest-user invitations or B2B collaboration. For automation, federation via Workload Identity Federation is the modern path.

### Can I migrate from Azure Key Vault to HashiCorp Vault?

Yes, though it's a one-time export-and-import. List the vault's contents via the Azure CLI, fetch each secret, key, and certificate, and write them into Vault's KV v2 or PKI engines as appropriate. [Pulumi ESC](/product/esc/) often makes migration unnecessary by sitting above both and brokering whichever vault each secret happens to live in.

### What is soft-delete and purge protection in Key Vault?

Soft-delete keeps deleted vaults and assets recoverable for 7 to 90 days (90 by default for new vaults). Purge protection prevents anyone — including subscription owners — from purging a soft-deleted vault before the retention window expires. Both are enabled by default on new vaults and are required for several Azure services that store CMKs.

## Learn more

Pulumi makes Azure Key Vault part of a coherent secrets program: [Pulumi ESC](/docs/pulumi-cloud/esc/) brokers Key Vault values to Pulumi programs, CI jobs, and applications under a single audited interface, and the [Pulumi Azure Native provider](/registry/packages/azure-native/) lets you declare every Key Vault, secret, key, and certificate as code in TypeScript, Python, Go, C#, Java, or YAML.

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Google Cloud Secret Manager?](/what-is/what-is-google-cloud-secret-manager/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
