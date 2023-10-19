---
title_tag: Understanding Stack Outputs | Learn Pulumi
title: "Understanding Stack Outputs"
layout: topic
date: 2021-09-20T08:33:26-05:00
draft: false
description: Learn how to share values from a stack to other places.
meta_desc: Learn what stack outputs are, how to retrieve stack outputs using the Pulumi CLI, and how to configure a stack in this tutorial.
index: 2
estimated_time: 10
meta_image: meta.png
authors:
    - matt-stratton
---

We've created some resources. Now, let's see how we can use outputs outside of
Pulumi. In this part, we're going to explore _stack outputs_. Stack outputs
are, as you might guess, the values exported from any given stack. These values
are shown during an update, can be retrieved with the Pulumi CLI, and are
displayed in the [Pulumi Service](https://app.pulumi.com) once you've exported
them. Example values include resource IDs, computed IP addresses, and DNS names.
They're extremely useful when you want to run commands with the CLI that
reference those values. Note, though, that stack outputs are for the current
stack only. If you want to get values from another stack, you want to use stack
references, which bridge different stacks through inter-stack dependencies.

Typically, you will pass some value from your resources into the output, but to
illustrate how stack outputs work, we will set some stack outputs manually:

At the end of the {{< langfile >}} file of `my-first-app`, add the following line:

{{< chooser language "typescript,python,go,csharp,yaml" / >}}

{{% choosable language typescript %}}

```typescript
export const url = pulumi.interpolate`http://localhost:${frontendPort}`;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
pulumi.export("url", pulumi.Output.format("http://localhost:{0}", frontend_port))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
ctx.Export("url", pulumi.Sprintf("http://localhost:%v", frontendPort))
```

Note that you'll want to insert this just before the last `return nil` statement.

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
return new Dictionary<string, object?>
{
    ["url"] = Output.Format($"http://localhost:{frontendPort}")
};
```

Add this return statement to the end of the deployment function.

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
outputs:
  url: http://localhost:${frontendPort}
```

Replace the existing `outputs: {}` line with this code.

{{% /choosable %}}

Now, run `pulumi up -y`

```bash
$ pulumi up

Previewing update (dev)

View Live: https://app.pulumi.com/***/my-first-app/dev/previews/...
...

Updating (dev)

View Live: https://app.pulumi.com/***/my-first-app/dev/updates/3
...

    pulumi:pulumi:Stack my-first-app-dev running
    pulumi:pulumi:Stack my-first-app-dev

Outputs:
    url: "http://localhost:3001"
...
```

Notice that there is now a stack output for the value of the key `url`.

We can also get this value by running `pulumi stack output <key>` on any
particular stack.

```bash
$ pulumi stack output url
http://localhost:3001
```

And we can use this in the `curl` command to check our website:

```bash
$ curl $(pulumi stack output url)
```

## Making a stack configurable

One of the main reasons to use stacks is to have different configurations
between them. In this example, we will set a configuration that varies between
our `dev` and `staging` stacks and set it programmatically.

First, we need to define the configuration. We have already set this in the
`dev` stack in the Fundamentals tutorial. Let's take a look! Make sure the
`dev` stack is active:

```bash
$ pulumi stack select dev
```

Now, run the following command to get the values for this stack's configuration:

{{% choosable language typescript %}}

```bash
$ pulumi config
KEY              VALUE
backendPort      3000
database         cart
frontendPort     3001
mongoHost        mongodb://mongo:27017
mongoPort        27017
nodeEnvironment  development
protocol         http://
```

Let's set the configuration for the `staging` stack. We'll use the same values
as `dev`, except the `frontendPort` will be set to `3002`.

```bash
$ pulumi stack select staging

$ pulumi config set frontendPort 3002
$ pulumi config set backendPort 3000
$ pulumi config set mongoPort 27017
$ pulumi config set mongoHost mongodb://mongo:27017
$ pulumi config set database cart
$ pulumi config set nodeEnvironment development
$ pulumi config set protocol http://
```

You should have two new files in your directory now: `Pulumi.dev.yaml` and
`Pulumi.staging.yaml`. If you take a look at them, you'll see each one has the
value for `frontendPort` set (along with some other values we set in the
Fundamentals tutorial):

```bash
$ cat Pulumi.staging.yaml

config:
  my-first-app:backendPort: "3000"
  my-first-app:database: cart
  my-first-app:frontendPort: "3002"
  my-first-app:mongoHost: mongodb://mongo:27017
  my-first-app:mongoPort: "27017"
  my-first-app:nodeEnvironment: development
  my-first-app:protocol: http://
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi config
KEY               VALUE
backend_port      3000
database          cart
frontend_port     3001
mongo_host        mongodb://mongo:27017
mongo_port        27017
node_environment  development
protocol          http://
```

Let's set the configuration for the `staging` stack. We'll use the same values
as `dev`, except the `frontend_port` will be set to `3002`.

```bash
$ pulumi stack select staging

$ pulumi config set frontend_port 3002
$ pulumi config set backend_port 3000
$ pulumi config set mongo_port 27017
$ pulumi config set mongo_host mongodb://mongo:27017
$ pulumi config set database cart
$ pulumi config set node_environment development
$ pulumi config set protocol http://
```

You should have two new files in your directory now: `Pulumi.dev.yaml` and
`Pulumi.staging.yaml`. If you take a look at them, you'll see each one has the
value for `frontend_port` set (along with some other values we set in the
Fundamentals tutorial):

```bash
$ cat Pulumi.staging.yaml

config:
  my-first-app:backend_port: "3000"
  my-first-app:database: cart
  my-first-app:frontend_port: "3002"
  my-first-app:mongo_host: mongodb://mongo:27017
  my-first-app:mongo_port: "27017"
  my-first-app:node_environment: development
  my-first-app:protocol: http://
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ pulumi config
KEY              VALUE
backendPort      3000
database         cart
frontendPort     3001
mongoHost        mongodb://mongo:27017
mongoPort        27017
nodeEnvironment  development
protocol         http://
```

Let's set the configuration for the `staging` stack. We'll use the same values as `dev`, except the `frontendPort` will be set to `3002`.

```bash
$ pulumi stack select staging

$ pulumi config set frontendPort 3002
$ pulumi config set backendPort 3000
$ pulumi config set mongoPort 27017
$ pulumi config set mongoHost mongodb://mongo:27017
$ pulumi config set database cart
$ pulumi config set nodeEnvironment development
$ pulumi config set protocol http://
```

You should have two new files in your directory now: `Pulumi.dev.yaml` and
`Pulumi.staging.yaml`. If you take a look at them, you'll see each one has the
value for `frontendPort` set (along with some other values we set in the
Fundamentals tutorial):

```bash
$ cat Pulumi.staging.yaml

config:
  my-first-app:backendPort: "3000"
  my-first-app:database: cart
  my-first-app:frontendPort: "3002"
  my-first-app:mongoHost: mongodb://mongo:27017
  my-first-app:mongoPort: "27017"
  my-first-app:nodeEnvironment: development
  my-first-app:protocol: http://
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ pulumi config
KEY              VALUE
backendPort      3000
database         cart
frontendPort     3001
mongoHost        mongodb://mongo:27017
mongoPort        27017
nodeEnvironment  development
protocol         http://
```

Let's set the configuration for the `staging` stack. We'll use the same values
as `dev`, except the `frontendPort` will be set to `3002`.

```bash
$ pulumi stack select staging

$ pulumi config set frontendPort 3002
$ pulumi config set backendPort 3000
$ pulumi config set mongoPort 27017
$ pulumi config set mongoHost mongodb://mongo:27017
$ pulumi config set database cart
$ pulumi config set nodeEnvironment development
$ pulumi config set protocol http://
```

You should have two new files in your directory now: `Pulumi.dev.yaml` and
`Pulumi.staging.yaml`. If you take a look at them, you'll see each one has the
value for `frontendPort` set (along with some other values we set in the
Fundamentals tutorial):

```bash
$ cat Pulumi.staging.yaml

config:
  my-first-app:backendPort: "3000"
  my-first-app:database: cart
  my-first-app:frontendPort: "3002"
  my-first-app:mongoHost: mongodb://mongo:27017
  my-first-app:mongoPort: "27017"
  my-first-app:nodeEnvironment: development
  my-first-app:protocol: http://
```

{{% /choosable %}}

Now, if you run `pulumi up` while in the `staging` stack, we should see that the
frontend port is now set to `3002`:

```bash
$ pulumi up

Previewing update (staging)
...
...

Outputs:
    url: "http://localhost:3002"
...
```

Next up, we'll explore how to share outputs with other stacks. Let's go!
