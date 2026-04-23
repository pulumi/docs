// Copyright 2016-2019, Pulumi Corporation.  All rights reserved.

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";
import * as fs from "fs";

import { getAIRedirectAndGoneAssociation, getEdgeRedirectAssociation } from "./cloudfrontLambdaAssociations";
import { getMarkdownNegotiationFunctionAssociation } from "./cloudfrontFunctions";

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

    // the guides stack to reference to route traffic to for `/guides` routes.
    guidesStack: stackConfig.get("guidesStack"),

    answersStack: stackConfig.get("answersStack"),


    // the marketing portal stack to reference to allow the marketing portal
    // to add items to the uploads bucket.
    marketingPortalStack: stackConfig.get("marketingPortalStack"),

    // Enable data warehouse access to CloudFront logs
    enableDataWarehouseAccess: stackConfig.getBoolean("enableDataWarehouseAccess") || false,

    // cdnLogDeliverySourceName is the name of the CloudFront-created log delivery source.
    // If not set, CDN log delivery configuration will be skipped.
    cdnLogDeliverySourceName: stackConfig.get("cdnLogDeliverySourceName") || undefined,

    // enableWaf toggles whether to create and associate a WAF WebACL with the CloudFront distribution.
    enableWaf: stackConfig.getBoolean("enableWaf") || false,

    // wafRateLimit is the maximum number of requests per 5-minute window per IP before WAF blocks.
    wafRateLimit: stackConfig.getNumber("wafRateLimit") || 500,
};

// CloudFront Function to lowercase URIs for .NET SDK docs so that
// case-insensitive requests resolve to the lowercase S3 keys.
const dotnetLowercaseFunction = new aws.cloudfront.Function("dotnet-lowercase-uri", {
    runtime: "cloudfront-js-2.0",
    comment: "Lowercases URI path for .NET SDK doc requests",
    code: `function handler(event) {
    var request = event.request;
    request.uri = request.uri.toLowerCase();
    return request;
}`,
    publish: true,
});

const aiAppStack = new pulumi.StackReference('pulumi/pulumi-ai-app-infra/prod');
const cloudAiAppDomain = aiAppStack.requireOutput('cloudAiAppDistributionDomain');

// Reference to the OSS Airflow on EKS stack for data warehouse access (only if enabled)
let airflowIrsaRoleArn: pulumi.Output<any> | undefined;
if (config.enableDataWarehouseAccess) {
    const airflowStack = new pulumi.StackReference('pulumi/dwh-workflows-orchestrate-airflow/production');
    airflowIrsaRoleArn = airflowStack.getOutput('irsaRoleArn');
}

// WAF WebACL for rate limiting. WebACLs for CloudFront must be in us-east-1.
let webAcl: aws.wafv2.WebAcl | undefined;

if (config.enableWaf) {
    const usEast1 = new aws.Provider("us-east-1-waf", {
        region: aws.Region.USEast1,
    });

    webAcl = new aws.wafv2.WebAcl("cdn-waf", {
        scope: "CLOUDFRONT",
        description: `Rate limiting for ${config.websiteDomain}`,
        defaultAction: { allow: {} },
        rules: [{
            name: "allow-link-checker",
            priority: 0,
            action: { allow: {} },
            statement: {
                byteMatchStatement: {
                    searchString: "pulumi+blc/0.1",
                    fieldToMatch: {
                        singleHeader: { name: "user-agent" },
                    },
                    positionalConstraint: "EXACTLY",
                    textTransformations: [{ priority: 0, type: "NONE" }],
                },
            },
            visibilityConfig: {
                cloudwatchMetricsEnabled: true,
                metricName: "cdn-waf-allow-link-checker",
                sampledRequestsEnabled: true,
            },
        }, {
            name: "rate-limit-per-ip",
            priority: 1,
            action: { block: {} },
            statement: {
                rateBasedStatement: {
                    limit: config.wafRateLimit,
                    aggregateKeyType: "IP",
                },
            },
            visibilityConfig: {
                cloudwatchMetricsEnabled: true,
                metricName: "cdn-waf-rate-limit",
                sampledRequestsEnabled: true,
            },
        }],
        visibilityConfig: {
            cloudwatchMetricsEnabled: true,
            metricName: "cdn-waf",
            sampledRequestsEnabled: true,
        },
    }, { provider: usEast1 });
}

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
const uploadsBucket = new aws.s3.Bucket("uploads-bucket", {});

const uploadsBucketWebsite = new aws.s3.BucketWebsiteConfiguration("uploads-bucket-website", {
    bucket: uploadsBucket.id,
    indexDocument: {
        suffix: "index.html",
    },
});

const uploadsBucketCors = new aws.s3.BucketCorsConfiguration("uploads-bucket-cors", {
    bucket: uploadsBucket.id,
    corsRules: [{
        allowedMethods: ["GET"],
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

const uploadsBucketAcl = new aws.s3.BucketAcl("uploads-bucket-acl", {
    bucket: uploadsBucket.id,
    acl: aws.s3.CannedAcl.PublicRead,
}, {
    dependsOn: [uploadsBucketPublicAccessBlock, uploadsBucketOwnershipControls],
});

// Bucket for tracking social media post state (idempotency).
const socialStateBucket = new aws.s3.Bucket("social-post-state", {});

new aws.s3.BucketVersioning("social-post-state-versioning", {
    bucket: socialStateBucket.id,
    versioningConfiguration: { status: "Enabled" },
});

new aws.s3.BucketPublicAccessBlock("social-post-state-public-access-block", {
    bucket: socialStateBucket.id,
    blockPublicAcls: true,
    blockPublicPolicy: true,
    ignorePublicAcls: true,
    restrictPublicBuckets: true,
});

const bundlesBucket = new aws.s3.Bucket("bundles-bucket", {
    forceDestroy: true,
});

const bundlesBucketWebsite = new aws.s3.BucketWebsiteConfiguration("bundles-bucket-website", {
    bucket: bundlesBucket.id,
    indexDocument: {
        suffix: "index.html",
    },
});

// Optionally create a fallback bucket for serving the website directly out of S3 when necessary.
// https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-custom-domain-walkthrough.html
if (config.makeFallbackBucket) {
    const fallbackBucket = new aws.s3.Bucket(
        "fallback-bucket",
        {
            bucket: config.websiteDomain,
            acl: aws.s3.CannedAcl.PublicRead,
        },
        {
            protect: true,
        },
    );

    const fallbackBucketWebsite = new aws.s3.BucketWebsiteConfiguration(
        "fallback-bucket-website",
        {
            bucket: fallbackBucket.id,
            indexDocument: {
                suffix: "index.html",
            },
            errorDocument: {
                key: "404.html",
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

// Enable ACLs on the logs bucket to support CloudWatch Logs delivery with bucket-owner-full-control ACL
const logsBucketOwnershipControls = new aws.s3.BucketOwnershipControls("logs-bucket-ownership-controls", {
    bucket: websiteLogsBucket.id,
    rule: {
        objectOwnership: "BucketOwnerPreferred"
    }
});

// Grant the CloudWatch Logs delivery service permission to write CloudFront logs to the bucket.
// Uses the new CloudWatch Logs infrastructure v2 for S3 delivery.
// https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html
const logsBucketPolicy = new aws.s3.BucketPolicy("logs-bucket-policy", {
    bucket: websiteLogsBucket.id,
    policy: config.enableDataWarehouseAccess && airflowIrsaRoleArn
        ? pulumi.all([websiteLogsBucket.arn, aws.getCallerIdentity(), airflowIrsaRoleArn])
            .apply(([bucketArn, caller, airflowRole]) => {
                const statements: any[] = [
                    {
                        Sid: "AWSLogDeliveryWriteObjects",
                        Effect: "Allow",
                        Principal: {
                            Service: "delivery.logs.amazonaws.com"
                        },
                        Action: "s3:PutObject",
                        Resource: `${bucketArn}/*`,
                        Condition: {
                            StringEquals: {
                                "s3:x-amz-acl": "bucket-owner-full-control",
                                "aws:SourceAccount": caller.accountId
                            },
                            ArnLike: {
                                "aws:SourceArn": `arn:aws:logs:us-east-1:${caller.accountId}:delivery-source:*`
                            }
                        }
                    },
                    {
                        Sid: "AWSLogDeliveryListBucket",
                        Effect: "Allow",
                        Principal: {
                            Service: "delivery.logs.amazonaws.com"
                        },
                        Action: "s3:ListBucket",
                        Resource: bucketArn,
                        Condition: {
                            StringEquals: {
                                "aws:SourceAccount": caller.accountId
                            },
                            ArnLike: {
                                "aws:SourceArn": `arn:aws:logs:us-east-1:${caller.accountId}:delivery-source:*`
                            }
                        }
                    },
                    // Data warehouse (OSS Airflow on EKS via IRSA) read access
                    {
                        Sid: "DataWarehouseReadObjects",
                        Effect: "Allow",
                        Principal: {
                            AWS: airflowRole
                        },
                        Action: ["s3:GetObject", "s3:GetObjectVersion"],
                        Resource: `${bucketArn}/*`
                    },
                    {
                        Sid: "DataWarehouseListBucket",
                        Effect: "Allow",
                        Principal: {
                            AWS: airflowRole
                        },
                        Action: ["s3:ListBucket", "s3:GetBucketLocation"],
                        Resource: bucketArn
                    },
                    // Enforce TLS
                    {
                        Sid: "RestrictToTLSRequestsOnly",
                        Effect: "Deny",
                        Principal: "*",
                        Action: "s3:*",
                        Resource: [bucketArn, `${bucketArn}/*`],
                        Condition: {
                            Bool: {
                                "aws:SecureTransport": "false"
                            }
                        }
                    }
                ];

                return JSON.stringify({
                    Version: "2012-10-17",
                    Statement: statements
                });
            })
        : pulumi.all([websiteLogsBucket.arn, aws.getCallerIdentity()])
            .apply(([bucketArn, caller]) => {
                const statements: any[] = [
                    {
                        Sid: "AWSLogDeliveryWriteObjects",
                        Effect: "Allow",
                        Principal: {
                            Service: "delivery.logs.amazonaws.com"
                        },
                        Action: "s3:PutObject",
                        Resource: `${bucketArn}/*`,
                        Condition: {
                            StringEquals: {
                                "s3:x-amz-acl": "bucket-owner-full-control",
                                "aws:SourceAccount": caller.accountId
                            },
                            ArnLike: {
                                "aws:SourceArn": `arn:aws:logs:us-east-1:${caller.accountId}:delivery-source:*`
                            }
                        }
                    },
                    {
                        Sid: "AWSLogDeliveryListBucket",
                        Effect: "Allow",
                        Principal: {
                            Service: "delivery.logs.amazonaws.com"
                        },
                        Action: "s3:ListBucket",
                        Resource: bucketArn,
                        Condition: {
                            StringEquals: {
                                "aws:SourceAccount": caller.accountId
                            },
                            ArnLike: {
                                "aws:SourceArn": `arn:aws:logs:us-east-1:${caller.accountId}:delivery-source:*`
                            }
                        }
                    },
                    // Enforce TLS
                    {
                        Sid: "RestrictToTLSRequestsOnly",
                        Effect: "Deny",
                        Principal: "*",
                        Action: "s3:*",
                        Resource: [bucketArn, `${bucketArn}/*`],
                        Condition: {
                            Bool: {
                                "aws:SecureTransport": "false"
                            }
                        }
                    }
                ];

                return JSON.stringify({
                    Version: "2012-10-17",
                    Statement: statements
                });
            })
});

const fiveMinutes = 60 * 5;
const tenMinutes = fiveMinutes * 2;
const thirtyMinutes = fiveMinutes * 6;
const oneHour = fiveMinutes * 12;
const oneWeek = oneHour * 24 * 7;
const oneYear = oneWeek * 52;

// AllViewerExceptHostHeader passes all cookies, querystrings, and headers except the Host header.
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html
const allViewerExceptHostHeaderId = "b689b0a8-53d0-40ab-baf2-68738e2966ac";

// Cache policies are required to serve Brotli-compressed responses. Legacy
// forwardedValues configurations only support gzip; enabling Brotli requires
// a CachePolicy with enableAcceptEncodingBrotli set. See:
// https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html
function cacheKeyPolicy(name: string, ttl: number, cacheKeyHeaders: string[] = []): aws.cloudfront.CachePolicy {
    const cachingEnabled = ttl > 0;
    return new aws.cloudfront.CachePolicy(name, {
        defaultTtl: ttl,
        maxTtl: ttl,
        minTtl: 0,
        parametersInCacheKeyAndForwardedToOrigin: {
            enableAcceptEncodingBrotli: cachingEnabled,
            enableAcceptEncodingGzip: cachingEnabled,
            cookiesConfig: { cookieBehavior: "none" },
            headersConfig: cacheKeyHeaders.length > 0
                ? { headerBehavior: "whitelist", headers: { items: cacheKeyHeaders } }
                : { headerBehavior: "none" },
            queryStringsConfig: { queryStringBehavior: "none" },
        },
    });
}

// Keys for each TTL bucket used by the distribution's cache behaviors. The
// "thirty-minute-cache" and "one-year-cache" names are preserved so Pulumi
// updates them in place (adding the Brotli/Gzip flags) rather than replacing.
//
// thirtyMinuteCachePolicy varies on the Accept header so /registry/* and
// /guides/* (which proxy to separate CDNs whose viewer-request functions do
// markdown content negotiation) cache HTML and markdown variants separately
// at the apex layer. Without this, whichever variant populates the apex cache
// first is served to every requester until TTL. Fragmentation is bounded to
// two entries per URI because the downstream functions normalize Accept to
// "text/markdown" or absent before the inner cache lookup.
const tenMinuteCacheKeyPolicy = cacheKeyPolicy("ten-minute-cache", tenMinutes);
const thirtyMinuteCachePolicy = cacheKeyPolicy("thirty-minute-cache", thirtyMinutes, ["Accept"]);
const oneHourCacheKeyPolicy = cacheKeyPolicy("one-hour-cache", oneHour);
const oneWeekCacheKeyPolicy = cacheKeyPolicy("one-week-cache", oneWeek);
const oneYearCachePolicy = cacheKeyPolicy("one-year-cache", oneYear);
const noCacheKeyPolicy = cacheKeyPolicy("no-cache", 0);

const baseSecurityHeadersConfig = {
    frameOptions: {
        frameOption: config.addSecurityHeaders ? 'DENY' : 'SAMEORIGIN',
        override: false,
    },
    contentSecurityPolicy: {
        // Allow embedding from LearnWorlds (LMS). X-Frame-Options is ignored by modern
        // browsers when frame-ancestors is present in CSP.
        contentSecurityPolicy: "frame-ancestors 'self' *.learnworlds.com",
        override: false,
    },
    // These remaining options are derived from:
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-response-headers-policies.html#managed-response-headers-policies-security
    // "SecurityHeadersPolicy" with ID "67f7725c-6f97-4210-82d7-5512b31e9d03"
    referrerPolicy: {
        referrerPolicy: 'strict-origin-when-cross-origin' as const,
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
};

// Fingerprinted/hashed assets get immutable browser caching (1 year).
// This is separate from CloudFront edge TTLs (defaultTtl/maxTtl) which only
// control CDN-level caching. Without this policy, browsers see no Cache-Control
// header and fall back to heuristic caching with 304 revalidation round-trips.
const BrandLogoCachePolicy = new aws.cloudfront.ResponseHeadersPolicy('brand-logo-cache-headers', {
    securityHeadersConfig: baseSecurityHeadersConfig,
    customHeadersConfig: {
        items: [{
            header: "Cache-Control",
            value: "public, max-age=1800",
            override: true,
        }],
    },
});

const DefaultCachePolicy = new aws.cloudfront.ResponseHeadersPolicy('default-cache-headers', {
    securityHeadersConfig: baseSecurityHeadersConfig,
    customHeadersConfig: {
        items: [{
            header: "Cache-Control",
            value: "max-age=60, stale-while-revalidate=300",
            override: true,
        }],
    },
});

const OneHourCachePolicy = new aws.cloudfront.ResponseHeadersPolicy('one-hour-cache-headers', {
    securityHeadersConfig: baseSecurityHeadersConfig,
    customHeadersConfig: {
        items: [{
            header: "Cache-Control",
            value: "public, max-age=3600",
            override: true,
        }],
    },
});

const ImmutableCachePolicy = new aws.cloudfront.ResponseHeadersPolicy('immutable-cache-headers', {
    securityHeadersConfig: baseSecurityHeadersConfig,
    customHeadersConfig: {
        items: [{
            header: "Cache-Control",
            value: "public, max-age=31536000, immutable",
            override: true,
        }],
    },
});

// Docs pages add Vary: Accept so downstream caches (browsers, proxies) know the
// response may differ based on the Accept header (HTML vs markdown).
const DocsResponseHeadersPolicy = new aws.cloudfront.ResponseHeadersPolicy('docs-response-headers', {
    securityHeadersConfig: baseSecurityHeadersConfig,
    customHeadersConfig: {
        items: [{
            header: "Vary",
            value: "Accept",
            override: false,
        }],
    },
});

// baseCacheBehavior holds the fields shared by every behavior. TTLs and
// cache-key config are NOT set here: each behavior (default or ordered) must
// attach its own cachePolicyId, or set forwardedValues + minTtl/defaultTtl/maxTtl
// if it needs CORS header forwarding that a cache policy can't express.
const baseCacheBehavior: aws.types.input.cloudfront.DistributionDefaultCacheBehavior = {
    targetOriginId: originBucket.arn,
    compress: true,

    viewerProtocolPolicy: "redirect-to-https",

    allowedMethods: ["GET", "HEAD", "OPTIONS"],
    cachedMethods: ["GET", "HEAD", "OPTIONS"],

    lambdaFunctionAssociations: config.doEdgeRedirects ? [getEdgeRedirectAssociation()] : [],
    responseHeadersPolicyId: DefaultCachePolicy.id,
};

const registryOrigins: aws.types.input.cloudfront.DistributionOrigin[] = [];
const registryBehaviors: aws.types.input.cloudfront.DistributionOrderedCacheBehavior[] = [];

const guidesOrigins: aws.types.input.cloudfront.DistributionOrigin[] = [];
const guidesBehaviors: aws.types.input.cloudfront.DistributionOrderedCacheBehavior[] = [];

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
            },
            // Origin Shield for registry should be configured in pulumi/registry,
            // not here, since the registry has its own CloudFront distribution.
        }
    );
    registryBehaviors.push(
        {
            ...baseCacheBehavior,
            targetOriginId: registryCDN,
            // "/registry*" (no slash) matches /registry, /registry.md, and
            // /registry/... so the .md URL-suffix convention reaches the
            // registry origin alongside the trailing-slash form.
            pathPattern: "/registry*",
            cachePolicyId: thirtyMinuteCachePolicy.id,
            originRequestPolicyId: allViewerExceptHostHeaderId,
        },
        // Registry package logos (e.g. /fingerprinted/logos/pkg/aws.<hash>.svg)
        // are served from the registry origin with year-long immutable caching.
        // Use /fingerprinted/logos/pkg/* (not /fingerprinted/*) so docs-site
        // fingerprinted assets (icons, brand logos, customer logos, product
        // images) fall through to the default docs origin.
        // See pulumi/registry#10488 for context.
        {
            ...baseCacheBehavior,
            targetOriginId: registryCDN,
            pathPattern: "/fingerprinted/logos/pkg/*",
            cachePolicyId: oneYearCachePolicy.id,
            originRequestPolicyId: allViewerExceptHostHeaderId,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
    )
}

if (config.guidesStack) {
    const guidesStack = new pulumi.StackReference(config.guidesStack);
    const guidesCDN = guidesStack.getOutput("cloudFrontDomain");

    guidesOrigins.push(
        {
            originId: guidesCDN,
            domainName: guidesCDN,
            customOriginConfig: {
                originProtocolPolicy: "https-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
            },
            // Origin Shield for guides should be configured in pulumi/guides,
            // not here, since guides has its own CloudFront distribution.
        }
    );
    guidesBehaviors.push(
        {
            ...baseCacheBehavior,
            targetOriginId: guidesCDN,
            pathPattern: "/guides/*",
            cachePolicyId: thirtyMinuteCachePolicy.id,
            originRequestPolicyId: allViewerExceptHostHeaderId,
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
            originShield: {
                enabled: true,
                originShieldRegion: "us-west-2",
            },
        },
        {
            originId: uploadsBucket.arn,
            domainName: uploadsBucketWebsite.websiteEndpoint,
            customOriginConfig: {
                originProtocolPolicy: "http-only",
                httpPort: 80,
                httpsPort: 443,
                originSslProtocols: ["TLSv1.2"],
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
        ...guidesOrigins,
        ...answersOrigins,
    ],

    // Default object to serve when no path is given.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DefaultRootObject.html
    defaultRootObject: "index.html",

    defaultCacheBehavior: {
        ...baseCacheBehavior,
        cachePolicyId: tenMinuteCacheKeyPolicy.id,
    },

    orderedCacheBehaviors: [
        ...registryBehaviors,
        ...guidesBehaviors,
        ...answersBehaviors,

        // Dotnet SDK docs: lowercase URIs so case-insensitive requests resolve.
        // Must come BEFORE /docs/* so the more specific pattern matches first.
        {
            ...baseCacheBehavior,
            pathPattern: "/docs/reference/pkg/dotnet/*",
            cachePolicyId: tenMinuteCacheKeyPolicy.id,
            functionAssociations: [{
                eventType: "viewer-request",
                functionArn: dotnetLowercaseFunction.arn,
            }],
        },

        // Docs pages support Accept: text/markdown content negotiation.
        {
            ...baseCacheBehavior,
            pathPattern: "/docs/*",
            cachePolicyId: tenMinuteCacheKeyPolicy.id,
            functionAssociations: [getMarkdownNegotiationFunctionAssociation()],
            responseHeadersPolicyId: DocsResponseHeadersPolicy.id,
        },
        // /uploads/* and /*/rss.xml stay on legacy forwardedValues because they
        // need to forward CORS request headers to the origin. These payloads
        // are mostly binary (uploads) or small (rss.xml), so the missed Brotli
        // opportunity is negligible.
        {
            ...baseCacheBehavior,
            targetOriginId: uploadsBucket.arn,
            pathPattern: "/uploads/*",
            minTtl: 0,
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
            minTtl: 0,
            defaultTtl: tenMinutes,
            maxTtl: tenMinutes,
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
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/css/marketing.*.css",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/css/homepage.*.css",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/css/marketing-homepage.*.css",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/bundle.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/search.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/chunk-*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/consent-manager.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/algolia.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/homepage.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/marketing-homepage.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/marketing.*.js",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/fonts/*",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        // Docs-site fingerprinted assets (icons, brand logos, customer logos,
        // product images) use content-hashed filenames and are served with
        // immutable 1-year caching from the default docs origin.
        {
            ...baseCacheBehavior,
            pathPattern: "/fingerprinted/*",
            cachePolicyId: oneYearCachePolicy.id,
            responseHeadersPolicyId: ImmutableCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/icons/*",
            cachePolicyId: oneHourCacheKeyPolicy.id,
            responseHeadersPolicyId: BrandLogoCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/logos/brand/*",
            cachePolicyId: oneHourCacheKeyPolicy.id,
            responseHeadersPolicyId: BrandLogoCachePolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/logos/*",
            cachePolicyId: oneHourCacheKeyPolicy.id,
            responseHeadersPolicyId: OneHourCachePolicy.id,
        },
        // Web-component loaders must not be cached, because the names of the files they
        // load will change between builds.
        {
            ...baseCacheBehavior,
            pathPattern: "/js/components.js",
            cachePolicyId: noCacheKeyPolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/components/components.js",
            cachePolicyId: noCacheKeyPolicy.id,
        },
        {
            ...baseCacheBehavior,
            pathPattern: "/js/components/components.esm.js",
            cachePolicyId: noCacheKeyPolicy.id,
        },

        // Build-metadata files are never cached.
        {
            ...baseCacheBehavior,
            pathPattern: "/metadata.json",
            cachePolicyId: noCacheKeyPolicy.id,
        },

        // /ai -> /product/neo/ redirect, /ai/* -> 410 Gone
        {
            ...baseCacheBehavior,
            pathPattern: '/ai',
            cachePolicyId: oneWeekCacheKeyPolicy.id,
            lambdaFunctionAssociations: [getAIRedirectAndGoneAssociation()],
        },
        {
            ...baseCacheBehavior,
            pathPattern: '/ai/*',
            cachePolicyId: oneWeekCacheKeyPolicy.id,
            lambdaFunctionAssociations: [getAIRedirectAndGoneAssociation()],
        },

    ],

    // "All" is the most broad distribution, and also the most expensive.
    // "100" is the least broad, and also the least expensive.
    priceClass: "PriceClass_All",

    httpVersion: "http2and3",

    // Customize error pages.
    // https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages.html
    customErrorResponses: [
        {
            errorCode: 404,
            responseCode: 404,
            errorCachingMinTtl: 10,
            responsePagePath: "/404.html",
        },
        // Map 403 Forbidden errors to 404 Not Found.
        // S3 returns 403 when it can't determine if an object exists due to bucket policy
        // that denies ListBucket permission. This provides a better user experience by
        // translating HTTP 403s into proper 404s and showing the 404 error page.
        {
            errorCode: 403,
            responseCode: 404,
            errorCachingMinTtl: 10,
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

    webAclId: webAcl?.arn,
};

// cdn is the CloudFront distribution that serves the content of the website.
const cdn = new aws.cloudfront.Distribution(
    "cdn",
    distributionArgs,
    {
        protect: true,
        dependsOn: [websiteLogsBucket],
    },
);

// https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.html

// Configure CDN log delivery if cdnLogDeliverySourceName is set
if (config.cdnLogDeliverySourceName) {

    const cdnLogDeliveryDestination = new aws.cloudwatch.LogDeliveryDestination("cdn-log-delivery-destination", {
        region: "us-east-1",
        name: "cdn-s3-destination",
        outputFormat: "parquet",
        deliveryDestinationConfiguration: {
            destinationResourceArn: websiteLogsBucket.arn,
        },
    }, {
        dependsOn: [logsBucketPolicy, logsBucketOwnershipControls],
    });

    // Reference the CloudFront-created log delivery source
    const cdnLogDelivery = new aws.cloudwatch.LogDelivery("cdn-log-delivery", {
        region: "us-east-1",
        deliverySourceName: config.cdnLogDeliverySourceName,
        deliveryDestinationArn: cdnLogDeliveryDestination.arn,
        s3DeliveryConfigurations: [{
            suffixPath: pulumi.all([aws.getCallerIdentity(), cdn.id]).apply(([caller, distributionId]) =>
                `${config.websiteDomain}/${caller.accountId}/${distributionId}/{yyyy}/{MM}/{dd}/{HH}`
            ),
            enableHiveCompatiblePath: false,
        }],
    });
}

// Split a domain name into its subdomain and parent domain names.
// e.g. "www.example.com" => "www", "example.com".
function getDomainAndSubdomain(domain: string): { subdomain: string, parentDomain: string } {
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
export const socialStateBucketName = socialStateBucket.bucket;
export const originBucketWebsiteDomain = originBucket.websiteDomain;
export const originBucketWebsiteEndpoint = originBucket.websiteEndpoint;
export const cloudFrontDomain = cdn.domainName;
export const cloudFrontDistributionId = cdn.id;
export const websiteDomain = config.websiteDomain;
export const originS3BucketName = originBucket.bucket;
export const wafWebAclArn = webAcl?.arn;
export const readme = fs.readFileSync("./README.md").toString();
