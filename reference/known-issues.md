---
layout: default 
nav_section: "reference"
---

<p><a href="/reference">Reference</a> &gt; <b>Known issues</b></p>

# Known issues

You should be aware of the following known issues and product limitations. The engineering team is actively working on fixing these issues. 

If you encounter an issue that's not on this list, please [contact us](/contact).

1. **`cloud.Service` updates are not blocking.** During a `pulumi update`, if a `cloud.Service` resource is updated from resource **A** to **B**, the update operation does not wait for the underlying ECS service for **B** to finish initializing and will proceed to the next resource update. So, if a later resource **SomeResource** depends on the new functionality in **B**, there will be an approximately 5-minute window where **SomeResource** will still be connecting to **A**. To work around this, ensure that the update to the `cloud.Service` retains backward compatibility. See [cloud.Service updates should wait for services to be stable before completing #312](https://github.com/pulumi/pulumi-cloud/issues/312).

1. **`pulumi destroy` uses current configuration, not previous** When performing a `pulumi destroy`, the current configuration (e.g. from `Pulumi.yaml`) is used, rather than the configuration at the time that the resources were created. To work around, roll back your config to the point where the resources were provisioned, then perform a `destroy` operation. See [Use old config when destroying resources #716](https://github.com/pulumi/pulumi/issues/716).

1. **Cannot directly expose port 80 in `cloud.Service`**. In a `cloud.Service`, it is not possible to specify the Internet-facing port that is exposed. For HTTP containers, the workaround is to add an `cloud.HttpEndpoint` and use the `proxy` method to proxy to the `cloud.Service` instance. See [Use container port for load balancer by default #220](https://github.com/pulumi/pulumi-cloud/issues/220).

1. **Cannot change project name in `Pulumi.yaml` when resources are provisioned**. The project name in `Pulumi.yaml` is assumed to be part of a stable identifier in identifying a stack (either a local or managed stack). Currently, renaming the project will result in all stack resources being orphaned. To work around this, run `pulumi destroy` before renaming the project. (If you have already changed the project name, simply change back to the old name and run `pulumi destroy`.) See [Changing `name` in Pulumi.yaml leads to assert #541](https://github.com/pulumi/pulumi/issues/541).