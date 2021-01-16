---
title: "Configuration"
meta_desc: This page provides an overview of how Pulumi manages cloud application configuration settings.
menu:
  intro:
    parent: concepts
    weight: 6

aliases: ["/docs/reference/config/"]
---

In many cases, different stacks for a single project will need differing values. For instance, you may want to use a different size for your AWS EC2 instance, or a different number of servers for your Kubernetes cluster between your development and production stacks.

Pulumi offers a configuration system for managing such differences. Instead of hard-coding the differences, you can store and retrieve configuration values using a combination of the [CLI]({{< relref "/docs/reference/cli" >}}) and the [programming model]({{< relref "/docs/intro/concepts#programmingmodel" >}}).

The key-value pairs for any given stack are stored in [your project's stack settings file]({{< relref "/docs/intro/concepts/project#stack-settings-file" >}}), which is automatically named `Pulumi.<stack-name>.yaml`. You can typically ignore this file, although you may want to check it in and version it with your project source code.

## Configuration Options {#config-stack}

You can use both the CLI and the programming model for your Pulumi configuration.

* The CLI offers a `config` command with `set` and `get` subcommands for managing key-value pairs.
* The programming model offers a `Config` object with various getters and setters for retrieving values.

> All shell environment variables are passed to the running program and can be accessed using standard runtime APIs, such as `process.env` in Node.js and `os.environ` in Python, which can also be used for dynamic behavior. Configuration is preferable, however, because it is designed for multi-stack collaborative scenarios.

## Configuration Keys

Configuration keys use the format `[<namespace>:]<key-name>`, with a colon delimiting the optional namespace and the actual key name. In cases where a simple name without a colon is used, Pulumi automatically uses the current [project name]({{< relref "/docs/intro/concepts/project#project-name" >}}) from `Pulumi.yaml` as the namespace.

As an example, this capability allows the AWS package to accept a configuration value for `aws:region` without conflicting with other packages using the common key name `region`. It also allows [custom components]({{< relref "/docs/intro/concepts/resources#components" >}}) to define their own key spaces without risk of conflicting with other components, packages, or projects.

## Setting and Getting Configuration Values

The `pulumi config` CLI command can get, set, or list configuration key-value pairs in your current project stack:

* `pulumi config set <key> [value]` sets a configuration entry `<key>` to `[value]`.
* `pulumi config get <key>` gets an existing configuration value with the key `<key>`.
* `pulumi config` gets all configuration key-value pairs in the current stack (as JSON if `--json` is passed).

{{% notes "info" %}}
When using the `config set` command, any existing values for `<key>` will be overridden without warning.
{{% /notes %}}

For example, to set and then get the current AWS region in the `aws` package, you would run the following:

```bash
$ pulumi config set aws:region us-west-2
$ pulumi config get aws:region
us-west-2
```

To set and get configuration in the current project (named `broome-proj` for example), we can use the simplified key name:

```bash
$ pulumi config set name BroomeLLC
$ pulumi config get name
BroomeLLC
```

If `[value]` is not specified when setting a configuration key, the CLI will prompt for it interactively. Alternatively, the value can be set from standard input, which is useful for multiline values or any value that must be escaped on the command line:

```bash
$ cat my_key.pub | pulumi config set publicKey
```

## Accessing Configuration from Code {#code}

Configuration values can be retrieved using either {{< pulumi-config-get >}} or {{< pulumi-config-require >}}. Using {{< pulumi-config-get >}} will return {{< language-null >}} if the configuration value was not provided, and {{< pulumi-config-require >}} will raise an exception with a helpful error message to prevent the deployment from continuing until the variable has been set using the CLI.

The following example uses an empty constructor. If you are writing code that will be imported into a broader project, such as your own library of components, you should pass your library's name to the constructor. This string is used as a namespace for all configuration keys. Similarly, if you want to access the config of another library, such as the config for a standard library like `aws`, you should also pass the library's name to the constructor. The default constructor automatically uses the current project for that namespace.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let config = new pulumi.Config();
let name = config.require("name");
let lucky = config.getNumber("lucky") || 42;
console.log(`Hello, ${name} -- I see your lucky number is ${lucky}!`);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let config = new pulumi.Config();
let name = config.require("name");
let lucky = config.getNumber("lucky") || 42;
console.log(`Hello, ${name} -- I see your lucky number is ${lucky}!`);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config = pulumi.Config();
name = config.require('name');
lucky = config.get_number('lucky') or 42
print(f'Hello, {name} -- I see your lucky number is {lucky}!')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)
func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        conf := config.New(ctx, "")
        name := conf.Require("name")
        lucky, err := conf.TryInt("lucky")
        if err != nil {
            lucky = 42
        }
        fmt.Printf("Hello, %v -- I see your lucky number is %v!\n", name, lucky)
        return nil
    }
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
var name = config.Require("name");
var lucky = config.GetInt32("lucky") ?? 42;
Console.WriteLine($"Hello, {name} -- I see your lucky number is {lucky}!");
```

{{% /choosable %}}

{{< /chooser >}}

## Structured Configuration

Structured configuration is also supported and can be set using `pulumi config set` and the `--path` flag. When `--path` is used, it indicates the config key contains a path of where to store the value in an object.

For example:

```bash
$ pulumi config set --path 'data.active' true
$ pulumi config set --path 'data.nums[0]' 1
$ pulumi config set --path 'data.nums[1]' 2
$ pulumi config set --path 'data.nums[2]' 3
```

The structure of `data` is persisted in the stack's `Pulumi.<stack-name>.yaml` file as:

```
config:
  proj:data:
    active: true
    nums:
    - 1
    - 2
    - 3
```

For structured config, `true` and `false` values are persisted as boolean values, and values convertible to integers are persisted as integers.

The `data` config can be accessed in your Pulumi program using:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let config = new pulumi.Config();
let data = config.requireObject("data");
console.log(`Active: ${data.active}`);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
interface Data {
    active: boolean;
    nums: number[];
}

let config = new pulumi.Config();
let data = config.requireObject<Data>("data");
console.log(`Active: ${data.active}`);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config = pulumi.Config()
data = config.require_object("data")
print("Active:", data.get("active"))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

type Data struct {
	Active bool
	Nums   []int
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		var d Data
		cfg := config.New(ctx, "")
		cfg.RequireObject("data", &d)
		fmt.Printf("Active: %v\n", d.Active)
		return nil
	})
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
var data = config.RequireObject<JsonElement>("data");
Console.WriteLine($"Active: {data.GetProperty("active")}");
```

{{% /choosable %}}

{{< /chooser >}}
