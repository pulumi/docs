"use strict";
const pulumi = require("@pulumi/pulumi");
const gcp = require("@pulumi/gcp");

const config = new pulumi.Config("gcp");
const projectId = config.require("project");

const serviceAcctEmailSuffix = `@${projectId}.iam.gserviceaccount.com`;
const serviceAcctDisplayName = "pulumi-tutorial-service-account"; // REPLACE
const serviceAcctEmailPrefix = "pulumi-tutorial-service-accoun"; // REPLACE

const importedTutorialServiceAccount = new gcp.serviceaccount.Account(
    "imported-tutorial-service-account",
    {
        accountId: serviceAcctEmailPrefix,
        displayName: serviceAcctDisplayName,
        project: projectId,
    },
    {
        import: `${serviceAcctEmailPrefix}${serviceAcctEmailSuffix}`,
    },
);
