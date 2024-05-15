import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

api = apigateway.RestAPI(
    "api",
    apigateway.RestAPIArgs(
        api_key_source=apigateway.APIKeySource.HEADER,
        routes=[
            apigateway.RouteArgs(
                path="/",
                method=apigateway.Method.GET,
                local_path="data",
                index="index.json",
                content_type="application/json",
                api_key_required=True,
            ),
        ],
    )
)

key = aws.apigateway.ApiKey("key")

plan = aws.apigateway.UsagePlan("plan", aws.apigateway.UsagePlanArgs(
    api_stages=[
        aws.apigateway.UsagePlanApiStageArgs(
            api_id=api.api.id,
            stage=api.stage.stage_name,
        ),
    ],
))

plan_key = aws.apigateway.UsagePlanKey("plan-key", aws.apigateway.UsagePlanKeyArgs(
    key_id=key.id,
    key_type="API_KEY",
    usage_plan_id=plan.id,
))

pulumi.export("url", api.url)
pulumi.export("apiKey", key.value)
