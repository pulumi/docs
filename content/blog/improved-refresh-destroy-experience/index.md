---
title: "Improved refresh and destroy experience for Pulumi IaC"
date: 2025-04-02
meta_desc: "Pulumi now runs your code before refresh and destroy operations, enabling dynamic credential updates and complex workflows"
meta_image: meta.png
authors:
    - will-jones
tags:
    - features
    - releases
    - iac
---

Pulumi enables teams to manage their infrastructure using the programming languages and tools they are already familiar with, supporting use cases such as complex authentication workflows, dynamically configured resources, and more.

In this post we're excited to announce an improvement to the `pulumi refresh` and `pulumi destroy` commands: the `--run program` flag! This new feature makes Pulumi even more powerful for teams with complex infrastructure workflows.

This enhancement is particularly valuable for teams working with short-lived credentials, dynamic resources, or any workflow where your code needs to run to establish the right context. Whether you're using OIDC-based authentication, dynamically fetching credentials from a secrets manager, or working with [dynamic providers](/docs/iac/concepts/resources/dynamic-providers), the `--run-program` flag ensures your infrastructure operations have the context they need to succeed.

<!--more-->

The `pulumi refresh` and `pulumi destroy` commands sit alongside `pulumi up` and support refreshing and destroying resources in your stack. While `refresh` and `destroy` take into account updated configuration (such as that specified in your `Pulumi.<stack>.yaml`), they have historically not taken into account changes in your *code*. For stacks which depend on code to update credentials for a provider, or to determine which resources to create, this can break or hamper the use of `refresh` and `destroy`. Well, no more! As of the latest release of Pulumi (v3.160.0), the `pulumi refresh` and `pulumi destroy` commands now support the `--run-program` flag, which allows you to run your program before refreshing or destroying your stack.

## Let's see it in action

We are writing a Pulumi program to deploy infrastructure to AWS. Our organization's platform team provides us with a library that we can use to dynamically fetch appropriate AWS credentials for our stack. We use this to retrieve some values and set up an explicit AWS provider ([1](https://www.pulumi.com/blog/disable-default-providers/), [2](https://www.pulumi.com/docs/iac/concepts/resources/providers/), [3](https://www.pulumi.com/registry/packages/aws/api-docs/provider/)):

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
package main

import (
    "github.com/org/config"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        awsConfig, err := config.GetAWSConfig(ctx)
        if err != nil {
            return err
        }

        provider, err := aws.NewProvider(ctx, "provider", &s3.ProviderArgs{
            AccessKey: awsConfig.AccessKey,
            SecretKey: awsConfig.SecretKey,
            Token:     awsConfig.SecurityToken,
            Region:    awsConfig.Region,
        })
        if err != nil {
            return err
        }

        bucket, err := s3.NewBucket(ctx, "bucket", &s3.BucketArgs{ ... }, pulumi.Provider(provider))
        if err != nil {
            return err
        }

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package app;

import com.org.AwsConfig;
import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.Provider;
import com.pulumi.aws.ProviderArgs;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.aws.s3.BucketArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        final var awsConfig = AwsConfig.getAWSConfig(ctx.projectName(), ctx.stackName());

        final var provider = new Provider("provider", ProviderArgs.builder()
            .accessKey(awsConfig.accessKey())
            .secretKey(awsConfig.secretKey())
            .token(awsConfig.securityToken())
            .region(awsConfig.region())
            .build());

        final var bucket = new Bucket("bucket", BucketArgs.builder().....build(),
            pulumi.CustomResourceOptions.builder().provider(provider).build());
    }
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Threading.Tasks;

using Org.Config;
using Pulumi;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}

class MyStack : Stack
{
    public MyStack()
    {
        var awsConfig = GetAwsConfig(
            project: Deployment.Instance.ProjectName,
            stack: Deployment.Instance.StackName
        );

        var provider = new Pulumi.Aws.Provider("provider", new Pulumi.Aws.ProviderArgs
        {
            AccessKey = awsConfig.AccessKey,
            SecretKey = awsConfig.SecretKey,
            Token = awsConfig.SecurityToken,
            Region = awsConfig.Region,
        });

        var bucket = new Pulumi.Aws.S3.Bucket("bucket", new Pulumi.Aws.S3.BucketArgs {
            ...
        }, new Pulumi.ResourceOptions {
            Provider = provider
        });
    }
}
```

{{% /choosable %}}

{{% /chooser %}}

We run `pulumi up` and everything works as we expect -- our program grabs the appropriate tokens and sets up our S3 bucket.

A few days, weeks, months, or even years later, we find that some tweaks have been made to the bucket in the AWS console. Before we update and re-run our program, we want to refresh Pulumi's state so that it picks up the current properties of the bucket. We run `pulumi refresh` and, after waiting a while... it fails! What has gone wrong?

The issue is that our program needs to run to fetch the latest credentials using our platform team's library. However, `pulumi refresh` doesn't run our program by default. To fix this, we can use the new `--run-program` flag:

```shell
pulumi refresh --run-program
```

This time, Pulumi will run our program before refreshing the state of our stack. As a result, our program will fetch the latest credentials using the library provided by our platform team, and everything will work as expected! If in a few months we need to clean up our stack, `pulumi destroy` also accepts the new option:

```shell
pulumi destroy --run-program
```

## What's next?

Running the program for all Pulumi operations paves the way for several other highly-requested features. Top of our list is [lifecycle hooks](https://github.com/pulumi/pulumi/issues/1691) -- the ability to run arbitrary program code at various points in the lifecycle of a Pulumi resource.

We'd love to hear how you're using the new `--run-program` flag! Share your experiences with us on [GitHub](https://github.com/pulumi/pulumi), [X](https://twitter.com/pulumicorp), or our [Community Slack](https://slack.pulumi.com/).
