---
title: Setup
redirect_from: /install/gcp.html
---

[Pulumi Google Cloud Platform Provider]: ./index.html
[Google Cloud Platform Credentials]: https://console.cloud.google.com/apis/credentials

The [Pulumi Google Cloud Platform Provider] needs to be configured with Google credentials
before it can be used to create resources.

You will need to provide the Google Cloud Platform Provider with your Google service account private key. You can
create and download credentials using the [Google Cloud Platform Credentials] page on the Google Cloud Platform Console.

In order to create new credentials to use with Pulumi, go to the `APIs and Services` section of of the Google Cloud Platform Console
and select the `Credentials` sub-menu. From here, select the `Create credentials` drop-down menu and click `Service account key`
to create a new key for a service account.

![Create new credentials](/images/gcp_configure/gcp_create_credentials.png)

On the next screen, select `JSON` as the key type and select the service account to which this key will be associated.

![Create new credentials](/images/gcp_configure/gcp_create_service_account_key.png)

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

## Optional Settings

The Pulumi Google Cloud Platform Provider accepts these environment variables
to further configure the provider:

* `GOOGLE_PROJECT` - The default project for new resources, if one is not specified
when creating a resource
* `GOOGLE_REGION` - The default region for new resources, if one is not specified
when creating a resource
* `GOOGLE_ZONE` - The default zone for new resources, if one is not specified when
creating a resource.

If these values are not provided, some resources may require you to provide these
values as `project`, `region`, or `zone` properties.
