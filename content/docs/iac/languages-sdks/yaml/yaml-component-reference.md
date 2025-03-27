---
title_tag: "Pulumi YAML Component Reference | Languages & SDKs"
meta_desc: Specification for the Pulumi YAML component format
title: Component Reference
h1: Pulumi YAML Component reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Component Reference
        parent: iac-languages-yaml
        weight: 1
    languages:
        parent: yaml-language
        weight: 1
aliases:
---

Pulumi components can be defined in many languages, and the Pulumi YAML dialect offers an additional language for authoring Pulumi components.

The Pulumi YAML provider supports components written in YAML or JSON. Each YAML component plugin consists of a top level `components` section, which consists of a map of component names to a component definition.

```yaml
components:
  myComponent:
    inputs: {}
    resources: {}
    variables: {}
    outputs: {}
```

Each component works similar to how a YAML program works.  See also the [YAML Reference documentation](/docs/iac/languages-sdks/yaml/yaml-language-reference/) for more information

## Component definition

Each component can have the following top level sections:

| Property | Type | Required | Expression | Description |
| - | - | - | - | - |
| `inputs` | [config options](/docs/reference/pulumi-yaml/#config-options) | No | No | Inputs specifies the inputs to the components. |
| `resources` | map[string]Resource | No | No | Resources declares the [Pulumi resources](/docs/concepts/resources/) that the component will consist of. |
| `variables` | map[string]Expression | No | Yes | Variables specifies intermediate values of the program, the values of variables are expressions that can be re-used. |
| `outputs` | map[string]Expression | No | Yes | Outputs specifies the [Pulumi stack outputs](/docs/concepts/stack#outputs) of the component. |

In many locations within this schema, values may be expressions which computed a value based on the `inputs`, `variables`, or outputs of `resources`.  These expressions can be provided in two ways:

* If an object is provided as a value, and has a key that has the prefix `fn::`, the object is treated as an expression, and the expression will be resolved to a new value that will be used in place of the object.
* Any string value is interpreted as an interpolation, with `${...}` being replaced by evaluating the expression in the `...`.

The supported expression forms for each of these can be found in the [YAML program reference](/docs/iac/languages-sdks/yaml/yaml-language-reference/)

### Inputs

`inputs` is a map of config property keys to structured declarations ([see here](/docs/reference/pulumi-yaml/#config-options)).

The value of `inputs` is an object whose keys are logical names by which the config input will be referenced in expressions within the program, and whose values are elements of the schema below.  Each item in this object represents an independent input.

| Property | Type | Required | Expression | Description |
| - | - | - | - | - |
| `type` | string | No | Yes | Type is the (required) data type for the parameter. It can be one of: `string`, `integer`, `boolean` or `array`. |
| `default` | any | No | No | Default is a value of the appropriate type for the component to use if no value is specified. |
| `items` | [config options](/docs/reference/pulumi-yaml/#config-options) | No | No | Required if `type` is `array`. Specifies the type of the array members |

### Resources

The value of `resources` is an object whose keys are logical resource names by which the resource will be referenced in expressions within the program, and whose values which are elements of the schema below.  Each item in this object represents a resource which will be managed by the Pulumi Component.

| Property  |  Type | Required | Expressions | Description |
|- | - | - | - | - |
| `type` | string | Yes | No | Type is the Pulumi type token for this resource. |
| `defaultProvider` | bool | No | No | DefaultProvider specifies if a provider should be used for resources without an explicit one set. Set only on provider resources. |
| `properties` | `map[string]Expression` | No | Yes | Properties contains the primary resource-specific keys and values to initialize the resource state. |
| `options` | [Resource Options](/docs/iac/languages-sdks/yaml/yaml-language-reference/#resource-options) | No | No | Options contains all resource options supported by Pulumi. |
| `get` | [Resource Getter](/docs/iac/languages-sdks/yaml/yaml-language-reference/#resource-getter) | No | Yes | A getter function for the resource. Supplying `get` is mutually exclusive to `properties`. |

### Outputs

The value of [`outputs`](https://www.pulumi.com/docs/concepts/stack/#outputs) is an object whose keys are the logical names of the outputs that are available from outside the Pulumi Component and whose values are potentially computed expressions that resolve to the values of the desired outputs.

```yaml
outputs:
  outputName: ${resource.id}
```
