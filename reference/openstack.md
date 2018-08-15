---
title: "OpenStack"
---

The OpenStack provider for Pulumi can be used to provision any of the cloud resources available in [OpenStack](https://www.openstack.org/).  The OpenStack provider must be configured with credentials to deploy and update resources in an OpenStack cloud.

See the [full API documentation](./pkg/nodejs/@pulumi/openstack/index.html) for complete details of the available OpenStack provider APIs.

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
* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/openstack
* Python: https://pypi.org/project/pulumi-openstack/
* Go: `github.com/pulumi/pulumi-openstack/sdk/go/openstack`

The OpenStack provider is open source and available in the [pulumi/pulumi-openstack](https://github.com/pulumi/pulumi-openstack) repo. 

## Authentication

The OpenStack provider supports several options for providing access to OpenStack credentials.  See [OpenStack installation page](/install/openstack.html) for details.
