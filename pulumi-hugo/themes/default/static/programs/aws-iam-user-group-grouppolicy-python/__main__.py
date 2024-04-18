import json
import pulumi_aws as aws

# Create our users.
jane = aws.iam.User('jane')
mary = aws.iam.User('mary')

# Define a group and assign a policy for it.
devs = aws.iam.Group('devs',
    path='/users/',
)
my_developer_policy = aws.iam.GroupPolicy('my_developer_policy',
    group=devs.id,
    policy=json.dumps({
        'Version': '2012-10-17',
        'Statement': [{
            'Action': [ 'ec2:Describe*' ],
            'Effect': 'Allow',
            'Resource': '*',
        }],
    }),
)

# Finally add the users as members to this group.
dev_team = aws.iam.GroupMembership('dev-team',
    group=devs.id,
    users=[ jane.id, mary.id ],
)
