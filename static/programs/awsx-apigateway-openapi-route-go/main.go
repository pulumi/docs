package main

import (
	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		GET := apigateway.MethodGET
		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			Routes: []apigateway.RouteArgs{
				{
					Path:   "/",
					Method: &GET,
					Data: map[string]interface{}{
						"x-amazon-apigateway-integration": map[string]interface{}{
							"httpMethod":          "GET",
							"passthroughBehavior": "when_no_match",
							"type":                "http_proxy",
							"uri":                 "https://httpbin.org/uuid",
						},
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
