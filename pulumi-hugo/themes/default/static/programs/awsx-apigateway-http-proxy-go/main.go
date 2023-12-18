package main

import (
	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			Routes: []apigateway.RouteArgs{
				{
					Path: "/",
					Target: &apigateway.TargetArgs{
						Type: apigateway.IntegrationType_Http_proxy,
						Uri:  pulumi.String("https://www.example.com/"),
					},
				},
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("url", api.Url)
		return nil
	})
}
