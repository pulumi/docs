---
title_tag: Install and Configure | Pulumi for Terraform Users
title: Install and Configure
h1: "Get started with Pulumi for Terraform Users"
stepper_link: "I'm ready to begin"
meta_desc: This page provides setup instructions for Pulumi alongside existing Terraform infrastructure.
weight: 2
menu:
    iac:
        name: Install and Configure
        parent: terraform-get-started
        weight: 2

aliases:
- /docs/iac/get-started/terraform/begin/
---

## Install Pulumi

Download and install Pulumi alongside your existing Terraform setup:

{{< install-pulumi >}}
{{% notes info %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

## Configure access to AWS

Pulumi can use the same cloud provider credentials as Terraform. In this tutorial we're going to focus on AWS.
If you're already using Terraform with AWS, or if you've <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html" target="_blank">installed</a> and <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html" target="_blank">configured</a> the AWS CLI, your existing configuration will work with Pulumi.

You must use an IAM user account that has [programmatic access](https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds-programmatic-access.html) with rights to deploy and manage S3 buckets.

### Testing access

To test that your AWS access is configured properly, run:

{{% choosable os "linux,macos" %}}

```bash
$ aws sts get-caller-identity
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> aws sts get-caller-identity
```

{{% /choosable %}}

If your AWS user ID, account, and ARN are printed, you are good to go. If not, read on:

```
{
    "UserId": "BXO3165...ZP36NYY5FOU:my-session",
    "Account": "9263...9123",
    "Arn": "arn:aws:sts::9263...9123:assumed-role/.../my-session"
}
```

### Alternative approaches

If you don't have the AWS CLI installed, or you plan on using Pulumi in a CI/CD pipeline, <a href="https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys" target="_blank">retrieve your access key ID and secret access key</a> and then set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables on your workstation:

{{% choosable os "linux,macos" %}}

```bash
$ export AWS_ACCESS_KEY_ID="<YOUR_ACCESS_KEY_ID>"
$ export AWS_SECRET_ACCESS_KEY="<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_ACCESS_KEY_ID = "<YOUR_ACCESS_KEY_ID>"
> $env:AWS_SECRET_ACCESS_KEY = "<YOUR_SECRET_ACCESS_KEY>"
```

{{% /choosable %}}

{{% notes type="info" %}}
Consider using [Pulumi ESC's AWS login support](/docs/esc/integrations/dynamic-login-credentials/aws-login) for dynamic,
short-lived AWS credentials via OpenID Connect (OIDC) instead of long-lived static credentials. This is a security best practice.
{{% /notes %}}

You may optionally use AWS profiles if your configuration requires them:

{{% choosable os "linux,macos" %}}

```bash
$ export AWS_PROFILE="<YOUR_PROFILE_NAME>"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:AWS_PROFILE = "<YOUR_PROFILE_NAME>"
```

{{% /choosable %}}

For detailed information on Pulumi's use of AWS credentials, see [AWS Setup](/registry/packages/aws/installation-configuration/).

## Choose your language

Next, make sure you have the necessary runtimes installed for your preferred Pulumi language:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> and <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* <a href="https://www.python.org/downloads/" target="_blank">Python</a> and <a href="https://pip.pypa.io/en/stable/installation/">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> or <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* <a href="https://go.dev/doc/install" target="_blank">Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> and <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* No additional language runtime required

{{% /choosable %}}

## Verify CLI installation

After installing Pulumi, verify everything is in working order by running the `pulumi` CLI:

{{% chooser os "macos,windows,linux" %}}

{{% choosable os macos %}}

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-macos-version">$ pulumi version</code></pre>
</div>

{{% /choosable %}}

{{% choosable os linux %}}

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-linux-version">$ pulumi version</code></pre>
</div>

{{% /choosable %}}

{{% choosable os windows %}}

<div class="highlight">
   <pre class="chroma"><code class="language-bash" data-lang="bash" data-track="install-pulumi-windows-version">&gt; pulumi version</code></pre>
</div>

{{% /choosable %}}

{{% /chooser %}}

If you run into trouble, please refer to the [Download and install Pulumi](/docs/iac/download-install/) page to troubleshoot your setup before moving on.

{{< get-started-stepper >}}
