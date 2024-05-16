import json
import pulumi
import pulumi_aws as aws
import pulumi_aws_apigateway as apigateway

# An execution role to use for the Lambda function.
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

# A Lambda function to invoke.
handler = aws.lambda_.Function(
    "handler",
    runtime="python3.9",
    handler="handler.handler",
    role=role.arn,
    code=pulumi.FileArchive("./function"),
)

# A REST API to route requests to the Lambda function.
api = apigateway.RestAPI(
    "api",
    routes=[
        apigateway.RouteArgs(
            path="/", method=apigateway.Method.GET, event_handler=handler
        )
    ],
)

# The URL at which the REST API will be served.
pulumi.export("url", api.url)
