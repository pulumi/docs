---
title_tag: "Pulumi ESC vs Infisical"
meta_desc: Learn about the major differences between Pulumi ESC and Infisical.
title: Pulumi ESC vs Infisical
h1: Pulumi ESC vs Infisical
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    Name: Infisical
    identifier: infisical
    parent: esc-vs
    weight: 2
aliases:
search:
  keywords:
    - infisical
    - esc
    - major
    - vs
    - td
    - differences
    - tr
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

Like Infisical, Pulumi ESC is a secrets manager for cloud applications and infrastructure. In both ESC and Infisical, secrets can be stored and accessed through a CLI, SDK, or Web editor interface. Granular access controls can be implemented across all secrets.

## Pulumi ESC vs. Infisical: Key Differences {#differences}

There are a couple of fundamental differences between Infisical and Pulumi ESC. First, ESC and Infisical differ in that Infisical can only add and manage secrets stored in Infisical. ESC adopts an open ecosystem approach, allowing you to pull secrets stored in most secrets and password managers during runtime and use them anywhere. This allows teams to use the best secrets management solution according their purposes and needs. Second, Infisical lacks the composability and hierarchical nature of ESC, which increases getting started speed and duplication of secrets. Third, ESC takes a software engineering approach to versioning with ability to add tags and import specific collections of secrets and configuration via those tags, similar to Docker. Fourth, ESC takes a more secure limited privilege path to provisioning dynamic short-term credentials as compared to Infisical.

Here's a detailed comparison of the two:

<table>
    <tr>
        <th>Feature</th>
        <th>Pulumi ESC</th>
        <th>Infisical</th>
    </tr>
    <tr>
        <th colspan=3>Architecture</th>
    </tr>
    <tr>
        <td>OSS License</td>
        <td>Yes, Apache License 2.0</td>
        <td>Yes, MIT expat license</td>
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
        <td>No, can only store and manage secrets stored in Infisical</td>
    </tr>
    <tr>
        <th colspan=3>Developer Experience</th>
    </tr>
    <tr>
        <td>Editing and Authoring</td>
        <td>Yes, supports both GUI and powerful Document Editor with autocomplete, docs hover, and error checking</td>
        <td>Limited, has GUI editor without YAML support</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>Yes, available as <code>esc</code> CLI or <code>pulumi</code> CLI</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Client SDKs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
      <tr>
        <td>Declarative Provider</td>
        <td>Yes, support via the Pulumi Service Provider, which allows management (create, update, delete) of collections of secrets and configuration as a resource through infrastructure as code.</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>Yes, simple set up of hierarchical environments that inherit values from imported environments</td>
        <td>No, can only reference singular secrets from other environments and references have to be duplicated in multiple environments</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, entire environments can be versioned and tagged and imported based on the specific version tags or revision numbers</td>
        <td>Limited</td>
    </tr>
    <tr>
        <td>Immutable History & Point in Time Recovery</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Values Can Be of Type Secret and Plaintext</td>
        <td>Yes</td>
        <td>No, values can only be secrets</td>
    </tr>
    <tr>
        <td>Interpolate Values from Other Values</td>
        <td>Yes, new dynamic values can be constructed through string interpolation</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Branching / Personal Configs</td>
        <td>Yes, environments can be forked for testing without rewriting entire environments and overriding specific values</td>
        <td>Limited, requires careful copying since secrets need to be downloaded in plaintext locally and then uploaded</td>
    </tr>
    <tr>
        <td>Compare Secrets across Environments</td>
        <td>No</td>
        <td>Yes</td>
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
        <td>Yes, TLS is used for encryption in transit and unique encryption keys per environment are employed for encryption at rest</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Access Controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Secure Dynamic Cloud Provider Credentials</td>
        <td>Yes, uses OIDC flows to generate dynamic credentials. Available for AWS, Azure, and Google Cloud.</td>
        <td>No, less secure as it requires access keys for highly privileged root accounts</td>
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
        <td>Yes, ESC offers a <code>read</code> mode that allows reading only plaintext values while not being able to decrypt secrets or  access dynamic credentials</td>
        <td>No</td>
    </tr>
</table>

{{< get-started-esc >}}
