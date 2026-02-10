---
title: "New Provider Resource Option: Environment Variable Remapping"
date: 2026-02-12
draft: false
meta_desc: "Remap provider environment variables to custom keys using the new resource option, pulumi.EnvVarMappings"
meta_image: meta.png
authors:
    - guinevere-saenger
tags:
    - features
    - packages
schema_type: auto

# Optional: Social media promotional copy (for reference only, does not auto-post)
social:
    twitter:
    linkedin:
---

Pulumi is excited to introduce environment variable remapping as a provider resource option.
From Pulumi version 3.220.0, you can use the new `envVarMappings` resource option to redirect provider environment variables to custom keys.
This is useful when you need multiple Pulumi providers to use different values for the same environment variable.

<!--more-->

When configuring a Pulumi provider to authenticate against a cloud provider, there are two main options available.
You can set authentication values as secrets in your Pulumi.yaml config:

```bash
$ pulumi config set azure-native:clientSecret <clientSecret> --secret
```

Alternately, you can also use the terminal environment of where you're running your Pulumi commands:

```bash
$ export ARM_CLIENT_SECRET=1234567
```

Using environment variables in this manner is especially useful in CI environments, or when you'd rather not write that auth token to state, even encrypted.
But there's currently several use cases where this breaks down, due to the hard-coded nature of the environment variables that a given provider expects.

## Multiple providers or provider instances that expect different authentication values but have the same variable key

For example, if you are using multiple explicit providers targeting different Azure accounts, you were not able to set these separate configurations via environment variable.

Instead, users would have to to set these values in the provider config, which may not be desirable for all use cases.
Not only does the provider config write secrets to state (albeit of course encrypted), but it can also result in a noisy diff on an otherwise no-op upgrade when token rotation is used.

## Remapping environment variables

For this and similar scenarios, we have a new solution for you: setting mappings of environment variable keys on your provider.
The concept is as follows:

"For any environment variable that my Pulumi provider expects, I want to be able to tell the provider to use the value of a custom-defined environment variable instead."

## Example

Let's say you want to give your provider a specific value for `ARM_CLIENT_SECRET`, one that is different from the `ARM_CLIENT_SECRET` otherwise in use in your shell.
You would first define a new, custom environment variable as follows:

```bash
$ export CUSTOM_ARM_CLIENT_SECRET=7654321
```

And then you'd tell your provider to setits `ARM_CLIENT_SECRET` to the value of your special  `CUSTOM_ARM_CLIENT_SECRET`.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
const provider = new command.Provider("command-provider", {}, {
    envVarMappings: {
        // If CUSTOM_ARM_CLIENT_SECRET exists, provider sees the value of ARM_CLIENT_SECRET
        "CUSTOM_ARM_CLIENT_SECRET": "ARM_CLIENT_SECRET",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
provider = command.Provider("command-provider",
    opts=pulumi.ResourceOptions(
        env_var_mappings={
            # If CUSTOM_ARM_CLIENT_SECRET exists, provider sees the value of ARM_CLIENT_SECRET
            "CUSTOM_ARM_CLIENT_SECRET": "ARM_CLIENT_SECRET",
        }
    )
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
provider, err := command.NewProvider(
    ctx,
    "command-provider",
    &command.ProviderArgs{},
    pulumi.EnvVarMappings(map[string]string{
        // If CUSTOM_ARM_CLIENT_SECRET exists, provider sees the value of ARM_CLIENT_SECRET
        "CUSTOM_ARM_CLIENT_SECRET": "ARM_CLIENT_SECRET",
    }),
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var provider = new Command.Provider("command-provider", new Command.ProviderArgs(), new CustomResourceOptions
{
    EnvVarMappings = new Dictionary<string, string>
    {
        // If CUSTOM_ARM_CLIENT_SECRET exists, provider sees the value of ARM_CLIENT_SECRET
        { "CUSTOM_ARM_CLIENT_SECRET", "ARM_CLIENT_SECRET" }
    }
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var provider = new Provider("command-provider", ProviderArgs.Empty, CustomResourceOptions.builder()
    .envVarMappings(Map.of(
         // If CUSTOM_ARM_CLIENT_SECRET exists, provider sees the value of ARM_CLIENT_SECRET
        "CUSTOM_ARM_CLIENT_SECRET", "ARM_CLIENT_SECRET"
    ))
    .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  command-provider:
    type: pulumi:providers:command
    options:
      envVarMappings:
        # If CUSTOM_ARM_CLIENT_SECRET exists, provider sees the value of ARM_CLIENT_SECRET
        CUSTOM_ARM_CLIENT_SECRET: ARM_CLIENT_SECRET
```

{{% /choosable %}}

{{< /chooser >}}

You can now customize each environment variable value your provider sees by defining a new environment variable, and then mapping your provider's defined variable to yours.

For full details, see the [envVarMappings documentation](/docs/iac/concepts/resources/options/envvarmappings/).

Happy coding!
