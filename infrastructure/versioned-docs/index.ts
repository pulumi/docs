// Copyright 2016-2026, Pulumi Corporation.  All rights reserved.
//
// Versioned SDK & CLI docs — storage stack.
//
// This stack owns ONLY the permanent, write-once archive bucket and the GitHub-OIDC
// publisher role used to write to it. The main www.pulumi.com stack
// (infrastructure/index.ts) consumes the exports here via a StackReference and adds
// the CloudFront origin + `/docs/versioned/*` behavior. Keeping the bucket in its own
// stack means its lifecycle is independent of the per-deploy atomic origin buckets,
// and dev stacks don't each spin up an archive bucket.
//
// Stacks: `testing` (account 571684982431) and `production` (account 388588623842).

import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const config = new pulumi.Config();

// env drives the bucket name. Taken from the stack name (testing | production)
// unless explicitly overridden via config.
const env = config.get("env") || pulumi.getStack();

const bucketName = `pulumi-docs-versioned-${env}`;

// Permanent archive bucket. `protect: true` guards against accidental teardown.
// Website hosting is required because the main distribution reaches S3 origins via
// their website endpoints, which is what resolves a directory URL like
// /docs/versioned/pulumi-cli/v3.246.0/up/ to .../up/index.html.
const bucket = new aws.s3.Bucket("versioned-docs", {
    bucket: bucketName,
}, {
    protect: true,
});

const bucketWebsite = new aws.s3.BucketWebsiteConfiguration("versioned-docs-website", {
    bucket: bucket.id,
    indexDocument: { suffix: "index.html" },
    errorDocument: { key: "404.html" },
});

// Versioning lets us recover an accidental overwrite and — unlike S3 Object Lock in
// compliance mode — does NOT block redaction. Immutability is operational: only the
// publisher role writes, and publish-version.sh refuses to overwrite an existing
// {tool}/{version}/ prefix without --force.
new aws.s3.BucketVersioning("versioned-docs-versioning", {
    bucket: bucket.id,
    versioningConfiguration: { status: "Enabled" },
});

// Abort dangling multipart uploads after 7 days. No object expiration — archives are
// permanent.
new aws.s3.BucketLifecycleConfiguration("versioned-docs-lifecycle", {
    bucket: bucket.id,
    rules: [{
        id: "abort-incomplete-multipart",
        status: "Enabled",
        filter: {},
        abortIncompleteMultipartUpload: { daysAfterInitiation: 7 },
    }],
});

// Public-read (GetObject) like the existing origin buckets, but deliberately NOT
// ListBucket — the archive is browsable by URL, not enumerable.
const ownership = new aws.s3.BucketOwnershipControls("versioned-docs-ownership", {
    bucket: bucket.id,
    rule: { objectOwnership: "ObjectWriter" },
});

const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("versioned-docs-public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
    blockPublicPolicy: false,
    ignorePublicAcls: false,
    restrictPublicBuckets: false,
});

new aws.s3.BucketPolicy("versioned-docs-policy", {
    bucket: bucket.id,
    policy: bucket.arn.apply(arn => JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Sid: "PublicReadObjects",
            Effect: "Allow",
            Principal: "*",
            Action: "s3:GetObject",
            Resource: `${arn}/*`,
        }],
    })),
}, { dependsOn: [publicAccessBlock, ownership] });

// --- Publisher role: assumed by pulumi/docs GitHub Actions via OIDC ---
//
// The SDK/CLI doc workflows have no AWS access today; they assume ONLY this narrow
// role to publish snapshots. The broad deploy role (ContinuousDelivery) is not reused.
//
// The GitHub OIDC provider already exists in both accounts (the ContinuousDelivery
// role relies on it), so we reference it by its well-known ARN rather than creating
// it (CreateOpenIDConnectProvider would fail if one already exists).
const accountId = aws.getCallerIdentityOutput().accountId;
const oidcProviderArn = accountId.apply(
    id => `arn:aws:iam::${id}:oidc-provider/token.actions.githubusercontent.com`,
);

// distributionArn (optional): when set, scopes cloudfront:CreateInvalidation to that
// distribution instead of "*". The distribution lives in the main stack, so by default
// we avoid coupling its ARN here — CreateInvalidation is low-risk.
const distributionArn = config.get("distributionArn");

const publisherRole = new aws.iam.Role("versioned-docs-publisher", {
    name: `versioned-docs-publisher-${env}`,
    description: "Assumed by pulumi/docs GitHub Actions to publish versioned SDK/CLI doc snapshots.",
    assumeRolePolicy: oidcProviderArn.apply(arn => JSON.stringify({
        Version: "2012-10-17",
        Statement: [{
            Effect: "Allow",
            Principal: { Federated: arn },
            Action: "sts:AssumeRoleWithWebIdentity",
            Condition: {
                StringEquals: {
                    "token.actions.githubusercontent.com:aud": "sts.amazonaws.com",
                },
                StringLike: {
                    // Restrict to the pulumi/docs repository (any ref).
                    "token.actions.githubusercontent.com:sub": "repo:pulumi/docs:*",
                },
            },
        }],
    })),
});

new aws.iam.RolePolicy("versioned-docs-publisher-policy", {
    role: publisherRole.id,
    policy: pulumi.all([bucket.arn, distributionArn]).apply(([arn, distArn]) => JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Sid: "BucketObjectReadWrite",
                Effect: "Allow",
                Action: ["s3:PutObject", "s3:GetObject", "s3:DeleteObject"],
                Resource: `${arn}/*`,
            },
            {
                Sid: "BucketList",
                Effect: "Allow",
                Action: ["s3:ListBucket", "s3:GetBucketLocation"],
                Resource: arn,
            },
            {
                Sid: "Invalidate",
                Effect: "Allow",
                Action: "cloudfront:CreateInvalidation",
                Resource: distArn || "*",
            },
        ],
    })),
});

// Consumed by the main stack's StackReference and by scripts/versioned-docs/*.
export const bucketNameOutput = bucket.bucket;
export const bucketArn = bucket.arn;
export const bucketWebsiteEndpoint = bucketWebsite.websiteEndpoint;
export const publisherRoleArn = publisherRole.arn;
