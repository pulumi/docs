import pulumi
import pulumi_aws as aws
import json

stack_ref = pulumi.StackReference("my-org/my-first-program/dev")
lambda_arn = stack_ref.get_output("lambdaArn")

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

scheduler = aws.scheduler.Schedule("scheduler",
    flexible_time_window=aws.scheduler.ScheduleFlexibleTimeWindowArgs(
        mode="OFF",
    ),
    schedule_expression="rate(1 minutes)",
    target=aws.scheduler.ScheduleTargetArgs(
        arn=lambda_arn,
        role_arn=scheduler_role.arn,
    )
)