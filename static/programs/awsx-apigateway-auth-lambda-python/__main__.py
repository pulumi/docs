import json
import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

role = aws.iam.Role(
    "role",
    assume_role_policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com",
                    },
                }
            ],
        }
    ),
    managed_policy_arns=[aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE],
)

authorizer = aws.lambda_.Function(
    "authorizer",
    runtime="python3.9",
    handler="handler.handler",
    role=role.arn,
    code=pulumi.FileArchive("./authorizer"),
)

api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/",
            method=apigateway.Method.GET,
            local_path="www",
            authorizers=[
                apigateway.AuthorizerArgs(
                    auth_type="custom",
                    type="request",
                    parameter_name="Authorization",
                    identity_source=["method.request.header.Authorization"],
                    handler=authorizer,
                ),
            ],
        ),
    ],
)

pulumi.export("url", api.url)
