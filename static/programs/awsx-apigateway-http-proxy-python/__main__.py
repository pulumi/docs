import pulumi
import pulumi_aws_apigateway as apigateway

api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/",
            method=apigateway.Method.GET,
            target=apigateway.TargetArgs(
                type="http_proxy",
                uri="https://www.example.com/",
            ),
        ),
    ],
)

pulumi.export("url", api.url)
