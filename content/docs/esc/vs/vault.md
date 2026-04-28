---
title_tag: "Pulumi ESC vs HashiCorp Vault: Secrets Management Compared"
meta_desc: "Compare Pulumi ESC and HashiCorp Vault for secrets management. See how ESC's managed SaaS and environment composition compare to Vault."
title: Pulumi ESC vs HashiCorp Vault
h1: Pulumi ESC vs HashiCorp Vault
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    esc:
        name: HashiCorp Vault
        identifier: vault
        parent: esc-vs
        weight: 1
aliases:
---

<style>
    main table {
        font-size: 0.94em;
    }

    main table th,
    main table td {
        width: 33.3%;
    }
</style>

Choosing the right [secrets management](/what-is/what-is-secrets-management/) tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. This page provides a detailed comparison of Pulumi ESC and HashiCorp Vault, covering architecture, developer experience, and security. It also explains how ESC and Vault can work together for teams that have existing Vault deployments.

## At a Glance

**HashiCorp Vault**

- Self-hosted or HCP Vault (requires HA clustering, unsealing, and ongoing upgrades)
- Dynamic secrets engine for databases and select cloud providers
- Business Source License 1.1
- Secrets-only store with no native configuration or environment concept

**Pulumi ESC**

- Fully managed SaaS with zero infrastructure to operate
- Composable environments combining secrets, configuration, and dynamic credentials
- Apache License 2.0
- Open ecosystem that aggregates secrets from Vault, 1Password, AWS Secrets Manager, and more

**Key Differences**

- Managed SaaS eliminates the operational burden of running a secrets infrastructure
- Environments store secrets and plaintext configuration together, not just secrets
- Composable, versionable environments replace flat key-value paths
- OIDC-based dynamic cloud credentials avoid storing long-lived root keys
- Open source under Apache 2.0 versus the Business Source License
- Multi-source secret aggregation versus a single-vendor store

## What is Pulumi ESC?

Pulumi ESC (Environments, Secrets, and Configuration) is a fully managed service for organizing and distributing secrets and configuration across your applications and infrastructure. Unlike traditional key-value secrets stores, ESC introduces the concept of composable environments: hierarchical collections of secrets and configuration that can import from each other, be versioned and tagged, and be consumed through a CLI, SDKs, or a web-based editor with autocomplete and inline documentation.

ESC also functions as an OIDC provider, generating short-lived dynamic credentials for AWS, Azure, and Google Cloud without storing any long-lived cloud credentials. Its open ecosystem lets teams pull secrets from multiple sources, including HashiCorp Vault, 1Password, AWS Secrets Manager, Azure Key Vault, and GCP Secret Manager, and manage them all from a single control plane. For more information, see the [Pulumi ESC documentation](/docs/esc/).

## What is HashiCorp Vault?

HashiCorp Vault is a secrets management platform that provides a centralized store for managing and controlling access to secrets, tokens, encryption keys, and certificates. Vault supports dynamic secret generation for databases and cloud providers, encryption as a service, and comprehensive access policies defined through HCL-based policy documents.

Vault can be self-hosted or consumed through HashiCorp Cloud Platform (HCP) Vault. Self-hosted Vault requires teams to manage high-availability clustering, storage backends (such as Raft or Consul), TLS certificate rotation, unsealing procedures, and version upgrades. HCP Vault reduces some of this operational overhead as a managed offering. For more information, see our [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/) overview.

## Feature by Feature Comparison

Here is a summary of the key differences between Pulumi ESC and HashiCorp Vault:

| Feature | Pulumi ESC | HashiCorp Vault |
| ------- | ---------- | --------------- |
| [Licensing](#licensing) | Apache License 2.0 | Business Source License 1.1 |
| [Architecture & operations](#operations) | Fully managed SaaS | Self-hosted or HCP Vault |
| [Open ecosystem](#open-ecosystem) | Aggregates secrets from multiple sources | Single-source store |
| [Environment composition](#composition) | Hierarchical, composable environments | No native concept |
| [Secrets & configuration](#secrets-and-config) | Stores both secrets and plaintext config | Secrets only |
| [Versioning & tagging](#versioning) | Full environment versioning with tags | Per-secret versioning only |
| [Dynamic cloud credentials](#dynamic-credentials) | OIDC-based for AWS, Azure, GCP | Root-key-based, primarily AWS |
| [Built-in functions](#functions) | toJSON, fromJSON, fromBase64, etc. | No |
| [Secret referencing & interpolation](#referencing) | Cross-environment references, string interpolation | No |
| [Branching & personal configs](#branching) | Fork environments for testing | No |
| [CLI](#cli) | `esc run` injects secrets as env vars | Secret CRUD only |
| [Editor & GUI](#editor) | Autocomplete, error checking, docs hover | JSON editor |
| [SDKs](#sdks) | TypeScript, Python, Go | Multiple language SDKs |
| [Declarative provider (IaC)](#declarative-provider) | Yes, via Pulumi Service Provider | No |
| [Access controls](#access-controls) | RBAC via Pulumi Cloud | Policy-based access |
| [Audit logging](#audit-logging) | Yes | Yes |
| [Encryption](#encryption) | TLS in transit, per-environment keys at rest | AES-256-GCM barrier encryption |
| [OIDC provider](#oidc-provider) | SDK, CLI, UI, and IaC | CLI-only configuration |

## Pulumi ESC and Vault: Better together

While ESC and Vault differ in important ways, they also work well together. ESC environments can reference secrets stored in Vault, which means teams with existing Vault deployments can adopt ESC without migrating secrets out of Vault. Through ESC, secrets in Vault can be organized into composable, versioned collections alongside non-secret configuration, giving teams a unified view of everything an application needs to run.

Here is an example ESC environment that authenticates to Vault via OIDC and pulls secrets:

```yaml
values:
  vault:
    login:
      fn::open::vault-login:
        address: https://vault.example.com:8200/
        jwt:
          role: my-app-role
    secrets:
      fn::open::vault-secrets:
        login: ${vault.login}
        read:
          api-key:
            path: secret/data/my-app/api-key
          db-password:
            path: secret/data/my-app/db-password
  app:
    config:
      region: us-west-2
      log-level: info
      api-key: ${vault.secrets.api-key}
      db-password: ${vault.secrets.db-password}
```

{{% notes type="info" %}}
To learn more about using ESC with Vault, see the [vault-login](/docs/esc/integrations/dynamic-login-credentials/vault-login/) provider, the [vault-secrets](/docs/esc/integrations/dynamic-secrets/vault-secrets/) provider, and the guide on [configuring OIDC for Vault](/docs/esc/guides/configuring-oidc/vault/).
{{% /notes %}}

## Get started with Pulumi ESC

{{< get-started-esc >}}

---

The following sections go into further detail on the differences between Pulumi ESC and HashiCorp Vault.

### Licensing {#licensing}

Pulumi ESC is open source under the [Apache License 2.0](https://github.com/pulumi/esc/blob/main/LICENSE), a permissive and business-friendly license with no usage restrictions. HashiCorp Vault switched from the Mozilla Public License 2.0 to the [Business Source License 1.1](https://github.com/hashicorp/vault/blob/main/LICENSE) in August 2023, which restricts production use that competes with HashiCorp's commercial offerings. For teams that value open source freedom, ESC provides the assurance that its core engine can be used, modified, and distributed without commercial licensing concerns.

### Architecture and operational simplicity {#operations}

Pulumi ESC is a fully managed SaaS service provided by Pulumi Cloud. There are no servers to provision, no storage backends to configure, no high-availability clusters to manage, and no unsealing ceremonies to perform. Teams can start storing secrets and configuration immediately after creating a Pulumi Cloud account.

HashiCorp Vault, by contrast, requires significant operational investment when self-hosted. Teams must configure a storage backend (Raft, Consul, or a cloud-managed option), set up TLS certificates, configure auto-unseal (or manage manual unsealing), plan for high availability, and schedule regular version upgrades. While HCP Vault reduces some of this overhead, it is a separate paid product and still requires networking configuration to connect to your infrastructure.

For platform and DevOps teams that want to focus on using secrets rather than operating secrets infrastructure, ESC eliminates the operational complexity entirely.

### Open ecosystem and secret aggregation {#open-ecosystem}

Pulumi ESC supports an open ecosystem model where a single environment can pull secrets from multiple external sources, including HashiCorp Vault, 1Password, AWS Secrets Manager, Azure Key Vault, and GCP Secret Manager. This means teams are not locked into a single vendor for secret storage. ESC acts as a universal access layer that aggregates and composes secrets from wherever they live.

Vault is a single-source store: it manages only secrets that are stored within Vault itself. While Vault has a robust secrets engine, teams that use multiple secret stores must build their own aggregation logic. ESC solves this natively through its provider model.

### Environment composition and inheritance {#composition}

ESC's central differentiator is composable environments. An environment is a collection of secrets and configuration that can import from other environments, creating a hierarchy with automatic inheritance. For example, a `base` environment can hold shared configuration, while `staging` and `production` environments import from `base` and override only the values that differ. Changes to `base` propagate automatically to all downstream environments.

Vault has no equivalent to environment composition. Secrets are organized by paths within a mount point, and users must manually replicate shared configuration across paths or build custom tooling to manage inheritance. ESC's composition model reduces duplication and makes it easy to understand how environments relate to each other.

### Secrets and configuration together {#secrets-and-config}

ESC stores both secret values and plaintext configuration in the same environment. Non-sensitive settings like feature flags, endpoint URLs, region names, and log levels sit alongside encrypted secrets. This gives developers a single place to find everything an application needs to run, rather than splitting configuration across multiple systems.

Vault treats every value as a secret. While this provides strong encryption guarantees, it also means that non-sensitive configuration either lives in Vault (adding unnecessary encryption overhead) or in a separate system entirely. ESC's approach reduces tool sprawl by combining secrets and configuration into one manageable unit.

### Versioning and tagging {#versioning}

ESC versions entire environments as atomic units, similar to how Docker images are tagged. Teams can pin deployments to a specific version tag, roll back to a previous version atomically, and use tagged versions in import chains to control propagation of changes. This makes it straightforward to answer the question "what configuration was this service running at 3 AM?"

Vault provides per-secret versioning through the KV v2 secrets engine, which tracks individual key versions. However, there is no concept of versioning a related group of secrets together. Coordinating rollbacks across multiple secrets in Vault requires external tooling or manual processes.

### Dynamic cloud credentials via OIDC {#dynamic-credentials}

Pulumi ESC uses OIDC token exchange to generate short-lived credentials for AWS, Azure, and Google Cloud. When an environment is opened, ESC presents a signed JWT to the cloud provider's OIDC endpoint, which issues temporary credentials. No long-lived cloud credentials are stored anywhere. This approach aligns with zero-trust principles and significantly reduces the blast radius of a credential leak. For setup instructions, see [Configuring OIDC for Vault](/docs/esc/guides/configuring-oidc/vault/).

Vault's dynamic secrets engine can generate credentials for databases and some cloud providers, but it typically requires storing root or admin credentials within Vault itself to generate those short-lived credentials. Vault's OIDC-based cloud credential generation is more limited in scope, primarily supporting AWS through the AWS secrets engine with IAM user or STS-based flows that still depend on stored access keys.

### Built-in functions {#functions}

ESC provides built-in functions such as `toJSON`, `fromJSON`, `toBase64`, `fromBase64`, and `toString` that allow data transformation directly within environment definitions. Teams can reshape values, encode secrets for specific consumers, or construct complex configuration objects without external scripting.

Vault does not offer in-store data transformation. Any value manipulation must happen in application code or through external tooling after secrets are retrieved.

### Secret referencing and interpolation {#referencing}

ESC environments support cross-environment references and string interpolation. A value in one environment can reference a value from an imported environment using `${...}` syntax, and new values can be constructed by combining existing ones. When a referenced value changes in the source environment, the change automatically propagates to all downstream environments.

Vault does not support cross-path references or interpolation between secrets. If multiple Vault paths need to share or derive values from one another, that logic must be implemented in application code or orchestration scripts.

### Branching and personal configurations {#branching}

ESC environments can be forked for testing or development purposes. A developer can create a personal environment that imports a shared team environment and overrides specific values, such as pointing to a local database while keeping all other configuration identical to staging. This makes it easy to experiment without modifying shared environments.

Vault has no equivalent branching concept. Testing with different secret values requires creating separate paths or using namespaces, and there is no native mechanism to inherit from and selectively override a base set of secrets.

### Developer experience — CLI {#cli}

The ESC CLI provides the `esc run` command, which opens an environment and injects its values as environment variables into any process. For example, `esc run my-org/my-env -- ./start-server` starts a process with all the secrets and configuration from that environment available as environment variables. The CLI also provides `esc open` to retrieve and display environment values and `esc env` commands to manage environments.

The Vault CLI is primarily designed for secret CRUD operations: writing, reading, and deleting secrets. It does not natively inject secrets as environment variables into arbitrary commands. Teams typically build wrapper scripts or use third-party tools to achieve similar functionality.

### Developer experience — editor and GUI {#editor}

Pulumi ESC provides a web-based document editor with YAML autocomplete, inline documentation, and real-time error checking. The editor understands the ESC environment schema, including provider configurations, built-in functions, and import syntax, and provides contextual help as you type. This reduces the feedback loop for authoring and debugging environments.

Vault's web UI includes a JSON editor for viewing and modifying individual secret values. It does not offer autocomplete, schema validation, or contextual documentation for the values being edited.

### SDKs and programmatic access {#sdks}

Both ESC and Vault provide SDKs for programmatic access. ESC offers TypeScript, Python, and Go SDKs, as well as a REST API. Vault provides client libraries in Go, Ruby, C#, Python, and Java, along with a comprehensive HTTP API. Both platforms enable applications to retrieve secrets at runtime without relying on the CLI.

### Declarative provider for infrastructure as code {#declarative-provider}

ESC environments can be managed as infrastructure using the Pulumi Service Provider. Teams can create, update, and delete environments programmatically as part of their infrastructure as code workflows. This means environment definitions can live in version control, go through code review, and be deployed alongside the infrastructure they configure.

Vault has a Terraform provider for managing Vault's own configuration (auth methods, policies, mounts), but it does not offer a declarative way to manage "collections of secrets and configuration" as a single resource in the way ESC does.

### Access controls {#access-controls}

Both ESC and Vault provide role-based access controls. ESC leverages Pulumi Cloud's organization, team, and role model, where permissions are assigned at the environment level. Vault uses policy documents written in HCL that are attached to tokens and authentication methods, providing fine-grained control over which paths and operations are permitted. Both approaches support the principle of least privilege, though ESC's model is simpler to configure for teams already using Pulumi Cloud.

### Audit logging {#audit-logging}

Both ESC and Vault provide audit logging. ESC audit logs are available through Pulumi Cloud and capture user activity, timestamps, source IPs, and the specific environments and values accessed. Vault provides detailed audit device logging that records every authenticated request and response. Both platforms give security teams the visibility they need for compliance and incident investigation.

### Encryption {#encryption}

ESC encrypts secrets in transit using TLS and at rest using unique encryption keys per environment. Customer-managed encryption keys are also supported for organizations with stricter compliance requirements.

Vault uses a security barrier that encrypts all data leaving Vault using AES-256-GCM with 96-bit nonces. All data stored in the backend is encrypted before it is written. Both platforms provide strong encryption guarantees for secrets at rest and in transit.

### OIDC provider {#oidc-provider}

Pulumi Cloud can function as an OIDC identity provider, issuing tokens that can be consumed by external systems. This capability is available from the Pulumi SDK, CLI, web UI, and the Pulumi Service Provider, making it straightforward to integrate OIDC-based authentication into automated workflows.

Vault can also be configured as an OIDC provider, but the setup is currently available only through the CLI. ESC's broader surface area for OIDC provider configuration makes it easier to integrate into diverse deployment pipelines.

## Try Pulumi ESC for free

Pulumi ESC's secrets and configuration management supports the widest range of secret sources, cloud providers, and deployment targets available. [Get started today](/docs/esc/get-started/).
