def handler(event, context):

    effect = "Allow" if event["headers"]["Authorization"] == "token a-good-token" else "Deny"

    return {
        "principalId": "my-user",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": effect,
                    "Resource": event["methodArn"],
                },
            ],
        },
    }
