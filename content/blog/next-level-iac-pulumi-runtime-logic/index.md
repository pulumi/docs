---
title: "Next-level IaC: Drop those wrapper scripts and let your language do that for you"
allow_long_title: true
date: 2024-04-30
meta_desc: Learn how to use your language of choice to do more than just declare cloud resources.
meta_image: meta.png
authors:
    - christian-nunciato
tags:
    - next-level-iac
    - nodejs
    - python
    - cloudformation
    - terraform
    - hcl
---

Our users are always telling us (particularly the ones who come to Pulumi from other IaC tools) that being able to use general-purpose languages to manage their infrastructure was a game changer for them.

I know it was for me. As a JavaScript developer, when I discovered Pulumi and saw that I could do pretty much everything I was doing with Terraform _but with TypeScript_, I was immediately hooked; that's all it took. Just being able to write my resource declarations in a language I knew well (and that my IDE understood) was huge.

But it's easy to forget, even when you've been using Pulumi for a while, that you aren't just getting the language alone --- you're getting the full capability of the language's runtime environment also. Not just JavaScript, but all of Node.js. Not just C#, but everything the .NET framework, runtime, and ecosystem have to offer.

This is quite a big deal, actually. Whereas with other tools, you're often bound by the limits of the tool's DSL, with Pulumi, you have no such constraints; you can do just about anything your chosen language can do. That means much more than just declaring long lists of cloud resources --- it means unlocking all kinds of capabilities that can help bring your infrastructure-management practice to a whole new level.

In this post, the first of a new series we're calling Next-level IaC, we'll show you a few small but useful ways you can take advantage of this reality --- first, by spotting some opportunities to simplify your deployments.

## Run pre-deployment tasks with Pulumi

Fundamentally, a Pulumi program is just a regular program. That means you can take actions programmatically at runtime --- before the Pulumi engine gets going.

Suppose you were tasked with writing the code to deploy and manage a static website. Conceptually, you might break this process up into a few separate steps:

1. Build the website
1. Deploy the supporting infrastructure (e.g, the cloud storage, maybe a content-delivery network)
1. Copy the content of the website into the infrastructure

This you might lead you to reach for Bash to write up a shell script like the one below, which uses [Hugo](https://gohugo.io/) (a popular static-site generator) to build the website, Pulumi to provision the infrastructure, and the AWS CLI to push the built website up into the AWS cloud:

```bash
#!/bin/bash

# Build the website.
hugo --destination ./public

# Provision the infrastructure.
pulumi up --yes

# Copy the website content into the infrastructure.
aws s3 sync ./public s3://$(pulumi stack output bucketName)
```

And this would definitely work. But it's also unnecessary. You can avoid both the Bash wrapper and the dependency on the AWS CLI by using your chosen language's built-in support for spawning shell processes:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as childProcess from "child_process";

// Build the website.
const result = childProcess.execSync("hugo --destination ./public", { stdio: "pipe", cwd: "./www" });

// Provision a storage bucket for the website.
const bucket = new aws.s3.Bucket("bucket", {
    website: {
        indexDocument: "index.html",
    },
});

// Copy the website home page into the bucket.
const homepage = new aws.s3.BucketObject(
    "index.html",
    {
        bucket: bucket.id,
        content: fs.readFileSync("./www/public/index.html", "utf-8"),
        contentType: "text/html",
        acl: "public-read",
    },
);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws
import subprocess

# Build the website.
result = subprocess.run(
    ["hugo", "--destination", "./public"],
    stdout=subprocess.PIPE,
    cwd="./www",
    check=True,
    shell=True,
)

# Provision a storage bucket for the website.
bucket = aws.s3.Bucket(
    "bucket", website=aws.s3.BucketWebsiteArgs(index_document="index.html")
)

# Copy the website home page into the bucket
homepage = aws.s3.BucketObject(
    "index.html",
    bucket=bucket.id,
    content=open("./www/public/index.html", "r").read(),
    content_type="text/html",
    acl="public-read",
)
```

{{% /choosable %}}

Running processes like these synchronously, as above, means they'll complete before Pulumi starts [registering resources](https://www.pulumi.com/docs/concepts/how-pulumi-works) --- important here because the `BucketObject` resource needs that `public` folder to exist for the deployment to succeed. Fortunately it does, so all is well:

```
$ pulumi up

Updating (dev)

     Type                               Name          Plan       Info
 +   pulumi:pulumi:Stack                example-dev   create     15 messages
 +   ├─ aws:s3:Bucket                   bucket        create
 +   └─ aws:s3:BucketObject             index.html    create

Diagnostics:
  pulumi:pulumi:Stack (example-dev):
    Start building sites ...

                       | EN
    -------------------+-----
      Pages            |  4
      Paginator pages  |  0
      Non-page files   |  0
      Static files     |  0
      Processed images |  0
      Aliases          |  0
      Sitemaps         |  1
      Cleaned          |  0
    Total in 11 ms

Resources:
    + 3 created
```

Also notice how the example captures the output of the process in `result` and writes it to the terminal. Standard logging like this tends not to be possible with static languages (at least not without some hackery) because there's no real way to do it programmatically. Similarly, those that do support spawning processes tend to require them to return strictly formatted JSON strings --- which, as the example shows, not all processes do. (Forcing you to have to wrap them with yet more shell scripts.)

Simple stuff, but flexible and powerful. With one line, you've kept your deployment process simple, dropping two tools you don't need thanks to the built-in capabilities of Pulumi and your language of choice.

## Fetch data to generate resources dynamically

To build on the static-website scenario, suppose you wanted to retrieve some data from an external source and use it to provision some cloud resources dynamically. For example, you might want to let your marketing team create short URLs on their own for social media posts. For this, you might once again turn to Bash and the AWS CLI to pull those URLs from your corporate CMS (e.g., with `curl`), either before or after running `pulumi`, and create the corresponding redirects imperatively using a follow-up shell command of some sort.

Again, a totally reasonable approach. But again, why bother, when you have the full capability of {{< langhost >}} at fingertips? Just add a few lines to your program to fetch the data and be on your way:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
// ...

// Fetch some redirects from a hypothetical CMS.
const redirects = fetch(`${process.env.CMS_ENDPOINT}/redirects.json`)
    .then(response => response.json())
    .then(items =>
        items.forEach((redirect: any, i: number) => {
            // Create an S3 website redirect for each one.
            new aws.s3.BucketObject(
                `redirect-${i}`,
                {
                    bucket: bucket.id,
                    key: redirect.from,
                    websiteRedirect: redirect.to,
                    acl: "public-read",
                },
                { dependsOn: [ownershipControls, publicAccess] },
            );
        }),
    );
```

{{% /choosable %}}

{{% choosable language python %}}

```python
#...
import json
import os
import requests

# ...

# Fetch some redirects from a hypothetical CMS.
response = requests.get(f"{os.environ['CMS_ENDPOINT']}/redirects.json")
redirects = json.loads(response.text)

# Create an S3 website redirect for each one.
for i, redirect in enumerate(redirects):
    aws.s3.BucketObject(
        f"redirect-{i}",
        bucket=bucket.id,
        key=redirect["from"],
        website_redirect=redirect["to"],
        acl="public-read",
    )
```

{{% /choosable %}}

Notice the example parses the response using the language's built-in JSON support. If your CMS happened to return data in some other format, or required some additional credentials for authorization, no problem --- your language and its package ecosystem are going to be there to help you.

Also notice the example reads the source URL directly from the environment. This is typically more cumbersome (if even possible) with other tools, requiring you to name your environment variables in tool-specific ways and then tack on additional blocks of configuration before you're able to use them. As you can see, {{< langhost >}} makes this much more convenient.

Finally, notice the redirects are translated into cloud resources using a familiar {{< langname >}} looping construct. We'll cover this topic in much more depth in an upcoming post. (Stay tuned!)

## Hook the event loop to run tasks after deployment

Finally, you can do nifty things like run tasks programmatically _after_ a Pulumi deployment completes --- once again, without ever having to leave the Pulumi program.

If your hypothetical website were sitting behind a CloudFront CDN, for example, you might want some way to clear the CDN's cache after a deployment. This generally requires some imperative action, like using the AWS CLI to run `aws cloudfront create-invalidation` sometime later. How might you do something like this with Pulumi, given Pulumi programs exit automatically when their operations complete?

One way --- again, since a Pulumi program is just a regular {{< langhost >}} program --- would be to write a {{< langname >}} function to create an invalidation request, and then ask the {{< langhost >}} runtime to run that function before exiting.

The mechanics of this vary slightly by language, but it works, and it's a very handy way to keep all of your deployment logic in one place --- again avoiding the need to relegate anything to a Bash script:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
// ...
import * as cloudfront from "@aws-sdk/client-cloudfront";

const config = new pulumi.Config("aws");
const region = config.require("region");

// Create a CloudFront distribution for the website.
const cdn = new aws.cloudfront.Distribution("cdn", {
    enabled: true,
    defaultRootObject: "index.html",
    origins: [{
        originId: bucket.arn,
        domainName: bucket.websiteEndpoint,
        // ...
    }],
    // ...
});

function createInvalidation(id: string) {
    // Only invalidate after a deployment.
    if (pulumi.runtime.isDryRun()) {
        console.log("This is a Pulumi preview, so skipping cache invalidation.");
        return;
    }

    process.on("beforeExit", () => {
        const client = new cloudfront.CloudFrontClient({ region });
        const command = new cloudfront.CreateInvalidationCommand({
            DistributionId: id,
            InvalidationBatch: {
                CallerReference: `invalidation-${Date.now()}`,
                Paths: {
                    Quantity: 1,
                    Items: ["/*"],
                },
            },
        });

        client
            .send(command)
            .then(result => {
                console.log(`Invalidation status for ${id}: ${result.Invalidation?.Status}.`);
                process.exit(0);
            })
            .catch(error => {
                console.error(error);
                process.exit(1);
            });
    });
}

// Register a function to be invoked before the program exits.
cdn.id.apply(id => createInvalidation(id));
```

The relevant code is the call to [`process.on("beforeExit")`](https://nodejs.org/api/process.html#event-beforeexit), which registers a function to be invoked just before the program exits using the resolved ID of the distribution. (For more on how the `apply()` method works, see [Inputs and Outputs](https://www.pulumi.com/docs/concepts/inputs-outputs/).) The function returns early for Pulumi previews --- no sense clearing the cache if the site hasn't changed --- and uses the [AWS SDK for JavaScript](https://aws.amazon.com/sdk-for-javascript/) to submit the invalidation request to CloudFront, naming it uniquely with a timestamp and logging the result to the console:

{{% /choosable %}}

{{% choosable language python %}}

```python
# ...
import boto3
import asyncio

def create_invalidation(id):
    # Don't bother invalidating unless it's an actual deployment.
    if pulumi.runtime.is_dry_run():
        print("This is a Pulumi preview, so skipping cache invalidation.")
        return

    client = boto3.client("cloudfront")
    result = client.create_invalidation(
        DistributionId=id,
        InvalidationBatch={
            "CallerReference": f"invalidation-{time.time()}",
            "Paths": {
                "Quantity": 1,
                "Items": ["/*"],
            },
        },
    )

    print(
        f"Cache invalidation for distribution {id}: {result['Invalidation']['Status']}."
    )


# Register a function to be invoked before the program exits.
cdn.id.apply(lambda id: atexit.register(lambda: create_invalidation(id)))
```

The relevant code is the call to [`atexit.register()`](https://docs.python.org/3/library/atexit.html), which registers a function to be invoked just before the program exits using the resolved ID of the distribution. (For more on how the `apply()` method works, see [Inputs and Outputs](https://www.pulumi.com/docs/concepts/inputs-outputs/).) The function returns early for Pulumi previews --- no sense clearing the cache if the site hasn't changed --- and uses [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to submit the invalidation request to CloudFront, naming it uniquely with a timestamp and logging the result to the console:

{{% /choosable %}}

```
$ pulumi preview

Previewing update (dev)
     Type                 Name           Info
     pulumi:pulumi:Stack  example-dev    16 messages

Diagnostics:
  pulumi:pulumi:Stack (example-dev):
    ...
    This is a Pulumi preview, so skipping cache invalidation.
```

```
$ pulumi up

Updating (dev)

     Type                 Name                        Status     Info
     pulumi:pulumi:Stack  example-dev             16 messages

Diagnostics:
  pulumi:pulumi:Stack (example-dev):
    ...
    Cache invalidation of distribution EAJOVC1QNGT13: InProgress.
```

Techniques like these are a great way to eliminate unnecessary scripts, glue code, and other dependencies while keeping your deployment logic clear, well contained, and amenable to change.

## Wrapping up

Hopefully this first post has given you a few new ways to think about how to do more with Pulumi and your language of choice. Over the next few weeks, as this series unfolds, we'll share a lot more, so keep an eye on this space --- and of course, if you haven't already, [consider giving Pulumi a try](/start).

You'll find the full source for the examples above on GitHub:

* [TypeScript version](https://github.com/pulumi/pulumi-hugo/tree/master/themes/default/static/programs/aws-static-website-with-runtime-logic-typescript)
* [Python version](https://github.com/pulumi/pulumi-hugo/tree/master/themes/default/static/programs/aws-static-website-with-runtime-logic-python)

Happy coding!
