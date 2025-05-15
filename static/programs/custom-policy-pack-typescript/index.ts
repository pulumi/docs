import * as aws from "@pulumi/aws";
import { PolicyPack, ReportViolation, ResourceValidationArgs, validateResourceOfType, ResourceValidationPolicy } from "@pulumi/policy";

export const REQUIRED_S3_PREFIX: string = "myproduct-";

// Policy: Ensure S3 buckets have product prefix enabled
export const s3ProductPrefixPolicy: ResourceValidationPolicy = {
    name: "s3-product-prefix",
    description: "Ensures S3 buckets have the correct product prefix.",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.s3.BucketV2, (bucket, args, reportViolation) => {
        const prefix = bucket.bucketPrefix || "";
        if (prefix != REQUIRED_S3_PREFIX) {
            reportViolation(`Invalid prefix: '${prefix}'. S3 buckets must use '${REQUIRED_S3_PREFIX}' prefix.`);
        }
    }),
};

export const REQUIRED_INSTANCE_TYPE: string = "t2.micro";

// Policy: Restrict EC2 instance types
export const ec2InstanceTypeRestrictedPolicy: ResourceValidationPolicy = {
    name: "ec2-instance-type-restricted",
    description: "Ensures EC2 instances use approved instance type.",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.ec2.Instance, (instance, args, reportViolation) => {
        const instanceType = instance.instanceType || "";
        if (instanceType !== REQUIRED_INSTANCE_TYPE) {
            reportViolation(`Invalid instance type: '${instanceType}'. EC2 instances must use '${REQUIRED_INSTANCE_TYPE}' instance type.`);
        }
    }),
};

// Policy: Ensure all AWS resources have at least one tag
export const allAwsResourcesMustHaveTagsPolicy: ResourceValidationPolicy = {
    name: "all-aws-resources-must-have-tags",
    description: "Ensures all AWS resources have at least one tag.",
    enforcementLevel: "mandatory",
    validateResource: (args: ResourceValidationArgs, reportViolation: ReportViolation) => {
        if (args.type.startsWith("aws")) {
            const tags = args.props.tags || {};
            if (Object.keys(tags).length === 0) {
                reportViolation("All AWS resources must have at least one tag.");
            }
        }
    },
};

new PolicyPack("custom-policy-pack", {
    policies: [s3ProductPrefixPolicy, ec2InstanceTypeRestrictedPolicy, allAwsResourcesMustHaveTagsPolicy],
});
