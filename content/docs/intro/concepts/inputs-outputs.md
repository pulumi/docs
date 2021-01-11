---
title: "Inputs and Outputs"
meta_desc: An in depth look at Pulumi Inputs and Outputs and their usage.
menu:
  intro:
    parent: concepts
    weight: 3

aliases: "/docs/reference/inputs-outputs/"

---

Resource properties are treated specially in Pulumi, both for purposes of input and output.

All resource arguments accept *inputs*. Inputs are values of type [Input<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}), a type that permits either a raw value of a given type (such as string, integer, boolean, list, map, and so on), an asynchronously computed value (i.e., a `Promise` or `Task`), or an output read from another resource’s properties.

All resource properties on the instance object itself are *outputs*. Outputs are values of type [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}), which behave very much like [promises](https://en.wikipedia.org/wiki/Futures_and_promises). This is necessary because outputs are not fully known until the infrastructure resource has actually completed provisioning, which happens asynchronously. Outputs are also how Pulumi tracks dependencies between resources.

Outputs, therefore, represent two things:

- The eventual raw value of the output
- The dependency on the source(s) of the output value

Pulumi automatically captures dependencies when you pass an output from one resource as an input to another resource. Capturing these dependencies ensures that the physical infrastructure resources are not created or updated until all their dependencies are available and up-to-date.

Because outputs are asynchronous, their actual raw values are not immediately available. If you need to access an output’s raw value—for example, to compute a derived, new value, or because you want to log it—you have these options:

- [Apply]({{< relref "#apply" >}}): a callback that receives the raw value, and computes a new output
- [Lifting]({{< relref "#lifting" >}}): directly read properties off an output value
- [Interpolation]({{< relref "#outputs-and-strings" >}}): concatenate string outputs with other strings directly

## Apply

To access the raw value of an output and transform that value into a new value, use [apply]({{> relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" }}). This method accepts a callback that will be invoked with the raw value, once that value is available.

For example, the following code creates an HTTPS URL from the DNS name (the raw value) of a virtual machine:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let url = virtualmachine.dnsName.apply(dnsName => "https://" + dnsName);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let url = virtualmachine.dnsName.apply(dnsName => "https://" + dnsName);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
url = virtual_machine.dns_name.apply(
    lambda dns_name: "https://" + dns_name
)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
url := vpc.DnsName.ApplyString(func(dnsName string) string {
    return "https://" + dnsName
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var url = virtualmachine.DnsName.Apply(dnsName => "https://" + dnsName);
```

{{% /choosable %}}

{{< /chooser >}}

The result of the call to [apply]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) is a new Output<T>. So in this example, the url variable is also an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}). It will resolve to the new value returned from the callback, and carries the dependencies of the original [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}). If the callback itself returns an Output<T>, the dependencies of that output are also kept in the resulting [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}).

Note: during some program executions, [apply]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) doesn’t run. For example, it won’t run during a preview, when resource output values may be unknown. Therefore, you should avoid side-effects within the callbacks. For this reason, you should not allocate new resources inside of your callbacks either, as it could lead to `pulumi preview` being wrong.

## All

If you have multiple outputs and need to join them, the `all` function acts like an `apply` over many resources. This function joins over an entire list of outputs. It waits for all of them to become available and then provides them to the supplied callback. This function can be used to compute an entirely new output value, such as by adding or concatenating outputs from two different resources together, or by creating a new data structure that uses them. Just like with [apply]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}), the result of  [Output.all]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.all" >}}) is itself an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}).

For example, let’s use a server and a database name to create a database connection string:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
var pulumi = require("@pulumi/pulumi");
// ...
let connectionString = pulumi.all([sqlServer.name, database.name])
    .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db}...`);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
// ...
let connectionString = pulumi.all([sqlServer.name, database.name])
    .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db}...`);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi import Output
# ...
connection_string = Output.all(sql_server.name, database.name) \
    .apply(lambda args: f"Server=tcp:{args[0]}.database.windows.net;initial catalog={args[1]}...")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
connectionString := pulumi.All(sqlServer.Name, database.Name).ApplyT(
    func (args []interface{}) (string, error) {
        server := args[0].(string)
        db := args[1].(string)
        return fmt.Sprintf("Server=tcp:%s.database.windows.net;initial catalog=%s...", server, db)
    },
)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// When all the input values have the same type, Output.All can be used and produces an ImmutableArray.
var connectionString = Output.All(sqlServer.name, database.name)
    .Apply(t => `Server=tcp:${t[0]}.database.windows.net;initial catalog=${t[1]}...`);

// For more flexibility, 'Output.Tuple' is used so that each unwrapped value will preserve their distinct type.
var connectionString2 = Output.Tuple(sqlServer.name, database.name)
    .Apply(t => `Server=tcp:${t.Item1}.database.windows.net;initial catalog=${t.Item2}...`);

// Or using a more natural Tuple syntax and a statement lambda expression.
var connectionString2 = Output.Tuple(sqlServer.name, database.name).Apply(t =>
{
    var (serverName, databaseName) = t;
    return `Server=tcp:${serverName}.database.windows.net;initial catalog=${databaseName}...`;
});
```

{{% /choosable %}}

{{< /chooser >}}

Notice that [Output.all]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.all" >}}) works by returning an output that represents the combination of multiple outputs so that, within the callback, the raw values are available inside of a tuple.

## Accessing Properties of an Output by Lifting {#lifting}

If you just need to access a property of an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) value in order to pass that property’s value as an argument to another resource’s constructor, you can often just directly access it.

For example, to read a domain record from an ACM certificate, you need to access a resource’s property value. Because that value is an output, we would normally need to use [apply]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}):

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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
        cert.DomainValidationOptions.ApplyString(func(opts []acm.CertificateDomainValidationOption) string {
            return *opts[0].ResourceRecordValue
        }),
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

{{< /chooser >}}

Instead, to make it easier to access simple property and array elements, an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) lifts the properties of the underlying value, behaving very much like an instance of it. Lift allows you to access properties and elements directly from the [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) itself without needing [apply]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}). If we return to the above example, we can now simplify it:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

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

{{< /chooser >}}

This approach is easier to read and write and does not lose any important dependency information that is needed to properly create and maintain the stack. This approach doesn’t work in all cases, but when it does, it can be a great help.

In JavaScript and TypeScript, a ‘lifted’ property access on an `Output<T>` that wraps undefined produces another `Output<T>` with the undefined value instead of throwing or producing a ‘faulted’ `Output<T>`. In other words, lifted property accesses behave like the [`?.` (optional chaining operator)](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#optional-chaining) in JavaScript and TypeScript. This behavior makes it much easier to form a chain of property accesses on an `Output<T>`.

```javascript
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],

// instead of

let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.apply(cc => cc ? cc.domainValidationOptions : undefined)
                           .apply(dvo => dvo ? dvo[0] : undefined)
                           .apply(o => o ? o.resourceRecordValue : undefined)],
```

```typescript
let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.domainValidationOptions[0].resourceRecordValue],

// instead of

let certValidation = new aws.route53.Record("cert_validation", {
  records: [certCertificate.apply(cc => cc ? cc.domainValidationOptions : undefined)
                           .apply(dvo => dvo ? dvo[0] : undefined)
                           .apply(o => o ? o.resourceRecordValue : undefined)],
```

## Working with Outputs and Strings {#outputs-and-strings}

Outputs that contain strings cannot be used directly in operations such as string concatenation. String interpolation lets you more easily build a string out of various output values, without needing [apply]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) or [Output.all]({{< relref "/docs/reference/pkg/python/pulumi#pulumi.Output.all" >}}). You can use string interpolation to export a stack output, provide a dynamically computed string as a new resource argument, or even simply for diagnostic purposes.

For example, say you want to create a URL from `hostname` and `port` output values. You can do this using `apply` and `all`.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let hostname = res.hostname;
let port = res.port;

// Would like to produce a string equivalent to: http://${hostname}:${port}/
let url = pulumi.all([hostname, port]).
    apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let hostname: Output<string>;
let port: Output<number>;

// Would like to produce a string equivalent to: http://${hostname}:${port}/
let url = pulumi.all([hostname, port]).
    apply(([hostname, port]) => `http://${hostname}:${port}/`);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
hostname: Output[str]
port: Output[int]

# Would like to produce a string equivalent to: http://${hostname}:${port}/
url = Output.all(hostname, port).apply(lambda l: f"http://{l[0]}:{l[1]}/")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
var hostname pulumi.StringOutput
var port pulumi.NumberOutput

// Would like to produce a string equivalent to: http://${hostname}:${port}/
url := pulumi.All(hostname, port).ApplyString(func (args []interface{}) string {
    return fmt.Sprintf("http://%s:%d/", args[0], args[1])
})
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
Output<string> hostname = // get some Output
Output<int> port = // get some Output

// Would like to produce a string equivalent to: http://{hostname}:{port}/
var url = Output.Tuple(hostname, port).Apply(t => $"http://{t.Item1}:{t.Item2}/");
```

{{% /choosable %}}

{{< /chooser >}}

However, this approach is verbose and unwieldy. To make this common task easier, Pulumi exposes helpers that allow you to create strings that contain outputs—internally hiding all of the messiness required to join them together:

{{% choosable language javascript %}}

```javascript
// concat takes a list of args and concatenates all of them into a single output:
const url1 = pulumi.concat("http://", hostname, ":", port, "/");
// interpolate takes a JavaScript "template literal" and expands outputs correctly:
const url2 = pulumi.interpolate `http://${hostname}:${port}/`;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
// concat takes a list of args and concatenates all of them into a single output:
const url1: Output<string> = pulumi.concat("http://", hostname, ":", port, "/");
// interpolate takes a JavaScript "template literal" and expands outputs correctly:
const url2: Output<string> = pulumi.interpolate `http://${hostname}:${port}/`;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# concat takes a list of args and concatenates all of them into a single output:
url = Output.concat("http://", hostname, ":", port, "/")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
url := pulumi.Sprintf("http://%s:%d/", hostname, port)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
// Format takes a FormattableString and expands outputs correctly:
var url = Output.Format($"http://{hostname}:{port}/");
```

{{% /choosable %}}

## Convert Input to Output through Interpolation

It is possible to turn an [Input<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) into an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) value. Resource arguments already accept outputs as input values however, in some cases you need to know that a value is definitely an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) at runtime. Knowing this can be helpful because, since [Input<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) values have many possible representations—a raw value, a promise, or an output—you would normally need to handle all possible cases. By first transforming that value into an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}), you can treat it uniformly instead.

For example, this code transforms an [Input<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) into an [Output<T>]({{< relref "/docs/reference/pkg/python/pulumi#outputs-and-inputs" >}}) so that it can use the `apply` function:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
function split(input) {
    let output = pulumi.output(input);
    return output.apply(v => v.split());
}
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
function split(input: pulumi.Input<string>): pulumi.Output<string[]> {
    let output = pulumi.output(input);
    return output.apply(v => v.split());
}
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def split(input):
    output = Output.from_input(input);
    return output.apply(lambda v: v.split());
}
```

{{% /choosable %}}
{{% choosable language go %}}

```go
func split(input pulumi.StringInput) pulumi.StringArrayOutput {
    return input.ToStringOutput().ApplyStringArray(func(s string) []string {
        return strings.Split(s, ",")
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
Output<string[]> Split(Input<string> input)
{
    var output = input.ToOutput()
    return output.Apply(v => v.Split(","));
}
```

{{% /choosable %}}

{{< /chooser >}}
