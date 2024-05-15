---
title: "GPT Your IaC"
layout: challenge/single
description: |
    Use Pulumi AI to generate the most interesting or sophisticated architecture possible
meta_desc: |
    Use Pulumi AI to generate the most interesting or sophisticated architecture possible
meta_image: /images/challenge/challenge-ai-meta.png
banner_image: /images/challenge/challenge-ai-banner.png
hubspot_form_id: 1pC3zwQ3ET8ijTyGxv0W2Zg2mxud
---

<h1 class="font-display text-6xl">GPT Your IaC Challenge!</h1>

## What you will learn

Why write your Pulumi programs yourself when you can have AI do it for you? Pulumi AI leverages large language models (LLMs) to author infrastructure as code for any architecture for any cloud in any language.

For the **GPT Your IaC Challenge**, your goal is to have Pulumi AI write a Pulumi program for any architecture you want and run a successful `pulumi up` with the program created. To participate in the challenge, you'll need to either visit [pulumi.com/ai](/ai) or download the [CLI](https://github.com/pulumi/pulumi-ai) so you can use Pulumi AI.

We will send you limited edition swag for completion of the challenge. We will also send you an even better piece of swag if you document this via a blog post, social media, or video. Tag us on social media or email us at [da@pulumi.com](mailto:da@pulumi.com), and we will help spread the word about your experience. All submissions will be judged at the end of the challenge, and the best submissions (there will be a few categories) will receive a special prize.

## Prerequisites

The challenge utilizes whatever cloud and whatever language you choose to ask Pulumi AI to write for you. Pulumi AI will do all the heavy lifting! However, in order to complete this challenge, you will need a couple things set up in advance.

- A [Pulumi account](https://app.pulumi.com/signup)
- The [Pulumi CLI](/docs/install/)
- Pulumi AI
- Cloud accounts
- OpenAI API Key

## An Example of Doing the Challenge

### Step 1. Go to Pulumi AI Website

There are two ways to complete this challenge: using the Pulumi AI website or the CLI. For this example of doing the challenge, we used the Pulumi AI website to generate a Pulumi program, and then used the Pulumi CLI to run the generated program. If you plan to use the CLI, though, you will need to export your cloud provider (we'll use AWS in this example) and OpenAI credentials. To access your OpenAI credentials, go to [__API Keys__ tab](https://platform.openai.com/account/api-keys) in the OpenAI platform console. Then click `Create new secret key` .

```shell
export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY_ID>
export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_ACCESS_KEY>
export OPENAI_API_KEY=<YOUR_API_KEY>
```

To begin the challenge, first navigate to [pulumi.com/ai](/ai).

![alt_text](/images/challenge/AIStep1.png "navigate to Pulumi AI website")

### Step 2. Generate Program

Next, you will use Pulumi AI to generate a program that will provision cloud infrastructure. In this example, we asked Pulumi AI to create some database infrastructure that will be used for a real-time application that generates lots of data. Using the chat widget on the Pulumi AI page, describe the infrastructure you would like to build. In our case, we supplied: `Deploy a Kinesis Data Stream, RDS database, DynamoDB database, and Timestream database.`

Pulumi AI returned to us the code below:

```python
import pulumi
import pulumi_aws as aws

# Create a VPC security group
security_group = aws.ec2.SecurityGroup("mySecurityGroup",
    description="Allow inbound connections",
    ingress=[
        {"protocol": "tcp", "from_port": 3306, "to_port": 3306, "cidr_blocks": ["0.0.0.0/0"]},
    ],
)

# Create a Kinesis Data Stream
kinesis_stream = aws.kinesis.Stream("myDataStream",
    shard_count=1
)

# Create an RDS Instance (MySQL)
rds_instance = aws.rds.Instance("my-rds-example",
    engine="mysql",
    engine_version="5.7",
    instance_class="db.t2.micro",
    allocated_storage=20,
    storage_type="gp2",
    username="master",
    password="examplePassword!",
    vpc_security_group_ids=[
        security_group.id,
    ],
    publicly_accessible=True,
    skip_final_snapshot=True
)

# Create a DynamoDB Table
dynamodb_table = aws.dynamodb.Table("myDynamoDBTable",
    attributes=[
        {
            "name": "id",
            "type": "S",
        },
    ],
    hash_key="id",
    read_capacity=5,
    write_capacity=5
)

# Create a Timestream Database
timestream_database = aws.timestreamwrite.Database("myTimestreamDB")

# Stack exports
pulumi.export("kinesisStreamArn", kinesis_stream.arn)
pulumi.export("rdsInstanceEndpoint", rds_instance.endpoint)
pulumi.export("dynamodbTableArn", dynamodb_table.arn)
pulumi.export("timestreamDatabaseArn", timestream_database.arn)
```

### Step 3. Execute Generated Pulumi Program

Now that you have a generated Pulumi program, you will create a new Pulumi program to run the program. Create a new directory and a new Pulumi python project.

```shell
mkdir ai-challenge && cd ai-challenge
pulumi new aws-python
```

Copy the Pulumi AI generated program into `__main__.py`. Save the program and then run `pulumi up`. If your `pulumi up` operation succeeds, then you're done! (Maybe try it again with something more complex?) In our case, there was an error:

```shell
Diagnostics:
  pulumi:pulumi:Stack (ai-challenge-dev):
    error: Program failed with an unhandled exception:
    Traceback (most recent call last):
      File "/home/kao/code/test-folder/ai-challenge/./__main__.py", line 47, in <module>
        timestream_database = aws.timestreamwrite.Database("myTimestreamDB")
      File "/home/kao/code/test-folder/ai-challenge/venv/lib/python3.8/site-packages/pulumi_aws/timestreamwrite/database.py", line 290, in __init__
        __self__._internal_init(resource_name, *args, **kwargs)
      File "/home/kao/code/test-folder/ai-challenge/venv/lib/python3.8/site-packages/pulumi_aws/timestreamwrite/database.py", line 309, in _internal_init
        raise TypeError("Missing required property 'database_name'")
    TypeError: Missing required property 'database_name'
```

### Step 4. Fix Program

Your Pulumi AI-generated program may not work when you run `pulumi up` the first time (like ours), but you can ask it to fix the error. It's OK to have Pulumi AI fix an error as part of the **GPT Your IaC Challenge**. Go back to [pulumi.com/ai](/ai) and enter in the chat widget `Fix this error <error output from pulumi up>`

![alt_text](/images/challenge/AIStep4.png "navigate to Pulumi AI website")

Pulumi AI will fix the error. In this case it said

```
I see that the error is caused because the required property
database_name is missing in the timestreamwrite.Database resource.
Let me update the program to include the missing property.
```

Pulumi AI will return back the original program with the error corrected, which in our example now includes the previously-missing `database_name` parameter.

```python
timestream_database = aws.timestreamwrite.Database("myTimestreamDB", database_name="my-db-name")
```

Take the new code generated by Pulumi AI and add it to your program. In our case, we used this new code to update `__main__.py`.

### Step 5. Execute Updated Pulumi Program

Now that the code is fixed, you will run `pulumi up` again. When we ran `pulumi up` again, our program executed successfully.

```shell
 Type                             Name              Status
 +   pulumi:pulumi:Stack              ai-challenge-dev  created (280s)
 +   ├─ aws:kinesis:Stream            myDataStream      created (21s)
 +   ├─ aws:ec2:SecurityGroup         mySecurityGroup   created (2s)
 +   ├─ aws:timestreamwrite:Database  myTimestreamDB    created (1s)
 +   ├─ aws:dynamodb:Table            myDynamoDBTable   created (7s)
 +   └─ aws:rds:Instance              my-rds-example    created (275s)

Outputs:
    dynamodbTableArn     : "arn:aws:dynamodb:us-west-2:616138583583:table/myDynamoDBTable-fad6451"
    kinesisStreamArn     : "arn:aws:kinesis:us-west-2:616138583583:stream/myDataStream-48c92be"
    rdsInstanceEndpoint  : "my-rds-example10eb710.chuqccm8uxqx.us-west-2.rds.amazonaws.com:3306"
    timestreamDatabaseArn: "arn:aws:timestream:us-west-2:616138583583:database/my-db-name"
```

There you go! Pulumi AI has helped us generate a program to provision important database infrastructure for our new app. What did Pulumi AI generate for you?

## Congratulations

Congratulations! You've completed this **Pulumi Challenge**. Follow the link below and complete your submission to receive limited edition swag for this challenge. You will need to upload a screenshot of the `pulumi up` output for us to verify completion.

{{< challenge/open-form-button >}}

If you want, please create a blog post, social media, or video documenting your work on this challenge. Tag us on social media or email us at [da@pulumi.com](mailto:da@pulumi.com) to claim another piece of even more special swag. Winners will be chosen in a few months and receive a special prize.

### What you have learned

In this challenge, you have learned how to use Pulumi AI to generate a Pulumi program. The example we shared provisions a Kinesis Data Stream, RDS database, Timestream database, and a DynamoDB table.

### Clean up

If you'd like to tear down all of these resources and delete your stack, run `pulumi destroy -rf --remove`. Otherwise, have fun playing around with your infrastructure stack and add whatever you like! 🙂
