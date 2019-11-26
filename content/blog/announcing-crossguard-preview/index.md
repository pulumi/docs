---
title: "Announcing Crossguard Preview"
date: 2019-12-02
draft: true
meta_desc: "Today we are announcing Pulumi CrossGuard, a Policy as Code solution, is available all Team Pro and Enterprise customers to preview."
meta_image: meta.png
authors: ["erin-krengel"]
tags: ["crossguard", "policy-as-code", "New-Features", "Pulumi-News", "Features"]
---

Over the past few months, we have been hard at work on Pulumi CrossGuard, a Policy as Code solution. Using the `pulumi-policy` library, you can express flexible business and security rules using code. CrossGuard enables organization administrators to enforce these policies across their organization or just on specific stacks. CrossGuard allows you to verify or enforce custom policies on changes before they are applied to your resources.

<!--more-->

You can run policies against any Pulumi stack, independent of the stack's language. This means you can have policies written in TypeScript and run them against a Python-based stack. Policies are grouped in *Policy Packs* and run against a stack during both `pulumi preview` and `pulumi up`. Each resource in a stack is run through the Policy Pack prior to creation, meaning you can block the creation of out-of-compliance resources.

## Why

Using Pulumi, developers and operators are empowered to self-provision their infrastructure and move quickly. One of our core goals is to allow you to codify best practices and share them with your team. We often hear from organization leaders that they are concerned about enforcing security and compliance best-practices. CrossGuard provides a way to automatically enforce compliance, allowing teams to operate self-sufficiently while still ensuring organization-wide requirements are met.

## Key Features

The key features available during the CrossGuard preview are:

* TypeScript [pulumi-policy SDK](https://github.com/pulumi/pulumi-policy) to express custom policies
* [Run Policy Packs locally](https://www.pulumi.com/docs/get-started/policy-as-code/authoring-a-policy-pack/#testing-the-policy-pack-locally) using the `--policy-pack` flag
* [AWSGuard library](https://github.com/pulumi/pulumi-awsguard) - codifies best practices for AWS
* [Enforce Policy Packs](https://www.pulumi.com/docs/get-started/policy-as-code/enforcing-a-policy-pack/) across your organization or particular stacks in the Pulumi Console
* View policy errors and Policy Packs for an update in the Pulumi Console

## Pulumi CrossGuard for Everyone

Pulumi CrossGuard has something to offer everyone in your organization.

### For Organization Administrators

You want your organization to be able to move quickly and deliver business value. To do so, your team needs to be able to self-service their infrastructure. Pulumi CrossGuard gives you the peace of mind that you need to allow your team to work independently. Codify business and security policies to ensure your team meets the requirements you set forth.

### For Security Engineers

There's a lot of complexity to security and often the rest of your organization does not have all the knowledge they need to deliver software securely. Express security policies that allow you to share your knowledge and prevent issues from ending up in production.

### For Developers and Operators

There are a ton of moving pieces in our ecosystems today. It is difficult to know everything about the cloud resources we use. Pulumi CrossGuard ensures you do not fall into the trap of insecure or unreasonable defaults.

## CrossGuard in Action

With an understanding of what CrossGuard enables, let's look at what that means in practice. The following is a policy pack definition that prohibits creating an AWS S3 bucket that is public readable. Our Policy Pack is not complicated. It uses a `validateTypedResource` helper function to filter for the resource type we care about and reports a violation if present.

```typescript
new PolicyPack("aws-typescript", {
    policies: [{
        name: "s3-no-public-read",
        description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
        enforcementLevel: "mandatory",
        validateResource: validateTypedResource(aws.s3.Bucket, (bucket, args, reportViolation) => {
            if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                reportViolation(
                    "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html");
            }
        }),
    }],
});
```

We initially run `pulumi preview` for an S3 bucket that will pass the policy.

```typescript
// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");
```

We then modify the bucket to have its access control list (ACL) set to `public-read`, which will cause our bucket to be out-of-compliance.

```typescript
// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket", {
    acl: "public-read",
});
```

![Demo of Policy as Code](pac-demo.gif)

While this is a simple demonstration of what you can do with Policy as Code, the framework is very flexible and supports much more complex policies. Our [AWSGuard library](https://github.com/pulumi/pulumi-awsguard) is a great example of how you can use Policy as Code to write configurable policies.

## Try it Today

Pulumi CrossGuard empowers everyone to build better, safer applications and infrastructure. Today, Pulumi CrossGuard is available to preview for all Team Pro and Enterprise organizations. Organization administrators can opt-in to the preview via the "Policies" tab in the Pulumi Console. To get started with CrossGuard today, here are some resources:

* If haven't played around with Pulumi yet, here is [Pulumi's Getting Started tutorial](https://www.pulumi.com/docs/get-started/).
* [Policy as Code Getting Started tutorial](https://www.pulumi.com/docs/get-started/policy-as-code/)

We've initially released Policy as Code with TypeScript and plan to add `pulumi-policy` SDKs for the other languages we support. We would love to hear any feedback you have! You can submit feedback via our [Contact Us form](https://www.pulumi.com/contact/) or in our [community slack](https://slack.pulumi.com/).
