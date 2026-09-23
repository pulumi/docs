---
title: Policy as code
title_tag: "Pulumi Policies | Discovery & governance"
meta_desc: Enforce compliance and security across all cloud infrastructure using policy as code with Pulumi Policies, for both IaC stacks and discovered resources.
h1: Policy as code
menu:
  discovery-governance:
    name: Policy as code
    parent: dg-concepts
    weight: 40
aliases:
- /docs/guides/crossguard/
- /policy-as-code/
- /docs/using-pulumi/crossguard/
- /docs/iac/packages-and-automation/crossguard/
- /docs/iac/using-pulumi/crossguard/
- /docs/iac/crossguard/
- /docs/insights/policy-as-code/
- /docs/insights/policy/core-concepts/
- /docs/iac/crossguard/core-concepts/
- /docs/iac/packages-and-automation/crossguard/core-concepts/
- /docs/iac/using-pulumi/crossguard/core-concepts/
- /docs/insights/policy/
- /docs/discovery-governance/policy/
- /docs/insights/policy/policy-as-code/snyk-policy/
- /docs/iac/crossguard/snyk-policy/
- /docs/guides/crossguard/snyk-container-scanning/
- /docs/using-pulumi/crossguard/snyk-container-scanning/
- /docs/using-pulumi/crossguard/snyk-policy/
- /docs/iac/packages-and-automation/crossguard/snyk-policy/
- /docs/iac/using-pulumi/crossguard/snyk-policy/
- /docs/insights/policy/snyk-policy/
- /docs/insights/policy/integrations/snyk-policy/
- /docs/discovery-governance/policy/integrations/snyk-policy/
---

Policy as code lets you write the rules your infrastructure must follow as code, then check every resource against them automatically. Pulumi Policies applies policy as code to resources you deploy with Pulumi IaC and to resources that Discovery finds in your cloud accounts, however those resources were created.

## What is policy as code?

Policy as code applies software engineering practices to infrastructure rules. Instead of documenting compliance requirements in a wiki or configuring them by hand in each cloud provider's console, you write them as code. That code is version-controlled, reviewed, tested, and shared like any other code, and a machine checks your infrastructure against it on every change.

Policy as code typically serves a few goals:

- **Security and compliance**: Prevent common misconfigurations, such as public storage buckets, exposed databases, or overly permissive network rules, and map your rules to frameworks like CIS, PCI DSS, or HIPAA.
- **Cost control**: Restrict expensive instance types, require the tags you use to allocate costs, and flag unused resources.
- **Early feedback**: Check changes before they're deployed, when fixing a violation is cheapest, instead of finding the problem in production.
- **Consistent standards**: Encode organizational conventions once and apply them to every team and environment.

## Policy as code in Pulumi

Pulumi Policies is Pulumi's policy as code product. You write policies in TypeScript, JavaScript, Python, or OPA (Rego), or use the pre-built policy packs that Pulumi publishes, and they apply to infrastructure written in any language.

{{% notes type="info" %}}
Policies run as [analyzer plugins](/docs/iac/concepts/plugins/#analyzer-plugins), which the Pulumi CLI installs automatically.
{{% /notes %}}

### Policies, policy packs, and policy groups

Pulumi Policies organizes rules in three layers:

1. **Policies** are individual rules that validate a resource or a whole stack, for example "S3 buckets must be private" or "VMs must use approved instance types."
1. **[Policy packs](/docs/discovery-governance/concepts/policy-packs/)** are versioned collections of related policies that you publish and manage together. Use Pulumi's [pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/), such as Pulumi Best Practices or packs for CIS, HITRUST, ISO 27001, NIST, PCI DSS, and CMMC, or [write your own](/docs/discovery-governance/guides/write-a-policy-pack/).
1. **[Policy groups](/docs/discovery-governance/concepts/policy-groups/)** apply policy packs to specific stacks or cloud accounts in Pulumi Cloud, so you can enforce stricter policies in production than in development.

### IaC-managed and discovered resources

When a policy runs depends on how the resource is managed.

**IaC-managed resources are checked before they're provisioned.** Pulumi evaluates policies against the resources a Pulumi program declares during `pulumi preview` and `pulumi up`, before anything changes in your cloud provider. A violation of a mandatory policy stops the deployment. This applies to Pulumi IaC stacks in every language. It also applies to Terraform and OpenTofu stacks that use Pulumi Cloud [remote execution](/docs/integrations/terraform/remote-execution/#enforce-policy), where policies evaluate the plan before an apply proceeds.

**Discovered resources are checked after they're provisioned.** [Discovery](/docs/discovery-governance/concepts/discovery/) scans your cloud accounts on a schedule and finds every resource in them, whether it was created with Pulumi, CloudFormation, Terraform, the cloud console, or a cloud service itself. Policies evaluate those resources after the fact and report violations in [Policy Findings](/docs/discovery-governance/operations/policy-findings/). They can't block a change that has already happened, but they cover infrastructure that no IaC tool manages. Terraform stacks that store their state in Pulumi Cloud but [run locally](/docs/integrations/terraform/state-backend/#audit-policies) are also checked this way.

### Enforcement modes

The two cases above correspond to Pulumi's two enforcement modes. These are Pulumi terms, and you choose one for each policy group:

- **Preventative** policy groups evaluate IaC-managed resources during `pulumi preview` and `pulumi up`, and can block a deployment.
- **Audit** policy groups evaluate discovered resources and the latest state of stacks, and report violations without blocking anything.

Each policy also has an **enforcement level**, which is specific to Pulumi as well: `advisory` reports a violation as a warning, `mandatory` blocks the deployment, `remediate` fixes the resource automatically, and `disabled` turns the policy off. Audit policy groups report violations rather than blocking them, whatever the enforcement level. For how to choose between them, see [Policy groups](/docs/discovery-governance/concepts/policy-groups/#best-practices).

### Local execution and Pulumi Cloud

#### Local policy execution

The open source Pulumi CLI runs policy packs locally. Pass the `--policy-pack` flag to `pulumi preview` or `pulumi up`:

```bash
pulumi preview --policy-pack /path/to/policy-pack
```

To apply more than one policy pack, repeat the flag:

```bash
pulumi up --policy-pack /path/to/pack-1 --policy-pack /path/to/pack-2
```

Local execution works with any backend, including the self-managed backend, and with both open source and custom policy packs. The policy pack must be on disk where you run Pulumi, and the machine needs the pack's [runtime](/docs/discovery-governance/concepts/policy-packs/#runtime-requirements) installed.

#### Pulumi Cloud

{{< pulumi-cloud "policy-enforcement" />}}

Pulumi Cloud adds central management on top of local execution:

- Apply policy packs to many stacks and cloud accounts with [policy groups](/docs/discovery-governance/concepts/policy-groups/), without passing `--policy-pack` on each command. Pulumi downloads the packs automatically.
- Use Pulumi's [pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/): Pulumi Best Practices on the Essentials edition and above, and compliance-framework packs on the Enterprise edition.
- Publish your own packs to your organization, with versioning and rollback.
- Run audit policies against discovered resources. Audit policies require Pulumi Cloud and aren't available with a self-managed backend.
- Track violations across your organization in [Policy Findings](/docs/discovery-governance/operations/policy-findings/).

## Languages

You can write policies in TypeScript, JavaScript, Python, or [OPA (Rego)](/docs/discovery-governance/guides/write-opa-policies/). Policies in any of these languages apply to Pulumi programs written in any language. For the SDKs, see the [Policy API and SDK reference](/docs/discovery-governance/reference/policy-api-sdk/).

## Next steps

Choose your path based on your needs:

- **New to Pulumi Policies?** Start with the [Get Started guide](/docs/discovery-governance/get-started/enforce-policy-as-code/) to configure your first policy group and apply policies to stacks or cloud accounts.
- **Want ready-made compliance rules?** Browse [pre-built policy packs](/docs/discovery-governance/guides/pre-built-policy-packs/) for CIS, PCI DSS, HITRUST, NIST, ISO 27001, CMMC, and other frameworks. Enable them directly from Pulumi Cloud with no code required.
- **Need custom policies?** Learn to [write custom policy packs](/docs/discovery-governance/guides/write-a-policy-pack/) in TypeScript, JavaScript, Python, or OPA (Rego). Create organization-specific rules tailored to your requirements.
- **Managing compliance?** View violations and track remediation progress in [Policy Findings](/docs/discovery-governance/operations/policy-findings/). Triage issues, assign owners, and monitor compliance trends across your organization.
- **Configuring discovered resources?** Visit the [Discovery Get Started tutorial](/docs/discovery-governance/get-started/) for a detailed guide on audit policies for cloud resources discovered outside Pulumi.
- **Using the CLI?** See the [`pulumi policy` commands](/docs/iac/cli/commands/pulumi_policy/) to create, publish, and manage policy packs from the command line.
- **Enforcing policies in CI/CD?** Learn how to [integrate policy enforcement](/docs/discovery-governance/guides/policies-in-ci-cd/) into GitHub Actions, Google Cloud Build, and other CI/CD pipelines.
- **Building custom tooling?** Explore the [API & SDK reference](/docs/discovery-governance/reference/policy-api-sdk/) for the Policy SDK and Pulumi Cloud REST API endpoints.
- **Looking for tutorials?** Follow the [custom policy pack tutorial](/dev/tutorials/custom-policy-pack/) to create, validate, and publish a policy pack step by step. Or learn how to [evaluate Terraform compliance with Pulumi](/dev/tutorials/eval-compliance-terraform/).
- **Building an internal developer platform?** Explore advanced patterns including [policies as tests](/docs/idp/guides/best-practices/patterns/policies-as-tests/), [validating component inputs using policy functions](/docs/idp/guides/best-practices/patterns/validating-component-inputs-using-policy-functions/), and [cost control using components, policies, and constrained inputs](/docs/idp/guides/best-practices/patterns/cost-control-using-components-policies-constrained-inputs/).

For common questions and troubleshooting, see the [FAQ](/docs/support/faq/policies/).
