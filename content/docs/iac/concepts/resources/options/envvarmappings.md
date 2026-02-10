---
title_tag: "envVarMappings | Resource Options"
meta_desc: The envVarMappings resource option remaps environment variables to custom keys for provider authentication.
title: "envVarMappings"
h1: "Resource option: envVarMappings"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: envVarMappings
    parent: options-concepts
    weight: 6
aliases:
  - /docs/iac/concepts/options/envvarmappings/
  - /docs/intro/concepts/resources/options/envvarmappings/
  - /docs/concepts/options/envvarmappings/
---

The `envVarMappings` resource option allows you to remap environment variables that a provider expects to custom environment variable names.
This is useful when you need to run multiple providers or provider instances that require different values for the same environment variable.

## When to use envVarMappings

Use this option when:

- **Running multiple providers targeting different accounts or regions**: For example, two AWS providers targeting different accounts can each use their own environment variable-based credentials without conflicting.

{{% notes type="info" %}}
The `envVarMappings` resource option only applies to provider resources.
It cannot be used on regular resources or component resources.
You must define an explicit provider to use this resource option.
{{% /notes %}}

## Example

The following example shows how to remap `CUSTOM_ARM_CLIENT_SECRET` to `ARM_CLIENT_SECRET` so the provider reads from your custom environment variable:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as azure from "@pulumi/azure-native";

const provider = new azure.Provider("azure-provider", {}, {
    envVarMappings: {
        "CUSTOM_ARM_CLIENT_SECRET": "ARM_CLIENT_SECRET",
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_azure_native as azure

provider = azure.Provider("azure-provider",
    opts=pulumi.ResourceOptions(
        env_var_mappings={
            "CUSTOM_ARM_CLIENT_SECRET": "ARM_CLIENT_SECRET",
        }
    )
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
provider, err := azure.NewProvider(ctx, "azure-provider", &azure.ProviderArgs{},
    pulumi.EnvVarMappings(map[string]string{
        "CUSTOM_ARM_CLIENT_SECRET": "ARM_CLIENT_SECRET",
    }),
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.AzureNative;

var provider = new Provider("azure-provider", new ProviderArgs(), new CustomResourceOptions
{
    EnvVarMappings = new Dictionary<string, string>
    {
        { "CUSTOM_ARM_CLIENT_SECRET", "ARM_CLIENT_SECRET" }
    }
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.azurenative.Provider;
import com.pulumi.azurenative.ProviderArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.Map;

var provider = new Provider("azure-provider", ProviderArgs.Empty,
    CustomResourceOptions.builder()
        .envVarMappings(Map.of(
            "CUSTOM_ARM_CLIENT_SECRET", "ARM_CLIENT_SECRET"
        ))
        .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  azure-provider:
    type: pulumi:providers:azure-native
    options:
      envVarMappings:
        CUSTOM_ARM_CLIENT_SECRET: ARM_CLIENT_SECRET
```

{{% /choosable %}}

{{< /chooser >}}

## Multi-provider example

A common use case is running two providers targeting different cloud accounts. Here's an example with two AWS providers for production and staging environments:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

// Production provider reads from PROD_AWS_ACCESS_KEY_ID and PROD_AWS_SECRET_ACCESS_KEY
const prodProvider = new aws.Provider("aws-prod", {}, {
    envVarMappings: {
        "PROD_AWS_ACCESS_KEY_ID": "AWS_ACCESS_KEY_ID",
        "PROD_AWS_SECRET_ACCESS_KEY": "AWS_SECRET_ACCESS_KEY",
    },
});

// Staging provider reads from STAGING_AWS_ACCESS_KEY_ID and STAGING_AWS_SECRET_ACCESS_KEY
const stagingProvider = new aws.Provider("aws-staging", {}, {
    envVarMappings: {
        "STAGING_AWS_ACCESS_KEY_ID": "AWS_ACCESS_KEY_ID",
        "STAGING_AWS_SECRET_ACCESS_KEY": "AWS_SECRET_ACCESS_KEY",
    },
});

// Use the providers explicitly
const prodBucket = new aws.s3.Bucket("prod-bucket", {}, { provider: prodProvider });
const stagingBucket = new aws.s3.Bucket("staging-bucket", {}, { provider: stagingProvider });
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws

# Production provider reads from PROD_AWS_ACCESS_KEY_ID and PROD_AWS_SECRET_ACCESS_KEY
prod_provider = aws.Provider("aws-prod",
    opts=pulumi.ResourceOptions(
        env_var_mappings={
            "PROD_AWS_ACCESS_KEY_ID": "AWS_ACCESS_KEY_ID",
            "PROD_AWS_SECRET_ACCESS_KEY": "AWS_SECRET_ACCESS_KEY",
        }
    )
)

# Staging provider reads from STAGING_AWS_ACCESS_KEY_ID and STAGING_AWS_SECRET_ACCESS_KEY
staging_provider = aws.Provider("aws-staging",
    opts=pulumi.ResourceOptions(
        env_var_mappings={
            "STAGING_AWS_ACCESS_KEY_ID": "AWS_ACCESS_KEY_ID",
            "STAGING_AWS_SECRET_ACCESS_KEY": "AWS_SECRET_ACCESS_KEY",
        }
    )
)

# Use the providers explicitly
prod_bucket = aws.s3.Bucket("prod-bucket", opts=pulumi.ResourceOptions(provider=prod_provider))
staging_bucket = aws.s3.Bucket("staging-bucket", opts=pulumi.ResourceOptions(provider=staging_provider))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Production provider reads from PROD_AWS_ACCESS_KEY_ID and PROD_AWS_SECRET_ACCESS_KEY
prodProvider, err := aws.NewProvider(ctx, "aws-prod", &aws.ProviderArgs{},
    pulumi.EnvVarMappings(map[string]string{
        "PROD_AWS_ACCESS_KEY_ID":     "AWS_ACCESS_KEY_ID",
        "PROD_AWS_SECRET_ACCESS_KEY": "AWS_SECRET_ACCESS_KEY",
    }),
)
if err != nil {
    return err
}

// Staging provider reads from STAGING_AWS_ACCESS_KEY_ID and STAGING_AWS_SECRET_ACCESS_KEY
stagingProvider, err := aws.NewProvider(ctx, "aws-staging", &aws.ProviderArgs{},
    pulumi.EnvVarMappings(map[string]string{
        "STAGING_AWS_ACCESS_KEY_ID":     "AWS_ACCESS_KEY_ID",
        "STAGING_AWS_SECRET_ACCESS_KEY": "AWS_SECRET_ACCESS_KEY",
    }),
)
if err != nil {
    return err
}

// Use the providers explicitly
prodBucket, err := s3.NewBucket(ctx, "prod-bucket", &s3.BucketArgs{},
    pulumi.Provider(prodProvider))
stagingBucket, err := s3.NewBucket(ctx, "staging-bucket", &s3.BucketArgs{},
    pulumi.Provider(stagingProvider))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Aws;
using Pulumi.Aws.S3;

// Production provider reads from PROD_AWS_ACCESS_KEY_ID and PROD_AWS_SECRET_ACCESS_KEY
var prodProvider = new Provider("aws-prod", new ProviderArgs(), new CustomResourceOptions
{
    EnvVarMappings = new Dictionary<string, string>
    {
        { "PROD_AWS_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID" },
        { "PROD_AWS_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY" }
    }
});

// Staging provider reads from STAGING_AWS_ACCESS_KEY_ID and STAGING_AWS_SECRET_ACCESS_KEY
var stagingProvider = new Provider("aws-staging", new ProviderArgs(), new CustomResourceOptions
{
    EnvVarMappings = new Dictionary<string, string>
    {
        { "STAGING_AWS_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID" },
        { "STAGING_AWS_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY" }
    }
});

// Use the providers explicitly
var prodBucket = new Bucket("prod-bucket", new BucketArgs(), new CustomResourceOptions
{
    Provider = prodProvider
});
var stagingBucket = new Bucket("staging-bucket", new BucketArgs(), new CustomResourceOptions
{
    Provider = stagingProvider
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
import com.pulumi.aws.Provider;
import com.pulumi.aws.ProviderArgs;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.Map;

// Production provider reads from PROD_AWS_ACCESS_KEY_ID and PROD_AWS_SECRET_ACCESS_KEY
var prodProvider = new Provider("aws-prod", ProviderArgs.Empty,
    CustomResourceOptions.builder()
        .envVarMappings(Map.of(
            "PROD_AWS_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID",
            "PROD_AWS_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY"
        ))
        .build());

// Staging provider reads from STAGING_AWS_ACCESS_KEY_ID and STAGING_AWS_SECRET_ACCESS_KEY
var stagingProvider = new Provider("aws-staging", ProviderArgs.Empty,
    CustomResourceOptions.builder()
        .envVarMappings(Map.of(
            "STAGING_AWS_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID",
            "STAGING_AWS_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY"
        ))
        .build());

// Use the providers explicitly
var prodBucket = new Bucket("prod-bucket", BucketArgs.Empty,
    CustomResourceOptions.builder()
        .provider(prodProvider)
        .build());
var stagingBucket = new Bucket("staging-bucket", BucketArgs.Empty,
    CustomResourceOptions.builder()
        .provider(stagingProvider)
        .build());
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  # Production provider reads from PROD_AWS_ACCESS_KEY_ID and PROD_AWS_SECRET_ACCESS_KEY
  aws-prod:
    type: pulumi:providers:aws
    options:
      envVarMappings:
        PROD_AWS_ACCESS_KEY_ID: AWS_ACCESS_KEY_ID
        PROD_AWS_SECRET_ACCESS_KEY: AWS_SECRET_ACCESS_KEY

  # Staging provider reads from STAGING_AWS_ACCESS_KEY_ID and STAGING_AWS_SECRET_ACCESS_KEY
  aws-staging:
    type: pulumi:providers:aws
    options:
      envVarMappings:
        STAGING_AWS_ACCESS_KEY_ID: AWS_ACCESS_KEY_ID
        STAGING_AWS_SECRET_ACCESS_KEY: AWS_SECRET_ACCESS_KEY

  # Use the providers explicitly
  prod-bucket:
    type: aws:s3:Bucket
    options:
      provider: ${aws-prod}

  staging-bucket:
    type: aws:s3:Bucket
    options:
      provider: ${aws-staging}
```

{{% /choosable %}}

{{< /chooser >}}

## How it works

The `envVarMappings` option is a map where:
- **Keys** are custom environment variables you have defined in your environment
- **Values** are the names of environment variables the provider expects

When the provider initializes, Pulumi checks if your custom environment variable exists.
If it does, the provider sees its value as if it were set under the mapped variable name.

## Limitations

- **Provider resources only**: This option only works on provider resources, not on regular resources or components.
- **One-way mapping**: Each custom variable maps to exactly one provider variable. You cannot map multiple custom variables to the same provider variable on a single provider.
