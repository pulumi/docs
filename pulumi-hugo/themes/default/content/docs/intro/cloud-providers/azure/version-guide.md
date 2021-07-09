---
title: Azure-Native Version Guide
meta_desc: How Azure API versions are represented in the native Azure provider for Pulumi.
---

The native Azure provider SDKs follow the semantic versioning convention, similarly to other Pulumi providers. At the same time, Azure API is structured around date-based API versions defined per Azure resource provider.

This guide describes how we combine both versioning approaches to achieve the following high-level design goals:

- Provide access to the entire API surface of Azure resources.
- Ship new updates as soon as Microsoft publishes them.
- Provide stable SDKs without unexpected breaking changes.
- Enable user experience similar to other Pulumi providers.

## Azure-Native Semantic Versioning

Releases of the Azure-Native SDKs follow the semantic versioning convention, where each version is identified with three numbers: `major.minor.patch` (for example, `1.2.1`).

- Patch versions contain bug fixes only.
- Minor versions may ship fixes and new functionality that doesn't break existing code: new resources, functions, properties.
- Major versions include breaking changes, where existing user code may need to be modified.

Microsoft has defined [Breaking changes guidelines](https://github.com/Azure/azure-rest-api-specs/blob/master/documentation/Breaking%20changes%20guidelines.md) for all the Azure API specifications. The native Azure provider generates SDKs from the Open API specifications, so we rely on Microsoft to follow their breaking changes guideline.

Occasionally, Microsoft ships breaking changes. For example, they may rename a misspelled property in the spec to match it with the actual service behavior. We treat these occurrences as bug fixes and ship them in patch or minor provider versions without revving the major version.

## Module Per Version

Every Azure API endpoint defines a set of API versions that it accepts. API versions are based on a date, for instance, `2020-03-01` or `2019-05-15-preview`. Breaking changes may occur between API versions. API versions are defined per Azure resource provider and are published frequently (almost every week).

The native Azure provider maps every published API version of every Azure resource provider and represents it 1:1 as a separate module. For example, the `Vault` resource of the `KeyVault` resource provider of version `2019-09-01` is published as the Pulumi resource `azure-native:keyvault/v20190901:Vault`. You can import this resource with the following statement:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import Vault from "@pulumi/azure-native/keyvault/v20190901";
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi_azure_native.keyvault.v20190901 import Vault
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi.AzureNative.KeyVault.V20190901;

new Vault(/*...*/);
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
    keyvault "github.com/pulumi/pulumi-azure-native/sdk/go/azure/keyvault/v20190901"
)

// ...
keyvault.NewVault(/*...*/)
// ...
```

{{% /choosable %}}

{{< /chooser >}}

As soon as Microsoft publishes a new API version, the corresponding module is created in the native Azure provider for Pulumi and will be published in the next minor release.

Older API versions remain in the provider indefinitely; therefore, you can pin all your resources to specific API versions. You can keep using them for as long as those versions are supported by Azure, even across major versions of the Pulumi Azure-Native provider.

## Top-Level Modules

In addition to all versioned modules described above, the Pulumi Azure-Native provider publishes a default version of every resource in top-level modules. For example, the `Vault` resource of the `KeyVault` resource provider is published as the Pulumi resource `azure-native:keyvault:Vault`. You can import this resource with the following statement:

{{< chooser language "typescript,python,csharp,go" >}}

{{% choosable language typescript %}}

```typescript
import Vault from "@pulumi/azure-native/keyvault";
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi_azure_native.keyvault import Vault
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi.AzureNative.KeyVault;

new Vault(/*...*/);
```

{{% /choosable %}}

{{% choosable language go %}}

```go
import (
    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/keyvault"
)

// ...
keyvault.NewVault(/*...*/)
// ...
```

{{% /choosable %}}

{{< /chooser >}}

Top-level resources are useful when you don't have a preference over which API version is used for every resource. We expect most users to use top-level resources most of the time, without the need to specify an explicit API version.

Each top-level resource maps internally to a specific API version. The native Azure provider maintains this mapping with the following guidelines:

- When a new major version of the provider is released, the API versions are set to the latest stable API version available at that moment. If no stable version is published yet, the newest preview version is used.
- Azure API reports a list of supported API versions per resource and resource provider. We promote resources to new API versions once they show up as supported with the `az provider list` command.
- The selected API version is pinned across all minor versions of the same major version. Even if a newer API version is released, we do not promote the top-level resources to it.
- We may introduce some manual overrides to the rules above. For example, we may use a new preview version when the latest stable version is obviously out of date. We may manually promote top-level resources to a new API version to get access to new necessary functionality. In any case, we adhere to the breaking changes policy.

Because of that, top-level resources may miss newly released features shipped in brand-new API versions after the last major release. In such cases, you are encouraged to use explicitly versioned modules to access the latest Azure functionality.

The [API reference docs]({{< relref "/docs/reference/pkg/azure-native/" >}}) describe top-level resources and do not currently show any module-per-version variations.

## Switching Between API Versions

You may switch between different API versions of a given resource, including to and from its top-level default representation, whenever you want. Resource types have aliases defined, so the switch does not require resource re-creation.
