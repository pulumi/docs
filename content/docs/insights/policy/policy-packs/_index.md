---
title: Policy Packs
title_tag: Policy Packs | Pulumi Policies
h1: Policy Packs
meta_desc: How policy packs are structured, versioned, and applied, including the runtime each pack requires on the machines that run Pulumi.
menu:
  insights:
    parent: insights-policy
    identifier: policy-packs
    weight: 20
aliases:
  - /docs/insights/policy/configuration/
  - /docs/using-pulumi/crossguard/configuration/
  - /docs/guides/crossguard/configuration/
  - /docs/iac/packages-and-automation/crossguard/configuration/
  - /docs/iac/crossguard/configuration/
  - /docs/iac/using-pulumi/crossguard/configuration/
  - /docs/insights/policy/policy-as-code/configuration/
---

A policy pack is the unit that Pulumi Policies publishes, versions, and applies. Each pack is a project directory holding a `PulumiPolicy.yaml` file and one or more policies, and each policy inspects resources and reports a violation when something does not meet your standards.

A pack does nothing on its own. To enforce it, add it to a [policy group](/docs/insights/policy/policy-groups/), which determines the stacks or cloud accounts it applies to and whether violations block a deployment or are reported for later.

## Types of policy packs

- <a id="pre-built-policy-packs"></a>**[Pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/)** are written and maintained by Pulumi. They cover common compliance frameworks, including CIS, PCI DSS, HITRUST, NIST, ISO 27001, and CMMC, as well as security, cost, and operational best practices for AWS, Azure, and Google Cloud. You enable them from Pulumi Cloud without writing any code. The Pulumi Best Practices and AWS Organizations Tag Policies packs are included in the Team edition and above; the compliance-framework packs require the [Business Critical edition](/pricing/#pre-built-policy-packs).

- <a id="custom-policy-packs"></a>**[Custom policy packs](/docs/insights/policy/policy-packs/authoring/)** are the ones you write yourself, in TypeScript, Python, or [OPA (Rego)](/docs/insights/policy/policy-packs/authoring/#opa), to enforce requirements specific to your organization. You can test a custom pack locally with `pulumi preview --policy-pack` before publishing it to Pulumi Cloud.

The two are meant to be combined. A policy group can hold a pre-built pack and your own pack at the same time, so you can adopt a framework wholesale and layer your organization's rules on top of it.

## What a policy pack contains

Every pack has a [`PulumiPolicy.yaml`](/docs/insights/policy/policy-packs/project-file/) project file, the policy equivalent of `Pulumi.yaml`. It declares the pack's runtime and, optionally, its version, description, and entry point.

Each policy in the pack has a name, a description, and a validation function. A policy can examine a single resource as it is declared, or the whole stack at once when a rule depends on more than one resource. Policies also carry [metadata](/docs/insights/policy/policy-packs/metadata/) that Pulumi surfaces alongside findings: a severity, remediation steps, links to external documentation, and references to the compliance framework control a policy implements.

Enforcement is set per policy. A policy can warn (`advisory`), block the deployment (`mandatory`), fix the violation automatically (`remediate`), or be turned off (`disabled`). A policy group can override these levels for the packs it applies, so the same pack can warn in one group and block in another.

A policy can also define a configuration schema, which turns fixed values into parameters that are set when the pack is applied. That is what lets one pack enforce a stricter threshold in production than in development without maintaining two copies of it.

## Versions

Policy packs follow [semantic versioning](https://semver.org/). Publishing a pack with [`pulumi policy publish`](/docs/iac/cli/commands/pulumi_policy_publish/) creates a new version rather than replacing the existing one.

A policy group references a particular version, so publishing does not change what is enforced until a group is pointed at the new version. If you would rather track releases automatically, enable `latest` instead of a specific version.

## Runtime requirements

Policy packs run on the machine that runs Pulumi, so the pack's runtime must be installed there. The [`runtime`](/docs/insights/policy/policy-packs/project-file/) declared in the pack's `PulumiPolicy.yaml` determines what is required, not the language your Pulumi program is written in. A Python or Go stack governed by a TypeScript policy pack still needs Node.js.

| Pack runtime | Requirement on the machine running Pulumi |
|:-------------|:--------------------------------------------------------------------------------|
| `nodejs` | Node.js |
| `python` | Python. Pulumi creates the virtual environment and installs dependencies for you. |
| `opa` | None. Pulumi CLI v3.227.0 and later install the OPA analyzer plugin on first use. |

**Pulumi's pre-built policy packs all run on Node.js.** If you enable CIS, PCI DSS, NIST, HITRUST, ISO 27001, CMMC, or Pulumi Best Practices, every machine that runs `pulumi preview` or `pulumi up` against a governed stack needs Node.js installed.

Bun is not a substitute. Although Pulumi supports [`runtime: bun`](/docs/iac/languages-sdks/javascript/#bun-runtime) for Pulumi programs, a policy pack that declares `runtime: nodejs` is always executed with Node.js, even when the stack's own program uses Bun.

When Pulumi Cloud enforces a policy pack through a [policy group](/docs/insights/policy/policy-groups/), the CLI downloads the pack to `~/.pulumi/policies` and installs its dependencies the first time it encounters a given version. That first run needs network access to the relevant package registry; later runs use the cached copy.

## Next steps

- [Browse pre-built policy packs](/docs/insights/policy/policy-packs/pre-built-packs/)
- [Write custom policy packs](/docs/insights/policy/policy-packs/authoring/)
- [Run policies in CI/CD](/docs/insights/policy/ci-cd/)
- [PulumiPolicy.yaml project file reference](/docs/insights/policy/policy-packs/project-file/)
- [Configure policy groups](/docs/insights/policy/policy-groups/)
- [View policy findings](/docs/insights/policy/policy-findings/)
