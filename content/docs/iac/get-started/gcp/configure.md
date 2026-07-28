---
title_tag: Configure access | Google Cloud
title: Configure access to Google Cloud
linkTitle: Configure access
h1: "Configure access to Google Cloud"
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

The Pulumi CLI needs access to your Google Cloud account to manage cloud resources. For this tutorial, you'll need a Google Cloud account with rights to deploy and manage resources such as Cloud Storage buckets.

If you've previously <a href="https://cloud.google.com/sdk/docs/install" target="_blank">installed</a> and <a href="https://cloud.google.com/sdk/docs/initializing" target="_blank">configured</a> the gcloud CLI, Pulumi will respect and use those settings, which you can test with the CLI directly:

```bash
$ gcloud config list

[core]
account = user@example.com
project = my-gcp-project

Your active configuration is: [default]
```

If your active account and project are printed, you're configured correctly. You can also verify your authentication status:

```bash
$ gcloud auth list
```

The gcloud CLI is convenient, but not required. You can also configure Pulumi with environment variables — for example, by <a href="https://cloud.google.com/iam/docs/keys-create-delete" target="_blank">creating a service account</a> and setting `GOOGLE_CREDENTIALS` to the contents of its JSON key file, or `GOOGLE_APPLICATION_CREDENTIALS` to the file's path:

{{% choosable os "linux,macos" %}}

```bash
$ export GOOGLE_CREDENTIALS="$(cat ~/path/to/service-account-key.json)"
```

```bash
$ export GOOGLE_APPLICATION_CREDENTIALS="$HOME/path/to/service-account-key.json"
```

{{% /choosable %}}
{{% choosable os windows %}}

```powershell
> $env:GOOGLE_CREDENTIALS = (Get-Content -Path "C:\path\to\service-account-key.json" -Raw)
```

```powershell
> $env:GOOGLE_APPLICATION_CREDENTIALS = "C:\path\to\service-account-key.json"
```

{{% /choosable %}}

You may also need to set your Google Cloud project explicitly:

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

For additional configuration options, see [Google Cloud Setup](/registry/packages/gcp/installation-configuration/).

{{< get-started-stepper >}}
