---
title: "Configuration and Secrets"
expanded_url: /docs/intro/concepts/
menu:
  intro:
    parent: concepts
    weight: 7
---

Often, your Pulumi program will need configuration values that change independently from the program itself. For example, you may want to use a different size of AWS EC2 instance depending on whether the program is deployed to a development or production stack.

For these configuration values, you can use _stack settings_. Stack settings are defined in [`Pulumi.<stack-name>.yaml`] and are set via the `pulumi config set` command.

## Configuring Stacks {#config-stack}

To add a new configuration key/value pair, use `pulumi config set <key> [value]`.

Since [Pulumi components]({{< relref "./programming-model.md#components" >}}) can define configuration keys, you can use a namespace with the syntax  `namespace:key`. If a namespace is not specified, the [project name] defined in `Pulumi.yaml` is used.

For example, if a project is named `broome-proj` and the active stack is `dev`, the following command adds the key  `broome-proj:name` to `Pulumi.dev.yaml`:

```bash
$ pulumi config set name BroomeLLC
```

To specify a particular namespace, use `config set namespace:name`. For instance, the [AWS package]({{< relref "/docs/quickstart/aws" >}}) defines the required setting `region`, which is set via `aws:region`.

By default, configuration values are saved in plaintext. To explicitly save a setting as plaintext, use the `--plaintext` flag.

```bash
$ pulumi config set --plaintext aws:region us-west-2
```

If `[value]` is not specified, the CLI will prompt for it. Alternatively, the config value can be set from standard input, which is useful for multiline values or any value that must be escaped on the command line.

```bash
$ cat my_key.pub | pulumi config set publicKey
```

> NOTE: When using the `config set` command, any existing values for `<key>` will be overridden without warning.

## Encrypted Secrets {#secrets}

To add an encrypted stack setting, such as for configuration secrets, use the `--secret` flag. Secrets are encrypted using a unique stack key that is stored on pulumi.com. Pulumi first adds a random encryption salt, so if you use the same plaintext value for two different keys, you'll have two different ciphertext values stored in  `Pulumi.<stackname>.yaml`.

```bash
$ pulumi config set --secret secretValue S3cr37

$ pulumi config
KEY                                              VALUE
aws:region                                       us-west-1
secretValue                                      ********
```

## Source Control

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them in to source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings.

For stacks that are ephemeral or are used in "inner loop" development, the stack settings are typically not checked in to source control.

## Viewing Configuration

To view the active settings for the currently selected stack, use `pulumi config`. To view the values of secrets, use the `--show-secrets` flag.

```bash
$ pulumi config
KEY                                              VALUE
aws:region                                       us-west-1
secretValue                                      ********
```

```bash
$ pulumi config --show-secrets
KEY                                              VALUE
aws:region                                       us-west-1
secretValue                                      S3cr37
```

## Using Configuration in Code

On `pulumi up`, secret values are decrypted. Your Pulumi program can read any configuration value that is set via `pulumi config`. Since secret values are decrypted before your program is executed, secret and plaintext values are accessed the same way, through APIs specific to each language.

Additionally, all shell environment variables are passed to the running program and can be accessed via standard runtime APIs, such as `process.env` in Node.js and `os.environ` in Python.

To access configuration values, use `pulumi.Config` and specify the configuration namespace. This is generally the same as the project name defined in `Pulumi.yaml`.

For example, assume the following configuration values have been set:

```bash
$ pulumi config set name BroomeLLC              # set a plaintext value
$ pulumi config set --secret secretValue S3cr37 # set a secret value
```

Use the following code to access these configuration values in your Pulumi program.

{{< langchoose >}}

```javascript
var pulumi = require("@pulumi/pulumi");

var config = new pulumi.Config("broome-proj"); // broome-proj is name defined in Pulumi.yaml

console.log(config.require("name"));           // prints "BroomeLLC"
console.log(config.require("secretValue"));    // prints "S3cr37"
```

```typescript
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config("broome-proj"); // broome-proj is name defined in Pulumi.yaml

console.log(config.require("name"));           // prints "BroomeLLC"
console.log(config.require("secretValue"));    // prints "S3cr37"
```

```python
import pulumi

config = pulumi.Config('broome-proj')  # broome-proj is name defined in Pulumi.yaml

print(config.require('name'))          # prints "BroomeLLC"
print(config.require('secretValue'))   # prints "S3cr37"
```

```go
c := config.New(ctx, "broome-proj")

fmt.Println(c.Require("name"))        // prints "BroomeLLC"
fmt.Println(c.Require("secretValue")) // prints "S3cr37"
```

<!-- MARKDOWN LINKS -->

[`Pulumi.<stack-name>.yaml`]: {{< relref "project.md#stack-settings-file" >}}
[project name]: {{< relref "project.md#project-name" >}}
[AWS package]: {{< relref "/docs/quickstart/aws" >}}
