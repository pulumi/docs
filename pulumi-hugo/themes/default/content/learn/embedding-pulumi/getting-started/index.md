---
title: "Getting Started"
layout: topic
date: 2021-12-15
draft: false
description: |
    Set up your local system to start building a working example of the
    Automation API.
meta_desc: |
    Set up your local system to start building a working example of the
    Automation API.
index: 0
estimated_time: 5
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - learn
block_external_search_index: false
---

Often when scaling up from an idea, an organization goes through a period of time where the engineering org is growing so fast that everyone is spinning up a lot of individual architectures in an attempt to build quickly. Eventually, the team reaches the point that someone needs to own all of the infrastructure and standard use cases have appeared. Often, once an organization understands its use cases for infrastructure, it starts to explore creating platforms for people to build on (versus everyone inventing infrastructure from scratch). And thus a platform engineering team, either only in duties or both in duties and name, is born.

With all of that in mind, let's imagine that the Pulumipus Boba Tea Shop, our company from the Fundamentals learning path, has been doing so well that we can expand to jump into other markets like selling tea blends or selling its boba tea automation application to other tea shops. We're now part of a cloud engineering platform team, and we need to make it easy for developers building our applications to work with the infrastructure we manage by making it something they don't need to think much about.

This is exactly where Pulumi's Automation API can come in handy. The Automation API lets you embed Pulumi into applications and interfaces to empower others to get the infrastructure they need in the way you expect them to use it. You can also use it to work with CI/CD systems, chatops systems, monitoring systems, gitops systems, or anything else where you want to integrate the automation of the state of your infrastructure. For example, if you want your monitoring system to spin up additional spot instances or tear down unused spot instances based on traffic patterns without needing human interaction, you can use the Automation API to let alerts trigger infrastructure changes (perhaps with some policy as code to provide some guardrails to prevent the automation from tearing down everything or running up your bill).

In our example scenario, let's pretend that we're starting to find development teams scaling across datacenters, regions, or zones. We're having trouble knowing what infrastructure is getting used, and we'd like to automatically stand up a small set of serverless functions for every region we enter so new infrastructure reports back to a central dashboard. Since we want this infrastructure to deploy without any human action, we can't use a standard CLI-based workflow like we would everywhere else. We're going to use the Automation API to integrate the creation of that serverless function infrastructure into every pipeline that stands up something new. For our function's output, we're going to gather bits of data related to time like timezones, time drift, and more. We'll set up a small monitoring function that reports this data on deployment without needing a lot of time, memory, or space to run (and therefore is cheap to use).

Let's get started!

## Setting up

We're going to embed Pulumi in a Python program so we can use it in pipelines, APIs, and web interfaces. For the Pulumi program we're using to test our automation, we'll get to some sample code in a moment. If you'd like to use your own Pulumi program, however, go for it!

Just like in all of our other pathways, we're going to create a new Pulumi project to hold our code. You could keep working in whatever project that you already have set up, but it will get a bit messy if you do. Create a new directory called `learn-auto-api`. We'll use this directory name in the rest of this pathway. If you name it something different, don't forget to change the value in the code!

Add `api` and `infra` directories in your project, and run `pulumi new` with the `aws-python` template in each one. If you need a refresher on how to do so, head to [Pulumi Fundamentals]({{< relref "/learn/pulumi-fundamentals" >}}). Add a directory called `time` inside your `api` directory to hold the actual application. Your project directory now should match this file tree:

```
learn-auto-api/
    api/
        time/
        venv/
        .gitignore
        __main__.py
        Pulumi.yaml
        requirements.txt
    infra/
        venv/
        .gitignore
        __main__.py
        Pulumi.yaml
        requirements.txt
```

## Making a local example

For our application to test the eventual API, we're going to use the a Lambda on AWS, so we'll use the AWS provider. Put the following code in a file called `time_me.py` in the `time` directory:

{{< code-filename file="learn-auto-api/api/time/time_me.py" >}}

```python {.line-numbers}
from os import environ
from time import localtime


def timezone(event, context):
    return localtime(0).tm_zone


def location(event, context):
    return environ['AWS_REGION']
```

{{< /code-filename >}}

This code will return a bit of information when run as a serverless function.

Next, let's add a Pulumi program that deploys this function. Add the following code in a file called `burner.py` in the `api` directory, and then we'll talk about what exactly this file is doing:

{{< code-filename file="learn-auto-api/api/burner.py" >}}

```python {.line-numbers}
from pulumi import AssetArchive, Config, export, FileArchive, ResourceOptions
from pulumi_aws import iam, lambda_


def pulumi_program():
    config = Config()
    request = config.require('request')
    if request == 'timezone':
        # Spin up a serverless function infra with the time function in the requested zone with the right permissions
        lambda_role = iam.Role(
            "role-2",
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
    }"""
        )

        lambda_policy = iam.RolePolicyAttachment(
            "role-policy",
            role=lambda_role.id,
            policy_arn=iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE
        )

        time_fn = lambda_.Function(
            "timezone-finder",
            runtime='python3.9',
            role=lambda_role.arn,
            handler="time_me.timezone",
            code=AssetArchive({
                ".": FileArchive("./time")
            }),
            opts=ResourceOptions(depends_on=lambda_role)
        )
        invoke_me = lambda_.Invocation(
            "test-invoke",
            function_name=time_fn.name,
            input="""{"request": "timezone"}"""
        )
        export(f'{request}', invoke_me.result)
    elif request == 'location':
        # Spin up a serverless function infra with the location function in the requested region with the right permissions
        lambda_role = iam.Role(
            "role-2",
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
    }"""
        )

        lambda_policy = iam.RolePolicyAttachment(
            "role-policy",
            role=lambda_role.id,
            policy_arn=iam.ManagedPolicy.AWS_LAMBDA_BASIC_EXECUTION_ROLE
        )

        location_fn = lambda_.Function(
            "location-finder",
            runtime='python3.9',
            role=lambda_role.arn,
            handler="time_me.location",
            code=AssetArchive({
                ".": FileArchive("./time")
            }),
            opts=ResourceOptions(depends_on=lambda_role)
        )
        invoke_me = lambda_.Invocation(
            "test-invoke",
            function_name=location_fn.name,
            input="""{"request": "location"}"""
        )
        export(f'{request}', invoke_me.result)
    else:
        print("Please send me something real")
```

{{< /code-filename >}}

With the Automation API, we can invoke programs that are passed inline (meaning all of the actual code that's being run is part of the automation we'll define later) or passed via a local program. "Local" in this case is local to the system running the Automation API itself, not necessarily local to your machine. Local programs are probably the most commonly used. However, inline programs are great for running tests or other smaller, atomized actions. Here, we're setting up a local program with the `pulumi_program` function, which makes the entire local program callable by the API. The function itself should be a usable, runnable Pulumi program as demonstrated here. The program itself is setting up an AWS Lambda function with the requisite roles and policies and an invocation. The exports will get fed up to our API program.

In the {{< langfile >}} in the `api` directory, replace all of the contents with the following code:

{{< code-filename file="learn-auto-api/api/requirements.txt" >}}

```python {.line-numbers}
import burner

burner.pulumi_program()
```

{{< /code-filename >}}

By setting things up this way, we call the right program from the API later, and we ensure we can call the program directly if we need to debug later.

In the `requirements.txt` file in the `api` directory, we need to add the requirements for our Lambda function. Update that file as follows:

{{< code-filename file="learn-auto-api/api/requirements.txt" >}}

``` text {.line-numbers}
falcon
pulumi
pulumi-aws
```

{{< /code-filename >}}

Here's the file structure so far:

```
learn-auto-api/
    api/
        time/
            time_me.py
        venv/
            ...
        .gitignore
        __main__.py
        burner.py
        Pulumi.yaml
        requirements.txt
    infra/
        venv/
            ...
        .gitignore
        __main__.py
        Pulumi.yaml
        requirements.txt
```

<br/>
<br/>

Now that we have our project initialized, let's add some Automation API code!
