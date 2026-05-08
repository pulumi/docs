---
title_tag: "Inputs & Outputs in Go | Languages & SDKs"
meta_desc: A comprehensive guide to using the Pulumi Go SDK's input and output types, including helper constructors, ApplyT, All, output lifting, and common patterns.
title: Inputs & outputs in Go
h1: Inputs & outputs in Go
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Inputs & outputs
        parent: iac-languages-go
        weight: 3
    languages:
        parent: go
        weight: 3
aliases:
    - /docs/languages-sdks/go/go-inputs-outputs/
---

The Pulumi Go SDK expresses inputs and outputs through a system of typed interfaces and concrete wrapper types that map directly onto Go's static type system. If you are already familiar with the [general concept of inputs and outputs](/docs/iac/concepts/inputs-outputs/), this page explains how those ideas are realized in Go specifically—covering the typed helper constructors, the `ApplyT` transformation function, output lifting, and a set of patterns that regularly come up when writing real programs.

## Inputs

Every resource constructor in the Go SDK accepts an `Args` struct whose fields are typed as input interfaces. For example, the `BucketArgs` struct in the AWS S3 provider has fields typed as `pulumi.StringInput`, `pulumi.BoolInput`, and so on. The `pulumi.XxxInput` interfaces are satisfied both by plain Go values wrapped in a helper and by `Output` values produced by other resources—this is what allows you to wire resources together without explicit sequencing logic.

### Constructing input values

The SDK provides a family of helper functions that wrap plain Go values in the appropriate input type:

```go
pulumi.String("us-east-1")        // pulumi.StringInput
pulumi.Int(8080)                   // pulumi.IntInput
pulumi.Bool(true)                  // pulumi.BoolInput
pulumi.Float64(3.14)               // pulumi.Float64Input
```

For optional fields that accept a pointer type, use the `Ptr` variants:

```go
pulumi.StringPtr("optional-value") // *string
pulumi.IntPtr(8080)                // *int
pulumi.BoolPtr(false)              // *bool
pulumi.Float64Ptr(1.5)             // *float64
```

The pointer helpers are typically needed when a resource argument is typed as `*string` (or similar) rather than `pulumi.StringInput`. Resource codegen produces both variants depending on whether the underlying provider schema marks the property as optional.

### Collection inputs

For array and map arguments, the SDK provides the corresponding collection types. Each element is itself an input, so you can mix plain values and outputs freely:

```go
// Array of string inputs
pulumi.StringArray{
    pulumi.String("subnet-aaa111"),
    pulumi.String("subnet-bbb222"),
}

// Map of string inputs
pulumi.StringMap{
    "Environment": pulumi.String("production"),
    "Team":        pulumi.String("platform"),
}

// Array of integer inputs
pulumi.IntArray{
    pulumi.Int(80),
    pulumi.Int(443),
}
```

The naming convention is consistent: `pulumi.XxxArray` for slices and `pulumi.XxxMap` for maps, where `Xxx` is the base type name.

Passing an output from another resource as an element works the same way because output types like `pulumi.StringOutput` implement `pulumi.StringInput`:

```go
// Passing a resource output as an element in an array input.
pulumi.StringArray{
    pulumi.String("subnet-static"),
    mySubnet.ID(), // pulumi.IDOutput also implements pulumi.StringInput
}
```

## Outputs

When a resource is created, its properties become available as output values. In Go, each property is a concrete typed output wrapper—`pulumi.StringOutput`, `pulumi.IntOutput`, `pulumi.BoolOutput`, `pulumi.Float64Output`, and many others. These wrappers embed the base `pulumi.Output` type and add type-specific methods.

You cannot read an output value directly as a plain Go value while the program is running. Outputs are resolved asynchronously after Pulumi deploys the resource, so the SDK requires you to work with them through the transformation and combination functions described below.

```go
bucket, err := s3.NewBucket(ctx, "my-bucket", nil)
if err != nil {
    return err
}

// bucket.Bucket is a pulumi.StringOutput — it is not a plain string.
// Passing it to another resource as an input works directly because
// pulumi.StringOutput implements pulumi.StringInput.
_, err = s3.NewBucketObject(ctx, "index", &s3.BucketObjectArgs{
    Bucket: bucket.Bucket, // wired directly, no conversion needed
    Key:    pulumi.String("index.html"),
})
if err != nil {
    return err
}
```

## Transforming outputs with ApplyT

`ApplyT` is the primary way to access the underlying value of an output and produce a new output from it. The function you pass to `ApplyT` receives the resolved plain Go value and returns a new value (or a `(value, error)` pair). Pulumi schedules this function to run only after the output has been resolved.

```go
// Derive a new StringOutput from an existing one.
url := bucket.Bucket.ApplyT(func(name string) string {
    return "https://" + name + ".s3.amazonaws.com"
}).(pulumi.StringOutput)
```

Because `ApplyT` accepts and returns the untyped `pulumi.Output` interface, the result must be type-asserted to the concrete output type you expect. The type assertion `.(pulumi.StringOutput)` is idiomatic Go and will panic at program startup if the types do not match—a mismatch is always a programming error, never a runtime condition.

When the transformation can fail, return `(value, error)`:

```go
port := rawPortOutput.ApplyT(func(s string) (int, error) {
    n, err := strconv.Atoi(s)
    if err != nil {
        return 0, fmt.Errorf("invalid port %q: %w", s, err)
    }
    return n, nil
}).(pulumi.IntOutput)
```

If you need access to a `context.Context` for cancellation or deadline propagation, use `ApplyTWithContext`:

```go
result := myOutput.ApplyTWithContext(ctx, func(ctx context.Context, v string) string {
    // ctx is the Pulumi run context; it is cancelled if the run is cancelled.
    return strings.TrimSpace(v)
}).(pulumi.StringOutput)
```

{{% notes type="warning" %}}
Avoid creating resources inside `ApplyT`. Resources created inside a transformation function are not visible to `pulumi preview` unless the output's value is already known, which makes previews unreliable. Pass the output directly to the resource's input arguments instead, and let Pulumi track the dependency automatically.
{{% /notes %}}

## Combining multiple outputs with All

When a transformation needs values from more than one output, use `pulumi.All`. It accepts any number of `Output` values and passes their resolved plain values to the callback as a `[]interface{}` slice:

```go
// Build a connection string from two separate outputs.
connStr := pulumi.All(dbInstance.Address, dbInstance.Port).ApplyT(
    func(args []interface{}) string {
        host := args[0].(string)
        port := args[1].(int)
        return fmt.Sprintf("postgres://%s:%d/mydb", host, port)
    },
).(pulumi.StringOutput)
```

Each element of `args` must be type-asserted to its underlying Go type—in the order the outputs were passed to `All`. The result of `All(...).ApplyT(...)` is type-asserted to the expected output type, just as with a plain `ApplyT`.

## Converting inputs to outputs

Resource component constructors typically accept `pulumi.XxxInput` parameters to give callers the flexibility to pass either a plain value or an existing output. Inside the component body, if you need to call `ApplyT` on such a parameter, you must first convert it to the corresponding output type using the `ToXxxOutput()` method that every typed input interface provides:

```go
// A component constructor accepts a flexible input.
func NewEndpointBuilder(
    ctx *pulumi.Context,
    name string,
    host pulumi.StringInput,
    opts ...pulumi.ResourceOption,
) (*EndpointBuilder, error) {
    // ToStringOutput() converts any StringInput to a guaranteed StringOutput,
    // enabling ApplyT to be called on it regardless of whether the caller
    // passed a plain string or an existing output.
    url := host.ToStringOutput().ApplyT(func(h string) string {
        return "https://" + h
    }).(pulumi.StringOutput)

    // ...
}
```

The `ToXxxOutput()` methods are generated for each typed input interface in the SDK. `pulumi.StringInput` has `ToStringOutput()`, `pulumi.IntInput` has `ToIntOutput()`, and so forth. When the input is already an output (which is a common case), the method is a no-op and returns the same underlying output directly.

## Output lifting

For structured output types—arrays, maps, and objects—the Go SDK generates typed accessor methods that let you extract a nested field without writing an explicit `ApplyT`. This is called output lifting and usually produces cleaner code when you only need a single nested value.

```go
cert, err := acm.NewCertificate(ctx, "cert", &acm.CertificateArgs{
    DomainName:       pulumi.String("example.com"),
    ValidationMethod: pulumi.String("DNS"),
})
if err != nil {
    return err
}

// ApplyT approach: extract a nested field from the first validation option.
recordName := cert.DomainValidationOptions.ApplyT(
    func(opts []acm.CertificateDomainValidationOption) string {
        return *opts[0].ResourceRecordName
    },
).(pulumi.StringOutput)

// Lifting approach: use generated Index/accessor methods on the output type.
// This is equivalent and typically more concise.
recordNameLifted := cert.DomainValidationOptions.
    Index(pulumi.Int(0)).
    ResourceRecordName().
    Elem()
```

The `.Index()` method is available on array output types and returns the output for a single element. The generated accessor methods like `.ResourceRecordName()` then expose the fields of structured elements. `.Elem()` dereferences a pointer output (`*pulumi.StringOutput`) to its value type (`pulumi.StringOutput`).

Not all output types have generated accessors; when they are absent, `ApplyT` is the right tool.

## String formatting with Sprintf

`pulumi.Sprintf` produces a `pulumi.StringOutput` from a format string that may contain output values. It works like Go's `fmt.Sprintf` but accepts `pulumi.Output` arguments alongside plain values:

```go
// pulumi.Sprintf returns a pulumi.StringOutput.
bucketUrl := pulumi.Sprintf("https://%s.s3.amazonaws.com", bucket.Bucket)
```

This is usually more readable than an equivalent `ApplyT` or `All` when you are purely building a string.

## Exporting stack outputs

Output values can be exported from a stack with `ctx.Export` so they are accessible to other stacks via stack references or via the Pulumi Cloud console. The second argument accepts any `pulumi.Input`, so you can export plain values, outputs, or expressions composed with `Sprintf` or `ApplyT`:

```go
ctx.Export("bucketName", bucket.Bucket)
ctx.Export("bucketArn", bucket.Arn)
ctx.Export("bucketUrl", pulumi.Sprintf("https://%s.s3.amazonaws.com", bucket.Bucket))
```

{{% notes type="info" %}}
`ctx.Export` must be called at the top level of your `pulumi.Run` function, not inside an `ApplyT` or `All` callback. Stack outputs created inside a callback are invisible to `pulumi preview` and will produce unexpected behavior.
{{% /notes %}}

## Common pitfalls

**Accessing an output value directly.** Outputs are not plain Go values. Attempting to read `bucket.Bucket` as a string will give you the struct representation of the output, not the bucket name. Always use `ApplyT` or one of the other transformation methods to work with the value.

**Missing the type assertion after ApplyT.** `ApplyT` returns `pulumi.Output`, not the concrete type. Every call to `ApplyT` must end with a type assertion—for example, `.(pulumi.StringOutput)`—or the value will not satisfy the typed input interface expected by resource arguments. Forgetting the assertion is the most common source of compile errors in Go Pulumi programs.

**Calling ToXxxOutput() unnecessarily.** If you are passing an output value directly to a resource argument, no conversion is needed—`pulumi.StringOutput` already implements `pulumi.StringInput`. The `ToStringOutput()` call is only necessary when you need to call `ApplyT` on a value typed as the input interface rather than a concrete output type.

**Type assertions within ApplyT.** When using `pulumi.All`, the `args []interface{}` slice must be type-asserted element by element. If the assertion does not match the actual type of the resolved value, the program will panic at runtime. Check the provider documentation to confirm the concrete Go types that a given resource property resolves to.

**Creating resources inside ApplyT.** As noted above, this breaks `pulumi preview` and should be avoided. If you need a resource that depends on another resource's output, pass the output as a direct input argument.

**Nil receivers.** `ApplyT` can be called on a nil output receiver and will return a zero output—it will not panic. This behavior is occasionally useful in component resources that conditionally populate outputs, but relying on it silently makes programs harder to reason about. Prefer explicitly initializing outputs to a known zero value where possible.

## Further reading

- [Inputs & outputs](/docs/iac/concepts/inputs-outputs/) — the language-neutral conceptual overview, with examples in all supported languages
- [Accessing single outputs with Apply](/docs/iac/concepts/inputs-outputs/apply/) — details on the `ApplyT` lifecycle and common usage patterns
- [Accessing multiple outputs with All](/docs/iac/concepts/inputs-outputs/all/) — the `All` function explained
- [Using output helpers](/docs/iac/concepts/inputs-outputs/helpers/) — `pulumi.Sprintf` and JSON helpers
- [Go SDK API reference](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi) — the complete package documentation

