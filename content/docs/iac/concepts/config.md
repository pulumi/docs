---
title_tag: "Configuration | Pulumi Concepts"
meta_desc: This page provides an overview of how Pulumi manages cloud application configuration settings.
title: Configuration
h1: Configuration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Configuration
        parent: iac-concepts
        weight: 40
    concepts:
        weight: 6
aliases:
- /docs/reference/config/
- /docs/tour/programs-configuration/
- /docs/tour/programs-configuring/
- /docs/intro/concepts/config/
- /docs/concepts/config
---

In many cases, different stacks for a single project will need differing values. For instance, you may want to use a different size for your AWS EC2 instance, or a different number of servers for your Kubernetes cluster between your development and production stacks.

Pulumi offers a configuration system for managing such differences. Instead of hard-coding the differences, you can store and retrieve configuration values using a combination of the [CLI](/docs/cli/) and the programming model.

The key-value pairs for any given stack are stored in [your project's stack settings file](/docs/concepts/projects#stack-settings-file), which is automatically named `Pulumi.<stack-name>.yaml`. Stack configuration files should be committed to version control because their values drive the behavior of your Pulumi program.

## Configuration Options {#config-stack}

You can use both the CLI and the programming model for your Pulumi configuration.

* The CLI offers a `config` command with `set` and `get` subcommands for managing key-value pairs.
* The programming model offers a `Config` object with various getters for retrieving values.

> All shell environment variables are passed to the running program and can be accessed using standard runtime APIs, such as `process.env` in Node.js and `os.environ` in Python, which can also be used for dynamic behavior. Configuration is preferable, however, because it is designed for multi-stack collaborative scenarios.

## Configuration Keys

Configuration keys use the format `[<namespace>:]<key-name>`, with a colon delimiting the optional namespace and the actual key name. In cases where a simple name without a colon is used, Pulumi automatically uses the current [project name](/docs/concepts/projects#project-name) from `Pulumi.yaml` as the namespace.

As an example, this capability allows the AWS package to accept a configuration value for `aws:region` without conflicting with other packages using the common key name `region`. It also allows [custom components](/docs/concepts/resources#components) to define their own key spaces without risk of conflicting with other components, packages, or projects.

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

## Using the Config Flag with `pulumi new`

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

## Accessing Configuration from Code {#code}

Configuration values can be retrieved for a given stack using either {{< pulumi-config-get >}} or {{< pulumi-config-require >}}. Using {{< pulumi-config-get >}} will return {{< language-null >}} if the configuration value was not provided, and {{< pulumi-config-require >}} will raise an exception with a helpful error message to prevent the deployment from continuing until the variable has been set using the CLI.

{{% notes type="info" %}}
Configuration values can only be **read** during program execution, not set. To programmatically manage stack configurations (like setting config values or creating stacks dynamically), use [Automation API](/docs/iac/automation-api/). Automation API provides full programmatic control over Pulumi operations, including writing configuration values to stack files and managing stack lifecycle.
{{% /notes %}}

For potentially-secret config, use {{< pulumi-config-getsecret >}} or {{< pulumi-config-requiresecret >}}, which will return the config value as an `Output` which carries both the value and the secret-ness of the config value so that it will be encrypted whenever serialized (see [secrets](/docs/concepts/secrets/) for more on managing secret values).

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
var secret = config.RequireSecret("secret")
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

To access a namespaced configuration value, such as one set for a provider library like `aws`, you must pass the library's name to the constructor. For example, to retrieve the configured value of `aws:region`:

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

Similarly, if you are writing code that will be imported into a broader project, such as your own library of [Pulumi components](/docs/concepts/resources/components/), you should instead pass your library's name to the {{< pulumi-config >}} constructor to limit the scope of the query to values prefixed with the name of your library:

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

```yaml
# Pulumi YAML config values are currently limited to String, Number, List<String> and List<Number>
```

{{% /choosable %}}

{{< /chooser >}}

### Accessing nested values

When you retrieve structured configuration using `requireObject` or `getObject`, the returned value is a plain object (or dictionary/map in other languages), not a Config instance. This means you access nested properties using standard object property access, not by chaining Config methods.

For example, if you have this configuration:

```bash
$ pulumi config set --path 'api.endpoint' "https://api.example.com"
$ pulumi config set --path 'api.timeout' 30
$ pulumi config set --path 'api.headers.authorization' "Bearer token123"
$ pulumi config set --path 'api.headers.content-type' "application/json"
```

This creates the following structure in your `Pulumi.<stack-name>.yaml` (where `myproject` is your project name from `Pulumi.yaml`):

```yaml
config:
  myproject:api:
    endpoint: https://api.example.com
    timeout: 30
    headers:
      authorization: Bearer token123
      content-type: application/json
```

You can access these nested values in your program like this:

{{< chooser language "typescript,python,go,csharp,java" >}}

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

{{< /chooser >}}

Alternatively, you can set individual nested values directly without using `--path`:

```bash
$ pulumi config set api '{"endpoint":"https://api.example.com","timeout":30}'
```

### Complete example: Database configuration

Here's a complete example that shows how to configure and access a database connection object with nested properties:

**Step 1:** Set the configuration values using the CLI:

```bash
$ pulumi config set --path 'database.host' "db.example.com"
$ pulumi config set --path 'database.port' 5432
$ pulumi config set --path 'database.name' "myapp"
$ pulumi config set --path 'database.credentials.username' "dbuser"
$ pulumi config set --path 'database.credentials.password' "secretpass" --secret
$ pulumi config set --path 'database.ssl.enabled' true
$ pulumi config set --path 'database.ssl.mode' "require"
```

**Step 2:** This creates the following in your `Pulumi.<stack-name>.yaml` (where `myproject` is your project name):

```yaml
config:
  myproject:database:
    host: db.example.com
    port: 5432
    name: myapp
    credentials:
      username: dbuser
      password:
        secure: AAABAKKj4T...  # encrypted
    ssl:
      enabled: true
      mode: require
```

**Step 3:** Access the configuration in your program:

{{< chooser language "typescript,python,go" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

interface DatabaseConfig {
    host: string;
    port: number;
    name: string;
    credentials: {
        username: string;
        password: string;
    };
    ssl: {
        enabled: boolean;
        mode: string;
    };
}

const config = new pulumi.Config();
const dbConfig = config.requireObject<DatabaseConfig>("database");

// Access nested values using standard object notation
const connectionString = pulumi.interpolate`postgresql://${dbConfig.credentials.username}:${dbConfig.credentials.password}@${dbConfig.host}:${dbConfig.port}/${dbConfig.name}?sslmode=${dbConfig.ssl.mode}`;

// Use the configuration to create resources
export const host = dbConfig.host;
export const port = dbConfig.port;
export const sslEnabled = dbConfig.ssl.enabled;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config()
db_config = config.require_object("database")

# Access nested values using dictionary notation
connection_string = f"postgresql://{db_config['credentials']['username']}:{db_config['credentials']['password']}@{db_config['host']}:{db_config['port']}/{db_config['name']}?sslmode={db_config['ssl']['mode']}"

# Use the configuration to create resources
pulumi.export("host", db_config["host"])
pulumi.export("port", db_config["port"])
pulumi.export("ssl_enabled", db_config["ssl"]["enabled"])
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

type SSLConfig struct {
    Enabled bool   `json:"enabled"`
    Mode    string `json:"mode"`
}

type Credentials struct {
    Username string `json:"username"`
    Password string `json:"password"`
}

type DatabaseConfig struct {
    Host        string      `json:"host"`
    Port        int         `json:"port"`
    Name        string      `json:"name"`
    Credentials Credentials `json:"credentials"`
    SSL         SSLConfig   `json:"ssl"`
}

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        cfg := config.New(ctx, "")
        var dbConfig DatabaseConfig
        cfg.RequireObject("database", &dbConfig)

        // Access nested values
        connectionString := fmt.Sprintf(
            "postgresql://%s:%s@%s:%d/%s?sslmode=%s",
            dbConfig.Credentials.Username,
            dbConfig.Credentials.Password,
            dbConfig.Host,
            dbConfig.Port,
            dbConfig.Name,
            dbConfig.SSL.Mode,
        )

        // Use the configuration
        ctx.Export("host", pulumi.String(dbConfig.Host))
        ctx.Export("port", pulumi.Int(dbConfig.Port))
        ctx.Export("sslEnabled", pulumi.Bool(dbConfig.SSL.Enabled))

        return nil
    })
}
```

{{% /choosable %}}

{{< /chooser >}}

## Project Level Configuration

There are cases where configuration for more than one stack in a given project is the same. For example, `aws:region` may be the same across multiple or all stacks in a project. Project level configuration (also sometimes referred to as hieararchical configuration) allows setting configuration at the project level instead of having to repeat the configuration setting in each stack's configuration file.

### Setting Project Level Configuration

Project level configuration is defined inside the project folder's `Pulumi.yaml` file using one's favorite editor.

{{% notes "info" %}}
At this time, the `pulumi config set` command does not support project level configuration. Therefore the configuration values are entered directly in the `Pulumi.yaml` file. Also, project level configuration only supports clear text configuration. Support for [pulumi config](https://github.com/pulumi/pulumi/issues/12041) and [project-level secrets](https://github.com/pulumi/pulumi/issues/11549) and other features are planned.
{{% /notes %}}

Project level configuration supports both simple and structured configuration as described in the sections above.

{{% notes type="warning" %}}
**Important:** Stack-level and project-level YAML files use different syntax for structured configuration:

* **Stack-level files** (`Pulumi.<stack-name>.yaml`): Use the format `projectname:key:` and nest structured values directly under the key
* **Project-level file** (`Pulumi.yaml`): Use the format `key:` (no project name prefix) and nest structured values under a `value:` wrapper

This distinction is easy to miss and can cause confusion when moving configuration between files.
{{% /notes %}}

The following example shows what the project level configuration (inside `Pulumi.yaml`) looks like based on the examples shown above:

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
  name: BroomeLLC
  myproject:data:             # Note: uses project name prefix and no 'value' key needed
    active: true
    nums:
    - 10
    - 20
    - 30
```

When project level configuration is set as such, the stacks will consume the project level configuration settings by default unless stack-specific configuration overrides the project-level settings.

### Project and Stack Configuration Scope

Stack level configuration using the same key supercedes the project level configuration for that key. For example, if, given the above project level configuration example, one had a `Pulumi.dev.yaml` file containing:

```
config:
  aws:region: us-east-2
  name: MopLLC
```

Then the `dev` stack would be deployed in `us-east-2` instead of `us-east-1` and the `name` configuration value would be `MopLLC` instead of `BroomeLLC` defined in the project configuration.

### Strongly Typed Configuration

The project level configuration can also be used to define type specifications for stack level configuration, including setting defaults. This enables commands like `pulumi preview` to throw an error if a stack level configuration value is not of the correct type.

For example, given this in the `Pulumi.yaml` file:

```
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

The stacks will default to using `BroomeLLC` for the name configuration item. And the `pulumi` cli will throw an error if the stack configuration file contains a `name` property set to, say, an integer. Similarly, if the stack configuration file has a `subnets` property and it is not defined as an array of strings, the `pulumi` cli will throw an error.

{{% notes "info" %}}
At this time, configuration specifications are not supported for structured configuration.
{{% /notes %}}

## Provider Configuration Options

There are three ways to configure providers:

1. Set configuration keys in the stack configuration file: `pulumi config set [PROVIDER]:[KEY] [VALUE]`
2. Set a provider-specific environment variable
3. Pass arguments to the provider's SDK constructor, in your program

Please note:

* Configuration file settings are only used by the default provider. If you instantiate a provider object, it will not read values from the stack configuration.
* The precedence of configuration sources (configuration file, environment and args) can vary between providers. Please refer to the provider's documentation for specific configuration instructions.

## Pulumi Configuration Options

This is a list of configuration keys that the Pulumi CLI is aware of:

### `pulumi:disable-default-providers`

A list of packages for which [default providers should be disabled](/docs/concepts/resources/providers#disabling-default-providers). `*` disables default providers for all
packages.

In the following example, the default providers for [aws](/registry/packages/aws/) and [kubernetes](/registry/packages/kubernetes/) are disabled.

```yaml
config:
  pulumi:disable-default-providers:
    - aws
    - kubernetes
```

### `pulumi:tags`

A list of [stack tags](/docs/concepts/stack/#stack-tags) which are read by the Pulumi CLI and automatically applied on the stack at
every `pulumi up` or `pulumi refresh` action.

```yaml
config:
  pulumi:tags:
    company: "Some LLC"
    team: Ops
```

Pulumi CLI only creates or updates tags which are listed in the config. If you remove a tag from the stack config, you have to remove it from the stack in Pulumi Cloud manually.

Stack tags applied by Pulumi CLI are listed in the `Tags` section of the Overview tab:

![Tags applied by Pulumi CLI](/images/docs/concepts/stack-config-tags.png)

## Using Pulumi ESC from Pulumi Stack Config

Often there is common configuration and secrets you do not want to duplicate in various stack configuration files. Pulumi ESC can help with that!

Once you have an [environment](/docs/esc/concepts/) set up and you are [projecting pulumi configuration](/docs/esc/environments/working-with-environments/#projecting-pulumi-config), you can [import that environment](/docs/esc/integrations/infrastructure/pulumi-iac/pulumi-stacks/) (or multiple environments) into your Pulumi stack.

```yaml
# import the test environment and all of its configuration
environment:
  - test
config:
    # normal pulumi config
```
