---
title_tag: "Pulumi ESC vs HashiCorp Vault"
meta_desc: Learn about the major differences between Pulumi ESC and HashiCorp Vault.
title: Pulumi ESC vs HashiCorp Vault
h1: Pulumi ESC vs HashiCorp Vault
menu:
    esc:
        name: HashiCorp Vault
        identifier: vault
        parent: esc-vs
        weight: 1
aliases:
---

Choosing the right [secrets management](/what-is/what-is-secrets-management/) tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We’ve created this document to help you understand how Pulumi ESC compares with HashiCorp Vault, and how ESC and Vault can be used together.

## What is HashiCorp Vault?

HashiCorp Vault is a secrets management tool that provides a centralized platform for managing and controlling access to secrets. It supports dynamic secret generation, encryption as a service, and comprehensive access policies.

## Pulumi ESC vs. Vault: Similarities {#similarities}

Like Vault, Pulumi ESC is a secrets manager for cloud applications and infrastructure. In both ESC and Vault, secrets can be stored and accessed through a CLI, SDK, or editor interface. Granular access controls can be implemented across all secrets.

## Pulumi ESC vs. Vault: Key differences {#differences}

Vault and Pulumi ESC differ in three fundamental ways. First, Vault is not open source: it uses the Business Source License model, whereas ESC is fully open source and Apache 2.0 licensed. Second, Vault stores secrets only, whereas ESC stores environments, secrets, and configurations. Third, ESC provides composability of collections of secrets and configuration: environments can be composed together from multiple other environments, so shared configuration is inherited rather than duplicated.

## Pulumi ESC and Vault: Better together

Pulumi ESC and Vault can be used together to store and manage infrastructure and application secrets. ESC environments can reference secrets stored in Vault, and through ESC those secrets can be organized as collections that are versioned, branched, and composed inside other collections. ESC also stores non-secret configuration alongside the secrets you keep in Vault.

Here is a summary of the key differences between Pulumi ESC and HashiCorp Vault:

<div class="table-wrapper">
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
        <td>Open source license</td>
        <td>Yes, Apache License 2.0</td>
        <td>No, Business Source License 1.1</td>
    </tr>
    <tr>
        <td>Hosting/management</td>
        <td>Fully managed SaaS service provided by Pulumi Cloud</td>
        <td>Offers hosted cloud service and self-hosting, which requires significant management overhead</td>
    </tr>
    <tr>
        <td>Key-value store</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Open ecosystem</td>
        <td>Yes, supports pulling and using secrets from multiple sources including HashiCorp Vault, 1Password, AWS Secrets Manager, etc.</td>
        <td>No, can only store and manage secrets stored in Vault</td>
    </tr>
    <tr>
        <th colspan=3>Developer experience</th>
    </tr>
    <tr>
        <td>Editing and authoring</td>
        <td>Yes, supports both GUI and powerful Document Editor with autocomplete, docs hover, and error checking</td>
        <td>Limited, offers a key/value form editor with a JSON toggle</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>Yes, available as <code>pulumi env</code> in the Pulumi CLI. Supports injecting application secrets as environment variables and modifying secrets.</td>
        <td>Limited, the <code>vault</code> CLI reads and writes secrets but does not inject them as environment variables. Vault Agent's process supervisor mode covers that separately.</td>
    </tr>
    <tr>
        <td>Client SDKs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Declarative provider</td>
        <td>Yes, support via the Pulumi Service Provider, which allows management (create, update, delete) of collections of secrets and configuration as a resource through infrastructure as code.</td>
        <td>Yes, individual secrets can be managed as resources with the Vault provider for Pulumi or Terraform</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>Yes, hierarchical environments inherit values from the environments they import</td>
        <td>No equivalent concept; secrets are organized by path convention and the structure is maintained by hand</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, entire environments can be versioned and tagged and imported based on the specific version tags or revision numbers</td>
        <td>Limited, secrets are individually versioned</td>
    </tr>
    <tr>
        <td>Values can be secret or plaintext</td>
        <td>Yes</td>
        <td>No, values can only be secrets</td>
    </tr>
    <tr>
        <td>Ability to see existing secrets</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Secret referencing</td>
        <td>Yes, environments can import secrets from another environment. Secrets updated from the referenced environment will automatically propagate to downstream environments</td>
        <td>No equivalent concept; Vault has no first-class environment to reference, so secrets are read by path</td>
    </tr>
    <tr>
        <td>Interpolate values from other values</td>
        <td>Yes, new dynamic values can be constructed through string interpolation</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Branching and personal configs</td>
        <td>Yes, environments can be forked for testing without rewriting entire environments and overriding specific values</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Compare secrets across environments</td>
        <td>Yes, <code>pulumi env diff</code> shows the changes between two environments or two versions of a single environment</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Built-in functions</td>
        <td>Yes, support for functions like <code>toJSON</code>, <code>fromJSON</code>, <code>fromBase64</code>, and <code>toString</code> allows data manipulation for any scenario</td>
        <td>Limited, provides templating and transformation functions, such as username templating and the Transform secrets engine, rather than functions for composing configuration values</td>
    </tr>
    <tr>
        <th colspan=3>Security and compliance</th>
    </tr>
    <tr>
        <td>Audit logs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Encrypted secrets storage</td>
        <td>Yes, TLS is used for encryption in transit and unique encryption keys per environment are employed for encryption at rest.</td>
        <td>Yes, Vault uses a security barrier for all requests made to the backend. The security barrier automatically encrypts all data leaving Vault using a 256-bit Advanced Encryption Standard (AES) cipher in the Galois Counter Mode (GCM) with 96-bit nonces.</td>
    </tr>
    <tr>
        <td>Access controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Secure dynamic cloud provider credentials</td>
        <td>Yes, uses OIDC flows to generate dynamic credentials. Available for AWS, Azure, and Google Cloud.</td>
        <td>Yes, cloud secrets engines generate short-lived credentials for AWS, Azure, and Google Cloud. Each engine is configured with a static credential that Vault uses to mint them.</td>
    </tr>
    <tr>
        <td>OIDC provider</td>
        <td>Yes, Pulumi Cloud can be used as an OIDC provider from the Pulumi SDK, CLI, UI, and <code>pulumi-service</code> provider.</td>
        <td>Limited, configuring Vault as an OIDC provider is only available from the CLI</td>
    </tr>
</table>
</div>

{{< get-started-esc >}}
