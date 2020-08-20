// Copyright 2016-2019, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as fs from "fs";

const stackConfig = new pulumi.Config();

const config = {
    // websiteDomain is the domain/host to serve content at.
    websiteDomain: stackConfig.require("websiteDomain"),
    // websiteLogsBucketName is the name of the S3 bucket used for storing access logs.
    websiteLogsBucketName: stackConfig.require("websiteLogsBucketName"),
    // ACM certificate for the target domain. Must be in the us-east-1 region.
    certificateArn: stackConfig.require("certificateArn"),
    // redirectDomain is the domain to use for any redirects.
    redirectDomain: stackConfig.get("redirectDomain") || undefined,
    // originBucketNameOverride is an optional value that can be used to manually pin the
    // website to a specific S3 bucket. Values are of the form "bucket-name-123", rather
    // than "s3://bucket-name-123".
    originBucketNameOverride: stackConfig.get("originBucketNameOverride") || undefined,
    // pathToOriginBucketMetadata is the path to the file produced at the end of the
    // sync-and-test-bucket script (i.e., scripts/sync-and-test-bucket.sh).
    pathToOriginBucketMetadata: stackConfig.require("pathToOriginBucketMetadata"),
};

// originBucketName is the name of the S3 bucket to use as the CloudFront origin for the
// website. This bucket is presumed to exist prior to the Pulumi run; if it doesn't, this
// program will fail.
export let originBucketName: string | undefined;

// If a build metadata file is present and contains valid content, use that for the bucket
// name by default. Will fail if there's a file present that isn't parsable as expected.
if (fs.existsSync(config.pathToOriginBucketMetadata)) {
    originBucketName = JSON.parse(fs.readFileSync(config.pathToOriginBucketMetadata).toString()).bucket;
}

// However, if the bucket's been configured manually, use that instead. A manually
// configured bucket means that someone's decided to pin it.
if (config.originBucketNameOverride) {
    originBucketName = config.originBucketNameOverride;
}

// If there's still no bucket selected, it's an error.
if (!originBucketName) {
    throw new Error("An origin bucket was not specified.");
}

// Fetch the bucket we'll use for the preview or update.
const originBucket = pulumi.output(aws.s3.getBucket({
    bucket: originBucketName,
}));

// The origin bucket needs to have the "public-read" ACL so its contents can be read by
// CloudFront and served. But we deny the s3:ListBucket permission to anyone but account
// users to prevent unintended disclosure of the bucket's contents.
const originBucketPolicy = new aws.s3.BucketPolicy("origin-bucket-policy", {
    bucket: originBucket.bucket,
    policy: originBucket.arn.apply(arn => JSON.stringify({
        Version: "2008-10-17",
        Statement: [
            {
                Effect: "Deny",
                Principal: "*",
                Action: "s3:ListBucket",
                Resource: arn,
                Condition: {
                    StringNotEquals: {
                        "aws:PrincipalAccount": aws.getCallerIdentity().accountId,
                    },
                },
            },
        ],
    })),
});

// websiteLogsBucket stores the request logs for incoming requests.
const websiteLogsBucket = new aws.s3.Bucket(
    "website-logs-bucket",
    {
        bucket: config.websiteLogsBucketName,
        acl: aws.s3.PrivateAcl,
    },
    {
        protect: true,
    },
);

const fiveMinutes = 60 * 5;
const oneHour = fiveMinutes * 12;
const oneWeek = oneHour * 24 * 7;
const oneYear = oneWeek * 52;

const baseCacheBehavior = {
    targetOriginId: originBucket.arn,
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

// domainAliases is a list of CNAMEs that accompany the CloudFront distribution. Any
// domain name to be used to access the website must be listed here.
const domainAliases = [];

// websiteDomain is the A record for the website bucket associated with the website.
domainAliases.push(config.websiteDomain);

// redirectDomain is the domain to use for fully-qualified 301 redirects.
if (config.redirectDomain) {
     domainAliases.push(config.redirectDomain);
}

// distributionArgs configures the CloudFront distribution. Relevant documentation:
// https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution.html
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
// https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront
const distributionArgs: aws.cloudfront.DistributionArgs = {
    enabled: true,

    aliases: domainAliases,

    // We only specify one origin for this distribution: the S3 content bucket.
    origins: [
        {
            originId: originBucket.arn,
            domainName: originBucket.websiteEndpoint,
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
            defaultTtl: oneYear,
            maxTtl: oneYear,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/bundle.min.*.js",
            defaultTtl: oneYear,
            maxTtl: oneYear,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/search.min.*.js",
            defaultTtl: oneYear,
            maxTtl: oneYear,
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

        // Web-component loaders must not be cached, because the names of the files they
        // load will change between builds.
        {
            ...baseCacheBehavior,
            pathPattern: "/js/components.js",
            defaultTtl: 0,
            minTtl: 0,
            maxTtl: 0,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/components/components.js",
            defaultTtl: 0,
            minTtl: 0,
            maxTtl: 0,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/components/components.esm.js",
            defaultTtl: 0,
            minTtl: 0,
            maxTtl: 0,
        },

        // Build-metadata files are never cached.
        {
            ...baseCacheBehavior,
            pathPattern: "/metadata.json",
            defaultTtl: 0,
            minTtl: 0,
            maxTtl: 0,
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
        bucket: websiteLogsBucket.bucketDomainName,
        includeCookies: false,
        prefix: `${config.websiteDomain}/`,
    },
};

// cdn is the CloudFront distribution that serves the content of the website.
const cdn = new aws.cloudfront.Distribution(
    "cdn",
    distributionArgs,
    {
        protect: true,
        dependsOn: [ websiteLogsBucket ],
    },
);

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
        },
        {
            protect: true,
        });
}

[...new Set(domainAliases)].map(alias => createAliasRecord(alias, cdn));

export const originBucketWebsiteDomain = originBucket.websiteDomain;
export const originBucketWebsiteEndpoint = originBucket.websiteEndpoint;
export const cloudFrontDomain = cdn.domainName;
