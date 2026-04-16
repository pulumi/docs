import * as pulumi from "@pulumi/pulumi";
import * as azuread from "@pulumi/azuread";
import * as resources from "@pulumi/azure-native/resources";

// Create a resource group using the Azure Native provider.
const resourceGroup = new resources.ResourceGroup("my-resource-group", {
    location: "eastus",
});

// Create an Entra ID application registration using the Azure AD provider.
const application = new azuread.Application("my-application", {
    displayName: "my-application",
});

// Create a service principal for the application.
const servicePrincipal = new azuread.ServicePrincipal("my-service-principal", {
    clientId: application.clientId,
});

export const resourceGroupName = resourceGroup.name;
export const applicationClientId = application.clientId;
export const servicePrincipalId = servicePrincipal.id;
