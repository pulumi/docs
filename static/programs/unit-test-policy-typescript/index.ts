import * as aws from "@pulumi/aws";

import { PolicyPack, validateResourceOfType, ResourceValidationPolicy } from "@pulumi/policy";

export const s3NoPublicReadPolicy: ResourceValidationPolicy = {
    name: "s3-no-public-read",
    description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
        if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
            reportViolation(
                "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html",
            );
        }
    }),
};

new PolicyPack("aws-typescript", {
    policies: [s3NoPublicReadPolicy],
});
