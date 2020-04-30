---
title: "AWS Elastic Container Registry (ECR)"
meta_desc: Pulumi Crosswalk for AWS ECR makes the provisioning of new ECR repositories as simple as one line of code.
linktitle: Elastic Container Registry (ECR)
menu:
  userguides:
    parent: crosswalk-aws
    weight: 4

aliases: ["/docs/reference/crosswalk/aws/ecr/"]
---

<a href="{{< prelref "./" >}}">
    <img src="/images/docs/reference/crosswalk/aws/logo.svg" align="right" width="280" style="margin: 0 0 32px 16px;">
</a>

[Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) is a managed Docker container registry that
makes it easy to store, manage, and deploy Docker container images. ECR supports private Docker registries with
resource-based permissions using AWS IAM, so specific users and instances can access images. Using ECR simplifies
going from development to production, and eliminates the need to operate your own container repositories or worry
about scaling the underlying infrastructure, while hosting your images in a highly available and scalable architecture.

## Overview

Pulumi Crosswalk for AWS ECR makes the provisioning of new ECR repositories as simple as one line of code,
integrates with Pulumi Crosswalk for AWS [ECS]({{< prelref "ecs" >}}) and [EKS]({{< prelref "eks" >}}) to ease
deployment of new application containers to your ECS, "Fargate", and/or Kubernetes clusters, and even supports
building and deploying Docker images from your developer desktop or CI/CD workflows.

## Provisioning an ECR Repository

Each AWS account automatically has an ECR [_registry_](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries.html),
and within each registry, you can create any number of [_repositories_](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) to actually contain your Docker images.

To create a new ECR repository, simply allocate an instance of the `awsx.ecr.Repository` class:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a repository.
const repo = new awsx.ecr.Repository("my-repo");

// And publish its URL, so we can push to it if we'd like.
export const url = repo.repository.repositoryUrl;
```

From there, we can just run `pulumi up` to provision a new repository:

```bash
$ pulumi up
Updating (dev):

     Type                           Name               Status
 +   pulumi:pulumi:Stack            crosswalk-aws-dev  created
 +   └─ awsx:ecr:Repository         my-repo            created
 +      ├─ aws:ecr:Repository       my-repo            created
 +      └─ aws:ecr:LifecyclePolicy  my-repo            created

Outputs:
    url: "012345678901.dkr.ecr.us-west-2.amazonaws.com/my-repo-e2fe830"

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
$ $(aws ecr get-login --no-include-email)
```

Notice the `$(...)` part, which executes the command returned by the AWS CLI (which is a `docker login ...` sequence).
For more information on authentication, please see [Registry Authentication](
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

The ECR repository class has a `buildAndPushImage` function that does this in one go:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a repository, as before.
const repo = new awsx.ecr.Repository("my-repo");

// Build an image from the "./app" directory (relative to our project and containing Dockerfile),
// and publish it to our ECR repository provisioned above.
export const image = repo.buildAndPushImage("./app");
```

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

```typescript
import * as awsx from "@pulumi/awsx";

// Build and publish an image.
const repo = new awsx.ecr.Repository("app");
const image = repo.buildAndPushImage("./app");

// Create a load balanced service using this image.
const lb = new awsx.lb.NetworkListener("app", { port: 80 });
const nginx = new awsx.ecs.FargateService("app", {
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: image,
                portMappings: [ lb ],
            },
        },
    },
    desiredCount: 2,
});

// Export the URL for the load balanced service.
export const url = lb.endpoint.hostname;
```

In the case where you don't really need to use the repository (except as a place to store the built image), the above
can be simplified to:

```typescript
import * as awsx from "@pulumi/awsx";

// Create a load balanced service using out of a built Docker image.
const lb = new awsx.lb.NetworkListener("app", { port: 80 });
const nginx = new awsx.ecs.FargateService("app", {
    taskDefinitionArgs: {
        containers: {
            nginx: {
                image: awsx.ecr.buildAndPushImage("app", "./app").image(),
                portMappings: [ lb ],
            },
        },
    },
    desiredCount: 2,
});

// Export the URL for the load balanced service.
export const url = lb.endpoint.hostname;
```

For information about ECS, refer to the [Pulumi Crosswalk for AWS ECS documentation]({{< prelref "ecs" >}}). For
information about consuming ECR images from ECS services specifically, please see
[Using Amazon ECR Images with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html).

### Consuming a Private Repository from EKS

To use your private repository from a Kubernetes service, such as one using EKS, reference it like so:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Build and publish to an ECR registry.
const repo = new awsx.ecr.Repository("my-repo");
const image = repo.buildAndPushImage("./app");

// Create a new EKS cluster.
const cluster = new eks.Cluster("cluster");

// Create a NGINX Deployment and load balanced Service, running our app.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image, // **Use the image built above**
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;
```

In the case where you don't really need to use the repository (except as a place to store the built image), the above
can be simplified to:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create a new EKS cluster.
const cluster = new eks.Cluster("cluster");

// Create a NGINX Deployment and load balanced Service, running our app.
const appName = "my-app";
const appLabels = { appClass: appName };
const deployment = new k8s.apps.v1.Deployment(`${appName}-dep`, {
    metadata: { labels: appLabels },
    spec: {
        replicas: 2,
        selector: { matchLabels: appLabels },
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: appName,
                    image: awsx.ecr.buildAndPushImage("my-repo", "./app").image(),
                    ports: [{ name: "http", containerPort: 80 }]
                }],
            }
        }
    },
}, { provider: cluster.provider });
const service = new k8s.core.v1.Service(`${appName}-svc`, {
    metadata: { labels: appLabels },
    spec: {
        type: "LoadBalancer",
        ports: [{ port: 80, targetPort: "http" }],
        selector: appLabels,
    },
}, { provider: cluster.provider });

// Export the URL for the load balanced service.
export const url = service.status.loadBalancer.ingress[0].hostname;
```

For information about EKS, refer to the [Pulumi Crosswalk for AWS EKS documentation]({{< prelref "eks" >}}).

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

See the [Pulumi Crosswalk for AWS IAM documentation]({{< prelref "iam" >}}) for instructions on how to manage
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

Policies can apply to all images, untagged images, or tagged images that match a specific tag-prefix.

By default an `awsx.ecr.Repository` is created with a policy that will only keep at most one untagged image
around. In other words, the following repositories have equivalent lifecycle policies:

```typescript
const repository1 = new awsx.ecr.Repository("app1");
const repository2 = new awsx.ecr.Repository("app2", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: "untagged",
            maximumNumberOfImages: 1,
        }],
    },
});
```

### Lifecycle Policy Rules

A custom lifecycle policy is built from one or more `rules`, ordered in the array from lowest priority to
highest priority. The collection of rules are interpreted as follows:

1. An image is expired by exactly one or zero rules.
2. An image that matches the tagging requirements of a higher priority rule cannot be expired by a
   rule with a lower priority.
3. Rules can never mark images that are marked by higher priority rules, but can still identify them
   as if they haven't been expired.
4. The set of rules must contain a unique set of tag prefixes.
5. Only one rule is allowed to select `untagged` images.
6. Expiration is always ordered by the "pushed at time" for an image, and always expires older
   images before newer ones.
7. When using the `tagPrefixList`, an image is successfully matched if all of the tags in the
   `tagPrefixList` value are matched against any of the image's tags.
8. With `maximumNumberOfImages`, images are sorted from youngest to oldest based on their "pushed at
   time" and then all images greater than the specified count are expired.
9. `maximumAgeLimit`, all images whose "pushed at time" is older than the specified number of days
   based on `countNumber` are expired.

For more details, refer to [Amazon ECR Lifecycle Policies](
https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html), however we will now examine
a number of examples to demonstrate how lifecycle policies are applied.

### Examples

#### Example A:

The following example shows the lifecycle policy syntax for a policy that expires untagged images older than 14 days:

```typescript
const repository = new awsx.ecr.Repository("app", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: "untagged",
            maximumAgeLimit: 14,
        }],
    },
});
```

#### Example B: Filtering on Multiple Rules

The following examples use multiple rules in a lifecycle policy. An example repository and lifecycle policy are given
along with an explanation of the outcome:

```typescript
const repository = new awsx.ecr.Repository("app", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: { tagPrefixList: ["prod"] },
            maximumNumberOfImages: 1,
        }, {
            selection: { tagPrefixList: ["beta"] },
            maximumNumberOfImages: 1,
        }],
    },
});
```

Repository contents:

* Image A, Taglist: `["beta-1", "prod-1"]`, Pushed: 10 days ago
* Image B, Taglist: `["beta-2", "prod-2"]`, Pushed: 9 days ago
* Image C, Taglist: `["beta-3"]`, Pushed: 8 days ago

The logic of this lifecycle policy would be:

1. Rule 1 identifies images tagged with prefix `prod`. It should mark images, starting with the
   oldest, until there is one or fewer images remaining that match. It marks Image A for expiration.

2. Rule 2 identifies images tagged with prefix beta. It should mark images, starting with the
   oldest, until there is one or fewer images remaining that match. It marks both Image A and Image
   B for expiration. However, Image A has already been seen by Rule 1 and if Image B were expired it
   would violate Rule 1 and thus is skipped.

Result: Image A is expired.

#### Example C: Filtering on Multiple Rules

This is the same repository as the previous example but the rule priority order is changed to illustrate the outcome:

```typescript
const repository = new awsx.ecr.Repository("app", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: { tagPrefixList: ["beta"] },
            maximumNumberOfImages: 1,
        }, {
            selection: { tagPrefixList: ["prod"] },
            maximumNumberOfImages: 1,
        }],
    },
});
```

Repository contents:

* Image A, Taglist: `["beta-1", "prod-1"]`, Pushed: 10 days ago
* Image B, Taglist: `["beta-2", "prod-2"]`, Pushed: 9 days ago
* Image C, Taglist: `["beta-3"]`, Pushed: 8 days ago

The logic of this lifecycle policy would be:

1. Rule 1 identifies images tagged with beta. It should mark images, starting with the oldest, until
   there is one or fewer images remaining that match. It sees all three images and would mark Image
   A and Image B for expiration.

2. Rule 2 identifies images tagged with prod. It should mark images, starting with the oldest, until
   there is one or fewer images remaining that match. It would see no images because all available
   images were already seen by Rule 1 and thus would mark no additional images.

Result: Images A and B are expired.

#### Example D: Filtering on Multiple Tags in a Single Rule

The following examples specify the lifecycle policy syntax for multiple tag prefixes in a single rule. An example
repository and lifecycle policy are given along with an explanation of the outcome.

When multiple tag prefixes are specified on a single rule, images must match all listed tag prefixes:

```typescript
const repository = new awsx.ecr.Repository("app", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: { tagPrefixList: ["alpha", "beta"] },
            maximumAgeLimit: 5,
        },
    },
});
```

Repository contents:

* Image A, Taglist: `["alpha-1"]`, Pushed: 12 days ago
* Image B, Taglist: `["beta-1"]`, Pushed: 11 days ago
* Image C, Taglist: `["alpha-2", "beta-2"]`, Pushed: 10 days ago
* Image D, Taglist: `["alpha-3"]`, Pushed: 4 days ago
* Image E, Taglist: `["beta-3"]`, Pushed: 3 days ago
* Image F, Taglist: `["alpha-4", "beta-4"]`, Pushed: 2 days ago

The logic of this lifecycle policy would be:

1. Rule 1 identifies images tagged with alpha and beta. It sees images C and F. It should mark
   images that are older than five days, which would be Image C.

2. Result: Image C is expired.

#### Example E: Filtering on All Images

The following lifecycle policy examples specify all images with different filters. An example repository and lifecycle
policy are given along with an explanation of the outcome:

```typescript
const repository = new awsx.ecr.Repository("app", {
    lifeCyclePolicyArgs: {
        rules: [{
            selection: "any",
            maximumNumberOfImages: 5,
        },
    },
});
```

Repository contents:

* Image A, Taglist: `["alpha-1"]`, Pushed: 4 days ago
* Image B, Taglist: `["beta-1"]`, Pushed: 3 days ago
* Image C, Taglist: `[]`, Pushed: 2 days ago
* Image D, Taglist: `["alpha-2"]`, Pushed: 1 day ago

The logic of this lifecycle policy would be:

1. Rule 1 identifies all images. It sees images A, B, C, and D. It should expire all images other
   than the newest one. It marks images A, B, and C for expiration.

2. Result: Images A, B, and C are expired.

## Additional ECR Resources

For more information about Amazon ECR, please see the following:

* [Amazon Elastic Container Registry homepage](https://aws.amazon.com/ecr/)
