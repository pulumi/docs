"use strict";
const aws = require("@pulumi/aws");

const bucket = new aws.s3.Bucket("my-bucket");

const ownershipControls = new aws.s3.BucketOwnershipControls("ownership-controls", {
    bucket: bucket.id,
    rule: {
        objectOwnership: "ObjectWriter",
    },
});

const publicAccessBlock = new aws.s3.BucketPublicAccessBlock("public-access-block", {
    bucket: bucket.id,
    blockPublicAcls: false,
});

const bucketMetric = new aws.s3.BucketMetric("my-bucket-metric", {
    bucket: bucket.bucket,
});

const bucketNotification = new aws.s3.BucketNotification("my-bucket-notification", {
    bucket: bucket.bucket,
});

const bucketObject = new aws.s3.BucketObject(
    "my-bucket-object",
    {
        bucket: bucket.bucket,
        content: "hello world",
    },
    { dependsOn: [publicAccessBlock, ownershipControls] },
);

const bucketPolicy = new aws.s3.BucketPolicy("my-bucket-policy", {
    bucket: bucket.bucket,
    policy: bucket.bucket.apply(publicReadPolicyForBucket),
});

function publicReadPolicyForBucket(bucketName) {
    return JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Effect: "Allow",
                Principal: "*",
                Action: ["s3:GetObject"],
                Resource: [
                    `arn:aws:s3:::${bucketName}/*`, // policy refers to bucket name explicitly
                ],
            },
        ],
    });
}
