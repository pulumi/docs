package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a Pulumi Config
		config := config.New(ctx, "")

		// Retrieve the value of "region" and "apiKey"
		region := config.Get("region")
		apiKey := config.GetSecret("apiKey")

		// Export values as outputs
		ctx.Export("Region", pulumi.String(region))
		ctx.Export("ApiKey", pulumi.StringOutput(apiKey))
		return nil
	})
}
