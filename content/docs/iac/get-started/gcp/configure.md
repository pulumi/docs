---
title_tag: Configure access | Google Cloud
title: Configure access
h1: "Get started with Pulumi and Google Cloud"
meta_desc: This page provides an overview on how to get started with Pulumi when starting a Google Cloud project.
weight: 3
menu:
    iac:
        name: Configure access
        parent: gcp-get-started
        weight: 3
        identifier: gcp-get-started.configure
aliases:
    - /docs/quickstart/gcp/configure/
    - /docs/get-started/gcp/configure/
    - /docs/clouds/gcp/get-started/configure/
---

## Configure access to Google Cloud

Pulumi's CLI needs access to your Google Cloud account to manage cloud resources.

If you've already <a href="https://cloud.google.com/sdk/docs/install" target="_blank">installed</a> and <a href="https://cloud.google.com/sdk/docs/initializing" target="_blank">initialized</a> the gcloud CLI, Pulumi will respect and use your configuration settings.

You must use a Google Cloud account that has rights to deploy and manage resources, such as Cloud Storage buckets.

### Testing access

To test that your Google Cloud access is configured properly, run:

{{% choosable os "linux,macos" %}}

```bash
$ gcloud config list
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> gcloud config list
```

{{% /choosable %}}

If your active account and project are printed, your configuration is correct. If not, read on:

```
[core]
account = user@example.com
disable_usage_reporting = True
project = my-gcp-project

Your active configuration is: [default]
```

You can also verify your authentication status:

{{% choosable os "linux,macos" %}}

```bash
$ gcloud auth list
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> gcloud auth list
```

{{% /choosable %}}

### Alternative approaches

If you don't have the gcloud CLI installed, or you plan on using Pulumi in a CI/CD pipeline, you can <a href="https://cloud.google.com/iam/docs/keys-create-delete" target="_blank">create a service account and download a JSON key file</a>. Then set the `GOOGLE_CREDENTIALS` environment variable on your workstation:

{{% choosable os "linux,macos" %}}

```bash
$ export GOOGLE_CREDENTIALS="$(cat ~/path/to/service-account-key.json)"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:GOOGLE_CREDENTIALS = (Get-Content -Path "C:\path\to\service-account-key.json" -Raw)
```

{{% /choosable %}}

Alternatively, you can set the path to the key file:

{{% choosable os "linux,macos" %}}

```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="$HOME/path/to/service-account-key.json"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:GOOGLE_APPLICATION_CREDENTIALS = "C:\path\to\service-account-key.json"
```

{{% /choosable %}}

{{% notes type="info" %}}
Consider using [Pulumi ESC's Google Cloud login support](/docs/esc/integrations/dynamic-login-credentials/gcp-login) for dynamic,
short-lived Google Cloud credentials via OpenID Connect (OIDC) instead of long-lived static credentials. This is a security best practice.
{{% /notes %}}

You may need to set your Google Cloud project explicitly:

{{% choosable os "linux,macos" %}}

```bash
$ export GOOGLE_PROJECT="<YOUR_PROJECT_ID>"
```

{{% /choosable %}}

{{% choosable os windows %}}

```powershell
> $env:GOOGLE_PROJECT = "<YOUR_PROJECT_ID>"
```

{{% /choosable %}}

For detailed information on Pulumi's use of Google Cloud credentials, see [Google Cloud Setup](/registry/packages/gcp/installation-configuration/).

{{< get-started-stepper >}}
