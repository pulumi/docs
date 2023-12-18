package main

import (
	"github.com/pulumi/pulumi-aws-apigateway/sdk/v2/go/apigateway"
	awsapigateway "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/apigateway"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		HEADER := apigateway.APIKeySourceHEADER
		api, err := apigateway.NewRestAPI(ctx, "api", &apigateway.RestAPIArgs{
			ApiKeySource: &HEADER,
			Routes: []apigateway.RouteArgs{
				{
					Path:           "/",
					LocalPath:      pulumi.StringRef("data"),
					Index:          pulumi.String("index.json"),
					ContentType:    pulumi.StringRef("application/json"),
					ApiKeyRequired: pulumi.BoolRef(true),
				},
			},
		})
		if err != nil {
			return err
		}

		key, err := awsapigateway.NewApiKey(ctx, "key", nil)
		if err != nil {
			return err
		}

		apiID := api.Api.ApplyT(func(api *awsapigateway.RestApi) pulumi.StringOutput {
			return api.ID().ToStringOutput()
		}).ApplyT(func(id interface{}) string {
			return id.(string)
		}).(pulumi.StringOutput)

		plan, err := awsapigateway.NewUsagePlan(ctx, "plan", &awsapigateway.UsagePlanArgs{
			ApiStages: awsapigateway.UsagePlanApiStageArray{
				&awsapigateway.UsagePlanApiStageArgs{
					ApiId: apiID,
					Stage: api.Stage.StageName(),
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = awsapigateway.NewUsagePlanKey(ctx, "plan-key", &awsapigateway.UsagePlanKeyArgs{
			KeyId:       key.ID(),
			KeyType:     pulumi.String("API_KEY"),
			UsagePlanId: plan.ID(),
		})
		if err != nil {
			return err
		}

		ctx.Export("url", api.Url)
		ctx.Export("apiKey", key.Value)
		return nil
	})
}
