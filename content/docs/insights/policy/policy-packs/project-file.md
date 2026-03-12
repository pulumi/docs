---
title_tag: Policy Pack Project File Reference
meta_desc: Documentation of the settings available in the PulumiPolicy.yaml policy pack project file.
title: Policy pack project file
h1: Policy pack project file reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: Project file reference
    parent: policy-packs
    weight: 25
aliases:
  - /docs/insights/policy/policy-packs/pulumi-policy-yaml/
---

Every Pulumi policy pack has a project file, `PulumiPolicy.yaml`, that specifies metadata about the policy pack such as its runtime and version. This file is analogous to the [`Pulumi.yaml`](/docs/iac/concepts/projects/project-file/) project file used by Pulumi IaC programs. The file must be named `PulumiPolicy.yaml` (case-sensitive) and placed in the root of your policy pack directory.

When you create a new policy pack with `pulumi policy new`, the CLI generates this file automatically.

## Attributes

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

| Name | Required | Description |
| - | - | - |
| `runtime` | required | Must be `nodejs`. Can be a string or an object with `name` and `options` fields. See [runtime options](#runtime-options). |
| `version` | optional | The version of the policy pack, following [semantic versioning](https://semver.org/). Overrides the version in `package.json` when set. |
| `main` | optional | Path to the policy pack entry point, relative to `PulumiPolicy.yaml`. Defaults to the directory containing `PulumiPolicy.yaml`. |
| `description` | optional | A brief description of the policy pack. |
| `author` | optional | The author of the policy pack. |
| `website` | optional | A URL for the policy pack's website or repository. |
| `license` | optional | The license for the policy pack (e.g., `Apache-2.0`, `MIT`). |

{{% /choosable %}}

{{% choosable language python %}}

| Name | Required | Description |
| - | - | - |
| `runtime` | required | Must be `python`. Can be a string or an object with `name` and `options` fields. See [runtime options](#runtime-options). |
| `version` | optional | The version of the policy pack, following [semantic versioning](https://semver.org/). This is the primary way to set the version for Python packs. |
| `main` | optional | Path to the policy pack entry point, relative to `PulumiPolicy.yaml`. Defaults to the directory containing `PulumiPolicy.yaml`. |
| `description` | optional | A brief description of the policy pack. |
| `author` | optional | The author of the policy pack. |
| `website` | optional | A URL for the policy pack's website or repository. |
| `license` | optional | The license for the policy pack (e.g., `Apache-2.0`, `MIT`). |

{{% /choosable %}}

{{% choosable language opa %}}

[OPA (Open Policy Agent)](https://github.com/pulumi/pulumi-policy-opa) policy packs let you write policies in [Rego](https://www.openpolicyagent.org/docs/latest/policy-language/) instead of TypeScript or Python. Install the analyzer plugin with `pulumi plugin install analyzer policy-opa`.

| Name | Required | Description |
| - | - | - |
| `runtime` | required | Must be `opa`. |
| `version` | optional | The version of the policy pack, following [semantic versioning](https://semver.org/). |
| `description` | optional | A brief description of the policy pack. |
| `inputFormat` | optional | Controls how resource properties are structured before OPA evaluation. Set to `kubernetes-admission` to enable [Kubernetes Admission Controller compatibility](#inputformat). When omitted, resources use the default Pulumi OPA input structure. |

{{% /choosable %}}

{{< /chooser >}}

### `runtime` options

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

The `runtime` attribute can be a simple string or an object with additional options.

**Simple form:**

```yaml
runtime: nodejs
```

**Object form:**

```yaml
runtime:
  name: nodejs
```

The Node.js runtime does not have additional options specific to policy packs.

{{% /choosable %}}

{{% choosable language python %}}

The `runtime` attribute can be a simple string or an object with additional options.

**Simple form:**

```yaml
runtime: python
```

**Object form with options:**

```yaml
runtime:
  name: python
  options:
    virtualenv: venv
```

The following option is available:

| Name | Description |
| - | - |
| `virtualenv` | Path to a Python virtual environment to use when running the policy pack. Defaults to `venv` for new projects created with `pulumi policy new`. Pulumi automatically creates the virtual environment and installs dependencies from `requirements.txt` into it. |

When `virtualenv` is set, Pulumi manages the virtual environment for you. If you prefer to manage it yourself (for example, with [Pipenv](https://github.com/pypa/pipenv)), remove the `virtualenv` option and use the simple string form.

For more details on Python dependency management in policy packs, see the [Policies FAQ](/docs/support/faq/policies/#how-are-dependencies-managed-with-python-policy-packs).

{{% /choosable %}}

{{% choosable language opa %}}

The `opa` runtime is always specified as a simple string and has no additional options:

```yaml
runtime: opa
```

{{% /choosable %}}

{{< /chooser >}}

### `inputFormat`

The `inputFormat` field is specific to OPA policy packs. The only supported value is `kubernetes-admission`, which wraps Kubernetes resources in the [OPA Gatekeeper](https://open-policy-agent.github.io/gatekeeper/) AdmissionReview structure before evaluation. This lets you reuse existing Gatekeeper constraint templates (`.rego` files) with Pulumi without modification.

When `inputFormat: kubernetes-admission` is set:

- Kubernetes resources are presented as `input.review.object` with `input.review.kind`, `input.review.name`, and `input.review.namespace` fields, matching the Gatekeeper schema.
- Non-Kubernetes resources are silently skipped.
- Per-rule policy configuration is injected as `input.parameters` for Gatekeeper Constraint compatibility.
- Pulumi-specific metadata (URN, options, provider) is available via `input._pulumi`.
- Both the Gatekeeper `violation[{"msg": ...}]` map format and the standard string-based rule format are supported.

For more details, see the [Pulumi OPA Policy Bridge documentation](https://github.com/pulumi/pulumi-policy-opa).

### Version handling

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

The version is read from `package.json` by default. If a `version` field is set in `PulumiPolicy.yaml`, it takes precedence over `package.json`.

Each version can only be published once. When you publish a new version, update the version number before running `pulumi policy publish`. See [managing policy pack versions](/docs/insights/policy/policy-packs/authoring/#managing-policy-pack-versions) for details.

{{% /choosable %}}

{{% choosable language python %}}

The version is read from the `version` field in `PulumiPolicy.yaml`. There is no fallback file.

Each version can only be published once. When you publish a new version, update the version number before running `pulumi policy publish`. See [managing policy pack versions](/docs/insights/policy/policy-packs/authoring/#managing-policy-pack-versions) for details.

{{% /choosable %}}

{{% choosable language opa %}}

The version is read from the `version` field in `PulumiPolicy.yaml`.

Each version can only be published once. When you publish a new version, update the version number before running `pulumi policy publish`.

{{% /choosable %}}

{{< /chooser >}}

## Examples

{{< chooser language "typescript,python,opa" >}}

{{% choosable language typescript %}}

**Minimal:**

```yaml
runtime: nodejs
```

**Full-featured:**

```yaml
runtime: nodejs
version: 1.2.0
main: src/
description: Acme Corp security and compliance policies
author: Platform Team
website: https://github.com/acme/policy-packs
license: Apache-2.0
```

{{% /choosable %}}

{{% choosable language python %}}

**Minimal:**

```yaml
runtime:
  name: python
  options:
    virtualenv: venv
```

**Full-featured:**

```yaml
runtime:
  name: python
  options:
    virtualenv: venv
version: 1.2.0
main: src/
description: Acme Corp security and compliance policies
author: Platform Team
website: https://github.com/acme/policy-packs
license: Apache-2.0
```

{{% /choosable %}}

{{% choosable language opa %}}

**Minimal:**

```yaml
runtime: opa
description: AWS security policies
```

**With version and Kubernetes Admission Controller compatibility:**

```yaml
runtime: opa
version: 1.0.0
description: Kubernetes Gatekeeper policies
inputFormat: kubernetes-admission
```

{{% /choosable %}}

{{< /chooser >}}
