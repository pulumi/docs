---
title_tag: "Designing for Multiple Languages | Pulumi Design Guidelines"
meta_desc: Design multi-language Pulumi components — the serialization constraints of the plugin boundary, representable types, enums, and schema-driven docs.
title: Designing for Multiple Languages
h1: Designing for Multiple Languages
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Designing for multiple languages
        parent: iac-guides-design-guidelines
        weight: 60
---

A multi-language component is authored once and consumed from every Pulumi language. That reach is the whole appeal — a platform team writes a component in TypeScript and an application team uses it from Python, Go, C#, Java, or YAML — but it comes with a constraint that shapes the design from the start. The component's inputs and outputs cross a serialization boundary between the consumer's program and the plugin that implements the component, and only data that can survive that crossing belongs on the public surface.

This constraint is not unique to Pulumi. Any system that projects a single API into multiple languages restricts that API to a comparable representable subset. Designing to a language-neutral surface is the price of write-once, consume-anywhere — and, handled well, it is a small price.

## Decide early: multi-language or single-language

Whether a component is multi-language is a packaging decision, and it changes what types you are allowed to use. A [native language package](/docs/iac/guides/building-extending/components/packaging-components/#native-language-packages) is an ordinary class in one language with no Pulumi plugin and no serialization boundary; its arguments can be any type the language supports, including ones that could never cross a wire. A [plugin package](/docs/iac/guides/building-extending/components/packaging-components/) — source-based or executable — is consumable from every language precisely because its surface is described by a schema and marshaled across the boundary.

{{% guideline type="do" %}}
**DO** decide up front whether you are building a multi-language plugin package or a single-language native package, because it determines which types you may put on inputs and outputs.
{{% /guideline %}}

The reason to decide early is that the choice is hard to reverse. If you ship a native package today and later want multi-language consumption, every input that relied on a non-representable type — a callback, a class instance, a union — becomes a breaking change to remove. Designing to the representable subset from the beginning costs little and keeps the door open. See [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) for the full trade-off.

## Think in schema, not language objects

A multi-language component's public surface is effectively a [schema](/docs/iac/guides/building-extending/packages/schema/): a language-neutral description of its inputs and outputs that Pulumi projects into each consuming language's SDK. The most reliable way to design that surface is to picture it as data rather than as objects in your authoring language.

{{% guideline type="do" %}}
**DO** design inputs and outputs as data — primitives, lists, maps, and nested typed objects — so the shape projects cleanly into every language.
{{% /guideline %}}

The constraint applies only to the public surface. Inside the constructor or factory function you are writing ordinary code in one language and may use any feature it offers: helper classes, closures, generics, third-party libraries. Only what crosses the boundary as an input or output is governed by what the schema can represent.

## Use representable types

The authoritative list of what can and cannot appear on a packaged component's arguments lives in [Component arguments and type requirements](/docs/iac/guides/building-extending/components/build-a-component/#component-arguments-and-type-requirements). In summary, the representable types are:

1. Primitives — strings, numbers (integers and floats), and booleans.
1. Lists of representable types.
1. Maps with string keys and representable values.
1. Nested object types whose properties are themselves representable.
1. Enums (with one caveat for Go, noted below).
1. [Assets and archives](/docs/iac/concepts/assets-archives/).
1. Any of the above wrapped in an `Input`/`Output` so consumers can pass values that aren't known until deploy time.

Types that do not serialize are not representable: functions and callbacks, arbitrary language classes and interfaces, and open-ended unions beyond optionality. The per-language section of the reference spells out the exact syntax and the edge cases for each.

{{% guideline type="do" %}}
**DO** keep every input and output within the representable set, and prefer a flat shape — deeply nested arguments are harder to construct in every language.
{{% /guideline %}}

Here is an argument type built entirely from representable types: primitives, a list, a map, a nested typed object, and an enum-modeled field. It defines the same contract in each authoring language.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
export interface TlsConfigArgs {
    enabled: pulumi.Input<boolean>;
    minimumProtocolVersion: pulumi.Input<string>;  // closed set: "TLSv1.2" | "TLSv1.3"
}

export interface WebServiceArgs {
    image: pulumi.Input<string>;
    replicas?: pulumi.Input<number>;
    domains: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<{ [key: string]: pulumi.Input<string> }>;
    tls: pulumi.Input<TlsConfigArgs>;
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class TlsConfigArgs(TypedDict):
    enabled: pulumi.Input[bool]
    minimum_protocol_version: pulumi.Input[str]  # closed set: "TLSv1.2" | "TLSv1.3"

class WebServiceArgs(TypedDict):
    image: pulumi.Input[str]
    replicas: NotRequired[pulumi.Input[int]]
    domains: pulumi.Input[Sequence[pulumi.Input[str]]]
    tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
    tls: pulumi.Input[TlsConfigArgs]
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type TlsConfigArgs struct {
    Enabled                pulumi.BoolInput   `pulumi:"enabled"`
    MinimumProtocolVersion pulumi.StringInput `pulumi:"minimumProtocolVersion"` // closed set: "TLSv1.2" | "TLSv1.3"
}

type WebServiceArgs struct {
    Image    pulumi.StringInput    `pulumi:"image"`
    Replicas pulumi.IntPtrInput    `pulumi:"replicas,optional"`
    Domains  pulumi.StringArrayInput `pulumi:"domains"`
    Tags     pulumi.StringMapInput `pulumi:"tags,optional"`
    Tls      TlsConfigArgs         `pulumi:"tls"`
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
public class TlsConfigArgs : ResourceArgs
{
    [Input("enabled", required: true)]
    public Input<bool> Enabled { get; set; } = null!;

    [Input("minimumProtocolVersion", required: true)] // closed set: "TLSv1.2" | "TLSv1.3"
    public Input<string> MinimumProtocolVersion { get; set; } = null!;
}

public class WebServiceArgs : ResourceArgs
{
    [Input("image", required: true)]
    public Input<string> Image { get; set; } = null!;

    [Input("replicas")]
    public Input<int>? Replicas { get; set; }

    [Input("domains", required: true)]
    public InputList<string> Domains { get; set; } = null!;

    [Input("tags")]
    public InputMap<string> Tags { get; set; } = null!;

    [Input("tls", required: true)]
    public Input<TlsConfigArgs> Tls { get; set; } = null!;
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
public final class WebServiceArgs extends ResourceArgs {
    @Import(name = "image", required = true)
    private Output<String> image;

    @Import(name = "replicas")
    private @Nullable Output<Integer> replicas;

    @Import(name = "domains", required = true)
    private Output<List<String>> domains;

    @Import(name = "tags")
    private @Nullable Output<Map<String, String>> tags;

    @Import(name = "tls", required = true)
    private Output<TlsConfigArgs> tls;

    // getters omitted for brevity
}
```

{{% /choosable %}}

{{< /chooser >}}

Property names are defined once in their canonical camelCase form and projected into each language's idiomatic casing automatically; you don't repeat the name per language. The [Naming](/docs/iac/guides/building-extending/design-guidelines/naming/) chapter covers that projection and how to choose names that survive it.

## No callbacks across the boundary

It is tempting in a single-language program to take a function as an argument — a transform applied to each resource, a predicate that decides a default, an inline policy. A function cannot be represented in the schema and cannot be marshaled to a consumer in another language, so it has no place on a multi-language component's surface.

{{% guideline type="dont" %}}
**DON'T** accept a function, lambda, or callback as a component input. It cannot cross the plugin boundary, and it cannot be expressed at all from YAML.
{{% /guideline %}}

Replace the callback with declarative configuration: a named mode, a policy object with explicit fields, or a closed set of options the component interprets internally. A `retryPolicy` object with `maxAttempts` and `backoffSeconds` says the same thing as a retry callback, works from every language, and reads cleanly in YAML.

## Closed sets are enums

When an input accepts one of a fixed set of values — a TLS version, a load-balancer scheme, a log level — model it as an enum rather than a free-form string. An enum projects into each language as a real type with named members, so consumers get autocomplete and compile-time checking instead of guessing at valid strings, and the allowed values are self-documenting in the generated SDK and the Registry.

{{% guideline type="consider" %}}
**CONSIDER** modeling a fixed set of choices as an enum. It projects into each language as a named type and documents the valid values without a separate note.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** reach for an enum before adding a second boolean. Two booleans encode four states, not all of which may be valid; a single enum names exactly the states you intend.
{{% /guideline %}}

The booleans-versus-enums rationale is covered in [Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/); the multi-language point is that the enum's value is amplified across languages. One caveat: Go has no native enum type, and Pulumi's Go schema inference does not synthesize an enum from string constants. A Go-authored component therefore expresses such a field as a plain string — the `minimumProtocolVersion` field above keeps to a string for exactly this reason. If enums in the generated SDKs matter to you, authoring in a language with native enum support is the more direct route.

## Watch the edges that differ by language

Most representable types behave identically everywhere, but a few details are expressed differently across languages and are worth a moment of thought.

{{% guideline type="consider" %}}
**CONSIDER** how optionality and numeric precision read in each target language, and stay within widely supported types rather than relying on one language's exotic type.
{{% /guideline %}}

Optionality and nullability are spelled differently per language — `?` in TypeScript, `Optional` in Python and Java, the `,optional` struct tag in Go, the `[Input]` attribute in C# — and the reference documents the canonical form for each. Numbers are the other common edge: very large integers and high-precision values don't have a single universal representation, so a value that fits comfortably in one language's numeric type may not in another. When in doubt, keep to ordinary integers and floats and consult [Component arguments and type requirements](/docs/iac/guides/building-extending/components/build-a-component/#component-arguments-and-type-requirements) for the specifics.

## Doc comments are your API docs

For a plugin package, the doc comments you write on argument and output properties are more than code comments — they flow into the generated schema and become the rendered API documentation in every language, in editor autocomplete, and in the [Registry](/docs/iac/guides/building-extending/packages/source-based-plugin/) or Pulumi Cloud IDP gallery. A consumer who never sees your source still sees these descriptions.

{{% guideline type="do" %}}
**DO** write a doc comment on every input and output property. For plugin packages these become the API documentation a consumer reads in their own language.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** shipping an undocumented public surface. An input with no description forces every consumer to read the source or guess, in a language where they may not have the source at all.
{{% /guideline %}}

## YAML is a consumer too

A multi-language component is consumable from YAML, and YAML is purely declarative — no `apply`, no loops, no glue code. It is the strictest consumer of your design, and a good check on whether the component is genuinely language-neutral.

{{% guideline type="do" %}}
**DO** sanity-check that your component is pleasant to use from YAML. If configuring it requires imperative glue, the design is leaning on features only one language offers.
{{% /guideline %}}

A component that reads naturally in YAML — declarative inputs, no callbacks, no values that only make sense after an `apply` — will read naturally everywhere. If you find yourself unable to express a sensible YAML usage, that is a signal to revisit the surface, not to exclude YAML.

## See also

- [Component arguments and type requirements](/docs/iac/guides/building-extending/components/build-a-component/#component-arguments-and-type-requirements) — the authoritative list of representable types
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — native versus plugin packages and what each allows
- [Pulumi package schema](/docs/iac/guides/building-extending/packages/schema/) — the language-neutral surface a component projects from
- [Naming](/docs/iac/guides/building-extending/design-guidelines/naming/) — one name, projected into every language
