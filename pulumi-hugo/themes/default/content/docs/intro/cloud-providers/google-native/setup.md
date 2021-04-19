---
title: Google-Native Setup
meta_desc: This page provides an overview on how to setup the native Google Cloud
           (Google-Native) provider with Pulumi.
aliases: ["/docs/reference/clouds/google-native/setup/"]
---

[Google-Native Provider]: {{< relref "./" >}}

The [Google-Native Provider] needs to be configured with Google credentials
before it can be used to create resources.

{{% configure-gcp %}}

{{% notes "info" %}}
If you are using Pulumi in an non-interactive setting (such as a CI/CD system) you will need to [configure and use a service account]({{< relref "service-account" >}}) instead.
{{% /notes %}}
