---
date: 2023-09-08
title: "Deploy a Huggingface Model on AWS SageMaker with Pulumi Python IaC"
allow_long_title: true
meta_desc: "Guided short tutorial on starting a Pulumi Infrastructure as Code project to deploy Huggingface LLM Models on Amazon Web Services SageMaker Machine Learning Platform"
meta_image: "meta.png"
authors:
    - kat-morgan
tags:
    - ai
    - ml
    - iac
    - aws
    - llm
    - vllm
    - mlops
    - llama
    - llama2
    - python
    - sagemaker
    - huggingface
---

Welcome to another post in the Pulumi + Python MLOps #MLOpsChallenge series!

In this short tutorial we will deploy a publicly available Huggingface model on Amazon AWS SageMaker, and test a prompt using a short python script.

We will be deploying:

* The [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf) model on [Hugging Face](https://huggingface.co/) 
* [Amazon AWS IAM Roles](https://www.pulumi.com/registry/packages/aws/api-docs/iam/role/)
* [Amazon AWS SageMaker Model Endpoint](https://www.pulumi.com/registry/packages/aws/api-docs/sagemaker/model/)
* [Amazon AWS CloudWatch MetricAlarm](https://www.pulumi.com/registry/packages/aws/api-docs/cloudwatch/metricalarm/)

[Pulumi templates](../how-to-create-and-share-a-pulumi-template) enhance Infrastructure as Code (IaC) development by providing a pre-written code framework designed to help you bootstrap new pulumi projects quickly.

You can use the `sagemaker-aws-python` template as a working python starting point for your own AWS SageMaker deployments, and customize the model you use, SageMaker configuration, and CloudWatch integration just to scratch the surface. Your only limits are your imagination.

## Requirements

* [Python3 (3.9+)](https://www.python.org/downloads/)
* [Pulumi CLI](https://www.pulumi.com/docs/install/)
* [Pulumi account](https://app.pulumi.com/signup)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Configured & Logged in with AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)

## Instructions

### 1. Login to Pulumi Cloud and initialize stack

Let's begin by logging into Pulumi Cloud

```bash
# There are many ways to store Pulumi state, here we use Pulumi Cloud
# Other state backends include S3, local file, and more
pulumi login
```

### 2. Prepare a new Pulumi Project

Here we create our new pulumi project directory and populate it from the `sagemaker-aws-python` [Pulumi template](https://github.com/pulumi/templates)

```bash
# Create a new directory & change directories into it
mkdir newSagemaker && cd newSagemaker

# Start your project from the sagemaker-aws-python template
# Follow along with the prompts to create your new project and initialize a stack
pulumi new sagemaker-aws-python
```

### 3. Deploy your model as a new SageMaker endpoint

This step may take between 10 and 20 minutes while Amazon AWS builds your infrastructure. You can follow along in the console as resources are provisioned, or open the link displayed in terminal for your stack in a browser to follow along there too!

```bash
pulumi up
```

## Try your new SageMaker Endpoint

Once your stack has finished deploying, use this rudimentary Python snippet to test the deployed SageMaker endpoint.

> NOTE: notice that we are using `us-east-1` in this script, be sure to change the reagion in python to match the reagion you deployed the SageMaker endpoint into.

### 4. Save the following python snippet as `test.py`

```python
import json, boto3, argparse

def main(endpoint_name):
    client = boto3.client('sagemaker-runtime', region_name='us-east-1')
    payload = json.dumps({"inputs": "In 3 words, name the biggest mountain on earth?"})
    response = client.invoke_endpoint(EndpointName=endpoint_name, ContentType="application/json", Body=payload)
    print("Response:", json.loads(response['Body'].read().decode()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("endpoint_name")
    main(parser.parse_args().endpoint_name)
```

### 5. Run the test prompt

Now source the local `venv` and run the script using the AWS name of your new endpoint from pulumi state outputs:

```bash
# On Linux & MacOS
source venv/bin/activate

# Execute test.py
python3 test.py $(pulumi stack output EndpointName)
```

### 6. Cleanup / Teardown

Finally, be sure to clean up un-used resources when you're done with one easy command.

```bash
pulumi destroy
```

## Conclusion

To recap, in a few commands, we created a new Pulumi project from a ready to roll template, deployed an LLM Model endpoint on AWS SageMaker, and tested it with a short python script to generate a response from our model!

AI and ML is becoming more of a necessity every day. It may appear daunting or out of reach at first glance, but with the power of IaC written in Pulumi Python programs, getting started has never been easier. 

If you followed along then tell us how it worked out for you! We would love to know what you are looking forward to, or if you have ideas for future installments of the Pulumi Python + MLOps series!

Join us on [Twitter](https://twitter.com/pulumicorp), and on the [Pulumi Community Slack](https://slack.pulumi.com) to decide what #MLOpsChallenge we take on next!