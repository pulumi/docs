---
title_tag: "Designing Inputs and Outputs | Pulumi Design Guidelines"
meta_desc: How to design a Pulumi component's inputs and outputs — argument shape, required versus optional, secure defaults, secrets, validation, and what to expose.
title: Designing Inputs and Outputs
h1: Designing Inputs and Outputs
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Designing inputs and outputs
        parent: iac-guides-design-guidelines
        weight: 30
---

A component's inputs and outputs are its contract. The inputs are what a consumer must understand to use it; the outputs are what they get to build on. Both are projected into every Pulumi language and, once published, are expensive to change. This chapter is about shaping that contract so it is small, safe, and stable.

## The args object

Pulumi components take their inputs as a single arguments object — `StaticPageArgs`, `VpcArgs` — passed as the constructor's second parameter after the instance name. This object is the component's front door: it is the first thing a consumer sees in autocomplete and the thing they fill in to call you.

{{% guideline type="do" %}}
**DO** group a component's inputs into one args type named after the component, with the `Args` suffix.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** take a long list of positional parameters. Positional arguments have no names at the call site, can't be reordered or made optional without breaking callers, and read terribly once there are more than two of them. The args object solves all three problems and is the convention every Pulumi consumer expects.
{{% /guideline %}}

Each field on the args type carries the same weight as a top-level property: it is named once, projected into every language, and part of the contract. See [Naming](/docs/iac/guides/building-extending/design-guidelines/naming/) for how to name those fields well.

## Required versus optional

The required inputs are the ones a consumer cannot avoid thinking about. Every required input is a question you force them to answer before they can deploy anything at all.

{{% guideline type="do" %}}
**DO** make an input required only when there is no sensible default — when the component genuinely cannot proceed without the consumer's answer. Everything else should be optional.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** the number of required inputs as a measure of the abstraction's altitude. A component with one or two required inputs is asking the consumer for the essential decisions and handling the rest. A component with a dozen required inputs is asking them to configure the underlying resources by hand — a sign the abstraction is too low. See [Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/).
{{% /guideline %}}

How each language expresses optionality is mechanical — `?` in TypeScript, `Optional` in Python, a pointer or zero value in Go, a nullable property in C#, an unset builder field in Java — but the design decision is the same everywhere: a consumer who supplies only the required inputs should still get a complete, working result.

## Sensible, secure defaults

A default is a decision you make on the consumer's behalf. The whole value of a component is that its author has the expertise to make those decisions well, so the defaults should be what a knowledgeable user would have chosen anyway.

{{% guideline type="do" %}}
**DO** choose defaults that are correct for the majority of consumers. A consumer who configures nothing optional should get a sound, production-reasonable result, not a starting point they have to harden.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** default to the secure posture: encryption enabled, public access denied, least-privilege permissions, logging on. The safe configuration should be the one a consumer gets for free.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** default to an insecure or permissive setting because it is convenient or makes a demo shorter. A default that quietly exposes data or grants broad access turns every consumer who didn't override it into an incident. If a consumer needs the unsafe option, make them ask for it explicitly.
{{% /guideline %}}

This is the same principle behind the [`StaticPage` component](/docs/iac/guides/building-extending/components/build-a-component/): it deliberately configures the bucket policy and public-access block so the page is reachable without leaving the account exposed. The consumer inherits that judgment. Good defaults are what let a consumer supply only what is unique to their case and inherit a sound baseline for the rest.

## Accept Input<T>

A property value in a Pulumi program is frequently not a plain, resolved value — it is an [output](/docs/iac/concepts/inputs-outputs/) of another resource that won't be known until deployment. Component inputs must accept these. The `Input<T>` type (`pulumi.Input<string>`, `pulumi.StringInput`, `Input<string>`, depending on the language) is the wrapper that accepts both a plain value and an unresolved output of that value.

{{% guideline type="do" %}}
**DO** type every input as `Input<T>` rather than a plain `T`. This lets a consumer wire your component's inputs directly to other resources' outputs, which is the normal way Pulumi programs connect resources together.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** accept an already-resolved plain value where an `Input<T>` belongs. A plain `string` parameter forces the consumer to `apply` or `await` the upstream output before calling you, which defeats Pulumi's dependency tracking and is awkward in every language.
{{% /guideline %}}

The canonical args type is small: one or two `Input<T>` fields for the essential decisions, the rest optional with defaults.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
export interface StaticPageArgs {
    // Required: no sensible default exists for the page's content.
    indexContent: pulumi.Input<string>;
    // Optional: defaults to "index.html" when omitted.
    indexDocument?: pulumi.Input<string>;
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class StaticPageArgs(TypedDict):
    index_content: pulumi.Input[str]
    """Required: no sensible default exists for the page's content."""
    index_document: NotRequired[pulumi.Input[str]]
    """Optional: defaults to "index.html" when omitted."""
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type StaticPageArgs struct {
    // Required: no sensible default exists for the page's content.
    IndexContent pulumi.StringInput `pulumi:"indexContent"`
    // Optional: defaults to "index.html" when omitted.
    IndexDocument pulumi.StringPtrInput `pulumi:"indexDocument"`
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
public sealed class StaticPageArgs : ResourceArgs {
    // Required: no sensible default exists for the page's content.
    [Input("indexContent")]
    public Input<string> IndexContent { get; set; } = null!;

    // Optional: defaults to "index.html" when omitted.
    [Input("indexDocument")]
    public Input<string>? IndexDocument { get; set; }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
class StaticPageArgs extends ResourceArgs {
    // Required: no sensible default exists for the page's content.
    @Import(name = "indexContent", required = true)
    private Output<String> indexContent;

    // Optional: defaults to "index.html" when omitted.
    @Import(name = "indexDocument")
    private Output<String> indexDocument;
}
```

{{% /choosable %}}

{{< /chooser >}}

## Validate early

Inputs that violate the component's assumptions should be rejected where the mistake was made — at construction — with an error that names the offending input and what it expected. The alternative is a confusing failure deep inside a provider call, after the consumer has waited for a deployment to get there.

{{% guideline type="do" %}}
**DO** validate inputs at construction and fail with a clear, specific message. "`cidrBlock` must be a valid CIDR range" is worth far more than letting the cloud provider reject it ten resources later.
{{% /guideline %}}

What you can validate, and when, depends on how the component is packaged — a same-language component can run arbitrary validation logic, while a component consumed across languages goes through schema-level constraints. See [Designing for multiple languages](/docs/iac/guides/building-extending/design-guidelines/designing-for-languages/).

## Group related inputs

A cluster of settings that belong together should look like one thing, not a scattering of loose fields. Flat boolean and string inputs that all configure the same sub-concern are hard to discover, and nothing stops a consumer from setting them inconsistently.

{{% guideline type="consider" %}}
**CONSIDER** a nested typed object for a group of related settings — `logging: { enabled, retentionDays, bucket }` rather than three top-level `logging*` fields. The nesting documents the relationship and keeps the top-level args readable.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** "flag soup": a pile of mutually dependent booleans where only certain combinations are valid. When two flags are only ever set together, or never together, they are usually one decision wearing two names.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** model a choice among named modes as an enum or string union — `tier: "standard" | "premium"` — rather than several mutually exclusive booleans like `isStandard` and `isPremium`. An enum makes the illegal combinations unrepresentable and projects cleanly into every language. See [Designing for multiple languages](/docs/iac/guides/building-extending/design-guidelines/designing-for-languages/).
{{% /guideline %}}

## Secrets

Some inputs and outputs carry sensitive material — passwords, tokens, private keys, connection strings. Pulumi can [encrypt these in state and mask them in CLI output](/docs/iac/concepts/secrets/), but only if the component marks them as secret.

{{% guideline type="do" %}}
**DO** mark sensitive inputs and outputs as secret so Pulumi encrypts them in state and masks them in `pulumi up` output. A credential that lands in plaintext state is a credential leak.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** propagate secretness from inputs into the outputs derived from them. If an output is computed from a secret input — or is itself a generated password — it must be secret too, or the encryption is undone the moment the value is exposed.
{{% /guideline %}}

## Designing outputs

Outputs are what a consumer builds the rest of their program on. The ones that matter most are the values a consumer cannot easily reconstruct themselves: endpoints, ARNs, generated names, connection strings. These are the reason they reach for your output instead of recomputing it. `eks.Cluster` exposes `kubeconfig` for exactly this reason — the one output nearly every consumer needs and none can reconstruct by hand.

{{% guideline type="do" %}}
**DO** expose the values a consumer needs to use or reference the thing the component created — especially values that are generated, assigned by the cloud, or otherwise not knowable from the inputs.
{{% /guideline %}}

A component registers its outputs by assigning them to public fields and calling `registerOutputs`. The fields are the typed contract; `registerOutputs` records the values into Pulumi's state.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
export class StaticPage extends pulumi.ComponentResource {
    // The output a consumer actually needs: the live URL.
    public readonly endpoint: pulumi.Output<string>;

    constructor(name: string, args: StaticPageArgs, opts?: pulumi.ComponentResourceOptions) {
        super("sample-components:index:StaticPage", name, args, opts);
        // ... create children ...
        this.endpoint = bucketWebsite.websiteEndpoint;
        this.registerOutputs({
            endpoint: this.endpoint,
        });
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
class StaticPage(pulumi.ComponentResource):
    endpoint: pulumi.Output[str]
    """The output a consumer actually needs: the live URL."""

    def __init__(self, name, args, opts=None):
        super().__init__("sample-components:index:StaticPage", name, {}, opts)
        # ... create children ...
        self.endpoint = bucket_website.website_endpoint
        self.register_outputs({
            "endpoint": self.endpoint,
        })
```

{{% /choosable %}}

{{% choosable language go %}}

```go
type StaticPage struct {
    pulumi.ResourceState
    // The output a consumer actually needs: the live URL.
    Endpoint pulumi.StringOutput `pulumi:"endpoint"`
}

func NewStaticPage(ctx *pulumi.Context, name string, args *StaticPageArgs, opts ...pulumi.ResourceOption) (*StaticPage, error) {
    comp := &StaticPage{}
    if err := ctx.RegisterComponentResource("sample-components:index:StaticPage", name, comp, opts...); err != nil {
        return nil, err
    }
    // ... create children ...
    comp.Endpoint = bucketWebsite.WebsiteEndpoint
    return comp, ctx.RegisterResourceOutputs(comp, pulumi.Map{
        "endpoint": comp.Endpoint,
    })
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
class StaticPage : ComponentResource {
    // The output a consumer actually needs: the live URL.
    [Output("endpoint")]
    public Output<string> Endpoint { get; set; }

    public StaticPage(string name, StaticPageArgs args, ComponentResourceOptions? opts = null)
        : base("sample-components:index:StaticPage", name, args, opts)
    {
        // ... create children ...
        this.Endpoint = bucketWebsite.WebsiteEndpoint;
        this.RegisterOutputs(new Dictionary<string, object?> {
            ["endpoint"] = this.Endpoint,
        });
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
class StaticPage extends ComponentResource {
    // The output a consumer actually needs: the live URL.
    @Export(name = "endpoint", refs = { String.class }, tree = "[0]")
    public final Output<String> endpoint;

    public StaticPage(String name, StaticPageArgs args, ComponentResourceOptions opts) {
        super("sample-components:index:StaticPage", name, null, opts);
        // ... create children ...
        this.endpoint = bucketWebsite.websiteEndpoint();
        this.registerOutputs(Map.of(
            "endpoint", this.endpoint));
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

## Keep the output contract stable and minimal

Every output is a promise. Once a consumer references it, you cannot remove or retype it without a [breaking change](/docs/iac/guides/building-extending/design-guidelines/versioning-and-evolution/). The output surface should therefore be the meaningful one, not the exhaustive one.

{{% guideline type="avoid" %}}
**AVOID** dumping every property of every child resource as an output. A wide output surface locks your internal resource layout into the contract — you can no longer swap a child or change how it's wired without breaking someone — and it buries the few outputs that matter under dozens that don't.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** exposing a child resource itself (or its id or ARN) when consumers legitimately need to extend or reference it. This is the same escape hatch described in [Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/): a deliberate, documented handle on one child is far better than a black box, and far better than reflexively exposing all of them. See [Composition and resource structure](/docs/iac/guides/building-extending/design-guidelines/composition/) for how children relate to the component.
{{% /guideline %}}

The discipline is the same on both sides of the contract. A small, well-chosen set of inputs and a small, well-chosen set of outputs are what let consumers adopt the component quickly and let you evolve it without breaking them.

## See also

- [Inputs and outputs](/docs/iac/concepts/inputs-outputs/) — the underlying concept
- [Secrets](/docs/iac/concepts/secrets/) — marking and handling sensitive values
- [Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/) — required-input count and escape hatches
- [Designing for multiple languages](/docs/iac/guides/building-extending/design-guidelines/designing-for-languages/) — validation and representable types
