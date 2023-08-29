---
date: 2023-08-23
title: "Pulumi Python + MLOps: Deploy a chatbot in 30 minutes or less!"
allow_long_title: true
meta_desc: "Accelerating AI/ML Innovation with Infrastructure as Code through a Hands-On Journey to deploy your own chatbot."
meta_image: "chatbot-api-prompt.png"
authors:
    - kat-morgan
tags:
    - ai
    - ml
    - iac
    - llm
    - vllm
    - mlops
    - azure
    - llama
    - llama2
    - python
---

# Deploy a chatbot in 30 minutes or less

Welcome to the future! Today *you* can deploy an advanced AI ChatBot in the cloud or on your own hardware, in 30 minutes or less. That's right, we're diving right in and getting hands on using Pulumi Python Infrastructure as Code (IaC) to practice MLOps with your very own chatbot API.

Allow me to introduce the start of a "Pulumi Python + MLOps" series where we walk the hero's journey of MLOps together and make things a bit easier for everyone along the way.

Did I mention this IaC is written in Python? While Pulumi supports many languages, we chose python for this project as it is already familiar to most in the AI industry.

Let's introduce some key concepts and technologies to start off.

- Infrastructure as Code (IaC) is a transformative approach to platform engineering and orchestration. By applying the rigor and precision of software development practices to cloud operations, IaC offers AI/ML professionals an efficient, reliable, and predictable way to develop at the highest velocity.

- Katwalk Server is a demo AI application written to host your choice of LLM either locally or in the cloud, and serve it as an OpenAI API compatible service. As a practical, hands-on introduction to IaC for the MLOps space, this project aims to demystify the concepts and showcase the benefits Pulumi can bring to your AI/ML projects.

- Large Language Model or "LLM"s like ChatGPT are machine learning models trained to generate human-like conversational text which have already become essential tools for businesses and individuals, transforming every day tasks and how we interact with technology.

> Or letting ChatGPT describe itself:

![Alt text](image-1.png)

Now, let's get to the fun part and deploy a chat API!

Requirements:

* [Pulumi](https://www.pulumi.com/docs/install/)
* [Python3](https://www.python.org/downloads/)
* [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [Huggingface Token](https://huggingface.co/docs/transformers.js/guides/private)
* [Huggingface access to LLaMa2](https://huggingface.co/meta-llama)
  * [Meta LLaMa2 Access](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

> !NOTE! Access to LLaMa2 via Huggingface is not required if using a non-private model repository. Learn more [HERE](https://huggingface.co/docs/transformers.js/guides/private)

Optional Requirements (must choose one)

* [Docker](https://docs.docker.com/engine/install/)
  * [Nvidia Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)
  * [Nvidia CUDA Enabled GPU](https://developer.nvidia.com/cuda-gpus)
* [Azure](https://azure.microsoft.com/en-us)
  * [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)


### 1. Prepare your Pulumi IaC Directory:

```bash
# Clone the repository and cd to the pulumi iac directory
gh repo clone usrbinkat/katwalk && cd katwalk/pulumi

# Create and initialize the python virtual env
python3 -m venv venv && source venv/bin/activate

# Install python dependencies
python -m pip install -r requirements.txt
```

## 2. Login & Initialize your pulumi state file and stack

```bash
# Create & Export a pulumi secret decryption password file
# This allows for decrypting any secrets in your Pulumi.<stack>.yaml file
# !WARNING! Please use a more secure password than this example.
export PULUMI_CONFIG_PASSPHRASE_FILE=$HOME/.pulumi/secret
echo "keepItSecretKeepItSafePassword" > ~/.pulumi/secret

# There are many ways to store pulumi state, here we use a local file.
# Other state backends include s3, Pulumi Cloud, and more.
pulumi login file://~/.pulumi

# Initialize your stack
# Here we name the stack "dev"
pulumi stack init --stack dev
```


## Configure required credentials

```bash
# Set Huggingface.co username
pulumi config set hfUsername <huggingface_username>

# Configure token as secret
pulumi config set --secret hfToken <huggingface_api_token>

# Set the model that you want to download
pulumi config set hfModel "meta-llama/Llama-2-7b-chat-hf"
```

## Deploy locally with Docker

> WARNING: LLM Models can use up 30 to 100 gigabytes of disk space or more!

```bash
# This enables the IaC to deploy Katwalk Server
pulumi config set deploy True

# Set the deploy runtime to docker to deploy locally
pulumi config set runtime docker

# (OPTIONAL): set a local directory to store llm model(s)
# If you do not set this path then Pulumi will fallback to
# provision and utilize a docker volume for model storage.
pulumi config set modelsPath /home/kat/models

# Finally, run `pulumi up` to deploy!
pulumi up

# When done, you can 'destroy' the stack to deprovision your deployment
pulumi destroy
```

## Deploy in the cloud on Azure Container Instances

```bash
# This enables the IaC to deploy Katwalk Server
pulumi config set deploy True

# Set the deploy runtime to docker to deploy locally
pulumi config set runtime azure

# Finally, run `pulumi up` to deploy!
pulumi up

# When done, you can 'destroy' the stack to deprovision your deployment
pulumi destroy
```

## Build the Katwalk Container

```bash
# Set image build to True
pulumi config set imageBuild True # Defaults to False

# Set registry and image location
# This should be compatible with any OCI registry
# - private registry
# - docker.io
# - quay.io
pulumi config set registry ghcr.io
pulumi config set registryNamespace usrbinkat

pulumi config set password --secret <registry_password_or_api_token>
pulumi config set username $USERNAME

kip pushing the image to a registry:

pulumi config set skipImageUpload True
```


```txt
...rest of instructions go here...
```

Using API developer tools such as Postman or Insomnia, or even directly from the command line with curl, go ahead and query your new endpoint to try the chatbot for yourself!

![chatbot-api-response](./chatbot-api-prompt.png)

In a world where data is the new black gold and tokens are money, deploying a ChatBot in 30 minutes is not just interesting, it is a novel capability quickly becoming a necessity.

Platform engineering, DevOps, or MLOps may be the next hardest step in building the AI future. However Pulumi lowers the barrier to success in ML research and product development, and Python based IaC empowers the MLOps community to build equity in common AI platform code, and share IaC in a familiar language.

If you followed along then tell us how it worked out for you! We would love to know what you are looking forward to, or if you have ideas for future installments of the Pulumi Python + MLOps series!

> *figure x: Midjourney generated image of an imagined machine learning research engineer working among cables, computers, keyboards, and screens, in the glow of electronic lights. Image was generated from a prompt ~80% produced by ChatGPT based on this blog post content and a few superficial details about the author.

![Midjourney generated image of an imagined machine learning research engineer working among cables, computers, keyboards, and screens, in the glow of electronic lights. Image was generated from a prompt produced by ChatGPT based on this blog post content and a few superficial details about the author.](image-2.png)
