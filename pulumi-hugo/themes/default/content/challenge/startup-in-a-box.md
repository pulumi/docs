---
title: "Startup in a Box"
layout: challenge/single
description: |
    Build and deploy your very own startup landing site to the cloud, complete with everything you need to get started!
meta_desc: |
    Build and deploy your very own startup landing site to the cloud, complete with everything you need to get started!
---

### Welcome to the Pulumi Challenge!

### Startup in a Box

Thinking about turning that side project into a little something more? Follow along to stand up a website for your startup on Amazon S3 with Cloudfront and Checkly, all using Pulumi. When you're done, we'll send you a fancy drink tumbler with a special Pulumipus on it, just for this Challenge!

### Prerequisites

In order to complete this challenge, you'll need a couple things set up in advance.

* A [Pulumi account](https://app.pulumi.com/signup)

* The [Pulumi CLI]({{< relref "/docs/get-started/install/" >}})

* AWS account

* [Checkly](https://www.checklyhq.com/) account

### Challenge

#### Step 1. Your First Pulumi Program

You will learn how to create a new Pulumi program using our Pulumi templates, specifically for AWS with TypeScript. Create a new directory called `pulumi-challenge` and run the following inside of it:

```shell
pulumi new aws-typescript
```

#### Step 2. Creating Your First Resource

Now that we have a base AWS project configured, we need to create our first resource. In this instance, we'll create a new S3 bucket which will allow us to store our static website. We'll also ensure that this bucket is private, as we want to expose it only via our CDN - which we'll configure next.

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

#### Step 3. Working with Local Files

Pulumi lets you use your favourite programming language to define your infrastructure. Today, we're using TypeScript, which means we have access to the Node API. This includes discovering directories and files.

Using these APIs, we can sync our local files, with the Pulumi resource model, to the S3 bucket.

We need to add the `mime` package from npm, as it is useful for passing the mime type of the file to S3 without hardcoding it.

```shell
npm install mime @types/mime
```

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

We need our actual website too, though. Create a directory called `website` at `pulumi-challenge/website`, and inside it, add `index.html`, `styles.css`, and `normalize.css`.

For `index.html`, we have the structure of a simple website, with places to put links to your project's GitHub and Twitter, as well as your LinkedIn:

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

In `style.css`, we're making it pretty with some bright colors and a CSS background:

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

To make sure our styles display consistently across browsers, we also need to normalize some styles. [Copy normalize.css from GitHub](https://github.com/necolas/normalize.css/blob/master/normalize.css).

#### Step 4. Creating a CDN

Next, we want to front our S3 bucket with Cloudfront. This is a pretty big object, but most of it can be copy and pasted without further thought.

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

#### Step 5. Introducing ComponentResources

Now... we can continue to add resource after resource, but Pulumi is more than that. We can build our own reusable components. Let's refactor what we have above into a `CdnWebsite` component at `pulumi-challenge/cdn-website/index.ts`.

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

    // We also need to register all the expected outputs for this
    // component resource that will get returned by default.
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

Now we can consume this! Awesome. Back in `pulumi-challenge/index.ts`, we now have this:

```typescript
// Deploy Website to S3 with CloudFront
// Also shows the challenger how to build a ComponentResource
import { CdnWebsite } from "./cdn-website";

const website = new CdnWebsite("your-startup", {});
```

#### Step 6. Adding Another Provider

Now that we have our website being delivered as fast as can we via our `CdnWebsite` component and S3 with Cloudfront, how do we know that what we've deployed actually works? We could leverage a fantastic service, such as Checkly, to ensure our website passes some sanity checks.

First, we need to add a new provider:

```shell
npm install @checkly/pulumi

# API KEY: https://app.checklyhq.com/settings/account/api-keys
pulumi config set checkly:apiKey --secret

# AccountID: https://app.checklyhq.com/settings/account/general
pulumi config set checkly:accountId
```

Next, we can use this in our code.

```typescript
import * as checkly from "@checkly/pulumi";
import * as fs from "fs";

new checkly.Check("index-page", {
  activated: true,
  frequency: 10,
  type: "BROWSER",
  locations: ["eu-west-2"],
  script: websiteUrl.apply((url) =>
    fs
      .readFileSync("checkly-embed.js")
      .toString("utf8")
      .replace("{{websiteUrl}}", url)
  ),
});
```

Our `pulumi-challenge/index.ts` should now look like this:

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
  locations: ["eu-west-2"],
  script: websiteUrl.apply((url) =>
    fs
      .readFileSync("checkly-embed.js")
      .toString("utf8")
      .replace("{{websiteUrl}}", url)
  ),
});
```

You'll notice we use `fs.readFileSync` from `fs` again. That's because we're keeping our Checkly code, which is also Node based, inside its own file where it can get good auto-completion and syntax highlightying, rather than storing as a string object within our existing code. Neat, huh? Add the following to `pulumi-challenge/checkly-embed.js`:

```javascript
const playwright = require("playwright");
const expect = require("expect");

const browser = await playwright.chromium.launch();
const page = await browser.newPage();

await page.goto("https://{{websiteUrl}}");
expect(await page.title()).toBe("Pulumi Challenge");

await browser.close();
```

#### Step 7. Introducing the Dynamic Swag Provider

Everyone likes SWAG and we want to give you some for completing this challenge. To do so, we're going to handle this via Pulumi with a Dynamic Provider. Create a new directory and file at `pulumi-challenge/swag-provider/index.ts`:

For this dynamic provider, we can only use CommonJS modules. For making an HTTP request, we can use `got` version `11.8.0`:

```shell
npm install got@11.8.0
```

```typescript
import * as pulumi from "@pulumi/pulumi";

const submittionUrl: string =
  "https://hooks.airtable.com/workflows/v1/genericWebhook/apptZjyaJx5J2BVri/wflmg3riOP6fPjCII/wtr3RoDcz3mTizw3C";

interface SwagInputs {
  name: string;
  email: string;
  address: string;
  size: "XS" | "S" | "M" | "L" | "XL" | "XXL" | "XXXL";
}

interface SwagCreateResponse {
  success: boolean;
}

interface SwagOutputs extends SwagInputs {
  id: string;
}

class SwagProvider implements pulumi.dynamic.ResourceProvider {
  private name: string;

  constructor(name: string) {
    this.name = name;
  }

  async create(props: SwagInputs): Promise<pulumi.dynamic.CreateResult> {
    const got = (await import("got")).default;

    let data = await got
      .post(submittionUrl, {
        headers: {
          "Content-Type": "application/json",
        },
        json: {
          ...props,
        },
      })
      .json<SwagCreateResponse>();

    return { id: props.email, outs: props };
  }
}

export class Swag extends pulumi.dynamic.Resource {
  constructor(
    name: string,
    props: SwagInputs,
    opts?: pulumi.CustomResourceOptions
  ) {
    super(new SwagProvider(name), name, props, opts);
  }
}
```

Now, add this final block to `pulumi-challenge/index.ts` and run `pulumi up`. Enjoy your SWAG!

```typescript
import { Swag } from "./swag-provider";

const swag = new Swag("your-startup", {
  name: "YOUR NAME",
  email: "YOUR EMAIL",
  address: "YOUR ADDRESS",
  size: SIZE,
});
```

Congratulations! You completed the first Pulumi Challenge. If you'd like to tear down all of these resources, run `pulumi destroy`. Otherwise, enjoy the new website! Change it around and make it your own. Your swag will be in the mail shortly!

Wanna yell it from the rooftops? Write a blog or record a post a quick video about it? Let us know and we'll send you an extra, super secret piece of swag! Tag us on social media, or email us at [da@pulumi.com](mailto:da@pulumi.com).
