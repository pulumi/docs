---
title: Stack exports
expanded_url: /docs/tour/programs/
menu:
  tour:
    parent: programs
    weight: 7
---

It can be handy to export values from your stacks.

Exporting a value simply records its final value anytime you perform a deployment.  These values are typically output
properties from resources, but they can be anything.

For instance, the following code creates a VM and exports its auto-assigned public IP address:

{{< langchoose >}}

```javascript
var aws = require("@pulumi/aws");
var server = new aws.ec2.Instance("my-vm", {
    ami: "ami-7172b611",
    instanceType: "t2.micro",
});
exports.ipAddress = server.publicIp;
```

```typescript
import * as aws from "@pulumi/aws";
let aws = require("@pulumi/aws");
let server = new aws.ec2.Instance("my-vm", {
    ami: "ami-7172b611",
    instanceType: "t2.micro",
});
export let ipAddress = server.publicIp;
```

```python
import pulumi
from pulumi_aws import ec2
server = ec2.Instance('my-vm',
    ami='ami-7172b611',
    instance_type='t2.micro')
pulumi.export('ipAddress', server.public_ip)
```

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

func main() {
    pulumi.Run(func (ctx *pulumi.Context) error {
        server, err := ec2.NewInstancectx, "my-vm", &ec2.InstanceArgs{
            Ami:          "ami-7172b611",
            InstanceType: "t2.micro",
        })
        if err != nil {
            return err
        }
        pulumi.Export("ipAddress", server.PublicIp)
        return nil
    })
}
```

After deploying this program with `pulumi up`, the exports will be printed, including any diffs.

And the `pulumi stack output` command may be used to retrieve all of them:

```bash
$ pulumi stack output
Current stack outputs (1):
    OUTPUT                  VALUE
    ipAddress               34.215.221.228
```

Or even a specific value:

```bash
$ pulumi stack output ipAddress
34.215.221.228
```

This command was designed to make scripting against the `pulumi` CLI easy, for instance if you need to plug that IP
address into another command as part of your automation, like `curl`ing or `ssh`ing into it.

***

This concludes the second lesson of the tour.  If there are topics you'd like to see added in the future, please
get in touch.  Feel free to file suggestions as issues directly in our
[pulumi/docs repo](https://github.com/pulumi/docs/issues).

If you're ready to start programming the cloud, check out the [getting started]({{< relref "/docs/quickstart" >}}) guide next!

<div class="tour-nav">
    <a class="tour-button enabled" href="{{< relref "programs-configuration.md" >}}" title="Custom configuration">◀</a>
    <span class="tour-index"><strong>8</strong>/8</span>
    <a class="tour-button disabled">▶</a>
</div>
