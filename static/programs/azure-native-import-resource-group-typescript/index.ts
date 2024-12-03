import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure-native";
import * as resources from "@pulumi/azure-native/resources";

async function createResourceGroup() {
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
