import json
import pulumi_aws as aws

user = aws.iam.User('webmaster',
    path='/system/',
    tags={ 'Name': 'webmaster' },
)
user_access_key = aws.iam.AccessKey('webmasterKey',
    user=user.name,
)
user_policy = aws.iam.UserPolicy('webmasterPolicy',
    user=user.id,
    policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Action': [ 'ec2:Describe*' ],
            'Effect': 'Allow',
            'Resource': '*'
        }],
    }),
)