package main

import (
	"fmt"
    
    "github.com/pulumi/pulumi-gcp/sdk/v6/go/gcp/serviceaccount"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
        conf := config.New(ctx, "gcp")
        projectId := conf.Require("project")
        
        serviceAcctEmailSuffix := fmt.Sprintf("@%s.iam.gserviceaccount.com", projectId)
        serviceAcctDisplayName := "pulumi-tutorial-service-account" // REPLACE
        serviceAcctEmailPrefix := "pulumi-tutorial-service-accoun" // REPLACE

        _, err := serviceaccount.NewAccount(ctx, "imported-tutorial-service-account", 
            &serviceaccount.AccountArgs{
                AccountId:   pulumi.String(serviceAcctEmailPrefix),
                DisplayName: pulumi.String(serviceAcctDisplayName),
                Project:    pulumi.String(projectId),
            },
            pulumi.Import(pulumi.ID(fmt.Sprintf("%s%s", serviceAcctEmailPrefix, serviceAcctEmailSuffix))),
        )
        if err != nil {
            return err
        }
        
        return nil
    })
}
