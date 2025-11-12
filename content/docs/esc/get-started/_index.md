---
title: Get Started
title_tag: Get Started with Pulumi ESC (Environments, Secrets, and Configuration)
h1: Get Started with Pulumi ESC
meta_desc: Get started with Pulumi ESC in 5 minutes. Create an environment, store a secret, and retrieve it programmatically.
weight: 1
menu:
  esc:
    parent: esc-home
    identifier: esc-get-started
aliases:
  - /docs/pulumi-cloud/esc/get-started/
  - /docs/esc/get-started/begin/
  - /docs/esc/get-started/create-environment/
  - /docs/pulumi-cloud/esc/get-started/begin/
  - /docs/pulumi-cloud/esc/get-started/create-environment/
---

Pulumi ESC (Environments, Secrets, and Configuration) is a centralized secrets and configuration management service. In this quick start, you'll create your first environment, store a secret, and retrieve it programmatically—all in about 5 minutes.

## Prerequisites

1. **Create a Pulumi account** at [app.pulumi.com](https://app.pulumi.com)
1. **Install the ESC CLI**

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
brew update && brew install pulumi/tap/esc
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
curl -fsSL https://get.pulumi.com/esc/install.sh | sh
```

{{% /choosable %}}

{{% choosable os windows %}}

<div class="mb-6 border-solid border-b-2 border-gray-200">
<div class="w-full">
<h3 class="no-anchor pt-4"><i class="fas fa-download pr-2"></i>Windows binary download</h3>
<p>
<a class="btn btn-secondary mx-2" href="https://get.pulumi.com/esc/releases/esc-v{{< latest-version-esc >}}-windows-x64.zip">amd64</a>
</p>
</div>
</div>

{{% /choosable %}}

{{% /chooser %}}

See the [ESC installation docs](/docs/install/esc/) for more options.

## Create your first environment

1. **Log in** to the ESC CLI:

```bash
esc login
```

You'll be prompted to log in via your browser or with an access token.

1. **Create an environment**:

```bash
esc env init my-project/dev
```

This creates a new environment named `dev` in a project called `my-project`. Environment names must be unique within a project.

1. **Verify** your environment was created:

```bash
esc env ls
```

You should see `<your-org>/my-project/dev` in the list.

## Store a secret

Add a secret to your environment using the Pulumi Cloud console:

1. Navigate to [Pulumi Cloud](https://app.pulumi.com) and log in
1. Select **Environments** in the left navigation
1. Select your `my-project/dev` environment
1. In the YAML editor, add the following:

   ```yaml
   values:
     apiKey:
       fn::secret: demo-secret-123
   ```

1. Select **Save**

The console encrypts the secret and stores it securely. The plaintext value is replaced with encrypted ciphertext in the YAML definition.

## Retrieve your secret

Open your environment to retrieve all values, including secrets:

```bash
esc env open my-project/dev
```

You should see output like:

```json
{
  "apiKey": "demo-secret-123"
}
```

That's it! You've created an environment, stored a secret, and retrieved it programmatically.

## What's next?

### Use ESC in your infrastructure code

Most Pulumi users integrate ESC with their IaC workflows to centralize secrets and configuration across all stacks. If you already use Pulumi IaC, learn how to reference ESC environments in your Pulumi programs:

**→ [Integrate ESC with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/)**

New to Pulumi IaC? Start with the [Pulumi IaC Get Started guide](/docs/get-started/) first.

### Explore other use cases

- **[Understand the concepts](/docs/esc/concepts/)** - Learn how ESC works under the hood
- **[Set up OIDC](/docs/esc/guides/setting-up-oidc/)** - Generate short-lived cloud credentials dynamically
- **[Pull secrets from external sources](/docs/esc/guides/external-secrets/)** - Integrate with AWS Secrets Manager, Azure Key Vault, and more
- **[Compose environments](/docs/esc/guides/importing-environments/)** - Share configuration across teams and projects
