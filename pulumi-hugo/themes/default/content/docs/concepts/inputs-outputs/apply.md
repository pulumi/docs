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

Sometimes an output has an object with deeply nested values, and there may be times where the values of these nested properties need to be passed as inputs to other resources. For example, let's say you have created an [AWS Certificate Manager certificate resource](/registry/packages/aws/api-docs/acm/certificate/) as shown below:

{{< example-program path="aws-acm-certificate" >}}

This resource will have outputs that resemble the following:

```plain
# Example truncated output of the ACM certificate resource
cert: {
    arn                      : "arn:aws:acm:eu-central-1..."
    certificate_authority_arn: ""
    certificate_body         : <null>
    certificate_chain        : <null>
    domain_name              : "example.com"
    domain_validation_options: [
        [0]: {
            domain_name          : "example.com"
            resource_record_name : "_0a822dde6347292b.example.com."
            resource_record_type : "CNAME"
            resource_record_value: "_527b1cdf2159204b.mhbtsbpdnt.acm-validations.aws."
        }
    ]
    ...
    ...
}
```

Suppose you want to validate your certificate by creating an [Amazon Route 53 record](/registry/packages/aws/api-docs/route53/record/). To do so, you will need to retrieve the value of the resource record from the ACM certificate. This value is nested in the domain validation options property of the certificate resource, which is an array. Because that value is an output, you would normally need to use {{< pulumi-apply >}} to retrieve it:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
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

{{% choosable language yaml %}}

```yaml
This example is not applicable in YAML.
```

{{% /choosable %}}

{{< /chooser >}}

An easier way to access deeply nested properties is by using _lifting_. Lifting allows you to access properties and elements directly from the {{< pulumi-output >}} itself without needing {{< pulumi-apply >}}. Returning to the example above, your code can now be simplified as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

{{% /choosable %}}

{{% choosable language python %}}

```python
record = aws.route53.Record('validation',
    records=[
        certificate.domain_validation_options[0].resource_record_value
    ],
...
```

{{% /choosable %}}

{{% choosable language go %}}

```go
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

## Creating new output values

### Outputs and Strings

Outputs that return to the engine as strings cannot be used directly in operations such as string concatenation until the output value has returned to Pulumi. In these scenarios, you'll need to wait for the value to return using [`apply`](/docs/concepts/inputs-outputs/apply/).

For example, the following code creates an HTTPS URL from the DNS name (the plain value) of a virtual machine (in this case an EC2 instance):

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

Often in the course of working with web technologies, you encounter JavaScript Object Notation (JSON) which is a popular specification for representing data. In many scenarios, you'll need to embed resource outputs into a JSON string. In these scenarios, you need to first _wait for the returned_ output, _then_ build the JSON string.

For example, let's say you want to create an S3 bucket and a bucket policy that allows the Lambda service to write objects to that bucket. The example below shows how to use `apply` to create the bucket policy JSON object using an output value from the S3 bucket resource (in this case the bucket's ARN):

{{< example-program path="aws-s3bucket-bucketpolicy" >}}

This operation is so common that Pulumi provides first-class helper functions to make it much easier. These helper functions can:

- convert native objects into JSON strings (i.e., serialization)
- convert JSON strings into native objects (i.e., deserialization)

#### Converting JSON objects to strings

If you need to construct a JSON string using output values from Pulumi resources, you can easily do so using a JSON stringify helper. These helpers unwrap Pulumi outputs without requiring the use of `apply` and produce JSON string outputs suitable for passing to other resources as inputs.

For example, you can write the definition of an AWS Step Function State Machine as a native JSON object, embed outputs from other resources (such as a Lambda Function ARN) within the JSON object, and then convert the entire definition into the JSON string representation that is required by the State Machine resource definition:

{{< example-program path="aws-lambda-stepfunctions-jsonhelper" >}}

#### Converting JSON strings to outputs

If you have an output in the form of a JSON string and you need to interact with it like you would a regular JSON object, you can use Pulumi's parsing helper function.

In the example below, you can parse a JSON string into a JSON object and then, inside of an `apply`, manipulate the object to remove all of the policy statements:

{{< example-program path="aws-iampolicy-jsonparse" >}}

{{% choosable language javascript %}}

For more details [view the Node.js documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language typescript %}}

For more details [view the Node.js documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language python %}}

For more details [view the Python documentation](/docs/reference/pkg/python/pulumi/).

{{% /choosable %}}

{{% choosable language go %}}

For more details [view the Go documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

{{% /choosable %}}

{{% choosable language csharp %}}

For more details [view the .NET documentation](/docs/reference/pkg/dotnet/Pulumi/Pulumi.Output.html).

{{% /choosable %}}
