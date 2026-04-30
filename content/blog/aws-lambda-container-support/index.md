---
title: Running Container Images in AWS Lambda
allow_long_title: true
date: 2020-12-01
updated: 2026-04-30
changelog:
    - 2026-04-30: Refreshed for 2026 with current Lambda container limits and pricing, side-by-side TypeScript and Python examples, a Lambda vs. Fargate vs. ECS comparison table, and updated SDK conventions. Restructured for answer-first readability and added HowTo schema.
    - 2025-03-11: Refreshed AWS guides links and modernized example references.
draft: false
meta_desc: Deploy AWS Lambda functions as container images with Pulumi. Compares Lambda ZIP, containers, Fargate, and ECS with 2026 limits, pricing, and runnable code.
meta_image: meta.png
authors:
    - mikhail-shilkov
tags:
    - aws
    - containers
    - serverless
---

**TL;DR** &mdash; To run a container image in AWS Lambda, build an OCI image that implements the [Lambda Runtime API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html) (most teams start from an [AWS-provided base image](https://gallery.ecr.aws/lambda/)), push it to Amazon ECR, and create a Lambda function with `packageType: "Image"` pointing at the image URI. Lambda containers support images up to 10&nbsp;GB, up to 10&nbsp;GB of memory, up to 10&nbsp;GB of `/tmp` ephemeral storage, and a 15-minute execution ceiling. Pulumi automates the build, push, and function wiring in a single program. Pick Lambda containers when your workload is event-driven and bursty but your dependencies (binaries, ML models, system libraries) outgrow the 250&nbsp;MB ZIP limit; pick [AWS Fargate or ECS](/docs/iac/guides/clouds/aws/) when you need long-running tasks, persistent connections, or multi-container pods.

<!--more-->

## How do I run a container image in AWS Lambda?

You package your function as a Linux container image, push it to [Amazon ECR](https://aws.amazon.com/ecr/), and create a Lambda function whose `packageType` is `Image`. The image must implement the Lambda Runtime API, which is an HTTP protocol Lambda uses to deliver invocation events and collect responses. The simplest path is to start `FROM` an AWS-provided base image (`public.ecr.aws/lambda/nodejs:22`, `public.ecr.aws/lambda/python:3.13`, `public.ecr.aws/lambda/java:21`, and so on) because they ship with the Runtime Interface Client preinstalled. If you want to use a different OS or runtime, add the open-source [Runtime Interface Client](https://github.com/aws/aws-lambda-runtime-interface-clients) yourself.

With Pulumi, one program covers the entire path: ECR repository, Docker build and push, IAM role, Lambda function, and event source. It works in TypeScript, Python, Go, .NET, Java, or YAML. The rest of this post walks through that program with a real video-thumbnailer example.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

const repo = new awsx.ecr.Repository("repo", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repo.url,
    context: "./app",
    platform: "linux/amd64",
});

const role = new aws.iam.Role("thumbnailerRole", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({ Service: "lambda.amazonaws.com" }),
});

new aws.iam.RolePolicyAttachment("lambdaExecute", {
    role: role.name,
    policyArn: aws.iam.ManagedPolicy.AWSLambdaExecute,
});

const thumbnailer = new aws.lambda.Function("thumbnailer", {
    packageType: "Image",
    imageUri: image.imageUri,
    role: role.arn,
    timeout: 900,
    memorySize: 2048,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws
import pulumi_awsx as awsx

repo = awsx.ecr.Repository("repo", force_delete=True)

image = awsx.ecr.Image(
    "image",
    repository_url=repo.url,
    context="./app",
    platform="linux/amd64",
)

role = aws.iam.Role(
    "thumbnailerRole",
    assume_role_policy=aws.iam.get_policy_document(statements=[{
        "actions": ["sts:AssumeRole"],
        "principals": [{"type": "Service", "identifiers": ["lambda.amazonaws.com"]}],
    }]).json,
)

aws.iam.RolePolicyAttachment(
    "lambdaExecute",
    role=role.name,
    policy_arn=aws.iam.ManagedPolicy.AWS_LAMBDA_EXECUTE,
)

thumbnailer = aws.lambda_.Function(
    "thumbnailer",
    package_type="Image",
    image_uri=image.image_uri,
    role=role.arn,
    timeout=900,
    memory_size=2048,
)
```

{{% /choosable %}}

{{< /chooser >}}

`pulumi up` builds the image from `./app`, pushes it to a fresh ECR repository, and deploys the Lambda &mdash; in one step, with one command, with no shell scripts.

## What is a Lambda container image?

A Lambda container image is an [OCI](https://opencontainers.org/) (or Docker v2) image whose entrypoint speaks the [Lambda Runtime API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html). The image is stored in Amazon ECR, and Lambda pulls it on cold start. Functionally, a container-image function behaves the same as a ZIP-package function: it is invoked by the same triggers (S3, SQS, API Gateway, EventBridge, and so on), it bills the same way (per request and per GB-second), and it is bound by the same 15-minute execution ceiling. The only meaningful difference is how the code is packaged and what limits apply to that package.

Lambda container images were announced at [re:Invent 2020](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-container-image-support/) and have been generally available ever since. They are not a separate service &mdash; they are a deployment format for the same Lambda runtime.

## What are the AWS Lambda container limits in 2026?

The hard limits below apply to every Lambda function regardless of packaging, except for the image-size column, which is specific to container images.

| Limit                       | Container image                                  | ZIP package                       |
| --------------------------- | ------------------------------------------------ | --------------------------------- |
| Maximum package size        | **10 GB** (uncompressed)                         | 250 MB (unzipped, including layers) |
| Maximum memory              | 10,240 MB                                        | 10,240 MB                         |
| Maximum ephemeral `/tmp`    | 10,240 MB                                        | 10,240 MB                         |
| Maximum execution timeout   | 15 minutes                                       | 15 minutes                        |
| Maximum payload (sync)      | 6 MB request / 6 MB response                     | 6 MB request / 6 MB response      |
| Architectures               | `x86_64`, `arm64`                                | `x86_64`, `arm64`                 |
| SnapStart support           | Not supported for container images               | Java, Python, .NET                |

Sources: [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html), [Lambda images](https://docs.aws.amazon.com/lambda/latest/dg/images-create.html), [SnapStart documentation](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html).

A note on cold starts: the public guidance from AWS is that container-image cold starts are typically comparable to ZIP cold starts when the image is well-optimized &mdash; AWS caches image layers and uses on-demand block-level loading so only the bytes touched at startup are downloaded. The biggest lever you have is image size: keep the image small, put rarely changed dependencies in lower layers, and prefer a minimal base. SnapStart, which is the most effective cold-start mitigation for Java, Python, and .NET ZIP functions, does **not** apply to container-image functions; if you need SnapStart, ship a ZIP.

## How much do Lambda container images cost?

Container-image functions are billed identically to ZIP functions:

- **Requests**: $0.20 per 1M requests (x86_64 and arm64 alike).
- **Duration**: $0.0000166667 per GB-second on x86_64, $0.0000133334 on arm64 (Graviton2) — roughly 20% lower per GB-second, with up to 34% better price-performance per AWS.
- **Free tier**: 1M requests and 400,000 GB-seconds per month, every month.
- **Storage**: ECR charges $0.10 per GB-month for image storage; data transfer to Lambda within the same Region is free.

Always confirm rates against the live [Lambda pricing](https://aws.amazon.com/lambda/pricing/) and [ECR pricing](https://aws.amazon.com/ecr/pricing/) pages, since AWS adjusts them periodically.

## How do Lambda containers compare to Fargate, ECS, and ZIP Lambdas?

The four options below all run containers, but they sit on a spectrum from "fully event-driven, scale to zero" to "long-running, always on."

| Dimension              | Lambda (ZIP)                          | Lambda (container image)              | AWS Fargate                                    | Amazon ECS (EC2)                          |
| ---------------------- | ------------------------------------- | ------------------------------------- | ---------------------------------------------- | ----------------------------------------- |
| Packaging              | ZIP up to 250 MB                      | OCI image up to 10 GB                 | OCI image (no Lambda runtime API needed)       | OCI image                                 |
| Cold start             | Milliseconds to seconds; SnapStart available | Seconds (image-size dependent); no SnapStart | Tens of seconds for new tasks            | Tens of seconds (capacity dependent)      |
| Max execution time     | 15 minutes                            | 15 minutes                            | Unbounded                                      | Unbounded                                 |
| Scale to zero          | Yes                                   | Yes                                   | No (minimum task count)                        | No (minimum container instances)          |
| Billing               | Per-ms duration + per-request         | Per-ms duration + per-request         | Per-second of vCPU and memory                  | Per-EC2-instance-hour + per-task overhead |
| Networking            | Optional VPC attachment               | Optional VPC attachment               | First-class VPC, ENIs, persistent connections  | First-class VPC, ENIs, persistent connections |
| Native event triggers | 100+ AWS services                     | 100+ AWS services                     | EventBridge / Step Functions integrations      | EventBridge / Step Functions integrations |
| Best for              | Short, bursty, event-driven workloads | Same as ZIP, but with heavy dependencies, native binaries, large ML models | Long-running services, daemons, persistent workloads | Workloads needing custom EC2 sizing or GPU |

The decision tree is short: if your workload runs for less than 15 minutes per invocation and you can fit it in 10 GB, Lambda is almost always cheaper and operationally simpler than Fargate. If you cannot fit in a 250 MB ZIP, use a Lambda container image. If your workload is long-running or needs persistent network connections, choose Fargate or ECS.

## How do I deploy a Lambda container image with Pulumi? (Step-by-step)

Let's walk through a complete program: a video thumbnailer that runs every time a `.mp4` is uploaded to an S3 bucket. The function uses [FFmpeg](https://ffmpeg.org/) &mdash; a binary that is impractical to ship in a 250 MB ZIP &mdash; to extract a thumbnail and write it back to the bucket. The full source is in [pulumi/examples](https://github.com/pulumi/examples/tree/master/aws-ts-lambda-thumbnailer).

<div class="bg-purple-100 text-sm rounded-lg py-1 px-4">

#### Quick start

1. Bootstrap a project: `pulumi new https://github.com/pulumi/examples/tree/master/aws-ts-lambda-thumbnailer`
1. Edit `./app/Dockerfile` and `./app/index.js` with your function's logic.
1. Deploy: `pulumi up`.

</div>

### 1. Define a Dockerfile

The container image is based on the AWS-provided Node.js 22 image, which preinstalls the Runtime Interface Client. It also installs the AWS CLI and FFmpeg, copies the handler, and points to `index.handler` as the entrypoint.

```dockerfile
FROM public.ecr.aws/lambda/nodejs:22

RUN dnf install -y tar xz unzip \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip && ./aws/install \
    && curl -O https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz \
    && tar -xf ffmpeg-release-amd64-static.tar.xz \
    && mv ffmpeg-*-amd64-static/ffmpeg /usr/local/bin/ \
    && rm -rf awscliv2.zip aws ffmpeg-*-amd64-static*

COPY index.js ${LAMBDA_TASK_ROOT}
CMD ["index.handler"]
```

### 2. Create an S3 bucket for inputs and outputs

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

const bucket = new aws.s3.Bucket("bucket");
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws

bucket = aws.s3.Bucket("bucket")
```

{{% /choosable %}}

{{< /chooser >}}

### 3. Build the image and push it to ECR

[Pulumi Crosswalk for AWS](/docs/iac/guides/clouds/aws/) wraps the ECR repository, the Docker build, and the push into two resources:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

const repo = new awsx.ecr.Repository("repo", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repo.url,
    context: "./app",
    platform: "linux/amd64",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_awsx as awsx

repo = awsx.ecr.Repository("repo", force_delete=True)

image = awsx.ecr.Image(
    "image",
    repository_url=repo.url,
    context="./app",
    platform="linux/amd64",
)
```

{{% /choosable %}}

{{< /chooser >}}

The `./app` directory holds the `Dockerfile` and the handler. `platform: "linux/amd64"` is explicit so the build is reproducible from Apple Silicon and Graviton developer machines. Switch to `linux/arm64` if you want the cheaper Graviton runtime.

### 4. Set up the IAM role

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const role = new aws.iam.Role("thumbnailerRole", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({ Service: "lambda.amazonaws.com" }),
});

new aws.iam.RolePolicyAttachment("lambdaExecute", {
    role: role.name,
    policyArn: aws.iam.ManagedPolicy.AWSLambdaExecute,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
role = aws.iam.Role(
    "thumbnailerRole",
    assume_role_policy=aws.iam.get_policy_document(statements=[{
        "actions": ["sts:AssumeRole"],
        "principals": [{"type": "Service", "identifiers": ["lambda.amazonaws.com"]}],
    }]).json,
)

aws.iam.RolePolicyAttachment(
    "lambdaExecute",
    role=role.name,
    policy_arn=aws.iam.ManagedPolicy.AWS_LAMBDA_EXECUTE,
)
```

{{% /choosable %}}

{{< /chooser >}}

`AWSLambdaExecute` is the AWS-managed policy that grants the read/write S3 access and CloudWatch Logs access this function needs. For a real production workload, scope this down to a custom policy that names the bucket explicitly.

### 5. Configure the Lambda function

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const thumbnailer = new aws.lambda.Function("thumbnailer", {
    packageType: "Image",
    imageUri: image.imageUri,
    role: role.arn,
    timeout: 900,
    memorySize: 2048,
    architectures: ["x86_64"],
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
thumbnailer = aws.lambda_.Function(
    "thumbnailer",
    package_type="Image",
    image_uri=image.image_uri,
    role=role.arn,
    timeout=900,
    memory_size=2048,
    architectures=["x86_64"],
)
```

{{% /choosable %}}

{{< /chooser >}}

`packageType: "Image"` is the only setting that distinguishes a container function from a ZIP function. The `imageUri` is the digest-pinned URI of the image we just pushed, so any change to the Dockerfile or handler triggers a redeploy on the next `pulumi up`.

### 6. Wire up the S3 trigger

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
new aws.s3.BucketNotification("onNewVideo", {
    bucket: bucket.id,
    lambdaFunctions: [{
        lambdaFunctionArn: thumbnailer.arn,
        events: ["s3:ObjectCreated:*"],
        filterSuffix: ".mp4",
    }],
});

new aws.lambda.Permission("allowBucket", {
    action: "lambda:InvokeFunction",
    function: thumbnailer.name,
    principal: "s3.amazonaws.com",
    sourceArn: bucket.arn,
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
aws.s3.BucketNotification(
    "onNewVideo",
    bucket=bucket.id,
    lambda_functions=[{
        "lambda_function_arn": thumbnailer.arn,
        "events": ["s3:ObjectCreated:*"],
        "filter_suffix": ".mp4",
    }],
)

aws.lambda_.Permission(
    "allowBucket",
    action="lambda:InvokeFunction",
    function=thumbnailer.name,
    principal="s3.amazonaws.com",
    source_arn=bucket.arn,
)
```

{{% /choosable %}}

{{< /chooser >}}

That is the entire program. `pulumi up` provisions everything in the right order, and a subsequent edit to the Dockerfile rebuilds and rolls out a new image automatically.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Deploy a container image to AWS Lambda with Pulumi",
  "description": "Build a Linux container image that implements the AWS Lambda Runtime API, push it to Amazon ECR, and deploy it as a Lambda function with Pulumi.",
  "totalTime": "PT15M",
  "tool": [
    {"@type": "HowToTool", "name": "Pulumi CLI"},
    {"@type": "HowToTool", "name": "AWS account"},
    {"@type": "HowToTool", "name": "Docker"},
    {"@type": "HowToTool", "name": "Node.js"}
  ],
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Define a Dockerfile",
      "text": "Create a Dockerfile that starts FROM an AWS-provided Lambda base image (such as public.ecr.aws/lambda/nodejs:22) and copies your handler into LAMBDA_TASK_ROOT.",
      "url": "https://www.pulumi.com/blog/aws-lambda-container-support/#1-define-a-dockerfile"
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Create an S3 bucket for inputs and outputs",
      "text": "Declare the S3 bucket the function will read from and write to using aws.s3.Bucket.",
      "url": "https://www.pulumi.com/blog/aws-lambda-container-support/#2-create-an-s3-bucket-for-inputs-and-outputs"
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Build and push the image to Amazon ECR",
      "text": "Use awsx.ecr.Repository and awsx.ecr.Image to provision the registry, build the Docker image from your local context, and push it.",
      "url": "https://www.pulumi.com/blog/aws-lambda-container-support/#3-build-the-image-and-push-it-to-ecr"
    },
    {
      "@type": "HowToStep",
      "position": 4,
      "name": "Create the Lambda execution role",
      "text": "Create an IAM role assumable by lambda.amazonaws.com and attach the AWSLambdaExecute managed policy (or a least-privilege custom policy).",
      "url": "https://www.pulumi.com/blog/aws-lambda-container-support/#4-set-up-the-iam-role"
    },
    {
      "@type": "HowToStep",
      "position": 5,
      "name": "Create the Lambda function",
      "text": "Create an aws.lambda.Function with packageType set to Image and imageUri pointing at the digest from awsx.ecr.Image.",
      "url": "https://www.pulumi.com/blog/aws-lambda-container-support/#5-configure-the-lambda-function"
    },
    {
      "@type": "HowToStep",
      "position": 6,
      "name": "Wire up the S3 trigger",
      "text": "Use aws.s3.BucketNotification and aws.lambda.Permission to invoke the function on new .mp4 uploads.",
      "url": "https://www.pulumi.com/blog/aws-lambda-container-support/#6-wire-up-the-s3-trigger"
    }
  ],
  "supply": [
    {"@type": "HowToSupply", "name": "AWS account with permissions to create ECR, IAM, Lambda, and S3 resources"}
  ]
}
</script>

## When should I choose Lambda containers over ZIP packages?

Reach for a container image when one or more of the following is true:

- **Your dependencies exceed 250 MB unzipped.** Native binaries (FFmpeg, ImageMagick, headless Chromium), large ML model weights, and full Python data-science stacks all blow past the ZIP limit quickly.
- **You need a custom OS, runtime, or system library.** Lambda's managed runtimes are good but opinionated. A container lets you pin a specific glibc version, install OS packages, or run a language Lambda doesn't natively support.
- **Your team's CI/CD already builds containers.** Reusing your existing image-build pipeline (and its scanning, signing, and SBOM tooling) is often easier than maintaining a parallel ZIP-packaging pipeline.
- **You want a single artifact format across Lambda, Fargate, and ECS.** A container image that runs in Lambda for short bursts can also run in Fargate for long jobs &mdash; convenient for hybrid workloads.

Stick with ZIP when your code is small, you want SnapStart, or you want the fastest possible cold starts.

{{< related-posts >}}

## Conclusion

AWS Lambda's container-image support brings the industry-standard packaging format to event-driven serverless functions, and Pulumi makes the full deploy &mdash; ECR repository, image build, IAM role, function, and event source &mdash; one program in the language you already use. If you have outgrown the ZIP package, this is the pattern you want.

Watch a demo of the thumbnailer below.

{{< youtube "gB9T1aW3gSk" >}}

Next steps:

- Browse the full [Lambda + container image example](https://github.com/pulumi/examples/tree/master/aws-ts-lambda-thumbnailer) in pulumi/examples.
- Read the [Pulumi AWS Lambda guide](/docs/iac/guides/clouds/aws/lambda/) for event sources, IAM patterns, and packaging tips.
- See [AWS Lambda SnapStart with Pulumi](/blog/aws-lambda-snapstart/) if you need faster cold starts on a ZIP-packaged Java, Python, or .NET function.
- Cut x86 costs with [Lambda functions powered by Graviton2](/blog/aws-lambda-functions-powered-by-graviton2/).
- [Get started](/docs/iac/get-started/aws/) with Pulumi for AWS today.
