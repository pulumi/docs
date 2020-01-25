// Copyright 2016-2019, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

import * as fs from "fs";
import * as glob from "glob";
import * as mime from "mime";
import * as path from "path";

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
    });

// contentBucket needs to have the "public-read" ACL so its contents can be ready by CloudFront and
// served. But we deny the s3:ListBucket permission to prevent unintended disclosure of the bucket's
// contents.
const denyListPolicyState: aws.s3.BucketPolicyArgs = {
    bucket: contentBucket.bucket,
    policy: contentBucket.arn.apply((arn: string) => JSON.stringify({
        Version: "2008-10-17",
        Statement: [
            {
                Effect: "Deny",
                Principal: "*",
                Action: "s3:ListBucket",
                Resource: arn,
            },
        ],
    })),
};
const denyListPolicy = new aws.s3.BucketPolicy("deny-list", denyListPolicyState);

// logsBucket stores the request logs for incoming requests.
const logsBucket = new aws.s3.Bucket(
    "requestLogs",
    {
        bucket: `${config.targetDomain}-logs`,
        acl: "private",
    },
    {
        protect: true,
    });

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
    });

// Some files do not get the correct mime/type inferred from the mime package, and we
// need to set our own.
function getMimeType(filePath: string): string | undefined {
    // Ensure that latest-version's mime type is always text/plain. Otherwise it
    // will end up being set to binary/octet-stream, which is not what we want.
    if (path.basename(filePath) === "latest-version") {
        return "text/plain";
    }

    return mime.getType(filePath) || undefined;
}

// Sync the contents of the source directory with the S3 bucket, which will in-turn show up on the CDN.
const webContentsRootPath = path.join(process.cwd(), config.pathToWebsiteContents);
console.log("Syncing contents from local disk at", webContentsRootPath);

// Certain files, like JavaScript and CSS files produced during the build, must exist
// before the website's HTML files can use them (otherwise, pages won't render properly,
// or may be unusable), and others, like fonts and images, would be nice to have there in
// advance, too. Extensions listed here are used for identifying files that should exist
// on S3 before any HTML pages are updated to reference them.
const assetTypes = [
    "js",
    "css",
    "png",
    "jpg",
    "gif",
    "svg",
    "pdf",
    "eot",
    "ttf",
    "woff",
    "woff2",
];

// Keep track of the asset paths we encounter and the resources we create from them, so we
// can declare the necessary dependency relationships.
const assetPaths = new Set<string>();
const assetResources: aws.s3.BucketObject[] = [];

// Find all files by pattern (e.g., "/path/to/begin/from/**/*.jpg"), matching those with
// dot-prefixed folders or filenames (".net", for example) and excluding directories.
// https://github.com/isaacs/node-glob#options
function filePathsByPattern(pattern: string): string[] {
    return glob.sync(pattern, { dot: true, nodir: true });
}

// Find all files matching the patterns above, creating a new BucketObject for each one.
// These objects are declared first in order to pass them conditionally as dependencies
// below.
assetTypes.forEach(pattern => {
    filePathsByPattern(`${webContentsRootPath}/**/*.${pattern}`).forEach(assetPath => {

        // Remember the asset path, so we can ignore it later.
        assetPaths.add(assetPath);

        // Turn the full (local) path into a relative path, so we can use it for an S3 object key.
        const relativeAssetPath = assetPath.replace(webContentsRootPath + "/", "");

        // Create a resource object with the asset.
        const assetResource = new aws.s3.BucketObject(
            relativeAssetPath,
            {
                acl: "public-read",
                key: relativeAssetPath,
                source: new pulumi.asset.FileAsset(assetPath),
                contentType: getMimeType(assetPath) || undefined,
                bucket: contentBucket,
            },
            {
                parent: contentBucket,
            },
        );

        // Add the bucket resource to the list of asset dependencies.
        assetResources.push(assetResource);
    });
});

// Now create bucket objects for everything else, bypassing anything created already.
filePathsByPattern(`${webContentsRootPath}/**/*`).forEach(filePath => {

    // Ignore previously encountered asset paths, since they'll already have been declared.
    if (assetPaths.has(filePath)) {
        return;
    }

    const relativeFilePath = filePath.replace(webContentsRootPath + "/", "");
    const baseArgs = {
        acl: "public-read",
        key: relativeFilePath,
        bucket: contentBucket,
    };

    // Create a new S3 object for most files, but HTML files that contain a redirect
    // just create a stubbed out S3 object with the right metadata so they return a
    // 301 redirect (instead of serving the HTML with a meta-redirect). This ensures
    // the right HTTP code response is returned for search engines, as well as
    // enables better support for URL anchors.
    const redirect = getMetaRefreshRedirect(filePath);
    if (!redirect) {
        const contentType = getMimeType(filePath) || undefined;

        const contentFile = new aws.s3.BucketObject(
            relativeFilePath,
            {
                ...baseArgs,
                source: new pulumi.asset.FileAsset(filePath),
                contentType,
            },
            {
                parent: contentBucket,

                // Only HTML files need depend on asset files.
                dependsOn: contentType === "text/html" ? assetResources : undefined,
            },
        );
    } else {
        const s3Redirect = new aws.s3.BucketObject(
            relativeFilePath,
            {
                ...baseArgs,
                source: new pulumi.asset.FileAsset("/dev/null"), // Empty file.
                websiteRedirect: translateRedirect(filePath, redirect),
            },
            {
                parent: contentBucket,
            },
        );
    }
});

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
export const contentBucketWebsiteDomain = contentBucket.websiteDomain;
export const contentBucketWebsiteEndpoint = contentBucket.websiteEndpoint;
export const cloudFrontDomain = cdn.domainName;
