import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an S3 bucket
const s3Bucket = new aws.s3.Bucket("myBucket");

// IAM Policy Document that allows the Lambda service to write to the S3 bucket
const s3BucketPolicyDocument = s3Bucket.arn.apply(arn =>
    JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Effect: "Allow",
                Principal: { Service: "lambda.amazonaws.com" },
                Action: ["s3:PutObject", "s3:PutObjectAcl"],
                Resource: `${arn}/*`,
            },
        ],
    }),
);

// Attach the policy to the bucket
const s3BucketPolicy = new aws.s3.BucketPolicy("myBucketPolicy", {
    bucket: s3Bucket.id,
    policy: s3BucketPolicyDocument,
});

// Export the names and ARNs of the created resources
export const bucketName = s3Bucket.id;
export const bucketArn = s3Bucket.arn;
