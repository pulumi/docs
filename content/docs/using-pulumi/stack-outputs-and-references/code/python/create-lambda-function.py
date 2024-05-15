import pulumi
import pulumi_aws as aws

# [Step 1: Create an S3 bucket.]
bucket = aws.s3.Bucket('my-bucket')

# [Step 2: Create a Lambda function.]

lambda_role = aws.iam.Role("s3-writer-role",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                },
                "Effect": "Allow",
                "Sid": ""
            }
        ]
    }""",
    managed_policy_arns=["arn:aws:iam::aws:policy/AmazonS3FullAccess"]
)

lambda_function = aws.lambda_.Function(
    resource_name='s3-writer-lambda-function',
    role=lambda_role.arn,
    runtime="python3.10",
    handler="lambda_function.lambda_handler",
    code=pulumi.AssetArchive({
        '.': pulumi.FileArchive('./s3_writer')
    }),
    timeout=15,
    memory_size=128,
    environment= { 
        "variables": {
            "BUCKET_NAME": bucket.id
        }
    }
)

# [Step 3: Create an export.]
# TO-DO