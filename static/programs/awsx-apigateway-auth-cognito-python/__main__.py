import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

user_pool = aws.cognito.UserPool("user-pool")

api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/",
            method=apigateway.Method.GET,
            local_path="www",
            authorizers=apigateway.AuthorizerArgs(
                parameter_name="Authorization",
                identity_source=["method.request.header.Authorization"],
                provider_arns=[user_pool.arn],
            ),
        )
    ],
)

pulumi.export("url", api.url)
