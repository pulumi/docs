---
title_tag: "Using Output Helpers | Inputs and Outputs"
meta_desc: "Learn how to use Pulumi's built-in output helper functions for string interpolation and JSON serialization."
title: Using output helpers
h1: Using output helpers
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Helpers
        parent: iac-concepts-inputs-outputs
        weight: 3
aliases:
    - /docs/concepts/inputs-outputs/helpers/
---

Pulumi's SDKs include helper functions designed for the most common output manipulation tasks: constructing strings from output values and working with JSON. These helpers wrap [`apply`](/docs/concepts/inputs-outputs/apply/) and [`all`](/docs/concepts/inputs-outputs/all/) internally, but expose a more concise interface that closely mirrors each language's native string and JSON facilities.

Using a helper is usually the right choice when you need to build a string from one or more outputs or serialize a data structure that contains outputs to JSON. Using `apply` or `all` directly gives you more flexibility when the transformation you need is more complex.

## String interpolation

Pulumi's string interpolation helpers let you construct a string from one or more output values without calling `apply` or `all` explicitly. The helpers work for both a single output and multiple outputs, so they serve as a convenient shorthand regardless of how many values you are combining.

{{< example-program path="aws-s3bucket-bucketobject-interpolate" >}}

{{% choosable language typescript %}}

TypeScript and JavaScript provide two string helpers:

- **`pulumi.interpolate`** — A tagged template literal that accepts Pulumi outputs directly inside `${}` expressions. It is the most idiomatic option in TypeScript and handles any number of values.
- **`pulumi.concat()`** — Concatenates a list of strings and outputs into a single `Output<string>`. Useful when you are building a string from a dynamic list of values rather than a fixed template.

For more details, see the [Node.js SDK documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/).

{{% /choosable %}}

{{% choosable language python %}}

Python provides two string helpers:

- **`pulumi.Output.format()`** — Works like Python's `str.format()`, accepting a format string with positional or keyword placeholders. This is the most idiomatic option for Python programs.
- **`pulumi.Output.concat()`** — Concatenates a list of strings and outputs into a single `Output[str]`.

For more details, see the [Python SDK documentation](/docs/reference/pkg/python/pulumi/).

{{% /choosable %}}

{{% choosable language go %}}

Go provides:

- **`pulumi.Sprintf()`** — Works like Go's `fmt.Sprintf()`, accepting a format string and a variadic list of arguments that may be plain values or Pulumi outputs. Returns a `pulumi.StringOutput`.

For more details, see the [Go SDK documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

{{% /choosable %}}

{{% choosable language csharp %}}

.NET provides:

- **`Output.Format()`** — Works like C#'s interpolated string syntax. Pass a C# interpolated string containing `Output<T>` values, and `Output.Format` returns a single `Output<string>`.

For more details, see the [.NET SDK documentation](/docs/reference/pkg/dotnet/Pulumi/Pulumi.Output.html).

{{% /choosable %}}

{{% choosable language java %}}

Java provides:

- **`Output.format()`** — Works like Java's `String.format()`, accepting a format string with `%s` placeholders and a list of arguments that may be plain values or Pulumi outputs. Returns an `Output<String>`.

For more details, see the [Java SDK documentation](/docs/reference/pkg/java/).

{{% /choosable %}}

{{% choosable language yaml %}}

Pulumi YAML supports string interpolation natively. Use `${...}` syntax directly within any string value to reference resource outputs or variables:

```yaml
outputs:
  s3Url: s3://${bucket.id}/${bucketObject.key}
```

For more details, see the [YAML language reference](/docs/iac/languages-sdks/yaml/yaml-language-reference/#expressions).

{{% /choosable %}}

## JSON helpers

Many cloud resources accept JSON strings as inputs — IAM policies, Lambda function configurations, S3 bucket policies, and others. Pulumi's JSON helpers let you work with data structures that contain outputs without needing to call `apply` manually to extract the underlying values.

### Converting outputs to JSON strings

If you need to produce a JSON string from a data structure that contains one or more output values, use one of the JSON stringify helpers. These helpers accept a mix of plain values and Pulumi outputs, serialize the entire structure to JSON, and return an `Output<string>` suitable for passing to another resource as an input.

{{< example-program path="aws-s3-bucketpolicy-jsonstringify" languages="javascript,typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

- **`pulumi.jsonStringify()`** — Accepts a value or output object and returns an `Output<string>` of its JSON representation. Equivalent in behavior to `JSON.stringify()`.

For more details, see the [Node.js SDK documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/functions/jsonStringify.html).

{{% /choosable %}}

{{% choosable language python %}}

- **`pulumi.Output.json_dumps()`** — Accepts a value or output and returns an `Output[str]` of its JSON representation. Equivalent in behavior to `json.dumps()`.

For more details, see the [Python SDK documentation](/docs/reference/pkg/python/pulumi/#pulumi.Output.json_dumps).

{{% /choosable %}}

{{% choosable language go %}}

- **`pulumi.JSONMarshal()`** — Accepts a `pulumi.Input` value and marshals it to a JSON string output using Go's `encoding/json` package.

For more details, see the [Go SDK documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

{{% /choosable %}}

{{% choosable language csharp %}}

- **`Output.JsonSerialize()`** — Accepts an `Output<T>` and returns an `Output<string>` of its JSON representation using `System.Text.Json`.

For more details, see the [.NET SDK documentation](/docs/reference/pkg/dotnet/Pulumi/Pulumi.Output.html).

{{% /choosable %}}

### Converting JSON strings to outputs

If you have an output in the form of a JSON string and need to read individual fields from it or pass it to a function that expects a plain object, use one of the JSON parse helpers. These accept an output containing a JSON string and return a deserialized output.

{{< example-program path="aws-iampolicy-jsonparse" >}}

{{% choosable language typescript %}}

- **`pulumi.jsonParse()`** — Accepts an `Output<string>` and returns an `Output<any>` of the parsed value. Equivalent in behavior to `JSON.parse()`.

For more details, see the [Node.js SDK documentation](/docs/reference/pkg/nodejs/pulumi/pulumi/functions/jsonParse.html).

{{% /choosable %}}

{{% choosable language python %}}

- **`pulumi.Output.json_loads()`** — Accepts an `Output[str]` and returns a deserialized output. Equivalent in behavior to `json.loads()`.

For more details, see the [Python SDK documentation](/docs/reference/pkg/python/pulumi/#pulumi.Output.json_loads).

{{% /choosable %}}

{{% choosable language go %}}

Go does not have a dedicated JSON parse helper. Use `ApplyT` with `json.Unmarshal` to parse a JSON string output into a Go struct or map.

For more details, see the [Go SDK documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi).

{{% /choosable %}}

{{% choosable language csharp %}}

- **`Output.JsonDeserialize<T>()`** — Accepts an `Output<string>` containing JSON and returns an `Output<T>` of the deserialized value using `System.Text.Json`.

For more details, see the [.NET SDK documentation](/docs/reference/pkg/dotnet/Pulumi/Pulumi.Output.html).

{{% /choosable %}}
