---
title: Environments
title_tag: Pulumi ESC Environments
h1: Environments
meta_desc: Pulumi ESC allows you to compose and manage hierarchical collections of configuration and secrets called environments and consume them in various ways.
menu:
  esc:
    identifier: esc-environments
    parent: esc-concepts
    weight: 2
search:
  boost: true
  keywords:
    - environments
    - secrets
    - configuration
aliases:
  - /docs/esc/environments/
  - /docs/esc/environments/working-with-environments/
  - /docs/pulumi-cloud/esc/environments/
  - /docs/esc/environments/dynamic-environment-variables/
  - /docs/esc/environments/syntax/
  - /docs/reference/esc-syntax/
  - /docs/esc/syntax-reference/
  - /docs/esc/reference/
  - /docs/esc/environments/structure/
  - /docs/esc/environments/syntax/top-level-keys/
  - /docs/reference/esc-syntax/top-level-keys/
  - /docs/esc/reference/top-level-keys/
  - /docs/esc/environments/syntax/top-level-keys/values/
  - /docs/reference/esc-syntax/top-level-keys/values/
  - /docs/esc/reference/top-level-keys/values/
  - /docs/esc/environments/syntax/sample-environment-definition/
  - /docs/reference/esc-syntax/sample-environment-definition/
  - /docs/esc/reference/sample-environment-definition/
---

An _environment_ is the fundamental unit of organization in Pulumi ESC (Environments, Secrets, and Configuration): a named, versioned YAML document that defines a collection of configuration and secrets. Environments combine static values, secrets, dynamically retrieved values from supported providers (including all major clouds through OpenID Connect), and values imported from other environments. When an environment is _opened_, ESC evaluates the document and produces a concrete set of values that any application, tool, or Pulumi IaC stack can consume.

Environments are accessible from the [`pulumi` CLI](/docs/iac/download-install/), the [Pulumi SDKs](/docs/esc/languages-sdks/), the [Pulumi Cloud console](#managing-environments), and the [REST API](/docs/pulumi-cloud/cloud-rest-api/). Pulumi ESC is a service of Pulumi Cloud.

## What's in an environment

The following environment shows the building blocks you'll use most often: a static configuration value, a secret, dynamic cloud credentials retrieved through OIDC, and two kinds of output — environment variables and Pulumi stack configuration.

```yaml
values:
  # A static, plaintext configuration value.
  environment: production

  # A secret. The plaintext you enter is encrypted on save (see below).
  stripeApiKey:
    fn::secret: sk_live_abc123

  # Dynamic, short-lived AWS credentials retrieved at open time via OIDC.
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/esc-oidc
          sessionName: pulumi-esc

  # Project the AWS credentials as environment variables.
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}

  # Expose the static value and secret as Pulumi stack configuration.
  pulumiConfig:
    environment: ${environment}
    stripeApiKey: ${stripeApiKey}
```

Every environment is defined under a top-level `values` key, optionally alongside an [`imports`](/docs/esc/concepts/imports/) key that composes in other environments. The sections below describe each of these building blocks conceptually; for the precise YAML grammar, see the reference pages linked throughout.

{{% notes type="info" %}}
The plaintext you supply to `fn::secret` is only present while you author the definition. As soon as the environment is saved, ESC encrypts the value, so when you reopen or re-edit the definition you'll see ciphertext rather than the original text:

```yaml
  stripeApiKey:
    fn::secret:
      ciphertext: ZXNjeAAAAAEAAAEHiyLU8L3J...
```

The value is decrypted back to plaintext only when the environment is opened by a user with the `open` permission.
{{% /notes %}}

## Values: static, secret, and dynamic

The `values` key holds the properties an environment produces. A value can be:

- **Static** — a plain YAML scalar, list, or map (like `environment: production` above). Static values are evaluated once and stored in the definition.
- **Secret** — any value wrapped in [`fn::secret`](/docs/esc/concepts/builtin-functions/fn-secret/) is encrypted at rest and masked in plaintext output. Secrets are only revealed when an environment is opened by a user with sufficient permissions.
- **Dynamic** — values produced at open time by a [provider](/docs/esc/concepts/providers/), such as short-lived cloud credentials from `aws-login` or secrets pulled from an external store like AWS Secrets Manager. Dynamic values are never persisted; they are generated fresh each time the environment is opened.

Values can reference one another using [interpolations and references](/docs/esc/concepts/interpolations-and-references/), and can be transformed with [built-in functions](/docs/esc/concepts/builtin-functions/). Environments can also [import](/docs/esc/concepts/imports/) values from other environments to avoid duplication and share configuration across teams.

## Outputs

Certain reserved properties under `values` give an environment consumer-aware outputs. In the example above, `environmentVariables` projects values as process environment variables and `pulumiConfig` exposes values as Pulumi stack configuration. ESC also supports projecting values to temporary `files` and to Pulumi policy packs via `policyConfig`. See [Outputs](/docs/esc/concepts/outputs/) for the full set of reserved properties and their semantics.

## Opening an environment

_Opening_ an environment is the act of evaluating its definition to produce a concrete set of values. When an environment is opened, ESC resolves its imports, runs providers to fetch dynamic values and credentials, decrypts secrets (for authorized users), evaluates interpolations and functions, and applies [precedence rules](/docs/esc/concepts/imports/#precedence-rules) to produce a single, fully resolved result.

Because evaluation happens at open time rather than when the environment is defined, credentials are always fresh and short-lived, and secrets are never stored in plaintext outside the environment's encrypted state. An open is reproducible: opening the same environment twice in quick succession returns logically equivalent values, apart from any dynamic credentials that are intentionally rotated or re-issued.

## Managing environments

Environments can be created, edited, versioned, and consumed through several surfaces, so you can choose the right tool for interactive work, scripting, or fully automated workflows:

- **Pulumi Cloud console** — a visual editor with an intelligent YAML editor, live evaluation preview, version history, revision tagging, and access-control management. Best for interactive authoring and review.
- **`pulumi` CLI** — the [`pulumi esc` subcommands](/docs/iac/cli/commands/pulumi_env/) cover the full lifecycle: initialize, list, get and set values, edit, open, run commands with injected values, diff and tag versions, clone, and delete. Best for day-to-day work and scripting. See the [CLI reference](/docs/iac/cli/commands/pulumi_env/) for the complete command set.
- **REST API** — the [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api/) performs standard CRUD operations on environments and is the foundation for custom integrations.
- **Automation API** — manage which environments a Pulumi stack imports programmatically with [Automation API](/docs/iac/concepts/automation-api/) (`addEnvironments`, `listEnvironments`, `removeEnvironment`).
- **Pulumi Service Provider** — manage environments as infrastructure-as-code with the [Pulumi Service provider](/docs/esc/integrations/pulumi-service-provider/)'s [`Environment`](/registry/packages/pulumiservice/api-docs/environment/) resource, so environment definitions are themselves provisioned and versioned through Pulumi.

Every change to an environment creates a new immutable revision. See [Versioning](/docs/esc/concepts/versioning/) for how to compare, tag, and pin revisions.

## Using environments with Pulumi IaC

Pulumi IaC has built-in support for ESC, letting you expose an environment's settings and secrets to your stacks instead of maintaining configuration and secrets locally in each `Pulumi.<stack>.yaml`. Values placed under an environment's [`pulumiConfig`](/docs/esc/concepts/outputs/#pulumiconfig) key become stack configuration, and values under [`environmentVariables`](/docs/esc/concepts/outputs/#environmentvariables) are set as process environment variables for the duration of Pulumi CLI operations. Secrets remain encrypted end to end.

There are several ways to reference an environment from a Pulumi IaC program:

- **In a stack configuration file** — add an `environment` block to `Pulumi.<stack>.yaml` listing the environments to import:

  ```yaml
  # Pulumi.dev.yaml
  environment:
    - myapp/dev
  ```

- **With the Pulumi CLI** — use `pulumi config env add <project>/<environment>` to add an environment to the current stack's configuration (or `pulumi config env init` to create a new environment from a stack's existing config).

- **With Automation API** — call `addEnvironments(...)` on a stack's workspace to attach environments programmatically in [Automation API](/docs/iac/concepts/automation-api/) workflows.

Once an environment is referenced, values flow into your program through the standard [configuration API](/docs/iac/concepts/config/#code):

```typescript
// index.ts
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();
const environment = config.require("environment");
const stripeApiKey = config.requireSecret("stripeApiKey");
```

Stacks may only read from environments that belong to the same Pulumi organization. To pin a stack to a specific, fixed revision, append a tag or revision number to the environment name (e.g. `myapp/dev@prod`); see [Versioning](/docs/esc/concepts/versioning/).

## Access control

Access to environments is governed by Pulumi Cloud's role-based access control. Organization-wide defaults (`none`, `read`, `open`, `write`) set the baseline permission every member has, and teams can be granted finer-grained roles (reader, opener, editor, admin) on individual environments. The `open` permission is what allows a user to decrypt secrets and retrieve dynamic credentials, so it can be granted independently of the `write` permission used to edit a definition. For the full permission model, see [Access control](/docs/esc/administration/access-control/).
