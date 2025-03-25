---
title_tag: "How Pulumi ESC Works"
meta_desc: An overview of how Pulumi ESC works and discussion of core concepts.
title: How Pulumi ESC works
h1: How Pulumi ESC works
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    parent: esc-concepts
    identifier: how-pulumi-esc-works
    weight: 1
search:
  keywords:
    - esc
    - works
    - discussion
    - core
    - concepts
    - overview
    - secrets
---

This article details how Pulumi ESC works, including its architecture, supported integrations, and core functionalities. To understand some of the core ESC concepts, like *environments*, *dynamic secrets*, and *configuration-as-code*, please read through the [ESC Concepts](/docs/esc/concepts/) doc.

## Architecture

Pulumi ESC is available as a hosted service provided as part of [Pulumi Cloud](/docs/pulumi-cloud/) or can be [self-hosted](/docs/esc/faq/#can-i-self-host-pulumi-esc) on your own infrastructure. ESC stores your secrets and configuration and proxies access to other secret stores through provider plugins.

Using configuration-as-code, these secrets and configuration values are composed into *environments* which are defined in YAML. ESC then makes these environments available to targets via common mechanisms like environment variables, configuration files, and directly via the ESC API and multi-language SDKs.

{{< figure src="/docs/esc/assets/esc-octopus-diagram.png" caption="Figure: A diagram showing the architecture of Pulumi ESC.">}}

## Secrets and configuration sources

By default, Pulumi ESC stores your configuration and secrets in Pulumi Cloud. However, ESC also integrates with a variety of third-party sources through an extensible *provider* plugin model. This allows teams to use their preferred providers without needing to manually copy or paste secrets across environments. The secrets will be dynamically fetched from the third-party API and integrated into your ESC environments.

By aggregating secrets from these providers, Pulumi ESC provides a unified interface for retrieving, using, and managing secrets, regardless of their source.

### Supported login and secret providers

Pulumi ESC integrates with many popular cloud login providers and secrets managers, including:

* [AWS OIDC](/docs/esc/integrations/dynamic-login-credentials/aws-login/) and [AWS Secrets Manager](/docs/esc/integrations/dynamic-secrets/aws-secrets/)
* [Azure OIDC](/docs/esc/integrations/dynamic-login-credentials/azure-login) and [Azure KeyVault](/docs/esc/integrations/dynamic-secrets/azure-secrets/)
* [GCP OIDC](/docs/esc/integrations/dynamic-login-credentials/gcp-login/) and [GCP Secrets Manager](/docs/esc/integrations/dynamic-secrets/gcp-secrets/)
* [HashiCorp Vault OIDC](/docs/esc/integrations/dynamic-login-credentials/vault-login/) and [Vault Secrets](/docs/esc/integrations/dynamic-secrets/vault-secrets/)
* [1Password](/docs/esc/integrations/dynamic-secrets/1password-secrets/), [Kubernetes](/docs/esc/integrations/kubernetes/), among others.

Teams can setup [OpenID Connect integration](/docs/pulumi-cloud/oidc/) in their cloud providers to allow ESC environments to pull short-lived credentials via **OIDC** for secure, time-limited access to secrets. These credentials can then be used in both [Pulumi IaC](/docs/pulumi-cloud/esc/environments/#using-with-pulumi-iac) workflows and [external CLIs](/docs/pulumi-cloud/esc/environments/#running-third-party-commands-using-pulumi-esc-secrets-and-config) like `aws`, `kubectl`, etc.

## The ESC data model

### Configuration and Secrets as Code

Pulumi ESC uses a configuration-as-code approach. ESC environments are defined in YAML, which contain named configuration values, encrypted secrets, and provider references.

A simple static environment can be thought of as a collection of key/value pairs. They can also contain interpolated values and complex [structured configuration](/docs/esc/environments/working-with-environments/#structured-configuration). Static secrets are also defined in YAML and are encrypted before they are stored to ensure security.

**Example:** *Defining configuration values, structured data, and encrypted secrets in YAML.*

```yaml
values:
  name: world
  salutation: hello
  greeting: ${salutation}, ${name}

  structured_data:
    active: true
    nums:
      - 1
      - 2

  myPassword:
    fn::secret:
      ciphertext: ZXNjeAA....
```

### Dynamic and Projected Values

Dynamic secrets are defined in YAML as provider references. The interpolation mechanism can also be used to *project* these ESC values as environment variables or files.

**Example:** *Defining dynamic secrets and projecting environment variables.*

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::01234567891011:role/some-role
          sessionName: some-session
          duration: 1h

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
    MY_ENV_VAR: "true"
```

### Tags and Versions

Every change to an ESC environment definition is recorded as a unique numeric version. Environments can be tagged at specific versions to allow for multiple versions of the same environment to be in use at the same time (for example, production vs staging, or for A/B testing). This also facilitates easy rollbacks of both secrets and credentials in a single action.

### Composing environments

ESC environments can be composed from other environments allowing for modularity and inheritance -- concepts usually only found in code:

* **Inheritance**: One environment can inherit values from another environment.
* **Overrides**: Values in child environments can override inherited values.
* **Nesting**: Environments can be arbitrarily nested for maximum flexibility, allowing complex hierarchies to be built out.

## Managing access: RBAC and auditing

### RBAC Implementation

Pulumi ESC handles access control with robust security measures, leveraging [RBAC (Role-Based Access Control)](/docs/esc/environments/access-control/) to manage permissions from within [Pulumi Cloud](/docs/pulumi-cloud). ESC environment permissions are set at organizational, team, and individual levels, allowing fine-grained control over who can update, preview, or retrieve environments and secrets. This ensures only authorized team members can interact with sensitive configuration or secrets..

### Auditing and Versioning

Every action, including opening an environment or making changes, is recorded in an **audit log**. This log tracks what changes were made, by whom, and when, providing a full history of interactions with secrets and configurations. Environments are also versioned, allowing teams to roll back changes if needed.

## Integration with the Pulumi ecosystem and beyond

### Pulumi IaC integration

Pulumi ESC integrates tightly with [Pulumi Infrastructure as Code (IaC)](/docs/iac/), allowing environments to be accessed during the deployment process using commands like `pulumi up`. Adding an ESC environment to a Pulumi program requires only a single YAML value indicating which environments your Pulumi stack needs access to.

**Example:** *Accessing an ESC environment from a Pulumi program.*

```yaml
# Pulumi.dev.yaml
environment:
  - myapp-dev
```

Every function of the ESC CLI is also available as a subcommand in the Pulumi IaC CLI.

### Standalone CLI and API

The [Pulumi ESC CLI](/docs/esc/cli/) and [ESC Automation API](/docs/esc/development/automation-api/) allow teams to interact with environments outside of [Pulumi IaC](/docs/iac/). This means secrets and configurations can be accessed from external applications, infrastructure providers, or automation systems.

### First-Class developer tools integration

Pulumi ESC also integrates with popular developer tools like [GitHub Actions](https://github.com/features/actions), [DirEnv](/docs/esc/integrations/dev-tools/direnv/), and [Docker](/docs/esc/integrations/dev-tools/docker/), enabling teams to pull configurations into their CI/CD pipelines and local development workflows.

### Multi-language SDKs

Pulumi ESC can also be used directly in your [TypeScript/JavaScript](/docs/esc/development/languages-sdks/javascript), [Go](/docs/esc/development/languages-sdks/go), or [Python](/docs/esc/development/languages-sdks/python) code using one of our [language-specific SDKs](/docs/esc/development/languages-sdks/). From the comfort of your favorite IDE, you can create and manage environments, retrieve dynamic secrets and configuration, and automate tagging and versioning directly from your CI/CD workflows.
