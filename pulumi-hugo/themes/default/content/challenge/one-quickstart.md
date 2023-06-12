---
title: "One Quickstart to Rule them All"
layout: challenge/single
description: |
    Build and deploy a serverless app on AWS using Pulumi Architecture Templates and a single command!
meta_desc: |
    Build and deploy a serverless app on AWS using Pulumi Architecture Templates and a single command!
meta_image: /images/challenge/challenge_cta.png
---

<div class="flex flex-wrap md:mt-12">
  <div>
    <h1 class="font-display text-6xl">One Quickstart to Rule them All!</h1>
    <div class="flex justify-center rounded-md bg-violet-100">
            <p class="text-center">
                ✨ The challenge is now over and no swag will be sent on completion, but feel free to continue testing your skills with this challenge ✨
            </p>
    </div>
    <p class="pr-12">
      Pulumi Architecture Templates make it quick and easy to get started with a wide variety of clouds, tools, and technologies when you want to try something new but don't want to write boilerplate yourself. It's a great way to get started with Pulumi quickly, no matter what you need to build. Try it for yourself with serverless AWS templates and win some swag in the process!
    </p>
    <h2>Prerequisites</h2>
    <p>In order to complete this challenge, you'll need a couple things set up in advance.</p>
    <ul>
      <li>
        A <a href="https://app.pulumi.com/signup" target="_blank" rel="noopener noreferrer">Pulumi account</a>
      </li>
      <li>
        The <a href="/docs/install/" target="_blank" rel="noopener noreferrer">Pulumi CLI</a>
      </li>
      <li>
          <a href="https://www.python.org/downloads/">Python 3.9 or higher</a>
      </li>
      <li>
        AWS account
      </li>
      <li>
        AWS CLI
      </li>
    </ul>
  </div>
</div>

## Challenge

### Step 1. Pulumi Architecture Templates

In this Challenge, you will learn how to create a new Pulumi program using [our new Pulumi Architecture Templates](/templates/), specifically for serverless blueprints for AWS with the language of your choice.

Pulumi can create a serverless app with AWS API Gateway and Lambda in many common programming languages. Today, we'll be working with Python. Create a new directory called `quickstart-challenge` and `cd` into it, then run the following:

```shell
pulumi new serverless-aws-python
```

Regardless of the language you choose, the Pulumi CLI will ask several questions of you. Name the project `one-quickstart` when prompted, and accept all other defaults. It will look something like this:

```shell
kat@Kats-MacBook-Pro testing-challenge % pulumi new serverless-aws-python
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: one-quickstart
project description: (A serverless app on AWS API Gateway and Lambda)
Created project 'one-quickstart'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'

aws:region: The AWS region to deploy into: (us-west-2)
Saved config
```

### Step 2. Exploring Blueprints

Run `pulumi up`. You will first be presented with a preview of the changes to occur.

```shell
     Type                                Name                    Plan
 +   pulumi:pulumi:Stack                 one-quickstart-dev      create
 +   ├─ aws:iam:Role                     role                    create
 +   ├─ aws:lambda:Function              fn                      create
 +   └─ aws-apigateway:index:RestAPI     api                     create
 +      ├─ aws:iam:Role                  api4c238266             create
 +      ├─ aws:s3:Bucket                 api                     create
 +      ├─ aws:iam:RolePolicyAttachment  api4c238266             create
 +      ├─ aws:apigateway:RestApi        api                     create
 +      ├─ aws:s3:BucketObject           api4c238266/index.html  create
 +      ├─ aws:apigateway:Deployment     api                     create
 +      ├─ aws:lambda:Permission         api-e7f981a5            create
 +      └─ aws:apigateway:Stage          api                     create

Outputs:
    url: output<string>

Resources:
    + 12 to create

Do you want to perform this update? yes
```

Select `yes` and watch your resources come online! With a single command, Pulumi is standing up an AWS API Gateway and Lambda instance, with all necessary roles and permissions, plus a `hello world` website displaying the current time. Cool, right?

Let's get you some swag, though.

### Step 3. Working with Policy Packs

When you're using Python or Typescript, Pulumi allows you to enforce gated deployments with [Policy Packs](/docs/using-pulumi/crossguard/configuration/), which can be used locally with the free tier. These are a set of rules, expressed programmatically, that are executed against the resources being deployed. Any violation of those rules will block the deployment. Usually, Policy Packs are used to enforce security or cost optimization rules, but in this case we're going to use one to interact with our swag provider.

Within your existing Pulumi program, create a new directory for your Policy Pack and navigate into it:

```shell
mkdir policy && cd policy
```

Creating your policy pack is simple:

```shell
pulumi policy new aws-python
```

Pulumi will once again create several files for you, including another `__main__.py`. The default Policy Pack prevents developers from allowing public read access on an AWS S3 bucket, but that isn't what we need here. Replace the contents of the new `__main__.py` with the following:

```python
import requests
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
    PolicyConfigSchema
)


def map_swag_to_form(swag_var):
    data_json = {
        'usp': 'pp_url'
    }
    swag = swag_var
    data_json['entry.1720843992'] = swag['name']
    data_json['entry.511943887'] = swag['email']
    data_json['entry.1289952319'] = swag['address']
    data_json['entry.1240089905'] = swag['size']
    return data_json


def pulumi_swag_not_submitted(args: ResourceValidationArgs, report_violation: ReportViolation):
    if not args.resource_type == "pulumi:pulumi:Stack":
        return
    swag = args.get_config()
    data_dict = map_swag_to_form(swag)
    print(data_dict)
    headers = {
        "Referer": "https://docs.google.com/forms/d/e/1FAIpQLSfBr2f6rhXYbMXi8Caftu-zWtNPRDoWUEukrTJKuwO3OyYRvg/viewform",
        "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
    }
    response = requests.post(
        url="https://docs.google.com/forms/d/e/1FAIpQLSfBr2f6rhXYbMXi8Caftu-zWtNPRDoWUEukrTJKuwO3OyYRvg/formResponse",
        headers=headers,
        data=data_dict
    )
    print(response.status_code)


submit_swag = ResourceValidationPolicy(
    name="pulumi-challenge-swag",
    description="stuff",
    validate=pulumi_swag_not_submitted,
    config_schema=PolicyConfigSchema(
        properties={
            "name": {
                "type": "string",
                "minLength": 2
            },
            "email": {
                "type": "string",
                "minLength": 6,
                "format": "email"
            },
            "address": {
                "type": "string",
                "minLength": 2
            },
            "size": {
                "type": "string",
                "minLength": 1,
                "enum": [
                    "XS",
                    "S",
                    "M",
                    "L",
                    "XL"
                ]
            }
        },
        required=[
            "name",
            "email",
            "address",
            "size"
        ]
    )
)

PolicyPack(
    name="aws-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        submit_swag
    ],
)
```

### Step 4. Complying with Policies

The Policy Pack we've defined requires that your Pulumi program involve a JSON file containing specific data. In order to comply with it and get swag, we need to create this file.

Navigate one directory up, back into your main Pulumi Challenge directory. Create a new file called `swag.json`, and add the following (replacing the values with your own information):

```json
{
  "pulumi-challenge-swag": {
    "name": "<your name>",
    "email": "<your email>",
    "address": "<your address>",
    "size": "<one of XS, S, M, L, XL>"
  }
}
```

We also have new dependencies to add to `requirements.txt` at the root of your repo. It should now look like this:

```text
pulumi>=3.0.0,<4.0.0
pulumi-aws>=5.10.0,<6.0.0
pulumi-aws-apigateway>=0.0.11
pulumi-awsx==1.0.0-beta.9
pulumi-policy>=1.3.0,<2.0.0
requests
```

Install the new requirements in the usual way:

```shell
pip install -r requirements.txt
```

Then, execute your policy pack against your Pulumi Program with the following command at the root of your repo to submit for your swag:

```shell
pulumi preview --policy-pack policy --policy-pack-config swag.json
```

Congratulations!. You've completed this Pulumi Challenge. If you'd like to tear down all of these resources, run `pulumi destroy -y`. Otherwise, have fun playing around with your new serverless application! Add whatever you like, or try one of the many other [Pulumi Architecture Templates](/templates/). Your swag will be in the mail shortly! Note that you'll only get one piece no matter how many times you submit. :)

Wanna yell it from the rooftops? Write a blog or post a quick video about it, send us the URL, and we'll send you a super secret piece of swag! Tag us on social media or email us at [da@pulumi.com](mailto:da@pulumi.com).
