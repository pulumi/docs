import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an S3 bucket.
const bucket = new aws.s3.Bucket("my-bucket");

// Create an S3 bucket policy that grants read access to all objects in the bucket.
// The Resource field uses pulumi.interpolate to append "/*" to the bucket ARN,
// targeting individual objects rather than the bucket itself.
const policy = new aws.s3.BucketPolicy("my-bucket-policy", {
    bucket: bucket.id,
    policy: pulumi.jsonStringify({
        Version: "2012-10-17",
        Statement: [
            {
                Effect: "Allow",
                Principal: "*",
                Action: "s3:GetObject",
                Resource: pulumi.interpolate`${bucket.arn}/*`,
            },
        ],
    }),
});

// Export the name of the bucket.
export const bucketName = bucket.id;
