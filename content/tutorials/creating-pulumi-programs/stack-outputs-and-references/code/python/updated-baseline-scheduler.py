import pulumi
import pulumi_aws as aws
import json

stack_ref = # TO-DO

lambda_arn = # TO-DO


# Gives the EventBridge Scheduler the ability to execute the Lambda function
scheduler_role = aws.iam.Role("scheduler_role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Principal": {
                    "Service": "scheduler.amazonaws.com"
                },
                "Effect": "Allow",
                "Sid": ""
            }
        ]
    }""",
    inline_policies=[
        aws.iam.RoleInlinePolicyArgs(
            name="my_inline_policy",
            policy=json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Action": ["lambda:*"],
                    "Effect": "Allow",
                    "Resource": "*" ,
                }],
            })
        )
    ]
)

scheduler = # TO-DO