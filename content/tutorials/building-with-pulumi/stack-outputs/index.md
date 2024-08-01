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
aliases:
    - /learn/building-with-pulumi/stack-outputs/
---

Now let's explore _stack outputs_. Stack outputs are values exported by a given stack. These values are shown during an update, can be retrieved with the Pulumi CLI, and are displayed in [Pulumi Cloud](https://app.pulumi.com) once you've exported them. Examples include resource IDs, computed IP addresses, and DNS names. They're useful in many ways, such as when you want to run CLI commands that reference those values.

To illustrate how stack outputs work, let's set one programmatically. At the end of {{< langfile >}} in `my-first-app`, add the following line:

{{< chooser language "typescript,python" />}}

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

Now, run `pulumi up`:

```bash
$ pulumi up

Previewing update (dev)

View in Browser: https://app.pulumi.com/***/my-first-app/dev/previews/...
...

Updating (dev)

View in Browser: https://app.pulumi.com/***/my-first-app/dev/updates/3
...

    pulumi:pulumi:Stack my-first-app-dev running
    pulumi:pulumi:Stack my-first-app-dev

Outputs:
    url: "http://localhost:3001"
...
```

Notice that there is now a stack output for the value of the key `url`.

We can get this value by running `pulumi stack output <key>` on any particular stack.

```bash
$ pulumi stack output url
http://localhost:3001
```

We can use it to open our website in a browser:

```bash
$ open $(pulumi stack output url)
```

Before moving on, destroy the `dev` stack, as we'll no longer need it for this tutorial:

```bash
$ pulumi destroy --yes
...

Destroying (dev)

     Type                         Name                  Status
 -   pulumi:pulumi:Stack          my-first-app-staging  deleted (0.16s)
 -   ├─ docker:index:Container    backendContainer      deleted (0.43s)
 -   ├─ docker:index:Container    mongoContainer        deleted (0.51s)
 -   ├─ docker:index:Container    frontendContainer     deleted (0.31s)
 -   ├─ docker:index:RemoteImage  mongoImage            deleted (0.60s)
 -   ├─ docker:index:RemoteImage  frontendImage         deleted (1s)
 -   ├─ docker:index:RemoteImage  backendImage          deleted (1s)
 -   └─ docker:index:Network      network               deleted (2s)

Outputs:
  - url: "http://localhost:3001"

Resources:
    - 8 deleted

Duration: 6s
```

## Making a stack configurable

One of the benefits of using Pulumi stacks is being able to configure each one independently. In this example, you'll learn how to do so by applying different settings to the `dev` and `staging` stacks.

For the `dev` stack, your work is already done; the stack itself may be empty (we just destroyed it above), but its configuration settings are still there in `Pulumi.dev.yaml` in case you need them again. Let's take a look. First, make sure the `dev` stack is still active:

```bash
$ pulumi stack select dev
```

Then run the following command to show all of its configuration values:

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

Now let's set the configuration for the `staging` stack --- only this time, we'll use a different value for the `frontendPort`:

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

{{< notes >}}

In addition to setting configuration values individually, you can also create a new stack and apply the settings from an existing stack in one step using `--copy-config-from`:

```bash
pulumi stack init staging --copy-config-from dev
```

{{< /notes >}}

You should now have two stack-configuration files in your project folder: `Pulumi.dev.yaml` and `Pulumi.staging.yaml`. If you take a look at them, you'll see each one has the value for `frontendPort` set (along with some other values we set in the Fundamentals tutorial):

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

Now, if you run `pulumi up` on the `staging` stack, you'll see that the frontend port is `3002`:

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

{{< tutorials/stepper >}}
