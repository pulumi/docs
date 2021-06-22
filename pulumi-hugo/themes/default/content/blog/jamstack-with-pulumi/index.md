---
title: "Building Jamstack Infrastructure With Pulumi"
date: 2020-06-09
meta_desc: "Build infrastructure for deploying a jamstack website with Pulumi."
meta_image: jamstack.png
authors:
    - sophia-parafina
tags:
    - aws
    - jamstack
---

A Jamstack is a modern architecture for building websites; JAM stands for JavaScript, APIs, and Markup. Jamstacks are deployed on a [CDN](https://en.wikipedia.org/wiki/Content_delivery_network), and content is stored on a cloud services provider. In addition to the speed and simplicity of deploying static content served from a CDN, there are other advantages such as maintaining content with git, modern build tools to generate the static content, automated builds, atomic deploys, and instant cache validation.

While build tools have simplified the process of creating content ready for deployment on a CDN, creating the infrastructure to serve the content remains complicated. You can use a cloud provider’s web interface or script the build using a CLI tool if you want to manage your infrastructure instead of using a hosted solution. The alternative is to use infrastructure as code tool to automate building and deploying cloud resources. This article demonstrates how to create a jamstack website and deploy it on AWS using Pulumi.

<!--more-->

## Creating Your Website with Hugo

There are many static site generators, but we’ll use Hugo to build the site for this example. We’ll use [Docker](https://docs.docker.com/get-docker/) to run Hugo in a [container](https://hub.docker.com/r/klakegg/hugo/). If you have Docker installed, create a directory to hold the website and change into that directory.

```bash
$ mkdir hugo
$ cd hugo
$ docker run --rm -it -v $(pwd):/src klakegg/hugo:0.72.0-alpine shell
```

The `docker run` command will fetch the container (klakegg/hugo:0.72.0-alpine), map the current directory to the `src` directory in the container, and open a shell.

In the container command line, we will use `hugo` to create a new site called *platypus*.

```bash
$ hugo new site platypus
$ cd platypus
```

Next, we’ll customize the site with a theme. There are many [themes available](https://themes.gohugo.io/), but for this example, we'll use the *ananke* theme. Download the theme to the container, unzip it, and rename the unzipped directory to *ananke*.

```bash
$ wget https://github.com/budparr/gohugo-theme-ananke/archive/master.zip
$ unzip master.zip
$ cp -rf gohugo-theme-ananke-master ./themes/ananke
$ rm -rf master.zip gohugo-theme-ananke-master/
```

Configure the site by editing the *config.toml* file with the following.

```toml
baseURL = "http://www.<your_domain>.com/"
languageCode = "en-us"
title = "Platypus"
theme = "ananke"
```

Use `hugo` to create a new markdown page in the posts directory.

```bash
$ hugo new posts/platypus.md
```

Now it’s time to add content to your site. You can use your favorite editor to write and edit content in your working directory on your machine instead of using the container shell. Edit the markdown file, below is an example page but feel free to add your content.

```md
## Platypus of the Day

**This platypus is a cool critter!**

![platypus](https://static01.nyt.com/images/2017/08/01/science/29TB-PLATYPUS1/29TB-PLATYPUS1-superJumbo.jpg)
```

Finally, we can build the static site with Hugo in the container command line.

```bash
$ hugo -D
```

Hugo will create a *public* directory with the static website.

## Building the Cloud Infrastructure

Configuring a static website can be complicated when using either the AWS web interfaces or the AWS CLI. To deploy a static website, we need to create and configure the following cloud resources.

- [Amazon S3](https://aws.amazon.com/s3/) to store the website's contents
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) for the CDN serving content
- [Amazon Route53](https://aws.amazon.com/route53/) to set up the DNS for the website
- [Amazon Certificate Manager](https://aws.amazon.com/certificate-manager/) for securing the site via HTTPS

Using Pulumi to deploy Infrastructure as Code, we can create and build our infrastructure using either TypeScript or Python. If you haven't installed Pulumi and configured it to work with your AWS credentials, follow the [Getting Started with AWS guide]({{< relref "/docs/get-started/aws" >}}).

To get started building our infrastructure, we’ll download the Python example for setting up a static website with AWS. There are many [examples on our GitHub repository](https://github.com/pulumi/), but we can clone just the AWS Static Website example using a [sparse checkout](https://git-scm.com/docs/git-sparse-checkout) which clones only the directory we specify,

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```bash
$ cd hugo
$ mkdir aws-website
$ cd aws-website

$ git init
$ git remote add origin -f https://github.com/pulumi/examples/
$ git config core.sparseCheckout true
$ echo aws-ts-static-website >> .git/info/sparse-checkout
$ git pull origin master
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ cd hugo
$ mkdir aws-website
$ cd aws-website

$ git init
$ git remote add origin -f https://github.com/pulumi/examples/
$ git config core.sparseCheckout true
$ echo aws-py-static-website >> .git/info/sparse-checkout
$ git pull origin master
```

{{% /choosable %}}
{{< /chooser >}}

Your project directory should look like this:

```bash
./ hugo
|_ playtpus
|_ aws-<language>-static-website
```

## Configuring and Deploying the Website

Now that we have a project to build the website, we will need to configure it so that it uses your domain name. Here are the steps to get it running.

1. Create a new stack or instance for testing:

    {{< chooser language "typescript,python" >}}
    {{% choosable language typescript %}}

```bash
$ cd aws-ts-static-website
$ pulumi stack init website-testing
```

    {{% /choosable %}}
    {{% choosable language python %}}

```bash
$ cd aws-py-static-website
$ pulumi stack init website-testing
```

    {{% /choosable %}}
    {{< /chooser >}}

1. Set the AWS region, you can use any region:

    ```bash
    $ pulumi config set aws:region us-east-1
    ```

1. Install [dependencies](https://www.pulumi.com/docs/intro/concepts/how-pulumi-works/) for our Pulumi program.

    {{< chooser language "typescript,python" >}}
    {{% choosable language typescript %}}

```bash
$ npm install
```

    {{% /choosable %}}
    {{% choosable language python %}}

```bash
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt
```

    {{% /choosable %}}
    {{< /chooser >}}

1. Edit `Pulumi.website-testing.yaml` to set the configuration parameters. The first parameter is the `targetDomain`, which is the domain for the website (e.g., www.example.com).  The parent domain must be a [Route53 Hosted Zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html) in the same AWS account as where the Pulumi program is running. The second parameter is `pathToWebsiteContents`, the relative path to the website’s contents created in Hugo.

    ```yaml
    config:
    aws:region: us-east-1
    static-website:targetDomain: www.<your_domain>.com
    static-website:pathToWebsiteContents: ../public
    ```

1. Run `pulumi up` to preview and deploy changes.  After the preview is displayed, you will be prompted if you want to continue and deploy the website. When all the resources have been created, you will see a listing of the resources similar to this:

    ```bash
    Updating (website-testing):
        Type                              Name                                               Status
    +   pulumi:pulumi:Stack               static-website-website-testing                     created
    +   ├─ pulumi:providers:aws           east                                               created
    +   ├─ aws:acm:Certificate            certificate                                        created
    +   ├─ aws:s3:Bucket                  contentBucket                                      created
    +   │  ├─ aws:s3:BucketObject         posts/page/1/index.html                            created
    ...
    +   ├─ aws:s3:Bucket                  requestLogs                                        created
    +   ├─ aws:route53:Record             www.sophiaparafina.com-validation                  created
    +   ├─ aws:acm:CertificateValidation  certificateValidation                              created
    +   ├─ aws:cloudfront:Distribution    cdn                                                created
    +   └─ aws:route53:Record             www.sophiaparafina.com                             created

    Outputs:
        cloudfront_domain              : "d1l27ffvw5kc32.cloudfront.net"
        content_bucket_url             : "s3://www.your_domain.com"
        content_bucket_website_endpoint: "www.your_domain.com.s3-website-us-west-2.amazonaws.com"
        target_domain_endpoint         : "https://www.your_domain.com/"

    Resources:
        + 27 created

    Duration: 4m15s

    Permalink: https://app.pulumi.com/spara/static-website/website-testing/updates/12
    ```

The website has been deployed, and you can browse it with your domain URL. Since this is a test deployment, don't forget to shut down and delete the cloud resources by running `pulumi destroy`.

## Examine the Code

Let's take a look at how the cloud resources are created, configured, and populated. First up is the S3 bucket where the static website is stored.

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```typescript
// contentBucket is the S3 bucket that the website's contents will be stored in.
const contentBucket = new aws.s3.Bucket("contentBucket",
    {
        bucket: config.targetDomain,
        acl: "public-read",
        // Configure S3 to serve bucket contents as a website. This way S3 will automatically convert
        // requests for "foo/" to "foo/index.html".
        website: {
            indexDocument: "index.html",
            errorDocument: "404.html",
        },
    });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Create an S3 bucket configured as a website bucket.
content_bucket = pulumi_aws.s3.Bucket('contentBucket',
    bucket=target_domain,
    acl='public-read',
    website={
        'index_document': 'index.html',
        'error_document': '404.html'
    })
```

{{% /choosable %}}
{{< /chooser >}}

We add the website content by crawling the `public` directory and converting the files to S3 objects.

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```typescript
// crawlDirectory recursive crawls the provided directory, applying the provided function
// to every file it contains. Doesn't handle cycles from symlinks.
function crawlDirectory(dir: string, f: (_: string) => void) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const filePath = `${dir}/${file}`;
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
            crawlDirectory(filePath, f);
        }
        if (stat.isFile()) {
            f(filePath);
        }
    }
}

// Sync the contents of the source directory with the S3 bucket, which will in-turn show up on the CDN.
const webContentsRootPath = path.join(process.cwd(), config.pathToWebsiteContents);
console.log("Syncing contents from local disk at", webContentsRootPath);
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
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def crawl_directory(content_dir, f):
    """
    Crawl `content_dir` (including subdirectories) and apply the function `f` to each file.
    """
    for file in os.listdir(content_dir):
        filepath = os.path.join(content_dir, file)

        if os.path.isdir(filepath):
            crawl_directory(filepath, f)
        elif os.path.isfile(filepath):
            f(filepath)

web_contents_root_path = os.path.join(os.getcwd(), path_to_website_contents)
def bucket_object_converter(filepath):
    """
    Takes a file path and returns a bucket object managed by Pulumi
    """
    relative_path = filepath.replace(web_contents_root_path + '/', '')
    # Determine the mimetype using the `mimetypes` module.
    mime_type, _ = mimetypes.guess_type(filepath)
    content_file = pulumi_aws.s3.BucketObject(
        relative_path,
        key=relative_path,
        acl='public-read',
        bucket=content_bucket,
        content_type=mime_type,
        source=FileAsset(filepath),
        opts=ResourceOptions(parent=content_bucket)
    )

# Crawl the web content root path and convert the file paths to S3 object resources.
crawl_directory(web_contents_root_path, bucket_object_converter)
```

{{% /choosable %}}
{{< /chooser >}}

Now that we have our content in an S3 bucket, we turn to configure and create the CDN that serves the website. The first task is to create an SSL/TLS certificate based on the domain name hosted on Route 53 DNS if we didn't specify the optional `certificateArn` config value of an existing certificate.

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```typescript
let certificateArn: pulumi.Input<string> = config.certificateArn!;

/**
 * Only provision a certificate (and related resources) if a certificateArn is _not_ provided via configuration.
 */
if (config.certificateArn === undefined) {

    const eastRegion = new aws.Provider("east", {
        profile: aws.config.profile,
        region: "us-east-1", // Per AWS, ACM certificate must be in the us-east-1 region.
    });

    const certificate = new aws.acm.Certificate("certificate", {
        domainName: config.targetDomain,
        validationMethod: "DNS",
    }, { provider: eastRegion });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
if certificate_arn is None:
    # CloudFront is in us-east-1 and expects the ACM certificate to also be in us-east-1.
    # So, we create an east_region provider specifically for these operations.
    east_region = pulumi_aws.Provider('east', profile=pulumi_aws.config.profile, region='us-east-1')

    # Get a certificate for our website domain name.
    certificate = pulumi_aws.acm.Certificate('certificate',
        domain_name=target_domain, validation_method='DNS', opts=ResourceOptions(provider=east_region))
```

{{% /choosable %}}
{{< /chooser >}}

We also create a bucket to hold the CDN logs for the website.

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```typescript
// logsBucket is an S3 bucket that will contain the CDN's request logs.
const logsBucket = new aws.s3.Bucket("requestLogs",
    {
        bucket: `${config.targetDomain}-logs`,
        acl: "private",
    });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Create a logs bucket for the CloudFront logs
logs_bucket = pulumi_aws.s3.Bucket('requestLogs', bucket=f'{target_domain}-logs', acl='private')
```

{{% /choosable %}}
{{< /chooser >}}

Now that we have an SSL/TLS certificate and a S3 bucket to store logs, we can create the CDN. In the CDN resource definition, `origin` sets the S3 bucket as the content source, the domain name, and the ports for serving content. We can also set the cache_behavior, the price class, access restrictions, the logging configuration, and other parameters.

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```typescript
// distributionArgs configures the CloudFront distribution. Relevant documentation:
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
// https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution.html
const distributionArgs: aws.cloudfront.DistributionArgs = {
    enabled: true,
    // Alternate aliases the CloudFront distribution can be reached at, in addition to https://xxxx.cloudfront.net.
    // Required if you want to access the distribution via config.targetDomain as well.
    aliases: [ config.targetDomain ],

    // We only specify one origin for this distribution, the S3 content bucket.
    origins: [
        {
            originId: contentBucket.arn,
            domainName: contentBucket.websiteEndpoint,
            customOriginConfig: {
                // Amazon S3 doesn't support HTTPS connections when using an S3 bucket configured as a website endpoint.
                // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginProtocolPolicy
                originProtocolPolicy: "http-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
        },
    ],

    defaultRootObject: "index.html",

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

    // "All" is the most broad distribution, and also the most expensive.
    // "100" is the least broad, and also the least expensive.
    priceClass: "PriceClass_100",

    // You can customize error responses. When CloudFront receives an error from the origin (e.g. S3 or some other
    // web service) it can return a different error code, and return the response for a different resource.
    customErrorResponses: [
        { errorCode: 404, responseCode: 404, responsePagePath: "/404.html" },
    ],

    restrictions: {
        geoRestriction: {
            restrictionType: "none",
        },
    },

    viewerCertificate: {
        acmCertificateArn: certificateArn,  // Per AWS, ACM certificate must be in the us-east-1 region.
        sslSupportMethod: "sni-only",
    },

    loggingConfig: {
        bucket: logsBucket.bucketDomainName,
        includeCookies: false,
        prefix: `${config.targetDomain}/`,
    },
};

const cdn = new aws.cloudfront.Distribution("cdn", distributionArgs);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
# Create the CloudFront distribution
cdn = pulumi_aws.cloudfront.Distribution('cdn',
    enabled=True,
    aliases=[
        target_domain
    ],
    origins=[{
        'originId': content_bucket.arn,
        'domain_name': content_bucket.website_endpoint,
        'customOriginConfig': {
            'originProtocolPolicy': 'http-only',
            'httpPort': 80,
            'httpsPort': 443,
            'originSslProtocols': ['TLSv1.2'],
        }
    }],
    default_root_object='index.html',
    default_cache_behavior={
        'targetOriginId': content_bucket.arn,
        'viewerProtocolPolicy': 'redirect-to-https',
        'allowedMethods': ['GET', 'HEAD', 'OPTIONS'],
        'cachedMethods': ['GET', 'HEAD', 'OPTIONS'],
        'forwardedValues': {
            'cookies': { 'forward': 'none' },
            'queryString': False,
        },
        'minTtl': 0,
        'defaultTtl': TEN_MINUTES,
        'maxTtl': TEN_MINUTES,
    },
    # PriceClass_100 is the lowest cost tier (US/EU only).
    price_class= 'PriceClass_100',
    custom_error_responses=[{
            'errorCode': 404,
            'responseCode': 404,
            'responsePagePath': '/404.html'
        }],
    # Use the certificate we generated for this distribution.
    viewer_certificate={
        'acmCertificateArn': certificate_arn,
        'sslSupportMethod': 'sni-only',
    },
    restrictions={
        'geoRestriction': {
            'restrictionType': 'none'
        }
    },
    # Put access logs in the log bucket we created earlier.
    logging_config={
        'bucket': logs_bucket.bucket_domain_name,
        'includeCookies': False,
        'prefix': f'${target_domain}/',
    },
    # CloudFront typically takes 15 minutes to fully deploy a new distribution.
    # Skip waiting for that to complete.
    wait_for_deployment=False)
```

{{% /choosable %}}
{{< /chooser >}}

To complete the deployment, we set the `alias_a_record` to point the CDN to our domain name in Route 53.

{{< chooser language "typescript,python" >}}
{{% choosable language typescript %}}

```typescript
// Creates a new Route53 DNS record pointing the domain to the CloudFront distribution.
function createAliasRecord(
    targetDomain: string, distribution: aws.cloudfront.Distribution): aws.route53.Record {
    const domainParts = getDomainAndSubdomain(targetDomain);
    const hostedZoneId = aws.route53.getZone({ name: domainParts.parentDomain }, { async: true }).then(zone => zone.zoneId);
    return new aws.route53.Record(
        targetDomain,
        {
            name: domainParts.subdomain,
            zoneId: hostedZoneId,
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
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def create_alias_record(target_domain, distribution):
    """
    Create a Route 53 Alias A record from the target domain name to the CloudFront distribution.
    """
    subdomain, parent_domain = get_domain_and_subdomain(target_domain)
    hzid = pulumi_aws.route53.get_zone(name=parent_domain).id
    return pulumi_aws.route53.Record(target_domain,
        name=subdomain,
        zone_id=hzid,
        type='A',
        aliases=[
            {
                'name': distribution.domain_name,
                'zoneId': distribution.hosted_zone_id,
                'evaluateTargetHealth': True
            }
        ]
    )

alias_a_record = create_alias_record(target_domain, cdn)
```

{{% /choosable %}}
{{< /chooser >}}

In a single program, we've created all the cloud resources to deploy our content and served it via a CDN.

## Conclusion

Building modern websites is evolving from provider-managed Content Management Systems or user-managed [LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle)) stacks. Static websites deployed in the cloud are popular because they separate content generation from the infrastructure that serves content. However, building and maintaining cloud infrastructure can be complicated and require multiple steps when using web client for configuration. A website using inexpensive storage such as S3 and serving content via Cloudfront can be deployed, versioned, and maintained using your favorite programming language. The Pulumi [examples repository](https://github.com/pulumi/examples) has many more code samples that demonstrate how to build and deploy cloud infrastructure across different cloud providers, using your favorite programming language.

Learn how to automate your cloud infrastructure with Pulumi's [Getting Started tutorials]({{< relref "/docs/get-started" >}}) and [User Guides]({{< relref "/docs/guides" >}}), or join us on [Slack](https://slack.pulumi.com/) if you have questions.
