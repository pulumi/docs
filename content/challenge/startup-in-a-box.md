---
title: "Startup in a Box"
layout: challenge/single
description: |
    Build and deploy your very own startup landing site to the cloud, complete with everything you need to get started!
meta_desc: |
    Build and deploy your very own startup landing site to the cloud, complete with everything you need to get started!
meta_image: /images/challenge/challenge_cta.png
---

<h1 class="font-display text-6xl">Startup in a Box!</h1>

Thinking about turning that side project into a little something more? Follow along to stand up a website for your startup on an object store and a CDN from your favorite cloud provider (Google Cloud or AWS) and Checkly, all using Pulumi.

## Prerequisites

In order to complete this challenge, you'll need a couple things set up in advance.

{{< chooser cloud "aws,gcp" >}}

{{% choosable cloud aws %}}

* A [Pulumi account](https://app.pulumi.com/signup)
* The [Pulumi CLI](/docs/install/)
* An AWS account
* A [Checkly account](https://www.checklyhq.com/)

{{% /choosable %}}

{{% choosable cloud gcp %}}

* A [Pulumi account](https://app.pulumi.com/signup)
* The [Pulumi CLI](/docs/install/)
* A Google Cloud [account](https://cloud.google.com/gcp) and [project](https://cloud.google.com/resource-manager/docs/creating-managing-projects/)
* A [Checkly account](https://www.checklyhq.com/)

{{< notes >}}
If you're new to Google Cloud, you can get $300 in free credits to run, test, and deploy workloads. <a href="https://cloud.google.com/gcp" target="_blank" rel="noopener noreferrer">Open a free Google Cloud account</a> and use it for this Pulumi Challenge!
{{< /notes >}}

{{% /choosable %}}

{{< /chooser >}}

## Challenge

Follow along with the steps outlined on this page.

### Step 1. Your First Pulumi Program

You will learn how to create a new Pulumi program using Pulumi templates, specifically for AWS or Google Cloud with TypeScript. Create a new directory called `pulumi-challenge` and run the following inside of it:

{{% chooser cloud "aws,gcp" %}}

{{% choosable cloud aws %}}

```shell
pulumi new aws-typescript
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

```shell
# create a new Pulumi project
pulumi new gcp-typescript
```

The `pulumi new gcp-typescript` command will prompt for the name of the Google Cloud project to use, but if you didn't enter one or need to change it, you can do so with the `pulumi config set` command. Setting the Google Cloud region is handled in the same way.

```shell
# set the project ID
pulumi config set gcp:project <Google Cloud_PROJECT_ID>

# optionally set the region as appropriate for your location
pulumi config set gcp:region europe-west1
```

{{% /choosable %}}

### Step 2. Creating Your First Resource

{{% choosable cloud aws %}}

Now that you have a base AWS project configured, you need to create your first resource. In this case, you'll create a new S3 bucket which will allow you to store your static website. You'll also want to ensure that this bucket is private, as you want to expose it only via your CDN (you'll configure that next).

```typescript
const bucket = new aws.s3.BucketV2(
  "bucketV2",
  {
    tags: {
      Name: "My bucket",
    },
  }
);

const bucketAcl = new aws.s3.BucketAclV2("bAcl", {
  bucket: bucket.id,
  acl: aws.s3.PublicReadAcl,
});
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

Now that you have a base Google Cloud project configured, you need to create your first resource. In this instance, you'll create a new [GCS bucket](https://cloud.google.com/storage/docs/buckets) which will allow you to store your static website. The command `pulumi new gcp-typescript` produced a file `pulumi-challenge/index.ts`. Clear the contents of the `index.ts` file and add the following code to create your first resources.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Create a Google Cloud resource (Storage Bucket)
const bucket = new gcp.storage.Bucket("mybucket", {
    // Set location as appropriate for wherever you are located
    location: "EU",
     website: {
        mainPageSuffix: "index.html",
    },
});

// Create an IAM binding to allow public read access to the bucket
const bucketIamBinding = new gcp.storage.BucketIAMBinding("bucket-iam-binding", {
    bucket: bucket.name,
    role: "roles/storage.objectViewer",
    members: ["allUsers"],
});
```

{{% /choosable %}}

{{% /chooser %}}

### Step 3. Working with Local Files

Pulumi lets you use your favourite programming language to define your infrastructure. Today, you're using TypeScript, which means you have access to the Node API. This includes discovering directories and files.

Using these APIs, you can sync your local files, with the Pulumi resource model, to the object storage platform.

You need to add the `mime` package from npm, as it is useful for passing the MIME type of the file to the object storage platform without hardcoding it.

```shell
npm install mime @types/mime
```

{{% chooser cloud "aws,gcp" %}}

{{% choosable cloud aws %}}

```typescript
import * as fs from "fs";
import * as mime from "mime";

const staticWebsiteDirectory = "website";

fs.readdirSync(staticWebsiteDirectory).forEach((file) => {
  const filePath = `${staticWebsiteDirectory}/${file}`;
  const fileContent = fs.readFileSync(filePath).toString();

  new aws.s3.BucketObject(file, {
    bucket: bucket.id,
    source: new pulumi.asset.FileAsset(filePath),
    contentType: mime.getType(filePath) || undefined,
    acl: aws.s3.PublicReadAcl,
  });
});
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

```typescript
import * as fs from "fs";
import * as mime from "mime";

const staticWebsiteDirectory = "website";

fs.readdirSync(staticWebsiteDirectory).forEach((file) => {
    const filePath = `${staticWebsiteDirectory}/${file}`;

    new gcp.storage.BucketObject(file, {
        name: file,
        bucket: bucket.id,
        source: new pulumi.asset.FileAsset(filePath),
        contentType: mime.getType(filePath) || undefined,
    });
});
```

{{% /choosable %}}

{{% /chooser %}}

You need your actual website too, though. Create a directory called `website` at `pulumi-challenge/website`, and inside it, add `index.html`, `style.css`, and `normalize.css`.

For `index.html`, you'll have the structure of a simple website, with places to put links to your project's GitHub and Twitter, as well as your LinkedIn:

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Pulumi Challenge</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="normalize.css">
</head>
<body>
  <header>
    <!-- The logo here is pulled from FontAwesome. Replace it with your own if you like! -->
    <div class="logo">
      <ul>
      <li><i class="fas fa-feather"></i></li>
      <li><p>Company Name</p></li>
      </ul>
    </div>
    <ul class="social">
      <!-- Add your GitHub and social links here! -->
                <li><a href="http://github.com/" target="_blank"><i class="fab fa-github-alt"></i></a></li>
                <li><a href="http://twitter.com/" target="_blank"><i class="fab fa-twitter"></i></a></li>
                <li><a href="http://linkedin.com/" target="_blank"><i class="fab fa-linkedin-in"></i></a></li>
            </ul>
  </header>
<div class="banner">
  <!-- Fill in the blanks for your startup's pitch! -->
    <h1>Your Startup Name Here</h1>
    <h3>Your Tagline</h3>
    <p>We're $CompanyName, and we're changing what it means to $Task. Our innovative use of $Technology makes life easier for $JobTitles, so they can focus on what they're really good at instead of wasting time and effort on $MenialOrDifficultTask. Streamline your $TaskProcess with $Product and take to the skies!</p>
</div>
</body>
<script src="https://kit.fontawesome.com/b4747495ea.js" crossorigin="anonymous"></script>
</html>
```

In `style.css`, you'll make it pretty with some bright colors and a CSS background:

```css
@import url('https://fonts.googleapis.com/css?family=News+Cycle|Teko&display=swap');

body {
    background-color: #f7f7fa;
    opacity: 0.8;
    background-image: radial-gradient(#f79645 0.5px, #f7f7fa 0.5px);
    background-size: 10px 10px;
}

ul {
    list-style-type: none;
}

ul li {
    display: inline-block;
}

a {
    color: white;
    -webkit-transition: color .5s ease-out;
    transition: color .5s ease-out;
    text-decoration: none;
}

a:hover, a:active {
    color: rgb(55, 188, 250);
}

header {
    background-color: rgba(214, 73, 73, .6);
    height: 80px;
    position: absolute;
    top: 0;
    width: 100%;
    box-shadow: 0px 2px 7px -1px rgba(0,0,0,0.75);
    -webkit-box-shadow: 0px 2px 7px -1px rgba(0,0,0,0.75);
    -moz-box-shadow: 0px 2px 7px -1px rgba(0,0,0,0.75);
}

header li {
    color: white;
}

.active a {
    color: rgb(255, 157, 112);
}

.social {
    position: absolute;
    right: 50px;
    top: -5px;
    font-size: 30px;
}

.social li {
    margin: 0 5px 0 5px;
}

.logo {
    font-family: Teko;
    position: absolute;
    left: 5px;
    top: -60px;
    font-size: 40px;
}

.banner {
    width: 60vw;
    font-family: Teko;
    font-size: 2vw;
    text-align: center;
    margin-top: 15vw;
    margin-left: 20vw;
}

.banner h1 {
    color: rgb(214, 73, 73);
}

.banner p, .about p {
    font-family: News Cycle;
}
```

To make sure styles display consistently across browsers, you also need to normalize some styles. [Copy normalize.css from GitHub](https://github.com/necolas/normalize.css/blob/master/normalize.css).

### Step 4. Creating a CDN

Next, you want to add a CDN to your website.

{{% chooser cloud "aws,gcp" %}}

{{% choosable cloud aws %}}

On AWS, this means you want to front your S3 bucket with Cloudfront. This is a pretty big object, but most of it can be copy and pasted without further thought.

```typescript
const s3OriginId = "myS3Origin";

const cloudfrontDistribution = new aws.cloudfront.Distribution(
  "s3Distribution",
  {
    origins: [
      {
        domainName: bucket.bucketRegionalDomainName,
        originId: s3OriginId,
      },
    ],
    enabled: true,
    isIpv6Enabled: true,
    comment: "Some comment",
    defaultRootObject: "index.html",
    defaultCacheBehavior: {
      allowedMethods: [
        "DELETE",
        "GET",
        "HEAD",
        "OPTIONS",
        "PATCH",
        "POST",
        "PUT",
      ],
      cachedMethods: ["GET", "HEAD"],
      targetOriginId: s3OriginId,
      forwardedValues: {
        queryString: false,
        cookies: {
          forward: "none",
        },
      },
      viewerProtocolPolicy: "allow-all",
      minTtl: 0,
      defaultTtl: 3600,
      maxTtl: 86400,
    },
    priceClass: "PriceClass_200",
    restrictions: {
      geoRestriction: {
        restrictionType: "whitelist",
        locations: ["US", "CA", "GB", "DE"],
      },
    },
    viewerCertificate: {
      cloudfrontDefaultCertificate: true,
    },
  }
);
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

On Google Cloud, that means you want to front your Cloud Storage Bucket with a [Load Balancer](https://cloud.google.com/load-balancing/docs/https) and enable its [CDN capabilities](https://cloud.google.com/cdn/docs/overview). Add the following additional code to your `index.ts` file in order to create a Google Cloud Load Balancer, Public IP address and URL Map to your Google Cloud storage bucket.

```typescript
// Google Cloud Load Balancer Backend
const backendBucket = new gcp.compute.BackendBucket("backend-bucket", {
    bucketName: bucket.name,
    enableCdn: true,
});

// Provision a global IP address for the CDN
const ip = new gcp.compute.GlobalAddress("ip");

// Create a URLMap to route requests to the storage bucket
const urlMap = new gcp.compute.URLMap("url-map", {defaultService: backendBucket.selfLink});

// Create an HTTP proxy to route requests to the URLMap
const httpProxy = new gcp.compute.TargetHttpProxy("http-proxy", {urlMap: urlMap.selfLink});

// Create a GlobalForwardingRule rule to route requests to the HTTP proxy
const httpForwardingRule = new gcp.compute.GlobalForwardingRule("http-forwarding-rule", {
    ipAddress: ip.address,
    ipProtocol: "TCP",
    portRange: "80",
    target: httpProxy.selfLink,
});
```

{{% /choosable %}}

{{% /chooser %}}

### Step 5. Introducing ComponentResources

Now... you _could_ continue to add resource after resource, but Pulumi is more than that. You can build your own reusable components. To do that, refactor what you have above into a `CdnWebsite` component at `pulumi-challenge/cdn-website/index.ts`.

{{% chooser cloud "aws,gcp" %}}

{{% choosable cloud aws %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";
import * as mime from "mime";

// This is a simpler verison of:
// https://github.com/pulumi/pulumi-aws-static-website
export class CdnWebsite extends pulumi.ComponentResource {
  private bucket: aws.s3.BucketV2;
  private bucketAcl: aws.s3.BucketAclV2;
  private cloudfrontDistribution: aws.cloudfront.Distribution;
  private s3OriginId: string = "myS3Origin";
  private staticWebsiteDirectory: string = "./website";

  constructor(name: string, args: any, opts?: pulumi.ComponentResourceOptions) {
    super("pulumi:challenge:CdnWebsite", name, args, opts);

    this.bucket = new aws.s3.BucketV2(
      "bucketV2",
      {
        tags: {
          Name: "My bucket",
        },
      },
      {
        parent: this,
      }
    );

    this.bucketAcl = new aws.s3.BucketAclV2(
      "bAcl",
      {
        bucket: this.bucket.id,
        acl: aws.s3.PublicReadAcl,
      },
      {
        parent: this,
      }
    );

    this.cloudfrontDistribution = new aws.cloudfront.Distribution(
      "s3Distribution",
      {
        origins: [
          {
            domainName: this.bucket.bucketRegionalDomainName,
            originId: this.s3OriginId,
          },
        ],
        enabled: true,
        isIpv6Enabled: true,
        comment: "Some comment",
        defaultRootObject: "index.html",
        defaultCacheBehavior: {
          allowedMethods: [
            "DELETE",
            "GET",
            "HEAD",
            "OPTIONS",
            "PATCH",
            "POST",
            "PUT",
          ],
          cachedMethods: ["GET", "HEAD"],
          targetOriginId: this.s3OriginId,
          forwardedValues: {
            queryString: false,
            cookies: {
              forward: "none",
            },
          },
          viewerProtocolPolicy: "allow-all",
          minTtl: 0,
          defaultTtl: 3600,
          maxTtl: 86400,
        },
        priceClass: "PriceClass_200",
        restrictions: {
          geoRestriction: {
            restrictionType: "whitelist",
            locations: ["US", "CA", "GB", "DE"],
          },
        },
        viewerCertificate: {
          cloudfrontDefaultCertificate: true,
        },
      },
      {
        parent: this,
      }
    );

    fs.readdirSync(this.staticWebsiteDirectory).forEach((file) => {
      const filePath = `${this.staticWebsiteDirectory}/${file}`;
      const fileContent = fs.readFileSync(filePath).toString();

      new aws.s3.BucketObject(
        file,
        {
          bucket: this.bucket.id,
          source: new pulumi.asset.FileAsset(filePath),
          contentType: mime.getType(filePath) || undefined,
          acl: aws.s3.PublicReadAcl,
        },
        {
          parent: this.bucket,
        }
      );
    });

    // You also need to register all the expected outputs for this
    // component resource that will get returned by default
    this.registerOutputs({
      bucketName: this.bucket.id,
      cdnUrl: this.cloudfrontDistribution.domainName,
    });
  }

  get url(): pulumi.Output<string> {
    return this.cloudfrontDistribution.domainName;
  }
}
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";
import * as fs from "fs";
import * as mime from "mime";

export class CdnWebsite extends pulumi.ComponentResource {
    private bucket: gcp.storage.Bucket;
    private backendBucket: gcp.compute.BackendBucket;
    private ip: gcp.compute.GlobalAddress;
    private httpForwardingRule: gcp.compute.GlobalForwardingRule;
    private staticWebsiteDirectory: string = "./website";


    constructor(name: string, args: any, opts?: pulumi.ComponentResourceOptions) {
        super("pulumi:challenge:CdnWebsite", name, args, opts);

        this.bucket = new gcp.storage.Bucket("mybucket", {
            location: "EU",
            website: {
                mainPageSuffix: "index.html",
            }
        }, opts);

        const bucketIamBinding = new gcp.storage.BucketIAMBinding("bucket-iam-binding", {
            bucket: this.bucket.name,
            role: "roles/storage.objectViewer",
            members: ["allUsers"],
        });

        const config = new pulumi.Config();
        const path = config.get("path") || "./website";

        fs.readdirSync(this.staticWebsiteDirectory).forEach((file) => {
            const filePath = `${this.staticWebsiteDirectory}/${file}`;

            new gcp.storage.BucketObject(file, {
                name: file,
                bucket: this.bucket.id,
                source: new pulumi.asset.FileAsset(filePath),
                contentType: mime.getType(filePath) || undefined,
            });
        });

        // Google Cloud Load Balancer Backend
        this.backendBucket = new gcp.compute.BackendBucket("backend-bucket", {
            bucketName: this.bucket.name,
            enableCdn: true,
        });

        // CDN Configuration
        this.ip = new gcp.compute.GlobalAddress("ip", {}, opts);
        const urlMap = new gcp.compute.URLMap("url-map", { defaultService: this.backendBucket.selfLink }, opts);
        const httpProxy = new gcp.compute.TargetHttpProxy("http-proxy", { urlMap: urlMap.selfLink });

        this.httpForwardingRule = new gcp.compute.GlobalForwardingRule("http-forwarding-rule", {
            ipAddress: this.ip.address,
            ipProtocol: "TCP",
            portRange: "80",
            target: httpProxy.selfLink,
        });

        // You also need to register all the expected outputs for this
        // component resource that will get returned by default
        this.registerOutputs({
            bucketName: this.bucket.id,
            cdnUrl: pulumi.interpolate`http://${this.ip.address}`
        });
    }

    get url(): pulumi.Output<string> {
        return pulumi.interpolate`http://${this.ip.address}`;
    }
}
```

{{% /choosable %}}

{{% /chooser %}}

Now you can consume this elsewhere. Awesome! Back in `pulumi-challenge/index.ts`, change it to have this:

{{% chooser cloud "aws,gcp" %}}

{{% choosable cloud aws %}}

```typescript
// Deploy Website to S3 with CloudFront
// Also shows the challenger how to build a ComponentResource
import { CdnWebsite } from "./cdn-website";

const website = new CdnWebsite("your-startup", {});

export const websiteUrl = website.url;
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Deploy Website to Google Cloud Storage with CDN
// Also shows the challenger how to build a ComponentResource
import { CdnWebsite } from "./cdn-website";

// List of Google Cloud API's That Need to be enabled on the Google Cloud Project
var apiDependencies: Array<pulumi.Resource> = []
var gcpServiceAPIs: Array<string> = [
    "compute.googleapis.com",
]

// Enable required API services for a Google Cloud Platform project
for (var idx in gcpServiceAPIs) {
    apiDependencies.push(
        // Enable Google Cloud Service API
        new gcp.projects.Service("".concat("gcp-api-", gcpServiceAPIs[idx]), {
            disableDependentServices: true,
            service: gcpServiceAPIs[idx],
            disableOnDestroy: false,
        })
    );
}

const website = new CdnWebsite("your-startup", {}, {dependsOn: apiDependencies});
export const websiteUrl = website.url;
```

You'll also note the presence of some code to enable the Google Cloud service APIs that are required to run certain Google Cloud services.

{{% /choosable %}}

{{% /chooser %}}

### Step 6. Adding Another Provider

{{% choosable cloud aws %}}

Now that you have your website being delivered as fast as you can via your `CdnWebsite` component and S3 with Cloudfront, how do you know that what you've deployed actually works? You could leverage a fantastic service, such as Checkly, to ensure your website passes some sanity checks.

{{% /choosable %}}

{{% choosable cloud gcp %}}

Now that you have your website being delivered as fast as possible via your `CdnWebsite` component and Cloud CDN, how do you know that what you've deployed actually works? You could leverage a fantastic service, such as Checkly, to ensure your website passes some sanity checks.

{{% /choosable %}}

First, you need to add a new provider:

```shell
npm install @checkly/pulumi

# API KEY: https://app.checklyhq.com/settings/account/api-keys
pulumi config set checkly:apiKey --secret

# AccountID: https://app.checklyhq.com/settings/account/general
pulumi config set checkly:accountId
```

Next, you can use this in your code.

```typescript
import * as checkly from "@checkly/pulumi";
import * as fs from "fs";

new checkly.Check("index-page", {
  activated: true,
  frequency: 10,
  type: "BROWSER",
  // Change this as needed for your location
  locations: ["eu-west-2"],
  script: websiteUrl.apply((url) =>
    fs
      .readFileSync("checkly-embed.js")
      .toString("utf8")
      .replace("{{websiteUrl}}", url)
  ),
});
```

Your `pulumi-challenge/index.ts` should now look like this:

{{% chooser cloud "aws,gcp" %}}

{{% choosable cloud aws %}}

```typescript
import { CdnWebsite } from "./cdn-website";

const website = new CdnWebsite("your-startup", {});

export const websiteUrl = website.url;

// Monitoring with Checkly
// Demonstrates Standard Package usage
import * as checkly from "@checkly/pulumi";
import * as fs from "fs";

new checkly.Check("index-page", {
  activated: true,
  frequency: 10,
  type: "BROWSER",
  // Change this as needed for your location
  locations: ["eu-west-2"],
  script: websiteUrl.apply((url) =>
    fs
      .readFileSync("checkly-embed.js")
      .toString("utf8")
      .replace("{{websiteUrl}}", url)
  ),
});
```

{{% /choosable %}}

{{% choosable cloud gcp %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

// Deploy Website to Google Cloud Storage with CDN
// Also shows the challenger how to build a ComponentResource
import { CdnWebsite } from "./cdn-website";

// List of Google Cloud API's That Need to be enabled on the Google Cloud Project
var apiDependencies: Array<pulumi.Resource> = []
var gcpServiceAPIs: Array<string> = [
    "compute.googleapis.com",
]

// Enable required API services for a Google Cloud Platform project
for (var idx in gcpServiceAPIs) {
    apiDependencies.push(
        // Enable Google Cloud Service API
        new gcp.projects.Service("".concat("gcp-api-", gcpServiceAPIs[idx]), {
            disableDependentServices: true,
            service: gcpServiceAPIs[idx],
            disableOnDestroy: false,
        })
    );
}

const website = new CdnWebsite("your-startup", {}, {dependsOn: apiDependencies});
export const websiteUrl = website.url;

import * as checkly from "@checkly/pulumi";
import * as fs from "fs";

new checkly.Check("index-page", {
  activated: true,
  frequency: 10,
  type: "BROWSER",
  // Change this as needed for your location
  locations: ["eu-west-2"],
  script: websiteUrl.apply((url) =>
    fs
      .readFileSync("checkly-embed.js")
      .toString("utf8")
      .replace("{{websiteUrl}}", url)
  ),
});
```

{{% /choosable %}}

{{% /chooser %}}

You'll notice the code uses `fs.readFileSync` from `fs` again. That's because the Checkly code, which is also Node based, is inside its own file where it can get good auto-completion and syntax highlighting, rather than storing it as a string object within your existing code. Neat, huh? Add the following to `pulumi-challenge/checkly-embed.js`:

```javascript
const playwright = require("playwright");
const expect = require("expect");

const browser = await playwright.chromium.launch();
const page = await browser.newPage();

await page.goto("https://{{websiteUrl}}");
expect(await page.title()).toBe("Pulumi Challenge");

await browser.close();
```

After adding this code, go ahead and run `pulumi up`. Depending on which cloud provider you're using, it may take a few minutes for the site to become available at the URL noted in the output of the `pulumi up` command. After a few minutes, though, the website for your new startup should be available.

Congratulations! You completed the first Pulumi Challenge. If you'd like to tear down all of these resources, run `pulumi destroy`. Otherwise, enjoy the new website!

Wanna yell it from the rooftops? Write a blog or post a quick video about it, send us the URL, and we'll help amplify your voice! Tag us on social media or email us at [da@pulumi.com](mailto:da@pulumi.com).
