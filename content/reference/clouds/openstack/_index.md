---
title: OpenStack
aliases: ["/reference/openstack.html"]
menu:
  quickstart:
    identifier: openstack
    weight: 8
---

<img src="/images/quickstart/openstack-purple.png" align="right">

The OpenStack provider for Pulumi can be used to provision any of the cloud resources available in [OpenStack](https://www.openstack.org/).  The OpenStack provider must be configured with credentials to deploy and update resources in an OpenStack cloud.

See the [full API documentation]({{< relref "/reference/pkg/nodejs/pulumi/openstack" >}}) for complete details of the available OpenStack provider APIs.

## Setup

The OpenStack provider supports several options for providing access to OpenStack credentials.  See the [OpenStack setup page]({{< relref "setup.md" >}}) for details.

## Example

```javascript
const openstack = require("@pulumi/openstack")

const instance = new os.compute.Instance("test", {
	flavorName: "s1-2",
	imageName: "Ubuntu 16.04",
});
```

## Libraries

The following packages are available in packager managers:

* JavaScript/TypeScript: [`@pulumi/openstack`](https://www.npmjs.com/package/@pulumi/openstack)
* Python: [`pulumi-openstack`](https://pypi.org/project/pulumi-openstack/)
* Go: [`github.com/pulumi/pulumi-openstack/sdk/go/openstack`](https://github.com/pulumi/pulumi-openstack)

The OpenStack provider is open source and available in the [pulumi/pulumi-openstack](https://github.com/pulumi/pulumi-openstack) repo. 
