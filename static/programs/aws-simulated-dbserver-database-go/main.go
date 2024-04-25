package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		sqlServer := pulumi.ToOutput(&pulumi.StringMap{
			"name":      pulumi.String("myDbServer"),
			"ipAddress": pulumi.String("10.0.0.0/24"),
		})

		database := pulumi.ToOutput(&pulumi.StringMap{
			"name":   pulumi.String("myExampleDatabase"),
			"engine": pulumi.String("sql-db"),
		})

		ctx.Export("sqlServerName", sqlServer.ApplyT(func(values map[string]string) string {
			return values["name"]
		}))

		ctx.Export("databaseName", database.ApplyT(func(values map[string]string) string {
			return values["name"]
		}))

		return nil
	})
}
