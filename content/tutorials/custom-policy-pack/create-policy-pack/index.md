---
title_tag: Create a Custom Policy Pack | Pulumi Crossguard
title: Create a Custom Policy Pack
layout: topic
description: Create a custom policy pack using Pulumi Crossguard.
meta_desc: Create a custom policy pack using Pulumi Crossguard.
weight: 1
estimated_time: 5
---

In this step, we'll create a policy pack to enforce the following rules for AWS resources:

1. S3 buckets must be prefixed with the product name `myproduct-`.
2. EC2 instances must use the `t2.micro` instance type.
3. All AWS resources must have at least one tag defined.

### Set up your policy pack project

First, create a new directory for your policy pack project:

```bash
mkdir custom-policy-pack
cd custom-policy-pack
```

Then, initialize your project. Choose Python or TypeScript based on your preferred language.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```bash
pulumi policy new aws-typescript
```

This will create the following files and directories:

- `PulumiPolicy.yaml`: A [Pulumi project file](https://www.pulumi.com/docs/iac/concepts/projects/) that indicates this a policy pack.
- `index.ts`: The TypeScript entry point where the policies will be defined in code.
- `node_modules/`: The [NPM modules directory](https://docs.npmjs.com/cli/v9/configuring-npm/folders#node-modules)
- `package-lock.json`: A list of the module dependencies used by [`npm`](https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json).
- `package.json`: The [`npm` package description file](https://docs.npmjs.com/cli/v11/configuring-npm/package-json).
- `tsconfig.json`: The [TypeScript configuration file](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html).

{{% notes type="info" %}}
In this example, we are using the [`aws-typescript`](https://github.com/pulumi/templates-policy/tree/master/aws-typescript) policy pack template. To see the full list of available policy pack templates, check out the [`pulumi/templates-policy`](https://github.com/pulumi/templates-policy) GitHub repository.
{{% /notes %}}

{{% /choosable %}}

{{% choosable language python %}}

```bash
pulumi policy new aws-python
```

This will create the following files and directories:

- `PulumiPolicy.yaml`: A [Pulumi project file](https://www.pulumi.com/docs/iac/concepts/projects/) that indicates this a policy pack.
- `__main__.py`: The Python entry point where the policies will be defined in code.
- `requirements.txt`: A list of the module dependencies used by [`pip`](https://pip.pypa.io/en/stable/reference/requirements-file-format/).
- `venv/`: The Python [virtual environment](https://docs.python.org/3/library/venv.html).

{{% notes type="info" %}}
In this example, we are using the [`aws-python`](https://github.com/pulumi/templates-policy/tree/master/aws-python) policy pack template. To see the full list of available policy pack templates, check out the [`pulumi/templates-policy`](https://github.com/pulumi/templates-policy) GitHub repository.
{{% /notes %}}

{{% /choosable %}}

This will initialize your project, creating the necessary files for Pulumi to use as a policy, including module dependencies to the providers that will let us interact with AWS resources.

### Define Policies

Policies are written in Python or TypeScript. Like Pulumi Programs, you can use the full power of your preferred language, including standard features like leveraging third-party modules, using conditional logic and control flow, and can be validated with unit testing frameworks.

By default the template sets up an example *resource policy* that prevents S3 buckets from being publically readable:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

**File: `custom-policy-pack/index.ts`**

```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("aws-typescript", {
    policies: [{
        name: "s3-no-public-read",
        description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
            if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                reportViolation(
                    "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html");
            }
        }),
    }],
});
```

{{% /choosable %}}

{{% choosable language python %}}

**File: `custom-policy-pack/__main__.py`**

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def s3_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:s3/bucket:Bucket" and "acl" in args.props:
        acl = args.props["acl"]
        if acl == "public-read" or acl == "public-read-write":
            report_violation(
                "You cannot set public-read or public-read-write on an S3 bucket. " +
                "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html")

s3_no_public_read = ResourceValidationPolicy(
    name="s3-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=s3_no_public_read_validator,
)

PolicyPack(
    name="aws-python",
    policies=[
        s3_no_public_read,
    ],
)
```

{{% /choosable %}}

Here you can see the basic structure of a policy pack:

- Some imports from the Pulumi Crossguard SDK
- a *function* that implements the policy
- a *policy* definition that wraps the implementation and describes the policy
- a *policy pack* definition that packages the policies together

While this example is a useful policy, it's not what we need right now. Let's delete all of that code and create some new custom policies.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

Replace the contents of `index.ts` with the following:

```typescript
{{< example-program-snippet path="custom-policy-pack" language="typescript">}}
```

Here we define three different policies:

- **s3-product-prefix**: Ensures S3 buckets are prefixed with the product name by checking the `bucketPrefix` property on all `aws:s3/bucket:BucketV2` resources.
- **ec2-instance-type-restricted**: Restricts EC2 instance types to only use the affordable `t2.micro` type, by checking the `instanceType` property on all `aws:ec2/instance:Instance` resources.
- **all-aws-resources-must-have-tags**: Ensures all AWS resources have at least one tag by checking the `tags` property on all resources who's type starts with `aws`.

Each of the policies uses the same pattern:

1. Define a `ResourceValidationPolicy` with a bit of metadata and a validation function. Each policy can have an individual enforcement level, name, and description.
1. The validation function is defined inline using the `validateResourceOfType` helper function. The way Crossguard *resource policies* work, each resource in the project will be passed to every policy in the pack. This strongly-typed helper function creates a filter that checks the resource type (e.g. `aws.ec2.Instance` from the `pulumi-aws` provider library) and will only run the validation function on resources that match the type.
1. The validation functions take an instance of the resource, an args property bag, and a function for reporting policy violations. Inside the validation function, we can check one or more properties on the strongly-typed resource instance.
1. If there is a problem with the property value, or some other aspect of the resource is out of compliance, we use the `reportViolation` function that was passed in to indicate that there's a problem. The error message should be a full sentence and give useful information on how to remediate the problem.

What's great about the strong typing in our SDK is that your IDE's intellisense knows the type definition and can give you dot-completion for properties on the resource instance, so there's no guessing about what the property is called, or what its type should be.

That said, sometimes you might need to write a policy that works against more than one resource type. For example, the `all-aws-resources-must-have-tags` policy checks every kind of AWS resource. In this case, instead of using the `validateResourceOfType` helper function, we just pass the anonymous function directly. Then, in the function we need to check the resource type *as a string* by inspecting the value of `args.type`.

If you're not sure what the correct resource type string is for your particular set of resources, you can run `pulumi stack` to list the resources in your current stack. The `TYPE` column of the output contains the same resource types strings that you would use to filter on inside of a policy. In our above example, we apply the policy to any resource who's type starts with `aws`.

```sh
$ pulumi stack
[...]
Current stack resources (5):
    TYPE                                    NAME
    pulumi:pulumi:Stack                     custom-policy-pack-integration-test-dev
    ├─ aws:s3/bucketV2:BucketV2             my-bucket
    ├─ aws:ec2/securityGroup:SecurityGroup  ssh-security-group
    ├─ aws:ec2/instance:Instance            web-server
    └─ pulumi:providers:aws                 default_6_65_0
```

Finally we assemble the policies into a policy pack object, giving it the name `custom-policy-pack`.

{{% notes type="tip" %}}
**Writing Testable Code**: We've structured this code to be a little bit more readable than the template example, and also more testable. Instead of defining everything in one big nested object, we break each policy out into its own definition and then assemble the policy pack at the end. We use the `export` keyword to make these policies available to the testing framework (although not technically necessary for the policy pack itself).

Have a look at the [`test`](https://github.com/pulumi/docs/blob/master/static/programs/custom-policy-pack-typescript/test/) directory in the [full version of this example](https://github.com/pulumi/docs/blob/master/static/programs/custom-policy-pack-typescript/) to see how you can write unit tests for each policy.

{{% /notes %}}

{{% /choosable %}}

{{% choosable language python %}}

Replace the contents of `__main__.py` with the following:

```python
{{< example-program-snippet path="custom-policy-pack" file="policies.py" language="python">}}
```

Here we define three different policies:

- **s3-product-prefix**: Ensures S3 buckets are prefixed with the product name by checking the `bucketPrefix` property on all `aws:s3/bucket:BucketV2` resources.
- **ec2-instance-type-restricted**: Restricts EC2 instance types to only use the affordable `t2.micro` type, by checking the `instanceType` property on all `aws:ec2/instance:Instance` resources.
- **all-aws-resources-must-have-tags**: Ensures all AWS resources have at least one tag by checking the `tags` property on all resources who's type starts with `aws`.

Each of the policies uses the same pattern:

1. Define a `ResourceValidationPolicy` with a bit of metadata and a validation function. Each policy can have an individual enforcement level, name, and description.
1. The validation function is defined separately and takes as its inputs an `args` object of type `ResourceValidationArgs` and `report_violation`, a function of type `ReportViolation`. The `args` object contains information about the resource to test, and the `report_violation` function is used to report policy violations.
1. The first step in a *resource policy* should always be to check the resource type using the `args.resource_type` property, to make sure it is something you want to act on. The way Crossguard *resource policies* work, each resource in the stack will be passed to every policy in the pack, so filtering out resources that don't relate to this check allows the policy engine to move on to the next policy/resource quickly.
1. Inside the validation function, we can check one or more properties on via the `args.props` property bag.
1. If there is a problem with the a property value, or some other aspect of the resource is out of compliance, we use the `reportViolation` function that was passed in to indicate that there's a problem. The error message should be a full sentence and give useful information on how to remediate the problem.

If you're not sure what the correct resource type string is for your particular set of resources, you can run `pulumi stack` to list the resources in your current stack. The `TYPE` column of the output contains the same resource types strings that you would use to filter on inside of a policy.

Sometimes you might need to write a policy that works against more than one type of resource. For example, the `all-aws-resources-must-have-tags` policy applies to every kind of AWS resource by checking if the resource type string starts with `aws`.

```sh
$ pulumi stack
[...]
Current stack resources (5):
    TYPE                                    NAME
    pulumi:pulumi:Stack                     custom-policy-pack-integration-test-dev
    ├─ aws:s3/bucketV2:BucketV2             my-bucket
    ├─ aws:ec2/securityGroup:SecurityGroup  ssh-security-group
    ├─ aws:ec2/instance:Instance            web-server
    └─ pulumi:providers:aws                 default_6_65_0
```

Finally we assemble the policies into a policy pack object in `__main__.py`, giving it the name `custom-policy-pack`.

```python
{{< example-program-snippet path="custom-policy-pack" file="__main__.py" language="python">}}
```

{{% notes type="tip" %}}
**Writing Testable Code**: We've structured this code to be a little bit more readable and testable than the template example. In the [full version of this example](https://github.com/pulumi/docs/blob/master/static/programs/custom-policy-pack-python/), the `PolicyPack` definition is in [`__main__.py`](https://github.com/pulumi/docs/blob/master/static/programs/custom-policy-pack-python/__main__.py) while the policies are in [`policies.py`](https://github.com/pulumi/docs/blob/master/static/programs/custom-policy-pack-python/policies.py). This allows us to import the policies into to the testing framework, without including the `PolicyPack`, which would cause a unit test run to hang. Have a look at the [`policy_tests.py`](https://github.com/pulumi/docs/blob/master/static/programs/custom-policy-pack-python/policy_tests.py) file to see how you can write unit tests for each policy.
{{% /notes %}}

{{% /choosable %}}

Next up, we'll validate our custom policy pack by checking some cloud resources for compliance. Let's go!

{{< tutorials/stepper >}}
