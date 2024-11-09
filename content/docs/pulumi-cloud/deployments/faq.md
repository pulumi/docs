---
title_tag: "Pulumi Deployments: FAQ & Pricing"
meta_desc: Frequently asked questions including pricing, general availability, and roadmap.
title: FAQ
h1: Pulumi Deployments FAQ
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: FAQ
    parent: pulumi-cloud-deployments
    weight: 9
    identifier: pulumi-cloud-deployments-faq
  pulumicloud:
    parent: deployments
    weight: 6
aliases:
  - /docs/intro/deployments/faq/
---

## Security and Isolation

Deployments run on single-use virtual machines and compute and storage are never shared across runs. We designed our architecture to maximize isolation. In addition, security features like OIDC allow you to fine tune credential scope, lifetime, and expiration policies at a per-deployment level. It is also possible to use [self-hosted runners](/docs/pulumi-cloud/deployments/customer-managed-agents/) if you require additional isolation.

## Dependency caching

When using Pulumi-managed deployment agents, you have the option to speed up deployments using *dependency caching*.

The caching method is simple: during the first deployment, the deployment agent will automatically detect downloaded dependencies using lock files, zip them up and store the archive in blob storage. During all subsequent deployments, agents will pull such an archive down and unpack it, saving time it would normally take to redownload those dependencies. When your dependencies change, deployment agents will automatically invalidate the old cache and create a new one.

Caches are shared on the project level, so all stacks within a project can share the same cache. However, caches are fully isolated and never shared between customers.

Dependency caching is supported for the following runtimes:

- `.NET` - no special configuration required
- `Python` - ensure that you have `requirements.txt` in the root of your source code.
- `Go` - ensure that you have `go.mod` and `go.sum` in the root of your source code.
- `NodeJS` - ensure that you have `packageManager` field specified in `package.json`. For now, only `npm` and `yarn` are supported.
  - For `npm`, ensure that you have `package-lock.json` in the root of your source code.
  - For `yarn`, ensure that you have `yarn.lock` in the root of your source code.

To confirm dependency caching is working and/or to troubleshoot, check out logs of your deployments, specifically the `Restore Cache` and `Save Cache` steps.

## Common recipes

See [Using Deployments](/docs/pulumi-cloud/deployments/reference/) for common recipes and best practices.

## More FAQ

- [Pulumi IaC FAQ](/docs/iac/support/faq/)
- [Pulumi ESC FAQ](/docs/esc/faq/)
- [Pulumi Cloud FAQ](/docs/pulumi-cloud/faq/)
- [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
- [Pulumi CrossGuard FAQ](/docs/using-pulumi/crossguard/faq/)
- [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
