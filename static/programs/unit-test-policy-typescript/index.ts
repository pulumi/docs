import * as aws from "@pulumi/aws";

import { PolicyPack, validateResourceOfType, ResourceValidationPolicy } from "@pulumi/policy";

export const rdsStorageEncryptionPolicy: ResourceValidationPolicy = {
    name: "rds-storage-encryption",
    description: "Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.rds.Instance, (instance, args, reportViolation) => {
        // Exempt instances explicitly tagged as non-production data.
        if (instance.tags?.["data-classification"] === "non-production") {
            return;
        }
        if (!instance.storageEncrypted) {
            reportViolation(
                "RDS instance must have storage encryption enabled " +
                "(or be tagged 'data-classification=non-production').");
        }
    }),
};

new PolicyPack("aws-typescript", {
    policies: [rdsStorageEncryptionPolicy],
});
