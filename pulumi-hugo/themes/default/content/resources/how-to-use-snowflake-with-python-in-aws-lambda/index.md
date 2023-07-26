---
title: "How to use Snowflake with Python in AWS Lambda"
allow_long_title: true
meta_desc: "Use Pulumi with Snowflake and AWS Lambda with Python via our guide. Perfect for developers integrating Snowflake into serverless workloads."
type: ai-answers
date: 2023-07-24
---

To accomplish your goal, you need to interact with Snowflake from a Lambda function. AWS Lambda does not provide out-of-the-box support for Snowflake. So, you need to manage the interaction with Snowflake from Python code.

We can create a program that achieves your goal by configuring Snowflake resources such as a Pipe and a Warehouse, coupled with AWS resources like aws.lambda.Function and optionally aws.cloudtrail.Trail.

A Snowflake Pipe can get the Snowflake to ingest data into internal Snowflake tables, that can be queried via AWS Lambda. We'll use aws.lambda.Function to deploy a Python-based AWS Lambda function that can connect to Snowflake for running any necessary queries.

Here's the Pulumi program skeleton that reflects our direction:

```python
import pulumi
from pulumi_snowflake import pipe, warehouse
from pulumi_aws import lambda_, iam

# Create an IAM role that will be used by the Lambda function
lambda_role = iam.Role('lambdaRole', assume_role_policy={{
    "Version": "2012-10-17",
    "Statement": [{{
        "Action": "sts:AssumeRole",
        "Principal": {{
            "Service": "lambda.amazonaws.com"
        }},
        "Effect": "Allow",
    }}]
}})

# The policy that is being passed to AWS Lambda Execution Role
_role_policy = iam.RolePolicyAttachment(
    'lambdaRolePolicy',
    role=lambda_role.id,
    policy_arn='arn:aws:iam::aws:policy/service-role/AWSLambdaVPCAccessExecutionRole'
)

# Python AWS Lambda function that connects to Snowflake to run necessary queries
lambda_function = lambda_.Function(
    'lambdaFunction',
    code=pulumi.AssetArchive({{
        '.': pulumi.FileArchive('./lambda_handler_dir')
    }}),
    role=lambda_role.arn,
    handler='lambda_handler.handler',
    runtime='python3.8'
)

# Snowflake resources
warehouse_ = warehouse.Warehouse(
    'warehouse',
    name='test_warehouse',
    warehouse_size='X-Small'
)

pipe_ = pipe.Pipe(
    'pipe',
    auto_ingest=False,
    database='<>',
    copy_statement='COPY into <table>',
    name='test_pipe',
    schema='<schema>'
)

pulumi.export('LambdaFunctionName', lambda_function.name)
pulumi.export('SnowflakePipeName', pipe_.name)
pulumi.export('SnowflakeWarehouseName', warehouse_.name)
```

In this example, we create a Snowflake pipe and a warehouse as well as an AWS Lambda function that's written in Python. The Lambda function's job would be to connect to Snowflake and run necessary SQL queries.

This is a simplified version and does not fully account for security hardening, nor does it provide the details of the Python function you would write to interact with Snowflake.

Please replace '_name', 'table', 'schema' with the actual values you would use.

The section of most interest to you would be the Python code for AWS Lambda function which does not have the necessary Python libraries to interact with Snowflake, nor does it contain logic to interact with Snowflake.

The Python function would end up in a directory, in this instance ./lambda_handler_dir. The handler file in this case should be named lambda_handler.py, thus making the Python handler method lambda_handler.handler.

You may refer to the following Pulumi Registry links for further details on used resources:

* [snowflake.Pipe](https://www.pulumi.com/registry/packages/snowflake/api-docs/pipe/)
* [snowflake.Warehouse](https://www.pulumi.com/registry/packages/snowflake/api-docs/warehouse/)
* [aws.lambda.Function](https://www.pulumi.com/registry/packages/aws/api-docs/lambda/function/)