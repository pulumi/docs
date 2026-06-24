---
title_tag: Pulumi Deployments Cloud Credentials
meta_desc: This page explains the options for supplying cloud credentials to a Pulumi Deployment
title: Supplying Cloud Credentials to Pulumi Deployments
h1: Supplying Cloud Credentials to Pulumi Deployments
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/pulumi-cloud/deployments/cloud-credentials/
- /docs/deployments/deployments/cloud-credentials/
menu:
  deployments:
    name: Cloud Credentials
    parent: deployments-guides
    weight: 10
    identifier: deployments-guides-cloud-credentials
---

In order for a Pulumi IaC operation like `update` or `preview` work, the Pulumi CLI must be able to access credentials that will allow it to perform the necessary CRUD operations on the resources in your stack. In order for Pulumi Deployments to access the necessary cloud credentials to run your Pulumi operation there are two common approaches you can take:

1. **Use [Pulumi ESC](/docs/esc/)** (recommended) to define an Environment (or Environments), and [import the environment(s) into your stack](/docs/esc/guides/integrate-with-pulumi-iac/).
2. **Use [Pulumi Deployments' OIDC integration](/docs/deployments/guides/oidc/)** where possible (we support [AWS](/docs/deployments/guides/oidc/aws/), [Azure](/docs/deployments/guides/oidc/azure/), and [Google Cloud](/docs/deployments/guides/oidc/gcp/)), and store any remaining required secrets or configuration in [Pulumi Deployments Environment Variables](/docs/deployments/concepts/settings/).

Pulumi recommends Pulumi ESC for most users. See [Choosing between Pulumi ESC Environments and Pulumi Deployments OIDC](#choosing-between-pulumi-esc-environments-and-pulumi-deployments-oidc) below for details.

## Choosing between Pulumi ESC Environments and Pulumi Deployments OIDC

Deployments OIDC predates Pulumi ESC and was originally the only way to use OIDC with Deployments, which is why it remains a common default. It's still a good fit for some scenarios — for example, [customer-managed agents](/docs/deployments/concepts/customer-managed-runners/) that can't reach Pulumi Cloud over the network to use ESC. For most users, though, Pulumi recommends using ESC Environments over Deployments OIDC for the following reasons:

- Pulumi ESC Environments are more portable compared to Deployments OIDC: Ignoring any locally stored credentials, e.g., environment variables set in your command shell, you can have greater confidence that a Pulumi Deployments operation will succeed if it succeeds on your local machine.
- Pulumi ESC Environments are more modular compared to Deployments OIDC: Deployments settings are applied on a per-stack basis, which means that the OIDC configuration must be repeated for every stack that is using Deployments OIDC. In comparison, Pulumi ESC Environments are centrally defined and may be imported into any number of Pulumi stacks.
- Pulumi ESC has [more native integrations](/docs/esc/integrations/) with popular clouds for both [OIDC](/docs/esc/providers/login/) and [managed secrets services](/docs/esc/providers/secrets/), and other tools like [Kubernetes](/docs/esc/guides/integrate-with/kubernetes-cluster-access/), [Docker](/docs/esc/guides/integrate-with/docker/), etc.
- Pulumi ESC Environments are composable: [Environments can import other Environments](/docs/esc/concepts/imports/), which removes the need to repeat configuration information.
- Pulumi ESC Environments support [versioning](/docs/esc/concepts/versioning/), allowing you to roll out changes to an environment in a controlled fashion by pinning Environment imports to a specific version of an Environment.

{{% notes type="info" %}}
One important difference to be mindful of is that Pulumi Deployments OIDC is available to [pre-run commands](/docs/deployments/concepts/settings/#pre-run-commands), whereas a Pulumi ESC environment is not: an ESC environment applies only to the Pulumi IaC operation (e.g. `pulumi up`), not to the rest of the Deployments process. To use ESC-supplied credentials in a pre-run command, prefix the command with [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run/) so it executes in the context of the specified Pulumi ESC Environment.

For example, to install packages from a private repository, you might run the following pre-run command:

```bash
pulumi env run my-esc-project/my-esc-environment -- npm install
```

{{% /notes %}}

## Next Steps

Both Pulumi Deployments OIDC and Pulumi ESC require configuring an OIDC Identity Provider in your cloud environment in order to enable the secure exchange of tokens between Pulumi Cloud and your cloud provider in order to obtain temporary credentials. For more information:

- If using Pulumi ESC, see [Configuring OpenID Connect for Pulumi ESC](/docs/esc/guides/configuring-oidc/).
- If using Pulumi Deployments OIDC, see [OIDC Setup for Pulumi Deployments](/docs/deployments/guides/oidc/).

After an OIDC Identity Provider has been configured:

- If you are using Pulumi ESC, ensure that your Pulumi Deployments token has permissions to open any imported Pulumi ESC Environments. For more information, see [Deployment Permissions](/docs/deployments/operations/permissions/)
- If you are using Pulumi Deployments OIDC, set up your [Deployment Settings](/docs/deployments/concepts/settings/) for your stack to use your OIDC configuration.
