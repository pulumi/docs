---
date: 2023-09-08
title: "Deploy a Hugging Face Model on Amazon SageMaker with Pulumi Python IaC"
allow_long_title: true
meta_desc: "Guided short tutorial on starting a Pulumi infrastructure as code project to deploy Hugging Face LLMs on Amazon SageMaker machine learning platform"
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

In this short tutorial we will deploy a publicly available Hugging Face model on Amazon SageMaker, and we will test a prompt using a short Python script. Now this sounds insanely cool---and it is!---but what's the value here? AI and ML can offer tremendous value to organizations, but only if AI/ML resources can be easily deployed and put to work. This short tutorial highlights a number of value propositions for Pulumi in the AI/ML space:

1. The ability to use Pulumi templates to create complex architectures that can be deployed by other users with a simple `pulumi new` command
2. The ability to easily create not just AI/ML infrastructure, but necessary supporting infrstructure _in the same Pulumi program_

With this value proposition in mind, let's look at what you'll deploy by following along with this tutorial:

* The [NousResearch/Llama-2-7b-chat-hf](https://huggingface.co/NousResearch/Llama-2-7b-chat-hf) model on [Hugging Face](https://huggingface.co/) 
* [AWS IAM Roles](/registry/packages/aws/api-docs/iam/role/)
* [Amazon SageMaker Model Endpoint](/registry/packages/aws/api-docs/sagemaker/model/)
* [Amazon CloudWatch MetricAlarm](/registry/packages/aws/api-docs/cloudwatch/metricalarm/)

[Pulumi templates](/blog/how-to-create-and-share-a-pulumi-template/) enhance the infrastructure as code (IaC) development experience by providing a pre-written code framework designed to help you bootstrap new Pulumi projects quickly.

You can use the `sagemaker-aws-python` template as a working Python starting point for your own Amazon SageMaker deployments, and customize the model you use, SageMaker configuration, and CloudWatch integration just to scratch the surface. Your only limits are your imagination.

## Requirements

* [Python3 (3.9+)](https://www.python.org/downloads/)
* [Pulumi CLI](/docs/install/)
* [Pulumi account](https://app.pulumi.com/signup)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
* [Configured & Logged in with AWS Credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-authentication.html)

## Instructions

### 1. Login to Pulumi Cloud and initialize stack

Let's begin by logging into Pulumi Cloud:

```bash
# There are many ways to store Pulumi state, here we use Pulumi Cloud
# Other state backends include S3, local file, and more
pulumi login
```

If you're unsure of which backend you're using, you can double-check that by running `pulumi whoami` (or `pulumi whoami -v` for more details).

### 2. Prepare a new Pulumi project

Here we create our new Pulumi project directory and populate it from the `sagemaker-aws-python` [Pulumi template](https://github.com/pulumi/templates)

```bash
# Create a new directory & change directories into it
mkdir newSagemaker && cd newSagemaker

# Start your project from the sagemaker-aws-python template
# Follow along with the prompts to create your new project and initialize a stack
pulumi new sagemaker-aws-python
```

### 3. Deploy your model as a new SageMaker endpoint

This step may take between 10 and 20 minutes while Amazon builds your infrastructure and deploys the configured model. You can follow along in the console as resources are provisioned, or open the link displayed in terminal for your stack in a browser to follow along there too!

```bash
pulumi up
```

### 4. Try your new SageMaker endpoint

Once your stack has finished deploying, use this rudimentary Python snippet to test the deployed SageMaker endpoint.

> NOTE: Notice that we are using `us-east-1` in this script. Be sure to change the region in Python to match the region you deployed the SageMaker endpoint into.

First, save the following python snippet as `test.py`:

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

Once you have the `test.py` script created, source the Python virtual environment named `venv` (created automatically by Pulumi) and run the script using the name of your new endpoint, taken directly from the Pulumi stack output:

```bash
# On Linux & MacOS
source venv/bin/activate

# Execute test.py
python3 test.py $(pulumi stack output EndpointName)
```

### 5. Cleanup all resources

Finally, when you're finished with testing your Hugging Face model on SageMaker, you can easily clean up un-used resources with one easy command.

```bash
pulumi destroy
```

## Conclusion

To recap, in a few commands, we created a new Pulumi Python project from a ready-to-roll template, deployed an LLM endpoint on Amazon SageMaker, and tested it with a short Python script to generate a response from our model!

AI and ML is becoming more of a necessity every day. It may appear daunting or out of reach at first glance, but with the power of IaC written in Pulumi Python programs, getting started has never been easier. 

If you followed along then tell us how it worked out for you! We would love to know what you are looking forward to, or if you have ideas for future installments of the Pulumi Python + MLOps series!

Join us on [Twitter](https://twitter.com/pulumicorp), and on the [Pulumi Community Slack](https://slack.pulumi.com) to decide what #MLOpsChallenge we take on next!