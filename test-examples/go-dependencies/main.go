// Go example showing cross-cloud dependencies
package main

import (
	"fmt"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lambda"
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/resources"
	"github.com/pulumi/pulumi-azure-native/sdk/go/azure/sql"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create Azure resource group first
		azureRg, err := resources.NewResourceGroup(ctx, "data-rg", &resources.ResourceGroupArgs{
			Location: pulumi.String("eastus"),
		})
		if err != nil {
			return err
		}

		// Create Azure SQL Server (simplified - normally would need more config)
		sqlServer, err := sql.NewServer(ctx, "sql-server", &sql.ServerArgs{
			ResourceGroupName: azureRg.Name,
			Location:          azureRg.Location,
			AdministratorLogin:         pulumi.String("adminuser"),
			AdministratorLoginPassword: pulumi.String("P@ssw0rd123!"),
		})
		if err != nil {
			return err
		}

		// Azure SQL Database created first
		azureDb, err := sql.NewDatabase(ctx, "main-db", &sql.DatabaseArgs{
			ResourceGroupName: azureRg.Name,
			ServerName:        sqlServer.Name,
			Location:          azureRg.Location,
			Sku: &sql.SkuArgs{
				Name: pulumi.String("S0"),
			},
		})
		if err != nil {
			return err
		}

		// AWS Lambda depends on Azure database
		// Pulumi automatically handles this cross-cloud dependency
		lambdaFunc, err := lambda.NewFunction(ctx, "processor", &lambda.FunctionArgs{
			Runtime: pulumi.String("go1.x"),
			Handler: pulumi.String("main"),
			Code:    pulumi.NewAssetArchive(map[string]interface{}{"main.go": pulumi.NewStringAsset("package main\nfunc main() {}")}),
			Role:    pulumi.String("arn:aws:iam::123456789012:role/lambda-role"), // Simplified
			Environment: &lambda.FunctionEnvironmentArgs{
				Variables: pulumi.StringMap{
					// This creates an explicit dependency
					"DB_CONNECTION": azureDb.ID().ApplyT(func(id string) string {
						return fmt.Sprintf("Server=%s.database.windows.net", id)
					}).(pulumi.StringOutput),
				},
			},
		})
		if err != nil {
			return err
		}

		// Export both resources
		ctx.Export("azureDatabaseId", azureDb.ID())
		ctx.Export("lambdaArn", lambdaFunc.Arn)

		return nil
	})
}