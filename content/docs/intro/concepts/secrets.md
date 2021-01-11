---
title: "Handling Secrets"
meta_desc: This page provides an overview of how Pulumi manages sensitive configuration data.
menu:
  intro:
    parent: concepts
    weight: 8
---

All resource input and output values are recorded as [`state`]({{< relref "/docs/intro/concepts/state" >}}), and are stored in the Pulumi Service, a file, or a pluggable provider that you choose. These raw values are usually just server names, configuration settings, and so on. In some cases, however, these values contain sensitive data, such as database passwords or service tokens.

The Pulumi Service always transmits and stores entire state files securely; however, Pulumi also supports encrypting specific values as “secrets” for extra protection. Encryption ensures that these values never appear as plaintext in your state file. By default, the encryption method uses automatic, per-stack encryption keys provided by the Pulumi Service or you can use a [provider of your own choosing]({{< relref "#configuring-secrets-encryption" >}}) instead.

To encrypt a configuration setting before runtime, you can use the CLI command [`config set`]({{< relref "/docs/intro/concepts/config#configuration" >}}) command with a [`--secret`]({{< relref "#secrets" >}}) flag. You can also set a secret during runtime. Any [`Output<T>`]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) value can be marked secret. If an output is a secret, any computed values derived from it—such as those derived through an [`apply`]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) call —will also be marked secret. All these encrypted values are stored in your state file.

An [`Output<T>`]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) can be marked secret in a number of ways:

- By reading a secret from configuration using [`Config.get_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.get_secret" >}})  or [`Config.require_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.require_secret" >}}).
- By creating a new secret value with [`Output.secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.secret" >}}), such as when generating a new random password.
- By marking a resource as having secret properties using [`additionalSecretOutputs`]({{< relref "/docs/intro/concepts/inputs-outputs" >}}).
- By computing a secret value by using [`apply`]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) or [`Output.all`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.all" >}}) with another secret value.

As soon as an `Output<T>` is marked secret, the Pulumi engine will encrypt it wherever it is stored.

{{% notes "info" %}}
Inside of an `apply` or `Output.all` call, your secret is decrypted into plaintext for use within the callback. It is up to your program to treat this value sensitively and only pass the plaintext value to code that you trust.
{{% /notes %}}

## Programmatically Creating Secrets

There are two ways to programmatically create secret values:

{{< chooser language "javascript,typescript,python,go,csharp" >}}
{{% choosable language javascript %}}

- Using [`getSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}) or [`requireSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}) when reading a value from config.
- Calling [`pulumi.secret(value)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#secret" >}}) to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language typescript %}}

- Using [`getSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret" >}}) or [`requireSecret(key)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret" >}}) when reading a value from config.
- Calling [`pulumi.secret(value)`]({{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi#secret" >}}) to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language python %}}

- Using [`get_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.get_secret" >}}) or [`require_secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Config.require_secret" >}}) when reading a value from config.
- Calling [`Output.secret`]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.secret" >}}) to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language go %}}

- Using `config.GetSecret(key)` or `config.RequireSecret(key)` when reading a value from config.
- Calling `pulumi.ToSecret(value)` to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language csharp %}}

- Using `Config.GetSecret(key)` or `Config.RequireSecret(key)` when reading a value from config.
- Calling `Output.CreateSecret(value)` to construct a secret from an existing value.

{{% /choosable %}}
{{< /chooser >}}

As an example, let’s create an AWS Parameter Store secure value. Parameter Store is an AWS service that stores strings. Those strings can either be secret or not. To create an encrypted value, we need to pass an argument to initialize the store’s `value` property. Unfortunately, the obvious thing to do —passing a raw, unencrypted value— means that the value is also stored in the Pulumi state, unencrypted so we need to ensure that the value is a secret:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const cfg = new pulumi.Config()
const param = new aws.ssm.Parameter("a-secret-param", {
    type: "SecureString",
    value: cfg.requireSecret("my-secret-value"),
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const cfg = new pulumi.Config()
const param = new aws.ssm.Parameter("a-secret-param", {
    type: "SecureString",
    value: cfg.requireSecret("my-secret-value"),
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
cfg = pulumi.Config()
param = ssm.Parameter("a-secret-param",
    type="SecureString",
    value=cfg.require_secret("my-secret-value"))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/ssm"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        cfg := config.New(ctx, "")
        param, err := ssm.NewParameter(ctx, "a-secret-param", &ssm.ParameterArgs{
            Type:  "SecureString",
            Value: cfg.RequireSecret("my-secret-value"),
        })
        if err != nil {
            return err
        }
        return nil
    }
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var cfg = new Pulumi.Config()
var param = new Aws.Ssm.Parameter("a-secret-param", new Aws.Ssm.ParameterArgs
{
    type = pulumi.String("SecureString"),
    value = cfg.RequireSecret("my-secret-value"),
});
```

{{% /choosable %}}

{{< /chooser >}}

The `Parameter` resource’s `value` property is encrypted in the Pulumi state file.

Pulumi tracks the transitive use of secrets, so that your secret won’t end up accidentally leaking into the state file. Tracking includes automatically marking data generated from secret inputs as secret themselves, as well as fully encrypting any resource properties that include secrets in them.

## How Secrets Relate to Outputs

Secrets have the same type, `Output<T>`, as do unencrypted resource outputs. The difference is that they are marked internally as needing encryption before persisting in the state file. When you combine an existing output that is marked as a secret using `apply`  or `Output.all`, the resulting output is also marked as a secret.

An `apply`’s callback is given the plaintext value of the underlying secret. Although Pulumi ensures that the value returned from an `apply` on a secret is also marked as secret, Pulumi cannot guarantee that the `apply` callback itself will not expose the secret value —for instance, by explicitly printing the value to the console or saving it to a file.

{{% notes "warning" %}}
Be careful that you do not pass this plaintext value to code that might expose it.
{{% /notes %}}

## Explicitly Marking Resource Outputs as Secrets

It is possible to mark resource outputs as containing secrets. In this case, Pulumi will automatically treat those outputs as secrets and encrypt them in the state file and anywhere they flow to. To do so, use the [`additional secret outputs`]({{< relref "/docs/intro/concepts/resources#additionalsecretoutputs" >}}) option.

## Encrypted Secrets in Configuration Data {#secrets}

Some configuration data is sensitive, such as database passwords or service tokens. For such cases, passing the `--secret` flag to the `config set` command encrypts the data and stores the resulting ciphertext instead of plaintext.

{{% notes "info" %}}
By default, the Pulumi CLI uses a per-stack encryption key managed by the Pulumi Service, and a per-value salt, to encrypt values. To use an alternative encryption provider, refer to [Configuring Secrets Encryption]({{< relref "#configuring-secrets-encryption" >}}).
{{% /notes %}}

For example, this command sets a configuration variable named `dbPassword` to the plaintext value `S3cr37`:

```bash
$ pulumi config set --secret dbPassword S3cr37
```

If we list the configuration for our stack, the plaintext value for `dbPassword` will not be printed:

```bash
$ pulumi config
KEY                        VALUE
aws:region                 us-west-1
dbPassword                 [secret]
```

Similarly, if our program attempts to print the value of `dbPassword` to the console-either intentionally or accidentally-Pulumi will mask it out:

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
print('Password: {}'.format(config.require('dbPassword')))
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

By default, configuration values are saved in plaintext. To explicitly denote a plaintext or unencrypted configuration value, pass the `--plaintext` flag. This flag can be used to indicate that you did not want an encrypted secret.

```bash
$ pulumi config set --plaintext aws:region us-west-2
```

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
package main

import (
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi/config"
)
func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        c := config.New(ctx, "")

        name := c.Require("name")
        dbPassword := c.RequireSecret("dbPassword")
    }
}
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

Notice the keys used above have no namespaces, both in the CLI gestures and in the `pulumi.Config` constructor. This means they have taken our project name as the default namespace. We could have specified this explicitly, as in `pulumi config set broome-proj:name BroomeLLC` and `new pulumi.Config("broome-proj")`.

Secrets within structured config are also supported. Consider a list of endpoints, each having a `url` and `token` property. The `token` value could be stored as a secret:

```bash
$ pulumi config set --path endpoints[0].url https://example.com
$ pulumi config set --path --secret endpoints[0].token accesstokenvalue
```

### A Warning: Using Secrets in Code

On `pulumi up`, secret values are decrypted and made available in plaintext at runtime. These may be read through any of the standard `pulumi.Config` getters shown above. While it is possible to read a secret using the ordinary non-secret getters, this is almost certainly not what you want. Use the secret variants of the configuration APIs instead, since this ensures that all transitive uses of that secret are themselves also marked as secrets.

## Configuring Secrets Encryption

The Pulumi Service automatically manages per-stack encryption keys on your behalf. Anytime you encrypt a value using `--secret` or by programmatically wrapping it as a secret at runtime, a secure protocol is used between the CLI and Pulumi Service that ensures secret data is encrypted in transit, at rest, and physically anywhere it gets stored. For more details about the concept of state files and backends, refer to [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).

The default encryption mechanism may be insufficient in the following scenarios:

1. If you are using the Pulumi CLI independent of the Pulumi Service-either in local mode, or by using one of the
   available backend plugins (such as those that store state in AWS S3, Azure Blob Store, or Google Object Storage).

2. If your team already has a preferred cloud encryption provider that you would like to use.

In both cases, you can continue using secrets management as described above, but instruct Pulumi to use an alternative encryption provider.

### Initializing a Stack with Alternative Encryption

To specify an alternative encryption provider, specify it at stack initialization time:

```
$ pulumi stack init <name> --secrets-provider="<provider>://<provider-settings>"
```

After doing so, all encryption operations for your stack will use the custom provider settings. The `<provider>` and `<provider-settings>` are specific to your chosen encryption provider. See below for the available providers and their options.

Pulumi uses the Go Cloud Development Kit to implement pluggable secrets providers. In the event configuration or authentication options below do not work, the [Go CDK documentation](https://gocloud.dev/howto/secrets/) can be consulted for debugging information.

### Available Encryption Providers

Pulumi supports the following encryption providers:

- `awskms`: [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- `azurekeyvault`: [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
- `gcpkms`: [Google Cloud Key Management Service (KMS)](https://cloud.google.com/kms/)
- `hashivault`: [HashiCorp Vault Transit Secrets Engine](https://www.vaultproject.io/docs/secrets/transit/index.html)

Each provider has its own unique `<provider-settings>` and authentication mechanisms.

#### AWS Key Management Service (KMS)

The `awskms` provider uses an existing KMS key in your AWS account for encryption. This key can be specified using one of three approaches:

1. By ID: `awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1`.
2. By alias: `awskms://alias/ExampleAlias?region=us-east-1`.
3. By ARN: `awskms:///arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34bc-56ef-1234567890ab?region=us-east-1`.

For example, this configures a stack to use an AWS KMS key with ID `1234abcd-12ab-34cd-56ef-1234567890ab`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"
```

If you have previously configured the AWS CLI, the same credentials will be used. These can also be overridden using the standard `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables. For more options, refer to the [AWS Go SDK documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/).

#### Azure Key Vault

The `azurekeyvault` provider uses an Azure Key Vault key for encryption. This key is specified using an [Azure Key object identifier](https://docs.microsoft.com/en-us/azure/key-vault/about-keys-secrets-and-certificates), which includes both your key vault's name and the key to use: `azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname`.

For example, this configures a stack to use an Azure Key Vault key named `payroll` in vault `acmecorpsec`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="azurekeyvault://acmecorpsec.vault.azure.net/keys/payroll"
```

By default, this provider will use [Azure Environment Authentication](https://docs.microsoft.com/en-us/azure/go/azure-sdk-go-authorization#use-environment-based-authentication). If you wish to login using the `az` command for authentication instead, set `AZURE_KEYVAULT_AUTH_VIA_CLI` to `true`.

#### Google Cloud Key Management Service (KMS)

The `gcpkms` provider uses an existing GCP KMS key for encryption. Specify the [key resource ID](https://cloud.google.com/kms/docs/object-hierarchy#key) for the key to use, which is a URL including your project, location, keyring, and key name: `gcpkms://projects/MYPROJECT/locations/MYLOCATION/keyRings/MYKEYRING/cryptoKeys/MYKEY`.

For example, this configures a stack to use a GCP KMS key `payroll` in project `acmecorpsec`, location `us-west1`, and key ring named `prod`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="gcpkms://projects//locations/us-west1/keyRings/acmecorpsec/cryptoKeys/payroll"
```

This provider will use your Google Cloud Application Default Credentials. If you've previously configured the `gcloud` CLI, the same credentials will be used for authentication. For alternative configuration mechanisms, refer to [Authenticating as a service account](https://cloud.google.com/docs/authentication/production).

#### HashiCorp Vault Transit Secrets Engine

The `hashivault` provider uses Vault's Transit Secrets Engine to encrypt and decrypt information. You only need to pass a key name for the provider setting: `hashivault://mykey`. The Vault server endpoint and authentication token to use are provided with the `VAULT_SERVER_URL` and `VAULT_SERVER_TOKEN`, respectively.

For example, this configures a stack to use a HashiCorp Vault transit key named `payroll`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="hashivault://payroll"
```

### Changing the Secrets Provider for a Stack

To change the secrets provider for an existing stack use the [`pulumi stack change-secrets-provider`]({{< relref "/docs/reference/cli/pulumi_stack_change-secrets-provider" >}}) command.

```bash
$ pulumi stack change-secrets-provider "<secrets-provider>"
```

This will change the encrypted secrets in the provider configuration and the stack's state file to use the new secrets provider.
The [supported secrets providers]({{< relref "/docs/reference/cli/pulumi_stack_init" >}}) are:

- `default`
- `passphrase`
- `awskms`
- `azurekeyvault`
- `gcpkms`
- `hashivault`

After the provider has been changed, you should be able to run `pulumi preview` and see no proposed changes.  Your configuration secrets
and state files are now encrypted using the new secrets provider.
