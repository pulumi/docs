---
title_tag: "hooks | Resource Options"
meta_desc: The hooks resource option provides a set of resource hooks linked to a resource.
title: "hooks"
h1: "Resource option: hooks"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: hooks
    parent: options-concepts
    weight: 7
aliases:
- /docs/intro/concepts/resources/options/hooks/
- /docs/concepts/options/hooks/
---

The `hooks` resource option provides a set of resource hooks linked to a resource. Hooks are used to execute custom logic at specific points in the resource lifecycle, such as before or after creation, update, or deletion.

Each hook is a callback that gets invoked by the Pulumi engine. Hooks that execute before an action are called **before hooks** and have names beginning with `before` or `Before` depending on the language. Hooks that execute after an action are called **after hooks** and have names beginning with `after` or `After` depending on the language. Pulumi currently supports the following hook types:

* *Create hooks* are called before or after a resource is created. This may occur during the initial creation of a resource or when a resource requires replacement due to e.g. a change in an immutable property.

* *Update hooks* are called before or after a resource is updated in-place.

* *Delete hooks* are called before or after a resource is deleted. This may occur during the deletion of a resource due to a `destroy` or that resource's removal from the program, or as part of a resource replacement due to e.g. a change in an immutable property.

When a hook is executed as part of a resource operation, it receives the resource's [URN](/docs/iac/concepts/resources/names/#urns) and ID, as well as any relevant input and output properties. Hooks may return errors. If a before hook returns an error, the action it precedes will *not* be executed and the Pulumi operation will fail with that error. If an after hook returns an error, Pulumi will log a warning diagnostic and the Pulumi operation will continue. The table below illustrates the combinations of inputs, outputs, and error behaviors for each hook type:

| Hook type     | Old inputs | New inputs | Old outputs | New outputs | Error behavior                    |
|---------------|------------|------------|-------------|-------------|-----------------------------------|
| Before create |            | ✓          |             |             | Prevent creation, fail deployment |
| After create  |            | ✓          |             | ✓           | Log warning, continue deployment  |
| Before update | ✓          | ✓          | ✓           |             | Prevent update, fail deployment   |
| After update  | ✓          | ✓          | ✓           | ✓           | Log warning, continue deployment  |
| Before delete | ✓          |            | ✓           |             | Prevent deletion, fail deployment |
| After delete  | ✓          |            | ✓           |             | Log warning, continue deployment  |

## Health checking example

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
import * as aws from "@pulumi/aws"
import * as pulumi from "@pulumi/pulumi"

export = async () => {
  // Define the instance's user data script to set up a simple HTTP server that
  // serves some static content. We'll try to fetch the health.json in a
  // lifecycle hook later on to check whether or not the server is up and running.
  const userData = `#!/bin/bash
echo "Hello, World!" > index.html
echo '{"ok": true}' > health.json
nohup python -m SimpleHTTPServer 80 &`

  // Define a resource hook that will run after create and update and not return
  // until the health check passes.
  const afterHook = new pulumi.ResourceHook("after", async args => {
    // Since this is an after hook, we'll have access to the new outputs of the
    // resource.
    const outputs = args.newOutputs

    // Attempt to fetch health.json from the instance's public endpoint, backing
    // off linearly if it is not yet available.
    const maxRetries = 30
    for (let i = 0; i < maxRetries; i++) {
      try {
        const response = await fetch(`http://${outputs.publicDns}/health.json`)
        if (response.ok) {
          const data = await response.json()
          console.log(`Health check passed: ${JSON.stringify(data)}`)
          return
        }
      } catch (error) {
        console.log(`Health check attempt ${i + 1} failed`)
      }

      await new Promise(resolve => setTimeout(resolve, (i + 1) * 1000))
    }
  })

  // Set up the resources needed to run the web server, as outlined in the
  // how-to guide linked above.

  const instanceType = "t2.micro"
  const ami = aws.ec2.getAmiOutput({
    filters: [{
      name: "name",
      values: ["amzn2-ami-hvm-*"],
    }],
    // Amazon owns this AMI so we'll use their owner ID.
    owners: ["137112412989"],
    mostRecent: true,
  })

  const group = new aws.ec2.SecurityGroup("webserver-secgrp", {
    ingress: [
      { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
      { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
  })

  const server = new aws.ec2.Instance("webserver-www", {
    instanceType,
    vpcSecurityGroupIds: [group.id],
    ami: ami.id,
    userData,
  }, {
    hooks: {
      afterCreate: [afterHook],
      afterUpdate: [afterHook],
    },
  })

  return {
    publicDns: server.publicDns,
    publicIp: server.publicIp,
  }
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws"
import * as pulumi from "@pulumi/pulumi"

export = async () => {
  // Define the instance's user data script to set up a simple HTTP server that
  // serves some static content. We'll try to fetch the health.json in a
  // lifecycle hook later on to check whether or not the server is up and running.
  const userData = `#!/bin/bash
echo "Hello, World!" > index.html
echo '{"ok": true}' > health.json
nohup python -m SimpleHTTPServer 80 &`

  // Define a resource hook that will run after create and update and not return
  // until the health check passes.
  const afterHook = new pulumi.ResourceHook("after", async args => {
    // Since this is an after hook, we'll have access to the new outputs of the
    // resource.
    const outputs = args.newOutputs as aws.ec2.InstanceState

    // Attempt to fetch health.json from the instance's public endpoint, backing
    // off linearly if it is not yet available.
    const maxRetries = 30
    for (let i = 0; i < maxRetries; i++) {
      try {
        const response = await fetch(`http://${outputs.publicDns}/health.json`)
        if (response.ok) {
          const data = await response.json()
          console.log(`Health check passed: ${JSON.stringify(data)}`)
          return
        }
      } catch (error) {
        console.log(`Health check attempt ${i + 1} failed`)
      }

      await new Promise(resolve => setTimeout(resolve, (i + 1) * 1000))
    }
  })

  // Set up the resources needed to run the web server, as outlined in the
  // how-to guide linked above.

  const instanceType = "t2.micro"
  const ami = aws.ec2.getAmiOutput({
    filters: [{
      name: "name",
      values: ["amzn2-ami-hvm-*"],
    }],
    // Amazon owns this AMI so we'll use their owner ID.
    owners: ["137112412989"],
    mostRecent: true,
  })

  const group = new aws.ec2.SecurityGroup("webserver-secgrp", {
    ingress: [
      { protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] },
      { protocol: "tcp", fromPort: 80, toPort: 80, cidrBlocks: ["0.0.0.0/0"] },
    ],
  })

  const server = new aws.ec2.Instance("webserver-www", {
    instanceType,
    vpcSecurityGroupIds: [group.id],
    ami: ami.id,
    userData,
  }, {
    hooks: {
      afterCreate: [afterHook],
      afterUpdate: [afterHook],
    },
  })

  return {
    publicDns: server.publicDns,
    publicIp: server.publicIp,
  }
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import json
import time

import pulumi
import requests
from pulumi_aws import ec2

# Define the instance's user data script to set up a simple HTTP server that
# serves some static content. We'll try to fetch the health.json in a
# lifecycle hook later on to check whether or not the server is up and running.
user_data = """#!/bin/bash
echo "Hello, World!" > index.html
echo '{"ok": true}' > health.json
nohup python -m SimpleHTTPServer 80 &"""


# Define a resource hook that will run after create and update and not return
# until the health check passes.
def health_check(args: pulumi.ResourceHookArgs):
    # Since this is an after hook, we'll have access to the new outputs of the
    # resource.
    outputs = args.new_outputs

    # Attempt to fetch health.json from the instance's public endpoint, backing
    # off linearly if it is not yet available.
    max_retries = 30
    for i in range(max_retries):
        try:
            response = requests.get(
                f"http://{outputs['publicDns']}/health.json", timeout=10
            )
            if response.status_code == 200:
                data = response.json()
                print(f"Health check passed: {json.dumps(data)}")
                return
        except Exception as error:
            print(f"Health check attempt {i + 1} failed: {error}")

        # Linear backoff - wait (i + 1) seconds before next attempt
        time.sleep(i + 1)


instance_type = "t2.micro"

ami = ec2.get_ami_output(
    filters=[
        {
            "name": "name",
            "values": ["amzn2-ami-hvm-*"],
        }
    ],
    # Amazon owns this AMI so we'll use their owner ID.
    owners=["137112412989"],
    most_recent=True,
)

group = ec2.SecurityGroup(
    "webserver-secgrp",
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 22,
            "to_port": 22,
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
)

server = ec2.Instance(
    "webserver-www",
    instance_type=instance_type,
    vpc_security_group_ids=[group.id],
    ami=ami.id,
    user_data=user_data,
    opts=pulumi.ResourceOptions(
        hooks=pulumi.ResourceHookBinding(
            after_create=[health_check],
            after_update=[health_check],
        ),
    ),
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Define a resource hook that will run after create and update and not return
// until the health check passes.
func healthCheck(args *pulumi.ResourceHookArgs) error {
	// Since this is an after hook, we'll have access to the new outputs of the
	// resource.
	publicDns := args.NewOutputs["publicDns"].StringValue()

	// Attempt to fetch health.json from the instance's public endpoint, backing
	// off linearly if it is not yet available.
	maxRetries := 30
	for i := 0; i < maxRetries; i++ {
		url := fmt.Sprintf("http://%s/health.json", publicDns)

		client := &http.Client{
			Timeout: 10 * time.Second,
		}

		resp, err := client.Get(url)
		if err == nil && resp.StatusCode == 200 {
			var data map[string]interface{}
			if err := json.NewDecoder(resp.Body).Decode(&data); err == nil {
				resp.Body.Close()
				dataJSON, _ := json.Marshal(data)
				fmt.Printf("Health check passed: %s\n", string(dataJSON))
				return nil
			}
			resp.Body.Close()
		}

		if resp != nil {
			resp.Body.Close()
		}

		fmt.Printf("Health check attempt %d failed: %v\n", i+1, err)

		// Linear backoff - wait (i + 1) seconds before next attempt
		time.Sleep(time.Duration(i+1) * time.Second)
	}

	return fmt.Errorf("health check failed after %d attempts", maxRetries)
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Define the instance's user data script to set up a simple HTTP server
		// that serves some static content. We'll try to fetch the health.json
		// in a lifecycle hook later on to check whether or not the server is up
		// and running.
		userData := `#!/bin/bash
echo "Hello, World!" > index.html
echo '{"ok": true}' > health.json
nohup python -m SimpleHTTPServer 80 &`

		instanceType := "t2.micro"

		ami, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
			Filters: []ec2.GetAmiFilter{
				{
					Name:   "name",
					Values: []string{"amzn2-ami-hvm-*"},
				},
			},
			// Amazon owns this AMI so we'll use their owner ID.
			Owners:     []string{"137112412989"},
			MostRecent: pulumi.BoolRef(true),
		})
		if err != nil {
			return err
		}

		group, err := ec2.NewSecurityGroup(ctx, "webserver-secgrp", &ec2.SecurityGroupArgs{
			Ingress: ec2.SecurityGroupIngressArray{
				&ec2.SecurityGroupIngressArgs{
					Protocol:   pulumi.String("tcp"),
					FromPort:   pulumi.Int(22),
					ToPort:     pulumi.Int(22),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
				&ec2.SecurityGroupIngressArgs{
					Protocol:   pulumi.String("tcp"),
					FromPort:   pulumi.Int(80),
					ToPort:     pulumi.Int(80),
					CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
				},
			},
		})
		if err != nil {
			return err
		}

		hook, err := ctx.RegisterResourceHook("health-check", healthCheck, nil)
		if err != nil {
			return err
		}

		server, err := ec2.NewInstance(ctx, "webserver-www", &ec2.InstanceArgs{
			InstanceType:        pulumi.String(instanceType),
			VpcSecurityGroupIds: pulumi.StringArray{group.ID()},
			Ami:                 pulumi.String(ami.Id),
			UserData:            pulumi.String(userData),
		}, pulumi.ResourceHooks(&pulumi.ResourceHookBinding{
			AfterCreate: []*pulumi.ResourceHook{hook},
			AfterUpdate: []*pulumi.ResourceHook{hook},
		}))
		if err != nil {
			return err
		}

		ctx.Export("publicDns", server.PublicDns)
		ctx.Export("publicIp", server.PublicIp)

		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System;

using System.Threading.Tasks;
using Pulumi;

using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;
using Pulumi.Command.Local;
using System.Diagnostics;
using System.Collections.Generic;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        // Define the instance's user data script to set up a simple HTTP server that
        // serves some static content. We'll try to fetch the health.json in a
        // lifecycle hook later on to check whether or not the server is up and running.
        var userData = @"#!/bin/bash
echo ""Hello, World!"" > index.html
echo '{""ok"": true}' > health.json
nohup python -m SimpleHTTPServer 80 &";

        // Define a resource hook that will run after create and update and not return
        // until the health check passes.
        var afterHook = new ResourceHook("after", async (args, cancellationToken) =>
        {
            // Since this is an after hook, we'll have access to the new outputs of the
            // resource.
            var outputs = args.NewOutputs

            // Attempt to fetch health.json from the instance's public endpoint, backing
            // off linearly if it is not yet available.
            const int maxRetries = 30;
            for (var i = 0; i < maxRetries; i++)
            {
                try
                {
                    using var client = new HttpClient();
                    var response = await client.GetAsync($"http://{outputs?["publicDns"]}/health.json");
                    if (response.IsSuccessStatusCode)
                    {
                        var data = await response.Content.ReadAsStringAsync();
                        Console.WriteLine($"Health check passed: {data}");
                        return;
                    }
                }
                catch (Exception)
                {
                    Console.WriteLine($"Health check attempt {i + 1} failed");
                }

                await Task.Delay((i + 1) * 1000);
            }
        });

        // Set up the resources needed to run the web server, as outlined in the
        // how-to guide linked above.

        var instanceType = "t2.micro";
        var ami = GetAmi.Invoke(new GetAmiArgs
        {
            Filters =
            {
                new GetAmiFilterArgs
                {
                    Name = "name",
                    Values = { "amzn2-ami-hvm-*" },
                },
            },
            Owners = { "137112412989" }, // Amazon owns this AMI so we'll use their owner ID.
            MostRecent = true,
        });

        var group = new SecurityGroup("webserver-secgrp", new SecurityGroupArgs
        {
            Ingress =
            {
                new SecurityGroupIngressArgs
                {
                    Protocol = "tcp",
                    FromPort = 22,
                    ToPort = 22,
                    CidrBlocks = { "0.0.0.0/0" },
                },
                new SecurityGroupIngressArgs
                {
                    Protocol = "tcp",
                    FromPort = 80,
                    ToPort = 80,
                    CidrBlocks = { "0.0.0.0/0" },
                },
            },
        });

        var server = new Instance("webserver-www", new InstanceArgs
        {
            InstanceType = instanceType,
            VpcSecurityGroupIds = { group.Id },
            Ami = ami.Apply(a => a.Id),
            UserData = userData,
        }, new CustomResourceOptions
        {
            Hooks =
            {
                AfterCreate = { afterHook },
                AfterUpdate = { afterHook },
            }
        });

        // Export the public DNS and IP of the server.
        this.PublicDns = server.PublicDns;
        this.PublicIp = server.PublicIp;
    }

    [Output]
    public Output<string> PublicDns { get; private set; }

    [Output]
    public Output<string> PublicIp { get; private set; }
}
```

{{% /choosable %}}
{{% choosable language java %}}

```java
// Pulumi Java support for hooks is coming soon
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
# Pulumi YAML does not support resource hooks
```

{{% /choosable %}}

{{< /chooser >}}

## Deletions and delete hooks

In order for delete hooks to run successfully, Pulumi must have access to any necessary hooks at the time of the deletion. You should take the following actions to ensure that delete hooks run as expected:

* When removing resources from your program, first remove *only* the resources you wish to delete, *leaving any delete hooks in place*. Upon running e.g. `pulumi up`, Pulumi will delete the resources and run any relevant delete hooks. Once this operation is complete, you can then remove the delete hooks from your program.

* When running `pulumi destroy`, you must pass the `--run-program` flag to instruct Pulumi to run your program and register any hooks that are to be executed. If Pulumi detects that you are trying to `destroy` a stack that contains hooks _without_ the `--run-program` flag, it will fail with an error.
