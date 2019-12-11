---
title: "Serving a Static Website on AWS with Pulumi"
authors: ["chris-smith"]
tags: ["AWS","Infrastructure","TypeScript"]
date: "2018-07-17"
meta_desc: "With around 200 lines of code, learn how Pulumi integrates four different AWS products (Amazon S3, CloudFront, Route53, and Certificate Manager) to host a static website served over HTTPS and from a worldwide CDN."

---

Hello! This post covers using [Pulumi](/) to create the
infrastructure for serving a static website on AWS. The full source code
for this example is [available on GitHub](https://github.com/pulumi/examples/blob/master/aws-ts-static-website/index.ts).

Setting up the infrastructure to serve a static website doesn't sound
like it would be all that difficult, but when you consider HTTPS
certificates, content distribution networks, and attaching it to a
custom domain, integrating all the components can be quite daunting.

Fortunately this is a task where Pulumi really shines. Pulumi's
code-centric approach not only makes configuring cloud resources easier
to do and maintain, but it also eliminates the pain of integrating
multiple products together.

This isn't a hypothetical benefit of using the Pulumi programming model.
We use a setup similar to the one described in this post for powering
our own static websites, like [www.pulumi.com](http://www.pulumi.com/)
and [get.pulumi.com](http://get.pulumi.com).
<!--more-->

## Overview

The architecture we will use for the website is to follow AWS "[Web Application Hosting](https://aws.amazon.com/architecture/)"
reference architecture ([pdf](https://media.amazonwebservices.com/architecturecenter/AWS_ac_ra_web_01.pdf)).
This integrates several AWS products:

- [Amazon S3](https://aws.amazon.com/s3/), used to store the
  website's contents
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/), a CDN
  improving site performance
- [Amazon Route53](https://aws.amazon.com/route53/), for managing DNS
- [Amazon Certificate Manager](https://aws.amazon.com/certificate-manager/), for serving
  content over HTTPS

## How it Works

If you are already familiar with static hosting on AWS, feel free to go
directly to our [examples repository](https://github.com/pulumi/examples) on GitHub, in the
aws-ts-static-website folder.

If you are new to AWS, we'll break down how to configure each component
using Pulumi.

## Uploading static content to S3

Amazon S3 is a service for storing and retrieving files. This is where
we will store the website's contents, and it is done by just creating an
S3 bucket resources and then crawling the www-directory when the Pulumi
program executes and creating an S3 bucket object resource for each
file.

The main thing to point out here is that we set the contentType property
for each bucket object. This way, the right HTTP headers are returned so
that files are interpreted the right way. (e.g. images are rendered as
images.) The process for inferring the MIME type based on file extension
is done by the [mime NPM package](https://www.npmjs.com/package/mime).
No need to write the code on your own, rather we can just reuse an
existing library - written in a different programming language, no less! - from our TypeScript application.

    const contentBucket = new aws.s3.Bucket("contentBucket",
        {
            ...
        });

    ...


    const webContentsRootPath = path.join(process.cwd(), config.pathToWebsiteContents);
    crawlDirectory(
        webContentsRootPath,
        (filePath: string) => {
            const relativeFilePath = filePath.replace(webContentsRootPath + "/", "");
            const contentFile = new aws.s3.BucketObject(
                relativeFilePath,
                {
                    key: relativeFilePath,

                    acl: "public-read",
                    bucket: contentBucket,
                    contentType: mime.getType(filePath) || undefined,
                    source: new pulumi.asset.FileAsset(filePath),
                },
                {
                    parent: contentBucket,
                });
        });

With the S3 bucket populated with the website's contents, we need to be
able to serve it.

S3 supports the ability to serve a website directly, but S3 when used
alone doesn't support serving the content over HTTPS. Also, by serving
the content via a content distribution network, like Amazon CloudFront,
content can be served much faster by caching resources across the world.
Rather than requiring every web request to go directly to the source S3
bucket.

## Setting up a CloudFront CDN backed by S3

There are a lot of details to configuring a CloudFront distribution,
from caching policies to rendering custom error pages. While some of
these details cannot be avoided, Pulumi programs being just code, allows
for using using constants like tenMinutes rather than the number 600.

    const distributionArgs: aws.cloudfront.DistributionArgs = {
        enabled: true,
        aliases: [ config.targetDomain ],

        ...

        // A CloudFront distribution can configure different cache behaviors based on the request path.
        // Here we just specify a single, default cache behavior which is just read-only requests to S3.
        defaultCacheBehavior: {
            targetOriginId: contentBucket.arn,

            viewerProtocolPolicy: "redirect-to-https",
            allowedMethods: ["GET", "HEAD", "OPTIONS"],
            cachedMethods: ["GET", "HEAD", "OPTIONS"],

            forwardedValues: {
                cookies: { forward: "none" },
                queryString: false,
            },

            minTtl: 0,
            defaultTtl: tenMinutes,
            maxTtl: tenMinutes,
        },

        ...
    };

## Attaching it to a domain via Route53

Finally, we hook up our domain to the CloudFront distribution. We just
create an alias (A) record that aliases our own domain (e.g.
[www.pulumi.com](http://www.pulumi.com/)) to the CloudFront distribution
(e.g. `dhy4niicdm7ba.cloudfront.net`).

There is a little extra processing we need to do to get the Amazon
Route53 Hosted Zone ID for the domain. But we can do that directly in
the Pulumi program, and taking advantage of TypeScript's async/await
support.

    // Creates a new Route53 DNS record pointing the domain to the CloudFront distribution.
    async function createAliasRecord(
            targetDomain: string, distribution: aws.cloudfront.Distribution): Promise {
        const domainParts = getDomainAndSubdomain(targetDomain);
        const hostedZone = await aws.route53.getZone({ name: domainParts.parentDomain });
        return new aws.route53.Record(
            targetDomain,
            {
                name: domainParts.subdomain,
                zoneId: hostedZone.zoneId,
                type: "A",
                aliases: [
                    {
                        name: distribution.domainName,
                        zoneId: distribution.hostedZoneId,
                        evaluateTargetHealth: true,
                    },
                ],
            });
    }

    const aRecord = createAliasRecord(config.targetDomain, cdn);

When the Pulumi program is run, the DNS record is created and after a
few minutes to allow for worldwide propagation, the website is live. No
need to manually log into the AWS console, enter various DNS records,
etc. You can create and populate the S3 bucket, setup the CloudFront
CDN, and attach it to Route53 all within the same Pulumi program.

## Wrapping Up

With around [200 lines of code](https://github.com/pulumi/examples/blob/master/aws-ts-static-website/index.ts)
we were able to integrate four different AWS products using Pulumi to
host a static website, served over HTTPS and from a world-wide CDN. Of
course there are other ways to host static websites too, and some
products or services can do all of that without needing any code at all.

But the benefit of using Pulumi for this is that you are in control of
your infrastructure. If later you need to add more functionality, e.g.
require authentication or serving some routes dynamically, you can just
write a little more code to configure CloudFront. If you wanted to setup
a testing or staging environment on a different domain, that would just
be a matter of running the same Pulumi program in a different stack.

Pulumi opens up a lot of possibilities and we are excited to see what
sorts of things people build using it. If you are interested in using
Pulumi for more sophisticated website hosting, or just have questions
about serving static files like described here, feel free to ask away on
our [Pulumi Community Slack](http://slack.pulumi.com/).
