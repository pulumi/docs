import { PolicyPack, validateResourceOfType, ResourceValidationArgs, ReportViolation } from "@pulumi/policy";

new PolicyPack("multi-cloud-compliance", {
    policies: [
        {
            name: "required-tags",
            description: "All resources must have required tags",
            enforcementLevel: "mandatory",
            validateResource: (args: ResourceValidationArgs, reportViolation: ReportViolation) => {
                const requiredTags = ["Environment", "Owner", "CostCenter"];
                
                // Check AWS resources
                if (args.type.startsWith("aws:")) {
                    const tags = args.props.tags || {};
                    requiredTags.forEach(tag => {
                        if (!tags[tag]) {
                            reportViolation(`Missing required tag: ${tag}`);
                        }
                    });
                }
                
                // Check Azure resources (same tag format)
                if (args.type.startsWith("azure-native:")) {
                    const tags = args.props.tags || {};
                    requiredTags.forEach(tag => {
                        if (!tags[tag]) {
                            reportViolation(`Missing required tag: ${tag}`);
                        }
                    });
                }
                
                // Check GCP resources (uses 'labels')
                if (args.type.startsWith("gcp:")) {
                    const labels = args.props.labels || {};
                    requiredTags.forEach(tag => {
                        const gcpLabel = tag.toLowerCase().replace(/([A-Z])/g, "_$1");
                        if (!labels[gcpLabel]) {
                            reportViolation(`Missing required label: ${gcpLabel}`);
                        }
                    });
                }
            },
        },
        {
            name: "encryption-required",
            description: "All storage must be encrypted",
            enforcementLevel: "mandatory",
            validateResource: (args: ResourceValidationArgs, reportViolation: ReportViolation) => {
                // Unified encryption checks across all providers
                if (args.type === "aws:s3/bucket:Bucket") {
                    if (!args.props.serverSideEncryptionConfiguration) {
                        reportViolation("S3 bucket must have encryption enabled");
                    }
                }
                if (args.type === "azure-native:storage:StorageAccount") {
                    if (!args.props.encryption?.services?.blob?.enabled) {
                        reportViolation("Azure Storage must have encryption enabled");
                    }
                }
                // GCP encrypts by default, but we can check for CMEK if required
            },
        },
    ],
});