---
title_tag: Getting Started with Encapsulation | Learn Pulumi
title: "Understanding Encapsulation"
layout: topic
date: 2021-11-17
draft: false
description: |
    Explore encapsulation of cloud resources with Pulumi.
meta_desc: Learn what encapsulation is in the context of infrastructure as code, why it is crucial for maintaining good IaC, and what encapsulation looks like in practice.
index: 0
estimated_time: 10
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - learn
---

Encapsulation is one part of what makes a programming language so powerful. Without encapsulation, programs would still be sets of commands. Encapsulation is generally considered as part of an object-oriented paradigm, but it's present in other software development paradigms like functional programming (e.g., lexical closures). But what does this have to do with infrastructure? Well, by using encapsulation we break logic down into reusable components. In doing so, we ensure better maintainability, readability, and reusability&mdash;all critical to good infrastructure as code both in theory and in practice.

Breaking apart Pulumi code is essential to keeping a clean, well-organized, and easily maintained code base that enables teams to collaborate to enhance current systems. Over the course of these pathways, we've been pretending we're part of a fictional organization called Pulumipus (after Pulumi's beloved mascot), so let's imagine that we've now scaled beyond the basic boba shop from the Fundamentals series to an entire brand with many, many smaller organizations. As the owners of the infrastructure for the Pulumipus brand, we've got a lot of resources to maintain, and it's much better to reuse code that we write once rather than repeating ourselves continuously in our program and throughout all of the programs we maintain. To illustrate that, let's explore a practical example.

## Breaking apart Pulumi code

Let's take a fairly uncomplicated piece of Pulumi code: the definition of an s3 bucket:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("my-bucket");

export const bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws_native as aws_native

bucket = aws_native.s3.Bucket("my-bucket")

pulumi.export("bucket", bucket.bucket_name)
```

{{% /choosable %}}

Here, we're creating one resource and exporting the output from that resource. In practice however, production systems typically have more requirements than a storage object. We need access policies, for one. Depending on how you're using that storage, you might need networking and other resources, as well. All of these use cases for a storage object requires some kind of policy, though, so when thinking about encapsulating our storage object needs, we probably want to put those two together. Let's adjust our code accordingly:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("my-bucket");
const bucketPolicy = new aws.s3.BucketPolicy("my-bucket-policy", {
    bucket: bucket.id,
    policy: {
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Principal: "*",
            Action: [
                "s3:GetObject"
            ],
            Resource: [
                pulumi.interpolate`${bucket.arn}/*`,
            ],
        }],
    },
});

export const bucketName = bucket.id;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
import pulumi
import pulumi_aws as aws_classic
import pulumi_aws_native as aws_native

bucket = aws_native.s3.Bucket(
    "my-bucket",
    public_access_block_configuration=aws_native.s3.BucketPublicAccessBlockConfigurationArgs(
        block_public_policy=False
    ),
)
bucket_policy = aws_classic.s3.BucketPolicy(
    "my-bucket-policy",
    bucket=bucket.id,
    policy=bucket.arn.apply(
        lambda arn: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": "*",
                        "Action": ["s3:GetObject"],
                        "Resource": [f"{arn}/*"],
                    }
                ],
            }
        )
    ),
    opts=pulumi.ResourceOptions(parent=bucket),
)

pulumi.export("bucket", bucket.bucket_name)
```

{{% /choosable %}}

Now, that's nice, but what if we need to make three different storage objects for three different use cases? Sure, we could copy and paste the code over and over, but that's not good practice. It introduces the possibility for errors, makes the whole codebase harder to maintain (what if there's an update to the policy versions that has to go out for security reasons?!?), and in general creates more headaches than it solves. Instead, let's encapsulate the code into something more reusable. We could start out by creating a resource grouping for the kind of resource we wanted to use:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
// ...

class OurBucketClass {
    private bucket: aws.s3.Bucket;
    private bucketPolicy: aws.s3.BucketPolicy;

    constructor(name: string, policyName: string) {
        this.bucket = new aws.s3.Bucket(name);
        this.bucketPolicy = new aws.s3.BucketPolicy(policyName, {
            bucket: this.bucket.id,
            policy: {
                Version: "2012-10-17",
                Statement: [{
                    Effect: "Allow",
                    Principal: "*",
                    Action: [
                        "s3:GetObject"
                    ],
                    Resource: [
                        pulumi.interpolate`${this.bucket.arn}/*`,
                    ],
                }],
            },
        }, { parent: this.bucket });
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
# ...

class OurBucketClass:
    def __init__(self, name: str, policy_name: str):
        self._bucket = aws_native.s3.Bucket(
            name,
            public_access_block_configuration=aws_native.s3.BucketPublicAccessBlockConfigurationArgs(
                block_public_policy=False
            ),
        )
        self._bucket_policy = aws_classic.s3.BucketPolicy(
            policy_name,
            bucket=self._bucket.id,
            policy=self._bucket.arn.apply(
                lambda arn: json.dumps(
                    {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Principal": "*",
                                "Action": ["s3:GetObject"],
                                "Resource": [f"{arn}/*"],
                            }
                        ],
                    }
                )
            ),
            opts=pulumi.ResourceOptions(parent=self._bucket),
        )
```

{{% /choosable %}}

But that JSON blob of the policy is also an object which we can encapsulate, making our storage object class more usable outside of this specific context. Let's imagine we have a referenceable list of common access policies, perhaps a simple key:value store. In the store, keys are strings that are names of policies, and the values are JSON documents stored in separate files so you can reuse them.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
// ...

type PolicyType = "default" | "locked" | "permissive";

class OurBucketClass {
    private bucket: aws.s3.Bucket;
    private bucketPolicy: aws.s3.BucketPolicy;

    private policies: { [K in PolicyType]: aws.iam.PolicyStatement } = {
        default: {
            Effect: "Allow",
            Principal: "*",
            Action: [
                "s3:GetObject"
            ],
        },
        locked: {
            /* ... */
        },
        permissive: {
            /* ... */
        },
    };

    private getBucketPolicy(policyType: PolicyType): aws.iam.PolicyDocument {
        return {
            Version: "2012-10-17",
            Statement: [{
                ...this.policies[policyType],
                Resource: [
                    pulumi.interpolate`${this.bucket.arn}/*`,
                ],
            }],
        }
    };

    constructor(name: string, policy: PolicyType) {
        this.bucket = new aws.s3.Bucket(name);
        this.bucketPolicy = new aws.s3.BucketPolicy(`${name}-policy`, {
            bucket: this.bucket.id,
            policy: this.getBucketPolicy(policy),
        }, { parent: this.bucket });
    }
}

const bucket = new OurBucketClass("laura-bucket-1", "default");
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import json
# ...

class OurBucketClass:
    _POLICIES = {
        "default": {
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
        },
        "locked": {
            # ...
        },
        "permissive": {
            # ...
        },
    }

    def __init__(self, name: str, policy_type: str):
        self._bucket = aws_native.s3.Bucket(
            name,
            public_access_block_configuration=aws_native.s3.BucketPublicAccessBlockConfigurationArgs(
                block_public_policy=False
            ),
        )
        self._bucket_policy = aws_classic.s3.BucketPolicy(
            f"{name}-policy",
            bucket=self._bucket.id,
            policy=self._get_bucket_policy(policy_type),
            opts=pulumi.ResourceOptions(parent=self._bucket),
        )

    def _get_bucket_policy(self, policy_type: str) -> pulumi.Output:
        try:
            statement = self._POLICIES[policy_type]
        except KeyError as e:
            add_note = "Policy type needs to be 'default', 'locked', or 'permissive'"
            raise ValueError(f"{add_note}. You used {policy_type}.") from e

        return self._bucket.arn.apply(
            lambda arn: json.dumps(
                {
                    "Version": "2012-10-17",
                    "Statement": [
                        {**statement, "Resource": [f"{arn}/*"]},
                    ],
                }
            )
        )


bucket = OurBucketClass("my-bucket", "default")
```

{{% /choosable %}}

This way of breaking out the code is only the beginning, though. It still is stuck in the weeds of being specifically following the resource model of an S3 bucket on AWS, and an end user building on top of your code probably doesn't care about these low-level constructs. In Pulumi, everything, including your resources, can be modeled, abstracted, and encapsulated just like anything in your programming language of choice. Why does that matter, or why should you care? The answer to that question is up next!
