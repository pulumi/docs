import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import { Output } from "@pulumi/pulumi";

import * as fs from "fs";
import * as mime from "mime";
import * as path from "path";

const stackConfig = new pulumi.Config("pulumi.io")

const config = {
    // pathToWebsiteContents is a relativepath to the website's contents.
    pathToWebsiteContents: stackConfig.require("pathToWebsiteContents"),
    // targetDomain is the domain/host to serve content at.
    targetDomain: stackConfig.require("targetDomain"),
    // alias is an optional domain alias the CDN will support as well.
    alias: stackConfig.get("alias") || undefined,
    // ACM certificate for the target domain. Must be in the us-east-1 region.
    certificateArn: stackConfig.require("certificateArn"),
};

const protectResource: pulumi.ResourceOptions = { protect: true };

// contentBucket stores the static content to be served via the CDN.
const contentBucket = new aws.s3.Bucket(
    "contentBucket",
    {
        bucket: config.targetDomain,
        acl: "public-read",
    },
    protectResource);

// logsBucket stores the request logs for incomming requests.
const logsBucket = new aws.s3.Bucket(
    "requestLogs",
    {
        bucket: `${config.targetDomain}-logs`,
        acl: "private",
    },
    protectResource);

const oneMinute = 60;

// distributionArgs configures the CloudFront distribution. Relevant documentation:
// https://www.terraform.io/docs/providers/aws/r/cloudfront_distribution.html
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html
// https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_cloudfront
const distributionArgs: aws.cloudfront.DistributionArgs = {
    enabled: true,
    aliases: (config.alias ? [ config.targetDomain, config.alias ] : [ config.targetDomain ]),

    // We only specify one origin for this distribution: the S3 content bucket.
    origins: [
        {
            originId: contentBucket.arn,
            domainName: contentBucket.bucketDomainName,
        },
    ],

    // Default object to serve when no path is given.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html
    defaultRootObject: "index.html",

    defaultCacheBehavior: {
        targetOriginId: contentBucket.arn,

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
        defaultTtl: oneMinute,
        maxTtl: oneMinute,
    },

    // "All" is the most broad distribution, and also the most expensive.
    // "100" is the least broad, and also the least expensive.
    priceClass: "PriceClass_All",

    // Customize error pages.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html
    customErrorResponses: [
        {
            errorCode: 404,
            responseCode: 404,
            errorCachingMinTtl: oneMinute,
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
//
// For information on how to work around this error, see "CloudFront ETag Out Of Sync":
// https://docs.pulumi.com/reference/known-issues.html
const cdn = new aws.cloudfront.Distribution("cdn", distributionArgs, protectResource);

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
                acl: "public-read",
                key: relativeFilePath,
                bucket: contentBucket,
                source: new pulumi.asset.FileAsset(filePath),
                contentType: mime.getType(filePath) || undefined,
            },
            {
                parent: contentBucket,
            });
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
const aRecord = createAliasRecord(config.targetDomain, cdn);

export const contentBucketUri = contentBucket.bucket.apply(b => `s3://${b}`);
export const cloudFrontDomain = cdn.domainName;
