// Copyright 2016-2019, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx"
import * as pulumi from "@pulumi/pulumi";

import * as fs from "fs";
import * as path from "path";
import * as tar from "tar";
import * as tmp from "tmp";
import * as glob from "glob";

const stackConfig = new pulumi.Config();

const config = {
    // pathToWebsiteContents is a relative path to the website's contents.
    pathToWebsiteContents: stackConfig.require("pathToWebsiteContents"),
    // targetDomain is the domain/host to serve content at.
    targetDomain: stackConfig.require("targetDomain"),
    // alias is an optional domain alias the CDN will support as well.
    alias: stackConfig.get("alias") || undefined,
    // ACM certificate for the target domain. Must be in the us-east-1 region.
    certificateArn: stackConfig.require("certificateArn"),
    // redirectDomain is the domain to use for any redirects.
    redirectDomain: stackConfig.get("redirectDomain") || undefined,
};

// redirectDomain is the domain to use when redirecting.
const redirectDomain = config.redirectDomain || config.targetDomain;

// contentBucket stores the static content to be served via the CDN.
const contentBucket = new aws.s3.Bucket(
    "contentBucket",
    {
        bucket: config.targetDomain,
        acl: "public-read",

        // Have S3 serve its contents as if it were a website. This is how we get the right behavior
        // for routes like "foo/", which S3 will automatically translate to "foo/index.html".
        website: {
            indexDocument: "index.html",
            errorDocument: "404.html",
        },
    },
    {
        protect: false,
    },
);

const cluster = awsx.ecs.Cluster.getDefault();
const archiveBucket = new aws.s3.Bucket("archive-bucket", { forceDestroy: true });
const archiveHandler = new awsx.ecs.FargateTaskDefinition("archiveHandler", {
    container: {
        image: awsx.ecs.Image.fromPath("archiveHandlerImage", "./"),
        // image: awsx.ecs.Image.fromFunction(() => {
        //     console.log("Boy it'd be neat if we could just do this.");
        // }),
        memory: 4096,
        cpu: 4,
    },
});

archiveBucket.onObjectCreated("onArchiveUploaded", new aws.lambda.CallbackFunction<aws.s3.BucketEvent, void>("onUploadHandler", {
    runtime: "nodejs10.x",
    policies: [
        aws.iam.ManagedPolicies.AWSLambdaFullAccess,
        aws.iam.ManagedPolicies.AmazonEC2ContainerServiceFullAccess,
    ],
    callback: async bucketArgs => {
        if (!bucketArgs.Records) {
            return;
        }

        for (const record of bucketArgs.Records) {
            console.log(`A file was uploaded to ${archiveBucket.id.get()} file: ${record.s3.object.key}`);
            const source = `s3://${archiveBucket.id.get()}/${record.s3.object.key}`;
            const dest = `s3://${contentBucket.id.get()}`;

            await archiveHandler.run({
                cluster,
                overrides: {
                    containerOverrides: [
                        {
                            name: "container",
                            command: [
                                source,
                                dest,
                            ],
                        },
                    ],
                },
            });
        }
    },
}));

// Upload the website archive.
if (!pulumi.runtime.isDryRun()) {

    pulumi.all([ archiveBucket.id, contentBucket.id ]).apply(async ([ archiveBucketId, contentBucketId ]) => {
        const s3 = new aws.sdk.S3();

        // Download the last few JS and CSS bundles, filtering for the ones we care about.
        // TODO: Age these out, like only keep them around for a month, or something.
        const cssResult = await s3.listObjectsV2({
            Bucket: contentBucketId,
            Prefix: "css/",
        }).promise();

        const jsResult = await s3.listObjectsV2({
            Bucket: contentBucketId,
            Prefix: "js/",
        }).promise();

        const cssBundles = (cssResult.Contents?.filter(f => f.Key?.match(/styles\..+\.css/)) || []).map(o => o.Key);
        const jsBundles = (jsResult.Contents?.filter(f => f.Key?.match(/bundle\.min\..+\.js/)) || []).map(o => o.Key);

        // Add them to the build.
        [ ...cssBundles, ...jsBundles ].forEach(async (key) => {
            if (key) {
                const bundlesResult = await s3.getObject({
                    Bucket: contentBucketId,
                    Key: key,
                }).promise();

                fs.writeFileSync(`${webContentsRootPath}/${key}`, bundlesResult.Body);
                console.log(`Wrote ${`${webContentsRootPath}/${key}`}`);
            }
        });



        // Tar everything up.
        const archivePath = tmp.fileSync({ postfix: ".tgz" }).name;
        tar.c(
            {
                gzip: true,
                sync: true,
                file: archivePath,
                C: config.pathToWebsiteContents,
                portable: true,
            },
            fs.readdirSync(config.pathToWebsiteContents),
        );

        // Upload the tarball.
        const result = s3.putObject({
            Bucket: archiveBucketId,
            Key: path.basename(archivePath),
            Body: fs.readFileSync(archivePath),
        })
        .promise();

        console.log(`Website archive ${archivePath} was uploaded.`);
    });
}

// logsBucket stores the request logs for incoming requests.
const logsBucket = new aws.s3.Bucket(
    "requestLogs",
    {
        bucket: `${config.targetDomain}-logs`,
        acl: "private",
    },
    {
        protect: true,
    },
);

const fiveMinutes = 60 * 5;
const oneHour = fiveMinutes * 12;
const oneWeek = oneHour * 24 * 7;

const baseCacheBehavior = {
    targetOriginId: contentBucket.arn,
    compress: true,
    viewerProtocolPolicy: "redirect-to-https",
    allowedMethods: ["GET", "HEAD", "OPTIONS"],
    cachedMethods: ["GET", "HEAD", "OPTIONS"],

    // S3 doesn't need take any of these values into account when serving content.
    forwardedValues: {
        cookies: {
            forward: "none",
        },
        queryString: false,
    },

    minTtl: 0,
    defaultTtl: fiveMinutes,
    maxTtl: fiveMinutes,
};

// distributionArgs configures the CloudFront distribution. Relevant documentation:
// https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution.html
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
// https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront
const distributionArgs: aws.cloudfront.DistributionArgs = {
    enabled: true,

    // We only specify one origin for this distribution: the S3 content bucket.
    origins: [
        {
            originId: contentBucket.arn,
            domainName: contentBucket.websiteEndpoint,
            customOriginConfig: {
                // > If your Amazon S3 bucket is configured as a website endpoint, [like we have here] you must specify
                // > HTTP Only. Amazon S3 doesn't support HTTPS connections in that configuration.
                // tslint:disable-next-line: max-line-length
                // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesOriginProtocolPolicy
                originProtocolPolicy: "http-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
        },
    ],

    // Default object to serve when no path is given.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html
    defaultRootObject: "index.html",

    defaultCacheBehavior: {
        ...baseCacheBehavior,
    },

    orderedCacheBehaviors: [
        {
            ...baseCacheBehavior,
            pathPattern: "/css/styles.*.css",
            defaultTtl: oneWeek,
            maxTtl: oneWeek,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/bundle.min.*.js",
            defaultTtl: oneWeek,
            maxTtl: oneWeek,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/search.min.*.js",
            defaultTtl: oneWeek,
            maxTtl: oneWeek,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/fonts/*",
            defaultTtl: oneHour,
            maxTtl: oneHour,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/icons/*",
            defaultTtl: oneHour,
            maxTtl: oneHour,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/logos/*",
            defaultTtl: oneHour,
            maxTtl: oneHour,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/images/home/*",
            defaultTtl: oneHour,
            maxTtl: oneHour,
        },
    ],

    // "All" is the most broad distribution, and also the most expensive.
    // "100" is the least broad, and also the least expensive.
    priceClass: "PriceClass_All",

    // Customize error pages.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html
    customErrorResponses: [
        {
            errorCode: 404,
            responseCode: 404,
            errorCachingMinTtl: fiveMinutes,
            responsePagePath: "/404.html",
        },
    ],

    restrictions: {
        geoRestriction: {
            restrictionType: "none",
        },
    },

    // CloudFront certs must be in us-east-1, just like API Gateway.
    viewerCertificate: {
        acmCertificateArn: config.certificateArn,
        sslSupportMethod: "sni-only",
        minimumProtocolVersion: "TLSv1.2_2018",
    },

    loggingConfig: {
        bucket: logsBucket.bucketDomainName,
        includeCookies: false,
        prefix: `${config.targetDomain}/`,
    },
};

// NOTE: Sometimes updating the CloudFront distribution will fail with:
// "PreconditionFailed: The request failed because it didn't meet the preconditions in one or more
// request-header fields."
//
// This is due to https://github.com/pulumi/pulumi/issues/1449:
// Error "CloudFront ETag Out Of Sync" when externally modifying CloudFront resource
const cdn = new aws.cloudfront.Distribution(
    "cdn",
    distributionArgs,
    {
        protect: true,
        dependsOn: [ contentBucket, logsBucket ],
    },
);

// Sync the contents of the source directory with the S3 bucket, which will in-turn show up on the CDN.
const webContentsRootPath = path.join(process.cwd(), config.pathToWebsiteContents);

// Returns the redirect URL if filePath is an HTML file that contains a meta refresh tag, otherwise undefined.
function getMetaRefreshRedirect(filePath: string): string | undefined {
    // Only .html files contain meta refresh redirects.
    if (path.extname(filePath) !== ".html") {
        return undefined;
    }

    // Extract the redirect from the content of the file.
    const text = fs.readFileSync(filePath, "utf8");
    const regex = /<meta\s+?http-equiv="refresh"\s+?content="0;\s+?url=(.*?)"/gmi;
    const match = regex.exec(text);

    if (match && match.length === 2) {
        const redirect = match[1];
        if (!redirect || redirect.length === 0) {
            throw new Error(`Meta refresh tag found in "${filePath}" but the redirect URL was empty.`);
        }
        return redirect;
    }

    return match && match.length === 2 ? match[1] : undefined;
}

// translateRedirect fixes up the redirect, if needed.
// If the redirect is already prefixed with "https://" or "http://", it is returned unmodified.
// If the redirect starts with "/", it is translated to an `https://${redirectDomain}${redirect}`.
// Otherwise, an Error is thrown.
function translateRedirect(filePath: string, redirect: string): string {
    // If the redirect already has the https or http protocol specified, return it.
    if (redirect.startsWith("https://") || redirect.startsWith("http://")) {
        return redirect;
    }

    // If the redirect starts with "/", prefix with the redirect domain and return it.
    if (redirect.startsWith("/")) {
        return `https://${redirectDomain}${redirect}`;
    }

    // Otherwise, it's not in a format that we expect so throw an error.
    throw new Error(`The redirect "${redirect}" in "${filePath}" is not in an expected format.`);
}

glob.sync(`${webContentsRootPath}/**/*.html`).map(filePath => {
    const relativeFilePath = filePath.replace(webContentsRootPath + "/", "");
    const redirect = getMetaRefreshRedirect(filePath);

    if (redirect) {
        const redirectObject = new aws.s3.BucketObject(
            relativeFilePath,
            {
                acl: "public-read",
                key: relativeFilePath,
                bucket: contentBucket,
                source: new pulumi.asset.FileAsset("/dev/null"), // Empty file.
                websiteRedirect: translateRedirect(filePath, redirect),
            },
            {
                parent: contentBucket,
            },
        );
    }
});

// Split a domain name into its subdomain and parent domain names.
// e.g. "www.example.com" => "www", "example.com".
function getDomainAndSubdomain(domain: string): { subdomain: string, parentDomain: string} {
    const parts = domain.split(".");
    if (parts.length < 2) {
        throw new Error(`No TLD found on ${domain}`);
    }
    if (parts.length === 2) {
        return {
            subdomain: "",
            parentDomain: domain + ".",
        };
    }

    const subdomain = parts[0];
    parts.shift();  // Drop first element.
    return {
        subdomain,
        // Trailing "." to canonicalize.
        parentDomain: parts.join(".") + ".",
    };
}

// Creates a new Route53 DNS record pointing the domain to the CloudFront distribution.
async function createAliasRecord(
        targetDomain: string, distribution: aws.cloudfront.Distribution): Promise<aws.route53.Record> {
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

// const aRecord = createAliasRecord(config.targetDomain, cdn);

export const contentBucketName = contentBucket.bucket;
export const contentBucketUri = contentBucket.bucket.apply(b => `s3://${b}`);
export const archiveBucketUri = archiveBucket.bucket.apply(b => `s3://${b}`);
export const contentBucketWebsiteDomain = contentBucket.websiteDomain;
export const contentBucketWebsiteEndpoint = contentBucket.websiteEndpoint;
export const cloudFrontDomain = cdn.domainName;
