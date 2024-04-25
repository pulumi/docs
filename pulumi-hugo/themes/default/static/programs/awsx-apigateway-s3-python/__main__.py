import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/",
            method=apigateway.Method.GET,
            local_path="www",
        )
    ],
)

pulumi.export("url", api.url)
