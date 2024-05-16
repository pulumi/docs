import json
import pulumi
import pulumi_aws as aws
import pulumi_aws_native as aws_native

lambda_role = aws.iam.Role("lambda-role", 
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com",
            },
        }],
    }),
    managed_policy_arns=[aws.iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE])

sfn_role = aws.iam.Role("sfn-role", 
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "states.amazonaws.com",
            },
        }],
    }),
    managed_policy_arns=["arn:aws:iam::aws:policy/AWSLambda_FullAccess"])

hello_function = aws.lambda_.Function("hello-function",
    runtime="python3.9",
    handler="handler.handler",
    role=lambda_role.arn,
    code=pulumi.FileArchive("./function"))

state_machine = aws_native.stepfunctions.StateMachine("stateMachine",
    role_arn=sfn_role.arn,
    state_machine_type="EXPRESS",
    definition_string=pulumi.Output.json_dumps({ # converts JSON into string
        "Comment": "A Hello World example of the Amazon States Language using an AWS Lambda Function",
        "StartAt": "Hello",
        "States": {
            "Hello": {
                "Type": "Task",
                "Resource": hello_function.arn, # unwraps Pulumi resource Output
                "Next": True
            }
        },
    })
)