---
title_tag: "Pulumi ESC vs Infisical"
meta_desc: Learn about the major differences between Pulumi ESC and Infisical.
title: Pulumi ESC vs Infisical
h1: Pulumi ESC vs Infisical
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumiesc:
        identifier: infisical
        parent: esc-vs
        weight: 2
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

Choosing the right [secrets management](/what-is/what-is-secrets-management/) tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We’ve created this document to help you understand how Pulumi ESC compares with Infisical.

## What is Infisical?

Infisical is a secrets management tool that provides a centralized platform for managing and controlling access to secrets. It supports dynamic secret generation, encryption as a service, and comprehensive access policies.

## Pulumi ESC vs. Infisical: Similarities {#similarities}

Like Infisical, Pulumi ESC is a secrets manager for cloud applications and infrastructure. In both ESC and Infisical, secrets can be stored and accessed through a CLI, SDK, or editor interface. Granular access controls can be implemented across all secrets.

## Pulumi ESC vs. Infisical: Key Differences {#differences}

There are a couple of fundamental differences between Infisical and Pulumi ESC. First, ESC and Infisical differ in that Infisical can only add and manage secrets stored in Infiniscal.  ESC supports pulling and centralizing the management of secrets from most secrets managers. Second, Infisical only stores secrets, whereas ESC stores environments, secrets, and configurations. Third, Infiniscal can only store static secrets while ESC can dynamically generate cloud provider credentials for AWS, Azure, and Google Cloud. Fourth, Infiniscal has limited composablity in its environments while ESC has full hierarchical inheritance between its environments.

Here is a summary of the key differences between Pulumi ESC and Infiniscal:

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
        <td>Yes, non-standard license</td>
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
        <td>No, can only store and manage secrets stored in Infisical</td>
    </tr>
    <tr>
        <th colspan=3>Developer Experience</th>
    </tr>
    <tr>
        <td>Flexible editor</td>
        <td>YAML editor with auto completion, hover documentation, and as-you-type error checking</td>
        <td>GUI editor without YAML support</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>ESC provides a CLI that supports injecting application secrets as environment variables and modifying secrets. All commands in the <code>esc</code> CLI are also available in the <code>pulumi</code> CLI.</td>
        <td>Yes</td>
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
        <td>Secret referencing</td>
        <td>Yes, environments can import secrets from another environment. Secrets updated from the referenced environment will automatically propagate to downstream environments</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Interpolate values from other values</td>
        <td>Yes, users can construct new dynamic values through string interpolation</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>Yes, ESC enables environments that are composed of multiple environments</td>
        <td>Limited, can reference singular secrets from other environments, but can not hierarchically inherit entire environments.</td>
    </tr>
    <tr>
        <td>Branching / Personal configs</td>
        <td>Yes, users can fork environments for testing without rewriting entire environments</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, ESC enables entire environments (sets of secrets and configuration) to be versioned. Stacks can be pinned to specific environment versions for quick rollbacks</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Compare secrets across environment</td>
        <td>No</td>
        <td>Yes</td>
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
        <td>Yes, ESC uses an unique encryption key per environment. All secrets are stored encrypted at rest.</td>
        <td>Yes, Infisical uses TLS for encryption in transit as well as AES256-GCM for symmetric encryption and x25519-xsalsa20-poly1305 for asymmetric encryption operations.</td>
    </tr>
    <tr>
        <td>Access controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Dynamically generate cloud provider credentials</td>
        <td>Yes, no root account keys are used to configure dynamic credentials. Available for AWS, Azure, and Google Cloud.</td>
        <td>No</td>
    </tr>
    <tr>
        <td>OIDC provider</td>
        <td>Yes, Pulumi Cloud can be used as an OIDC provider from the Pulumi SDK, CLI, UI, and <code>pulumi-service</code> provider.</td>
        <td>No</td>
    </tr>
</table>

{{< get-started-esc >}}
