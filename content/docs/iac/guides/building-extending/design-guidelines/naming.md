---
title_tag: "Naming | Pulumi Design Guidelines"
meta_desc: Naming guidelines for Pulumi components — type tokens, packages, properties, and child resources — designed for a great experience in every Pulumi language.
title: Naming
h1: Naming
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Naming
        parent: iac-guides-design-guidelines
        weight: 20
---

Names are the most visible part of a component and the most expensive to change. A consumer sees them in their editor's autocomplete, in `pulumi up` output, in state, and in the Registry. Once a component is published, its names are a contract: renaming anything is a [breaking change](/docs/iac/guides/building-extending/design-guidelines/versioning-and-evolution/). Good names are worth the time they take to get right.

This is doubly true for [multi-language components](/docs/iac/concepts/components/), where a single name you choose is projected into every Pulumi language. A name that reads well in one language and awkwardly in another degrades the experience for everyone who isn't using your authoring language.

## Type tokens

Every component has a type token of the form `package:module:Name` — for example, `awsx:ec2:Vpc` or `sample-components:index:StaticPage`. This token is the component's public identity. It appears in state, in CLI output, and in the Registry.

{{% guideline type="do" %}}
**DO** name the component type with a PascalCase noun that describes the concept it models: `Vpc`, `StaticPage`, `KubernetesCluster`. The type name is a thing, not an action.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** use a short, lowercase package name that identifies your library or platform — for example, `awsx` or your team's name. Use `index` as the module for top-level types, and introduce named modules only when a package is large enough that grouping helps.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** stutter in the token. `network:vpc:Vpc` repeats the same word three times. Prefer a distinct package, module, and type so the full token reads cleanly.
{{% /guideline %}}

## Properties: one name, every language

You define a component's input and output property names once, in their canonical camelCase form. Pulumi projects each name into the idiomatic casing of every consuming language automatically — so a single, well-chosen name becomes natural everywhere.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
// Canonical name: numberOfAvailabilityZones → TypeScript camelCase.
const vpc = new Vpc("app", {
    numberOfAvailabilityZones: 3,
});
export const subnets = vpc.privateSubnetIds;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# Canonical name: numberOfAvailabilityZones → Python snake_case.
vpc = Vpc("app", {
    "number_of_availability_zones": 3,
})
pulumi.export("subnets", vpc.private_subnet_ids)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// Canonical name: numberOfAvailabilityZones → Go PascalCase.
vpc, _ := NewVpc(ctx, "app", &VpcArgs{
    NumberOfAvailabilityZones: pulumi.Int(3),
})
ctx.Export("subnets", vpc.PrivateSubnetIds)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Canonical name: numberOfAvailabilityZones → C# PascalCase.
var vpc = new Vpc("app", new VpcArgs {
    NumberOfAvailabilityZones = 3,
});
this.Subnets = vpc.PrivateSubnetIds;
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Canonical name: numberOfAvailabilityZones → Java camelCase.
var vpc = new Vpc("app", VpcArgs.builder()
    .numberOfAvailabilityZones(3)
    .build());
ctx.export("subnets", vpc.privateSubnetIds());
```

{{% /choosable %}}

{{< /chooser >}}

Because the same name is reshaped per language, choose names that survive the trip:

{{% guideline type="do" %}}
**DO** spell names out. `numberOfAvailabilityZones` translates cleanly into every casing convention; `numAZs` becomes cryptic in all of them.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** names that collide with reserved words or built-ins in a target language — `class`, `type`, `object`, `lambda`, `import`. A name that is fine in your authoring language can force an awkward rename or escaping in another.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** treat acronyms consistently. Pick one canonical form — `vpcId`, `apiKey`, `htmlContent` — and rely on the per-language projection to do the rest. Mixing `URL` and `Url` across properties reads as carelessness once projected.
{{% /guideline %}}

## Names that describe intent

{{% guideline type="do" %}}
**DO** name a property after what it means to the consumer, not after the underlying resource attribute it happens to map to. `domainName` is clearer than `route53RecordFqdn`.
{{% /guideline %}}

{{% guideline type="do" %}}
**DO** phrase boolean inputs as positive assertions of the enabled state: `enableLogging`, `publiclyAccessible`. Negated names like `disableLogging` force the reader to untangle a double negative when they set them to `false`.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** matching the vocabulary of the domain you model. If a consumer thinks in terms of "availability zones" and "CIDR blocks," use those words. Familiar names make a component feel like a natural part of the platform.
{{% /guideline %}}

{{% guideline type="avoid" %}}
**AVOID** vague, overloaded names like `config`, `options`, `data`, or `settings` for a specific input. They tell the consumer nothing about what belongs there. See [Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/) for grouping related inputs well.
{{% /guideline %}}

## Naming child resources

A component's children each need a name. Those names form the resources' [URNs](/docs/iac/concepts/resources/names/) and, with [auto-naming](/docs/iac/concepts/resources/names/#autonaming), often influence the physical names in the cloud.

{{% guideline type="do" %}}
**DO** derive child resource names from the component instance's name, typically by prefixing it: `` `${name}-bucket` ``, `` `${name}-policy` ``. This keeps children unique across multiple instances of the component and makes their origin obvious in state and CLI output.
{{% /guideline %}}

{{% guideline type="dont" %}}
**DON'T** hard-code a fixed string as a child's name. Two instances of the component in the same stack would then collide. The component instance name is what disambiguates them.
{{% /guideline %}}

{{% guideline type="consider" %}}
**CONSIDER** keeping child name suffixes stable over the life of the component. Changing a child's name suffix changes its URN, which Pulumi sees as a delete-and-replace. Use [`aliases`](/docs/iac/concepts/resources/options/aliases/) when you must rename one. See [Versioning and evolution](/docs/iac/guides/building-extending/design-guidelines/versioning-and-evolution/).
{{% /guideline %}}

## See also

- [Resource names and auto-naming](/docs/iac/concepts/resources/names/)
- [Designing inputs and outputs](/docs/iac/guides/building-extending/design-guidelines/inputs-and-outputs/)
- [Designing for multiple languages](/docs/iac/guides/building-extending/design-guidelines/designing-for-languages/)
- [Pulumi package schema](/docs/iac/guides/building-extending/packages/schema/)
