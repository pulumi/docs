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

To demonstrate, let's say we have the following simple program that creates a VPC resource in AWS. In this program, we have added a print/log statement to print the `vpc` variable so that we can see the properties of this resource.

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

As shown above, using this method will not provide a JSON representation of the VPC resource complete with its properties and associated property values. This is because, when it comes to Pulumi resource classes, there is no custom `String` method that outputs this kind of JSON representation for each resource.

Ultimately, if you want to view the properties of a resource, you will need to access them individually using {{< pulumi-apply >}}.

## Using Apply { search.keywords="pulumi.apply" }

Let's say we want to print the ID of the VPC we've created. Given that this is an individual resouce property and not the entire resource itself, we could try logging the value like normal:

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

However, if we update our program as shown above and run `pulumi up`, we will still not receive the value we are looking for as shown in the following CLI output:

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

This is where {{< pulumi-apply >}} comes into play. As mentioned before, all properties of a resource are of type Output<T>, meaning the values only become known after the infrastructure has been provisioned. When a Pulumi program is executed with `pulumi up`, the {{< pulumi-apply >}} function will wait for the resource to be created and for its properties to be resolved before printing the desired value of the property. This is not something a standard `print | log` statement is capable of doing.

### Accessing single output values

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

{{< notes type="warning" >}}
The {{< pulumi-apply >}} method should only be used on a resource's properties and never on the whole resource itself. Using apply directly on a resource will result in unexpected issues and errors.
{{< /notes >}}

This means that if we want to print out the value of our VPC ID, our program needs to look like the following:

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

We can now see the value of the VPC ID property that we couldn't see before when using a regular `print | log` statement.

### Creating new output values

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

{{< notes type="info" >}}
During some program executions, {{< pulumi-apply >}} does not run. For example, it won’t run during `pulumi preview` when resource output values may be unknown. Therefore, you should avoid side-effects within the callbacks, such as allocating new resources within `apply`, as it could lead to `pulumi preview` being wrong.
{{< /notes >}}
