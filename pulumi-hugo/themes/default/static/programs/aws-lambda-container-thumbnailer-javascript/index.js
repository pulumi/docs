"use strict";
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create a bucket to store videos and thumbnails.
const bucket = new aws.s3.Bucket("bucket", {
    forceDestroy: true,
});

// Create a ECR repository for the thumbnailer container image.
const repo = new awsx.ecr.Repository("repo", {
    forceDelete: true,
});

// Create the thumbnailer container image.
const image = new awsx.ecr.Image("image", {
    repositoryUrl: repo.url,
    context: "./app",
    platform: "linux/amd64",
});

// Create an IAM role to grant the Lambda functions access to Amazon S3.
const role = new aws.iam.Role("role", {
    assumeRolePolicy: aws.iam.assumeRolePolicyForPrincipal({
        Service: "lambda.amazonaws.com",
    }),
});

const attachment = new aws.iam.RolePolicyAttachment("attachment", {
    role: role.name,
    policyArn: aws.iam.ManagedPolicy.AWSLambdaExecute,
});

// Create a Lambda function to execute an ffmpeg container task in response to video uploads.
bucket.onObjectCreated(
    "video-handler",
    new aws.lambda.Function("thumbnailer", {
        packageType: "Image",
        imageUri: image.imageUri,
        role: role.arn,
        timeout: 900,
    }),
    { filterSuffix: ".mp4" },
);

// Create another Lambda function to log to CloudWatch when new thumbnails are created.
bucket.onObjectCreated(
    "thumbnail-handler",
    new aws.lambda.CallbackFunction("thumbnail-callback", {
        role,
        callback: async bucketArgs => {
            if (bucketArgs.Records) {
                for (const record of bucketArgs.Records) {
                    console.log(`New thumbnail: File ${record.s3.object.key} saved at ${record.eventTime}.`);
                }
            }
        },
    }),
    { filterSuffix: ".jpg" },
);

// Export the bucket name.
exports.bucketName = bucket.id;
