"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");

const contentBucket = new aws.s3.Bucket("content-bucket", {
    acl: "private",
    website: {
        indexDocument: "index.html",
        errorDocument: "index.html",
    },
    forceDestroy: true,
});

const originAccessIdentity = new aws.cloudfront.OriginAccessIdentity("cloudfront", {
    comment: pulumi.interpolate`OAI-${contentBucket.bucketDomainName}`,
});

new aws.s3.BucketPolicy("cloudfront-bucket-policy", {
    bucket: contentBucket.bucket,
    policy: pulumi.all([contentBucket.bucket, originAccessIdentity.iamArn]).apply(([bucketName, iamArn]) =>
        JSON.stringify({
            Version: "2012-10-17",
            Statement: [
                {
                    Sid: "CloudfrontAllow",
                    Effect: "Allow",
                    Principal: {
                        AWS: iamArn,
                    },
                    Action: "s3:GetObject",
                    Resource: `arn:aws:s3:::${bucketName}/*`,
                },
            ],
        }),
    ),
});
