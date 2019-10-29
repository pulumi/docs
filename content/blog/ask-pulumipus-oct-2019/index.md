---
title: "Ask Pulumipus"
date: "2019-10-24"
meta_desc: "Answers to questions from Stack Overflow"
meta_image: "twitter_card_pulumipus.svg"
authors: ["sophia-parafina"]
tags: ["Pulumi","questions","support","slack","stack overflow"]
---

# Ask Pulumipus

Welcome to Ask Pulumipus, an irregular series of questions and answers from the community. Where do these questions come from? In addition to issues on Github, we also get questions from Stack Overflow.

And just who is Pulumipus? Glad you asked! Pulumipus is our platypus mascot who inspires us to build applications such as Platypull which automates our build process.

## Getting Secrets with Pulumi

[Stack Exchange Data Explorer](https://data.stackexchange.com/) is good resource for revealing the most popular queation. We can get a list of questions ranked by the number of views a question has received. Our first and most popular [question](https://data.stackexchange.com/) is how to retrieve a secret through the Pulumi API.

>"I have a service with an inline plaintext config that requires certain information that is stored in Kubernetes secrets. What @pulumi/kubernetes API method can be used to access raw kubernetes secret values?"

StackOverflow user [Dominik](https://stackoverflow.com/users/1168315/dominik) correctly notes that every Pulumi resource has a get() method that lets you get all the the details for a resource such as [Secrets](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/kubernetes/core/v1/#Secret). It's important to note that Pulumi automatically encrypts `data` and `stringData` fields only in Pulumi's context, but Kubernetes does not encrypt secrets by default and users can access secrets with tools such as `kubectl`.

Dominik provides a concise example for getting a Secret using the Pulumi API.

```typescript
import * as k8s from "@pulumi/kubernetes";
​
type KubernetesSecretData = { [key: string]: string }
​
const namespace = 'kube-public'
const secretName = 'default-token-tdcdz'
​
export const token =
    k8s.core.v1.Secret.get('testSecret',`${namespace}/${secretName}`)
        .data.apply(v => {
        return (<KubernetesSecretData> v)["token"]
    })
```

Although the topic of question is about secrets, the get() method will work on any Pulumi ressource.

## Setting the Order of Resource Creation

It's not uncommon for a resource to depend on another resource before it can be created. In general, Pulumi handles the resource creation order automatically. Pulumi resolves all parameters needed by a resource; so if a resource is needed to create another resource, the dependent resource will be create first.

However, there are cases where there is an explicit dependency between resource usually when the dependency is outside of the Pulumi context. Here's the [question](https://stackoverflow.com/questions/50957692/how-to-control-resource-creation-order-in-pulumia) from StackOverflow:

> "I'm trying to create some resources and need to enforce some sort of creation order. e.g. creating an aws.s3.Bucket for storing the logs before it can be used as an input to aws.cloudfront.Distribution.
>
> How do I control resource creation order when using Pulumi?"

The answer is that you can use `pulumi.ResourceOptions` and set the `dependsOn` property to the required resource. The Pulumi engine resolves the all the resources specified in the `dependsOn` array.

In this example, we want to place files in AWS S3 buckets. In the first case, we want to create a file in a bucket. Pulumi will create a bucket before creating `file1`. In the second case, we want to create `file2` in a bucket called `example-bucket` but Pulumi doesn't know to create `example-bucket` before create `file2`. You can use the `dependsOn` array to make the Pulumi engine create the `example-bucket` before creating `file2`.

```typescript
// Create a bucket named "example-bucket", available at s3://example-bucket.
let bucket = new aws.s3.Bucket("bucket",
    {
        bucket: "example-bucket",
    });

let file1 = new aws.s3.BucketObject("file1", {
    // The bucket field of BucketObjectArgs is an instance of
    // aws.s3.Bucket. Pulumi will know to create the "bucket"
    // resource before this BucketObject resource.
    bucket: bucket,
});

let file2 = new aws.s3.BucketObject("file2",
    {
        // The bucket field of BucketObjectArgs is a string. So
        // Pulumi does not know to block creating the file2 resource
        // until the S3 bucket exists.
        bucket: "example-bucket",
    } as aws.s3.BucketArgs,
    {
        // By putting "bucket" in the "dependsOn" array here,
        // the Pulumi engine will create the bucket resource before
        // this file2 resource.
        dependsOn: [ bucket ],
    } as pulumi.ResourceOptions);
```

## We Love Questions

Stack Overflow is great resource because it easy to search but for faster and more direct responses join us on [Pulumi Community Slack](https://pulumi-community.slack.com).
