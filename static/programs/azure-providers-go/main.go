package main

import (
	"github.com/pulumi/pulumi-azure-native-sdk/resources/v2"
	"github.com/pulumi/pulumi-azuread/sdk/v4/go/azuread"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a resource group using the Azure Native provider.
		resourceGroup, err := resources.NewResourceGroup(ctx, "my-resource-group", &resources.ResourceGroupArgs{
			Location: pulumi.String("eastus"),
		})
		if err != nil {
			return err
		}

		// Create an Entra ID application registration using the Azure AD provider.
		application, err := azuread.NewApplication(ctx, "my-application", &azuread.ApplicationArgs{
			DisplayName: pulumi.String("my-application"),
		})
		if err != nil {
			return err
		}

		// Create a service principal for the application.
		servicePrincipal, err := azuread.NewServicePrincipal(ctx, "my-service-principal", &azuread.ServicePrincipalArgs{
			ClientId: application.ClientId,
		})
		if err != nil {
			return err
		}

		ctx.Export("resourceGroupName", resourceGroup.Name)
		ctx.Export("applicationClientId", application.ClientId)
		ctx.Export("servicePrincipalId", servicePrincipal.ID())
		return nil
	})
}
