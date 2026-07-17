---
title_tag: "Accessing Single Outputs with Apply | Inputs and Outputs"
meta_desc: "Learn how to access a single output value using the apply method in Pulumi."
title: Accessing single outputs with Apply
h1: Accessing single outputs with Apply
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

- [Printing output values](#printing-output-values) for debugging Pulumi programs
- [Accessing nested values](#accessing-nested-output-values) in complex types (outputs that are objects or dictionaries)
- [Transforming an output](#creating-new-output-values) by referencing its plain value
- [Converting inputs to outputs](#converting-inputs-to-outputs) to call `apply` on a value typed as `Input<T>`

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

{{% notes type="info" %}}
The `apply` method does not apply to Pulumi YAML. YAML is a declarative language with no facility for running a function against a resolved value, so it has no `apply` equivalent. To use an output value in a YAML program, reference it directly with interpolation syntax (for example, `${myResource.myProperty}`) and Pulumi resolves the value for you. For this reason, the examples on this page do not include YAML.
{{% /notes %}}

## Printing output values { search.keywords="pulumi.apply" }

Suppose you want to print the ID of a resource you've created. These kinds of values are outputs - values that cannot be known until after a resource is provisioned. You might try logging the value like you would any other string:

{{< chooser language "typescript,python,go,csharp,java" / >}}

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

This is where {{< pulumi-apply >}} comes into play: When a Pulumi program is executed with `pulumi up`, the {{< pulumi-apply >}} function will wait for the resource to be created and for its properties to be resolved before printing the desired value of the property.

To print out the value of the VPC ID, use the `apply` function:

{{< chooser language "typescript,python,go,csharp,java" / >}}

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
The function `ApplyT` spawns a Goroutine to await the availability of the implicated dependencies. This function accepts a `T` or `(T, error)` signature; the latter accommodates for error handling. Alternatively, one may use the `ApplyTWithContext` function in which the provided context can be used to reject the output as canceled. Error handling may also be achieved using an `error` `chan`. For details on how errors returned from the callback surface during an update, see [Handling errors in apply](#handling-errors-in-apply).
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

{{< chooser language "typescript,python,go,csharp,java" / >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="apply-nested-output-values" language="typescript" from="1" to="10" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="apply-nested-output-values" language="python" from="1" to="10" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="apply-nested-output-values" language="go" from="1" to="24" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="apply-nested-output-values" language="csharp" from="1" to="16" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
{{< example-program-snippet path="apply-nested-output-values" language="java" from="1" to="24" >}}
```

{{% /choosable %}}

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

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="apply-nested-output-values" language="typescript" from="12" to="24" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="apply-nested-output-values" language="python" from="12" to="27" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="apply-nested-output-values" language="go" from="26" to="44" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="apply-nested-output-values" language="csharp" from="18" to="26" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
{{< example-program-snippet path="apply-nested-output-values" language="java" from="26" to="39" >}}
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

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="apply-nested-output-values" language="typescript" from="26" to="35" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="apply-nested-output-values" language="python" from="29" to="38" >}}
```

{{< notes type="warning" >}}
**Python implementation note**: In Python, output lifting is implemented by overriding the special `__getattr__` method on resources. The expression `resource.output` (which results in a call to `resource.__getattr__("output")`) becomes `resource.apply(lambda r: r.output)`. This means that using `hasattr`, which calls `__getattr__` under the hood and looks for an `AttributeError` to determine whether or not a property exists, will not work as expected on resource outputs.
{{< /notes >}}

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="apply-nested-output-values" language="go" from="46" to="58" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="apply-nested-output-values" language="csharp" from="28" to="36" >}}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// Lifting is currently not supported in Java.
// Use apply as shown in the previous section.
```

{{% /choosable %}}

{{< /chooser >}}

## Creating new output values

### Outputs and strings

Outputs that return to the engine as strings cannot be used directly in operations such as string concatenation until the output value has returned to Pulumi. In these scenarios, you'll need to wait for the value to return using [`apply`](/docs/concepts/inputs-outputs/apply/).

{{% notes type="info" %}}
For the common case of building a string from output values, Pulumi's [output helpers](/docs/concepts/inputs-outputs/helpers/#string-interpolation) provide a more concise alternative that doesn't require calling `apply` directly.
{{% /notes %}}

For example, the following code creates an HTTPS URL from the DNS name (the plain value) of a virtual machine (in this case an EC2 instance):

{{< chooser language "typescript,python,go,csharp,java" / >}}

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

Many cloud resources require JavaScript Object Notation (JSON) documents, such as policies that control access to resources. The Pulumi SDK provides helper methods in most languages to make it easier to work with Pulumi outputs and JSON documents. These helper methods have similar names and function signatures to their plain-value analogues. For a consolidated reference of all JSON helpers, see [Using output helpers](/docs/concepts/inputs-outputs/helpers/#json-helpers).

#### Converting JSON objects to strings

If you need to construct a JSON string using output values from Pulumi resources, you can do so using a JSON stringify helper that is defined in the Pulumi SDK. These helpers unwrap Pulumi outputs without requiring the use of `apply` and produce JSON string outputs suitable for passing to other resources as inputs.

The following example demonstrates using helper methods for JSON serialization:

{{< example-program path="aws-s3-bucketpolicy-jsonstringify" languages="typescript,python,go,csharp,java" >}}

When constructing a JSON policy document, it is often necessary to build a resource identifier by appending a path suffix to an output value. For example, Amazon S3 bucket policies that apply to objects rather than to the bucket itself require a resource ARN ending in `/*`. Because the bucket ARN is a Pulumi output, you must combine the JSON stringify helper with your language's string interpolation facility to produce the correct value.

The following example demonstrates this pattern, using the bucket's ARN as a base and appending `/*` to target all objects in the bucket:

{{< example-program path="aws-s3-bucketpolicy-jsonstringify-interpolate" languages="typescript,python,go,csharp,java" >}}

#### Converting JSON strings to outputs

If you have an output in the form of a JSON string and you need to interact with it like you would a regular JSON object, you can use Pulumi's parsing helper function.

The following example shows how to use a helper method to parse an IAM policy defined as a `pulumi.Output<string>` into a native object and then manipulate that object to remove all of the policy statements:

{{< example-program path="aws-iampolicy-jsonparse" languages="typescript,python,go,csharp,java" >}}

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

For more details [view the .NET documentation](/docs/reference/pkg/dotnet/pulumi/pulumi.output.html).

{{% /choosable %}}

## Handling errors in apply

The function you pass to {{< pulumi-apply >}} can fail—for example, when a resolved value doesn't meet a condition your program requires. In every Pulumi language, an unhandled error raised inside an `apply` callback is reported as a deployment failure: `pulumi up` aborts the update and prints the error in its diagnostics. The error is not swallowed (with one Go-specific exception described below), and the language process is not left in an unrecoverable state—you do not need to wrap `apply` in your language's try/catch construct to surface it. In fact, raising an error from inside the callback is the idiomatic way to fail an update when a value doesn't satisfy a requirement.

How you signal an error from the callback depends on the language.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

Throw an exception from the callback (or return a rejected promise). The thrown error rejects the resulting output and fails the update.

```typescript
const validated = name.apply(n => {
    if (!n.includes("a")) {
        throw new Error(`name "${n}" must contain the letter 'a'`);
    }
    return n;
});
```

The update fails whether or not `validated` is later used in the program.

{{% /choosable %}}

{{% choosable language python %}}

Raise an exception from the callback. The exception rejects the resulting output and fails the update.

```python
def validate(n: str) -> str:
    if "a" not in n:
        raise Exception(f'name "{n}" must contain the letter \'a\'')
    return n

validated = name.apply(validate)
```

The update fails whether or not `validated` is later used in the program.

{{% /choosable %}}

{{% choosable language go %}}

Return a non-nil error as the second return value. The `ApplyT` callback accepts either a `func(T) U` or a `func(T) (U, error)` signature; the second form is what lets you report an error. Returning an error does **not** panic—it rejects the resulting output.

```go
validated := name.ApplyT(func(n string) (string, error) {
    if !strings.Contains(n, "a") {
        return "", fmt.Errorf("name %q must contain the letter 'a'", n)
    }
    return n, nil
})
```

{{% notes type="warning" %}}
Unlike the other Pulumi languages, Go surfaces a rejected output's error only when the output is _consumed_—that is, exported as a [stack output](/docs/iac/concepts/stacks/#outputs) or passed as an input to another resource. If you call `ApplyT` purely for a side effect (such as printing) and discard the returned output, an error you return from the callback is silently dropped and the update succeeds. To make sure validation errors fail the update, either consume the resulting output or handle the error inside the callback.
{{% /notes %}}

For cancellation-aware error handling, use `ApplyTWithContext`, whose callback receives a `context.Context` that can be used to reject the output when the context is canceled.

{{% /choosable %}}

{{% choosable language csharp %}}

Throw an exception from the callback. The thrown error rejects the resulting output and fails the update.

```csharp
var validated = name.Apply(n =>
{
    if (!n.Contains("a"))
    {
        throw new Exception($"name \"{n}\" must contain the letter 'a'");
    }
    return n;
});
```

The update fails whether or not `validated` is later used in the program.

{{% /choosable %}}

{{% choosable language java %}}

Throw an exception from the callback. The thrown error rejects the resulting output and fails the update.

```java
var validated = name.applyValue(n -> {
    if (!n.contains("a")) {
        throw new RuntimeException("name \"" + n + "\" must contain the letter 'a'");
    }
    return n;
});
```

The update fails whether or not `validated` is later used in the program.

{{% /choosable %}}

{{< /chooser >}}

To handle a potential failure gracefully and continue rather than failing the update, do the handling inside the callback—for example, catch the error and return a fallback value instead of raising.

## Converting inputs to outputs

Resource arguments in Pulumi accept `Input<T>` values, which means they will take either a plain value or an `Output<T>`. In most programs this flexibility is all you need. There are situations, however, where you have a value typed as `Input<T>` and need to ensure it is a definite `Output<T>`—most commonly to call `apply` on it.

This situation arises most often in the following cases:

- **Writing a component resource.** Component constructors typically accept `Input<T>` parameters to give callers the flexibility to pass either a plain value or an existing output. Inside the component body, you often need to call `apply` or chain other output operations on those parameters, which requires `Output<T>`.
- **Writing utility functions that accept `Input<T>`.** A function that accepts `Input<T>` for caller flexibility must convert to `Output<T>` internally before it can call `apply` to perform any transformation.
- **Combining values with `all`.** While the `all` function accepts a mix of plain values and outputs in most SDKs, explicitly converting to outputs first can make your program’s data flow clearer and more predictable.

Pulumi's SDKs provide a dedicated function to wrap any `Input<T>` as a guaranteed `Output<T>`:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

`pulumi.output()` accepts any `Input<T>`—a plain value or an existing `Output<T>`—and returns `Output<T>`. The example below defines a helper that requires `Output<string>` internally, then calls it with both a plain string and with an `Output<string>` from a resource to show that both work.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

function buildUrl(host: pulumi.Input<string>): pulumi.Output<string> {
    return pulumi.output(host).apply(h => `https://${h}`);
}

const fromPlain = buildUrl("example.com");

const bucket = new aws.s3.BucketV2("my-bucket");
const fromOutput = buildUrl(bucket.websiteEndpoint);
```

{{% /choosable %}}

{{% choosable language python %}}

`pulumi.Output.from_input()` accepts any `Input[T]`—a plain value or an existing `Output[T]`—and returns `Output[T]`.

```python
import pulumi
import pulumi_aws as aws

# A helper function that accepts Input[str] but needs to call apply.
def build_url(host: pulumi.Input[str]) -> pulumi.Output[str]:
    return pulumi.Output.from_input(host).apply(lambda h: f"https://{h}")

# Works with a plain string.
from_plain = build_url("example.com")

# Works equally well with an Output[str] from a resource.
bucket = aws.s3.BucketV2("my-bucket")
from_output = build_url(bucket.website_endpoint)
```

{{% /choosable %}}

{{% choosable language go %}}

In Go, each typed input interface exposes a `ToXxxOutput()` method that returns the corresponding concrete output type. For example, `pulumi.StringInput` provides `ToStringOutput()`. The snippet below defines a helper that requires `pulumi.StringOutput` internally, then calls it with both a plain value and a `StringOutput` from a resource.

```go
import (
    awss3 "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func buildURL(input pulumi.StringInput) pulumi.StringOutput {
    return input.ToStringOutput().ApplyT(func(host string) string {
        return "https://" + host
    }).(pulumi.StringOutput)
}

// Inside a Pulumi program:
fromPlain := buildURL(pulumi.String("example.com"))

bucket, _ := awss3.NewBucketV2(ctx, "my-bucket", nil, nil)
fromOutput := buildURL(bucket.Bucket)
```

Each typed input interface in the Go SDK—`pulumi.StringInput`, `pulumi.IntInput`, `pulumi.BoolInput`, and so on—follows this same `ToXxxOutput()` pattern.

{{% /choosable %}}

{{% choosable language csharp %}}

In C#, `Input<T>` exposes `Apply` through Pulumi SDK extension methods, so you can often call `Apply` without an explicit conversion step:

```csharp
// Input<T> supports Apply through extension methods in the Pulumi C# SDK.
Input<string> host = "example.com"; // could be a plain string or Output<string>
Output<string> url = host.Apply(h => $"https://{h}");
```

When you need to construct a standalone `Output<T>` from a plain value, use `Output.Create`:

```csharp
Output<string> output = Output.Create("example.com");
```

{{% /choosable %}}

{{% choosable language java %}}

`Output.of()` wraps a plain value as an `Output<T>`. When your value is already an `Output<T>`, you can use it directly without any conversion.

```java
import com.pulumi.core.Output;

Output<String> output = Output.of("example.com");
Output<String> url = output.applyValue(host -> "https://" + host);
```

{{% /choosable %}}

{{< /chooser >}}

When the value you pass is already an `Output<T>`, the conversion function returns it unchanged. When you pass a plain value, Pulumi wraps it in a new output that resolves immediately with that value. In either case, the result is a definite `Output<T>` on which you can call `apply` or any other output method.
