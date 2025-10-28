---
title_tag: "Accessing Single Outputs with Apply | Inputs and Outputs"
meta_desc: "Learn how to access a single output value using the apply method in Pulumi."
title: Accessing single outputs with Apply
h1: Accessing single outputs with Apply
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Apply
        parent: iac-concepts-inputs-outputs
        weight: 1
    concepts:
        weight: 2
        parent: inputs-outputs
aliases:
    - /docs/concepts/inputs-outputs/apply/
---

The `apply` method is used to access the plain value of a single [output](/docs/iac/concepts/inputs-outputs/#outputs) and perform operations on it. Because outputs are asynchronous values that only become known after a resource has finished provisioning, you cannot directly access or manipulate their values using standard language operations (like printing or string concatenation). The `apply` method solves this by waiting for the output value to become available and then executing a function with that plain value.

The `apply` method is typically used for:

- [Printing output values](#accessing-single-output-values) for debugging Pulumi programs
- [Accessing nested values](#accessing-nested-output-values) in complex types (outputs that are objects or dictionaries)
- [Transforming an output](#creating-new-output-values) by referencing its plain value

For more information about what outputs are and why they are necessary in Pulumi programs, see [Inputs and Outputs](/docs/iac/concepts/inputs-outputs/).

{{% notes type="info" %}}
The `apply` method is designed for accessing single output values. If you need to access multiple output values across multiple resources, use Pulumi's [`all` method](/docs/concepts/inputs-outputs/all/) instead.
{{% /notes %}}

{{% notes type="warning" %}}
Creating resources inside an `apply` should be avoided whenever possible. Resources created inside `apply` will not appear in `pulumi preview` unless the output's value is already known. This means the preview output may not match the actual changes when `pulumi up` is run, making it difficult to understand what changes will be made to your infrastructure.

If you need to create a resource that depends on an output value, pass the output directly as an input to the resource instead of using `apply`. Pulumi will automatically handle the dependency tracking and ensure resources are created in the correct order.
{{% /notes %}}

{{% notes type="warning" %}}
You cannot create [stack outputs](/docs/iac/concepts/stacks/#outputs) (using `export` in TypeScript/JavaScript, `pulumi.export()` in Python, `ctx.Export()` in Go, etc.) inside an `apply`. Stack outputs must be created at the top level of your Pulumi program. If you need to export a value that depends on an output, you can export the output directly—Pulumi will automatically handle resolving the value when the stack output is accessed.
{{% /notes %}}

## Accessing single output values { search.keywords="pulumi.apply" }

Suppose you want to print the ID of a resource you've created. These kinds of values are outputs - values that cannot be known until after a resource is provisioned. You might try logging the value like you would any other string:

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

However, if you run the program as shown with `pulumi up`, you will receive something like the following CLI output:

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

This is where {{< pulumi-apply >}} comes into play: When a Pulumi program is executed with `pulumi up`, the {{< pulumi-apply >}} function will wait for the resource to be created and for its properties to be resolved before printing the desired value of the property.

To print out the value of the VPC ID, use the `apply` function:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language javascript %}}

```javascript
{{< example-program-snippet path="awsx-vpc" language="javascript" from="1" to="3" >}}

{{< example-program-snippet path="awsx-vpc" language="javascript" from="6" to="6" >}}

vpc.vpcId.apply(id => console.log(`VPC ID: ${id}`));
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="awsx-vpc" language="typescript" from="1" to="2" >}}

{{< example-program-snippet path="awsx-vpc" language="typescript" from="5" to="5" >}}

vpc.vpcId.apply(id => console.log(`VPC ID: ${id}`));
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
The function `ApplyT` spawns a Goroutine to await the availability of the implicated dependencies. This function accepts a `T` or `(T, error)` signature; the latter accommodates for error handling. Alternatively, one may use the `ApplyTWithContext` function in which the provided context can be used to reject the output as canceled. Error handling may also be achieved using an `error` `chan`.
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
```

## Accessing nested output values

Sometimes a resource has an output property that is an array or a more complex object multiple levels of nested values. For example, if you created an [AWS Certificate Manager certificate resource](/registry/packages/aws/api-docs/acm/certificate/) as shown below:

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

### Using lifting to simplify nested access

An easier way to access deeply nested properties is by using _lifting_. Lifting allows you to access properties and elements directly from a {{< pulumi-output >}} without needing an {{< pulumi-apply >}}.

Lifting is handled automatically by Pulumi's type system, making it largely transparent to use. When you access a property or array element on an output value, Pulumi automatically "lifts" that access into the output context, returning a new output that will resolve to that nested value. This approach is easier to read and write and does not lose any important dependency information that is needed to properly create and maintain the stack.

{{% notes type="info" %}}
Lifting works in most scenarios for accessing nested properties and array elements. However, you may occasionally encounter runtime errors with lifting depending on your language. For example, in TypeScript, if an output resolves to `undefined`, using lifting to reference `outputThatResolvesToUndefined.someProperty` would cause a runtime error. In such cases, use `apply` with appropriate null checking instead.
{{% /notes %}}

Returning to the certificate validation example from the previous section, you can use lifting to simplify the code as shown below:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        // Lifting: Access nested property directly, without apply
        // Type: certCertificate.domainValidationOptions is Output<Array>
        // Result: certCertificate.domainValidationOptions[0].resourceRecordValue is Output<string>
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
let certValidation = new aws.route53.Record("cert_validation", {
    records: [
        // Lifting: Access nested property directly, without apply
        // Type: certCertificate.domainValidationOptions is Output<Array>
        // Result: certCertificate.domainValidationOptions[0].resourceRecordValue is Output<string>
        certCertificate.domainValidationOptions[0].resourceRecordValue
    ],
...
```

{{% /choosable %}}

{{% choosable language python %}}

```python
record = aws.route53.Record('validation',
    records=[
        # Lifting: Access nested property directly, without apply
        # Type: certificate.domain_validation_options is Output[List]
        # Result: certificate.domain_validation_options[0].resource_record_value is Output[str]
        certificate.domain_validation_options[0].resource_record_value
    ],
...
```

{{< notes type="warning" >}}
**Python implementation note**: In Python, output lifting is implemented by overriding the special `__getattr__` method on resources. The expression `resource.output` (which results in a call to `resource.__getattr__("output")`) becomes `resource.apply(lambda r: r.output)`. This means that using `hasattr`, which calls `__getattr__` under the hood and looks for an `AttributeError` to determine whether or not a property exists, will not work as expected on resource outputs.
{{< /notes >}}

{{% /choosable %}}

{{% choosable language go %}}

```go
record, err := route53.NewRecord(ctx, "validation", &route53.RecordArgs{
    Records: pulumi.StringArray{
        // Lifting: Access nested property through helper methods
        // Type: cert.DomainValidationOptions is pulumi.ArrayOutput
        // Operations:
        // * `Index` looks up an index in an `ArrayOutput` and returns a new `Output`.
        // * `ResourceRecordValue` is an accessor method that looks up a property of a
        //   custom struct `Output` and returns a new `Output`.
        // * `Elem` dereferences a `PtrOutput` to an `Output`, equivalent to `*`.
        // Result: pulumi.StringOutput
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
    // Lifting: Partial support in C#
    // Type: cert.DomainValidationOptions is Output<ImmutableArray<T>>
    // Operations:
    // * `GetAt` looks up an index in an `Output<ImmutableArray<T>>` and returns a new `Output<T>`
    // * There are not yet accessor methods for referencing properties like `ResourceRecordValue`
    //   on an `Output<T>` directly, so `Apply` is still needed for the property access.
    Records = cert.DomainValidationOptions.GetAt(0).Apply(opt => opt.ResourceRecordValue!),
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Lifting is currently not supported in Java.
// Use apply as shown in the previous section.
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
        # Type: cert.domainValidationOptions is an array output
        # Result: A string output that resolves to the resource record value
        - ${cert.domainValidationOptions[0].resourceRecordValue}
```

{{% /choosable %}}

{{< /chooser >}}

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

url = server.public_dns.apply(
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

        url := server.PublicDns.ApplyT(func(dns string) string {
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

The returned value of the call to {{< pulumi-apply >}} is a new `pulumi.Output<string>`, meaning the `url` variable is now of an Output. This variable will wait for the new value to be returned from the {{< pulumi-apply >}} function, and any dependencies of the original output (i.e. the `public DNS` property of the `server` resource) are also kept in the resulting `pulumi.Output<string>`.

### Outputs and JSON

Many cloud resources require JavaScript Object Notation (JSON) documents, such as policies that control access to resources. The Pulumi SDK provides helper methods in most languages to make it easier to work with Pulumi outputs and JSON documents. These helper methods have similar names and function signatures to their plain-value analogues.

#### Converting JSON objects to strings

If you need to construct a JSON string using output values from Pulumi resources, you can do so using a JSON stringify helper that is defined in the Pulumi SDK. These helpers unwrap Pulumi outputs without requiring the use of `apply` and produce JSON string outputs suitable for passing to other resources as inputs.

The following example demonstrates using helper methods for JSON serialization:

{{< example-program path="aws-s3-bucketpolicy-jsonstringify" languages="javascript,typescript,python,go,csharp" >}}

#### Converting JSON strings to outputs

If you have an output in the form of a JSON string and you need to interact with it like you would a regular JSON object, you can use Pulumi's parsing helper function.

The following example shows how to use a helper method to parse an IAM policy defined as a `pulumi.Output<string>` into a native object and then manipulate that object to remove all of the policy statements:

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
