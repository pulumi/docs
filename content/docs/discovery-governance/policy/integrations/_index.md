---
title: Integrations
title_tag: Integrations | Pulumi Policies
meta_desc: Integrate Pulumi Policies with third-party security and compliance tools to enhance your infrastructure security and compliance posture.
---

Pulumi Policies integrates with leading security and compliance tools to provide comprehensive protection for your infrastructure as code. These integrations enable you to leverage specialized scanning capabilities and security insights alongside Pulumi's native policy enforcement.

## Third-party integrations

- [Snyk Container Scanning](/docs/insights/policy/integrations/snyk-policy/) - Scan container images for vulnerabilities using Snyk and enforce results as Pulumi policies.
- [AWS Organizations Tag Policies](/docs/insights/policy/integrations/aws-organizations-tag-policies/) - Validate that infrastructure resources have required tags by integrating with AWS Organizations tag policies.

## CI/CD integration

Pulumi policies are enforced automatically when `pulumi preview` or `pulumi up` runs in CI/CD pipelines. For detailed guidance on integrating policy enforcement into your CI/CD workflows, including caching policy packs in GitHub Actions and enforcing policies in Google Cloud Build, see the [CI/CD integration guide](/docs/insights/policy/ci-cd/).
