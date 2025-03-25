---
title: "Run DeepSeek-R1 on AWS EC2 Using Ollama"
date: 2025-01-27
updated: 2025-03-10
draft: false
meta_desc: |
  Learn how to set up and run DeepSeek-R1 on an AWS EC2 instance using Ollama and Pulumi. Follow this step-by-step guide for AI deployment in the cloud.

meta_image: meta.png

authors:
  - engin-diri

tags:
  - ai
  - deepseek
  - pulumi
  - aws
  - ec2
  - ollama

social:
  twitter: |
    DeepSeek is the new kid on the block in the AI community. Learn how to set up and run DeepSeek R1 on an AWS EC2 instance using Pulumi and Ollama.
  linkedin: |
    Excited to share our latest blog post on how to set up and run DeepSeek R1—a cutting-edge open-source AI model—on an AWS EC2 instance using Pulumi and Ollama.

    Why DeepSeek R1? DeepSeek R1 has quickly become a standout in the AI community, offering exceptional performance and reasoning capabilities. Competing with industry giants like OpenAI and Meta, it excels in benchmarks such as AIME 2024 for mathematics, Codeforces for coding, and MMUL for general knowledge.

    What You'll Learn:

        Infrastructure as Code with Pulumi: Automate the deployment of your AWS EC2 instances seamlessly.
        Managing LLMs with Ollama: Simplify the process of running and managing large language models.
        Hands-On Setup: Step-by-step instructions with code snippets in TypeScript, Python, Go, C#, and YAML.
        Performance Insights: Understand how DeepSeek R1 outperforms rivals in key areas.

    Why Pulumi and AWS EC2? Leveraging Pulumi's Infrastructure as Code (IaC) capabilities with AWS EC2 provides a robust and scalable environment for running advanced AI models like DeepSeek R1. This combination ensures flexibility, reliability, and ease of management.

    Get Started: Whether you're looking to experiment with AI models or scale your applications in the cloud, this guide has you covered. From setting up your environment to deploying and accessing the DeepSeek Web UI, you'll find all the resources you need.

    Read the full blog post here: <link>
search:
  keywords:
    - ec2
    - deepseek
    - ollama
    - r1
    - aws
    - run
    - using
---

This weekend, my "for you" page on all of my social media accounts was filled with only one thing: [DeepSeek](https://www.deepseek.com/). DeepSeek really managed to shake up the AI community with a series of very strong language models like DeepSeek R1.

<!--more-->

**But why?** The answer is simple: DeepSeek entered the market as an open-source (MIT license) project with excellent performance and reasoning capabilities.

1. [The Company Behind DeepSeek](/blog/run-deepseek-on-aws-ec2-using-pulumi/#the-company-behind-deepseek)
2. [DeepSeek R1 Model](/blog/run-deepseek-on-aws-ec2-using-pulumi/#deepseek-r1-model)
3. [What Are Distilled Models?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#what-are-distilled-models)
4. [Setting Up The Environment](/blog/run-deepseek-on-aws-ec2-using-pulumi/#setting-up-the-environment)
5. [Next Steps](/blog/run-deepseek-on-aws-ec2-using-pulumi/#next-steps)

## The Company Behind DeepSeek

DeepSeek is a Chinese AI startup founded in 2023 by Lian Wenfeng. One interesting fact about DeepSeek is that the cost of training and developing DeepSeek's models was only a fraction of what OpenAI or Meta spent on their models.

This on its own sparked a lot of interest and curiosity in the AI community. DeepSeek R1 is near or even better than its rival models on some of the important benchmarks like AIME 2024 for mathematics, Codeforces for coding, and MMUL for general knowledge.

![A bar chart compares the performance of DeepSeek and OpenAI models across six benchmarks: AIME 2024, Codeforces, GPQA Diamond, MATH-500, MMLU, and SWE-bench Verified. The models evaluated include DeepSeek-R1, DeepSeek-R1-32B, DeepSeek-V3, OpenAI-o1-1217, and OpenAI-o1-mini, with accuracy or percentile scores represented as bars. DeepSeek-R1 (blue-striped) consistently ranks among the top performers, particularly excelling in MATH-500 (97.3%), MMLU (90.8%), and Codeforces (96.3%). The chart visually distinguishes each model using different colors and shading.](img_1.png)

### Mathematics: AIME 2024 & MATH-500

DeepSeek-R1 shows robust multi-step reasoning, scoring **79.8%** on AIME 2024, edging out OpenAI o1-1217 at **79.2%**.
On MATH-500—which tests a wide range of high-school-level problems—DeepSeek-R1 again leads with **97.3%**, slightly
above OpenAI o1-1217’s **96.4%**.

### Coding: Codeforces & SWE-bench Verified

In algorithmic reasoning (Codeforces), OpenAI o1-1217 stands at **96.6%**, marginally ahead of DeepSeek-R1’s **96.3%**.
Yet on SWE-bench Verified, which focuses on software engineering reasoning, DeepSeek-R1 scores **49.2%**, surpassing
OpenAI o1-1217’s **48.9%** and showcasing strong software verification capabilities.

### General Knowledge: GPQA Diamond & MMLU

OpenAI o1-1217 excels in factual queries (GPQA Diamond) with **75.7%**, outperforming DeepSeek-R1 at **71.5%**. For
broader academic coverage (MMLU), the margin is still tight: **91.8%** (OpenAI o1-1217) vs. **90.8%** (DeepSeek-R1),
indicating near-parity in multitask language understanding.

{{< related-posts >}}

## DeepSeek R1 Model

DeepSeek R1 is a large language model developed with a strong focus on reasoning tasks. It excels at problems requiring multi-step analysis and logical thinking. Unlike typical models that rely heavily on Supervised Fine-Tuning (SFT), DeepSeek R1 uses Reinforcement Learning (RL) as its primary training strategy. This emphasis on RL empowers it to figure out solutions with greater independence.

## What Are Distilled Models?

Besides the main model, DeepSeek AI has introduced distilled versions in various parameter sizes—1.5B, 7B, 8B, 14B, 32B, and 70B. These distilled models draw on Qwen and Llama architectures, preserving much of the original model’s reasoning capabilities while being more accessible for personal computer use.

Notably, the 8B and smaller models can operate on standard CPUs, GPUs, or Apple Silicon machines, making them convenient for anyone interested in experimenting at home.

That's why I decided to run DeepSeek on an AWS EC2 instance using Pulumi. I wanted to see how easy it is to set up and run DeepSeek on the cloud using [Infrastructure as Code (IaC)](/blog/what-is/what-is-infrastructure-as-code/). So, let's get started!

## Setting Up The Environment

### Prerequisites

Before we start, make sure you have the following prerequisites:

- An [AWS account](https://aws.amazon.com/account/)
- [Pulumi CLI](/docs/iac/download-install/) installed
- [AWS CLI](https://aws.amazon.com/cli/) installed
- Understanding of [Ollama](https://ollama.com/)

### What Is Ollama?

![A black-and-white digital illustration of Ollama’s mascot, a stylized llama, wearing a “WORK!!” headband while intensely focused on paperwork. The mascot sits at a desk surrounded by towering stacks of documents, with scattered sheets and a coffee mug, conveying a sense of heavy workload and determination.](img_2.png)

Ollama allows you to run and manage large language models (LLMs) on your own computer. By simplifying the process of downloading, running, and using these models. It supports macOS, Linux, and Windows, making it accessible across different operating systems. Ollama is easy to use. It has simple commands to pull, run, and manage models.

In addition to local usage, Ollama provides an API for integrating LLMs into other applications. An experimental compatibility layer with the OpenAI API means many existing OpenAI-compatible tools can now work with a local Ollama server. It can leverage GPUs for faster processing and includes features like custom model creation and sharing.

Ollama provides strong support for many large language models such as Llama 2, Code Llama, or in our case DeepSeek R1, granting users secure, private, and local access. It offers GPU acceleration on macOS and Linux and provides libraries for Python and JavaScript.

### Running DeepSeek On AWS EC2

![A diagram illustrating an AWS-based deployment with an EC2 GPU-enabled instance running Ollama and Open-WebUI within a public subnet of a VPC. The setup includes a Docker container and is connected to an external LLM (DeepSeek-R1:7B), represented by a blue box with an arrow pointing from the EC2 instance. The Ollama mascot is depicted as part of the architecture.](img_4.png)

First, we need to create a new Pulumi project. You can do this by running the following command:

```bash
# Select your preferred language (e.g., typescript, python, go, etc.)
pulumi new aws-<language>
```

Please choose the [language you are most comfortable with](/docs/iac/languages-sdks/).

This will create a new Pulumi project with the necessary files and configurations and a sample code. In our example code, it will also install the [AWS provider](/registry/packages/aws/) for you.

Since you will not be using the sample code, feel free to delete it. After that, you can copy and paste the following code snippets into your Pulumi project.

#### Create An Instance Role With S3 Access

To download the NVIDIA drivers needed to create an instance role with S3 access. Copy the following code to your Pulumi project:

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="deepseek-ollama" language="typescript" from="1" to="30" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="deepseek-ollama" language="python" from="1" to="37" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="deepseek-ollama" language="go" from="1" to="13" >}}
{{< example-program-snippet path="deepseek-ollama" language="go" from="15" to="53" >}}
{{< example-program-snippet path="deepseek-ollama" language="go" from="205" to="208" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="1" to="12" >}}
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="12" to="66" >}}
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="220" to="225" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="deepseek-ollama" language="yaml" from="1" to="53" >}}
```

{{% /choosable %}}

#### Create The Network

Next, we need to create a VPC, subnet, Internet Gateway, and route table. Copy the following code to your Pulumi project:

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="deepseek-ollama" language="typescript" from="31" to="94" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="deepseek-ollama" language="python" from="37" to="106" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="deepseek-ollama" language="go" from="1" to="13" >}}
                // omitted for brevity
{{< example-program-snippet path="deepseek-ollama" language="go" from="53" to="141" >}}
{{< example-program-snippet path="deepseek-ollama" language="go" from="205" to="208" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="1" to="12" >}}
            // omitted for brevity
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="67" to="142" >}}
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="220" to="225" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="deepseek-ollama" language="yaml" from="53" to="114" >}}
```

{{% /choosable %}}

#### Create An EC2 Instance

Finally, we need to create the EC2 instance. For this, we need to create our SSH key pair and retrieve the Amazon Machine Images to use in our instances. We are going to use `Amazon Linux`, as it is the most common and has all the necessary packages installed for us.

I also use a `g4dn.xlarge`, but you can change the instance type to any other instance type that supports GPU. You can find more information about the [instance types](https://aws.amazon.com/ec2/instance-types/g4/).

If you need to create the key pair, run the following command:

```bash
openssl genrsa -out deepseek.pem 2048
openssl rsa -in deepseek.pem -pubout > deepseek.pub
ssh-keygen -f mykey.pub -i -mPKCS8 > deepseek.pem
```

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
{{< example-program-snippet path="deepseek-ollama" language="typescript" from="95" to="136" >}}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
{{< example-program-snippet path="deepseek-ollama" language="python" from="106" to="142" >}}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
{{< example-program-snippet path="deepseek-ollama" language="go" from="1" to="13" >}}
                // omitted for brevity
{{< example-program-snippet path="deepseek-ollama" language="go" from="141" to="204" >}}
{{< example-program-snippet path="deepseek-ollama" language="go" from="205" to="208" >}}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="1" to="12" >}}
            // omitted for brevity
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="142" to="219" >}}
{{< example-program-snippet path="deepseek-ollama" language="csharp" from="220" to="225" >}}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
{{< example-program-snippet path="deepseek-ollama" language="yaml" from="114" to="141" >}}
```

{{% /choosable %}}

#### Install Ollama And Run DeepSeek

After we set up all the infrastructure needed for our GPU-powered EC2 instance, we can install Ollama and run DeepSeek. This will all be done as part of the user data script we pass to the EC2 instance.

In the `runcmd` section of the user data script, we will install the necessary packages, download the NVIDIA GRID drivers from S3, install Docker, and run the Ollama and Open WebUI containers.

```yaml
#cloud-config
users:
- default

package_update: true

packages:
- apt-transport-https
- ca-certificates
- curl
- openjdk-17-jre-headless
- gcc

runcmd:
- yum install -y gcc kernel-devel-$(uname -r)
- aws s3 cp --recursive s3://ec2-linux-nvidia-drivers/latest/ .
- chmod +x NVIDIA-Linux-x86_64*.run
- /bin/sh ./NVIDIA-Linux-x86_64*.run --tmpdir . --silent
- touch /etc/modprobe.d/nvidia.conf
- echo "options nvidia NVreg_EnableGpuFirmware=0" | sudo tee --append /etc/modprobe.d/nvidia.conf
- yum install -y docker
- usermod -a -G docker ec2-user
- systemctl enable docker.service
- systemctl start docker.service
- curl -s -L https://nvidia.github.io/libnvidia-container/stable/rpm/nvidia-container-toolkit.repo | sudo tee /etc/yum.repos.d/nvidia-container-toolkit.repo
- yum install -y nvidia-container-toolkit
- nvidia-ctk runtime configure --runtime=docker
- systemctl restart docker
- docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama --restart always ollama/ollama
- sleep 120
- docker exec ollama ollama run deepseek-r1:7b
- docker exec ollama ollama run deepseek-r1:14b
- docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

{{< related-posts >}}

#### Using DeepSeek Models via Ollama

DeepSeek provides a diverse range of models in the Ollama library, each tailored to different resource requirements and use cases. Below is a concise overview:

##### Model Sizes

The library offers models in sizes like 1.5B, 7B, 8B, 14B, 32B, 70B, and even 671B parameters (where “B” indicates billions). While larger models tend to deliver stronger performance, they also demand more computational power.

##### Quantized Models

Certain DeepSeek models come in quantized variants (for example, q4_K_M or q8_0). These are optimized to use less memory and may run faster, though there can be a minor trade-off in quality.

##### Distilled Versions

DeepSeek also releases distilled models (e.g., qwen-distill, llama-distill). These versions are lighter, having been trained to mimic the behavior of larger models and offering a more balanced mix of performance and resource efficiency.

##### Tags

Each model has both a “latest” tag and specialized tags indicating its size, quantization level, or distillation approach. For example: `latest`, `1.5b`, `7b`,`8b`,`14b`, `32b`, `70b`, `671b` and more.

To pull a model, use the following command:

```bash
# Replace <tag> with the desired model tag
ollama pull deepseek-r1:<tag>
```

In our case, we will pull the 7B model:

```bash
ollama pull deepseek-r1:7b
```

### Deploy the Infrastructure

Before deploying the infrastructure, make sure you have the necessary AWS credentials set up. You can do this by running the following command:

```bash
aws configure
```

Pulumi supports a wide range of configuration options, including environment variables, configuration files, and more. You can find more information in the [Pulumi documentation](/registry/packages/aws/installation-configuration/).

After setting up the credentials, you can deploy the infrastructure by running the following command:

```bash
pulumi up
```

This command will give you first a handy preview of the actions Pulumi will take. If you are happy with the changes, you can confirm the deployment by typing `yes`.

```
pulumi up
Please choose a stack, or create a new one: <create a new stack>
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`): dev
Please enter your desired stack name.
Created stack 'dev'
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/deepseek-ollama-typescript/dev/previews/1dbb18ea-ba31-4d5b-9510-5dce19eb8ee8

     Type                              Name                            Plan
 +   pulumi:pulumi:Stack               deepseek-ollama-typescript-dev  create
 +   ├─ aws:ec2:KeyPair                deepSeekKey                     create
 +   ├─ aws:ec2:Vpc                    deepSeekVpc                     create
 +   ├─ aws:iam:Role                   deepSeekRole                    create
 +   ├─ aws:iam:InstanceProfile        deepSeekProfile                 create
 +   ├─ aws:ec2:SecurityGroup          deepSeekSecurityGroup           create
 +   ├─ aws:ec2:RouteTable             deepSeekRouteTable              create
 +   ├─ aws:ec2:InternetGateway        deepSeekInternetGateway         create
 +   ├─ aws:ec2:Subnet                 deepSeekSubnet                  create
 +   ├─ aws:iam:RolePolicyAttachment   deepSeekS3Policy                create
 +   ├─ aws:ec2:RouteTableAssociation  deepSeekRouteTableAssociation   create
 +   └─ aws:ec2:Instance               deepSeekInstance                create

Outputs:
    amiId            : "ami-085131ff43045c877"
    instanceId       : output<string>
    instancePublicDns: output<string>

Resources:
    + 12 to create

Do you want to perform this update? yes
Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/deepseek-ollama-typescript/dev/updates/1

     Type                              Name                            Status
 +   pulumi:pulumi:Stack               deepseek-ollama-typescript-dev  created (40s)
 +   ├─ aws:ec2:KeyPair                deepSeekKey                     created (0.47s)
 +   ├─ aws:iam:Role                   deepSeekRole                    created (1s)
 +   ├─ aws:ec2:Vpc                    deepSeekVpc                     created (12s)
 +   ├─ aws:iam:InstanceProfile        deepSeekProfile                 created (6s)
 +   ├─ aws:iam:RolePolicyAttachment   deepSeekS3Policy                created (0.90s)
 +   ├─ aws:ec2:InternetGateway        deepSeekInternetGateway         created (0.69s)
 +   ├─ aws:ec2:Subnet                 deepSeekSubnet                  created (11s)
 +   ├─ aws:ec2:SecurityGroup          deepSeekSecurityGroup           created (2s)
 +   ├─ aws:ec2:RouteTable             deepSeekRouteTable              created (1s)
 +   ├─ aws:ec2:RouteTableAssociation  deepSeekRouteTableAssociation   created (0.92s)
 +   └─ aws:ec2:Instance               deepSeekInstance                created (12s)

Outputs:
    amiId            : "ami-085131ff43045c877"
    instanceId       : "i-0ae7495781ace3e81"
    instancePublicDns: "18.159.211.136"

Resources:
    + 12 created

Duration: 42s
```

While the infrastructure is relatively quickly deployed, the user data script will take some time to download the necessary packages and run the containers.

You can check that everything is up and running by either connecting via `ssh` to the instance or navigating to the public IP address of the instance in your browser.

```
ssh -i deepseek.pem ec2-user@<instance-public-ip>
```

And then run the following command to check the status of the containers:

```bash
sudo docker ps
CONTAINER ID   IMAGE                                COMMAND               CREATED         STATUS                   PORTS                                           NAMES
c8714335e205   ghcr.io/open-webui/open-webui:main   "bash start.sh"       6 minutes ago   Up 6 minutes (healthy)   0.0.0.0:3000->8080/tcp, :::3000->8080/tcp       open-webui
bf4bb3b7ede1   ollama/ollama                        "/bin/ollama serve"   8 minutes ago   Up 7 minutes             0.0.0.0:11434->11434/tcp, :::11434->11434/tcp   ollama
[ec2-user@ip-10-0-58-122 ~]$
```

### Accessing the Web UI

When the EC2 instance is up and running and the containers are started, you can access the Ollama Web UI by navigating to `http://<ec2-public-ip>:3000`.

{{% notes type="warning" %}}

Keep in mind that the Ollama Web UI is not secure by default. Make sure to secure it before exposing it to the public.

{{% /notes %}}

We can give it a spin by running a few queries. For example, we can ask DeepSeek to solve a math problem:

![A screenshot of a chat interface with DeepSeek-R1:7B, showing a query asking for the square root of 144. The AI responds with a step-by-step explanation, defining the square root, setting up the equation, solving for x, and confirming that \sqrt{144} = 12. The interface has a dark theme, with the query displayed at the top and the AI’s structured response below.](img_6.png)

What is nice about DeepSeek is that we can also see the reasoning behind the answer. This is very helpful to understand how the model came to a conclusion.

### Accessing DeepSeek with Ollama OpenAI-Compatible API

Ollama provides an OpenAI-compatible API that allows you to interact with DeepSeek models programmatically. This allows you to use existing OpenAI-compatible tools and applications with your local Ollama server.

I am not going to cover how to use the API in this post, but you can find more information in the [Ollama documentation](https://github.com/ollama/ollama/blob/main/docs/api.md).

### Cleaning Up

After you are done experimenting with DeepSeek, you can clean up the resources by running the following command:

```bash
pulumi destroy
```

## Next Steps

This post demonstrated how easy it is to set up and run DeepSeek on an AWS EC2 instance using Pulumi. By leveraging IaC, we were able to create the necessary infrastructure with a few lines of code. From here, we can easily configure the code to run any other AI model on the cloud, change the instance type, or even set additional infrastructure for the application connection to the model.

If you have any questions or need help with the code, feel free to reach out to me and if you want to give DeepSeek with Pulumi a try, head over to the [Pulumi documentation](/docs/get-started/).

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}

If you want to learn more about what we learned from using GenAI in production, check out the [Recipe for a Better AI-based Code Generator
](/blog/codegen-learnings/) blog post.
