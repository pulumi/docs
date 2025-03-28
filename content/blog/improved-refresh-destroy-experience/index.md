---
title: "Improved refresh and destroy experience"
date: 2025-04-01
meta_desc: "Refreshing and destroying programs will now use updates from your program"
authors:
    - fraser-waters
    - meagan-cojocar
tags:
    - features
---

Pulumi enables teams to manage their infrastructure using the programming
languages and tools they are already familiar with, supporting use cases such as
more complex authentication workflows, dynamically configured resources, and
more. Loops, conditionals, environment variables, external calls -- if your
language can do it, `pulumi up` will run it.

The `pulumi refresh` and `pulumi destroy` commands sit alongside `pulumi up` and
support refreshing and destroying resources in your stack. While `refresh` and
`destroy` take into account updated configuration (such as that specified in
your `Pulumi.<stack>.yaml`), they have historicall not taken into account
changes in your *code*. For stacks which depend on code to update credentials
for a provider, or to determine which resources to create, this can break or
severely hamper the use of `refresh` and `destroy`. Well, no more! As of the
latest release of Pulumi, the `pulumi refresh` and `pulumi destroy` commands now
support the `--run-program` flag, which allows you to run your program before
refreshing or destroying your stack. (And no, this is not an April Fool's joke!)

<!--more-->

## What does this mean?

We are writing a Pulumi program to deploy infrastructure to AWS. Our
organization's platform team provides us with a library that we can use to
dynamically fetch appropriate AWS credentials for our stack (perhaps backed by
something like [Pulumi ESC](https://www.pulumi.com/docs/esc)). We use this to
retrieve some values and set up an explicit AWS provider
([1](https://www.pulumi.com/blog/disable-default-providers/),
[2](https://www.pulumi.com/docs/iac/concepts/resources/providers/),
[3](https://www.pulumi.com/registry/packages/aws/api-docs/provider/)):

{{% chooser language "javascript,typescript,python,go,java,csharp" %}}

{{% choosable language javascript %}}

```javascript
import * as orgConfig from "@org/config";
import * as aws from "@pulumi/aws";

export = async () => {
    const awsConfig = await orgConfig.getAWSConfig({
        project: pulumi.getProject(),
        stack: pulumi.getStack(),
    });

    const provider = new aws.Provider("provider", {
        accessKey: awsConfig.accessKey,
        secretKey: awsConfig.secretKey,
        token: awsConfig.securityToken,
        region: awsConfig.region,
    });

    const bucket = new aws.s3.Bucket("bucket", { ... }, { provider });
};
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as orgConfig from "@org/config";
import * as aws from "@pulumi/aws";

export = async () => {
    const awsConfig = await orgConfig.getAWSConfig({
        project: pulumi.getProject(),
        stack: pulumi.getStack(),
    });

    const provider = new aws.Provider("provider", {
        accessKey: awsConfig.accessKey,
        secretKey: awsConfig.secretKey,
        token: awsConfig.securityToken,
        region: awsConfig.region,
    });

    const bucket = new aws.s3.Bucket("bucket", { ... }, { provider });
};
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import org_config
import pulumi
import pulumi_aws as aws

aws_config = org_config.get_aws_config(
    project=pulumi.get_project(),
    stack=pulumi.get_stack(),
)

provider = aws.Provider("provider",
    access_key=aws_config.access_key,
    secret_key=aws_config.secret_key,
    token=aws_config.security_token,
    region=aws_config.region,
)

bucket = aws.s3.Bucket("bucket", ... , opts=pulumi.ResourceOptions(provider=provider))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
```

{{% /choosable %}}

{{% choosable language java %}}

```java
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
```

{{% /choosable %}}

{{% /chooser %}}

We run `pulumi up` and everything works as we expect -- our program grabs the
appropriate tokens and sets up our S3 bucket.

A few days, weeks, months, or even years later, we find that some tweaks have
been made to the bucket in the AWS console. Before we update and re-run our
program, we want to refresh Pulumi's state so that it picks up the current
properties of the bucket. We run `pulumi refresh` and, after waiting a while...
it fails! What has gone wrong?

## The current state of affairs

Historically, `pulumi refresh` has had a simple task -- to refresh the state of
every single resource in a given stack. In order to do this, it looks at each
resource in the Pulumi state, comparing what it finds with the latest changes
read from the provider. If it finds any differences, it updates the state
accordingly. No program necessary! Unless, for instance, reading from the
provider requires some dynamic configuration that is either not present in the
Pulumi state, or is present but is now stale or out-of-date.
