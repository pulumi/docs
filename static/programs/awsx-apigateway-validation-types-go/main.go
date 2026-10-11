package main

import (
	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		GET := apigateway.MethodGET
		ALL := apigateway.RequestValidatorALL
		PARAMS_ONLY := apigateway.RequestValidator_PARAMS_ONLY

		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			RequestValidator: &PARAMS_ONLY,

			Routes: []apigateway.RouteArgs{
				{
					Path:   "/search",
					Method: &GET,
					Target: &apigateway.TargetArgs{
						Type: apigateway.IntegrationType_Http_proxy,
						Uri:  pulumi.String("https://www.example.com/"),
					},
					RequestValidator: &ALL,
					RequiredParameters: []apigateway.RequiredParameterArgs{
						{
							Name: pulumi.StringPtr("q"),
							In:   pulumi.StringPtr("query"),
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
