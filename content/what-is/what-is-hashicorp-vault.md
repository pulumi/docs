---
title: What is HashiCorp Vault?
meta_desc: "HashiCorp Vault is an identity-based secrets and encryption management system. Learn its basics and how it pairs with Pulumi ESC."
meta_image: /images/what-is/what-is-hashicorp-vault-meta.png
type: what-is
page_title: "What is HashiCorp Vault?"
authors: ["james-denyer"]
---

**HashiCorp Vault is an identity-based secrets and encryption management system that stores, generates, and brokers access to credentials, encryption keys, and certificates for applications, machines, and humans.** It's distributed as open source software (Community edition) and as a commercial product (Vault Enterprise and HCP Vault Dedicated), and is one of the most widely deployed secrets managers in production environments.

Vault's defining feature is the *secrets engine*: a pluggable backend that doesn't just store credentials, but generates them on demand with short lifetimes. A request for a database credential, an AWS IAM role, or a PKI certificate returns a freshly-minted credential scoped to the requester, valid for minutes or hours, and revoked automatically when the lease expires. Vault sits well in multi-cloud, hybrid, and on-premises environments because it isn't tied to any single cloud provider. [Pulumi ESC](/product/esc/) integrates with Vault as a [secrets provider](/docs/pulumi-cloud/esc/providers/vault-secrets/), pulling Vault-managed secrets into Pulumi programs, CI jobs, and applications through a single brokered interface.

In this article, we'll cover the key questions about HashiCorp Vault:

* Why do teams use HashiCorp Vault?
* What are Vault's core components?
* What are secrets engines?
* What is the difference between static and dynamic secrets?
* Which Vault edition should I use?
* How does Vault compare to AWS Secrets Manager, Azure Key Vault, and GCP Secret Manager?
* How does Vault handle authentication?
* What are Vault's deployment options?
* How does Pulumi ESC integrate with HashiCorp Vault?
* Frequently asked questions about HashiCorp Vault

## Why do teams use HashiCorp Vault?

Vault is most often chosen for three reasons that the cloud-native vaults don't fully cover.

### Cloud-agnostic, multi-cloud secrets management

A single Vault cluster can broker secrets across AWS, Azure, GCP, on-premises, and SaaS. For organizations that span more than one cloud, that uniform interface is the alternative to running three different cloud-native vaults with three different access models.

### Dynamic, short-lived credentials by default

Vault's database, cloud IAM, PKI, and SSH secrets engines generate credentials on demand and revoke them on lease expiration. Many of the recurring credential-leak patterns — long-lived API keys, shared database passwords, certificates that outlive the service that requested them — simply don't exist when credentials are minted per-request.

### Transit engine for encryption-as-a-service

Vault's transit engine lets applications encrypt and decrypt data without ever holding the underlying key. The data goes to Vault, the ciphertext comes back, and the key never leaves. It's the basis for application-layer encryption and customer-managed-key patterns where the cloud KMS isn't a fit.

## What are Vault's core components?

A Vault deployment is built from a small set of well-defined pieces:

* **Vault server.** The process that holds the cipher and brokers all secret operations. Runs in HA clusters of three or five nodes in production.
* **Storage backend.** Persistent storage for encrypted secret data (Integrated Storage / Raft is the standard choice; older deployments may use Consul, etcd, or cloud blob storage).
* **Seal.** The mechanism that protects the master encryption key. Auto-unseal with a cloud KMS (AWS KMS, Azure Key Vault, GCP Cloud KMS) or HSM is standard in production; Shamir's Secret Sharing is the manual fallback.
* **Auth methods.** How clients prove who they are: tokens, AppRole, AWS IAM, Azure, GCP, Kubernetes service accounts, OIDC, LDAP, GitHub, and others.
* **Secrets engines.** Pluggable backends that store or generate secrets (KV v2, database, AWS, Azure, GCP, PKI, SSH, transit, Consul, RabbitMQ, and many more).
* **Policies.** HCL-formatted ACLs that say which identities can perform which operations on which paths.
* **Audit devices.** Append-only logs of every request and response, written to file, syslog, or socket.

A Vault interaction is always: authenticate via an auth method, receive a token with attached policies, request a secret from an engine path, receive a leased response, optionally renew or revoke.

## What are secrets engines?

A secrets engine is the pluggable backend that handles a specific class of secret. Vault ships dozens; the ones most production deployments rely on:

| Engine | What it does | Typical use |
|---|---|---|
| **KV v2** | Versioned key/value storage | Static application configuration, passwords, tokens |
| **Database** | Generates short-lived DB credentials | PostgreSQL, MySQL, MongoDB, MSSQL, Snowflake, and others |
| **AWS / Azure / GCP** | Generates short-lived cloud IAM credentials | Per-request cloud access for apps, CI, contractors |
| **PKI** | Issues X.509 certificates from an internal CA | mTLS, service mesh, internal TLS |
| **SSH** | Issues signed SSH certificates or one-time passwords | Just-in-time access to fleet servers |
| **Transit** | Encryption, decryption, signing, key derivation as a service | Application-layer crypto without holding keys |
| **Kubernetes** | Generates service account tokens for K8s clusters | Per-request Kubernetes access |
| **TOTP** | Generates and validates TOTP codes | Programmatic 2FA |

Engines are mounted at paths (`database/`, `pki/internal/`, `aws/team-a/`) and each path has its own policy surface, so two teams can share the same Vault without sharing access to each other's engines.

## What is the difference between static and dynamic secrets?

Vault supports both, and the distinction is one of the things that sets it apart.

| Aspect | Static secrets (KV v2) | Dynamic secrets |
|---|---|---|
| Origin | Stored when a human or system writes them | Generated on demand by an engine |
| Lifetime | Indefinite until rotated | Lease-bound; typically minutes to hours |
| Revocation | Manual (overwrite or delete) | Automatic on lease expiration; can be revoked early |
| Audit | Read events logged | Issue, renew, and revoke events logged |
| Best for | API keys to third-party SaaS, application config | Databases, cloud IAM, PKI, SSH, RabbitMQ, message brokers |

In a mature Vault deployment, anything that *can* be a dynamic secret usually is. The recurring credential-leak risk shrinks to the smaller set of static secrets that have to be entered by hand.

## Which Vault edition should I use?

HashiCorp publishes three packagings of the same core:

| Edition | Hosting | Licensing | Notable features |
|---|---|---|---|
| **Vault Community** | Self-hosted | MPL 2.0 / BUSL 1.1 (post-August 2023 releases) | Core engines, auth methods, storage backends, HA |
| **Vault Enterprise** | Self-hosted | Commercial | Performance replication, DR replication, namespaces, HSM auto-unseal, FIPS 140-2, Sentinel policy, MFA, control groups |
| **HCP Vault Dedicated** | HashiCorp-managed | Subscription | Fully managed Vault Enterprise clusters in AWS or Azure |

Community Vault is fine for many production deployments. Enterprise becomes the right choice when you need multi-tenancy via namespaces, geographic replication, FIPS-validated cryptography, or HashiCorp's commercial support. HCP Vault Dedicated removes the operational burden of running the cluster yourself.

Note that HashiCorp re-licensed Vault from the Mozilla Public License to the Business Source License (BUSL) in August 2023. The OpenBao project, hosted by the Linux Foundation, is an MPL-licensed fork of the Community edition for organizations that need the older license.

## How does Vault compare to AWS Secrets Manager, Azure Key Vault, and GCP Secret Manager?

| Capability | HashiCorp Vault | [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/) | [Azure Key Vault](/what-is/what-is-azure-key-vault/) | [Google Cloud Secret Manager](/what-is/what-is-google-cloud-secret-manager/) |
|---|---|---|---|---|
| Deployment | Self-hosted or HCP managed | Fully managed (AWS) | Fully managed (Azure) | Fully managed (GCP) |
| Cloud scope | Multi-cloud, hybrid, on-prem | AWS-native | Azure-native | GCP-native |
| Dynamic secrets | Many engines (DB, cloud IAM, PKI, SSH) | Lambda-driven rotation | Limited (via Functions) | Manual rotation |
| Encryption as a service | Yes (transit) | No (use KMS separately) | No (use Key Vault keys separately) | No (use Cloud KMS separately) |
| Pricing | OSS free; Enterprise per-cluster; HCP per-hour | Per secret/month + API calls | Per operation; HSM per key | Per active secret version + access ops |
| Best fit | Multi-cloud, hybrid, encryption needs | AWS-centric workloads | Azure-centric workloads | GCP-centric workloads |

Vault is the most flexible of the four and the only one that runs anywhere. The cloud-native vaults are simpler when the workload is entirely inside their respective cloud. Many organizations use Vault *and* one of the cloud vaults — and use [Pulumi ESC](/product/esc/) to compose them.

## How does Vault handle authentication?

Every Vault operation requires a token. Tokens are issued either directly or by an auth method that maps an external identity to a token. The most common auth methods:

* **AppRole.** Role-id + secret-id pair for machine identity. Common for services that aren't running in a cloud with native identity.
* **AWS, Azure, GCP IAM.** A workload running in a cloud presents its native identity (EC2 instance profile, Azure managed identity, GCP service account) and gets back a Vault token. No static secret to manage.
* **Kubernetes.** A pod's service account token is exchanged for a Vault token. Pairs well with the Vault Agent Injector.
* **OIDC / JWT.** Federates with corporate IdPs (Okta, Azure AD, Google Workspace) and CI systems (GitHub Actions, GitLab) that issue JWT identities.
* **LDAP / userpass / GitHub.** Direct authentication for human users when an IdP isn't available.
* **TLS certificates.** Mutual TLS for machine authentication.

Once authenticated, the resulting token carries a set of policies that determine what the holder can read, write, or generate. Tokens have TTLs and can be revoked.

## What are Vault's deployment options?

Three common shapes:

1. **Self-hosted on-cluster.** A three- or five-node HA cluster on Kubernetes, EC2, or bare metal with Integrated Storage (Raft) and cloud-KMS auto-unseal. The default for organizations that want full control.
1. **HCP Vault Dedicated.** HashiCorp-operated Vault Enterprise clusters in AWS or Azure. You get the Enterprise feature set without operating the cluster.
1. **Vault Agent / Vault Secrets Operator.** Sidecar (Vault Agent) or operator (VSO) that runs inside Kubernetes and projects Vault secrets into pod filesystems or Kubernetes Secrets. The standard pattern for application consumption of Vault.

In production, expect to run the cluster behind a load balancer, with TLS terminated at the Vault listener, audit logs shipped to a SIEM, and either Vault Enterprise replication or a documented DR procedure across regions.

## How does Pulumi ESC integrate with HashiCorp Vault?

Pulumi ESC pulls secrets and configuration from many sources, including HashiCorp Vault, and exposes a single audited interface to Pulumi programs, CI jobs, and applications. The [Vault Secrets provider](/docs/pulumi-cloud/esc/providers/vault-secrets/) and the [HCP Vault Secrets provider](/docs/pulumi-cloud/esc/providers/hcp-vault-secrets/) let an ESC environment read from a self-hosted Vault cluster or HCP Vault Secrets respectively.

Concrete patterns:

* **Compose Vault with other vaults.** A single ESC environment can read database credentials from Vault's database engine, an AWS credential via OIDC, and a CMEK reference from GCP Secret Manager.
* **Broker Vault secrets to non-Vault consumers.** An application or CI job that doesn't speak the Vault API can still consume Vault secrets through ESC's standard environment-variable or file output.
* **Layer environments.** A `production-base` environment can mount common Vault paths; a `production-team-a` environment can extend it with team-specific paths.
* **End-to-end audit.** Every ESC read logs identity, timestamp, and the underlying Vault path that was fetched.

Pulumi also publishes a [Vault Pulumi provider](/registry/packages/vault/) for declaring Vault configuration (auth methods, policies, secrets engines, namespaces) as Pulumi code.

## Frequently asked questions about HashiCorp Vault

### Is HashiCorp Vault free?

Vault Community is free under the Business Source License (BUSL 1.1) as of August 2023; older releases were MPL 2.0. Vault Enterprise and HCP Vault Dedicated are commercial. The OpenBao fork, hosted by the Linux Foundation, is MPL-licensed for organizations that need the original license.

### Is HashiCorp Vault open source?

The Community edition's source is publicly available, but BUSL is not an OSI-approved open source license. After a four-year change date, BUSL-licensed code reverts to MPL 2.0. OpenBao is a true open source (MPL 2.0) fork of pre-BUSL Vault.

### Can Vault generate database credentials?

Yes. The database secrets engine creates short-lived database credentials on demand, with a Vault-managed root credential, configurable TTLs, and automatic revocation on lease expiration. Supported databases include PostgreSQL, MySQL, MongoDB, MSSQL, Oracle, Snowflake, Cassandra, Redis, and others.

### How does Vault handle high availability?

Vault clusters run three or five nodes with Integrated Storage (Raft) for HA. One node is the active leader; the others are standby. Failover is automatic on leader loss. Vault Enterprise adds Performance Replication (read replicas in other regions) and Disaster Recovery Replication (warm-standby clusters that can be promoted).

### What is the difference between Vault and Consul?

Both are HashiCorp tools, but they solve different problems. Consul is a service-discovery and service-mesh tool that also offers a key/value store for configuration. Vault is a secrets manager. The two integrate cleanly — Consul is a supported storage backend for Vault, and Vault can issue mTLS certificates for Consul Connect — but neither replaces the other.

### Is Vault FIPS 140-2 compliant?

Vault Enterprise ships a FIPS 140-2 validated build (Vault Enterprise + HSM) that uses FIPS-validated cryptographic modules. Community Vault is not FIPS-validated. HCP Vault Dedicated offers FIPS-compliant cluster tiers.

### Does Vault support HIPAA and SOC 2 workloads?

Yes. HashiCorp publishes a current SOC 2 Type II for the HCP services, and Vault's audit, access-control, and encryption capabilities map cleanly onto HIPAA Security Rule technical safeguards. Vault is a common substrate for both. See [What is HIPAA?](/what-is/what-is-hipaa/) and [What is SOC 2?](/what-is/what-is-soc-2/) for the broader framework context.

### How do I rotate the Vault root token?

Run `vault token revoke` against the active root token after generating a new one via `vault operator generate-root` and a quorum of unseal keys (or the recovery keys when using auto-unseal). The general guidance is to use root tokens only for initial setup and break-glass, and to manage day-to-day operations with policy-scoped tokens.

### Can I migrate from Vault to AWS Secrets Manager (or vice versa)?

Yes, though both directions are usually a one-time export-and-import. For AWS-centric workloads, AWS Secrets Manager removes the Vault operational burden; for multi-cloud or encryption-as-a-service needs, Vault is the destination. [Pulumi ESC](/product/esc/) often eliminates the need to migrate at all, by sitting above both and brokering secrets from each.

### How does Vault Agent compare to the Vault Secrets Operator?

Vault Agent is a sidecar that authenticates to Vault, fetches secrets, and renders them into files inside the pod. The Vault Secrets Operator (VSO) runs as a Kubernetes controller that reads secrets from Vault and projects them as Kubernetes Secret resources. Agent is the older, more flexible pattern; VSO is simpler for teams that want secrets to flow into the standard Kubernetes Secret API.

## Learn more

Pulumi works hand-in-hand with HashiCorp Vault: ESC composes Vault secrets with other vaults under a single audited interface, and the [Vault Pulumi provider](/registry/packages/vault/) lets you declare Vault configuration as code. [Get started with Pulumi ESC](/docs/pulumi-cloud/esc/) to broker Vault secrets to your Pulumi programs, CI jobs, and applications.

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Azure Key Vault?](/what-is/what-is-azure-key-vault/)
* [What is Google Cloud Secret Manager?](/what-is/what-is-google-cloud-secret-manager/)
* [What is Cloud Security?](/what-is/what-is-cloud-security/)
* [What is SOC 2?](/what-is/what-is-soc-2/)
