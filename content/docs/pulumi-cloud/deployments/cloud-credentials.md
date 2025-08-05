---
title_tag: Pulumi Deployments Cloud Credentials
meta_desc: This page explains the options for supplying cloud credentials to a Pulumi Deployment
title: Supplying Cloud Credentials to Pulumi Deployments
h1: Supplying Cloud Credentials to Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Cloud Credentials
    parent: pulumi-cloud-deployments
    weight: 30
    identifier: pulumi-cloud-deployments-cloud-credentials
---

In order for a Pulumi IaC operation like `update` or `preview` work, the Pulumi CLI must be able to access credentials that will allow it to perform the necessary CRUD operations on the resources in your stack. In order for Pulumi Deployments to access the necessary cloud credentials to run your Pulumi operation there are two common approaches you can take:

1. **Use [Pulumi Deployments' OIDC integration](/docs/pulumi-cloud/deployments/oidc/)** where possible (we support [AWS](/docs/pulumi-cloud/deployments/oidc/aws/), [Azure](/docs/pulumi-cloud/deployments/oidc/azure/), and [Google Cloud](/docs/pulumi-cloud/deployments/oidc/gcp/)), and store any remaining required secrets or configuration in [Pulumi Deployments Environment Variables](/docs/pulumi-cloud/deployments/reference/#deployment-settings).
2. **Use [Pulumi ESC](/docs/esc/)** to define an Environment (or Environments), and [import the environment(s) into your stack](/docs/esc/get-started/integrate-with-pulumi-iac/).

## Choosing between Pulumi ESC Environments and Pulumi Deployments OIDC

Pulumi recommends using ESC Environments over Deployments OIDC for the following reasons:

- Pulumi ESC Environments are more portable compared to Deployments OIDC: Ignoring any locally stored credentials, e.g., environment variables set in your command shell, you can have greater confidence that a Pulumi Deployments operation will succeed if it succeeds on your local machine.
- Pulumi ESC Environments are more modular compared to Deployments OIDC: Deployments settings are applied on a per-stack basis, which means that the OIDC configuration must be repeated for every stack that is using Deployments OIDC. In comparison, Pulumi ESC Environments are centrally defined and may be imported into any number of Pulumi stacks.
- Pulumi ESC has [more native integrations](/docs/esc/integrations/) with popular clouds for both [OIDC](/docs/esc/integrations/dynamic-login-credentials/) and [managed secrets services](/docs/esc/integrations/dynamic-secrets/), and other tools like [Kubernetes](/docs/esc/integrations/kubernetes/kubernetes/), [Docker](/docs/esc/integrations/dev-tools/docker/), etc.
- Pulumi ESC Environments are composable: [Environments can import other Environments](/docs/esc/environments/imports/), which removes the need to repeat configuration information.
- Pulumi ESC Environments support [versioning](/docs/esc/environments/versioning/), allowing you to roll out changes to an environment in a controlled fashion by pinning Environment imports to a specific version of an Environment.

{{% notes type="info" %}}
One important difference to be mindful of is that Pulumi Deployments OIDC applies to the entire Deployments process (including pre-run commands), whereas a Pulumi ESC environment only applies to the Pulumi IaC operation (e.g. `pulumi up`). However, there is a workaround for this limitation: Each pre-run command can be prefixed with the [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run/) command so that the pre-run command executes in the context of specified Pulumi ESC Environment.

For example, to install packages from a private repository, you might run the following pre-run command:

```bash
pulumi env run my-esc-project/my-esc-environment -- npm install
```

{{% /notes %}}

## Next Steps

Both Pulumi Deployments OIDC and Pulumi ESC require configuring an OIDC Identity Provider in your cloud environment in order to enable the secure exchange of tokens between Pulumi Cloud and your cloud provider in order to obtain temporary credentials. For more information:

- If using Pulumi ESC, see [Configuring OpenID Connect for Pulumi ESC](/docs/esc/environments/configuring-oidc/).
- If using Pulumi Deployments OIDC, see [OIDC Setup for Pulumi Deployments](/docs/pulumi-cloud/deployments/oidc/).

After an OIDC Identity Provider has been configured:

- If you are using Pulumi ESC, ensure that your Pulumi Deployments token has permissions to open any imported Pulumi ESC Environments. For more information, see [Deployment Permissions](/docs/pulumi-cloud/deployments/reference/#deployment-permissions)
- If you are using Pulumi Deployments OIDC, set up your [Deployment Settings](/docs/pulumi-cloud/deployments/reference/#deployment-settings) for your stack to use your OIDC configuration.
