package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lambda"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		policy, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Principal": map[string]interface{}{
						"Service": "lambda.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}

		role, err := iam.NewRole(ctx, "role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(policy),
			ManagedPolicyArns: pulumi.StringArray{
				iam.ManagedPolicyAWSLambdaBasicExecutionRole,
			},
		})
		if err != nil {
			return err
		}

		authorizer, err := lambda.NewFunction(ctx, "authorizer", &lambda.FunctionArgs{
			Runtime: pulumi.String("python3.9"),
			Handler: pulumi.String("handler.handler"),
			Role:    role.Arn,
			Code:    pulumi.NewFileArchive("./authorizer"),
		})
		if err != nil {
			return err
		}

		methodGET := apigateway.MethodGET
		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			Routes: []apigateway.RouteArgs{
				{
					Path:      "/",
					Method:    &methodGET,
					LocalPath: pulumi.StringRef("www"),
					Authorizers: []apigateway.AuthorizerArgs{
						{
							AuthType:       pulumi.StringRef("custom"),
							Type:           pulumi.StringRef("request"),
							ParameterName:  "Authorization",
							IdentitySource: []string{"method.request.header.Authorization"},
							Handler:        authorizer,
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
