---
title_tag: "Configuration | Pulumi Concepts"
meta_desc: This page provides an overview of how Pulumi manages cloud application configuration settings.
title: Configuration
h1: Configuration
menu:
    iac:
        name: Configuration
        parent: iac-concepts
        weight: 40
aliases:
- /docs/reference/config/
- /docs/tour/programs-configuration/
- /docs/tour/programs-configuring/
- /docs/intro/concepts/config/
- /docs/concepts/config
---

Different stacks for a single project often need different values. You might want a different size for your AWS EC2 instance, or a different number of servers for your Kubernetes cluster, between your development and production stacks.

Pulumi offers a configuration system for managing such differences. Instead of hard-coding the differences, you can store and retrieve configuration values using a combination of the [CLI](/docs/iac/cli/) and the programming model.

The key-value pairs for any given stack are stored in [your project's stack settings file](/docs/iac/concepts/projects/#stack-settings-file), which is automatically named `Pulumi.<stack-name>.yaml`. Stack configuration files should be committed to version control because their values drive the behavior of your Pulumi program.

## Configuration options {#config-stack}

You can use both the CLI and the programming model for your Pulumi configuration.

* The CLI offers a `config` command with `set` and `get` subcommands for managing key-value pairs.
* The programming model offers a `Config` object with getters for retrieving values.

{{% notes type="info" %}}
All shell environment variables are passed to the running program and can be read with standard runtime APIs, such as `process.env` in Node.js and `os.environ` in Python, which can also drive dynamic behavior. Prefer configuration, however, because it's designed for multi-stack collaborative scenarios.
{{% /notes %}}

## Configuration keys

Configuration keys use the format `[<namespace>:]<key-name>`, with a colon delimiting the optional namespace and the actual key name. When a key name is used without a colon, Pulumi uses the current [project name](/docs/iac/concepts/projects/#pulumi-yaml) from `Pulumi.yaml` as the namespace.

This namespacing allows the AWS package to accept a configuration value for `aws:region` without conflicting with other packages using the common key name `region`. It also allows [custom components](/docs/iac/concepts/components/) to define their own key spaces without risk of conflicting with other components, packages, or projects.

## Setting and getting configuration values

The `pulumi config` CLI command can get, set, or list configuration key-value pairs in your current project stack:

* `pulumi config set <key> [value]` sets a configuration entry `<key>` to `[value]`.
* `pulumi config get <key>` gets an existing configuration value with the key `<key>`.
* `pulumi config` gets all configuration key-value pairs in the current stack (as JSON if `--json` is passed).

{{% notes type="info" %}}
When using the `config set` command, any existing value for `<key>` is overwritten without warning.
{{% /notes %}}

For example, to set and then get the current AWS region in the `aws` package, run the following:

```bash
$ pulumi config set aws:region us-west-2
$ pulumi config get aws:region
us-west-2
```

To set and get configuration in the current project (named `broome-proj`, for example), use the key name on its own:

```bash
$ pulumi config set name BroomeLLC
$ pulumi config get name
BroomeLLC
```

If you omit `[value]` when setting a configuration key, the CLI prompts for it interactively. You can also pipe the value in on standard input, which helps with multiline values or any value that would otherwise need escaping on the command line:

```bash
$ cat my_key.pub | pulumi config set publicKey
```

## Using the config flag with `pulumi new`

Configuration keys and values can be passed when using `pulumi new`.

To pass a single key/value config pair use:

```bash
$ pulumi new template-name --config="key=value"
```

To pass multiple key/value config pairs use:

```bash
$ pulumi new template-name --config="key=value" --config="key=value"
```

And a complete example showing how to pass in the AWS region:

```bash
$ pulumi new aws-typescript --config="aws:region=us-west-2"
```

## Accessing configuration from code {#code}

Configuration values can be retrieved for a given stack using either {{< pulumi-config-get >}} or {{< pulumi-config-require >}}. {{< pulumi-config-get >}} returns {{< language-null >}} if the configuration value was not provided, and {{< pulumi-config-require >}} raises an exception with an explanatory error message, stopping the deployment until the value is set with the CLI.

{{% notes type="info" %}}
Configuration values can only be **read** during program execution, not set. To programmatically manage stack configurations (like setting config values or creating stacks dynamically), use [Automation API](/docs/iac/concepts/automation-api/). Automation API provides full programmatic control over Pulumi operations, including writing configuration values to stack files and managing stack lifecycle.
{{% /notes %}}

For potentially secret config, use {{< pulumi-config-getsecret >}} or {{< pulumi-config-requiresecret >}}, which return the config value as an `Output` that carries both the value and its secret-ness, so the value is encrypted whenever it's serialized (see [secrets](/docs/iac/concepts/secrets/) for more on managing secret values).

Configuration methods operate on a particular namespace, which by default is the name of the current project. Passing an empty constructor to {{< pulumi-config >}}, as in the following example, sets it up to read values set without an explicit namespace (e.g., `pulumi config set name Joe`):

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let config = new pulumi.Config();
let name = config.require("name");
let lucky = config.getNumber("lucky") || 42;
let secret = config.requireSecret("secret");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
config = pulumi.Config()
name = config.require('name')
lucky = config.get_int('lucky') or 42
secret = config.require_secret('secret')
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)
func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        conf := config.New(ctx, "")
        name := conf.Require("name")
        lucky, err := conf.TryInt("lucky")
        if err != nil {
            lucky = 42
        }
        secret := conf.RequireSecret("secret")
        ctx.Export("name", pulumi.String(name))
        ctx.Export("lucky", pulumi.Int(lucky))
        ctx.Export("secret", secret)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
var name = config.Require("name");
var lucky = config.GetInt32("lucky") ?? 42;
var secret = config.RequireSecret("secret");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
public static void stack(Context ctx) {
    var config = ctx.config();
    var name = config.require("name");
    var lucky = config.getInteger("lucky").orElse(42);
    var secret = config.requireSecret("secret");
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  name:
    type: string
  lucky:
    default: 42
  secret:
    type: string
    secret: true
```

{{% /choosable %}}

{{< /chooser >}}

To access a namespaced configuration value, such as one set for a provider library like `aws`, you must pass the library's name to the constructor. The examples below assume the value has already been set in your stack's configuration file (e.g., `Pulumi.dev.yaml`) — either by running `pulumi config set aws:region us-west-2` from the command line, or by adding it to the file directly:

```yaml
# Pulumi.dev.yaml
config:
  aws:region: us-west-2
```

Given that configuration, the following shows how to read the value from within your Pulumi program:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
let awsConfig = new pulumi.Config("aws");
let awsRegion = awsConfig.require("region");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
aws_config = pulumi.Config("aws")
aws_region = aws_config.require("region")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
awsConfig := config.New(ctx, "aws")
awsRegion := awsConfig.Require("region")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var awsConfig = new Pulumi.Config("aws");
var awsRegion = awsConfig.Require("region");
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var awsConfig = ctx.config("aws");
var awsRegion = awsConfig.require("region");
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  awsRegion: ${aws:region}
```

{{% /choosable %}}

{{< /chooser >}}

Similarly, if you are writing code that will be imported into a broader project, such as your own library of [Pulumi components](/docs/iac/concepts/components/), pass your library's name to the {{< pulumi-config >}} constructor to limit the scope of the query to values prefixed with the name of your library:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
class MyComponent extends pulumi.ComponentResource {
    constructor(name: string, args = {}, opts: pulumi.ComponentResourceOptions = {}) {
        super("mylib:index:MyComponent", name, args, opts);

        // Read settings from the 'mylib' namespace (e.g., 'mylib:name').
        const config = new pulumi.Config("mylib");
        const name = config.require("name");
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class MyComponent(pulumi.ComponentResource):
    def __init__(self, name, opts = None):
        super().__init__("mylib:index:MyComponent", name, None, opts)

        # Read settings from the 'mylib' namespace (e.g., 'mylib:name').
        config = pulumi.Config("mylib")
        name = config.require("name")

        # ...

```

{{% /choosable %}}

{{% choosable language go %}}

```go
type MyComponent struct {
    pulumi.ResourceState
}

func NewMyComponent(ctx *pulumi.Context, name string, opts ...pulumi.ResourceOption) (*MyComponent, error) {
    myComponent := &MyComponent{}
    err := ctx.RegisterComponentResource("mylib:index:MyComponent", name, myComponent, opts...)
    if err != nil {
        return nil, err
    }

    // Read settings from the 'mylib' namespace (e.g., 'mylib:name').
    conf := config.New(ctx, "mylib")
    name := conf.Require("name")

    // ...
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
class MyComponent : Pulumi.ComponentResource
{
    public MyComponent(string name, ComponentResourceOptions opts)
        : base("mylib:index:MyComponent", name, opts)
    {

        // Read settings from the 'mylib' namespace (e.g., 'mylib:name').
        var config = new Pulumi.Config("mylib");
        var name = config.Require("name");

        // ...
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;

class MyComponent extends ComponentResource {
    public MyComponent(String name, ComponentResourceOptions opts) {
        super("mylib:index:MyComponent", name, null, opts);

        // Read settings from the 'mylib' namespace (e.g., 'mylib:name').
        var config = ctx.config("mylib");
        var name = config.require("name");

        // ...
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

## Structured configuration

Pulumi also supports structured configuration, which you set with `pulumi config set` and the `--path` flag. `--path` tells the CLI to treat the config key as a path to a location within an object.

For example:

```bash
$ pulumi config set --path 'data.active' true
$ pulumi config set --path 'data.nums[0]' 1
$ pulumi config set --path 'data.nums[1]' 2
$ pulumi config set --path 'data.nums[2]' 3
```

The structure of `data` is persisted in the stack's `Pulumi.<stack-name>.yaml` file as:

```yaml
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

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

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
    "fmt"

    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
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
{{% choosable language java %}}

```java
public static void stack(Context ctx) {
    var config = ctx.config();
    var data = config.requireObject("data", Map.class);
    ctx.log().info(String.format("Active: %s", data.get("active")));
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

In Pulumi YAML, you declare the config inputs your program accepts using the `config` block in your `Pulumi.yaml` file. To work with structured (object) configuration, declare the key with `type: Object`. Pass the value from the stack configuration file using `pulumi config set --path`, and reference the whole object or individual properties in your program using `${configKey}` interpolation.

```yaml
name: my-project
runtime: yaml
config:
  data:
    type: Object
    default:
      active: true
      nums:
        - 1
        - 2
        - 3
resources:
  my-bucket:
    type: aws:s3:BucketV2
    properties:
      tags:
        Active: ${data.active}
```

{{% /choosable %}}

{{< /chooser >}}

### Accessing nested values

`requireObject` and `getObject` return a plain object — a dictionary or map, depending on the language — and not a `Config` instance. So once you have the object, reach into it with ordinary property or key access rather than chaining more `Config` calls. Nesting can go deeper than one level, as in this `api` key:

```bash
$ pulumi config set --path 'api.endpoint' "https://api.example.com"
$ pulumi config set --path 'api.timeout' 30
$ pulumi config set --path 'api.headers.authorization' "Bearer token123"
$ pulumi config set --path 'api.headers.content-type' "application/json"
```

Read the whole `api` object once, then walk it:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
interface ApiConfig {
    endpoint: string;
    timeout: number;
    headers: {
        authorization: string;
        "content-type": string;
    };
}

const config = new pulumi.Config();
const apiConfig = config.requireObject<ApiConfig>("api");

// Access nested properties directly using standard object notation
const endpoint = apiConfig.endpoint;  // "https://api.example.com"
const timeout = apiConfig.timeout;    // 30
const authHeader = apiConfig.headers.authorization;  // "Bearer token123"

// You CANNOT chain config.require() calls like this:
// const endpoint = config.require("api").require("endpoint");  // This does NOT work!
// Reason: requireObject() returns a plain JavaScript object, not a Config instance,
// and only Config instances have the require() method.
```

{{% /choosable %}}

{{% choosable language python %}}

```python
config = pulumi.Config()
api_config = config.require_object("api")

# Access nested properties using dictionary notation
endpoint = api_config["endpoint"]  # "https://api.example.com"
timeout = api_config["timeout"]    # 30
auth_header = api_config["headers"]["authorization"]  # "Bearer token123"
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type ApiConfig struct {
    Endpoint string
    Timeout  int
    Headers  map[string]string
}

cfg := config.New(ctx, "")
var apiConfig ApiConfig
cfg.RequireObject("api", &apiConfig)

// Access nested properties directly
endpoint := apiConfig.Endpoint  // "https://api.example.com"
timeout := apiConfig.Timeout    // 30
authHeader := apiConfig.Headers["authorization"]  // "Bearer token123"
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
var apiConfig = config.RequireObject<JsonElement>("api");

// Access nested properties
var endpoint = apiConfig.GetProperty("endpoint").GetString();  // "https://api.example.com"
var timeout = apiConfig.GetProperty("timeout").GetInt32();    // 30
var authHeader = apiConfig.GetProperty("headers")
    .GetProperty("authorization").GetString();  // "Bearer token123"
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var config = ctx.config();
var apiConfig = config.requireObject("api", Map.class);

// Access nested properties
var endpoint = (String) apiConfig.get("endpoint");  // "https://api.example.com"
var timeout = (Integer) apiConfig.get("timeout");   // 30
var headers = (Map<String, String>) apiConfig.get("headers");
var authHeader = headers.get("authorization");  // "Bearer token123"
```

{{% /choosable %}}

{{% choosable language yaml %}}

In Pulumi YAML, declare the object config input in your `Pulumi.yaml` file, then reference its properties using dot notation in interpolation expressions.

```yaml
name: my-project
runtime: yaml
config:
  api:
    type: Object
    default:
      endpoint: https://api.example.com
      timeout: 30
      headers:
        authorization: Bearer token123
        content-type: application/json
outputs:
  # Access nested properties using dot notation in interpolation expressions
  endpoint: ${api.endpoint}
  timeout: ${api.timeout}
  authHeader: ${api.headers.authorization}
```

{{% /choosable %}}

{{< /chooser >}}

## Project-level configuration

Some configuration is the same for more than one stack in a project — `aws:region`, for example, is often shared across several stacks or all of them. Project-level configuration (also called hierarchical configuration) lets you set such values once at the project level instead of repeating them in every stack's configuration file.

### Setting project-level configuration

You define project-level configuration in the project folder's `Pulumi.yaml` file, using any text editor.

{{% notes type="info" %}}
The `pulumi config set` command does not currently support project-level configuration. Enter the configuration values directly in the `Pulumi.yaml` file instead. Project-level configuration also supports plaintext values only. Support for [setting project-level config from the CLI](https://github.com/pulumi/pulumi/issues/12041), [project-level secrets](https://github.com/pulumi/pulumi/issues/11549), and other features is planned.
{{% /notes %}}

Project-level configuration supports both flat and structured configuration, in the same forms described in [Structured configuration](/docs/iac/concepts/config/#structured-configuration).

{{% notes type="warning" %}}
**Important:** Stack-level and project-level YAML files use different syntax for structured configuration:

* **Stack-level files** (`Pulumi.<stack-name>.yaml`): use the format `projectname:key:`, and nest structured values directly under the key.
* **Project-level file** (`Pulumi.yaml`): use the format `key:` with no project name prefix, and nest structured values under a `value:` wrapper.

Watch for this difference when you move configuration between the two files.
{{% /notes %}}

Using the keys from the earlier examples, project-level configuration inside `Pulumi.yaml` looks like this:

```yaml
config:
  aws:region: us-east-1
  name: BroomeLLC
  data:
    value: # Required for project-level structured config
      active: true
      nums:
      - 10
      - 20
      - 30
```

The same configuration in a stack-level file (`Pulumi.dev.yaml`) would look like this (assuming your project name is `myproject`):

```yaml
config:
  aws:region: us-east-1
  myproject:name: BroomeLLC
  myproject:data:             # Note: uses project name prefix and no 'value' key needed
    active: true
    nums:
    - 10
    - 20
    - 30
```

With project-level configuration in place, every stack in the project uses those values by default, unless a stack's own configuration overrides them.

### Project and stack configuration scope

Stack-level configuration using the same key supersedes the project-level configuration for that key. For example, given the project-level configuration above and a `Pulumi.dev.yaml` file containing:

```yaml
config:
  aws:region: us-east-2
  name: MopLLC
```

Then the `dev` stack would be deployed in `us-east-2` instead of `us-east-1` and the `name` configuration value would be `MopLLC` instead of `BroomeLLC` defined in the project configuration.

### Strongly typed configuration

Project-level configuration can also define type specifications for stack-level configuration, including defaults. Commands like `pulumi preview` then fail with an error if a stack-level configuration value has the wrong type.

For example, given this in the `Pulumi.yaml` file:

```yaml
config:
    name:
        type: string
        description: Base name to use for resources.
        default: BroomeLLC
    subnets:
        type: array
        description: Array of subnets to create.
        items:
            type: string
```

Stacks default to `BroomeLLC` for the `name` configuration item, and the Pulumi CLI reports an error if a stack configuration file sets `name` to, say, an integer. The CLI reports an error in the same way if a stack's `subnets` property is not an array of strings.

{{% notes type="info" %}}
At this time, configuration specifications are not supported for structured configuration.
{{% /notes %}}

## Provider configuration options

There are three ways to configure providers:

1. Set configuration keys in the stack configuration file: `pulumi config set [PROVIDER]:[KEY] [VALUE]`
2. Set a provider-specific environment variable
3. Pass arguments to the provider's SDK constructor, in your program

Note the following:

* Only the default provider reads configuration file settings. A provider object that you instantiate yourself does not read values from the stack configuration.
* The precedence of configuration sources (configuration file, environment, and constructor arguments) can vary between providers. Refer to the provider's documentation for its specific rules.

## Pulumi configuration options

This is a list of configuration keys that the Pulumi CLI is aware of:

### `pulumi:disable-default-providers`

A list of packages for which [default providers should be disabled](/docs/iac/concepts/providers/#disabling-default-providers). `*` disables default providers for all
packages.

In the following example, the default providers for [aws](/registry/packages/aws/) and [kubernetes](/registry/packages/kubernetes/) are disabled.

```yaml
config:
  pulumi:disable-default-providers:
    - aws
    - kubernetes
```

### `pulumi:tags`

A list of [stack tags](/docs/iac/concepts/stacks/#stack-tags) which are read by the Pulumi CLI and automatically applied on the stack at
every `pulumi up` or `pulumi refresh` action.

```yaml
config:
  pulumi:tags:
    company: "Some LLC"
    team: Ops
```

The Pulumi CLI only creates or updates tags listed in the config. If you remove a tag from the stack config, remove it from the stack in Pulumi Cloud manually as well.

Stack tags applied by Pulumi CLI are listed in the `Tags` section of the Overview tab:

![Tags applied by Pulumi CLI](/images/docs/concepts/stack-config-tags.png)

## Using Pulumi ESC from Pulumi stack config

{{< pulumi-cloud />}}

Configuration and secrets that several stacks share don't have to be duplicated across their stack configuration files — Pulumi ESC can hold them centrally instead.

Once you have an [environment](/docs/esc/concepts/) set up and are [projecting Pulumi configuration](/docs/esc/concepts/outputs/#pulumiconfig) from it, you can [import that environment](/docs/esc/guides/pulumi-iac/) (or several environments) into your Pulumi stack.

```yaml
# import the test environment and all of its configuration
environment:
  - test
config:
    # normal pulumi config
```

When a key is set both by an imported environment and explicitly in your stack configuration, the explicit stack value takes precedence. See [Precedence](/docs/esc/concepts/outputs/#precedence-1) for the full rules.
