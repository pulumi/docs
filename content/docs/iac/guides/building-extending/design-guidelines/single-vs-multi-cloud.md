---
title_tag: "Single- vs. Multi-Cloud Abstractions | Pulumi Design Guidelines"
meta_desc: When a cloud-agnostic Pulumi component earns its keep, and when it becomes a leaky lowest common denominator that hides what matters.
title: Single- vs. Multi-Cloud Abstractions
h1: Single- vs. Multi-Cloud Abstractions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Single- vs. multi-cloud
        parent: iac-guides-design-guidelines
        weight: 50
---

A cloud-agnostic component is valuable only when the clouds underneath it differ in ways the consumer genuinely doesn't care about. When the value the consumer is paying for lives in cloud-specific features, hiding those features behind a portable interface throws away the reason they chose that cloud in the first place.

## Decide whether portability is a real requirement

The first question is not how to build a multi-cloud abstraction. It is whether you should build one at all.

{{% guideline type="do" %}}
**DO** ask whether portability is an actual requirement or an aesthetic preference. A cloud-agnostic interface is only worth its cost if something concrete depends on it.
{{% /guideline %}}

Most teams run on one primary cloud and will for the life of the component. A multi-cloud abstraction that never gets exercised on a second cloud is pure cost: more surface area to design, more concepts for the consumer to learn, and a wider gap between what the interface promises and what the platform actually does. Worse, the unused path is rarely even correct. An implementation for a second cloud that has never been deployed and tested there is a guess, not a feature — the first consumer who tries it inherits the bugs.

"Portable" also has a real and limited meaning. Pulumi already gives you one kind of portability for free: the same program, written in the same language, deploys to any cloud, and a component is reusable across every stack. The question here is narrower — whether one component instance should be able to target more than one cloud provider behind a single interface.

## The lowest-common-denominator trap

The most common failure is an abstraction that exposes only what every target cloud has in common.

{{% guideline type="avoid" %}}
**AVOID** abstractions whose surface is the intersection of what every cloud supports. The intersection is small and bland, and it strips out the differentiated capabilities that justified picking a particular cloud.
{{% /guideline %}}

Object storage is a fair candidate for a portable concept. "A durable, addressable bucket of blobs" means nearly the same thing on Amazon S3, Azure Blob Storage, and Google Cloud Storage, and most consumers of a bucket want exactly that. A consumer who stores and retrieves objects rarely cares which of the three is underneath.

A managed database or a serverless platform is usually a poor candidate. The reason a team chooses Amazon Aurora, Azure Cosmos DB, or Google Spanner is the specific behavior of that service — its consistency model, its scaling story, its query surface, its operational guarantees. An abstraction that flattens those into a generic `Database` keeps the part that is interchangeable (it stores rows) and discards the part the team actually paid for. The same is true of AWS Lambda versus Azure Functions versus Google Cloud Run: the triggers, execution model, and concurrency semantics differ in ways application code depends on. Hide them and you have an interface that compiles against three clouds and is genuinely useful on none.

The test is to ask what the consumer would lose by going through your abstraction instead of the native resource. If the answer is "nothing they care about," portability is cheap. If the answer is "the features they chose this cloud for," the abstraction is taking away the value, not adding it.

## When multi-cloud earns its keep

Portability is worth building when two conditions hold at once: the concept is genuinely uniform across providers, and the organization has a real reason to span them.

{{% guideline type="consider" %}}
**CONSIDER** a cloud-agnostic component when the concept is genuinely uniform across providers — an object store, a DNS record, a container running somewhere — *and* a concrete portability requirement exists.
{{% /guideline %}}

Concepts that survive the trip are the ones where the clouds converged on the same model: object storage, DNS records, TLS certificates, a container image running behind an address. These are commodities, and the differences between providers are mostly billing and region names.

The requirement side has to be every bit as real. Legitimate drivers include regulatory or sovereignty rules that mandate a specific cloud in a specific geography, an acquisition that left the company running two clouds it must support, a genuine multi-region strategy that spans providers, and — most commonly — selling software that customers deploy into *their own* cloud account, where you don't control which one. That last case is the strongest: the second cloud isn't hypothetical, it's a customer you already have.

If neither condition holds, you are paying for portability you will never use. If only one holds — a uniform concept with no portability requirement, or a real requirement around a concept that isn't uniform — the abstraction is premature or doomed, respectively.

## Designing a multi-cloud abstraction well

Once you've decided to build one, the quality of the abstraction comes down to whether swapping clouds is actually real and whether the consumer can still get at cloud-specific power when they need it.

{{% guideline type="do" %}}
**DO** keep the public shape — inputs, outputs, and [naming](/docs/iac/guides/building-extending/design-guidelines/naming/) — identical across the cloud-specific implementations, so that switching providers is a one-line change and not a rewrite.
{{% /guideline %}}

If the AWS implementation calls an input `bucketName` and the Azure one calls it `containerName`, the abstraction isn't portable; it only looks portable until someone tries to switch. The shared shape is the contract, and it only means something if every implementation honors it identically.

{{% guideline type="do" %}}
**DO** provide a deliberate escape hatch to the underlying cloud-specific resource, for the consumer who needs a feature the portable interface doesn't expose.
{{% /guideline %}}

A multi-cloud abstraction will always lag the native services, and a consumer will eventually need something that lives below your interface. Exposing the underlying resource as an output lets them reach past the abstraction for that one feature without abandoning it. The general escape-hatch guidance — and the tension it creates with the altitude of the abstraction — is covered in [Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/).

Three structural patterns are common:

1. One component that takes a cloud or provider selector and branches internally. Simplest for the consumer, but the component carries every cloud's logic and dependencies.
1. Separate, identically shaped components per cloud — `AwsObjectStore`, `AzureObjectStore` — that the consumer picks between. More explicit; the shared shape lives in convention or a common interface.
1. An interface or abstract base that per-cloud implementations satisfy, with the consumer programming against the interface. Cleanest for swapping, and the most work to set up.

Whichever you choose, the consumer-facing experience should read the same. Here a consumer instantiates a cloud-agnostic `ObjectStore` and selects the backing cloud through one input:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
// One shape, one selector. The component picks the right cloud-specific
// resources; the consumer's code is identical whichever cloud they target.
const store = new ObjectStore("assets", {
    cloud: "aws",
    versioned: true,
});
export const url = store.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# One shape, one selector. The component picks the right cloud-specific
# resources; the consumer's code is identical whichever cloud they target.
store = ObjectStore("assets", {
    "cloud": "aws",
    "versioned": True,
})
pulumi.export("url", store.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// One shape, one selector. The component picks the right cloud-specific
// resources; the consumer's code is identical whichever cloud they target.
store, err := NewObjectStore(ctx, "assets", &ObjectStoreArgs{
    Cloud:     pulumi.String("aws"),
    Versioned: pulumi.Bool(true),
})
ctx.Export("url", store.Url)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// One shape, one selector. The component picks the right cloud-specific
// resources; the consumer's code is identical whichever cloud they target.
var store = new ObjectStore("assets", new ObjectStoreArgs {
    Cloud = "aws",
    Versioned = true,
});
this.Url = store.Url;
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// One shape, one selector. The component picks the right cloud-specific
// resources; the consumer's code is identical whichever cloud they target.
var store = new ObjectStore("assets", ObjectStoreArgs.builder()
    .cloud("aws")
    .versioned(true)
    .build());
ctx.export("url", store.url());
```

{{% /choosable %}}

{{< /chooser >}}

## Single-cloud, done deliberately

A focused single-cloud component that fully exploits its platform is usually the better abstraction, and choosing it on purpose is not a compromise.

The evidence points the same way across the industry. The most widely used infrastructure libraries are overwhelmingly single-provider, and Pulumi's own high-level libraries — AWSX, the EKS and Azure Native components — are each built for one cloud, precisely so they can use that cloud to its fullest.

{{% guideline type="dont" %}}
**DON'T** add multi-cloud indirection on speculation. It bakes the cost in now to hedge against a second cloud that may never arrive — and if it does arrive, the untested path probably won't work anyway.
{{% /guideline %}}

This is the same instinct as not [distilling an abstraction from a single example](/docs/iac/guides/building-extending/design-guidelines/abstraction/): an interface drawn from one real implementation and one imagined one tends to fit the real one and mislead about the rest. When a second cloud genuinely arrives, you can extract a portable interface from the working single-cloud component, informed by two real implementations instead of one and a guess.

{{% guideline type="consider" %}}
**CONSIDER** naming and structuring a single-cloud component so a portable layer could be lifted out later without a rewrite. A clean `bucketName` reads as well under a future `ObjectStore` as it does today; a leaky `s3BucketArn` in the public surface does not.
{{% /guideline %}}

## Don't pretend the clouds are the same

The worst outcome is an abstraction that hides a real behavioral difference behind a name that implies sameness.

{{% guideline type="dont" %}}
**DON'T** paper over genuine semantic differences — consistency models, IAM and identity models, networking and VPC semantics — behind a uniform name that quietly lies about them.
{{% /guideline %}}

If `ObjectStore` is strongly consistent on one cloud and eventually consistent on another, a consumer who reads-after-write correctly on the first will write a subtle bug on the second, and the abstraction is what led them there. A leaky abstraction that conceals a difference the consumer must account for is worse than no abstraction at all, because it costs them the time to discover the lie on top of the time to handle the difference. When the semantics truly diverge, two honest cloud-specific components that each tell the truth about their platform serve the consumer better than one that flattens the distinction.

## See also

- [Choosing the right abstraction](/docs/iac/guides/building-extending/design-guidelines/abstraction/)
- [Naming](/docs/iac/guides/building-extending/design-guidelines/naming/)
- [Providers](/docs/iac/concepts/providers/)
- [Components](/docs/iac/concepts/components/)
