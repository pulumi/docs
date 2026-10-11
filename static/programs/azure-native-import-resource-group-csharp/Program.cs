using Pulumi;
using Pulumi.AzureNative.Resources;
using Pulumi.AzureNative.Authorization;

return await Pulumi.Deployment.RunAsync(async () =>
{
    var clientConfig = await GetClientConfig.InvokeAsync();
    var subscriptionId = clientConfig.SubscriptionId;
    var resourceGroupName = new Config().Get("resourceGroupName"); // REPLACE
    var lookupProp = $"/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}";

    var importedResourceGroup = new ResourceGroup("imported-rg", new(),
        new CustomResourceOptions { ImportId = lookupProp }
    );
});