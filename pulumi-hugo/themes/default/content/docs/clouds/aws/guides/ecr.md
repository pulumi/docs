---
title_tag: "Using AWS Elastic Container Registry (ECR) | Crosswalk"
title: ECR
h1: AWS Elastic Container Registry (ECR)
meta_desc: Pulumi Crosswalk for AWS ECR makes the provisioning of new ECR repositories as simple as one line of code.
meta_image: /images/docs/meta-images/docs-clouds-aws-meta-image.png
menu:
  clouds:
    parent: aws-guides
    identifier: aws-guides-ecr
    weight: 4

aliases:
- /docs/reference/crosswalk/aws/ecr/
- /docs/guides/crosswalk/aws/ecr/
---

<a href="./">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) is a managed Docker container registry that
makes it easy to store, manage, and deploy Docker container images. ECR supports private Docker registries with
resource-based permissions using AWS IAM, so specific users and instances can access images. Using ECR simplifies
going from development to production, and eliminates the need to operate your own container repositories or worry
about scaling the underlying infrastructure, while hosting your images in a highly available and scalable architecture.

## Overview

Pulumi Crosswalk for AWS ECR makes the provisioning of new ECR repositories as simple as one line of code,
integrates with Pulumi Crosswalk for AWS [ECS](/docs/clouds/aws/guides/ecs/) and [EKS](/docs/clouds/aws/guides/eks/) to ease
deployment of new application containers to your ECS, "Fargate", and/or Kubernetes clusters, and even supports
building and deploying Docker images from your developer desktop or CI/CD workflows.

## Provisioning an ECR Repository

Each AWS account automatically has an ECR [_registry_](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html),
and within each registry, you can create any number of [_repositories_](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) to actually contain your Docker images.

To create a new ECR repository, allocate an instance of the `awsx.ecr.Repository` class:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript" %}}

```javascript
"use strict";
const awsx = require("@pulumi/awsx");

const repo = new awsx.ecr.Repository("repo");
exports.url = repo.url;
```

{{% /choosable %}}

{{% choosable language "typescript" %}}

```typescript
import * as awsx from "@pulumi/awsx";

const repo = new awsx.ecr.Repository("repo");
export const url = repo.url;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("repository")
pulumi.export("url", repository.url)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/go/awsx/ecr"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		repository, err := ecr.NewRepository(ctx, "repository", nil)
		if err != nil {
			return err
		}

		ctx.Export("url", repository.Url)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var repository = new Awsx.Ecr.Repository("repository");

    return new Dictionary<string, object?>
    {
        ["url"] = repository.Url,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.awsx.ecr.Repository;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var repository = new Repository("repository");

        ctx.export("url", repository.url());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
resources:
  repository:
    type: awsx:ecr:Repository
outputs:
  url: ${repository.url}
```

{{% /choosable %}}

From there, we can just run `pulumi up` to provision a new repository:

```bash
$ pulumi up
Updating (dev):

     Type                           Name               Status
 +   pulumi:pulumi:Stack            crosswalk-aws-dev  created
 +   ├─ awsx:ecr:Repository         repository         created
 +   │  └─ aws:ecr:Repository       repository         created
 +   └─ aws:ecr:LifecyclePolicy     repository         created

Outputs:
    url: "012345678901.dkr.ecr.us-west-2.amazonaws.com/repository-e2fe830"

Resources:
    + 4 created

Duration: 4s
```

The `url` emitted is what we will use to push and pull images to and from the newly created repository. We can do
so either using the Docker CLI or through infrastructure as code in our Pulumi program.

## Building and Publishing Container Images

Amazon ECR stores [_images_](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images.html) inside of the
repositories you create. You can use the Docker CLI to push and pull images explicitly, using the `build`, `push`,
and `pull` commands, targeting the repository's URL. Alternatively, you can use your Pulumi program to build and
publish container images as part of your Pulumi deployment, and consume them from ECS or EKS directly.

### Building and Publishing Images Manually Using the Docker CLI

All repositories in your account's ECR registry will have a URL of the form
`<aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repo>`, where `<aws_account_id>` is your AWS account ID,
`<region>` is the location for the repository, and `<repo>` is the name given to the repository. In the above example,
the resulting URL is exported and printed to the console.

To build and publish a new Docker image to such a repository, first retrieve your container image in the usual way,
e.g. either using [`docker build`](https://docs.docker.com/engine/reference/commandline/build/) or
[`docker pull`](https://docs.docker.com/engine/reference/commandline/pull/).

The image then needs to be tagged with the URL of the repository you're publishing to. This can be done using
`docker build`'s `-t` argument, while building the image, as in:

```bash
$ docker build -t 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830 .
```

Alternatively, this can be done by tagging the image with [`docker tag`](
https://docs.docker.com/engine/reference/commandline/tag/) after building or pulling it. For example, if the image
ID to tag is `e9ae3c220b23`, then we would run the following:

```bash
$ docker tag e9ae3c220b23 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830
```

By default, this tag will be tagged as `latest`; if you'd like to tag it using something else, do so as usual:

```bash
$ docker tag e9ae3c220b23 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830:v2.0
```

After building and tagging, we then need to authenticate with the ECR registry. Each authentication token covers a
single registry and lasts 12 hours. The AWS CLI provides an easy way to do this:

```bash
$ aws ecr get-login-password | docker login --username AWS --password-stdin 012345678901.dkr.ecr.us-west-2.amazonaws.com
```

For more information on authentication, see [Registry Authentication](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html#registry_auth)

Finally, after building, tagging, and logging in, we are ready to push to our repository:

```bash
$ docker push 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830
The push refers to repository [012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830]
8a453b312607: Pushed
e6b5722b9fb4: Pushed
137a99b96f0d: Pushed
d6c6b3975afa: Pushed
36daa25da760: Pushed
be03501d5dd0: Pushed
3f9a4fb2ec3f: Pushed
a464c54f93a9: Pushed
latest: digest: sha256:f2d7dca5c0800e2dce13b655a439f368587b77ad82de11675851be4c9f2cbf91 size: 1999
```

Afterwards, we can then pull the image from the registry by authenticating and pulling from the repository URL.

### Building and Publishing Images Automatically in Code

Instead of using the Docker CLI directly, Pulumi supports building, publishing, and consuming Docker images
entirely from code. This lets you version and deploy container changes easily alongside the supporting infrastructure.

In the following example, creating an `Image` resource will build an image from the "./app" directory (relative to our project and containing Dockerfile), and publish it to our ECR repository provisioned above.

{{< example-program path="awsx-ecr-image" >}}

As we run `pulumi up`, we will see Docker build output in the Pulumi CLI display. If there is an error, it'll
be printed in the diagnostics section, but otherwise the resulting image name is printed:

```bash
$ pulumi up
Updating (dev):

     Type                           Name               Status
 +   pulumi:pulumi:Stack            crosswalk-aws-dev  created
 +   └─ awsx:ecr:Repository         my-repo            created
 +      ├─ aws:ecr:Repository       my-repo            created
 +      └─ aws:ecr:LifecyclePolicy  my-repo            created

Outputs:
    image: "012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830:latest"

Resources:
    + 4 created

Duration: 13s
```

This image URL can then be used anywhere you'd normally use a Docker image name. For example, we can run it:

```bash
$ docker run -p 80:80 012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830:latest
```

As we will see below, this can also be consumed from your container orchestrator, to run the container as a service.

### Deleting Images

If you are done using an image, you can delete it from your repository. This can be done by [defining a lifecycle
policy](#managing-container-image-lifecycles-using-policies) or manually using the AWS CLI. For more information on
how to manually delete an image, see the ECR documentation on [Deleting an Image](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html).

## Using a Private Repository from Your Container Orchestrator

To use your ECR images with Amazon ECS and EKS, use the full repository name as the image name. As seen above,
this is of the form `<aws_account_id>.dkr.ecr.<region>.amazonaws.com/<repo>[:<tag>]`, where the `<tag>` is optional (it
defaults to `latest`). The container instances require IAM permissions which are typically enabled by default.

### Consuming a Private Repository from ECS

To use your private repository from an ECS task definition, reference it like so:

{{< example-program path="awsx-load-balanced-fargate-ecr" >}}

For information about ECS, refer to the [Pulumi Crosswalk for AWS ECS documentation](/docs/clouds/aws/guides/ecs/). For
information about consuming ECR images from ECS services specifically, see
[Using Amazon ECR Images with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html).

### Consuming a Private Repository from EKS

To use your private repository from a Kubernetes service, such as one using EKS, reference it like so:

{{< example-program path="awsx-ecr-eks-deployment-service" >}}

For information about EKS, refer to the [Pulumi Crosswalk for AWS EKS documentation](/docs/clouds/aws/guides/eks/).

### IAM Permissions Required to use ECR

For the above examples to work, the container instances powering your ECS or EKS cluster need proper IAM
policy permissions to access your Amazon ECR registry. The following example defines such an IAM policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:BatchCheckLayerAvailability",
                "ecr:BatchGetImage",
                "ecr:GetDownloadUrlForLayer",
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
```

See the [Pulumi Crosswalk for AWS IAM documentation](/docs/clouds/aws/guides/iam/) for instructions on how to manage
such policies.

## Managing Container Image Lifecycles using Policies

[ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) allow
you to specify the lifecycle management of images in a repository. A lifecycle policy is a set of one or more rules,
where each rule defines an action for Amazon ECR. The actions apply to images that contain tags prefixed with the
given strings. This allows the automation of cleaning up unused images, for example expiring images based on age or
count. You should expect that after creating a lifecycle policy the affected images are expired within 24 hours.

Pulumi Crosswalk for AWS ECR module makes it easy to configure a repository's lifecycle policy, using the
`lifeCyclePolicyArgs` property on the `Repository` class's constructor. Using this property, there are two main ways
to control how an image is purged from the repository:

1. Once a maximum number of images has been reached (`maximumNumberOfImages`).
2. Once an image reaches a maximum allowed age (`maximumAgeLimit`).

### Lifecycle Policy Rules

For more details, refer to [Amazon ECR Lifecycle Policies](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html), however we will now examine
a number of examples to demonstrate how lifecycle policies are applied.

## Additional ECR Resources

For more information about Amazon ECR, see the following:

* [Amazon Elastic Container Registry homepage](https://aws.amazon.com/ecr/)
