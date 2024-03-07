---
title_tag: "Accessing Single Outputs with Apply | Inputs and Outputs"
meta_desc: "Learn how to access a single output value using the apply method in Pulumi."
title: Accessing single outputs with Apply
h1: Accessing single outputs with Apply
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 2
    parent: inputs-outputs
---

[Outputs](/docs/concepts/inputs-outputs/#outputs) are asynchronous, meaning their actual plain values are not immediately available. Their values will only become available once the resource has finished provisioning. The asynchronous nature of Outputs is also why, when certain operations such as [`pulumi preview`](/docs/cli/commands/pulumi_preview/) runs, the outputs for a new resource do not yet have any possible values. As such, there are limitations on the ways in which you can retrieve and interact with these values.

To demonstrate, let's say you have the following simple program that creates an [AWSX VPC resource](/registry/packages/awsx/api-docs/ec2/vpc/) in AWS. In this program, you want to view all of the properties of this resource, so you have added a print/log statement to print the `vpc` variable.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="awsx-vpc" language="javascript" from="1" to="3" >}}

{{< example-program-snippet path="awsx-vpc" language="javascript" from="6" to="6" >}}

console.log(vpc);
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="awsx-vpc" language="typescript" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="typescript" from="5" to="5" >}}

console.log(vpc);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="awsx-vpc" language="python" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="python" from="5" to="5" >}}

print(vpc)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="awsx-vpc" language="go" from="1" to="3" >}}
    "fmt"
{{< example-program-snippet path="awsx-vpc" language="go" from="4" to="10" >}}
{{< example-program-snippet path="awsx-vpc" language="go" from="12" to="15" >}}

        fmt.Println(vpc)

{{< example-program-snippet path="awsx-vpc" language="go" from="21" to="23" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="awsx-vpc" language="csharp" from="1" to="6" >}}
{{< example-program-snippet path="awsx-vpc" language="csharp" from="8" to="8" >}}

    Console.WriteLine(vpc);

{{< example-program-snippet path="awsx-vpc" language="csharp" from="17" to="17" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
{{< example-program-snippet path="awsx-vpc" language="java" from="1" to="9" >}}
{{< example-program-snippet path="awsx-vpc" language="java" from="11" to="11" >}}

            System.out.println(vpc);

{{< example-program-snippet path="awsx-vpc" language="java" from="17" to="19" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
This example is not applicable in YAML.
```

{{% /choosable %}}

However, deploying this program will show CLI output similar to the following:

{{% choosable language javascript %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-js-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
    ...
    ...

Diagnostics:
  pulumi:pulumi:Stack (aws-js-dev):
    <ref *1> Vpc {
          __pulumiResource: true,
          __pulumiType: 'awsx:ec2:Vpc',
          ...
          ...
          vpc: OutputImpl {
            __pulumiOutput: true,
            resources: [Function (anonymous)],
            allResources: [Function (anonymous)],
            isKnown: Promise { <pending> },
            ...
            ...
          },
          ...
        }
Resources:
    + 34 created

Duration: 2m17s
```

{{< notes type="info" >}}
You can see an example of the complete Diagnostics CLI output in [this gist](https://gist.github.com/toriancrane/be03601a7b9f0fd2e197d55ed5a41b31).
{{< /notes >}}

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-ts-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
    ...
    ...

Diagnostics:
  pulumi:pulumi:Stack (aws-ts-dev):
    <ref *1> Vpc {
          __pulumiResource: true,
          __pulumiType: 'awsx:ec2:Vpc',
          ...
          ...
          vpc: OutputImpl {
            __pulumiOutput: true,
            resources: [Function (anonymous)],
            allResources: [Function (anonymous)],
            isKnown: Promise { <pending> },
            ...
            ...
          },
          ...
        }
Resources:
    + 34 created

Duration: 2m17s
```

{{< notes type="info" >}}
You can see an example of the complete Diagnostics output in [this gist](https://gist.github.com/toriancrane/4aba791447af71a67cce06715a282a19).
{{< /notes >}}

{{% /choosable %}}

{{% choosable language python %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-py-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
    ...
    ...

Diagnostics:
  pulumi:pulumi:Stack (aws-py-dev):
    <pulumi_awsx.ec2.vpc.Vpc object at 0x7f77ac256130>

Resources:
    + 34 created

Duration: 2m17s
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-go-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
    ...
    ...

Diagnostics:
  pulumi:pulumi:Stack (aws-go-dev):
    &{{{} {{0 0} 0 0 {{} 0} {{} 0}} {0xc000196e00} {0xc000196d90} map[] map[] <nil>   [] vpc [] true} {0xc0001961c0} {0xc000196230} {0xc0001962a0} {0xc000196460} {0xc0001964d0} {0xc000196690} {0xc000196700} {0xc0001967e0} {0xc000196850} {0xc0001968c0} {0xc000196930} {0xc000196a10} {0xc000196a80} {0xc000196b60}}

Resources:
    + 34 created

Duration: 3m7s
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-csharp-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
    ...
    ...

Diagnostics:
  pulumi:pulumi:Stack (aws-csharp-dev):
    Pulumi.Awsx.Ec2.Vpc

Resources:
    34 created

Duration: 3m7s
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-java-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
...
...

# Nothing is printed

Resources:
    + 34 created

Duration: 2m17s
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
This example is not applicable in YAML.
```

{{% /choosable %}}

As shown above, using this method will not provide a JSON representation of the VPC resource complete with its properties and associated property values. This is because, when it comes to Pulumi resource classes, there is no way to output this kind of JSON representation for a resource.

Ultimately, if you want to view the properties of a resource, you will need to access them at the individual property level. The rest of this guide will demonstrate how to access and interact with a single property using {{< pulumi-apply >}}.

{{< notes type="info" >}}
The `apply` method is great for when you need to access single values. However, if you need to access multiple output values across multiple resources, you will need to use Pulumi's [`all` method](/docs/concepts/inputs-outputs/all) instead.
{{< /notes >}}

## Accessing single output values { search.keywords="pulumi.apply" }

Let's say you want to print the ID of the VPC you've created. Given that this is an individual resouce property and not the entire resource itself, you might try logging the value like normal:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="awsx-vpc" language="javascript" from="1" to="3" >}}

{{< example-program-snippet path="awsx-vpc" language="javascript" from="6" to="6" >}}

console.log(vpc.vpcId);
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="awsx-vpc" language="typescript" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="typescript" from="5" to="5" >}}

console.log(vpc.vpcId);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="awsx-vpc" language="python" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="python" from="5" to="5" >}}

print(vpc.vpc_id)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="awsx-vpc" language="go" from="1" to="3" >}}
    "fmt"
{{< example-program-snippet path="awsx-vpc" language="go" from="4" to="10" >}}
{{< example-program-snippet path="awsx-vpc" language="go" from="12" to="15" >}}

        fmt.Println(vpc.VpcId)

{{< example-program-snippet path="awsx-vpc" language="go" from="21" to="23" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="awsx-vpc" language="csharp" from="1" to="6" >}}
{{< example-program-snippet path="awsx-vpc" language="csharp" from="8" to="8" >}}

    Console.WriteLine(vpc.VpcId);

{{< example-program-snippet path="awsx-vpc" language="csharp" from="17" to="17" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
{{< example-program-snippet path="awsx-vpc" language="java" from="1" to="9" >}}
{{< example-program-snippet path="awsx-vpc" language="java" from="11" to="11" >}}

            System.out.println(vpc.vpcId());

{{< example-program-snippet path="awsx-vpc" language="java" from="17" to="19" >}}
```

{{% /choosable %}}

However, if you update the program as shown above and run `pulumi up`, you will still not receive the value you are looking for as shown in the following CLI output:

{{% choosable language javascript %}}

```bash
# Example CLI output (truncated)
Diagnostics:
  pulumi:pulumi:Stack (aws-js-dev):
    OutputImpl {
      __pulumiOutput: true,
      resources: [Function (anonymous)],
      allResources: [Function (anonymous)],
      isKnown: Promise { <pending> },
      isSecret: Promise { <pending> },
      promise: [Function (anonymous)],
      toString: [Function (anonymous)],
      toJSON: [Function (anonymous)]
    }
```

{{% /choosable %}}

{{% choosable language typescript %}}

```bash
# Example CLI output (truncated)
Diagnostics:
  pulumi:pulumi:Stack (aws-js-dev):
    OutputImpl {
      __pulumiOutput: true,
      resources: [Function (anonymous)],
      allResources: [Function (anonymous)],
      isKnown: Promise { <pending> },
      isSecret: Promise { <pending> },
      promise: [Function (anonymous)],
      toString: [Function (anonymous)],
      toJSON: [Function (anonymous)]
    }
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
# Example CLI output (truncated)
Diagnostics:
  pulumi:pulumi:Stack (aws-iac-dev):
    Calling __str__ on an Output[T] is not supported.
    To get the value of an Output[T] as an Output[str] consider:
    1. o.apply(lambda v: f"prefix{v}suffix")
    See https://www.pulumi.com/docs/concepts/inputs-outputs for more details.
    This function may throw in a future version of Pulumi.
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
# Example CLI output (truncated)
Diagnostics:
  pulumi:pulumi:Stack (aws-go-dev):
    {0xc000137180}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
# Example CLI output (truncated)
Diagnostics:
  pulumi:pulumi:Stack (aws-csharp-dev):
    Calling [ToString] on an [Output<T>] is not supported.
    To get the value of an Output<T> as an Output<string> consider:
    1. o.Apply(v => $"prefix{v}suffix")
    2. Output.Format($"prefix{hostname}suffix");
    See https://www.pulumi.com/docs/concepts/inputs-outputs for more details.
    This function may throw in a future version of Pulumi.
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
# Example CLI output (truncated)
Updating (pulumi/dev)
    Type                                          Name           Status              Info
 +   pulumi:pulumi:Stack                           aws-java-dev     created (1s)        391 messages
 +   └─ awsx:ec2:Vpc                               vpc            created (1s)
...
...

# Nothing is printed

Resources:
    + 34 created

Duration: 2m17s
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
This example is not applicable in YAML.
```

{{% /choosable %}}

This is where {{< pulumi-apply >}} comes into play. There are many resources that have properties of type Output<T>, meaning these property values only become known after the infrastructure has been provisioned. When a Pulumi program is executed with `pulumi up`, the {{< pulumi-apply >}} function will wait for the resource to be created and for its properties to be resolved before printing the desired value of the property. This is not something a standard `print | log` statement is capable of doing.

The syntax of {{< pulumi-apply >}} is shown below:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```javascript
<resource>.<property-name>.apply(<property-name> => <function-to-apply>)
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
<resource>.<property-name>.apply(<property-name> => <function-to-apply>)
```

{{% /choosable %}}

{{% choosable language python %}}

```python
<resource>.<property-name>.apply(lambda <property-name>: <function-to-apply>)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
<resource>.<property-name>.ApplyT(func(<property-name> string) error {
    <function-to-apply>
    return nil
})
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
<resource>.<property-name>.Apply(<property-name> => {
    <function-to-apply>;
    return <property-name>;
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
<resource>.<property-name>().applyValue(<property-name> -> {
    <function-to-apply>;
    return null;
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
You can directly access resource properties without the use of Apply in YAML.
```

{{% /choosable %}}

The breakdown of the different parts of the syntax is as follows:

- `<resource>` is the name of the resource (i.e. `vpc`)
- `<property-name>` is the name of the property to retrieve (i.e. `vpc_id`)
- `<function-to-apply>` is the function to apply against the value of the property

This means that if you want to print out the value of the VPC ID, the program needs to look like the following:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="awsx-vpc" language="javascript" from="1" to="3" >}}

{{< example-program-snippet path="awsx-vpc" language="javascript" from="6" to="6" >}}

vpc.vpcId.apply(id => console.log(`VPC ID: {id}`));
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="awsx-vpc" language="typescript" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="typescript" from="5" to="5" >}}

vpc.vpcId.apply(id => console.log(`VPC ID: {id}`));
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="awsx-vpc" language="python" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="python" from="5" to="5" >}}

vpc.vpc_id.apply(lambda id: print('VPC ID:', id))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="awsx-vpc" language="go" from="1" to="3" >}}
    "fmt"
{{< example-program-snippet path="awsx-vpc" language="go" from="4" to="10" >}}
{{< example-program-snippet path="awsx-vpc" language="go" from="12" to="15" >}}

        vpc.VpcId().ApplyT(func(id string) error {
            fmt.Printf("VPC ID: %s", id)
        	return nil
        })

{{< example-program-snippet path="awsx-vpc" language="go" from="21" to="23" >}}
```

{{% notes %}}
**A note on error handling** The function `ApplyT` spawns a Goroutine to await the availability of the implicated dependencies. This function accepts a `T` or `(T, error)` signature; the latter accomodates for error handling. Alternatively, one may use the `ApplyTWithContext` function in which the provided context can be used to reject the output as canceled. Error handling may also be achieved using an `error` `chan`.
{{% /notes %}}

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="awsx-vpc" language="csharp" from="1" to="6" >}}
{{< example-program-snippet path="awsx-vpc" language="csharp" from="8" to="8" >}}

    vpc.VpcId.Apply(id => { Console.WriteLine($"VPC ID: {id}"); return id; });

{{< example-program-snippet path="awsx-vpc" language="csharp" from="17" to="17" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
{{< example-program-snippet path="awsx-vpc" language="java" from="1" to="9" >}}
{{< example-program-snippet path="awsx-vpc" language="java" from="11" to="11" >}}

            vpc.vpcId().applyValue(i -> {
                System.out.println("VPC ID: " + i);
                return null;
            });

{{< example-program-snippet path="awsx-vpc" language="java" from="17" to="19" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# YAML does not have the Apply method, but you can access values directly.
{{< example-program-snippet path="awsx-vpc" language="yaml" from="1" to="4" >}}
{{< example-program-snippet path="awsx-vpc" language="yaml" from="6" to="7" >}}
{{< example-program-snippet path="awsx-vpc" language="yaml" from="9" to="9" >}}
{{< example-program-snippet path="awsx-vpc" language="yaml" from="11" to="11" >}}
```

{{% /choosable %}}

The above example will wait for the value to be returned from the API and print it to the console as shown below:

```bash
Updating (pulumi/dev)

     Type                 Name         Status     Info
     pulumi:pulumi:Stack  aws-iac-dev             1 message

Diagnostics:
  pulumi:pulumi:Stack (aws-iac-dev):
    VPC ID: vpc-0f8a025738f2fbf2f

Resources:
    34 unchanged

Duration: 12s
```

You can now see the value of the VPC ID property that you couldn't see before when using a regular `print | log` statement.

## Accessing nested output values

Sometimes an output has an object with deeply nested values. There may also be times where the values of these nested properties need to be passed as inputs to other resources. For example, to read a domain record from an ACM certificate, you need to access the domain validation options, which returns an array. Because that value is an output, we would normally need to use {{< pulumi-apply >}}:

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

An easier way to access simple property and array elements is by using _lifting_. Lifting allows you to access properties and elements directly from the {{< pulumi-output >}} itself without needing {{< pulumi-apply >}}. If we return to the above example, we can now simplify it as shown below:

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

In JavaScript and TypeScript, a lifted property access on an `Output<T>` that wraps `undefined` produces another `Output<T>` with the undefined value instead of throwing or producing a faulted `Output<T>`. In other words, lifted property accesses behave like the [`?.` (optional chaining operator)](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html#optional-chaining) in JavaScript and TypeScript. This behavior makes it much easier to form a chain of property accesses on an `Output<T>`.

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

## Creating new output values

The {{< pulumi-apply >}} method can also be used to create new output values, and these new values can also be passed as inputs to another resource. For example, the following code creates an HTTPS URL from the DNS name (the plain value) of a virtual machine (in this case an EC2 instance):

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="javascript" from="1" to="4" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="javascript" from="17" to="19" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="javascript" from="21" to="21" >}}

const url = server.publicDns.apply(dnsName => `https://${dnsName}`);

exports.InstanceUrl = url;
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="typescript" from="1" to="3" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="typescript" from="16" to="18" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="typescript" from="20" to="20" >}}

const url = server.publicDns.apply(dnsName => `https://${dnsName}`);

export const InstanceUrl = url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="python" from="1" to="3" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="python" from="17" to="20" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="python" from="22" to="22" >}}

url = instance.public_dns.apply(
    lambda dns_name: "https://" + dns_name
)

pulumi.export("InstanceUrl", url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="go" from="1" to="9" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="go" from="24" to="26" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="go" from="28" to="31" >}}

        url := server.PublicDns.ApplyT(func(dns string) (string, error) {
			return "https://" + dns
		}).(pulumi.StringOutput)

        ctx.Export("InstanceUrl", url)
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="go" from="35" to="37" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="csharp" from="1" to="7" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="csharp" from="20" to="22" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="csharp" from="24" to="24" >}}

    var url = server.PublicDns.Apply(dns => $"https://{dns}");

{{< example-program-snippet path="aws-ec2-instance-with-sg" language="csharp" from="26" to="27" >}}
        ["InstanceUrl"] = url,
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="csharp" from="30" to="31" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="java" from="1" to="19" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="java" from="32" to="35" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="java" from="37" to="37" >}}

        var url = server.publicDns().applyValue(dns -> "https://" + dns);

        ctx.export("InstanceUrl", url);
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="java" from="41" to="42" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# YAML does not have the Apply method, but you can access values directly.
name: aws-ec2-instance-yaml
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="yaml" from="2" to="4" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="yaml" from="15" to="19" >}}
{{< example-program-snippet path="aws-ec2-instance-with-sg" language="yaml" from="22" to="22" >}}
  InstanceUrl: https://${server.publicDns}
```

{{% /choosable %}}

The CLI output of this code would look something like the following:

```bash
Updating (pulumi/dev)

     Type                 Name         Status
     pulumi:pulumi:Stack  aws-iac-dev
 -   └─ awsx:ec2:Vpc      vpc

Outputs:
    InstanceUrl: "https://ec2-52-59-110-22.eu-central-1.compute.amazonaws.com"

Duration: 5s
```

The result of the call to {{< pulumi-apply >}} is a new Output<T>, meaning the `url` variable is now of type Output. This variable will wait for the new value to be returned from the {{< pulumi-apply >}} function, and any [dependencies](/docs) of the original output (i.e. the `public DNS` property of the `server` resource) are also kept in the resulting Output<T>.

### Outputs and JSON

Often in the course of working with web technologies, you encounter JavaScript Object Notation (JSON) which is a popular specification for representing data. In many scenarios, you'll need to embed resource outputs into a JSON string. In these scenarios, you need to first _wait for the returned_ output, _then_ build the JSON string:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
const contentBucket = new aws.s3.Bucket("content-bucket", {
  acl: "private",
  website: {
    indexDocument: "index.html",
    errorDocument: "index.html",
  },
  forceDestroy: true,
});

const originAccessIdentity = new aws.cloudfront.OriginAccessIdentity(
  "cloudfront",
  {
    comment: pulumi.interpolate`OAI-${contentBucket.bucketDomainName}`,
  }
);

// apply method
new aws.s3.BucketPolicy("cloudfront-bucket-policy", {
  bucket: contentBucket.bucket,
  policy: pulumi
    .all([contentBucket.bucket, originAccessIdentity.iamArn])
    .apply(([bucketName, iamArn]) =>
      JSON.stringify({
        Version: "2012-10-17",
        Statement: [
          {
            Sid: "CloudfrontAllow",
            Effect: "Allow",
            Principal: {
              AWS: iamArn,
            },
            Action: "s3:GetObject",
            Resource: `arn:aws:s3:::${bucketName}/*`,
          },
        ],
      })
    ),
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
bucket = aws.s3.Bucket(
    "content-bucket",
    acl="private",
    website=aws.s3.BucketWebsiteArgs(
        index_document="index.html", error_document="404.html"
    ),
)

origin_access_identity = aws.cloudfront.OriginAccessIdentity(
    "cloudfront",
    comment=pulumi.Output.concat("OAI-", bucket.id),
)

bucket_policy = aws.s3.BucketPolicy(
    "cloudfront-bucket-policy",
    bucket=bucket.bucket,
    policy=pulumi.Output.all(
        cloudfront_iam_arn=origin_access_identity.iam_arn,
        bucket_arn=bucket.arn
    ).apply(
        lambda args: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "CloudfrontAllow",
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": args["cloudfront_iam_arn"],
                        },
                        "Action": "s3:GetObject",
                        "Resource": f"{args['bucket_arn']}/*",
                    }
                ],
            }
        )
    ),
    opts=pulumi.ResourceOptions(parent=bucket)
)
```

{{% /choosable %}}

{{% choosable language go %}}

{{% notes type="info" %}}
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked [here](https://github.com/pulumi/pulumi/issues/12460).

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
{{% /notes %}}

```go
bucket, err := s3.NewBucket(ctx, "content-bucket", &s3.BucketArgs{
	Acl: pulumi.String("private"),
	Website: &s3.BucketWebsiteArgs{
		IndexDocument: pulumi.String("index.html"),
		ErrorDocument: pulumi.String("404.html"),
	},
})
if err != nil {
	return err
}

originAccessIdentity, err := cloudfront.NewOriginAccessIdentity(ctx, "cloudfront", &cloudfront.OriginAccessIdentityArgs{
		Comment: pulumi.Sprintf("OAI-%s", bucket.ID()),
})
if err != nil {
	return err
}

_, err = s3.NewBucketPolicy(ctx, "cloudfront-bucket-policy", &s3.BucketPolicyArgs{
	Bucket: bucket.ID(),
	Policy: pulumi.All(bucket.Arn, originAccessIdentity.IamArn).ApplyT(
		func(args []interface{}) (pulumi.StringOutput, error) {
			bucketArn := args[0].(string)
			iamArn := args[1].(string)

			policy, err := json.Marshal(map[string]interface{}{
				"Version": "2012-10-17",
				"Statement": []map[string]interface{}{
					{
						"Sid":    "CloudfrontAllow",
						"Effect": "Allow",
						"Principal": map[string]interface{}{
							"AWS": iamArn,
						},
						"Action":   "s3:GetObject",
						"Resource": bucketArn + "/*",
					},
				},
			})

			if err != nil {
				return pulumi.StringOutput{}, err
			}
			return pulumi.String(policy).ToStringOutput(), nil
		}).(pulumi.StringOutput),
}, pulumi.Parent(bucket))
if err != nil {
	return err
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var bucket = new Bucket("content-bucket", new BucketArgs
{
    Acl = "private",
    Website = new BucketWebsiteArgs
    {
        IndexDocument = "index.html",
        ErrorDocument = "404.html",
    },
});

var originAccessIdentity = new OriginAccessIdentity("cloudfront", new OriginAccessIdentityArgs
{
    Comment = Output.Format($"OAI-{bucket.Id}"),
});

var bucketPolicy = new BucketPolicy("cloudfront-bucket-policy", new BucketPolicyArgs
{
    Bucket = bucket.Bucket,
    Policy = Output.Tuple(bucket.Arn, originAccessIdentity.IamArn)
    .Apply(t =>
    {
        string bucketArn = t.Item1;
        string cloudfrontIamArn = t.Item2;

        var policy = new
        {
            Version = "2012-10-17",
            Statement = new object[]
            {
                new
                {
                    Sid = "CloudfrontAllow",
                    Effect = "Allow",
                    Principal = new { AWS = cloudfrontIamArn },
                    Action = "s3:GetObject",
                    Resource = $"{bucketArn}/*",
                },
            },
        };

        return JsonSerializer.Serialize(policy);
    }),
}, new CustomResourceOptions { Parent = bucket });
```

{{% /choosable %}}

{{< /chooser >}}

This operation is so common, Pulumi provides first-class helper functions for deserializing JSON string outputs into your language's native objects and serializing your language's native objects to JSON string outputs. These helper functions are designed to remove the process of manually resolving the output inside a {{< pulumi-apply >}}.

### Converting outputs to JSON

You can natively represent the definition of an AWS Step Function State Machine and embed outputs from other resources then convert it to a JSON string.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const stateMachine = new awsnative.stepfunctions.StateMachine("stateMachine", {
    roleArn: sfnRole.arn,
    stateMachineType: "EXPRESS",
    definitionString: pulumi.jsonStringify({
        "Comment": "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": helloFunction.arn, // Pulumi Resource Output
                "Next": "World",
            },
            "World": {
                "Type": "Task",
                "Resource": worldFunction.arn, // Pulumi Resource Output
                "End": true,
            },
        },
    })
});
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
const stateMachine = new awsnative.stepfunctions.StateMachine("stateMachine", {
    roleArn: sfnRole.arn,
    stateMachineType: "EXPRESS",
    definitionString: pulumi.jsonStringify({
        "Comment": "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": helloFunction.arn, // Pulumi Resource Output
                "Next": "World",
            },
            "World": {
                "Type": "Task",
                "Resource": worldFunction.arn, // Pulumi Resource Output
                "End": true,
            },
        },
    })
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
state_machine = aws_native.stepfunctions.StateMachine("stateMachine",
    role_arn=sfn_role.arn,
    state_machine_type="EXPRESS",
    definition_string=pulumi.Output.json_dumps({
        "Comment": "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": hello_function.arn, # Pulumi Resource Output
                "Next": "World",
            },
            "World": {
                "Type": "Task",
                "Resource": world_function.arn, # Pulumi Resource Output
                "End": True,
            },
        },
    })
)
```

{{% /choosable %}}

{{% choosable language go %}}

{{% notes type="info" %}}
The Pulumi Go SDK does not currently support serializing or deserializing maps with unknown values.
It is tracked [here](https://github.com/pulumi/pulumi/issues/12460).

The following is a simplified example of using `pulumi.JSONMarshal` in Go.
{{% /notes %}}

```go
pulumi.JSONMarshal(pulumi.ToMapOutput(map[string]pulumi.Output{
    "bool": pulumi.ToOutput(true),
    "int":  pulumi.ToOutput(1),
    "str":  pulumi.ToOutput("hello"),
    "arr": pulumi.ToArrayOutput([]pulumi.Output{
        pulumi.ToOutput(false),
        pulumi.ToOutput(1.0),
        pulumi.ToOutput(""),
        pulumi.ToMapOutput(map[string]pulumi.Output{
            "key": pulumi.ToOutput("value"),
        }),
    }),
    "map": pulumi.ToMapOutput(map[string]pulumi.Output{
        "key": pulumi.ToOutput("value"),
    }),
    // The following functionality is currently unsupported as myResource
    // is an unknown value.
    "unknown": myResource.ApplyT(func(res interface{}) (interface{}, error) {
        return "Hello World!", nil
    }),
}))
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var stateMachine = Pulumi.Output.JsonSerialize(Output.Create(new {
        Comment = "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
        StartAt = "Hello",
        States = new Dictionary<string, object?>{
        ["Hello"] = new {
            Type = "Task",
            Resource = helloFunction.Arn, // Pulumi Resource Output
            Next = "World",
        },
        ["World"] = new {
            Type = "Task",
            Resource = worldFunction.Arn, // Pulumi Resource Output
            End = true,
        },
    },
}));
```

{{% /choosable %}}

{{< /chooser >}}

### Creating outputs from JSON

You can parse a JSON string into an object and then, inside of an `apply`, manipulate the object to remove all of the policy statements:

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
const jsonIAMPolicy = pulumi.output(`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}`);

const policyWithNoStatements = pulumi.jsonParse(jsonIAMPolicy).apply(policy => {
    // delete the policy statements
    policy.Statement = [];
    return policy;
});
```

For more details [view the Node.js documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
const jsonIAMPolicy = pulumi.output(`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}`);

const policyWithNoStatements: Output<object> = pulumi.jsonParse(jsonIAMPolicy).apply(policy => {
    // delete the policy statements
    policy.Statement = [];
    return policy;
});
```

For more details [view the Node.js documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language python %}}

```python
json_iam_policy = pulumi.Output.from_input('''
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}
''')

def update_policy(policy):
    # delete the policy statements
    policy.update({'Statement': []})
    return policy

policy_with_no_statements = \
    pulumi.Output.json_loads(json_IAM_policy).apply(update_policy)
```

For more details [view the Python documentation](/docs/reference/pkg/python/pulumi/).

{{% /choosable %}}

{{% choosable language go %}}

```go
jsonIAMPolicy := pulumi.ToOutput(`{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}`).(pulumi.StringInput)

policyWithNoStatements := pulumi.JSONUnmarshal(jsonIAMPolicy).ApplyT(
    func(v interface{}) (interface{}, error) {

        // delete the policy statements
        v.(map[string]interface{})["Statement"] = []pulumi.ArrayOutput{}
        return v, nil
    })
```

For more details [view the Go documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var jsonIAMPolicy = Output.Create(@"
        {
            ""Version"": ""2012-10-17"",
            ""Statement"": [
                {
                    ""Sid"": ""VisualEditor0"",
                    ""Effect"": ""Allow"",
                    ""Action"": [
                        ""s3:ListAllMyBuckets"",
                        ""s3:GetBucketLocation""
                    ],
                    ""Resource"": ""*""
                },
                {
                    ""Sid"": ""VisualEditor1"",
                    ""Effect"": ""Allow"",
                    ""Action"": [
                        ""s3:*""
                    ],
                    ""Resource"": ""arn:aws:s3:::my-bucket""
                }
            ]
        }
    ");

var policyWithNoStatements = Pulumi.Output.JsonDeserialize<IAMPolicy>(jsonIAMPolicy).Apply(policy =>
{
    // delete the policy statements.
    policy.Statement = Pulumi.Output.Create(new List<StatementEntry> { });
    return policy;
})
```

For more details [view the .NET documentation](/docs/reference/pkg/dotnet/Pulumi/Pulumi.Output.html).

{{% /choosable %}}

{{< /chooser >}}
