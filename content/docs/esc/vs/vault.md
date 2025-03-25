---
title_tag: "Pulumi ESC vs HashiCorp Vault"
meta_desc: Learn about the major differences between Pulumi ESC and HashiCorp Vault.
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
search:
  keywords:
    - vault
    - esc
    - td
    - hashicorp
    - vs
    - tr
    - differences
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
        <th>Pulumi ESC</th>
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
        <td>Key-value Store</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Open Ecosystem</td>
        <td>Yes, supports pulling and using secrets from multiple sources including HashiCorp Vault, 1Password, AWS Secrets Manager, etc.</td>
        <td>No, can only store and manage secrets store in Vault</td>
    </tr>
    <tr>
        <th colspan=3>Developer Experience</th>
    </tr>
    <tr>
        <td>Editing and Authoring</td>
        <td>Yes, supports both GUI and powerful Document Editor with autocomplete, docs hover, and error checking</td>
        <td>Limited, has a JSON editor</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>Yes, available as <code>esc</code> CLI or <code>pulumi</code> CLI. Supports injecting application secrets as environment variables and modifying secrets.</td>
        <td>Limited, has a CLI but lacks the capabilities of injecting secrets as environment variables. The CLI is for modifying secrets only. </td>
    </tr>
    <tr>
        <td>Client SDKs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    </tr>
      <tr>
        <td>Declarative Provider</td>
        <td>Yes, support via the Pulumi Service Provider, which allows management (create, update, delete) of collections of secrets and configuration as a resource through infrastructure as code.</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>Yes, simple set up of hierarchical environments that inherit values from imported environments</td>
        <td>No, users have to create the structure themselves</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, entire environments can be versioned and tagged and imported based on the specific version tags or revision numbers</td>
        <td>Limited, secrets are individually versioned</td>
    </tr>
    <tr>
        <td>Values Can Be of Type Secret and Plaintext</td>
        <td>Yes</td>
        <td>No, values can only be secrets</td>
    </tr>
    <tr>
        <td>Ability to See Existing Secrets</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Secret Referencing</td>
        <td>Yes, environments can import secrets from another environment. Secrets updated from the referenced environment will automatically propagate to downstream environments</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Interpolate Values from Other Values</td>
        <td>Yes, new dynamic values can be constructed through string interpolation</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Branching / Personal Configs</td>
        <td>Yes, environments can be forked for testing without rewriting entire environments and overriding specific values</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Compare Secrets across Environment</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>In-built Functions</td>
        <td>Yes, support for functions like <code>toJSON, fromJSON, fromBase64, toString</code> allows data manipulation for any scenario</td>
        <td>No</td>
    </tr>
    <tr>
        <th colspan=3>Security and Compliance</th>
    </tr>
    <tr>
        <td>Audit Logs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Encrypted Secrets Storage</td>
        <td>Yes, TLS is used for encryption in transit and unique encryption keys per environment are employed for encryption at rest.</td>
        <td>Yes, Vault uses a security barrier for all requests made to the backend. The security barrier automatically encrypts all data leaving Vault using a 256-bit Advanced Encryption Standard (AES) cipher in the Galois Counter Mode (GCM) with 96-bit nonces.</td>
    </tr>
    <tr>
        <td>Access Controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Secure Dynamic Cloud Provider Credentials</td>
        <td>Yes, uses OIDC flows to generate dynamic credentials. Available for AWS, Azure, and Google Cloud.</td>
        <td>Limited, requires the usage of root account keys. Only available for AWS.</td>
    </tr>
    <tr>
        <td>OIDC Provider</td>
        <td>Yes, Pulumi Cloud can be used as an OIDC provider from the Pulumi SDK, CLI, UI, and <code>pulumi-service</code> provider.</td>
        <td>Limited, configuring Vault as an OIDC provider is only available from the CLI</td>
    </tr>
</table>

{{< get-started-esc >}}
