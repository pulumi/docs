"use strict";
const pulumi = require("@pulumi/pulumi");
const azure = require("@pulumi/azure-native");
const resources = require("@pulumi/azure-native/resources");

async function importResourceGroup() {
    const clientConfig = await azure.authorization.getClientConfig();
    const subscriptionId = clientConfig.subscriptionId;
    const resourceGroupName = new pulumi.Config().get("resourceGroupName"); // REPLACE
    const lookupProp = `/subscriptions/${subscriptionId}/resourceGroups/${resourceGroupName}`;

    const importedResourceGroup = new resources.ResourceGroup(
        "imported-rg",
        {},
        {
            import: lookupProp,
        },
    );

    return importedResourceGroup;
}
