---
title: Setup Service Account
meta_desc: This page provides an overview of how set up a Google Cloud Platform Service Account
           with Pulumi.
aliases: ["/docs/reference/clouds/gcp/service-account/"]
---

[Google Cloud Platform Credentials]: https://console.cloud.google.com/apis/credentials

Using a Google service account allows you to use Pulumi in a non-interactive setting (for example CI/CD systems, where a person can not complete the normal `gcloud auth application-default login` flow). A service account can also be used when developing locally to ensure a specific set of scoped credentials not tied to a user account are used. This can be useful even when developing locally to give you more control over the account role used for deployment.

To use a service account with Pulumi you will need to provide the Google Cloud Platform Provider with your Google service account private key. You can
create and download credentials using the [Google Cloud Platform Credentials] page on the Google Cloud Platform Console.

In order to create new credentials to use with Pulumi, go to the `APIs and Services` section of of the Google Cloud Platform Console
and select the `Credentials` sub-menu. From here, select the `Create credentials` drop-down menu and click `Service account key`
to create a new key for a service account.

![Create new credentials](/images/docs/gcp_configure/gcp_create_credentials.png)

On the next screen, select `JSON` as the key type and select the service account to which this key will be associated.

![Create new credentials](/images/docs/gcp_configure/gcp_create_service_account_key.png)

Pressing the `Create` button will download a JSON file. This file contains your
new credentials.

> Your credentials are only used to authenticate with Google Cloud APIs on your behalf. Your credentials are never sent to pulumi.com.

To communicate your credentials to the Pulumi Google Cloud Platform Provider,
export the contents of your credentials file to the `GOOGLE_CREDENTIALS`
environment variable:

Linux and Mac OS X

```bash
export GOOGLE_CREDENTIALS=$(cat credentials.json)
```

Windows Powershell

```bash
$env:GOOGLE_CREDENTIALS=cat credentials.json
```
