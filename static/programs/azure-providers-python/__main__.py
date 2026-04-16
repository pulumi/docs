import pulumi
import pulumi_azuread as azuread
import pulumi_azure_native.resources as resources

# Create a resource group using the Azure Native provider.
resource_group = resources.ResourceGroup("my-resource-group",
    location="eastus",
)

# Create an Entra ID application registration using the Azure AD provider.
application = azuread.Application("my-application",
    display_name="my-application",
)

# Create a service principal for the application.
service_principal = azuread.ServicePrincipal("my-service-principal",
    client_id=application.client_id,
)

pulumi.export("resourceGroupName", resource_group.name)
pulumi.export("applicationClientId", application.client_id)
pulumi.export("servicePrincipalId", service_principal.id)
