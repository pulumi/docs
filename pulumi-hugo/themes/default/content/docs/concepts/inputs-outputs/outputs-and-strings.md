---
title_tag: "Working with Outputs and Strings | Inputs and Outputs"
meta_desc: "Learn more about outputs and how to use them with strings in Pulumi."
title: Outputs & strings
h1: Working with outputs and strings
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 5
    parent: inputs-outputs
---

Outputs that return to the engine as strings cannot be used directly in operations such as string concatenation until the output has returned to Pulumi. In these scenarios, you'll need to wait for the value to return using [`apply`](/docs/content/inputs-outputs/apply/).

For example, say you want to create a URL from `hostname` and `port` output values. You can do this using `apply` and [`all`](/docs/content/inputs-outputs/all/).

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
hostname := pulumi.String("localhost").ToStringOutput()
port := pulumi.Int(8080).ToIntOutput()

// Would like to produce a string equivalent to: http://${hostname}:${port}/
url := pulumi.All(hostname, port).ApplyT(func (args []interface{}) string {
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

{{% choosable language java %}}

```java
Output<String> hostname = Output.of("localhost"); // get some Output
Output<Integer> port = Output.of(8080); // get some Output

// Would like to produce a string equivalent to: http://{hostname}:{port}/
var url = Output.tuple(hostname, port)
        .applyValue(t -> String.format("http://%s:%s/", t.t1, t.t2));
```

{{% /choosable %}}

{{< /chooser >}}

However, this approach is verbose and unwieldy. To make this common task easier, Pulumi exposes interpolation helpers that allow you to create strings that contain outputs. These interpolation methods wrap [all](/docs/concepts/inputs-outputs/all/) and [apply](/docs/concepts/inputs-outputs/apply/) with an interface that resembles your language's native string formatting functions.

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
# format takes a template string and a list of args or keyword args and formats the string, expanding outputs correctly:
url2 = Output.format("http://{0}:{1}/", hostname, port);
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

{{% choosable language java %}}

```java
// Format takes a FormattableString and expands outputs correctly:
var url = Output.format("http://%s:%s/", hostname, port);
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
variables:
  url: https://${hostname}:${port}
```

{{% /choosable %}}

You can use string interpolation to export a stack output, provide a dynamically computed string as a new resource argument, or even for diagnostic purposes.
