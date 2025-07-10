---
title: "Resource hooks"
date: 2025-06-30
meta_desc: "Pulumi now allows you to run custom code at any point in the resource lifecycle"
meta_image: meta.png
authors:
    - will-jones
    - julien-poissonnier
tags:
    - features
    - releases
    - iac
---

Pulumi programs are _declarative_, allowing you to specify the desired state of your infrastructure while Pulumi figures out the rest. But what about the times where you want to be more involved in what Pulumi is doing? **Resource hooks** are [one of our most requested features](https://github.com/pulumi/pulumi/issues/1691), and from Pulumi 3.179.0 we're excited to announce that you'll be able to use them to run arbitrary code at any point in Pulumi's resource lifecycle!

<!--more-->

When you run `pulumi up`, Pulumi runs your program and works out the set of create, update and delete operations required to realise the state it describes. Hooks allow you to attach custom callbacks to these operations, enabling you to execute custom behaviour before or after they occur. You might want to set up an SSH tunnel to a bastion host before Pulumi attempts to create or update a virtual machine or database; or you may wish to send metrics to your data warehouse whenever Pulumi updates certain resources or properties. Hooks allow you to do all this and more -- as with everything else in Pulumi, you are free to make use of the full power of your favourite programming language.

## Hooks in action

Let's check out the use case of opening a tunnel to a remote host before running a command. For this we'll use a contrived example where we use the [`socat`](http://www.dest-unreach.org/socat/) command to open a local TCP port that forwards to a remote host. Here we'll open `localhost:1234` and forward it to [`example.com:80`](https://example.com). We'll then use Pulumi's [`command` provider](https://www.pulumi.com/registry/packages/command/) to invoke `curl` to make a request to that local port, which will be forwarded to the remote host. To start with, let's write the program without hooks:

{{% chooser language "javascript,typescript,python,go,csharp" %}}

{{% choosable language javascript %}}

```javascript
import * as command from "@pulumi/command"

export = async () => {
  const curl = "curl -H'Host: example.com' localhost:1234"

  const cmd = new command.local.Command("curl", {
    create: curl,
    update: curl,
    delete: curl,
    triggers: [new Date().toString()],
  })

  return {
    stdout: cmd.stdout,
  }
}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as command from "@pulumi/command"

export = async () => {
  const curl = "curl -H'Host: example.com' localhost:1234"

  const cmd = new command.local.Command("curl", {
    create: curl,
    update: curl,
    delete: curl,
    triggers: [new Date().toString()],
  })

  return {
    stdout: cmd.stdout,
  }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import datetime
import pulumi
import pulumi_command

curl = "curl -H'Host: example.com' localhost:1234"

cmd = pulumi_command.local.Command("curl",
    create=curl,
    update=curl,
    delete=curl,
    triggers=[str(datetime.datetime.now())],
)

pulumi.export("stdout", cmd.stdout)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"time"

	"github.com/pulumi/pulumi-command/sdk/go/command/local"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		curl := "curl -H'Host: example.com' localhost:1234"

		cmd, err := local.NewCommand(ctx, "curl", &local.CommandArgs{
			Create:   pulumi.String(curl),
			Update:   pulumi.String(curl),
			Delete:   pulumi.String(curl),
			Triggers: pulumi.StringArray{pulumi.String(time.Now().String())},
		})
		if err != nil {
			return err
		}

		ctx.Export("stdout", cmd.Stdout)

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Command.Local;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        var curl = "curl -H'Host: example.com' localhost:1234";

        var cmd = new Command("curl", new CommandArgs
        {
            Create = curl,
            Update = curl,
            Delete = curl,
            Triggers = { System.DateTime.Now.ToString() },
        });

        return new Dictionary<string, object?>
        {
            ["stdout"] = cmd.Stdout,
        };
    }
}
```

{{% /choosable %}}

{{% /chooser %}}

We set up a local `Command` that will run the same `curl` command whether it is being created, updated, or deleted. For the purposes of illustration, we also set the `triggers` property to the current date and time, so that the command will always be run when we run `pulumi up`. Let's now do just that:

```shell
pulumi up
```

Assuming we have nothing running on port `1234`, we'll get an error such as the following:

```
Updating (...)

View in Browser (Ctrl+O): https://app.pulumi.com/...

     Type                      Name               Status                  Info
     pulumi:pulumi:Stack       resource-hooks     **failed**              1 error; 9 messages
 ++  └─ command:local:Command  curl               **creating failed**     [diff: ]; 1 error

Diagnostics:
  command:local:Command (curl):
    error: exit status 7: running "curl -H'Host: example.com' localhost:1234":
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
    curl: (7) Failed to connect to localhost port 1234 after 0 ms: Could not connect to server
```

As expected, nothing is listening on port `1234`, so `curl` fails with an error. Previously, we might have fixed this by using a wrapped around our Pulumi program, such as the [Automation API](https://www.pulumi.com/automation/). With resource hooks, however, the solution is at our fingertips! We'll hook into the `Command` resource's lifecycle to open a tunnel before any operation is run, and to close it afterwards:

{{% chooser language "javascript,typescript,python,go,csharp" %}}

{{% choosable language javascript %}}

```javascript
import * as child_process from "child_process"
import * as command from "@pulumi/command"
import * as pulumi from "@pulumi/pulumi"

export = async () => {
  let tunnel

  const beforeHook = new pulumi.ResourceHook("before", async args => {
    console.log("Opening tunnel")

    tunnel = child_process.spawn(
      "socat",
      [
        "TCP-LISTEN:1234,fork",
        "TCP:example.com:80",
      ],
      { detached: true }
    )

    console.log(`Tunnel opened: ${tunnel?.pid}`)
  })

  const afterHook = new pulumi.ResourceHook("after", async args => {
    console.log(`Closing tunnel: ${tunnel?.pid}`)
    tunnel?.kill("SIGKILL")
  })

  const curl = "curl -H'Host: example.com' localhost:1234"

  const cmd = new command.local.Command("curl", {
    create: curl,
    update: curl,
    delete: curl,
    triggers: [new Date().toString()],
  }, {
    hooks: {
      beforeCreate: [beforeHook],
      afterCreate: [afterHook],
      beforeUpdate: [beforeHook],
      afterUpdate: [afterHook],
      beforeDelete: [beforeHook],
      afterDelete: [afterHook],
    },
  })

  return {
    stdout: cmd.stdout,
  }
}
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as child_process from "child_process"
import * as command from "@pulumi/command"
import * as pulumi from "@pulumi/pulumi"

export = async () => {
  let tunnel: child_process.ChildProcessWithoutNullStreams | undefined

  const beforeHook = new pulumi.ResourceHook("before", async args => {
    console.log("Opening tunnel")

    tunnel = child_process.spawn(
      "socat",
      [
        "TCP-LISTEN:1234,fork",
        "TCP:example.com:80",
      ],
      { detached: true }
    )

    console.log(`Tunnel opened: ${tunnel?.pid}`)
  })

  const afterHook = new pulumi.ResourceHook("after", async args => {
    console.log(`Closing tunnel: ${tunnel?.pid}`)
    tunnel?.kill("SIGKILL")
  })

  const curl = "curl -H'Host: example.com' localhost:1234"

  const cmd = new command.local.Command("curl", {
    create: curl,
    update: curl,
    delete: curl,
    triggers: [new Date().toString()],
  }, {
    hooks: {
      beforeCreate: [beforeHook],
      afterCreate: [afterHook],
      beforeUpdate: [beforeHook],
      afterUpdate: [afterHook],
      beforeDelete: [beforeHook],
      afterDelete: [afterHook],
    },
  })

  return {
    stdout: cmd.stdout,
  }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import datetime
import subprocess
import pulumi
import pulumi_command

tunnel = None

def before(args: pulumi.ResourceHookArgs):
    global tunnel
    pulumi.log.info("Opening tunnel")
    tunnel = subprocess.Popen(
        ["socat", "TCP-LISTEN:1234,fork", "TCP:example.com:80"],
    )
    pulumi.log.info(f"Tunnel opened: {tunnel.pid}")


before_hook = pulumi.ResourceHook("before", before)

def after(args: pulumi.ResourceHookArgs):
    global tunnel
    if tunnel:
        pulumi.log.info(f"Closing tunnel: {tunnel.pid}")
        tunnel.terminate()
        tunnel.wait()
        tunnel = None

after_hook = pulumi.ResourceHook("after", after)

curl = "curl -H'Host: example.com' localhost:1234"

cmd = pulumi_command.local.Command(
    "curl",
    create=curl,
    update=curl,
    delete=curl,
    triggers=[str(datetime.datetime.now())],
    opts=pulumi.ResourceOptions(
        hooks=pulumi.ResourceHookBinding(
            before_create=[before_hook],
            after_create=[after_hook],
            before_update=[before_hook],
            after_update=[after_hook],
            before_delete=[before_hook],
            after_delete=[after_hook],
        )
    ),
)

pulumi.export("stdout", cmd.stdout)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"fmt"
	"os/exec"
	"time"

	"github.com/pulumi/pulumi-command/sdk/go/command/local"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var tunnel *exec.Cmd

func before(args *pulumi.ResourceHookArgs) error {
	fmt.Println("Opening tunnel")
	tunnel = exec.Command("socat", "TCP-LISTEN:1234,fork", "TCP:example.com:80")
	err := tunnel.Start()
	if err != nil {
		return fmt.Errorf("failed to start tunnel: %w", err)
	}
	fmt.Printf("Tunnel opened: %d\n", tunnel.Process.Pid)
	return nil
}

func after(args *pulumi.ResourceHookArgs) error {
	if tunnel != nil && tunnel.Process != nil {
		fmt.Printf("Closing tunnel: %d", tunnel.Process.Pid)
		if err := tunnel.Process.Kill(); err != nil {
			return err
		}
		tunnel.Wait()
		tunnel = nil
	}
	return nil
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		beforeHook, err := ctx.RegisterResourceHook("before", before, nil)
		if err != nil {
			return err
		}
		afterHook, err := ctx.RegisterResourceHook("after", after, nil)
		if err != nil {
			return err
		}

		curlCmd := "curl -H'Host: example.com' localhost:1234"

		cmd, err := local.NewCommand(ctx, "curl", &local.CommandArgs{
			Create:   pulumi.String(curlCmd),
			Update:   pulumi.String(curlCmd),
			Delete:   pulumi.String(curlCmd),
			Triggers: pulumi.Array{pulumi.String(fmt.Sprintf("%d", time.Now().Unix()))},
		}, pulumi.ResourceHooks(&pulumi.ResourceHookBinding{
			BeforeCreate: []*pulumi.ResourceHook{beforeHook},
			AfterCreate:  []*pulumi.ResourceHook{afterHook},
			BeforeUpdate: []*pulumi.ResourceHook{beforeHook},
			AfterUpdate:  []*pulumi.ResourceHook{afterHook},
			BeforeDelete: []*pulumi.ResourceHook{beforeHook},
			AfterDelete:  []*pulumi.ResourceHook{afterHook},
		}),
		)
		if err != nil {
			return err
		}

		ctx.Export("stdout", cmd.Stdout)

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Diagnostics;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Command.Local;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        Process? tunnel = null;

        var beforeHook = new ResourceHook("before", async (args, cancellationToken) =>
        {
            System.Console.WriteLine("Opening tunnel");

            tunnel = Process.Start(new ProcessStartInfo
            {
                FileName = "socat",
                Arguments = "TCP-LISTEN:1234,fork TCP:example.com:80",
                UseShellExecute = false,
                CreateNoWindow = true,
            });

            System.Console.WriteLine($"Tunnel opened: {tunnel?.Id}");
        });

        var afterHook = new ResourceHook("after", async (args, cancellationToken) =>
        {
            System.Console.WriteLine($"Closing tunnel: {tunnel?.Id}");
            tunnel?.Kill();
        });

        var curl = "curl -H'Host: example.com' localhost:1234";

        var cmd = new Command("curl", new CommandArgs
        {
            Create = curl,
            Update = curl,
            Delete = curl,
            Triggers = { System.DateTime.Now.ToString() },
        }, new CustomResourceOptions
        {
            Hooks =
            {
                BeforeCreate = { beforeHook },
                AfterCreate = { afterHook },
                BeforeUpdate = { beforeHook },
                AfterUpdate = { afterHook },
                BeforeDelete = { beforeHook },
                AfterDelete = { afterHook },
            }
        });

        return new Dictionary<string, object?>
        {
            ["stdout"] = cmd.Stdout,
        };
    }
}
```

{{% /choosable %}}

{{% /chooser %}}

When we run `pulumi up` now, the hooks will be invoked before and after the relevant operation. Since our previous operation failed, we should expect to see a hooked create on our first run:

```shell
pulumi up
```

```
Updating (...)

View in Browser (Ctrl+O): https://app.pulumi.com/...

     Type                      Name               Status              Info
 +   pulumi:pulumi:Stack       resource-hooks     created (3s)        3 messages
 +   └─ command:local:Command  curl               created (0.66s)

Diagnostics:
  pulumi:pulumi:Stack (resource-hooks):
    Opening tunnel
    Tunnel opened: 2131167
    Closing tunnel: 2131167

Outputs:
    stdout: "<!doctype html>\n<html>\n<head>\n    <title>Example Domain</title>\n\n    <meta charset=\"utf-8\" />\n    <meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\" />\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />\n    <style type=\"text/css\">\n    body {\n        background-color: #f0f0f2;\n        margin: 0;\n        padding: 0;\n        font-family: -apple-system, system-ui, BlinkMacSystemFont, \"Segoe UI\", \"Open Sans\", \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n        \n    }\n    div {\n        width: 600px;\n        margin: 5em auto;\n        padding: 2em;\n        background-color: #fdfdff;\n        border-radius: 0.5em;\n        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);\n    }\n    a:link, a:visited {\n        color: #38488f;\n        text-decoration: none;\n    }\n    @media (max-width: 700px) {\n        div {\n            margin: 0 auto;\n            width: auto;\n        }\n    }\n    </style>    \n</head>\n\n<body>\n<div>\n    <h1>Example Domain</h1>\n    <p>This domain is for use in illustrative examples in documents. You may use this\n    domain in literature without prior coordination or asking for permission.</p>\n    <p><a href=\"https://www.iana.org/domains/example\">More information...</a></p>\n</div>\n</body>\n</html>"

Resources:
    + 2 created

Duration: 5s
```

Success! The tunnel was opened before our create operation and our stack output contains the HTML of the page at `example.com`.

## Another example: application health checks

Let's tackle a more realistic scenario where hooks can be useful. We'll take the [how-to guide for creating an EC2 web server](https://www.pulumi.com/registry/packages/aws/how-to-guides/ec2-webserver/) and add resource hooks to health check the web server before allowing Pulumi to mark the deployment as complete. In this way, we know that when Pulumi is finished, the application is up and ready to go!

{{% chooser language "javascript,typescript,python,go,csharp" %}}

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

{{% /chooser %}}

Thanks to our hooks, `pulumi up` will now wait until the web server is up and running before marking the deployment as complete. We can see this in action thanks to our logging output:

```shell
pulumi up
```

```shell
Updating (...)

View in Browser (Ctrl+O): https://app.pulumi.com/...

     Type                      Name               Status            Info
 +   pulumi:pulumi:Stack       resource-hooks     created (79s)     6 messages
 +   ├─ aws:ec2:SecurityGroup  webserver-secgrp   created (3s)
 +   └─ aws:ec2:Instance       webserver-www      created (67s)

Diagnostics:
  pulumi:pulumi:Stack (resource-hooks):
    Health check attempt 1 failed
    Health check attempt 2 failed
    Health check attempt 3 failed
    Health check attempt 4 failed
    Health check attempt 5 failed
    Health check passed: {"ok":true}

Outputs:
    publicHostName: "ec2-XXX-YYY-ZZZ-WWW.us-west-2.compute.amazonaws.com"
    publicIp      : "XXX.YYY.ZZZ.WWW"

Resources:
    + 3 created

Duration: 1m21s
```

And indeed, a command such as `curl http://ec2-XXX-YYY-ZZZ-WWW.us-west-2.compute.amazonaws.com/health.json` returns `{"ok":true}` immediately, without us having to wait for the web server to start up after the `pulumi up` command completes!

## Where can we go from here?

Resource hooks are a powerful new feature that allow you to run custom code at any point in the resource lifecycle. This opens up a wide range of possibilities, such as:

* Custom application health checks after creating or updating resources
* Collecting logs or metrics when your Pulumi resources change
* Running custom scripts such as database migrations as part of your Pulumi workflow.

{{% notes %}}
Resource hooks require Pulumi to run your program. For `refresh` and `destroy` operations, this means you must use the `--run-program` flag for hooks to work. Read the full [documentation on resource hooks](/docs/iac/concepts/options/hooks/) to learn more.
{{% /notes %}}

Share any issues with your experience with us on [GitHub](https://github.com/pulumi/pulumi), [X](https://twitter.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
