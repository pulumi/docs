package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create a Pulumi Config
		config := config.New(ctx, "")

		// Retrieve the value of "myEnvironment" and "myPassword"
		environment := config.Get("myEnvironment")
		password := config.GetSecret("myPassword")

		// Export values as outputs
		ctx.Export("Environment", pulumi.String(environment))
		ctx.Export("Password", pulumi.StringOutput(password))
		return nil
	})
}
