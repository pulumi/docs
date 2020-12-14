---
title: "Announcing Cross-Language Enum Support"
date: 2020-12-14
draft: true
meta_desc: "Cross-language enum support provides a quality-of-life improvement to the development experience."
meta_image: meta.png
authors:
- komal-ali
tags:
- enums
- python
- go
- c#
- typescript
---

Here at Pulumi, we believe in leveraging the best features of programming languages to create a delightful development experience for our users. Today, we continue our contributions in this area by announcing cross-language support for `enum` types in our provider SDKs.

<!--more-->

## Enum types explained

An enum (short for enumerated) type is a data type consisting of a set of named values. In the Pulumi resource model, a property is an enum type when its value can only be set to a finite number of predetermined values.

For instance, consider a simple S3 bucket.

{{< chooser language "typescript,python,csharp,go" >}}

{{< choosable language typescript >}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { s3 } from "@pulumi/aws";

const myBucket = new s3.Bucket("myBucket", { acl: "private" });
```

{{< /choosable >}}
{{< choosable language python >}}

```python
import pulumi
from pulumi_aws import s3

my_bucket = s3.Bucket("myBucket", acl="private")
```

{{< /choosable >}}
{{< choosable language csharp >}}

```csharp
using Pulumi;
using S3 = Pulumi.Aws.S3;

class MyStack : Stack
{
    public MyStack()
    {
        var myBucket = new S3.Bucket("myBucket", new S3.BucketArgs
        {
            Acl = "private",
        });
    }
}
```

{{< /choosable >}}
{{< choosable language go >}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        myBucket, err := s3.NewBucket(ctx, "myBucket", &s3.BucketArgs{
            Acl: pulumi.String("private"),
        })
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{< /choosable >}}
{{< /chooser >}}

In the above code, the S3 `Bucket` resource has a property called `acl`, where we pass in the string `private` to indicate that this is a private bucket.

If we look at the [resource docs](https://www.pulumi.com/docs/reference/pkg/aws/s3/bucket/#acl_nodejs), we can see that the `acl` property can only be set to one of a few different values: `private`, `public-read`, `public-read-write`, `aws-exec-read`, `authenticated-read`, and `log-delivery-write`. The `acl` property is the perfect candidate for an enum type and is emitted as one, so you can use the following code instead.

{{< chooser >}}
{{< choosable language typescript >}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import { s3 } from "@pulumi/aws";

const myBucket = new s3.Bucket("myBucket", { acl: s3.CannedAcl.Private });
```

{{< /choosable >}}
{{< choosable language python >}}

```python
import pulumi
from pulumi_aws import s3

my_bucket = s3.Bucket("myBucket", acl=s3.CannedAcl.PRIVATE)
```

{{< /choosable >}}
{{< choosable language csharp >}}

```csharp
using Pulumi;
using S3 = Pulumi.Aws.S3;

class MyStack : Stack
{
    public MyStack()
    {
        var myBucket = new S3.Bucket("myBucket", new S3.BucketArgs
        {
            Acl = S3.CannedAcl.Private,
        });
    }
}
```

{{< /choosable >}}
{{< choosable language go >}}

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        myBucket, err := s3.NewBucket(ctx, "myBucket", &s3.BucketArgs{
            Acl: s3.CannedAclPrivate,
        })
        if err != nil {
            return err
        }
        return nil
    })
}
```

{{< /choosable >}}
{{< /chooser >}}

## IDE Superpowers

Enum properties provide discoverable and normalized constants that can be used in place of raw strings, allowing you to move faster with the added boosts of IDE tooling like type hints and autocomplete.

Using the provided constants, you can avoid referring back to the documentation to remember the valid values and save precious moments in the development cycle that would be lost to debugging errors caused by typos.

{{< chooser >}}
{{< choosable language typescript >}}

![ENUM_TYPESCRIPT](ts-enum.gif)

{{< /choosable >}}
{{< choosable language python >}}

![ENUM_PYTHON](python-enum.gif)

{{< /choosable >}}
{{< choosable language csharp >}}

![ENUM_CSHARP](csharp-enum.gif)

{{< /choosable >}}
{{< choosable language go >}}

![ENUM_GO](go-enum.gif)

{{< /choosable >}}
{{< /chooser >}}

## Optimized for flexibility

While some properties make sense as "strict" enums (i.e., the input value **must** be one of the enumerated values), there are times when it would be beneficial to have constants for commonly used values without restricting the input to **only** those values. We call this second category "relaxed" enums, and we model them a little differently in our schema.

### "Strict" enums

A property is a "strict" enum when the input value **must** be one of the enumerated values. In this case, the property type is specified as the enum type. Currently, only the Azure NextGen provider uses "strict" enums as the OpenAPI specification explicitly defines its properties as such.

```json5
{
  "resources": {
    "azure-nextgen:storage/latest:StorageAccount": {
      "inputProperties": {
        "accessTier": {
          "$ref": "#/types/azure-nextgen:storage/latest:AccessTier"
        },
      },
    },
  },
  "types": {
    "azure-nextgen:storage/latest:AccessTier": {
      "type": "string",
      "enum": [
        {
          "value": "Hot"
        },
        {
          "value": "Cool"
        }
      ],
    },
  },
}
```

### "Relaxed" enums

When a property is a "relaxed" enum, the property type is specified as the `Union` of the enum type and the underlying primitive type. This means that you have the convenience of using the enum constants (i.e., `s3.CannedAcl.Private`), but you may also pass in the raw string (i.e., `"private"`).

In the AWS provider (and other Terraform-based providers), we have opted for **only** using "relaxed" enums. The reasoning here is twofold. Allowing the primitive type maintains backward compatibility and also allows users to use values that may not yet be represented in the Pulumi schema (e.g., a new Managed Policy ARN, EC2 Instance type, etc.).

```json5
{
  "resources": {
    "aws:s3/bucket:Bucket": {
      "inputProperties": {
        "acl": {
          "oneOf": [
            {
              "type": "string"
            },
            {
              "$ref": "#/types/aws:s3/CannedAcl:CannedAcl"
            },
          ]
        },
      },
    },
  },
  "types": {
    "aws:s3/CannedAcl:CannedAcl": {
      "type": "string",
      "enum": [
        {
          "name": "Private",
          "value": "private"
        },
        ...
      ],
    },
  },
}
```

## Try them out!

You can find enum types integrated into v3.19.0 of the AWS provider and v0.3.0 of the Azure NextGen provider.

**Azure NextGen**: In the Azure NextGen provider, all properties labeled as enums in the OpenAPI spec are represented as such. In all, there are over 1300 enums provided in the SDKs.

**AWS**: The AWS provider enums are manually identified and maintained as part of the [provider schema](https://github.com/pulumi/pulumi-aws/blob/master/provider/resources.go#L2392-L3375). We've already added many that you might find useful, such as Lambda Runtimes, EC2 Instance Types, and IAM Managed Policies, and will continue to add more across our provider SDKs in the coming months.

Take the new providers for a spin and let us know what you think in the [Community Slack](https://slack.pulumi.com/)! If there are properties that you would like to see represented as enums, let us know. Or even better, submit a PR to add them to the schema!
