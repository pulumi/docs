---
title_tag: "Schema for Pulumi Packages"
meta_desc: This page describes the schema for a Pulumi Package, describing the resources, functions and types
           that define a Pulumi Package.
title: Schema
h1: Pulumi package schema
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Schema reference
        parent: iac-extending-pulumi
        weight: 8
aliases:
- /docs/guides/pulumi-packages/schema/
- /docs/using-pulumi/pulumi-packages/schema/
- /docs/iac/packages-and-automation/pulumi-packages/schema/
- /docs/iac/using-pulumi/pulumi-packages/schema/
- /docs/iac/using-pulumi/extending-pulumi/schema/
---

Pulumi Packages are described by a package schema, which is used to drive code generation for SDKs in each supported Pulumi language, as well as generation of language-agnostic package documentation.  This schema can be manually authored (for component packages) or generated from some other source (such as a cloud provider's API specifications for a native Pulumi resource provider).  Packages can expose resources and functions, define types used by these resources and functions, and provide packaging metadata for language-specific SDKs.

## Example

An example of the Pulumi Package Schema is below.  This schema describes a package named `apigateway`, with a single resource `RestAPI` which is a [component](/docs/concepts/resources#components), and which has a required input property `routes` and required (always populated) output properties `url` of type `string` and `api` which references the external type of the AWS API Gateway [`RestAPI`](/docs/reference/pkg/aws/apigateway/restapi/) resource.  The type of the `routes` input is a custom type named `EventHandlerRoute` defined in the schema, which is an object type with `path`,`method` and `function` properties. The schema supports generation of SDKs for `csharp`, `go`, `nodejs` and `python`, with metadata configuring each of the generated SDKs in the corresponding sections.

```json
{
    "name": "apigateway",
    "types": {
        "apigateway:index:EventHandlerRoute": {
            "type": "object",
            "properties": {
                "path": {
                    "type": "string"
                },
                "method": {
                    "type": "string"
                },
                "function": {
                    "$ref": "/aws/v3.30.0/schema.json#/resources/aws:lambda%2Ffunction:Function"
                }
            }
        }
    },
    "resources": {
        "apigateway:index:RestAPI": {
            "isComponent": true,
            "inputProperties": {
                "routes": {
                    "type": "array",
                    "items": {
                        "$ref": "#/types/apigateway:index:EventHandlerRoute"
                    }
                }
            },
            "requiredInputs": [
                "routes"
            ],
            "properties": {
                "url": {
                    "type": "string"
                },
                "api": {
                    "$ref": "/aws/v3.30.0/schema.json#/resources/aws:apigateway%2FrestApi:RestApi"
                }
            },
            "required": [
                "url",
                "api"
            ]
        }
    },
    "language": {
        "csharp": {
            "packageReferences": {
                "Pulumi": "3.*",
                "Pulumi.Aws": "4.*"
            }
        },
        "go": {
            "generateResourceContainerTypes": true,
            "importBasePath": "github.com/acmecorp/pulumi-apigateway/sdk/go/apigateway"
        },
        "nodejs": {
            "dependencies": {
                "@pulumi/aws": "^4.5.1"
            },
            "devDependencies": {
                "typescript": "^3.7.0"
            }
        },
        "python": {
            "requires": {
                "pulumi": ">=3.0.0,<4.0.0",
                "pulumi-aws": ">=4.0.0,<5.0.0"
            }
        }
    }
}
```

Complete schema examples that include a much wider range of schema configuration styles are available in these existing packages:

* [AWS](https://github.com/pulumi/pulumi-aws/blob/master/provider/cmd/pulumi-resource-aws/schema.json) - Bridged Provider Package
* [Azure Native](https://github.com/pulumi/pulumi-azure-native/blob/master/provider/cmd/pulumi-resource-azure-native/schema.json) - Native Pulumi Provider Package
* [EKS](https://github.com/pulumi/pulumi-eks/blob/master/provider/cmd/pulumi-resource-eks/schema.json) - Component Package

## Pulumi Package Schema

### Package

| Property            | Type                                       | Required | Description                                                                                                                       |
|---------------------|--------------------------------------------|----------|-----------------------------------------------------------------------------------------------------------------------------------|
| `name`              | `string`                                   | Yes      | Name is the unqualified name of the package (e.g. "aws", "azure", "gcp", "kubernetes", "random")                                  |
| `displayName`       | `string`                                   | No       | The human-friendly name of the package.                                                                                           |
| `version`           | `string`                                   | Yes      | Version is the version of the package. The version must be valid semver.                                                          |
| `description`       | `string`                                   | No       | Description is the description of the package.                                                                                    |
| `keywords`          | `array[string]`                            | No       | Keywords is the list of keywords that are associated with the package, if any.<br><br>Reserved keywords can be specified that help with categorizing the package in the [Pulumi registry](/registry/). `category/<name>` and `kind/<type>` are the only reserved keywords at this time, where `<name>` can be one of: `cloud`, `database`, `infrastructure`, `network`, `utility`, `vcs` and `<type>` is either `native` or `component`. If the package is a bridged Terraform provider, then don't include a `kind/` label. |
| `homepage`          | `string`                                   | No       | Homepage is the package's homepage.                                                                                               |
| `license`           | `string`                                   | No       | License indicates which license is used for the package's contents.                                                               |
| `attribution`       | `string`                                   | No       | Attribution allows freeform text attribution of derived work, if needed.                                                          |
| `repository`        | `string`                                   | No       | Repository is the URL at which the source for the package can be found.                                                           |
| `logoUrl`           | `string`                                   | No       | LogoURL is the URL for the package's logo, if any.                                                                                |
| `pluginDownloadURL` | `string`                                   | No       | PluginDownloadURL is the URL to use to acquire the provider plugin binary, if any. See [Authoring & Publishing](/docs/using-pulumi/pulumi-packages/how-to-author#publish-your-package) for more details. |
| `publisher`         | `string`                                   | No       | The name of the person or organization that authored and published the package.                                                   |
| `namespace`         | `string`                                   | No       | The namespace of the package. Used to disambiguate the package name. Defaults to 'pulumi' when not specified                          |
| `meta`              | [`Metadata`](#metadata)                    | No       | Meta contains information for the importer about this package.                                                                    |
| `config`            | [`Config`](#config)                        | No       | Config describes the set of configuration variables defined by this package.                                                      |
| `types`             | [`map[ComplexType]`](#complextype)         | No       | Types is a map from type token to ComplexType that describes the set of complex types (ie. object, enum) defined by this package. |
| `provider`          | [`Resource`](#resource)                    | No       | Provider describes the provider type for this package.                                                                            |
| `resources`         | [`map[Resource]`](#resource)               | No       | Resources is a map from type token to Resource that describes the set of resources defined by this package.                       |
| `functions`         | [`map[Function]`](#function)               | No       | Functions is a map from token to Function that describes the set of functions defined by this package.                            |
| `language`          | [`map[PackageLanguage]`](#packagelanguage) | No       | Language specifies additional language-specific data about the package.                                                           |
| `parameterization`  | [`ParameterizationSpec`](#parameterizationspec) | No  | Specifies the parameters for the package to specialize a parameterized provider for a concrete use case.                          |

### Metadata

Metadata for the importer about this package.

| Property       | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                                                   |
|----------------|----------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `moduleFormat` | `string` | No       | ModuleFormat is a regex that is used by the importer to extract a module name from the module portion of a type token. Packages that use the module format "namespace1/namespace2/.../namespaceN" do not need to specify a format. The regex must define one capturing group that contains the module name, which must be formatted as "namespace1/namespace2/...namespaceN". |

### Config

A package's configuration variables.

| Property    | Type                         | Required | Description                                                                                           |
|-------------|------------------------------|----------|-------------------------------------------------------------------------------------------------------|
| `variables` | [`map[Property]`](#property) | No       | Variables is a map from variable name to Property that describes a package's configuration variables. |
| `required`  | `array[string]`              | No       | Required is a list of the names of the package's required configuration variables.                    |

### ObjectType

An object type.

| Property      | Type                                            | Required | Description                                                                                                                                                       |
|---------------|-------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `description` | `string`                                        | No       | Description is the description of the type, if any.                                                                                                               |
| `properties`  | [`map[Property]`](#property)                    | No       | Properties, if present, is a map from property name to Property that describes the type's properties.                                                             |
| `type`        | `string`                                        | No       | Type must be "object" if this is an object type, or the underlying type for an enum.                                                                              |
| `required`    | `array[string]`                                 | No       | Required, if present, is a list of the names of an object type's required properties. These properties must be set for inputs and will always be set for outputs. |
| `language`    | [`map[ObjectTypeLanguage]`](#objecttypelanguage) | No       | Language specifies additional language-specific data about the type.                                                                                              |

### ComplexType

An object or enum type.

| Property                                                | Type                             | Required | Description                                                        |
|---------------------------------------------------------|----------------------------------|----------|--------------------------------------------------------------------|
| All [`ObjectType`](#objecttype) properties, as well as: |                                  |          |                                                                    |
| `enum`                                                  | [`array[EnumValue]`](#enumvalue) | No       | Enum, if present, is the list of possible values for an enum type. |

### Resource

A resource description.

| Property                                                | Type                                         | Required | Description                                                                                                                                                          |
|---------------------------------------------------------|----------------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| All [`ObjectType`](#objecttype) properties, as well as: |                                              |          |                                                                                                                                                                      |
| `inputProperties`                                       | [`map[Property]`](#property)                 | No       | Description is the description of the property, if any.                                                                                                              |
| `requiredInputs`                                        | `array[string]`                              | No       | RequiredInputs is a list of the names of the resource's required input properties.                                                                                   |
| `stateInputs`                                           | [`ObjectType`](#objecttype)                  | No       | StateInputs is an optional ObjectType that describes additional inputs that may be necessary to get an existing resource. If this is unset, only an ID is necessary. |
| `aliases`                                               | [`array[Alias]`](#alias)                     | No       | Aliases is the list of aliases for the resource.                                                                                                                     |
| `deprecationMessage`                                    | `string`                                     | No       | DeprecationMessage indicates whether or not the resource is deprecated.                                                                                              |
| `language`                                              | [`map[ResourceLanguage]`](#resourcelanguage) | No       | Language specifies additional language-specific data about the resource.                                                                                             |
| `isComponent`                                           | `boolean`                                    | No       | IsComponent indicates whether the resource is a ComponentResource.                                                                                                   |
| `methods`                                               | `map[string]string`                          | No       | Methods maps method names to functions in this schema.                                                                                                               |

### Function

A function description.

| Property             | Type                                         | Required | Description                                                              |
|----------------------|----------------------------------------------|----------|--------------------------------------------------------------------------|
| `description`        | `string`                                     | No       | Description is the description of the function, if any.                  |
| `inputs`             | [`ObjectType`](#objecttype)                  | No       | Inputs is the bag of input values for the function, if any.              |
| `outputs`            | [`ObjectType`](#objecttype)                  | No       | Outputs is the bag of output values for the function, if any.            |
| `deprecationMessage` | `string`                                     | No       | DeprecationMessage indicates whether or not the function is deprecated.  |
| `language`           | [`map[FunctionLanguage]`](#functionlanguage) | No       | Language specifies additional language-specific data about the function. |

### Type

A reference to a type.

| Property               | Type                              | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------|-----------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `type`                 | `string`                          | Yes      | Type is the primitive or composite type, if any. May be "boolean", "integer", "number", "string", "array", or "object".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `$ref`                 | `string`                          | Yes      | Ref is a reference to a type in this or another document. For example, the built-in `Archive`, `Asset`, and `Any` types are referenced as `"pulumi.json#/Archive"`, `"pulumi.json#/Asset"`, and `"pulumi.json#/Any"`, respectively. A type from this document is referenced as `"#/types/pulumi:type:token"`. A type from another document is referenced as `"path#/types/pulumi:type:token"`, where path is of the form: `"/provider/vX.Y.Z/schema.json"` or `"pulumi.json"` or `"http[s]://example.com /provider/vX.Y.Z/schema.json"`. A resource from this document is referenced as "#/resources/pulumi:type:token". A resource from another document is referenced as `"path#/resources/pulumi:type:token"`, where path is of the form: `"/provider/vX.Y.Z/schema.json"` or `"pulumi.json"` or `"http[s]://example.com /provider/vX.Y.Z/schema.json"`. |
| `additionalProperties` | [`Type`](#type)                   | No       | AdditionalProperties, if set, describes the element type of an "object" (i.e. a string -> value map).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `items`                | [`Type`](#type)                   | No       | Items, if set, describes the element type of an array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `oneOf`                | [`array[Type]`](#type)            | No       | OneOf indicates that values of the type may be one of any of the listed types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `discriminator`        | [`Discriminator`](#discriminator) | No       | Discriminator informs the consumer of an alternative schema based on the value associated with it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `plain`                | `boolean`                         | No       | Plain indicates that when used as an input, this type does not accept eventual values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Property

An object or resource property.

| Property                                    | Type                                         | Required | Description                                                                                                                   |
|---------------------------------------------|----------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------|
| All [`Type`](#type) properties, as well as: |                                              |          |                                                                                                                               |
| `description`                               | `string`                                     | No       | Description is the description of the property, if any.                                                                       |
| `const`                                     | `any`                                        | No       | Const is the constant value for the property, if any. The type of the value must be assignable to the type of the property.   |
| `default`                                   | `any`                                        | No       | Default is the default value for the property, if any. The type of the value must be assignable to the type of the property.  |
| `defaultInfo`                               | `Default`                                    | No       | DefaultInfo contains additional information about the property's default value, if any.                                       |
| `deprecationMessage`                        | `string`                                     | No       | DeprecationMessage indicates whether or not the property is deprecated.                                                       |
| `language`                                  | [`map[PropertyLanguage]`](#propertylanguage) | No       | Language specifies additional language-specific data about the property.                                                      |
| `secret`                                    | `boolean`                                    | No       | Secret specifies if the property is secret (default false).                                                                   |
| `replaceOnChanges`                          | `boolean`                                    | No       | ReplaceOnChanges specifies if the associated object should be updated with a replace operation instead of a update operation. |
| `willReplaceOnChanges`                      | `boolean`                                    | No       | WillReplaceOnChanges indicates that the provider will replace the resource when this property is changed. |

### EnumValue

The values metadata associated with an enum type.

| Property             | Type     | Required | Description                                                                                          |
|----------------------|----------|----------|------------------------------------------------------------------------------------------------------|
| `name`               | `string` | No       | Name, if present, overrides the name of the enum value that would usually be derived from the value. |
| `description`        | `string` | No       | Description of the enum value.                                                                       |
| `value`              | `any`    | No       | Value is the enum value itself.                                                                      |
| `deprecationMessage` | `string` | No       | DeprecationMessage indicates whether or not the value is deprecated.                                 |

### Alias

An alias description.

| Property  | Type     | Required | Description                                          |
|-----------|----------|----------|------------------------------------------------------|
| `name`    | `string` | No       | Name is the name portion of the alias, if any.       |
| `project` | `string` | No       | Project is the project portion of the alias, if any. |
| `type`    | `string` | No       | Type is the type portion of the alias, if any.       |

### Default

Extra information about the default value for a property.

| Property      | Type                                       | Required | Description                                                                        |
|---------------|--------------------------------------------|----------|------------------------------------------------------------------------------------|
| `environment` | `array[string]`                            | Yes      | Environment specifies a set of environment variables to probe for a default value. |
| `language`    | [`map[DefaultLanguage]`](#defaultlanguage) | No       | Language specifies additional language-specific data about the default value.      |

### Discriminator

Informs the consumer of an alternative schema based on the value associated with it.

| Property       | Type          | Required | Description                                                                                           |
|----------------|---------------|----------|-------------------------------------------------------------------------------------------------------|
| `propertyName` | `string`      | Yes      | PropertyName is the name of the property in the payload that will hold the discriminator value.       |
| `mapping`      | `map[string]` | No       | Mapping is an optional object to hold mappings between payload values and schema names or references. |

## Language-Specific Extensions

Several schema types contain a `language` field which is a map from a supported language to a language-specific schema type.  The schema for this type is language dependent, and offers extensibility for language-specific SDK code generators to encode language-specific information about the schema entry.

### PackageLanguage

Language-specific information for a package.

{{% chooser language "javascript,typescript,python,go,csharp,java" / %}}

{{% choosable language "javascript,typescript" %}}

For `javascript, typescript`:

| Property                       | Type          | Required | Description                                                                                            |
|--------------------------------|---------------|----------|--------------------------------------------------------------------------------------------------------|
| `packageName`                  | `string`      | No       | Custom name for the NPM package.                                                                       |
| `packageDescription`           | `string`      | No       | Description for the NPM package.                                                                       |
| `readme`                       | `string`      | No       | Readme contains the text for the package's README.md files.                                            |
| `dependencies`                 | `map[string]` | No       | NPM dependencies to add to package.json.                                                               |
| `devDependencies`              | `map[string]` | No       | NPM dev-dependencies to add to package.json.                                                           |
| `peerDependencies`             | `map[string]` | No       | NPM peer-dependencies to add to package.json.                                                          |
| `resolutions`                  | `map[string]` | No       | NPM resolutions to add to package.json                                                                 |
| `typescriptVersion`            | `string`      | No       | A specific version of TypeScript to include in package.json.                                           |
| `moduleToPackage`              | `map[string]` | No       | A map containing overrides for module names to package names.                                          |
| `compatibility`                | `string`      | No       | Toggle compatibility mode for a specified target.                                                      |
| `disableUnionOutputTypes`      | `boolean`     | No       | Disable support for unions in output types.                                                            |
| `containsEnums`                | `boolean`     | No       | An indicator for whether the package contains enums.                                                   |
| `providerNameToModuleName`     | `boolean`     | No       | A map allowing you to map the name of a provider to the name of the module encapsulating the provider. |
| `liftSingleValueMethodReturns` | `boolean`     | No       | Determines whether to make single-return-value methods return an output object or the single value.    |
| `respectSchemaVersion`         | `boolean`     | No       | Use the [`package.version`](#package) field in the generated SDK                                       |
| `pluginName`                   | `string`      | No       | The name of the plugin, which might be different from the package name.                                |
| `pluginVersion`                | `string`      | No       | The version of the plugin, which might be different from the version of the package.                   |

{{% /choosable %}}
{{% choosable language python %}}

For `python`:

| Property                       | Type          | Required | Description                                                                                                                                            |
|--------------------------------|---------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| `packageName`                  | `string`      | No       | PackageName is an override for the name of the generated python package.                                                                               |
| `pythonRequires`               | `string`      | No       | PythonRequires determines the Python versions that the generated provider supports.                                                                    |
| `requires`                     | `map[string]` | No       | Description for the PyPi package.                                                                                                                      |
| `readme`                       | `string`      | No       | Readme contains the text for the package's README.md files.                                                                                            |
| `moduleNameOverrides`          | `map[string]` | No       | Optional overrides for Pulumi module names.                                                                                                            |
| `compatibility`                | `string`      | No       | Toggle compatibility mode for a specified target.                                                                                                      |
| `liftSingleValueMethodReturns` | `boolean`     | No       | Determines whether to make single-return-value methods return an output object or the single value.                                                    |
| `respectSchemaVersion`         | `boolean`     | No       | Use the [`package.version`](#package) field in the generated SDK.                                                                                      |
| `pyproject`                    | `object`      | No       | If enabled, a pyproject.toml file will be generated.                                                                                                   |
| `inputTypes`                   | `string`      | No       | Controls the types of resource inputs. Either `classes` for args-classes or `classes-and-dicts` for args-classes side by side with typed dictionaries. |

{{% /choosable %}}
{{% choosable language go %}}

For `go`:

| Property                         | Type          | Description                                                                                                                                    |
|----------------------------------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| `importBasePath`                 | `string`      | Base path for package imports.                                                                                                                 |
| `modulePath`                     | `string`      | Module path for go.mod.                                                                                                                        |
| `rootPackageName`                | `string`      | Explicit package name, which may be different to the import path.                                                                              |
| `moduleToPackage`                | `map[string]` | Map from module -> package name.                                                                                                               |
| `packageImportAliases`           | `map[string]` | Map from package name -> package alias.                                                                                                        |
| `importPathPattern`              | `string`      | Defines the pattern for how import paths should be constructed from the base import path and used module.                                      |
| `generateResourceContainerTypes` | `boolean`     | Generate container types (arrays, maps, pointer output types etc.) for each resource. These are typically used to support external references. |
| `pulumiSDKVersion`               | `string`      | The version of the Pulumi SDK used with this provider, e.g. 3.                                                                                 |
| `liftSingleValueMethodReturns`   | `boolean`     | Determines whether to make single-return-value methods return an output object or the single value.                                            |
| `internalModuleName`             | `string`      | When set, the code generator will use this name for the generated internal module instead of "internal"                                        |
| `generateExtraInputTypes`        | `boolean`     | GenerateExtraInputTypes determines whether or not the code generator generates input (and output) types for all plain types.                   |
| `omitExtraInputTypes`            | `boolean`     | omitExtraInputTypes determines whether the code generator generates input (and output) types for all plain types.                              |
| `respectSchemaVersion`           | `boolean`     | Use the [`package.version`](#package) field in the generated SDK.                                                                              |
| `internalDependencies`           | `[]string`    | InternalDependencies are blank imports emitted in the SDK so `go mod tidy` doesn't remove the associated module dependencies from the go.mod.  |

{{% /choosable %}}
{{% choosable language csharp %}}

For `csharp`:

| Property                       | Type          | Required | Description                                                                                         |
|--------------------------------|---------------|----------|-----------------------------------------------------------------------------------------------------|
| `packageReferences`            | `map[string]` | No       |                                                                                                     |
| `namespaces`                   | `map[string]` | No       |                                                                                                     |
| `compatibility`                | `string`      | No       |                                                                                                     |
| `dictionaryConstructors`       | `boolean`     | No       |                                                                                                     |
| `projectReferences`            | `[]string`    | No       |                                                                                                     |
| `liftSingleValueMethodReturns` | `boolean`     | No       | Determines whether to make single-return-value methods return an output object or the single value. |
| `rootNamespace`                | `string`      | No       | The root namespace that the generated package should live under. This setting defaults to "Pulumi". |
| `respectSchemaVersion`         | `boolean`     | No       | Use the [`package.version`](#package) field in the generated SDK.                                   |

{{% /choosable %}}
{{% choosable language java %}}

For `java`:

| Property                          | Type          | Required | Description                                                                                                                 |
|-----------------------------------|---------------|----------|-----------------------------------------------------------------------------------------------------------------------------|
| `packages`                        | `map[string]` | No       | Overrides for module names to Java package names. Example: "autoscaling/v1" -> "autoscaling.v1".                            |
| `basePackage`                     | `string`      | No       | Prefixes the generated Java package. This setting defaults to "com.pulumi".                                                 |
| `buildFiles`                      | `string`      | No       | Generates build files for the chosen build tool. Supported values: "gradle".                                                |
| `repositories`                    | `map[string]` | No       | If non-empty, specifies a list of Maven repositories that should be referenced by the generated package.                    |
| `dependencies`                    | `map[string]` | No       | Java dependencies to use with the `buildFiles`. Example: "com.pulumi.gcp" -> "6.23.0".                                      |
| `gradleNexusPublishPluginVersion` | `string`      | No       | If BuildFiles="gradle", use the given version of io.github.gradle-nexus.publish-plugin in the generated Gradle build files. |
| `gradleTest`                      | `string`      | No       | If BuildFiles="gradle", generates a section to enable `gradle test` to run unit tests. Supported values: "JUnitPlatform".   |

{{% /choosable %}}

### PropertyLanguage

Language-specific info for a property.

For `csharp`:

| Property | Type     | Required | Description |
|----------|----------|----------|-------------|
| `name`   | `string` | No       |             |

### DefaultLanguage

Not yet supported in any target languages.

### ResourceLanguage

Not yet supported in any target languages.

### FunctionLanguage

Not yet supported in any target languages.

### ObjectTypeLanguage

Not yet supported in any target languages.

### ParameterizationSpec

NOTE: this is an advanced feature.

Parameterized packages should populate `ParameterizationSpec` with concrete parameter values. Pulumi code generators
read this section to emit SDKs that preserves the parameter values and communicates them back to the provider at runtime
when the code is in use.

Parameter values should be stored as a base64-encoded string under `parameter`.

| Property       | Type                                    | Required | Description                                          |
|----------------|-----------------------------------------|----------|------------------------------------------------------|
| `baseProvider` | [`BaseProviderSpec`](#baseproviderspec) | No       | The base provider to parameterize.                   |
| `parameter`    | `string`                                | No       | Base64-encoded string of provider parameters.        |

### BaseProviderSpec

| Property   | Type     | Required | Description                                                                     |
|------------|----------|----------|---------------------------------------------------------------------------------|
| `name`     | `string` | No       | The base provider name, such as "myprov" for a `pulumi-resource-myprov` binary. |
| `version`  | `string` | No       | The base provider version, such as "1.2.3" without the leading "v".             |
