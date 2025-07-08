---
title_tag: Stack Settings File Reference
meta_desc: Documentation of the settings that are valid for Pulumi stack configuration files (Pulumi.<stack-name>.yaml).
title: Stack settings file reference
h1: Pulumi stack settings file reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Stack settings file reference
        parent: iac-concepts-projects
        weight: 2
    concepts:
        parent: projects
        weight: 2

aliases:
- /docs/reference/stack-settings-file/
- /docs/concepts/projects/stack-settings-file/
---

Every Pulumi stack has a settings file named `Pulumi.<stack-name>.yaml` that contains configuration specific to that stack. This file typically resides in the root of the project directory and stores stack-specific configuration values, secrets metadata, and environment settings.

{{< notes type="info" >}}
Stack settings files are typically managed through Pulumi CLI commands such as [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set/) and [`pulumi config get`](/docs/iac/cli/commands/pulumi_config_get/). While you can edit these files directly, it's recommended to use the CLI commands as they handle encryption and validation properly.
{{< /notes >}}

The stack settings file must be named exactly `Pulumi.<stack-name>.yaml` where `<stack-name>` matches your stack name. For example, if your stack is named `dev`, the file would be `Pulumi.dev.yaml`. The file format must be YAML.

## Attributes

| Name | Required | Description |
| - | - | - |
| `secretsprovider` | optional | The secrets provider used for encrypting sensitive configuration values. |
| `encryptedkey` | optional | The KMS-encrypted ciphertext for the data key used for secrets encryption. Only used for cloud-based secrets providers. |
| `encryptionsalt` | optional | The stack's base64 encoded encryption salt. Only used for passphrase-based secrets providers. |
| `config` | optional | A map of configuration key-value pairs for the stack. |
| `environment` | optional | Environment definition or list of environments for Pulumi ESC integration. |

### `secretsprovider`

The `secretsprovider` attribute specifies which secrets provider to use for encrypting sensitive configuration values. Common values include:

- `default`: Uses the Pulumi Cloud's default encryption
- `passphrase`: Uses a local passphrase for encryption  
- `awskms://alias/my-key`: Uses AWS KMS with the specified key
- `azurekeyvault://vault-name/key-name`: Uses Azure Key Vault
- `gcpkms://projects/my-project/locations/us-central1/keyRings/my-ring/cryptoKeys/my-key`: Uses Google Cloud KMS
- `hashivault://my-secret-path`: Uses HashiCorp Vault

### `encryptedkey`

When using cloud-based secrets providers (like AWS KMS, Azure Key Vault, or Google Cloud KMS), this field contains the encrypted data encryption key. This field is automatically managed by Pulumi and should not be manually edited.

### `encryptionsalt`

When using the `passphrase` secrets provider, this field contains the base64-encoded salt used for key derivation. This field is automatically generated and managed by Pulumi when you first set up passphrase encryption.

### `config`

The `config` section contains all configuration key-value pairs for the stack. Configuration keys can be:

- **Project-namespaced**: Keys without a namespace (e.g., `name`, `instanceType`) that belong to your project
- **Provider-namespaced**: Keys with a provider namespace (e.g., `aws:region`, `azure:location`)

Configuration values can be:

- **Plain text**: Simple string, number, or boolean values
- **Encrypted secrets**: Values that are encrypted using the stack's secrets provider (marked with `secure:` prefix in the YAML)
- **Structured data**: Complex objects or arrays

### `environment`

The `environment` section enables Pulumi ESC (Environments, Secrets, and Configuration) integration. This can be:

- A **string**: Single environment name to import
- **Array of strings**: Multiple environment names to import  
- **Inline definition**: Complete environment definition with imports and values

## Configuration file location

By default, stack settings files are stored in the same directory as your `Pulumi.yaml` project file. You can change this location by setting the `stackConfigDir` attribute in your project file to specify a relative directory where stack configuration files should be stored.

## Security considerations

- **Secret values**: When you set configuration values marked as secrets (using `pulumi config set --secret`), they are encrypted in the file and safe to commit to version control
- **Version control**: It's recommended to check stack settings files into version control for team collaboration, especially for shared environments
- **Ephemeral stacks**: For temporary or ephemeral stacks, you may choose not to commit these files

## Example stack settings files

### Minimal stack settings file

```yaml
config:
  myproject:name: my-application
  aws:region: us-west-2
```

### Stack with encrypted secrets

```yaml
secretsprovider: default
config:
  myproject:name: my-application
  myproject:database-password:
    secure: AAABAJcNQDPX5IKQc3Tn[...encrypted...]
  aws:region: us-west-2
```

### Stack with passphrase encryption

```yaml
secretsprovider: passphrase
encryptionsalt: v1:BNJOCpOPGV4=:v1:9jpeMm7HcnK+6+Wt:gcfklR9vOw==
config:
  myproject:name: my-application  
  myproject:api-key:
    secure: v1:LToJ+3kqSG30mW3P:6F1Gm7QFBUwKOBPBz[...encrypted...]
  aws:region: us-west-2
```

### Stack with AWS KMS encryption

```yaml
secretsprovider: awskms://alias/pulumi-secrets
encryptedkey: AQECAHgFl1+CIJQc3Tn[...encrypted...]
config:
  myproject:name: my-application
  myproject:database-url:
    secure: AAABAHgFl1+CIJQc3T[...encrypted...]
  aws:region: us-west-2
```

### Stack with Pulumi ESC environment

```yaml
config:
  myproject:name: my-application
  aws:region: us-west-2
environment:
  - shared-config
  - database-config
```

### Stack with inline environment definition

```yaml
config:
  myproject:name: my-application
environment:
  imports:
    - shared-config
  values:
    database:
      host: db.example.com
      port: 5432
```

### Stack with structured configuration

```yaml
config:
  myproject:name: my-application
  myproject:database:
    host: db.example.com
    port: 5432
    ssl: true
  myproject:replicas: 3
  myproject:features:
    - authentication
    - logging
    - monitoring
  aws:region: us-west-2
```

## Related CLI commands

The following CLI commands are commonly used to manage stack settings files:

- [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set/): Set a configuration value
- [`pulumi config set --secret`](/docs/iac/cli/commands/pulumi_config_set/): Set an encrypted configuration value
- [`pulumi config get`](/docs/iac/cli/commands/pulumi_config_get/): Get a configuration value
- [`pulumi config`](/docs/iac/cli/commands/pulumi_config/): List all configuration values
- [`pulumi config rm`](/docs/iac/cli/commands/pulumi_config_rm/): Remove a configuration value
- [`pulumi stack export`](/docs/iac/cli/commands/pulumi_stack_export/): Export the entire stack state
- [`pulumi stack import`](/docs/iac/cli/commands/pulumi_stack_import/): Import stack state from a file

## See also

- [Configuration](/docs/iac/concepts/config/): Learn about Pulumi's configuration system
- [Secrets](/docs/iac/concepts/secrets/): Learn about managing secrets in Pulumi
- [Project file reference](/docs/iac/concepts/projects/project-file/): Learn about the Pulumi.yaml project file
- [Pulumi ESC](/docs/esc/): Learn about Pulumi's Environments, Secrets, and Configuration service
