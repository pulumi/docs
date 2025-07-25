// Copyright 2016-2019, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as fs from "fs";

import { getAIAnswersRewriteAssociation, getEdgeRedirectAssociation } from "./cloudfrontLambdaAssociations";

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
    // addSecurityHeaders indicates if standard security headers should be added.
    // Setting this true will configure security headers to be more strict.
    addSecurityHeaders: stackConfig.getBoolean("addSecurityHeaders") || false,
    // doEdgeRedirects is whether to perform redirects at the CloudFront layer.
    // Setting this true will add a Lambda@Edge function that handles that redirect logic.
    doEdgeRedirects: stackConfig.getBoolean("doEdgeRedirects") || false,
    // doAIAnswersRewrites indicates whether to rewrite HTTP status for AI Answers pages that 404
    // (e.g., due to unpublishing) as HTTP 410 (Gone). Setting this true will add a Lambda@Edge
    // function that handles this logic.
    doAIAnswersRewrites: stackConfig.getBoolean("doAIAnswersRewrites") || false,
    // makeFallbackBucket toggles whether to configure a bucket for serving the website
    // directly out of S3 --- for example, when CloudFront is unavailable. In order to
    // comply with AWS configuration rules, the bucket will be named to match the
    // configured `websiteDomain`.
    makeFallbackBucket: stackConfig.getBoolean("makeFallbackBucket") || false,

    // hostedZone is a config value that represents the hosted zone the A record
    // will be added to. If not set, it will be set to the parent domain of the
    // `websiteDomain` config value.
    hostedZone: stackConfig.get("hostedZone") || undefined,

    // setRootRecord assumes the name of the hosted zone specified for the A record. In production
    // we run a dedicated hosted zone wired up via an NS record. If you wish to share a hosted zone
    // (e.g. in dev environment) you may want to set this to false. This will then take the subdomain
    // of the `websiteDomain` rather than use the root of that zone.
    setRootRecord: stackConfig.get("setRootRecord") || undefined,

    // the registry stack to reference to route traffic to for `/registry` routes.
    registryStack: stackConfig.get("registryStack"),

    answersStack: stackConfig.get("answersStack"),


    // the marketing portal stack to reference to allow the marketing portal
    // to add items to the uploads bucket.
    marketingPortalStack: stackConfig.get("marketingPortalStack"),
};

const aiAppStack = new pulumi.StackReference('pulumi/pulumi-ai-app-infra/prod');
const aiAppDomain = aiAppStack.requireOutput('aiAppDistributionDomain');
const cloudAiAppDomain = aiAppStack.requireOutput('cloudAiAppDistributionDomain');

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

// Create a bucket to store files we do not keep in source control.
const uploadsBucket = new aws.s3.Bucket("uploads-bucket", {
    website: {
        indexDocument: "index.html",
    },
    corsRules: [{
        allowedMethods: [
            "GET",
        ],
        allowedOrigins: ["*"],
    }],
});

if (config.marketingPortalStack) {
    const marketingAppStack = new pulumi.StackReference(config.marketingPortalStack);
    const ecsRoleArn = marketingAppStack.requireOutput("ecsRoleArn");

    const uploadsBucketPolicy = new aws.s3.BucketPolicy("uploads-bucket-policy", {
        bucket: uploadsBucket.bucket,
        policy: pulumi.all([uploadsBucket.arn, ecsRoleArn])
            .apply(([bucketArn, roleArn]) => JSON.stringify({
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Action": [
                            "s3:ListBucket",
                            "s3:GetBucketLocation"
                        ],
                        "Principal": {
                            "AWS": roleArn,
                            },
                        "Effect": "Allow",
                        "Resource": bucketArn,
                    },
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "AWS": roleArn,
                        },
                        "Action": [
                            "s3:GetObject",
                            "s3:PutObject"
                        ],
                        "Resource": `${bucketArn}/*`,
                    },
                ]
            })),
    });
}

// This needs to be set in order to allow the use of ACLs. This was added to update our infrastructure to be
// compatible with the default S3 settings from AWS' April update. `ObjectWriter` was the prior default, so
// changing it to that here to match the configuration prior to the update.
// https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/
const uploadsBucketOwnershipControls = new aws.s3.BucketOwnershipControls("uploads-bucket-ownership-controls", {
    bucket: uploadsBucket.id,
    rule: {
        objectOwnership: "ObjectWriter"
    }
});

const uploadsBucketPublicAccessBlock = new aws.s3.BucketPublicAccessBlock("uploads-public-access-block", {
    bucket: uploadsBucket.id,
    blockPublicAcls: false,
});

const uploadsBucketAcl = new aws.s3.BucketAclV2("uploads-bucket-acl", {
    bucket: uploadsBucket.id,
    acl: aws.s3.PublicReadAcl,
}, {
    dependsOn: [uploadsBucketPublicAccessBlock, uploadsBucketOwnershipControls],
});

const bundlesBucket = new aws.s3.Bucket("bundles-bucket", {
    forceDestroy: true,
    website: {
        indexDocument: "index.html",
    },
});

// Optionally create a fallback bucket for serving the website directly out of S3 when necessary.
// https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html
if (config.makeFallbackBucket) {
    const fallbackBucket = new aws.s3.Bucket(
        "fallback-bucket", {
            bucket: config.websiteDomain,
            acl: aws.s3.PublicReadAcl,
            website: {
                indexDocument: "index.html",
                errorDocument: "404.html",
            },
        },
        {
            protect: true,
        },
    );
}

// We deny the s3:ListBucket permission to anyone but account users to prevent unintended
// disclosure of the bucket's contents.
const originBucketPolicy = new aws.s3.BucketPolicy("origin-bucket-policy", {
    bucket: originBucket.bucket,
    policy: pulumi.all([originBucket.arn, aws.getCallerIdentity()])
        .apply(([arn, awsCallerIdentityResult]) => JSON.stringify({
            Version: "2008-10-17",
            Statement: [
                {
                    Effect: "Deny",
                    Principal: "*",
                    Action: "s3:ListBucket",
                    Resource: arn,
                    Condition: {
                        StringNotEquals: {
                            "aws:PrincipalAccount": awsCallerIdentityResult.accountId,
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
    },
    {
        protect: true,
    },
);

// This needs to be set in order to allow the use of ACLs. This was added to update our infrastructure to be
// compatible with the default S3 settings from AWS' April update. `ObjectWriter` was the prior default, so
// changing it to that here to match the configuration prior to the update.
// https://aws.amazon.com/blogs/aws/heads-up-amazon-s3-security-changes-are-coming-in-april-of-2023/
const logsBucketOwnershipControls = new aws.s3.BucketOwnershipControls("logs-bucket-ownership-controls", {
    bucket: websiteLogsBucket.id,
    rule: {
        objectOwnership: "ObjectWriter"
    }
});

const logsBucketACL = new aws.s3.BucketAclV2("logs-bucket-acl", {
    bucket: websiteLogsBucket.id,
    acl: aws.s3.PrivateAcl,
}, {
    dependsOn: [logsBucketOwnershipControls],
});

// The canonical user ID for the account.
const owner = aws.s3.getCanonicalUserId({});
// Grant the CloudFront log delivery account permission to write to the bucket.
const logsBucketDeliveryACL = new aws.s3.BucketAclV2("logs-bucket-delivery-acl", {
    bucket: websiteLogsBucket.id,
    accessControlPolicy: {
        grants: [
            {
                grantee: {
                    // The canconical ID for the `awslogsdelivery` account.
                    // see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html#AccessLogsOverview
                    id: "c4c1ede66af53448b93c283ce9448c4ba468c9432aa01d700d3878632f77d2d0",
                    type: "CanonicalUser",
                },
                permission: "WRITE",
            },
        ],
        owner: {
            id: owner.then(owner => owner.id),
        },
    },
}, {
    dependsOn: [logsBucketOwnershipControls],
});

const fiveMinutes = 60 * 5;
const oneHour = fiveMinutes * 12;
const oneWeek = oneHour * 24 * 7;
const oneYear = oneWeek * 52;

// AllViewerExceptHostHeader passes all cookies, querystrings, and headers except the Host header.
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html
const allViewerExceptHostHeaderId = "b689b0a8-53d0-40ab-baf2-68738e2966ac";

// CachingDisabled sets min, max, and default cache TTLs to 0.
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html
const cachingDisabledId = "4135ea2d-6df8-44a3-9df3-4b5a84be39ad";

function newSecurityHeadersPolicy(name: string, frameOption: string) {
    return new aws.cloudfront.ResponseHeadersPolicy(name, {
        securityHeadersConfig: {
            frameOptions: {
                frameOption,
                override: false,
            },
            // These remaining options are derived from:
            // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-response-headers-policies.html#managed-response-headers-policies-security
            // "SecurityHeadersPolicy" with ID "67f7725c-6f97-4210-82d7-5512b31e9d03"
            referrerPolicy: {
                referrerPolicy: 'strict-origin-when-cross-origin',
                override: false,
            },
            contentTypeOptions: {
                override: true,
            },
            strictTransportSecurity: {
                accessControlMaxAgeSec: 31536000,
                override: false,
            },
            xssProtection: {
                protection: true,
                modeBlock: true,
                override: false,
            }
        }
    });
}

// Most of the site
const SecurityHeadersPolicy = newSecurityHeadersPolicy('security-headers', config.addSecurityHeaders ? 'DENY' : 'SAMEORIGIN');
// Copilot lives in an iframe
const CopilotSecurityHeadersPolicy = newSecurityHeadersPolicy('copilot-security-headers', 'SAMEORIGIN');

const baseCacheBehavior: aws.types.input.cloudfront.DistributionDefaultCacheBehavior = {
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
    lambdaFunctionAssociations: config.doEdgeRedirects ? [getEdgeRedirectAssociation()] : [],
    responseHeadersPolicyId: SecurityHeadersPolicy.id,
};

const registryOrigins: aws.types.input.cloudfront.DistributionOrigin[] = [];
const registryBehaviors: aws.types.input.cloudfront.DistributionOrderedCacheBehavior[] = [];

const answersOrigins: aws.types.input.cloudfront.DistributionOrigin[] = [];
const answersBehaviors: aws.types.input.cloudfront.DistributionOrderedCacheBehavior[] = [];

if (config.registryStack) {
    const registryStack = new pulumi.StackReference(config.registryStack);
    const registryCDN = registryStack.getOutput("cloudFrontDomain");

    registryOrigins.push(
        {
            originId: registryCDN,
            domainName: registryCDN,
            customOriginConfig: {
                originProtocolPolicy: "https-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            }
        }
    );
    registryBehaviors.push(
        {
            ...baseCacheBehavior,
            targetOriginId: registryCDN,
            pathPattern: "/registry/*",
            defaultTtl: 0,
            minTtl: 0,
            maxTtl: 0,
            originRequestPolicyId: allViewerExceptHostHeaderId,
            cachePolicyId: cachingDisabledId,
            forwardedValues: undefined, // forwardedValues conflicts with cachePolicyId, so we unset it.
        },
    )
}

// domainAliases is a list of CNAMEs that accompany the CloudFront distribution. Any
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
        {
            originId: uploadsBucket.arn,
            domainName: uploadsBucket.websiteEndpoint,
            customOriginConfig: {
                originProtocolPolicy: "http-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
        },
        {
            originId: aiAppDomain,
            domainName: aiAppDomain,
            customOriginConfig: {
                originProtocolPolicy: "https-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
                originReadTimeout: 60,
                originKeepaliveTimeout: 60,
            },
        },
        {
            originId: cloudAiAppDomain,
            domainName: cloudAiAppDomain,
            customOriginConfig: {
                originProtocolPolicy: "https-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
                originReadTimeout: 60,
                originKeepaliveTimeout: 60,
            },
        },
        ...registryOrigins,
        ...answersOrigins,
    ],

    // Default object to serve when no path is given.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html
    defaultRootObject: "index.html",

    defaultCacheBehavior: {
        ...baseCacheBehavior,
    },

    orderedCacheBehaviors: [
        ...registryBehaviors,
        ...answersBehaviors,
        {
            ...baseCacheBehavior,
            targetOriginId: uploadsBucket.arn,
            pathPattern: "/uploads/*",
            defaultTtl: oneHour,
            maxTtl: oneHour,
            forwardedValues: {
                cookies: {
                    forward: "none",
                },
                queryString: false,
                headers: [
                    "Origin",
                    "Access-Control-Request-Headers",
                    "Access-Control-Request-Method",
                ],
            },
        },
        {
            ...baseCacheBehavior,
            targetOriginId: originBucket.arn,
            pathPattern: "/*/rss.xml",
            defaultTtl: oneHour,
            maxTtl: oneHour,
            forwardedValues: {
                cookies: {
                    forward: "none",
                },
                queryString: false,
                headers: [
                    "Origin",
                    "Access-Control-Request-Headers",
                    "Access-Control-Request-Method",
                ],
            },
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/css/bundle.*.css",
            defaultTtl: oneYear,
            maxTtl: oneYear,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/css/marketing.*.css",
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

        // AI app with caching handled by the app
        {
            ...baseCacheBehavior,
            // allow all methods
            allowedMethods: ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"],
            cachedMethods: [
                "GET", "HEAD", "OPTIONS",
            ],
            targetOriginId: aiAppDomain,
            pathPattern: '/ai',
            originRequestPolicyId: allViewerExceptHostHeaderId,
            cachePolicyId: cachingDisabledId,
            lambdaFunctionAssociations: [],
            forwardedValues: undefined, // forwardedValues conflicts with cachePolicyId, so we unset it.
        },
        {
            ...baseCacheBehavior,
            // allow all methods
            allowedMethods: ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"],
            cachedMethods: [
                "GET", "HEAD", "OPTIONS",
            ],
            targetOriginId: aiAppDomain,
            pathPattern: '/ai/*',
            originRequestPolicyId: allViewerExceptHostHeaderId,
            cachePolicyId: cachingDisabledId,
            lambdaFunctionAssociations: config.doAIAnswersRewrites ? [getAIAnswersRewriteAssociation()] : [],
            forwardedValues: undefined, // forwardedValues conflicts with cachePolicyId, so we unset it.
        },

        // Copilot app
        {
            ...baseCacheBehavior,
            // allow all methods
            allowedMethods: ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"],
            cachedMethods: [
                "GET", "HEAD", "OPTIONS",
            ],
            targetOriginId: cloudAiAppDomain,
            pathPattern: '/pulumi-ai/copilot',
            originRequestPolicyId: allViewerExceptHostHeaderId,
            cachePolicyId: cachingDisabledId,
            lambdaFunctionAssociations: [],
            forwardedValues: undefined, // forwardedValues conflicts with cachePolicyId, so we unset it.
            responseHeadersPolicyId: CopilotSecurityHeadersPolicy.id,
        },
        {
            ...baseCacheBehavior,
            // allow all methods
            allowedMethods: ["DELETE", "GET", "HEAD", "OPTIONS", "PATCH", "POST", "PUT"],
            cachedMethods: [
                "GET", "HEAD", "OPTIONS",
            ],
            targetOriginId: cloudAiAppDomain,
            pathPattern: '/pulumi-ai/copilot/*',
            originRequestPolicyId: allViewerExceptHostHeaderId,
            cachePolicyId: cachingDisabledId,
            lambdaFunctionAssociations: [],
            forwardedValues: undefined, // forwardedValues conflicts with cachePolicyId, so we unset it.
            responseHeadersPolicyId: CopilotSecurityHeadersPolicy.id,
        }
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
        minimumProtocolVersion: "TLSv1.2_2021",
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
    const hostedZone = await aws.route53.getZone({ name: config.hostedZone || domainParts.parentDomain });
    return new aws.route53.Record(
        config.websiteDomain,
        {
            name: config.setRootRecord ? "" : domainParts.subdomain,
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

export const uploadsBucketName = uploadsBucket.bucket;
export const originBucketWebsiteDomain = originBucket.websiteDomain;
export const originBucketWebsiteEndpoint = originBucket.websiteEndpoint;
export const cloudFrontDomain = cdn.domainName;
export const websiteDomain = config.websiteDomain;
export const originS3BucketName = originBucket.bucket;
