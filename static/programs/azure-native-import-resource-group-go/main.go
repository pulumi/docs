package main

import (
    "fmt"
    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/authorization"
    "github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        clientConfig, err := authorization.GetClientConfig(ctx, nil)
        if err != nil {
            return err
        }

        conf := config.New(ctx, "")
        resourceGroupName := conf.Require("resourceGroupName") // REPLACE
        lookupProp := fmt.Sprintf("/subscriptions/%s/resourceGroups/%s", clientConfig.SubscriptionId, resourceGroupName)

        _, err = resources.NewResourceGroup(ctx, "imported-rg", &resources.ResourceGroupArgs{}, 
			pulumi.Import(pulumi.ID(lookupProp)))
        if err != nil {
            return err
        }
        return nil
    })
}