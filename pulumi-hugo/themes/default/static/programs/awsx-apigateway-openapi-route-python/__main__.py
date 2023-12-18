import pulumi
import pulumi_aws_apigateway as apigateway

api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/",
            method=apigateway.Method.GET,
            data={
                "x-amazon-apigateway-integration": {
                    "httpMethod": "GET",
                    "passthroughBehavior": "when_no_match",
                    "type": "http_proxy",
                    "uri": "https://httpbin.org/uuid",
                },
            },
        ),
    ],
)

pulumi.export("url", api.url)
