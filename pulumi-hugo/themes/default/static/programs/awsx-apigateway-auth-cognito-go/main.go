package main

import (
	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/cognito"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		userPool, err := cognito.NewUserPool(ctx, "user-pool", nil)
		if err != nil {
			return err
		}

		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			Routes: []apigateway.RouteArgs{
				{
					Path:      "/",
					LocalPath: pulumi.StringRef("www"),
					Authorizers: []apigateway.AuthorizerArgs{
						{
							ParameterName:  "Authorization",
							IdentitySource: []string{"method.request.header.Authorization"},
							ProviderARNs: []pulumi.StringInput{
								userPool.Arn,
							},
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
