---
title: "Configuration and Secrets"
meta_desc: This page provides an overview of how Pulumi manages cloud application Configuration and Secrets.
menu:
  intro:
    parent: concepts
    weight: 4

aliases: ["/docs/reference/config/"]
---

In many cases, different stacks for a single project will need differing values. For instance, you may want to use a different size for your AWS EC2 instance, or a different number of servers for your Kubernetes cluster between your development and production stacks.

Pulumi offers a configuration system for managing such differences. Instead of hard-coding the differences, you can store and retrieve configuration values using a combination of the [CLI]({{< prelref "/docs/reference/cli" >}}) and the [programming model]({{< prelref "/docs/intro/concepts/programming-model" >}}).

The key-value pairs for any given stack are stored in [your project's stack settings file]({{< prelref "project#stack-settings-file" >}}), which is automatically named `Pulumi.<stack-name>.yaml`. You can typically ignore this file, although you may want to check it in and version it with your project source code.

## Configuration {#config-stack}

You can use both the CLI and the programming model for your Pulumi configuration.

* The CLI offers a `config` command with `set` and `get` subcommands for managing key-value pairs.
* The programming model offers a `Config` object with various getters and setters for retrieving values.

> All shell environment variables are passed to the running program and can be accessed using standard runtime APIs, such as `process.env` in Node.js and `os.environ` in Python, which can also be used for dynamic behavior. Configuration is preferable, however, because it is designed for multi-stack collaborative scenarios.

### Configuration Keys

Configuration keys use the format `[<namespace>:]<key-name>`, with a colon delimiting the optional namespace and the actual key name. In cases where a simple name without a colon is used, Pulumi automatically uses the current [project name]({{< prelref "project#project-name" >}}) from `Pulumi.yaml` as the namespace.

As an example, this capability allows the AWS package to accept a configuration value for `aws:region` without conflicting with other packages using the common key name `region`. It also allows [custom components]({{< prelref "./programming-model#components" >}}) to define their own key spaces without risk of conflicting with other components, packages, or projects.

### Setting and Getting Configuration Values

The `pulumi config` CLI command can get, set, or list configuration key-value pairs in your current project stack:

* `pulumi config set <key> [value]` sets a configuration entry `<key>` to `[value]`.
* `pulumi config get <key>` gets an existing configuration value with the key `<key>`.
* `pulumi config` gets all configuration key-value pairs in the current stack (as JSON if `--json` is passed).

> **Note:** When using the `config set` command, any existing values for `<key>` will be overridden without warning.

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

### Encrypted Secrets {#secrets}

Some configuration data is sensitive, such as database passwords or service tokens. For such cases, passing the `--secret` flag to the `config set` command encrypts the data and stores the resulting ciphertext instead of plaintext.

> By default, the CLI uses a per-stack encryption key managed by the Pulumi Service, and a per-value salt, to encrypt values. To use an alternative encryption provider, refer to [Configuring Secrets Encryption](#configuring-secrets-encryption).

For example, this command sets a configuration variable named `dbPassword` to the plaintext value `S3cr37`:

```bash
$ pulumi config set --secret dbPassword S3cr37
```

If we list the configuration for our stack, the plaintext value for `dbPassword` will not be printed:

```bash
$ pulumi config
KEY                        VALUE
aws:region                 us-west-1
dbPassword                 ********
```

Similarly, if our program attempts to print the value of `dbPassword` to the console---either intentionally or accidentally---Pulumi will mask it out:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
var pulumi = require("@pulumi/pulumi");
var config = new pulumi.Config();
console.log("Password: " + config.require("dbPassword"));
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
const config = new pulumi.Config();
console.log(`Password: ${config.require("dbPassword")}`);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
config = pulumi.Config()
print('Password: %s'.format(config.require('dbPassword')))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
c := config.New(ctx, "")
fmt.Println("Password: "+c.Require("dbPassword"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var config = new Pulumi.Config();
Console.WriteLine($"Password: {config.Require("dbPassword")}");
```

{{% /choosable %}}

{{< /chooser >}}

Running this program yields the following result:

```bash
$ pulumi up
Password: [secret]
```

> By default, configuration values are saved in plaintext. To explicitly denote a plaintext or unencrypted configuration value, pass the `--plaintext` flag: `$ pulumi config set --plaintext aws:region us-west-2`. This can be used to indicate that you did not want an encrypted secret.

## Using Configuration and Secrets in Code

To access configuration or secret values for your package, project, or component, use the `pulumi.Config` type. This type offers a collection of getters and setters for retrieving configuration values of various types by their key.

To begin, allocate an instance of the `pulumi.Config` object. Its constructor takes an optional namespace for all configuration keys being read back. Similar rules to the CLI usage apply here, in that if you omit the namespace argument, the current project is used. This is the common case for project configuration but is not what you want for packages and components which need their own isolated configuration.

For example, assume the following configuration values have been set:

```bash
$ pulumi config set name BroomeLLC             # set a plaintext value
$ pulumi config set --secret dbPassword S3cr37 # set an encrypted secret value
```

Use the following code to access these configuration values in your Pulumi program:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
var pulumi = require("@pulumi/pulumi");

var config = new pulumi.Config();

var name = config.require("name");
var dbPassword = config.requireSecret("dbPassword");
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();

const name = config.require("name");
const dbPassword = config.requireSecret("dbPassword");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi

config = pulumi.Config()

print(config.require('name'))
print(config.require_secret('dbPassword'))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
c := config.New(ctx, "")

name := c.Require("name")
dbPassword := c.Require("dbPassword")
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;
using Pulumi;

class MyStack : Stack
{
    public MyStack()
    {
        var config = new Config();

        var name = config.Require("name");
        var dbPassword = config.RequireSecret("dbPassword");
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

In this example, we have read back the `name` and `dbPassword` configuration variables programmatically. The `name` is just the string `BroomeLLC`, while the `dbPassword` is a secret output value that is encrypted.

> Notice the keys used above have no namespaces, both in the CLI gestures and in the `pulumi.Config` constructor. This means they have taken our project name as the default namespace. We could have specified this explicitly, as in `pulumi config set broome-proj:name BroomeLLC` and `new pulumi.Config("broome-proj")`.

For more advanced details of interacting with configuration and secrets, refer to the
[Programming Model documentation]({{< prelref "programming-model" >}}).

### A Warning: Using Secrets in Code

On `pulumi up`, secret values are decrypted and made available in plaintext at runtime. These may be read through any of the standard `pulumi.Config` getters shown above. While it is possible to read a secret using the ordinary non-secret getters, this is almost certainly not what you want. Use the secret variants of the configuration APIs instead, since this ensures that all transitive uses of that secret are themselves also marked as secrets.

## Structured Configuration

Structured configuration is also supported and can be set using `pulumi config set` and the `--path` flag. When `--path` is used, it indicates the config key contains a path of where to store the value in an object.

For example:

```bash
$ pulumi config set --path data.active true
$ pulumi config set --path data.nums[0] 1
$ pulumi config set --path data.nums[1] 2
$ pulumi config set --path data.nums[2] 3
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
print(f"Active: ${data.active}")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
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

Secrets within structured config are also supported. Consider a list of endpoints, each having a `url` and `token` property. The `token` value could be stored as a secret:

```bash
$ pulumi config set --path endpoints[0].url https://example.com
$ pulumi config set --path --secret endpoints[0].token accesstokenvalue
```

## Configuring Secrets Encryption

The Pulumi Service automatically manages per-stack encryption keys on your behalf. Anytime you encrypt a value using `--secret` or by programmatically wrapping it as a secret at runtime, a secure protocol is used between the CLI and Pulumi Service that ensures secret data is encrypted in transit, at rest, and physically anywhere it gets stored. For more details about the concept of state files and backends, refer to [State]({{< prelref "state" >}}).

The default encryption mechanism may be insufficient in the following scenarios:

1. If you are using the Pulumi CLI independent of the Pulumi Service---either in local mode, or by using one of the
   available backend plugins (such as those that store state in AWS S3, Azure Blob Store, or Google Object Storage).

2. If your team already has a preferred cloud encryption provider that you would like to use.

In both cases, you can continue using secrets management as described above, but instruct Pulumi to use an alternative encryption provider.

### Initializing a Stack with Alternative Encryption

To specify an alternative encryption provider, specify it at stack initialization time:

```
$ pulumi stack init <name> --secrets-provider="<provider>://<provider-settings>"
```

After doing so, all encryption operations for your stack will use the custom provider settings. The `<provider>` and `<provider-settings>` are specific to your chosen encryption provider. See below for the available providers and their options.

> Pulumi uses the Go Cloud Development Kit to implement pluggable secrets providers. In the event configuration or authentication options below do not work, [the Go CDK documentation](https://gocloud.dev/howto/secrets/) can be consulted for debugging information.

### Available Encryption Providers

Pulumi supports the following encryption providers:

* `awskms`: [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
* `azurekeyvault`: [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
* `gcpkms`: [Google Cloud Key Management Service (KMS)](https://cloud.google.com/kms/)
* `hashivault`: [HashiCorp Vault Transit Secrets Engine](https://www.vaultproject.io/docs/secrets/transit/index.html)

Each provider has its own unique `<provider-settings>` and authentication mechanisms.

#### AWS Key Management Service (KMS)

The `awskms` provider uses an existing KMS key in your AWS account for encryption. This key can be specified using one of three approaches:

1. By ID: `awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1`.
2. By alias: `awskms://alias/ExampleAlias?region=us-east-1`.
3. By ARN: `awskms://arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34bc-56ef-1234567890ab?region=us-east-1`.

For example, this configures a stack to use an AWS KMS key with ID `1234abcd-12ab-34cd-56ef-1234567890ab`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"
```

If you have previously configured the AWS CLI, the same credentials will be used. These can also be overridden using the standard `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables. For more options, refer to the [AWS Go SDK documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/).

#### Azure Key Vault

The `azurekeyvalue` provider uses an Azure Key Vault key for encryption. This key is specified using an [Azure Key object identifier](https://docs.microsoft.com/en-us/azure/key-vault/about-keys-secrets-and-certificates), which includes both your key vault's name and the key to use: `azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname`.

For example, this configures a stack to use an Azure Key Vault key named `payroll` in vault `acmecorpsec`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="azurekeyvault://acmecorpvault.vault.azure.net/keys/payroll"
```

By default, this provider will use [Azure Environment Authentication](https://docs.microsoft.com/en-us/azure/go/azure-sdk-go-authorization#use-environment-based-authentication). If you wish to login using the `az` command for authentication instead, set `AZURE_KEYVAULT_AUTH_VIA_CLI` to `true`.

#### Google Cloud Key Management Service (KMS)

The `gcpkms` provider uses an existing GCP KMS key for encryption. Specify the [key resource ID](https://cloud.google.com/kms/docs/object-hierarchy#key) for the key to use, which is a URL including your project, location, keyring, and key name: `gcpkms://projects/MYPROJECT/locations/MYLOCATION/keyRings/MYKEYRING/cryptoKeys/MYKEY`.

For example, this configures a stack to use a GCP KMS key `payroll` in project `acmecorpsec`, location `us-west1`, and key ring named `prod`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="gcpkms://projects//locations/us-west1/keyRings/acmecorpsec/cryptoKeys/payroll"
```

This provider will use your GCP Application Default Credentials. If you've previously configured the `gcloud` CLI, the same credentials will be used for authentication. For alternative configuration mechanisms, refer to [Setting Up Authentication for Server to Server Production Applications
](https://cloud.google.com/docs/authentication/production).

#### HashiCorp Vault Transit Secrets Engine

The `hashivault` provider uses Vault's Transit Secrets Engine to encrypt and decrypt information. You only need to pass a key name for the provider setting: `hashivault://mykey`. The Vault server endpoint and authentication token to use are provided with the `VAULT_SERVER_URL` and `VAULT_SERVER_TOKEN`, respectively.

For example, this configures a stack to use a HashiCorp Vault transit key named `payroll`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="hashivault://payroll"
```
