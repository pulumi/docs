### Simplified Outputs in Pulumi 0.17.0

The `Output<T>` type is used an enormous amount in any Pulumi application.  It is the way that Resources expose their values, and it is commonly used to pass values from one Resource to another.  Importantly `Outputs` are a key part of how Pulumi tracks dependencies between resources.  In fact, Outputs are similar to promises/futures that you may be familiar with from other programming models but also carry along dependency information.

In 0.17.0 of the `@pulumi/pulumi` package, we've made a very common pattern for working with Outputs much simpler.  Prior to this release of  `@pulumi/pulumi` package, it wasn't uncommon to find yourself having to write code like the following:

```ts
const certCertificate = new aws.acm.Certificate("cert", {
    domainName: "example.com",
    validationMethod: "DNS",
});
const zone = pulumi.output(aws.route53.getZone({
    name: "example.com.",
    privateZone: false,
}));
const certValidation = new aws.route53.Record("cert_validation", {
    records: [certCertificate.domainValidationOptions.apply(domainValidationOptions => domainValidationOptions[0].resourceRecordValue)],
    ttl: 60,
    type: certCertificate.domainValidationOptions.apply(domainValidationOptions => domainValidationOptions[0].resourceRecordType),
    zoneId: zone.apply(zone => zone.id),
});
```

In particular, creating the `aws.route53.Record` involve a fair amount of complexity with those arrow functions.  i.e.:

```ts
    records: [certCertificate.domainValidationOptions.apply(domainValidationOptions => domainValidationOptions[0].resourceRecordValue)],
    ttl: 60,
    type: certCertificate.domainValidationOptions.apply(domainValidationOptions => domainValidationOptions[0].resourceRecordType),
    zoneId: zone.apply(zone => zone.id),
```

The idea of the `.apply` function is similar to `Promise.then`.  It allows one to pass a piece of code that will be applied to the underlying value, and will return an `Output` that then points to the transformed underlying value.  Importantly, the new `Output` will still track dependency information properly.  In the above example the `aws.route53.Record` will know that it both depends on `certCertificate` and on `zone`, even though neither of those resources (or their direct Outputs) are passed directly do the constructor.  

Unfortunately, while `.apply` gives a lot of power and flexibility, it is also somewhat verbose and clunky for describing such a simple concept.  Fortunately, we found a way to improve the situation greatly.  This realization came about from great work done in our Python package.  First, before diving into the low level details, let's first see what the above code would now look like in 0.17.0:

```ts
// certCertificate and zone created as above

const certValidation = new aws.route53.Record("cert_validation", {
    records: [certCertificate.domainValidationOptions[0].resourceRecordValue],
    ttl: 60,
    type: certCertificate.domainValidationOptions[0].resourceRecordType,
    zoneId: zone.id,
});
```

That's a lot nicer than before!  The following improvements happened:
1. there's no more lambda!
2. there's no need for a repetive lambda parameter (which might conflict with some other name in scope).
3. the code *is* just pure simple *idiomatic* JavaScript/TypeScript that clearly conveys its intent

Importantly, no information has been lost here.  The exact same dependency information flows along here like it did before.  And, thanks to TypeScript's flexible type system, the above it totally typesafe and will let you know the right types of things and will still error if you happen to make mistakes.

So, how was this done?  

