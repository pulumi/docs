import json
import pulumi_aws as aws

role = aws.iam.Role('my-role',
    assume_role_policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Action': 'sts:AssumeRole',
            'Principal': {
                'Service': 'ec2.amazonaws.com'
            },
            'Effect': 'Allow',
        }],
    }),
)

role_policy_attachment = aws.iam.RolePolicyAttachment('my-rpa',
    role=role.id,
    policy_arn=aws.iam.ManagedPolicy.IAM_READ_ONLY_ACCESS,
)
