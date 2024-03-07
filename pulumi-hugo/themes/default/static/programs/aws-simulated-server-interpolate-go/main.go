package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		webServer := pulumi.ToOutput(&pulumi.StringMap{
			"hostName":  pulumi.String("www.mywebserver.com"),
			"ipAddress": pulumi.String("8080"),
		})

		url := pulumi.Sprintf("http://%s:%d/", webServer.hostName, webServer.port)

		ctx.Export("serverUrl", url)

		return nil
	})
}
