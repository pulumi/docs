---
title: "Using Go Generics with Pulumi"
date: 2023-09-20
draft: false
meta_desc: "Try out a preview of using Go generics with Pulumi"
meta_image: meta.png
authors:
    - zaid-ajaj
    - justin-vanpatten
tags:
    - go
    - aws
---

Pulumi loves Go, it's what powers Pulumi. We've kept a close eye on the design and development of support for generics in the Go programming language over the years, a feature that allows developers to write type-safe, concise, and reusable code. We've been exploring what it'd look like to improve Pulumi's Go SDKs with generics and recently published a public [RFC](https://github.com/pulumi/pulumi/discussions/13057) detailing our plans. We've been making progress on the implementation and are excited to announce preview support for Go generics in our core and AWS Go SDKs. If you're using Go with Pulumi, we'd love for you to give it a try and share your feedback!

```go
// Given
var a pulumi.IntOutput
var b pulumi.StringOutput

// Before (could panic at runtime if you got something wrong)
o := pulumi.All(a, b).ApplyT(func(vs []interface{}) string { // could panic
    a := vs[0].(int) // could panic
    b := vs[1].(string) // could panic
    return strconv.Itoa(a) + b
}).(pulumi.StringOutput) // could panic

// After (compile-time type-safety)
o := pulumix.Apply2(a, b, func(a int, b string) string {
    return strconv.Itoa(a) + b
})
```

<!--more-->

## Why Generics?

Before looking at what's available in the preview, let's first review the motivations for adding support for generics, from the [RFC](https://github.com/pulumi/pulumi/discussions/13057).

### Unsafe Inputs, Outputs, and Apply

A common complaint about the Pulumi Go SDK is the lack of type safety. The `Input` and `Output` types, and the `apply` operation rely heavily on `interface{}`. This makes them effectively untyped at compile-time, instead relying on type matching at runtime.

For instance, the `apply` operation is implemented in Go as the following method:

```go
func (*OutputState) ApplyT(applier interface{}) Output
```

The contract for `ApplyT` states that `applier` must be a function with one of the following signatures:

```go
func(U) T
func(U) (T, error)
```

Where `U` must be assignable from the type contained in the underlying `Output`. If it isn't, the operation will panic.

The caller will usually want to cast the result into a specific output type. If they choose the wrong output type, this operation will panic.

So given a typical usage like the following, there are two spots that can panic: the `ApplyT` invocation and the `IntOutput` cast.

```go
intOutput := stringOutput.ApplyT(func(v string) int {
    return len(v)
}).(pulumi.IntOutput)
```

### Excessive code generation

The Go SDK relies heavily on code generation in an attempt to alleviate the pain of untyped operations. It generates type-specific input and output wrapper types for nearly every type it encounters.

In the core Pulumi SDK, this includes all primitive types, their pointers, containers, and containers of containers. For instance, the core SDK has 22 `String*` types besides type `String` itself, covering nearly all variations of the following pattern:

```
String(Ptr|(Array|Map)?(Array|Map))?(Input|Output)?
```

This pattern of code generation carries over to code generated for provider SDKs, though not to this degree of nesting. Every type gets an input and output type, a pointer variant if the type is referenced as a pointer, and container variants if the type is referenced from a container.

In general, this generates extremely large packages that are ungainly to navigate&mdash;both in source form and in their API reference.

## Introducing Go Generics in the Pulumi Go SDK

We can address the above by leveraging Go generics to incorporate type-safety into the core concepts (inputs, outputs, and apply) and reduce the amount of generated code.

Starting with v3.80 of the Pulumi Go SDK, we have added a new `pulumix` subpackage (containing "extensions"), which includes new generic `Input[T]` and `Output[T]` types as well as type-safe generics-based APIs to work with them such as `Apply`.

With the new support for generics, the previous untyped example can now be written in a type-safe manner as follows:

```go
intOutput := pulumix.Apply(stringOutput, func(v string) int {
    return len(v)
})
```

This is checked at compile-time: if you mistakenly specified an incorrect type, it will be caught at compile-time rather than panicking at runtime.

{{% notes type="info" %}}
We recommend using Go 1.21 or later, which has improved type inference for generics, allowing you to write the call to `Apply` above without having to explicitly specify generic type parameters.
{{% /notes %}}

## Adopting Generics in Your Pulumi Programs

Here's a larger example that uses the non-generic `pulumi.All` function and `ApplyT` method to produce a JSON string representing a policy for a `BucketPolicy`:

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/cloudfront"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
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
				func(args []any) (string, error) {
					bucketArn := args[0].(string)
					iamArn := args[1].(string)

					policy, err := json.Marshal(map[string]any{
						"Version": "2012-10-17",
						"Statement": []map[string]any{
							{
								"Sid":    "CloudfrontAllow",
								"Effect": "Allow",
								"Principal": map[string]any{
									"AWS": iamArn,
								},
								"Action":   "s3:GetObject",
								"Resource": bucketArn + "/*",
							},
						},
					})
					if err != nil {
						return "", err
					}
					return string(policy), nil
				}).(pulumi.StringOutput),
		}, pulumi.Parent(bucket))
		if err != nil {
			return err
		}

		return nil
	})
}
```

`pulumi.All` is used to combine `bucket.Arn` and `originAccessIdentity.IamArn` into a single `Output` and then uses `ApplyT` construct a policy in JSON using the values.

If we wanted to take advantage of the type-safety provided by the new `pulumix` subpackage, we could rewrite the above example to use `pulumix.Apply`. First, import `"github.com/pulumi/pulumi/sdk/v3/go/pulumix"`. Then, replace the use of `pulumi.All` and `ApplyT` with the generic `pulumix.Apply`:

```go
			Policy: pulumix.Apply2Err(bucket.Arn, originAccessIdentity.IamArn,
				func(bucketArn, iamArn string) (string, error) {
					policy, err := json.Marshal(map[string]any{
						"Version": "2012-10-17",
						"Statement": []map[string]any{
							{
								"Sid":    "CloudfrontAllow",
								"Effect": "Allow",
								"Principal": map[string]any{
									"AWS": iamArn,
								},
								"Action":   "s3:GetObject",
								"Resource": bucketArn + "/*",
							},
						},
					})
					if err != nil {
						return "", err
					}
					return string(policy), nil
				}),
```

Here, we're specifically using `pulumix.Apply2Err`, a variant of `pulumix.Apply` that accepts two generic arguments and a callback function that supports returning an error. There are other variants of `pulumix.Apply` that accept up to 8 generic arguments, and variants that return an error and accept a `context.Context`.

The result of our call to `pulumix.Apply2Err` in this example is `pulumix.Output[string]`. We can pass this directly to the `Policy` argument because it happens to be weakly typed as `pulumi.Input`, which `pulumix.Output[T]` implements.

If the `Policy` argument had been typed as `pulumi.StringInput`, for example, we would have had to cast the `pulumix.Output[string]` to `pulumi.StringOutput` using the `pulumix.Cast` function:

```go
policy := pulumix.Apply2Err(bucket.Arn, originAccessIdentity.IamArn,
    func(bucketArn, iamArn string) (string, error) {
        // ...
    })

// ...

Policy: pulumix.Cast[pulumi.StringOutput](policy),
```

Here's the updated example in full:

```go
package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/cloudfront"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
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

		_, err = s3.NewBucketPolicy(ctx, "bucket-policy", &s3.BucketPolicyArgs{
			Bucket: bucket.ID(),
			Policy: pulumix.Apply2Err(bucket.Arn, originAccessIdentity.IamArn,
				func(bucketArn, iamArn string) (string, error) {
					policy, err := json.Marshal(map[string]any{
						"Version": "2012-10-17",
						"Statement": []map[string]any{
							{
								"Sid":    "CloudfrontAllow",
								"Effect": "Allow",
								"Principal": map[string]any{
									"AWS": iamArn,
								},
								"Action":   "s3:GetObject",
								"Resource": bucketArn + "/*",
							},
						},
					})
					if err != nil {
						return "", err
					}
					return string(policy), nil
				}),
		}, pulumi.Parent(bucket))
		if err != nil {
			return err
		}

		return nil
	})
}
```

Notice how we are importing `pulumix` alongside `pulumi`. Being a subpackage means you can start using the generics-based types and functions alongside the current APIs as necessary without having to switch your code fully from using the old types to the new generic ones. Instead, you can migrate your code gradually to these new APIs where it makes sense. When needed, there are APIs to covert between generics-based APIs and the old ones using functions such as `pulumix.Cast` and `pulumix.ConvertTyped`.

## Generics-Based Cloud Provider SDKs

We've seen how the `pulumix` subpackage on its own can be used with existing Pulumi provider SDKs. We can go further and adopt generics in the provider SDKs themselves. To make the transition non-breaking and gradual for your Pulumi programs, we intend to publish generic-based variants of the provider Go SDKs under a subpackage called `x` (for "extensions"). This allows you to migrate your code resource by resource.

### Migrating an AWS Program to leverage Go generics

The following example is an AWS Pulumi program which we'll migrate into the generics-based API. Here is what `pulumi new aws-go` gives you today:

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an AWS resource (S3 Bucket)
		bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
			Website: &s3.BucketWebsiteArgs{
				IndexDocument: pulumi.String("index.html"),
			},
    	})
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("bucketName", bucket.ID())
		return nil
	})
}
```

To start using the generics-based version of the S3 module from AWS, you need to change the import from `"https://github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"` to `"https://github.com/pulumi/pulumi-aws/sdk/v6/go/aws/x/s3"` (notice the `x` after `aws/`), then change input values to use `pulumix.Ptr` instead of `pulumi.String`.

{{% notes type="info" %}}
Rather than passing values as `pulumi.String("foo")` and `pulumi.Int(42)`, with generics, you can simply use `pulumix.Val("foo")` and `pulumix.Val(42)`. Similarly, you can use the `pulumix.Ptr` function for pointer values.
{{% /notes %}}

```go
package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/x/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create an AWS resource (S3 Bucket)
		bucket, err := s3.NewBucket(ctx, "my-bucket", &s3.BucketArgs{
			Website: &s3.BucketWebsiteArgs{
				IndexDocument: pulumix.Ptr("index.html"),
			},
		})
		if err != nil {
			return err
		}

		// Export the name of the bucket
		ctx.Export("bucketName", bucket.ID())
		return nil
	})
}
```

You'll also need to update your `go.mod` to use the preview branch of the Pulumi AWS Go SDK that includes the `x` subpackage with generic APIs. Run the following:

```sh
go get github.com/pulumi/pulumi-aws/sdk/v6@generics
go mod tidy
```

The changes look minimal, except the fact that the inputs of `s3.BucketArgs` and the outputs of `Bucket` are now fully generics-based. Here is the `Bucket` type you get from `NewBucket`:

```go
type Bucket struct {
	pulumi.CustomResourceState
	AccelerationStatus pulumix.Output[string] `pulumi:"accelerationStatus"`
	Acl pulumix.Output[*string] `pulumi:"acl"`
	Arn pulumix.Output[string] `pulumi:"arn"`
	Bucket pulumix.Output[string] `pulumi:"bucket"`
	// ....
}
```

And here are its input arguments:

```go
type BucketArgs struct {
	AccelerationStatus pulumix.Input[*string]
	Acl pulumix.Input[*string]

	Arn pulumix.Input[*string]
	Bucket pulumix.Input[*string]
	// ...
}
```

## Authoring Generics-based Go SDKs

For Pulumi package authors, it is possible to start generating Go SDKs for your providers that include the generics-based variant under the `x` subpackage using v3.84.0 of Pulumi. By default, this is not enabled so you will have to explicitly opt-in to it using a specific option in the go language section of your Pulumi schema. The new option is called `"generics"` and it has three possible values:

- `"none"` is the default value when the option is not set. This doesn’t generate the generics-based variant
- `"side-by-side"` is the option we are using for our select providers which generates the variant under the x subdirectory.
- `"generics-only"` if you want your provider to only emit generics-based APIs. Since this is a preview feature, things might still be rough around the edges, so use this option with caution as fixes in the SDK-generation code might result in breaking changes in your APIs.

Here is how this looks in JSON:

```json
{
   "language": {
       "go": {
           "generics": "side-by-side"
        }
   }
}
```

We eventually intend to make `"side-by-side"` be the default, such that all providers get a generics-based variant under the `x` subpackage, so that all users can use the full generics API.

## Try it out!

We are excited for you to try out these new APIs and would love to hear your feedback! You can learn more details on the design and add comments to the [RFC](https://github.com/pulumi/pulumi/discussions/13057), or chat with us in the `#golang` channel on the [Pulumi Community Slack](https://slack.pulumi.com).

If you'd like to learn more about building cloud applications with Go and Pulumi, we have a workshop coming up in October. [Sign up here](https://www.pulumi.com/resources/build-web-scale-cloud-app-golang-iac/).

We'll also be at [GopherCon](https://info.pulumi.com/gophercon-2023), if you'd like to meet with us.
