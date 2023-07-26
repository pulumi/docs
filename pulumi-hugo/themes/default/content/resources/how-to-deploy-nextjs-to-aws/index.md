---
title: "How to deploy Next.js to AWS"
allow_long_title: true
meta_desc: "Use Pulumi to deploy Next.js apps to AWS with our guide. Ideal for developers managing Next.js setups and routine deployments on AWS"
type: ai-answers
date: 2023-07-24
---

I will show you how to declare the AWS resources in Pulumi to deploy a Node.js application, which includes Next.js applications as well.

We'll use the Amazon S3 to store our static content, AWS Lambda for server-side rendering, CloudFront for content delivery, and Route53 for DNS.

First, you'll need to export your Next.js app to a static HTML application by running next build and next export. This should generate a directory named out which you will need to deploy to your newly created S3 bucket.

Here is the Pulumi code to accomplish it:

```typescript

import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";
import * as s3 from "@pulumi/aws/s3";

// Create a bucket and expose a bucket object website
let siteBucket = new s3.Bucket("s3-website-bucket", {
    website: {
        indexDocument: "index.html",
    },
});

let siteDir = "out";  // Compiled Next.js site

// Deploy site assets
let bucketObject = new s3.BucketObject("nextjs-bucket", {
    bucket: siteBucket,                       // The S3 bucket object
    source: new pulumi.asset.FileArchive(siteDir),  // Project static site directory
    key: "index.html"                         // S3 object store name
})

// Wire up the static website bucket with a CDN
let cdn = new aws.cloudfront.Distribution("cdn", {
    origins: [
        {
            originPath: '/',
            domainName: bucketObject.bucket.bucketRegionHostname, // CloudFront origins refer to S3 buckets that stores our website assets.
            s3OriginConfig: {
                originAccessIdentity: cdnOriginPath
            },
        },
    ],
    //...additional configuration
});

// Export the website URL
export const websiteUrl = pulumi.interpolate`http://${siteBucket.websiteEndpoint. hostname}`;

// Export the Cloudfront URL
export const cdUrl = cdn.domainName.apply(n => `https://${n}`)

```

Please note that this is for a statically exported Next.js app. If you want to use server-side rendering (SSR), you would need to deploy Next.js app as a lambda function, which makes the setup a lot more complex.

* [aws.s3.Bucket](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucket/)
* [aws.s3.BucketObject](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucketobject/)
* [aws.cloudfront.Distribution](https://www.pulumi.com/registry/packages/aws/api-docs/cloudfront/distribution/)