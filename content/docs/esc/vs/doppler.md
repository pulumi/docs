---
title_tag: "Pulumi ESC vs Doppler"
meta_desc: Learn about the major differences between Pulumi ESC and Doppler.
title: Pulumi ESC vs Doppler
h1: Pulumi ESC vs Doppler
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    Name: Doppler
    identifier: Doppler
    parent: esc-vs
    weight: 3
aliases:
search:
  keywords:
    - doppler
    - esc
    - differences
    - td
    - vs
    - tr
    - major
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

Choosing the right [secrets management](/what-is/what-is-secrets-management/) tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We’ve created this document to help you understand how Pulumi ESC compares with Doppler.

## What is Doppler?

Doppler is a secrets management tool that provides a centralized platform for managing and controlling access to secrets. It supports dynamic secret generation, encryption as a service, and comprehensive access policies.

## Pulumi ESC vs. Doppler: Similarities {#similarities}

Like Doppler, Pulumi ESC is a secrets manager for cloud applications and infrastructure. In both ESC and Doppler, secrets can be stored and accessed through a CLI, SDK, or Web editor interface. Secrets can also be pulled from other secrets and password managers. Granular access controls can be implemented across all secrets.

## Pulumi ESC vs. Doppler: Key Differences {#differences}

There are a couple of fundamental differences between Doppler and Pulumi ESC. Doppler has basic per secret inheritance as opposed to fully composable and hierarchical environments of ESC. Second, ESC environments can be managed (create, update, delete) through infrastructure as code. Third, ESC takes a more secure limited privilege path to provisioning dynamic short-term credentials as compared to Doppler.

Here's a detailed comparison of the two:

<table>
    <tr>
        <th>Feature</th>
        <th>Pulumi ESC</th>
        <th>Doppler</th>
    </tr>
    <tr>
        <th colspan=3>Architecture</th>
    </tr>
    <tr>
        <td>OSS License</td>
        <td>Yes, Apache License 2.0</td>
        <td>No</td>
    </tr>
     <tr>
        <td>Document Store</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Key-value Store</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Open Ecosystem</td>
        <td>Yes, supports pulling and using secrets from multiple sources including HashiCorp Vault, 1Password, AWS Secrets Manager, etc.</td>
        <td>Yes, supports pulling and using secrets from a variety of stores</td>
    </tr>
    <tr>
        <th colspan=3>Developer Experience</th>
    </tr>
    <tr>
        <td>Editing and Authoring</td>
        <td>Yes, supports both GUI and IDE editing, with a powerful Document Editor with autocomplete, docs hover, and error checking</td>
        <td>Limited, has GUI editor with multiple import formats</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>Yes, available via <code>esc</code> CLI and <code>pulumi</code> CLI</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Client SDKs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
      <tr>
        <td>Declarative Provider</td>
        <td>Yes, support via the Pulumi Service Provider, which allows management (create, update, delete) of collections of secrets and configuration as a resource through infrastructure as code</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>Yes, simple set up of hierarchical environments that inherit values from imported environments</td>
        <td>Limited, can create projects that have secret values that can be individually inherited by other projects</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, entire environments can be versioned and tagged and imported based on the specific version tags or revision numbers</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Immutable History & Point in Time Recovery</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Values Can Be of Type Secret and Plaintext</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Interpolate Values from Other Values</td>
        <td>Yes, new dynamic values can be constructed through string interpolation</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Branching / Personal Configs</td>
        <td>Yes, environments can be forked for testing without rewriting entire environments and overriding specific values</td>
        <td>Yes, environments has a root and branches and each developer automatically get their own personal development config per project</td>
    </tr>
    <tr>
        <td>Compare Secrets across Environments</td>
        <td>No</td>
        <td>No</td>
    </tr>
    <tr>
        <td>In-built Functions</td>
        <td>Yes, support for functions like <code>toJSON, fromJSON, fromBase64, toString</code> allows data manipulation for any scenario</td>
        <td>Limited, only <code>toJSON</code> and <code>fromJSON</code> available</td>
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
        <td>Yes, TLS is used for encryption in transit and unique encryption keys per environment are employed for encryption at rest</td>
        <td>Yes, TLS is used for encryption in transit and all secrets are encrypted with AES-GCM</td>
    </tr>
    <tr>
        <td>Access Controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Secure Dynamic Cloud Provider Credentials</td>
        <td>Yes, uses OIDC flows to generate dynamic credentials. Available for AWS, Azure, and Google Cloud</td>
        <td>Limited, OIDC not used to generate dynamic credentials. TTL based leases are used to generate dynamic secrets</td>
    </tr>
    <tr>
        <td>OIDC Trust</td>
        <td>Yes, trust relationships are established with third-party OIDC providers</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Secure Environment Variables</td>
        <td>Yes, the <code>esc run</code> CLI command can be used to specify which secrets are available as environment variables</td>
        <td>No, all values are available as environment variables</td>
    </tr>
        <td>Plaintext Read Only Mode</td>
        <td>Yes, ESC offers a <code>read</code> mode that allows reading only plaintext values while not being able to decrypt secrets or access dynamic credentials</td>
        <td>No</td>
    </tr>
</table>

{{< get-started-esc >}}
