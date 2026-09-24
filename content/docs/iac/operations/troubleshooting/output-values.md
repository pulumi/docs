---
title_tag: "Troubleshooting Pulumi Output Value Errors"
meta_desc: "Diagnose errors from treating a Pulumi Output as a plain value: string conversion, JSON serialization, program branching, and reading outputs."
title: Output value errors
h1: Output value errors
menu:
    iac:
        name: Output Value Errors
        parent: iac-operations-troubleshooting
        weight: 70
aliases:
    - /docs/support/troubleshooting/common-issues/output-values/
---

Pulumi resource properties are represented as [Outputs](/docs/iac/concepts/inputs-outputs/#outputs) rather than plain values, because their real values are not known until the resource providing them has actually been created or updated. This is central to how Pulumi builds a dependency graph and runs `pulumi preview`, but it also means a whole family of ordinary-looking code fails in ways that are not obvious from the error message alone: pulling a value out of an Output too early, branching on it directly, or trying to read it the way you would read a variable in a normal script.

This page collects the errors and symptoms this pattern produces, matched to their cause and fix. If you have not already read [Accessing single outputs with Apply](/docs/iac/concepts/inputs-outputs/apply/) and [Working with multiple outputs](/docs/iac/concepts/inputs-outputs/all/), start there for the underlying model; this page assumes that background and focuses on diagnosis.

## Calling toString on an output is not supported

If you concatenate, log, or otherwise convert an output value to a string directly instead of going through `apply` or an equivalent helper, Pulumi does not raise an error by default. Instead it silently substitutes a placeholder message in place of the value:

{{< chooser language "typescript,python,go,csharp" >}}

{{% choosable language typescript %}}

```typescript
// Silently produces a broken string; no exception is thrown.
console.log(`The bucket name is ${bucket.bucketName}`);
```

The resulting string contains literal text such as `Calling [toString] on an [Output<T>] is not supported`, followed by guidance to use `apply` or `pulumi.interpolate` instead. The same placeholder mechanism backs JSON serialization: calling `JSON.stringify()` on an output, or letting one flow into a JSON body, produces a `Calling [toJSON] on an [Output<T>] is not supported` string rather than the value.

{{% /choosable %}}

{{% choosable language python %}}

```python
# Silently produces a broken string; no exception is raised.
print(f"The bucket name is {bucket.bucket}")
```

The resulting string contains literal text such as `Calling __str__ on an Output[T] is not supported`, and Pulumi also logs a warning. Passing an output to `json.dumps()` fails outright with `TypeError: Object of type Output is not JSON serializable`, because `Output` has no `__str__`-based fallback that `json.dumps` can use.

{{% /choosable %}}

{{% choosable language go %}}

Go's static typing generally prevents this: passing a `pulumi.StringOutput` where a `string` is expected is a compile error, not a runtime surprise. If you go around the type system with `fmt.Sprintf("%v", output)`, you get the output's internal struct representation printed instead of its value, rather than a helpful message.

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
// Silently produces a broken string; no exception is thrown.
Console.WriteLine($"The bucket name is {bucket.BucketName}");
```

The resulting string contains literal text such as `Calling [ToString] on an [Output<T>] is not supported`, followed by guidance to use `Apply` or `Output.Format` instead.

{{% /choosable %}}

{{< /chooser >}}

Because this fails by producing a string rather than throwing, the mistake is easy to miss during development: the program runs, `pulumi up` succeeds, and the placeholder text only surfaces later, embedded in a log line, a generated config file, or a downstream resource property. To catch it immediately instead, set the environment variable `PULUMI_ERROR_OUTPUT_STRING=true` (TypeScript, Python, and C#) while developing; with it set, the same code throws an exception at the point of the mistake instead of returning the placeholder text.

The fix is the same across languages: keep the output inside an `apply`/`Apply` callback (or Python's equivalent), or use the string-composition helpers built for this purpose — `pulumi.interpolate` and `Output.concat`/`Output.format` in TypeScript, `Output.concat`/`Output.format`/`Output.json_dumps` in Python, `pulumi.Sprintf`/`pulumi.JSONMarshal` in Go, and `Output.Format` in C#. See [Printing output values](/docs/iac/concepts/inputs-outputs/apply/#printing-output-values) for worked examples of each.

## A value that "worked" outside `apply` stops working further down the program

A subtler version of the same mistake: the value read out of an output inside an `apply`/`Apply` callback is only available inside that callback (or in another output derived from it). Assigning it to an outer variable and using that variable later, outside the callback, does not do what it looks like it does:

```typescript
let bucketName: string | undefined;
bucket.bucketName.apply((name) => {
    bucketName = name; // Runs asynchronously, later.
});

// bucketName is still undefined here — the apply callback above has not run yet.
new aws.s3.BucketObject("readme", {
    bucket: bucketName, // undefined, or a stale value from a previous run.
    key: "README.md",
});
```

The `apply` callback runs asynchronously once the output resolves, which in general is after the rest of your program's top-level code has already finished running. Reading the outer variable before that happens gets you `undefined` (or, in a language without a compiler catching the type mismatch, a stale value left over from a previous invocation). This is not a timing bug you can fix by adding a delay: the callback runs when the engine resolves the dependency graph, not on your program's clock.

The fix is to never let the plain value leave the callback chain. Either do the downstream work inside the same `apply`, chain a further `apply` on the result, or — usually the better option — pass the output itself as the input to whatever needs it, and let Pulumi resolve the dependency:

```typescript
new aws.s3.BucketObject("readme", {
    bucket: bucket.bucketName, // Pass the Output directly; no apply needed here at all.
    key: "README.md",
});
```

Before reaching for `apply` at all, check whether the resource you are configuring can accept the output directly as one of its inputs, since Pulumi resources are built to accept outputs everywhere a plain value would otherwise go.

## Branching program logic on an output produces the wrong branch, or an error at synthesis time

Code like `if (someOutput) { ... } else { ... }`, or a loop bound, or a Python `for _ in range(some_output)`, does not do what it looks like. In a dynamically typed language the output object itself is what gets evaluated, not its eventual value, so an `if` on an output is generally always true (an object is a true value in a boolean context) regardless of what the output resolves to. In a statically typed language this is usually a compile error instead, because an `Output<bool>` is not a `bool`.

This only applies to values that come from resources — outputs, in other words. A value that is already known when your program starts, such as a stack configuration setting read with `pulumi.Config`, an environment variable, or a hardcoded flag, is a plain value and branches on it exactly the way you would expect; there is nothing to fix there.

When the branch genuinely depends on a resource's output, the branch itself has to move inside `apply`, which means both possible outcomes need to be expressed as values rather than as program structure:

```typescript
// Does not work: the branch is evaluated on the Output object, not its value.
if (vpc.vpcId) {
    // ...
}

// Works: derive a new Output whose value depends on the branch.
const subnetCount = vpc.vpcId.apply((id) => (id.startsWith("vpc-0") ? 3 : 6));
```

Because the two branches can no longer be expressed as separate blocks of resource-creation code (only as separate values), a runtime branch on an output usually means restructuring the program so both possible sets of resources are described unconditionally, and the output only decides between values passed into them, or so the branch is on a plain config value instead of a resource output.

## Using an output as a resource name, a map key, or a loop bound

A resource's logical name (the first argument to its constructor) and the loop bounds or map keys you use while authoring a program all need to be known plain values while your program is still being evaluated, before any resource actually exists. An output is a promise of a future value, so passing one in any of these positions either fails to compile, or fails at runtime once the mismatch is discovered.

If you need resource names or counts to depend on data that is only known once a resource has been created, the two usual fixes are: derive that data from configuration or another data source that is already available as a plain value at program-authoring time, or, if it genuinely cannot be known until an earlier resource has been provisioned, restructure the dependent resources so they are provisioned in a later, separate stack that consumes the first stack's outputs through a [`StackReference`](/docs/iac/concepts/stacks/#stackreferences).

## Trying to read an output's value synchronously

Reaching for `await` on an output outside of an `async` `apply` callback, or a `.get()`/`.Result` method, generally does not compile or fails at runtime — Pulumi does not expose a way to block your program and pull a resolved value out of an output synchronously, in any of the supported languages. This is deliberate: doing so would defeat the whole point of building a dependency graph up front, since the engine would need the value before it has finished figuring out in what order to create anything.

If what you actually want is to read a value that a Pulumi program has already produced, from outside that program, the output is not the right place to reach for it. Use one of:

- `pulumi stack output <name>` from the CLI, to read a single stack output after a deployment.
- A [`StackReference`](/docs/iac/concepts/stacks/#stackreferences) from another Pulumi program, to consume one stack's outputs as another stack's inputs.
- The [Automation API](/docs/iac/automation-api/)'s `summary.outputs` (or the equivalent in your language's Automation API package), when driving deployments programmatically.

All three read a value that has already resolved, rather than trying to unwrap an in-flight output from inside the same program that created it.
