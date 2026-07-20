---
title_tag: "Custom Executor Images | Pulumi Deployments"
meta_desc: Override the default deployment image to pin a Pulumi CLI version or add your own tools
title: "Custom Executor Images"
h1: "Custom Executor Images"
menu:
  deployments:
    name: Custom Executor Images
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-custom-executor-images
    weight: 80
---

By default, deployments run inside the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) image, which includes the `pulumi` CLI and [LTS versions](https://github.com/pulumi/pulumi-docker-containers/blob/main/README.md#version-policy) of all supported language runtimes. You can override this from the **Custom Executor Image** field in your stack's deployment settings, either to pin a specific Pulumi CLI version or to use your own image with additional tools.

When you enable **Use a custom executor image**, you provide an **Image reference** (required) and, for an image in a private registry, an **Image repository username** and **Image repository password**.

{{% notes type="warning" %}}
Private registries are authenticated with **static username and password credentials only** — OIDC and IAM-role-based pulls are not supported for custom executor images. As a result, a **private Amazon ECR** registry does not work: ECR has no long-lived credentials. Its registry password is an authorization token from `aws ecr get-login-password` that expires after 12 hours, so a pasted token soon stops working and deployments can no longer pull the image. (A *public* image on [Amazon ECR Public](https://gallery.ecr.aws/) needs no credentials and works fine.)

If you need to pull a private image from ECR — or your security model requires short-lived registry credentials — use [Customer-Managed Workflow Runners](/docs/deployments/concepts/customer-managed-runners/), which run in your own infrastructure and can authenticate to the registry with an IAM role or any other mechanism you configure.
{{% /notes %}}

For guidance on choosing between a pre-run install hook and a custom image, building a custom image, supported base images, and the trade-offs to consider, see [Deployment execution environment](/docs/deployments/guides/custom-images/).
