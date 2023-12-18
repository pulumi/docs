package main

import (
	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			SwaggerString: pulumi.String(`{
				"swagger": "2.0",
				"info": {
					"title": "example",
					"version": "1.0"
				},
				"paths": {
					"/": {
						"get": {
							"x-amazon-apigateway-integration": {
							"httpMethod": "GET",
							"passthroughBehavior": "when_no_match",
							"type": "http_proxy",
							"uri": "https://httpbin.org/uuid"
							}
						}
					}
				},
				"x-amazon-apigateway-binary-media-types": ["*/*"]
			}`),
		})
		if err != nil {
			return err
		}

		ctx.Export("url", api.Url)
		return nil
	})
}
