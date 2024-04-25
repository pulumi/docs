---
title_tag: "Secrets | Pulumi Concepts"
meta_desc: This page provides an overview of how Pulumi manages sensitive configuration data using secrets.
title: Secrets
h1: Secrets
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 7
aliases:
- /docs/intro/concepts/secrets/
- /secrets/
---

All resource input and output values are recorded as stack [_state_](/docs/concepts/state) and stored in Pulumi Cloud, in a state file, or in your self-managed [backend](/docs/concepts/state/) of choice. These values are usually just plain-text strings, such as configuration settings, computed URLs, or resource identifiers. Sometimes, however, these values contain sensitive data, such as database passwords or service tokens, that must be handled carefully and protected from exposure.

Pulumi Cloud transmits and stores entire state files securely, but Pulumi also supports encrypting individual values as _secrets_ for additional protection. Encryption ensures that these values never appear as plain text in your state file. By default, the encryption method uses automatic, per-stack encryption keys provided by Pulumi Cloud, but you can also use a [provider of your own choosing](#configuring-secrets-encryption) instead.

{{% notes %}}
The Pulumi CLI **never** transmits your cloud credentials to Pulumi Cloud.
{{% /notes %}}

To encrypt a configuration setting before runtime, use the [`pulumi config set`](/docs/concepts/config#configuration) CLI command with a [`--secret`](#secrets) flag. You can also declare secrets at runtime; any [output](/docs/concepts/inputs-outputs/#outputs) value can also be marked secret. If an output is a secret, any computed values derived from it, such as those derived from a call to [`apply`](/docs/concepts/inputs-outputs/#apply), will also be marked secret. All these of encrypted values are stored as ciphertext in your state file.

An output can be marked secret in a number of ways:

- By reading a secret from configuration using {{< pulumi-config-getsecret >}} or {{< pulumi-config-requiresecret >}}.
- By creating a new secret value with {{< pulumi-secret-new >}}, such as when generating a new random password.
- By marking a resource as having secret properties using [`additionalSecretOutputs`](/docs/concepts/inputs-outputs).
- By computing a secret value by using [`apply`](/docs/concepts/inputs-outputs/#apply) or {{< pulumi-all >}} with another secret value.

As soon as an output is marked secret, the Pulumi engine will encrypt it wherever it is stored.

{{% notes "info" %}}
Note that when using `apply` or `Output.all`, secrets are decrypted into plain text for use within the callback handler. It is up to your program to treat this value sensitively and only pass the plain-text value to code that you trust.
{{% /notes %}}

## Creating secrets programmatically

There are two ways to programmatically create secret values:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

- Using [`getSecret(key)`](/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret) or [`requireSecret(key)`](/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret) when reading a value from config.
- Calling [`pulumi.secret(value)`](/docs/reference/pkg/nodejs/pulumi/pulumi#secret) to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language typescript %}}

- Using [`getSecret(key)`](/docs/reference/pkg/nodejs/pulumi/pulumi#Config-getSecret) or [`requireSecret(key)`](/docs/reference/pkg/nodejs/pulumi/pulumi#Config-requireSecret) when reading a value from config.
- Calling [`pulumi.secret(value)`](/docs/reference/pkg/nodejs/pulumi/pulumi#secret) to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language python %}}

- Using [`get_secret`](/docs/reference/pkg/python/pulumi/#pulumi.Config.get_secret) or [`require_secret`](/docs/reference/pkg/python/pulumi/#pulumi.Config.require_secret) when reading a value from config.
- Calling [`Output.secret`](/docs/reference/pkg/python/pulumi/#pulumi.Output.secret) to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language go %}}

- Using `config.GetSecret(key)` or `config.RequireSecret(key)` when reading a value from config.
- Calling `pulumi.ToSecret(value)` to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language csharp %}}

- Using `Config.GetSecret(key)` or `Config.RequireSecret(key)` when reading a value from config.
- Calling `Output.CreateSecret(value)` to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language java %}}

- Using `ctx.config().getSecret(key)` or `ctx.config().requireSecret(key)` when reading a value from config.
- Calling `Output.of(value).asSecret()` to construct a secret from an existing value.

{{% /choosable %}}
{{% choosable language yaml %}}

- Setting `configuration.${KEY}.Secret: true` when reading a value from the config.
- Calling `Fn::Secret` to construct a secret from an existing value.

{{% /choosable %}}

{{< /chooser >}}

As an example, let’s create an AWS Parameter Store secure value. Parameter Store is an AWS service that stores strings. Those strings can either be secret or not. To create an encrypted value, we need to pass an argument to initialize the store’s `value` property. Unfortunately, the obvious thing to do —passing a raw, unencrypted value— means that the value is also stored in the Pulumi state, unencrypted so we need to ensure that the value is a secret:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
    "github.com/pulumi/pulumi-aws/sdk/v4/go/aws/ssm"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
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
{{% choosable language java %}}

```java
var config = ctx.config();
var param = new com.pulumi.aws.ssm.Parameter("a-secret-param",
    com.pulumi.aws.ssm.ParameterArgs.builder()
    .type("SecureString")
    .value(config.requireSecret("my-secret-value"))
    .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
configuration:
  mySecretValue:
    secret: true

resources:
  param:
    type: aws:ssm:Parameter
    properties:
      type: SecureString
      value: mySecretValue
```

{{% /choosable %}}

{{< /chooser >}}

The `Parameter` resource’s `value` property is encrypted in the Pulumi state file.

Pulumi tracks the transitive use of secrets, so that your secret won’t end up accidentally leaking into the state file. Tracking includes automatically marking data generated from secret inputs as secret themselves, as well as fully encrypting any resource properties that include secrets in them.

## How secrets relate to outputs

Secrets have the same type, `Output<T>`, as unencrypted resource outputs. The difference is that they are marked internally as needing encryption before persisting in the state file. When you combine an existing output that is marked as a secret using `apply`  or `Output.all`, the resulting output is also marked as a secret.

An `apply`’s callback is given the plain-text value of the underlying secret. Although Pulumi ensures that the value returned from an `apply` on a secret is also marked as secret, Pulumi cannot guarantee that the `apply` callback itself will not expose the secret value —for instance, by explicitly printing the value to the console or saving it to a file.

{{% notes "warning" %}}
Be careful that you do not pass this plain-text value to code that might expose it.
{{% /notes %}}

## Explicitly marking resource outputs as secrets

It is possible to mark resource outputs as containing secrets. In this case, Pulumi will automatically treat those outputs as secrets and encrypt them in the state file and anywhere they flow to. To do so, use the [`additional secret outputs`](/docs/concepts/resources#additionalsecretoutputs) option.

## Encrypted secrets in configuration data {#secrets}

Some configuration data is sensitive, such as database passwords or service tokens. For such cases, passing the `--secret` flag to the `config set` command encrypts the data and stores the resulting ciphertext instead of plain text.

{{% notes "info" %}}
By default, the Pulumi CLI uses a per-stack encryption key managed by Pulumi Cloud, and a per-value salt, to encrypt values. To use an alternative encryption provider, refer to [Configuring Secrets Encryption](#configuring-secrets-encryption).
{{% /notes %}}

For example, this command sets a configuration variable named `dbPassword` to the plain-text value `S3cr37`:

```bash
$ pulumi config set --secret dbPassword S3cr37
```

If we list the configuration for our stack, the plain-text value for `dbPassword` will not be printed:

```bash
$ pulumi config
KEY                        VALUE
aws:region                 us-west-1
dbPassword                 [secret]
```

Similarly, if our program attempts to print the value of `dbPassword` to the console-either intentionally or accidentally-Pulumi will mask it out:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
{{% choosable language java %}}

```java
var config = ctx.config();
ctx.log().info(String.format("Password: %s", config.require("dbPassword")));
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  dbPassword:
    type: string
    secret: true
outputs:
    password: ${dbPassword}
```

{{% /choosable %}}

{{< /chooser >}}

Running this program yields the following result:

```bash
$ pulumi up
Password: [secret]
```

By default, configuration values are saved in plain text. To explicitly denote a plain text or unencrypted configuration value, pass the `--plaintext` flag. This flag can be used to indicate that you did not want an encrypted secret.

```bash
$ pulumi config set --plaintext aws:region us-west-2
```

## Using configuration and secrets in code

To access configuration or secret values for your package, project, or component, use the `pulumi.Config` type. This type offers a collection of getters and setters for retrieving configuration values of various types by their key.

To begin, allocate an instance of the `pulumi.Config` object. Its constructor takes an optional namespace for all configuration keys being read back. Similar rules to the CLI usage apply here, in that if you omit the namespace argument, the current project is used. This is the common case for project configuration but is not what you want for packages and components which need their own isolated configuration.

For example, assume the following configuration values have been set:

```bash
$ pulumi config set name BroomeLLC             # set a plain-text value
$ pulumi config set --secret dbPassword S3cr37 # set an encrypted secret value
```

Use the following code to access these configuration values in your Pulumi program:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
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
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Exports;
import com.pulumi.Pulumi;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var config = ctx.config();

        var name = config.require("name");
        var dbPassword = config.requireSecret("dbPassword");
    }
}
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
config:
  name:
    type: string
  dbPassword:
    type: string
    secret: true
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

{{% notes type="warning" %}}
Secret values are decrypted and made available in plain text to the program at runtime. These values may be read using any of the standard `pulumi.Config` getters shown above. While it is possible to read a secret using the ordinary non-secret getters, this is almost certainly not what you want. Use the secret variants of the configuration APIs instead, as this ensures that all transitive uses of that secret are themselves also marked as secrets.
{{% /notes %}}

## Configuring secrets encryption

Pulumi Cloud automatically manages per-stack encryption keys on your behalf. Anytime you encrypt a value using `--secret` or by programmatically wrapping it as a secret at runtime, a secure protocol is used between the CLI and Pulumi Cloud that ensures secret data is encrypted in transit, at rest, and physically anywhere it gets stored. For more details about the concept of state files and backends, refer to [State and Backends](/docs/concepts/state/).

The default encryption mechanism may be insufficient in the following scenarios:

1. If you are using the Pulumi CLI independent of Pulumi Cloud --- either in local mode, or by using one of the
   available backend plugins (such as those that store state in AWS S3, Azure Blob Store, or Google Object Storage).

2. If your team already has a preferred cloud encryption provider that you would like to use.

In both cases, you can continue using secrets management as described above, but instruct Pulumi to use an alternative encryption provider.

### Initializing a stack with alternative encryption

To specify an alternative encryption provider, specify it at stack initialization time:

```
$ pulumi stack init <name> --secrets-provider="<provider>://<provider-settings>"
```

After doing so, all encryption operations for your stack will use the custom provider settings. The `<provider>` and `<provider-settings>` are specific to your chosen encryption provider. See below for the available providers and their options.

Pulumi uses the Go Cloud Development Kit to implement pluggable secrets providers. In the event configuration or authentication options below do not work, the [Go CDK documentation](https://gocloud.dev/howto/secrets/) can be consulted for debugging information.

### Available encryption providers

Pulumi supports the following encryption providers:

- `awskms`: [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- `azurekeyvault`: [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
- `gcpkms`: [Google Cloud Key Management Service (KMS)](https://cloud.google.com/kms/)
- `hashivault`: [HashiCorp Vault Transit Secrets Engine](https://www.vaultproject.io/docs/secrets/transit)

Each provider has its own unique `<provider-settings>` and authentication mechanisms.

#### AWS Key Management Service (KMS)

The `awskms` provider uses an existing KMS key in your AWS account for encryption. This key can be specified using one of three approaches:

1. By ID: `awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1`.
1. By alias: `awskms://alias/ExampleAlias?region=us-east-1`.
1. By ARN: `awskms:///arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34bc-56ef-1234567890ab?region=us-east-1`.

For example, this configures a stack to use an AWS KMS key with ID `1234abcd-12ab-34cd-56ef-1234567890ab`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1"
```

If you have previously configured the AWS CLI, the same credentials will be used. These can also be overridden using the standard `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables. For more options, refer to the [AWS Go SDK documentation](https://docs.aws.amazon.com/sdk-for-go/api/aws/session/).

{{% notes "info" %}}
As of Pulumi CLI v3.33.1, instead of specifying the AWS Profile using the `AWS_PROFILE` environment variable, add `awssdk=v2` and `profile=` followed by the profile name to the query string.

1. By ID: `awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1&awssdk=v2&profile=dev`.
1. By alias: `awskms://alias/ExampleAlias?region=us-east-1&awssdk=v2&profile=qa`.
1. By ARN: `awskms:///arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34bc-56ef-1234567890ab?region=us-east-1&awssdk=v2&profile=prod`.
{{% /notes %}}
{{% notes "info" %}}
As of Pulumi CLI v3.41.1, this secrets backend supports [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) by setting `context_{key}={value}` in the query string.
Encryption context can be used in [IAM policies conditions](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-encryption-context) and it appears in Cloudtrail logs.

For example, take a look at `awskms://1234abcd-12ab-34cd-56ef-1234567890ab?region=us-east-1&awssdk=v2&profile=dev&context_project=myproject&context_environment=staging`.

The encryption context here is `{"project": "myproject", "environment": "staging"}`. Together with an appropriate IAM policy with conditions, one can grant some user permissions only to
encrypt/decrypt secrets for `staging` environment of the `myproject` project.
{{% /notes %}}

#### Azure Key Vault

The `azurekeyvault` provider uses an Azure Key Vault key for encryption. This key is specified using an [Azure Key object identifier](https://docs.microsoft.com/en-us/azure/key-vault/keys/about-keys), which includes both your key vault's name and the key to use: `azurekeyvault://mykeyvaultname.vault.azure.net/keys/mykeyname`.

For example, this configures a stack to use an Azure Key Vault key named `payroll` in vault `acmecorpsec`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="azurekeyvault://acmecorpsec.vault.azure.net/keys/payroll"
```

By default, this provider will use [Azure Environment Authentication](https://docs.microsoft.com/en-us/azure/go/azure-sdk-go-authorization#use-environment-based-authentication). If you wish to login using the `az` command for authentication instead, set `AZURE_KEYVAULT_AUTH_VIA_CLI` to `"true"` (using double quotes).

#### Google Cloud Key Management Service (KMS)

The `gcpkms` provider uses an existing Google Cloud KMS key for encryption. Specify the [key resource ID](https://cloud.google.com/kms/docs/object-hierarchy#key) for the key to use, which is a URL including your project, location, keyring, and key name: `gcpkms://projects/MYPROJECT/locations/MYLOCATION/keyRings/MYKEYRING/cryptoKeys/MYKEY`. The key's [purpose](https://cloud.google.com/kms/docs/algorithms#key_purposes) needs to be `ENCRYPT_DECRYPT`.

For example, this configures a stack to use a Google Cloud KMS key `payroll` in project `acmecorpsec`, location `us-west1`, and key ring named `prod`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="gcpkms://projects/acmecorpsec/locations/us-west1/keyRings/prod/cryptoKeys/payroll"
```

This provider will use your Google Cloud Application Default Credentials. If you've previously configured the `gcloud` CLI, the same credentials will be used for authentication. For alternative configuration mechanisms, refer to [Authenticating as a service account](https://cloud.google.com/docs/authentication/production).

#### HashiCorp Vault Transit Secrets Engine

The `hashivault` provider uses Vault's Transit Secrets Engine to encrypt and decrypt information. You only need to pass a key name for the provider setting: `hashivault://mykey`. The Vault server endpoint and authentication token to use are provided with the `VAULT_SERVER_URL` and `VAULT_SERVER_TOKEN`, respectively.

For example, this configures a stack to use a HashiCorp Vault transit key named `payroll`:

```bash
$ pulumi stack init my-stack \
    --secrets-provider="hashivault://payroll"
```

### Changing the secrets provider for a stack

To change the secrets provider for an existing stack use the [`pulumi stack change-secrets-provider`](/docs/cli/commands/pulumi_stack_change-secrets-provider) command.

```bash
$ pulumi stack change-secrets-provider "<secrets-provider>"
```

This will change the encrypted secrets in the provider configuration and the stack's state file to use the new secrets provider.
The [supported secrets providers](/docs/cli/commands/pulumi_stack_init/) are:

- `default`
- `passphrase`
- `awskms`
- `azurekeyvault`
- `gcpkms`
- `hashivault`

After the provider has been changed, you should be able to run `pulumi preview` and see no proposed changes.  Your configuration secrets
and state files are now encrypted using the new secrets provider.

## Committing configuration to source control {# search.keywords="checking version control"}

When you run `pulumi config set --secret` to generate a new Pulumi secret, the Pulumi CLI uses the stack's unique encryption key to encrypt the raw value and store the resulting ciphertext in the stack configuration file (`Pulumi.dev.yaml`, for example). If you opened this file in a text editor, you'd see that the contents would look something like this:

```yaml
config:
  myStack:somePlainTextItem: somePlainText
  myStack:someSecretItem:
    secure: AAABAIIlW0ewSuZ1FJxw/+Rpw6BNqTUvGJ30O8WkpL2hB4aPyS7UU68=
```

Decrypting this ciphertext requires the encryption key that was used to create it. For stacks managed with Pulumi Cloud, these keys are obtained automatically, but only for users with [read access](/docs/pulumi-cloud/projects-and-stacks/#stack-permissions) to the stack. For self-managed backends, the keys must be supplied by the user, either by providing the stack's current passphrase (when using the [`passphrase`](#changing-the-secrets-provider-for-a-stack) provider) or by authenticating with the stack's [encryption provider](#available-encryption-providers).

It's therefore considered safe and good practice to check these files into source control (including the `encryptionSalt`s used with the passphrase provider), as doing so allows you to version your code and configuration in tandem. If you'd prefer not to check in these files, however, you can easily rebuild them, using the most recently deployed configuration, with [`pulumi config refresh`](/docs/cli/commands/pulumi_config_refresh/).

## Managing secrets with Pulumi ESC environments

With Pulumi ESC, you can manage secrets wherever they live. Pulumi ESC provides a centralized abstraction in front of the most common secrets manager/vaults while providing security through RBAC and audit controls.

### Sharing secrets across multiple teams

You may have multiple teams that each own different secrets and manage their lifetimes, and choose to store them in various AWS secret manager secrets.

For example, let's say you have a centralized billing service team that manages your team's payment process API keys. They can have a `Billing` environment defined like this:

```yaml
values:
    aws:
        creds:
            fn::open::aws-login:
            oidc:
                duration: 1h
                roleArn: arn:aws:iam::************:role/billing-oidc
                sessionName: pulumi-environments-session
    team:
        secrets:
        fn::open::aws-secrets:
            region: us-west-2
            login: ${aws.creds}
            get:
                paymentApiKey:
                    secretId: production/paymentAPIKey
                backupPaymentAPIKey:
                    secretId: production/backupPaymentAPIKey
```

There could be another environment for the Subscription Management team, `Subscription_Management_Prod`, that imports the `Billing` environment.

```yaml
imports:
- Prod
- Billing
values:
    serviceName: Subscription Management
    numInstances: 3
    # more service specific values  here

    secrets:
        fn::open::aws-secrets:
            region: us-west-2
            login: ${aws.creds}
            get:
                dbPassword:
                    secretId: production/rdsPassword
```

We can use the command line to open this environment and access this secret, if access controls allow:

```bash
$ pulumi env open myorg/subscription_management_prod
```

Which should look like this:

```json
{
  "aws": {
    "creds": {
      "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
      "secretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
      "sessionToken": "eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2OTY1NzA3NTIsImV4cCI6MTcyODEwNjc1MiwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.yUSeKObQ29c6VHBdmOA4a35yW3SyhZ5DPiG96_u6Tvk"
    }
  },
  "secrets": {
    "backupPaymentAPIKey": "prod_3c88Pc8ZfdBdpa135DUEXAMPLE",
    "dbPassword": "correct horse battery staple",
    "paymentApiKey": "prod_4kcdWj8ZfdBfgjQea135DU00EXAMPLE"
  }
}
```

### Cross-cloud secrets

Imagine you have a cross-cloud product that leverages services in GCP and Azure, and you have to manage secrets to access those services in GCP Secrets Manager and in Azure KeyVault.  With Pulumi ESC, you can coalesce your secret access to a single entry point.

Here is an example environment config named `Cross_Cloud`:

```yaml
values:
    azure:
        login:
            fn::open::azure-login:
                clientId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
                tenantId: aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
                subscriptionId: /subscriptions/00000000-0000-0000-0000-000000000000
                oidc: true
    secrets:
        fn::open::azure-secrets:
            login: ${azure.login}
            vault: https://vault-name.vault.azure.net/type/name/version
            get:
                api-key:
                    name: api-key
                app-secret:
                    name: app-secret

    # GCP Provider examples
    gcp:
        login:
            fn::open::gcp-login:
                project: 123456789
                oidc:
                    workloadPoolId: pulumi-esc
                    providerId: pulumi-esc
                    serviceAccount: pulumi-esc@foo-bar-123456.iam.gserviceaccount.com
    secrets:
        fn::open::gcp-secrets:
            login: ${gcp.login}
            access:
                dbPassword:
                    name: db-key
```

Now stacks or other environments that import this environment will have access to the Azure and GCP secrets from one easy access point.

```bash
$ pulumi env open myorg/cross_cloud
```

Which should look like this:

```json
{
  "gcp": {
    "login": {
      // removed for brevity
    }
  },
  "azure": {
    "login": {
      // removed for brevity
    }
  },
  "secrets": {
    "api-key": "ZPUpfjKtY2PDWq3EnyVN",
    "app-secret": "vW62BqN9uewuoTtKJB2W3BCxUbHDXc",
    "dbPassword": "Rule-Danger-Gray-Dust-9"
  }
}
```
