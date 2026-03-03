---
title: CI/CD Integration
title_tag: "CI/CD Integration | Pulumi Policies"
h1: Policy Enforcement in CI/CD
meta_desc: Enforce Pulumi policies in CI/CD pipelines to automatically block non-compliant infrastructure changes before deployment.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    name: CI/CD Integration
    parent: insights-policy
    weight: 56
---

Pulumi policies integrate with CI/CD pipelines to automatically enforce compliance and security rules on every deployment. When policy packs are enabled for your organization, they run during `pulumi preview` and `pulumi up`, including when these commands execute in CI/CD workflows. Non-compliant changes are blocked before they reach production.

## How policy enforcement works in CI/CD

When your CI/CD pipeline runs Pulumi commands, policy enforcement happens automatically:

1. The pipeline runs `pulumi preview` or `pulumi up`.
1. Pulumi Cloud downloads the policy packs assigned to the stack via [policy groups](/docs/insights/policy/policy-groups/).
1. Each policy pack evaluates the proposed infrastructure changes.
1. If any policy in **advisory** mode detects a violation, a warning is logged but the operation continues.
1. If any policy in **mandatory** mode detects a violation, the operation fails and the pipeline stops.

You can also run policy packs locally in CI by passing the `--policy-pack` flag:

```bash
pulumi preview --policy-pack /path/to/policy-pack
```

## GitHub Actions

Pulumi provides an official [GitHub Action](https://github.com/pulumi/actions) that supports policy enforcement out of the box. When your stack has policy packs enabled in Pulumi Cloud, the action enforces them automatically.

### Caching policy packs

GitHub Actions downloads policy packs on each workflow run. You can cache the `~/.pulumi/policies` directory to avoid re-downloading them and speed up your workflows.

```yaml
- name: Cache Pulumi policy packs
  uses: actions/cache@v4
  with:
    path: ~/.pulumi/policies
    key: ${{ runner.os }}-pulumi-policies-${{ hashFiles('**/package.json') }}
    restore-keys: |
      ${{ runner.os }}-pulumi-policies-
```

For complete workflow examples including plugin caching, multiple languages, and environment configuration, see the [GitHub Actions guide](/docs/iac/guides/continuous-delivery/github-actions/#caching-plugins-and-policy-packs).

## Google Cloud Build

Google Cloud Build can enforce Pulumi policies using the Pulumi Cloud Builder. Policy packs enabled through Pulumi Cloud are applied automatically during build steps that run `pulumi preview` or `pulumi up`.

For detailed setup instructions, see the [Google Cloud Build guide](/docs/iac/guides/continuous-delivery/google-cloud-build/).

## Other CI/CD providers

Pulumi policies work with any CI/CD system that can run the Pulumi CLI. Policy enforcement requires no special configuration. If your stack has policy packs enabled in Pulumi Cloud, they are enforced automatically. For local policy execution, pass the `--policy-pack` flag.

Pulumi provides integration guides for many CI/CD providers:

- [AWS Code Services](/docs/iac/guides/continuous-delivery/aws-code-services/)
- [Azure DevOps](/docs/iac/integrations/azure-devops/)
- [CircleCI](/docs/iac/guides/continuous-delivery/circleci/)
- [GitLab CI](/docs/iac/guides/continuous-delivery/gitlab-ci/)
- [Jenkins](/docs/iac/guides/continuous-delivery/jenkins/)
- [Travis CI](/docs/iac/guides/continuous-delivery/travis/)

For the full list of CI/CD integrations, see the [continuous delivery guides](/docs/iac/guides/continuous-delivery/).

## Best practices

- **Use policy groups to vary enforcement by environment.** Apply stricter (mandatory) policies to production stacks and advisory policies to development stacks. See [policy groups](/docs/insights/policy/policy-groups/) for details.
- **Cache policy packs in CI.** Caching the `~/.pulumi/policies` directory reduces download time on repeated runs.
- **Test policy changes before enforcing.** Publish policy pack updates and test them in advisory mode before switching to mandatory enforcement.
- **Run `pulumi preview` in pull request checks.** This catches policy violations early, before changes are merged.
