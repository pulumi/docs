---
title: Enforce policies in CI/CD
title_tag: "Enforce policies in CI/CD | Pulumi Policies"
h1: Enforce policies in CI/CD
meta_desc: Enforce Pulumi policies in CI/CD pipelines to automatically block non-compliant infrastructure changes before deployment.
menu:
  discovery-governance:
    name: Enforce policies in CI/CD
    parent: dg-guides
    weight: 90
aliases:
- /docs/insights/policy/ci-cd/
- /docs/discovery-governance/policy/ci-cd/
---

Pulumi policies integrate with CI/CD pipelines to automatically enforce compliance and security rules on every deployment. When policy packs are enabled for your organization, they run during `pulumi preview` and `pulumi up`, including when these commands execute in CI/CD workflows. Non-compliant changes are blocked before they reach production.

## How policy enforcement works in CI/CD

{{< pulumi-cloud "policy-enforcement" />}}

When your CI/CD pipeline runs Pulumi commands, policy enforcement happens automatically:

1. The pipeline runs `pulumi preview` or `pulumi up`.
1. Pulumi Cloud downloads the policy packs assigned to the stack via [policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/).
1. Each policy pack evaluates the proposed infrastructure changes.
1. If any policy in **advisory** mode detects a violation, a warning is logged but the operation continues.
1. If any policy in **mandatory** mode detects a violation, the operation fails and the pipeline stops.

{{% notes type="warning" %}}
Your CI image needs the policy pack's [runtime](/docs/discovery-governance/concepts/policy-as-code/policy-packs/#runtime-requirements) installed, which is not necessarily the runtime your Pulumi program uses. All of Pulumi's pre-built policy packs run on Node.js, so a Python or Go pipeline that enforces one needs Node.js in the image as well.
{{% /notes %}}

You can also run policy packs locally in CI by passing the `--policy-pack` flag:

```bash
pulumi preview --policy-pack /path/to/policy-pack
```

## Pulumi Deployments

[Pulumi Deployments](/docs/deployments/) runs `pulumi preview` and `pulumi up` for you in Pulumi Cloud, triggered by a push to your repository, a pull request, a schedule, or an API call. Because Deployments runs the same commands, the policy packs in your stack's policy groups apply with no extra setup: a mandatory violation fails the deployment, and advisory violations appear in its logs. If you use a [custom executor image](/docs/deployments/concepts/settings/custom-executor-images/), make sure it includes the runtime your policy packs need.

## Pulumi CI/CD integrations

Pulumi maintains integrations for two CI/CD systems. Both run the Pulumi CLI, so policy groups apply to them automatically.

### GitHub Actions

The [Pulumi GitHub Action](https://github.com/pulumi/actions) installs the Pulumi CLI and runs Pulumi commands in your workflows. When your stack has policy packs enabled in Pulumi Cloud, the action enforces them.

GitHub Actions downloads policy packs on each workflow run. Cache the `~/.pulumi/policies` directory to avoid downloading them again and speed up your workflows:

```yaml
- name: Cache Pulumi policy packs
  uses: actions/cache@v4
  with:
    path: ~/.pulumi/policies
    key: ${{ runner.os }}-pulumi-policies-${{ hashFiles('**/package.json') }}
    restore-keys: |
      ${{ runner.os }}-pulumi-policies-
```

For complete workflow examples, see the [GitHub Actions guide](/docs/iac/operations/continuous-delivery/github-actions/#speed-up-runs-with-caching).

### Azure Pipelines

The [Pulumi Task Extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) runs Pulumi commands in Azure Pipelines, and enforces the policy packs enabled for your stack. See the [Azure DevOps guide](/docs/iac/operations/continuous-delivery/azure-devops/).

## Other CI/CD systems

Policy enforcement works in any CI/CD system that can run the Pulumi CLI, with no policy-specific configuration. Set up Pulumi in your pipeline by following the [continuous delivery guide](/docs/iac/operations/continuous-delivery/) for your system. Once the pipeline runs `pulumi preview` or `pulumi up`, the policy packs enabled for the stack are enforced.

## Best practices

- **Use policy groups to vary enforcement by environment.** Apply stricter (mandatory) policies to production stacks and advisory policies to development stacks. See [policy groups](/docs/discovery-governance/concepts/policy-as-code/policy-groups/) for details.
- **Test policy changes before enforcing.** Publish policy pack updates and test them in advisory mode before switching to mandatory enforcement.
- **Run `pulumi preview` in pull request checks.** This catches policy violations early, before changes are merged.
