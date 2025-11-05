import * as aws from "@pulumi/aws";

import { PolicyPack, validateResourceOfType, ResourceValidationPolicy } from "@pulumi/policy";

export const s3BucketPrefixPolicy: ResourceValidationPolicy = {
    name: "s3-bucket-prefix",
    description: "Ensures S3 buckets use the required naming prefix.",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
        const requiredPrefix = "mycompany-";
        const bucketPrefix = bucket.bucketPrefix || "";
        if (!bucketPrefix.startsWith(requiredPrefix)) {
            reportViolation(`S3 bucket must use '${requiredPrefix}' prefix. Current prefix: '${bucketPrefix}'`);
        }
    }),
};

new PolicyPack("aws-typescript", {
    policies: [s3BucketPrefixPolicy],
});
