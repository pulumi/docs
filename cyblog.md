### Simplified Outputs in Pulumi 0.17.0

The `Output<T>` type is used an enormous amount in any Pulumi application.  It is the way that Resources expose their values and it is commonly used to pass values from one Resource to another.  Importantly, `Outputs` are a key part of how Pulumi tracks dependencies between resources.  In fact, Outputs are similar to promises/futures that you may be familiar with from other programming models but also carry along dependency information.

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

Yikes!  This is so verbose, it doesn't even fit on the width of the page!

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
3. the code *is* just pure simple *idiomatic* JavaScript/TypeScript that clearly conveys its intent.

Importantly, no information has been lost here.  The exact same dependency information flows along here like it did before.  And, thanks to TypeScript's flexible type system, the above is totally typesafe and will let you know the right types of things and will still error if you happen to make mistakes.

So, how was this done?  Well, the core part of the change is thanks to a little-known feature of JavaScript: (Proxies)[https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy].

Proxies allow you to return objects where you can control many facets of how JavaScript works at runtime.  There are many things a Proxy lets you control, however for our needs the most important bit was that it allows you to override how member-lookup works.  In other words, when you write `someProxy.someMember` you get a chance to determine what should happen an what `someMember` should actually return!  With that flexible interception point available, we actually took our core `Output` type and made it into a `Proxy`.  We then added the right interception code so that if you ever write `someOutput.someMember` that that gets translated exactly into `someOutput.apply(o => o.someMember)`.   his also works just fine for array-accesses (which are just property-lookups from JavaScript's perspective).  In other words, at runtime, the member-lookup form and the `.apply` form will be equivalent (except that the former is so much nicer to write!).  This is why, for example, `certCertificate.domainValidationOptions[0].resourceRecordValue` will have the correct value (with all the right dependency information).  At runtime it really will be equivalent to the original `certCertificate.apply(certCertificate => certCertificate.domainValidationOptions[0].resourceRecordValue)` form.

Now, while this was fairly easy to get working at runtime from a JavaScript perspective, it was a little more challenging to figure out how to make this work in TypeScript's typing system.  For example, if you had a value like so:

```ts
const cert: Output<{ domainValidationOptions: pulumi.Output<{ domainName: string, resourceRecordName: string, resourceRecordType: string, resourceRecordValue: string }[]> }>;
const firstOption: Output<{ domainName: string, resourceRecordName: string, resourceRecordType: string, resourceRecordValue: string }> = cert[0];
const domainName = firstOption.domainName;
```

Then how do you let TypeScript know that `cert` should have a property on it called `domainValidationOptions`?  And how can it know that `domainValidationOptions` can be indexed into?  And how would it know that once indexed, that Output would have a `domainName` property?  Clearly, these are all `Outputs`.  Yet, each `Output<...>` has a different set of properties exposed off of it!

To do this required taking advantage of some very interesting and advanced parts of TypeScript's type system.  If this is a part of TypeScript that interests you, or you just want to see how we did this, you can dive in deep into the source (here)[https://github.com/pulumi/pulumi/blob/7d7e104ee3184d1244ea3517ab5cae5f52170dba/sdk/nodejs/output.ts#L624-L631]!  And, if you want to see how we did the actual runtime Proxy work, that code is self-contained (https://github.com/pulumi/pulumi/blob/7d7e104ee3184d1244ea3517ab5cae5f52170dba/sdk/nodejs/output.ts#L220-L282)[here].  Thanks to TypeScript's advanced type-system, these types can be properly expressed and the entire tooling ecosystem understands them.  For example, in VSCode, if you try to write code like the above, you'll see all the expected properties with the expected types:

![image](https://user-images.githubusercontent.com/4564579/54156772-29999600-4404-11e9-9419-95b9b44bad08.png)


We definitely hope these changes to `@pulumi/pulumi` in 0.17.0 will make the programming experience more pleasant and much less clunky.  And, if you've ever wanted to do some fancy tricks like what we're doing here, these updates can show you how you too can do approach some of these advanced techniques for both JavaScript and TypeScript!
