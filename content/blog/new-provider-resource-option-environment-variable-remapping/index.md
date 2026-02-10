---
title: "Introducing envVarMappings for Provider Credentials"
date: 2026-02-12
draft: false
meta_desc: "Use envVarMappings to run multiple providers with different credentials in the same Pulumi program, no more environment variable conflicts."
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

Running multiple providers with different credentials in the same Pulumi program has always been tricky.
Providers expect fixed environment variable names like `AWS_ACCESS_KEY_ID` or `ARM_CLIENT_SECRET`, so if you need two AWS providers targeting different accounts, you couldn't configure them both via environment variables.

Pulumi v3.220.0 introduces `envVarMappings`, a new resource option that solves this problem by letting you remap provider environment variables to custom keys.

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

Let's say your provider expects `ARM_CLIENT_SECRET`, but you want it to use a different value than the one set in your shell. First, define a custom environment variable with your desired value:

```bash
$ export CUSTOM_ARM_CLIENT_SECRET=7654321
```

Then, use `envVarMappings` to tell the provider: "When you look for `ARM_CLIENT_SECRET`, read from `CUSTOM_ARM_CLIENT_SECRET` instead." The mapping format is `{ "SOURCE_VAR": "TARGET_VAR" }`:

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
Try it out with Pulumi v3.220.0 today!

For full details, see the [envVarMappings documentation](/docs/iac/concepts/resources/options/envvarmappings/).

Happy coding!
