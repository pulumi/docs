---
title: "Resource hooks"
date: 2025-06-30
meta_desc: "Pulumi now allows you to run custom code at any point in the resource lifecycle"
meta_image: meta.png
authors:
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

{{% chooser language "javascript,typescript,python,go,java,csharp" %}}

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
import pulumi_command

curl = "curl -H'Host: example.com' localhost:1234"

cmd = pulumi_command.local.Command("curl",
    create=curl,
    update=curl,
    delete=curl,
    triggers=[str(datetime.datetime.now())],
)
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

{{% choosable language java %}}

```java
package app;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.command.local.Command;
import com.pulumi.command.local.CommandArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var curl = "curl -H'Host: example.com' localhost:1234";

        var cmd = new Command("curl", CommandArgs.builder()
            .create(curl)
            .update(curl)
            .delete(curl)
            .triggers(java.util.Collections.singletonList(java.time.LocalDateTime.now().toString()))
            .build());

        ctx.export("stdout", cmd.stdout());
    }
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

{{% chooser language "javascript,typescript,python,go,java,csharp" %}}

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
import pulumi_command

curl = "curl -H'Host: example.com' localhost:1234"

cmd = pulumi_command.local.Command("curl",
    create=curl,
    update=curl,
    delete=curl,
    triggers=[str(datetime.datetime.now())],
)
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

{{% choosable language java %}}

```java
package app;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.command.local.Command;
import com.pulumi.command.local.CommandArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var curl = "curl -H'Host: example.com' localhost:1234";

        var cmd = new Command("curl", CommandArgs.builder()
            .create(curl)
            .update(curl)
            .delete(curl)
            .triggers(java.util.Collections.singletonList(java.time.LocalDateTime.now().toString()))
            .build());

        ctx.export("stdout", cmd.stdout());
    }
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

## Where can we go from here?

Resource hooks are a powerful new feature that allow you to run custom code at any point in the resource lifecycle. This opens up a wide range of possibilities, such as:

* Custom application health checks after creating or updating resources
* Collecting logs or metrics when your Pulumi resources change
* Running custom scripts such as database migrations as part of your Pulumi workflow.

{{% notes %}}
Notes
{{% /notes %}}

Share any issues with your experience with us on [GitHub](https://github.com/pulumi/pulumi), [X](https://twitter.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
