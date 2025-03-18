---
title_tag: Validate a Custom Policy Pack | Pulumi Crossguard
title: Validate a Custom Policy Pack
layout: topic
description: Validate a custom policy pack using Pulumi Crossguard.
meta_desc: Validate a custom policy pack using Pulumi Crossguard.
weight: 2
estimated_time: 5
---

## Test the Policy Pack

In the previous step we created a custom policy pack. Now, let's see it in action. We'll create some AWS resources that violate the policies, run our custom policy pack to check compliance, and then fix the resources to adhere to the policies.

### Step 1: Create Non-Compliant Resources

First, create a new Pulumi project from a template:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```sh
$ mkdir custom-policy-pack-integration-test-typescript && cd custom-policy-pack-integration-test-typescript
$ pulumi new aws-typescript
```

Follow the prompts as usual to set up your project.

Below are examples of non-compliant resources defined in Pulumi. Replace the contents of `index.ts` with this code.

```typescript
{{< example-program-snippet path="custom-policy-pack-integration-test" file="index.non-compliant.ts" language="typescript" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```sh
$ mkdir custom-policy-pack-integration-test-python && cd custom-policy-pack-integration-test-python
$ pulumi new aws-python
```

Follow the prompts as usual to set up your project.

Below are examples of non-compliant resources defined in Pulumi. Replace the contents of `__main__.py` with this code.

```python
{{< example-program-snippet path="custom-policy-pack-integration-test" file="non_compliant.py" language="python" >}}
```

{{% /choosable %}}

This Pulumi project defines an S3 Bucket, a Security Group, and an EC2 instance. As written, these violate our custom policies in the following ways:

- The Bucket has a `tag` property, but it's empty.
- The Bucket has a non-compliant prefix.
- The Security Group has no `tags` property.
- The EC2 instance uses a non-compliant instance type.

So, if we run `pulumi preview` on these with our custom policy pack applied, we should see four policy violations. Let's try it!

### Step 2: Run the Policy Pack

From the root of the Pulumi project, run `pulumi preview` with the `--policy-pack` option, pointing to the directory containing our custom policies. Pulumi will evaluate the policy pack against these resources and report any violations.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```sh
$ pulumi preview --policy-pack ../custom-policy-pack-typescript

Loading policy packs...

     Type                      Name                                                Plan
 +   pulumi:pulumi:Stack       custom-policy-pack-integration-test-typescript-dev  create
 +   ├─ aws:s3:BucketV2        my-bucket                                           create
 +   ├─ aws:ec2:Instance       web-server                                          create
 +   └─ aws:ec2:SecurityGroup  ssh-security-group                                  create

Policies:
    ❌ custom-policy-pack@v0.0.1 (local: ../custom-policy-pack-typescript)
        - [mandatory]  all-aws-resources-must-have-tags  (aws:ec2/securityGroup:SecurityGroup: ssh-security-group)
          Ensures all AWS resources have at least one tag.
          All AWS resources must have at least one tag.
        - [mandatory]  all-aws-resources-must-have-tags  (aws:s3/bucketV2:BucketV2: my-bucket)
          Ensures all AWS resources have at least one tag.
          All AWS resources must have at least one tag.
        - [mandatory]  ec2-instance-type-restricted  (aws:ec2/instance:Instance: web-server)
          Ensures EC2 instances use approved instance type.
          Invalid instance type: 't3.micro'. EC2 instances must use 't2.micro' instance type.
        - [mandatory]  s3-product-prefix  (aws:s3/bucketV2:BucketV2: my-bucket)
          Ensures S3 buckets have the correct product prefix.
          Invalid prefix: 'something-unexpected-'. S3 buckets must use 'myproduct-' prefix.
```

{{% /choosable %}}

{{% choosable language python %}}

```sh
$ pulumi preview --policy-pack ../custom-policy-pack-python

Loading policy packs...

     Type                      Name                                            Plan
 +   pulumi:pulumi:Stack       custom-policy-pack-integration-test-python-dev  create
 +   ├─ aws:s3:BucketV2        my-bucket                                       create
 +   ├─ aws:ec2:Instance       web-server                                      create
 +   └─ aws:ec2:SecurityGroup  ssh-security-group                              create

Policies:
    ❌ custom-policy-pack@v0.0.1 (local: ../custom-policy-pack-python)
        - [mandatory]  all-aws-resources-must-have-tags  (aws:ec2/securityGroup:SecurityGroup: ssh-security-group)
          Ensures all AWS resources have at least one tag.
          All AWS resources must have at least one tag.
        - [mandatory]  all-aws-resources-must-have-tags  (aws:s3/bucketV2:BucketV2: my-bucket)
          Ensures all AWS resources have at least one tag.
          All AWS resources must have at least one tag.
        - [mandatory]  ec2-instance-type-restricted  (aws:ec2/instance:Instance: web-server)
          Ensures EC2 instances use approved instance type.
          Invalid instance type: 't3.micro'. EC2 instances must use 't2.micro' instance type.
        - [mandatory]  s3-product-prefix  (aws:s3/bucketV2:BucketV2: my-bucket)
          Ensures S3 buckets have the correct product prefix.
          Invalid prefix: 'something-unexpected-'. S3 buckets must use 'myproduct-' prefix.
```

{{% /choosable %}}

### Step 3: Fix the Resources

Ok, now that we see the expected violations, let's update the resources to comply with the policies.

We need to:

- Update the Bucket to use the correct prefix: `myproduct-`
- Update the Bucket to have at least one tag
- Update the Security Group to have at least one tag
- Update the EC2 instance to use the correct instance type: `t2.micro`

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

Replace the contents of `index.ts` with this code.

```python
{{< example-program-snippet path="custom-policy-pack-integration-test" file="index.ts" language="typescript" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

Replace the contents of `__main__.py` with this code.

```python
{{< example-program-snippet path="custom-policy-pack-integration-test" file="__main__.py" language="python" >}}
```

{{% /choosable %}}

### Step 4: Verify Compliance

Run `pulumi preview` again. This time, no policy violations should be reported.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```sh
$ pulumi preview --policy-pack ../custom-policy-pack-typescript

Loading policy packs...

     Type                      Name                                                Plan
 +   pulumi:pulumi:Stack       custom-policy-pack-integration-test-typescript-dev  create
 +   ├─ aws:s3:BucketV2        my-bucket                                           create
 +   ├─ aws:ec2:Instance       web-server                                          create
 +   └─ aws:ec2:SecurityGroup  ssh-security-group                                  create

Policies:
    ✅ custom-policy-pack@v0.0.1 (local: ../custom-policy-pack-typescript)
```

{{% /choosable %}}

{{% choosable language python %}}

```sh
$ pulumi preview --policy-pack ../custom-policy-pack-python

Loading policy packs...

     Type                      Name                                            Plan
 +   pulumi:pulumi:Stack       custom-policy-pack-integration-test-python-dev  create
 +   ├─ aws:s3:BucketV2        my-bucket                                       create
 +   ├─ aws:ec2:Instance       web-server                                      create
 +   └─ aws:ec2:SecurityGroup  ssh-security-group                              create

Policies:
    ✅ custom-policy-pack@v0.0.1 (local: ../custom-policy-pack-python)
```

{{% /choosable %}}

Congratulations! You've successfully created and tested a policy pack with Pulumi CrossGuard.

## Next Steps

To learn more about using Pulumi CrossGuard and policies, explore the following:

- [Pulumi Crossguard: Policy as Code Documentation](https://www.pulumi.com/docs/guides/crossguard/)
- [Advanced Policy Examples](https://github.com/pulumi/examples/tree/master/policy-packs)

If you are using *Pulumi Business Critical* edition, you can also publish this policy to your Pulumi Cloud organization, which enables server-side policy enforcement on all Pulumi projects in your organization. See [pricing](/pricing/) for more details.

{{< tutorials/stepper >}}
