import pulumi
import pulumi_aws_apigateway as apigateway

api = apigateway.RestAPI(
    "api",
    apigateway.RestAPIArgs(
        request_validator=apigateway.RequestValidator.PARAM_S_ONLY,
        routes=[
            apigateway.RouteArgs(
                path="/search",
                method=apigateway.Method.GET,
                target=apigateway.TargetArgs(
                    type="http_proxy",
                    uri="https://www.example.com/",
                ),
                request_validator=apigateway.RequestValidator.ALL,
                required_parameters=[
                    apigateway.RequiredParameterArgs(
                        name="q",
                        in_="query",
                    ),
                ],
            ),
        ],
    )

)

pulumi.export("url", api.url)
