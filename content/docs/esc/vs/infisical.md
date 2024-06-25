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

Like Infisical, Pulumi ESC is a secrets manager for cloud applications and infrastructure. In both ESC and Infisical, secrets can be stored and accessed through a CLI, SDK, or Web editor interface. Granular access controls can be implemented across all secrets.

## Pulumi ESC vs. Infisical: Key Differences {#differences}

There are a couple of fundamental differences between Infisical and Pulumi ESC. First, ESC and Infisical differ in that Infisical can only add and manage secrets stored in Infisical. ESC adopts a truly open ecosystem approach, allowing you to pull secrets stored in most secret and password managers during runtime and use them anywhere. This reduces the time to take full inventory of your secrets across your organization , enabling you to utilize the best solution for the purpose.  Second, Infisical lacks the composability and hierarchical nature of ESC, which increases getting started speed and duplication of secrets. Third, ESC takes a software engineering approach to versioning with ability to add tags and import specific collections of secrets and configuration via those tags, similar to Docker. Fourth, ESC takes a more secure limited privilege path to provisioning dynamic short-term credentials compared to Infisical.

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
        <td>Document store</td>
        <td>Yes</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Key-value store</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Open Ecosystem</td>
        <td>Yes, ESC supports pulling and using secrets from multiple sources including HashiCorp Vault, 1Password, AWS Secrets Manager, etc.</td>
        <td>No, can only store and manage secrets stored in Infisical</td>
    </tr>
    <tr>
        <th colspan=3>Developer Experience</th>
    </tr>
    <tr>
        <td>Editing and Authoring</td>
        <td>Supports both GUI and powerful Document Editor with autocomplete, docs hover, and error checking</td>
        <td>GUI editor without YAML support</td>
    </tr>
    <tr>
        <td>CLI</td>
        <td>Yes. Available as <code>esc</code> CLI or <code>pulumi</code> CLI</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Client SDKs</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
      <tr>
        <td>Declarative Provider</td>
        <td>ESC is supported via the Pulumi Service Provider that has built-in solutions for retries, and not needing to handle create vs. update scenarios and managing your collection of secrets and configuration as a resource</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Composability</td>
        <td>ESC allows easy set up of hierarchical environments that inherit values from imported environments</td>
        <td>No, can only reference singular secrets from other environments and have to duplicate that reference in multiple environments</td>
    </tr>
    <tr>
        <td>Versioning</td>
        <td>Yes, ESC allows you to version entire environments and tag them. Use and import specific using version tags or revision number</td>
        <td>Limited</td>
    </tr>
    <tr>
        <td>Immutable History & Point in time recovery</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Values can be of type Secret and Plaintext</td>
        <td>Yes</td>
        <td>No. Values can only be secrets</td>
    </tr>
    <tr>
        <td>Interpolate values from other values</td>
        <td>Yes, users can construct new dynamic values through string interpolation</td>
        <td>No</td>
    </tr>
    <tr>
        <td>Branching / Personal configs</td>
        <td>Yes, users can fork environments for testing without rewriting entire environments and override specific values</td>
        <td>Limited. Requires careful copying as secrets need to be downloaded in plaintext locally and then uploaded </td>
    </tr>
    <tr>
        <td>Compare secrets across environments</td>
        <td>No</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>In-Built Functions</td>
        <td>ESC offers functions like toJSON, fromJSON, fromBase64, toString that allow you to manipulate the data for any scenario</td>
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
        <td>Yes, ESC uses TLS for encryption in transit and employs unique encryption key per environment for encryption at rest</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Access controls</td>
        <td>Yes</td>
        <td>Yes</td>
    </tr>
    <tr>
        <td>Secure dynamic cloud provider credentials</td>
        <td>Yes. Uses OIDC flows to generate dynamic credentials. Available for AWS, Azure, and Google Cloud.</td>
        <td>No. Less secure as it requires access keys for highly privileged root accounts</td>
    </tr>
    <tr>
        <td>OIDC Trust</td>
        <td>Yes. Establish trust relationships with third-party OIDC providers</td>
        <td>No</td>
    </tr>
    <tr>
    <td>Secure Environment Variables</td>
    <td>Yes. You can specify which secrets are available as environment variables when using <code>esc run</code> CLI command</td>
    <td>No. All values are available as environment variables</td>
    </tr>
      <td>Read plaintext but not decrypt secrets access mode</td>
    <td>Yes. ESC offers a <code>read</code> mode that allows other members to see only plaintext values but cannot decrypt secrets and access dynamic credentials</td>
    <td>No</td>
    </tr>
</table>

{{< get-started-esc >}}
