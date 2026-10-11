using System.Collections.Generic;
using Pulumi;
using AzureNative = Pulumi.AzureNative;
using AzureAD = Pulumi.AzureAD;

return await Deployment.RunAsync(() =>
{
    // Create a resource group using the Azure Native provider.
    var resourceGroup = new AzureNative.Resources.ResourceGroup("my-resource-group", new()
    {
        Location = "eastus",
    });

    // Create an Entra ID application registration using the Azure AD provider.
    var application = new AzureAD.Application("my-application", new()
    {
        DisplayName = "my-application",
    });

    // Create a service principal for the application.
    var servicePrincipal = new AzureAD.ServicePrincipal("my-service-principal", new()
    {
        ClientId = application.ClientId,
    });

    return new Dictionary<string, object?>
    {
        ["resourceGroupName"] = resourceGroup.Name,
        ["applicationClientId"] = application.ClientId,
        ["servicePrincipalId"] = servicePrincipal.Id,
    };
});
