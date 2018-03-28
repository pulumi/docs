---
title: "Configuration"
---

Often, your Pulumi program will need configuration values that change independently from the program itself. For example, you may want to use a different size of AWS EC2 instance depending on whether the program is deployed to a development or production stack. 

For these configuration values, you can use _stack settings_. Stack settings are defined in [`Pulumi.<stack-name>.yaml`] and are set via the `pulumi config set` command. 

## Defining and setting stack settings {#config-stack}

To add a new stack setting, use `pulumi config set <key> [value]`. 

Since [Pulumi components](./resource.html) can define configuration keys, you can use a namespace with the syntax  `namespace:key`. If a namespace is not specified, the [project name] defined in `Pulumi.yaml` is used. 

For example, if a project is named `broome-proj` and the active stack is `dev`, the following command adds the key  `broome-proj:name` to `Pulumi.dev.yaml`:

```
$ pulumi config set name BroomeLLC
warning: saved config key 'broome-proj:name' value 'BroomeLLC' as plaintext; re-run with --secret to encrypt the value instead
```

To specify a particular namespace, use `config set namespace:name`. For instance, the [AWS package](./aws.html) defines the required setting `region`, which is set via `aws:region`.

By default, configuration values are saved in plaintext. To explicitly save a setting as plaintext, use the `--plaintext` flag.

```bash
$ pulumi config set --plaintext aws:region us-west-2
```

If `[value]` is not specified, the CLI will prompt for it. Alternatively, the config value can be set from standard input, which is useful for multiline values or any value that must be escaped on the command line. 

```bash
$ cat my_key.pub | pulumi config set publicKey
```

> NOTE: When using the `config set` command, any existing values for `<key>` will be overridden without warning. 

### Encrypted configuration values

To add an encrypted stack setting, such as for configuration secrets, use the `--secret` flag. Secrets are encrypted with an encryption salt and passphrase. The encryption salt for each stack is stored in `Pulumi.<stack-name>.yaml`. The salt value is based on your passphrase, but is not itself a secret and can safely be stored in source control. The first time a passphrase is configured for a stack, the CLI prompts twice for its value. 

If you wish to change your passphrase, delete the config value for `encryptionsalt` in `Pulumi.<stack-name>.yaml` and delete your existing secure values. To avoid the interactive prompt, set the environment variable `PULUMI_CONFIG_PASSPHRASE`.

```
$ pulumi config set --secret secretValue S3cr37
Enter your passphrase to protect config/secrets: 
Re-enter your passphrase to confirm: 
```

### Stack settings and source control

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them in to source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings.

For stacks that are ephemeral or are used in "inner loop" development, the stack settings are typically not checked in to source control.

## Viewing stack settings

To view all settings for the currently selected stack, use `pulumi config`. To view the values of secrets, use the `--show-secrets` flag.

```
$ pulumi config
KEY                                              VALUE                                           
aws:region                                       us-west-1                                       
secretValue                                      ********                                        
```

```
$ pulumi config --show-secrets
Enter your passphrase to unlock config/secrets
    (set PULUMI_CONFIG_PASSPHRASE to remember): 
KEY                                              VALUE                                           
aws:region                                       us-west-1                                       
secretValue                                      S3cr37                                          
```

## Using configuration values in code

On `pulumi preview` and `pulumi update`, secret values are decrypted. If the the environment variable `PULUMI_CONFIG_PASSPHRASE` is not set, the CLI performs an interactive prompt.

Your Pulumi program can read any configuration value that is set via `pulumi config`. Since secret values are decrypted before your program is executed, secret and plaintext values are accessed the same way, through APIs specific to each language.

Additionally, all shell environment variables are passed to the running program and can be accessed via standard runtime APIs, such as `process.env` in Node.js and `os.environ` in Python.

#### JavaScript {#javascript}

In JavaScript, use `pulumi.Config` in the `@pulumi` namespace, passing in the configuration namespace. This is typically  the name defined in `Pulumi.yaml`.

```
pulumi config set name BroomeLLC              # set a plaintext value
pulumi config set --secret secretValue S3cr37 # set a secret value
```

```javascript
const pulumi = require("@pulumi/pulumi");

let config = new pulumi.Config("broome-proj"); // broome-proj is name defined in Pulumi.yaml

console.log(`Hello, ${config.require("name")}!`);	    // prints "BroomeLLC"
console.log(`Psst, ${config.require("secretValue")}`);  // prints "S3cr37"
```

#### Python

TODO add Python example

<!-- MARKDOWN LINKS -->

[`Pulumi.<stack-name>.yaml`]: ./project.html#stack-settings-file
[project name]: ./project.html#project-name
[AWS package]: ./aws.html
