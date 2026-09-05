---
title_tag: "Schema for Pulumi Packages"
meta_desc: This page describes the schema for a Pulumi Package, describing the resources, functions and types
           that define a Pulumi Package.
title: Schema
h1: Pulumi package schema
menu:
    iac:
        name: Schema reference
        parent: iac-guides-packages
        weight: 70
aliases:
- /docs/guides/pulumi-packages/schema/
- /docs/using-pulumi/pulumi-packages/schema/
- /docs/iac/packages-and-automation/pulumi-packages/schema/
- /docs/iac/using-pulumi/pulumi-packages/schema/
- /docs/iac/using-pulumi/extending-pulumi/schema/
- /docs/iac/extending-pulumi/schema/
- /docs/iac/build-with-pulumi/schema/
---

Pulumi Packages are described by a package schema, which is used to drive code generation for SDKs in each supported Pulumi language, as well as generation of language-agnostic package documentation. This schema can be manually authored (for component packages) or generated from some other source (such as a cloud provider's API specifications for a native Pulumi resource provider). Packages can expose resources and functions, define types used by these resources and functions, and provide packaging metadata for language-specific SDKs.

## Example

An example of the Pulumi Package Schema is below. This schema describes a package named `apigateway`, with a single resource `RestAPI` which is a [component](/docs/iac/concepts/components/), and which has a required input property `routes` and required (always populated) output properties `url` of type `string` and `api` which references the external type of the AWS API Gateway [`RestAPI`](/registry/packages/aws/api-docs/apigateway/restapi/) resource. The type of the `routes` input is a custom type named `EventHandlerRoute` defined in the schema, which is an object type with `path`,`method` and `function` properties. The schema supports generation of SDKs for `csharp`, `go`, `nodejs` and `python`, with metadata configuring each of the generated SDKs in the corresponding sections.

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
                    "$ref": "/aws/v7.44.0/schema.json#/resources/aws:lambda%2Ffunction:Function"
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
                    "$ref": "/aws/v7.44.0/schema.json#/resources/aws:apigateway%2FrestApi:RestApi"
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
                "Pulumi.Aws": "7.*"
            }
        },
        "go": {
            "generateResourceContainerTypes": true,
            "importBasePath": "github.com/acmecorp/pulumi-apigateway/sdk/go/apigateway"
        },
        "nodejs": {
            "dependencies": {
                "@pulumi/aws": "^7.44.0"
            },
            "devDependencies": {
                "typescript": "^5.0.0"
            }
        },
        "python": {
            "requires": {
                "pulumi": ">=3.0.0,<4.0.0",
                "pulumi-aws": ">=7.0.0,<8.0.0"
            }
        }
    }
}
```

Complete schema examples that include a much wider range of schema configuration styles are available in these existing packages:

* [AWS](https://github.com/pulumi/pulumi-aws/blob/master/provider/cmd/pulumi-resource-aws/schema.json) - Bridged Provider Package
* [Azure Native](https://github.com/pulumi/pulumi-azure-native/blob/master/provider/cmd/pulumi-resource-azure-native/schema.json) - Native Pulumi Provider Package
* [EKS](https://github.com/pulumi/pulumi-eks/blob/master/provider/cmd/pulumi-resource-eks/schema.json) - Component Package

## Pulumi package schema

{{< package-schema-version >}}

Every type below is one shape a package schema can contain. Names are the JSON keys you
write; a linked type means that property's value takes the shape of another type on this
page. To check a schema you've written against these rules, run
[`pulumi schema check`](/docs/iac/cli/commands/pulumi_schema_check/).

{{< package-schema group="core" >}}

## Language-specific extensions

A `language` field maps a supported language to a language-specific object. The shape of
that object is decided by that language's SDK code generator rather than by the schema
itself, which is how a generator gets to encode what it alone needs — an NPM package name,
a Java base package, a Go import path.

Each generator owns its extension, so each section below is generated from that language's
own repository and carries the release it came from. A language that has no entry for a
section does not read one.

{{< package-schema group="language" >}}
