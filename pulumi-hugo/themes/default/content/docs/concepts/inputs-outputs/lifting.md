---
title_tag: "Accessing Nested Properties with Lifting | Inputs and Outputs"
meta_desc: "Learn how to access nested output values using the lifting method in Pulumi."
title: Accessing nested properties with Lifting
h1: Accessing nested properties with Lifting
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 4
    parent: inputs-outputs
---

While often, Outputs return asynchronous values that wrap primitive types like strings or integers, sometimes an output has an object with deeply nested values. These properties need to be passed to other inputs as well.

For example, to read a domain record from an ACM certificate, you need to access the domain validation options, which returns an array. Because that value is an output, we would normally need to use {{< pulumi-apply >}}:

{{< chooser language "javascript,typescript,python,go,csharp,java" >}}

{{% choosable language javascript %}}

```javascript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        // Need to pass along a deep subproperty of this Output
        certCertificate.domainValidationOptions.apply(
            domainValidationOptions => domainValidationOptions[0].resourceRecordValue),
    ],
    ...
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        // Need to pass along a deep subproperty of this Output
        certCertificate.domainValidationOptions.apply(
            domainValidationOptions => domainValidationOptions[0].resourceRecordValue),
    ],
    ...
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
certificate = aws.acm.Certificate('cert',
    domain_name='example.com',
    validation_method='DNS'
)

record = aws.route53.Record('validation',
    records=[
        # Need to pass along a deep subproperty of this Output
        certificate.domain_validation_options.apply(
            lambda domain_validation_options: domain_validation_options[0]['resourceRecordValue']
        )
    ],
    ...
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
cert, err := acm.NewCertificate(ctx, "cert", &acm.CertificateArgs{
    DomainName:       pulumi.String("example"),
    ValidationMethod: pulumi.String("DNS"),
})
if err != nil {
    return err
}

record, err := route53.NewRecord(ctx, "validation", &route53.RecordArgs{
    Records: pulumi.StringArray{
        cert.DomainValidationOptions.ApplyT(func(opts []acm.CertificateDomainValidationOption) string {
            return *opts[0].ResourceRecordValue
        }).(pulumi.StringOutput),
    },
    ...
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var cert = new Certificate("cert", new CertificateArgs
{
    DomainName = "example",
    ValidationMethod = "DNS",
});

var record = new Record("validation", new RecordArgs
{
    Records = {
        cert.DomainValidationOptions.Apply(opts => opts[0].ResourceRecordValue!)
    },
    ...
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var cert = new Certificate("cert",
    CertificateArgs.builder()
        .domainName("example")
        .validationMethod("DNS")
        .build());

var record = new Record("validation",
    RecordArgs.builder()
        .records(
            cert.domainValidationOptions()
            .applyValue(opts -> opts.get(0).resourceRecordValue().get())
            .applyValue(String::valueOf)
            .applyValue(List::of))
        .build());
```

{{% /choosable %}}

{{< /chooser >}}

Instead, to make it easier to access simple property and array elements, an {{< pulumi-output >}} lifts the properties of the underlying value, behaving very much like an instance of it. Lift allows you to access properties and elements directly from the {{< pulumi-output >}} itself without needing {{< pulumi-apply >}}. If we return to the above example, we can now simplify it:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
let certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

{{% /choosable %}}

{{% choosable language python %}}

```python
certificate = aws.acm.Certificate('cert',
    domain_name='example.com',
    validation_method='DNS'
)

record = aws.route53.Record('validation',
    records=[
        certificate.domain_validation_options[0].resource_record_value
    ],
...
```

{{% /choosable %}}

{{% choosable language go %}}

```go
cert, err := acm.NewCertificate(ctx, "cert", &acm.CertificateArgs{
    DomainName:       pulumi.String("example"),
    ValidationMethod: pulumi.String("DNS"),
})
if err != nil {
    return err
}

record, err := route53.NewRecord(ctx, "validation", &route53.RecordArgs{
    Records: pulumi.StringArray{
        // Notes:
        // * `Index` looks up an index in an `ArrayOutput` and returns a new `Output`.
        // * Accessor methods like `ResourceRecordValue` lookup properties of a custom struct `Output` and return a new `Output`.
        // * `Elem` dereferences a `PtrOutput` to an `Output`, equivalent to `*`.
        cert.DomainValidationOptions.Index(pulumi.Int(0)).ResourceRecordValue().Elem(),
    },
    ...
})
if err != nil {
    return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var cert = new Certificate("cert", new CertificateArgs
{
    DomainName = "example",
    ValidationMethod = "DNS",
});

var record = new Record("validation", new RecordArgs
{
    // Notes:
    // * `GetAt` looks up an index in an `Output<ImmutableArray<T>>` and returns a new `Output<T>`
    // * There are not yet accessor methods for referencing properties like `ResourceRecordValue` on an `Output<T>` directly,
    //   so the `Apply` is still needed for the property access.
    Records = cert.DomainValidationOptions.GetAt(0).Apply(opt => opt.ResourceRecordValue!),
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Lifting is currently not supported in Java.
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  cert:
    type: aws:acm:Certificate
    properties:
      domainName: example
      validationMethod: DNS
  record:
    type: aws:route53:Record
    properties:
      records:
        # YAML handles inputs and outputs transparently.
        - ${cert.domainValidationOptions[0].resourceRecordValue}
```

{{% /choosable %}}

{{< /chooser >}}

This approach is easier to read and write and does not lose any important dependency information that is needed to properly create and maintain the stack. This approach doesn’t work in all cases, but when it does, it can be a great help.

In JavaScript and TypeScript, a ‘lifted’ property access on an `Output<T>` that wraps undefined produces another `Output<T>` with the undefined value instead of throwing or producing a ‘faulted’ `Output<T>`. In other words, lifted property accesses behave like the [`?.` (optional chaining operator)](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#optional-chaining) in JavaScript and TypeScript. This behavior makes it much easier to form a chain of property accesses on an `Output<T>`.

{{< chooser language "javascript,typescript" >}}

{{% choosable language javascript %}}

```javascript
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],

// instead of

let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.apply(cc => cc ? cc.domainValidationOptions : undefined)
                           .apply(dvo => dvo ? dvo[0] : undefined)
                           .apply(o => o ? o.resourceRecordValue : undefined)],
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],

// instead of

let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.apply(cc => cc ? cc.domainValidationOptions : undefined)
                           .apply(dvo => dvo ? dvo[0] : undefined)
                           .apply(o => o ? o.resourceRecordValue : undefined)],
```

{{% /choosable %}}

{{< /chooser >}}
