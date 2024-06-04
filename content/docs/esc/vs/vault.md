---
title_tag: "Pulumi ESC vs HashiCorp Vault"
meta_desc: Learn about the major differences between Pulumi ESC and HashiCorp Vault.
title: Pulumi ESC vs HashiCorp Vault
h1: Pulumi ESC vs HashiCorp Vault
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumiesc:
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

Choosing the right [secrets management](/what-is/what-is-secrets-management/) tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We’ve created this document to help you understand how Pulumi ESC compares with HashiCorp Vault, and how ESC and Vault can be used together.

## What is HashiCorp Vault?

HashiCorp Vault is a secrets management tool that provides a centralized platform for managing and controlling access to secrets. It supports dynamic secret generation, encryption as a service, and comprehensive access policies.

## Pulumi ESC vs. Vault: Similarities {#similarities}

Like Vault, Pulumi ESC is a secrets manager for cloud applications and infrastructure. In both ESC and Vault, secrets can be stored and accessed through a CLI, SDK, or editor interface. Granular access controls can be implemented across all secrets.

## Pulumi ESC vs. Vault: Key Differences {#differences}

There are a couple of fundamental differences between Vault and Pulumi ESC. First, ESC and Vault differ in that Vault is not open source, using the Business Source License model. In contrast, ESC is fully open source and Apache 2.0 licensed. Second, Vault only stores secrets, whereas ESC stores environments, secrets, and configurations. Third, ESC provides composability of collections of secrets and configuration. Environments can be composed together from multiple other environments, enabling easy inheritance of shared configuration.

## Pulumi ESC and Vault:  Better Together

While there are differences and similarities between Pulumi ESC and Vault, they can actually be used together for a more powerful experience to store and manage infrastructure and application secrets. ESC environments can reference secrets stored in Vault. Through ESC, secrets in Vault can be organized as collections of secrets that can be versioned, branched, and composed inside other collections. With ESC, non-secret configuration can be stored alongside secrets in Vault. ESC enhances Vault, and they work better together.

Here is a summary of the key differences between Pulumi ESC and HashiCorp Vault:

<table>
    <tr>
        <th>Feature</th>
        <th>Pulumi</th>
        <th>Vault</th>
    </tr>
    <tr>
        <th colspan=3>Architecture</th>
    </tr>
    <tr>
        <td>OSS License</td>
        <td>Yes, Apache License 2.0</td>
        <td>No, Business Source License 1.1</td>
    </tr>
    <tr>
        <td>Hosting/management</td>
        <td>Fully-managed SaaS service provided by Pulumi Cloud</td>
        <td>Offers hosted cloud service and self-hosting, which requires significant management overhead</td>
    </tr>
    <tr>
        <td>Key-value store</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Open Ecosystem</td>
        <td>Yes, ESC supports pulling and centralizing the management of secrets from 1Password, AWS OIDC, AWS Secrets Manager, Azure OIDC, Azure Key Vault, Google Cloud OIDC, Google Cloud Secrets Manager, Pulumi stacks, Vault OIDC, and Vault.</td>
        <td>No, can only store and manage secrets store in Vault</td>
    </tr>
    <tr>
        <th colspan=3>Developer Experience</th>
    </tr>
    <tr>
        <td>Flexible editor</td>
        <td>YAML editor with auto completion, hover documentation, and as-you-type error checking</td>
        <td>JSON editor</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>ESC provides a CLI that supports injecting application secrets as environment variables and modifying secrets. All commands in the <code>esc</code> CLI are also available in the <code>pulumi</code> CLI.</td>
        <td>Limited, Vault has a CLI but lacks the capabilities of injecting secrets as environment variables. The CLI is for modifying secrets. </td>
    </tr>
    <tr>
        <td>Client SDKs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Values can be non-secret</td>
        <td>Yes, can store configuration and environments</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Ability to see existing secrets</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Secret referencing</td>
        <td>Yes, environments can import secrets from another environment. Secrets updated from the referenced environment will automatically propagate to downstream environments</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Interpolate values from other values</td>
        <td>Yes, users can construct new dynamic values through string interpolation</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>Yes, ESC enables environments that are composed of multiple environments</td>
        <td>No, Vault users have to create the structure themselves</td>
    </tr>
    <tr>
        <td>Branching / Personal configs</td>
        <td>Yes, users can fork environments for testing without rewriting entire environments</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, ESC enables entire environments (sets of secrets and configuration) to be versioned. Stacks can be pinned to specific environment versions for quick rollbacks</td>
        <td>Limited, secrets are individually versioned</td>
    </tr>
    <tr>
        <td>Compare secrets across environment</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <th colspan=3>Security and Compliance</th>
    </tr>
    <tr>
        <td>Audit logs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Encrypted Secrets Storage</td>
        <td>Yes, ESC uses an unique encryption key per environment. All secrets are stored encrypted at rest. </td>
        <td>Yes, Vault uses a security barrier for all requests made to the backend. The security barrier automatically encrypts all data leaving Vault using a 256-bit Advanced Encryption Standard (AES) cipher in the Galois Counter Mode (GCM) with 96-bit nonces.</td>
    </tr>
    <tr>
        <td>Access controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Dynamically generate cloud provider credentials</td>
        <td>Yes, no root account keys are used to configure dynamic credentials. Available for AWS, Azure, and Google Cloud.</td>
        <td>Limited, requires the usage of root account keys. Only available for AWS.</td>
    </tr>
    <tr>
        <td>OIDC provider</td>
        <td>Yes, Pulumi Cloud can be used as an OIDC provider from the Pulumi SDK, CLI, UI, and <code>pulumi-service</code> provider.</td>
        <td>Limited, configuring Vault as an OIDC provider is only available from the CLI</td>
    </tr>
</table>

{{< get-started-esc >}}
