---
title: OpenStack Setup
meta_desc: This page provides an overview on how to set up the Pulumi OpenStack Provider with proper credentials.
aliases: ["/docs/reference/clouds/openstack/setup/"]
---

<!-- markdownlint-disable url -->
[Pulumi OpenStack Provider]: {{< prelref "./" >}}
[Download your OpenStack credentials]: https://docs.openstack.org/newton/user-guide/common/cli-set-environment-variables-using-openstack-rc.html
<!-- markdownlint-enable url -->

The [Pulumi OpenStack Provider] needs to be configured with OpenStack credentials
before it can be used to create resources.

You will need to provide the OpenStack Provider with your OpenStack account details. You can [Download your OpenStack credentials] as a sourceable rc file from the OpenStack dashboard.

> Your credentials are only used to authenticate with OpenStack APIs on your behalf. Your credentials are never sent to pulumi.com.

To communicate your credentials to the Pulumi OpenStack Provider, source the rc file downloaded from OpenStack.

```bash
source openrc.sh
```
