---
title: "Run Open-Source LLMs on AWS EC2 with Ollama and Pulumi"
date: 2025-01-27
updated: 2026-04-30
draft: false
meta_desc: |
    Self-host DeepSeek, Llama, Qwen, or Mistral on AWS EC2 with Ollama and Pulumi. Includes instance-type recommendations, cost math, and copy-paste IaC.

meta_image: meta.png

authors:
- engin-diri

tags:
- ai
- llm
- ollama
- deepseek
- llama
- qwen
- mistral
- pulumi
- aws
- ec2

social:
  twitter: |
    Want to self-host an open-source LLM on AWS? This guide deploys Ollama on a GPU EC2 instance with Pulumi—run DeepSeek, Llama, Qwen, or Mistral with one config change.
  linkedin: |
    Updated guide: how to self-host open-source LLMs on AWS EC2 with Ollama and Pulumi.

    Whether you want DeepSeek-R1, Llama 3, Qwen, or Mistral, the same Pulumi program deploys the GPU EC2 instance, installs the NVIDIA drivers, and starts Ollama with Open WebUI. Switching models is a one-line change.

    What's inside:

        Instance-type recommendations by model size (which g-class EC2 instance you actually need)
        Cost-per-token math comparing self-hosted Ollama to OpenAI and Anthropic APIs
        Copy-paste Pulumi programs in TypeScript, Python, Go, C#, and YAML
        OpenAI-compatible API access from your existing tooling

    Read the full guide: <link>
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Run an open-source LLM on AWS EC2 with Ollama and Pulumi",
  "description": "Deploy Ollama on a GPU-enabled AWS EC2 instance with Pulumi and run open-source models like DeepSeek-R1, Llama 3, Qwen, or Mistral.",
  "totalTime": "PT30M",
  "tool": [
    {"@type": "HowToTool", "name": "Pulumi CLI"},
    {"@type": "HowToTool", "name": "AWS CLI"},
    {"@type": "HowToTool", "name": "AWS Account"},
    {"@type": "HowToTool", "name": "Ollama"}
  ],
  "supply": [
    {"@type": "HowToSupply", "name": "AWS GPU EC2 instance (g4dn, g5, or g6 family)"}
  ],
  "step": [
    {
      "@type": "HowToStep",
      "position": 1,
      "name": "Create a new Pulumi project",
      "text": "Run pulumi new aws-<language> to scaffold a new project, replacing <language> with typescript, python, go, csharp, or yaml."
    },
    {
      "@type": "HowToStep",
      "position": 2,
      "name": "Create an IAM role and instance profile",
      "text": "Define an IAM role with S3 read access so the EC2 instance can pull NVIDIA GRID drivers from the ec2-linux-nvidia-drivers bucket, then attach it to an instance profile."
    },
    {
      "@type": "HowToStep",
      "position": 3,
      "name": "Provision the network",
      "text": "Create a VPC, public subnet, internet gateway, route table, and security group that exposes ports 22 (SSH), 3000 (Open WebUI), and 11434 (Ollama API)."
    },
    {
      "@type": "HowToStep",
      "position": 4,
      "name": "Launch the GPU EC2 instance",
      "text": "Create an SSH key pair and launch a g4dn.xlarge (or larger) Amazon Linux instance with the IAM profile and security group attached."
    },
    {
      "@type": "HowToStep",
      "position": 5,
      "name": "Install Ollama via cloud-init",
      "text": "Use a cloud-init user-data script to install NVIDIA drivers, Docker, the NVIDIA Container Toolkit, and start the Ollama and Open WebUI containers. The script also pulls and runs your chosen model—for example deepseek-r1:7b, llama3.1:8b, qwen2.5:7b, or mistral:7b."
    },
    {
      "@type": "HowToStep",
      "position": 6,
      "name": "Deploy the infrastructure",
      "text": "Run pulumi up to provision all resources. After the stack is created, Pulumi outputs the public IP address of the instance."
    },
    {
      "@type": "HowToStep",
      "position": 7,
      "name": "Access the Web UI or OpenAI-compatible API",
      "text": "Open http://<instance-public-ip>:3000 for Open WebUI, or point any OpenAI-compatible client at http://<instance-public-ip>:11434/v1."
    }
  ]
}
</script>

**TL;DR. Want to self-host an open-source LLM on AWS?** Use a `g4dn.xlarge` ($0.526/hr on-demand, 16 GB GPU memory) for 7B/8B models, a `g5.xlarge` ($1.006/hr, 24 GB) for 13B–14B models, a `g5.2xlarge` ($1.212/hr, 24 GB) for 32B models, or a `g6e.2xlarge` ($2.242/hr, 48 GB) for 70B models. Deploy with the Pulumi program below and Ollama will run any model from its library: DeepSeek-R1, Llama 3, Qwen, or Mistral, with a one-line change.

<!--more-->

This guide walks through that deployment end-to-end: a single Pulumi program that provisions a GPU-enabled EC2 instance, installs Ollama and Open WebUI via cloud-init, and exposes both a chat UI and an OpenAI-compatible API. The model is configurable, so you can swap DeepSeek-R1 for Llama 3.1, Qwen 2.5, or Mistral without touching the infrastructure code.

1. [Why run open-source LLMs on AWS EC2?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#why-run-open-source-llms-on-aws-ec2)
1. [Which models can I run, and which EC2 instance do I need?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#which-models-can-i-run-and-which-ec2-instance-do-i-need)
1. [How much does this cost vs. hosted APIs?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#how-much-does-this-cost-vs-hosted-apis)
1. [How do I deploy Ollama on AWS EC2 with Pulumi?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#how-do-i-deploy-ollama-on-aws-ec2-with-pulumi)
1. [How do I switch models?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#how-do-i-switch-models)
1. [What are the next steps?](/blog/run-deepseek-on-aws-ec2-using-pulumi/#what-are-the-next-steps)

## Why run open-source LLMs on AWS EC2?

Self-hosting an open-source LLM on AWS gives you three things hosted APIs can't: data stays inside your VPC, per-token costs collapse to a flat hourly rate at high volume, and you can fine-tune or quantize models freely under permissive licenses. Ollama handles all three concerns from a single binary: it downloads, manages, and serves models behind an OpenAI-compatible API on port 11434.

The original version of this post focused on [DeepSeek-R1](https://www.deepseek.com/) because it landed in late January 2025 and reset expectations for what an open-weight reasoning model could do. DeepSeek-R1 is still an excellent default (MIT-licensed, strong on math and coding, with distilled 1.5B–70B variants) but the same infrastructure runs [Meta's Llama 3](https://ai.meta.com/llama/), [Alibaba's Qwen](https://qwenlm.ai/), and [Mistral](https://mistral.ai/) equally well. Picking a model is now a config change, not an infrastructure decision.

![A bar chart compares the performance of DeepSeek and OpenAI models across six benchmarks: AIME 2024, Codeforces, GPQA Diamond, MATH-500, MMLU, and SWE-bench Verified. The models evaluated include DeepSeek-R1, DeepSeek-R1-32B, DeepSeek-V3, OpenAI-o1-1217, and OpenAI-o1-mini, with accuracy or percentile scores represented as bars. DeepSeek-R1 (blue-striped) consistently ranks among the top performers, particularly excelling in MATH-500 (97.3%), MMLU (90.8%), and Codeforces (96.3%). The chart visually distinguishes each model using different colors and shading.](img_1.png)

For reference, DeepSeek-R1 scores **79.8%** on AIME 2024 (vs. **79.2%** for OpenAI o1-1217), **97.3%** on MATH-500 (vs. **96.4%**), **96.3%** on Codeforces (vs. **96.6%**), and **49.2%** on SWE-bench Verified (vs. **48.9%**)—near-parity with closed frontier models on most reasoning benchmarks, with the same caveat that benchmark scores age fast.

{{< related-posts >}}

## Which models can I run, and which EC2 instance do I need?

The bottleneck for inference is GPU memory (VRAM): the model weights have to fit in it, plus a few GB of headroom for the KV cache. The table below maps the most common Ollama models to the smallest AWS GPU instance that comfortably runs them at 4-bit (Q4) quantization, which is what `ollama pull <model>` gives you by default.

| Model family | Sizes | Approx. VRAM (Q4) | Smallest EC2 instance | On-demand price (us-east-1) |
| --- | --- | --- | --- | --- |
| DeepSeek-R1 (distill) | 1.5B / 7B / 8B | 1–6 GB | `g4dn.xlarge` (T4, 16 GB) | $0.526/hr |
| Llama 3.1 / Llama 3.2 | 8B | ~5 GB | `g4dn.xlarge` (T4, 16 GB) | $0.526/hr |
| Qwen 2.5 | 7B | ~5 GB | `g4dn.xlarge` (T4, 16 GB) | $0.526/hr |
| Mistral 7B / Mistral Nemo | 7B / 12B | 5–8 GB | `g4dn.xlarge` (T4, 16 GB) | $0.526/hr |
| DeepSeek-R1 (distill) | 14B | ~10 GB | `g5.xlarge` (A10G, 24 GB) | $1.006/hr |
| Llama 3.3 / DeepSeek-R1 | 32B / 32B distill | ~20 GB | `g5.2xlarge` (A10G, 24 GB) | $1.212/hr |
| Llama 3.1 / DeepSeek-R1 | 70B | ~42 GB | `g6e.2xlarge` (L40S, 48 GB) | $2.242/hr |
| DeepSeek-R1 (full) | 671B (MoE) | 400 GB+ | `p5.48xlarge` or multi-node | $98.32/hr |

For most workloads—internal tools, RAG backends, code assistants—a `g4dn.xlarge` running an 8B model is the right starting point. Move up only if quality is the bottleneck.

## How much does this cost vs. hosted APIs?

A `g4dn.xlarge` running 24/7 costs **~$378/month** on-demand, or **~$237/month** with a 1-year reserved instance. Whether that's cheaper than a hosted API depends entirely on your token volume.

Compare against hosted pricing as of April 2026 (input + output blended, rough numbers):

| Provider | Model | Approx. blended price |
| --- | --- | --- |
| OpenAI | GPT-4o-mini | ~$0.30 per 1M tokens |
| OpenAI | GPT-4o | ~$5.00 per 1M tokens |
| Anthropic | Claude Sonnet 4 | ~$6.00 per 1M tokens |
| DeepSeek (hosted) | DeepSeek-V3 | ~$0.50 per 1M tokens |

A `g4dn.xlarge` running Llama 3.1 8B sustains roughly **40–60 tokens/sec** under single-user load, or about **100–155M tokens/month** at 100% utilization. At that ceiling the effective rate is **~$2.40/M tokens**—cheaper than GPT-4o or Claude, more expensive than GPT-4o-mini or DeepSeek's own hosted API.

The takeaway: **self-hosting wins on data residency, latency, and predictable cost at high utilization. Hosted APIs win below ~10M tokens/month or when you need frontier-class quality.** Run the math against your actual token volume before committing.

## How do I deploy Ollama on AWS EC2 with Pulumi?

### Prerequisites

Before we start, make sure you have the following:

- An [AWS account](https://aws.amazon.com/account/)
- [Pulumi CLI](/docs/iac/download-install/) installed
- [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- A working understanding of [Ollama](https://ollama.com/)

### What is Ollama?

![A black-and-white digital illustration of Ollama’s mascot, a stylized llama, wearing a “WORK!!” headband while intensely focused on paperwork. The mascot sits at a desk surrounded by towering stacks of documents, with scattered sheets and a coffee mug, conveying a sense of heavy workload and determination.](img_2.png)

Ollama is an open-source runtime that downloads, manages, and serves large language models from a single binary. It runs on macOS, Linux, and Windows, supports GPU acceleration through CUDA and Metal, and exposes both a native HTTP API and an OpenAI-compatible API on port 11434. Most clients written for the OpenAI SDK work against an Ollama endpoint with only a base-URL change.

It supports the major open-weight families—DeepSeek-R1, Llama 3, Qwen, Mistral, Gemma, Phi—plus quantized and distilled variants for each. You pull a model by name and tag (`ollama pull llama3.1:8b`) and run it (`ollama run llama3.1:8b`); Ollama handles the rest.

### Architecture

![A diagram illustrating an AWS-based deployment with an EC2 GPU-enabled instance running Ollama and Open-WebUI within a public subnet of a VPC. The setup includes a Docker container connected to an open-source LLM served by Ollama (such as DeepSeek-R1:7B or any Ollama-supported model), represented by a blue box with an arrow pointing from the EC2 instance. The Ollama mascot is depicted as part of the architecture.](img_4.png)

### Create a new Pulumi project

First, scaffold a new Pulumi project. Run the following from an empty directory:

```bash
# Replace <language> with typescript, python, go, csharp, or yaml
pulumi new aws-<language>
```

Pick the [language you are most comfortable with](/docs/iac/languages-sdks/). The template installs the [AWS provider](/registry/packages/aws/) and creates a working sample. You can delete the sample code—we'll replace it with the snippets below.

### Step 1: Create an instance role with S3 access

The EC2 instance needs to download NVIDIA drivers from a public AWS-managed S3 bucket. Create an IAM role with S3 read access and attach it to an instance profile:

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

### Step 2: Create the network

Next, create the VPC, subnet, internet gateway, and route table. The security group opens ports 22 (SSH), 3000 (Open WebUI), and 11434 (Ollama API):

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

### Step 3: Launch the GPU EC2 instance

Now create the EC2 instance itself. The example uses Amazon Linux because the NVIDIA driver install path is well-trodden, plus an SSH key pair you generate locally.

The default instance type is `g4dn.xlarge`—the cheapest option that fits any 7B/8B model. Bump it up if you picked a larger model from the [table above](#which-models-can-i-run-and-which-ec2-instance-do-i-need): `g5.xlarge` for 13B–14B, `g5.2xlarge` for 32B, `g6e.2xlarge` for 70B. AWS publishes full specs for the [G4](https://aws.amazon.com/ec2/instance-types/g4/), [G5](https://aws.amazon.com/ec2/instance-types/g5/), and [G6](https://aws.amazon.com/ec2/instance-types/g6/) families.

Generate the key pair if you don't already have one:

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

### Step 4: Install Ollama via cloud-init

The EC2 instance is a blank box until cloud-init runs. The user-data script below installs the NVIDIA GRID drivers, Docker, and the NVIDIA Container Toolkit, then starts the Ollama and Open WebUI containers. To switch models, edit the `ollama run` line—the rest is identical regardless of which model you want.

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
- docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

{{< related-posts >}}

### Step 5: Deploy the infrastructure

Make sure your AWS credentials are configured:

```bash
aws configure
```

Pulumi supports several other [authentication methods](/registry/packages/aws/installation-configuration/) for the AWS provider. Once credentials are in place, deploy the infrastructure:

```bash
pulumi up
```

Pulumi previews the changes; type `yes` to confirm.

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

The infrastructure provisions in under a minute, but the cloud-init script needs another 5–10 minutes to install drivers, pull container images, and download the model weights. SSH in to watch the progress, or just wait and load the Web UI when it's ready.

```
ssh -i deepseek.pem ec2-user@<instance-public-ip>
```

Check the container status:

```bash
sudo docker ps
CONTAINER ID   IMAGE                                COMMAND               CREATED         STATUS                   PORTS                                           NAMES
c8714335e205   ghcr.io/open-webui/open-webui:main   "bash start.sh"       6 minutes ago   Up 6 minutes (healthy)   0.0.0.0:3000->8080/tcp, :::3000->8080/tcp       open-webui
bf4bb3b7ede1   ollama/ollama                        "/bin/ollama serve"   8 minutes ago   Up 7 minutes             0.0.0.0:11434->11434/tcp, :::11434->11434/tcp   ollama
[ec2-user@ip-10-0-58-122 ~]$
```

### Step 6: Access the Web UI or API

Once the containers are healthy, open `http://<instance-public-ip>:3000` in your browser for Open WebUI:

{{% notes type="warning" %}}

Open WebUI is not secured by default. Restrict the security group to your IP, put it behind an authenticated proxy, or terminate TLS at an ALB before exposing it to the internet.

{{% /notes %}}

![A screenshot of a chat interface with DeepSeek-R1:7B, showing a query asking for the square root of 144. The AI responds with a step-by-step explanation, defining the square root, setting up the equation, solving for x, and confirming that \sqrt{144} = 12. The interface has a dark theme, with the query displayed at the top and the AI’s structured response below.](img_6.png)

For programmatic access, Ollama exposes an [OpenAI-compatible API](https://github.com/ollama/ollama/blob/main/docs/openai.md) on port 11434. Most clients written for the OpenAI SDK only need a base-URL change:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://<instance-public-ip>:11434/v1",
    api_key="ollama",  # required by the SDK, ignored by Ollama
)

response = client.chat.completions.create(
    model="llama3.1:8b",
    messages=[{"role": "user", "content": "Why is the sky blue?"}],
)
print(response.choices[0].message.content)
```

## How do I switch models?

Ollama hosts every major open-weight family in its [model library](https://ollama.com/library). Pulling a different model is two commands inside the EC2 instance—or a one-line edit to the cloud-init script if you want it provisioned automatically:

```bash
# DeepSeek-R1 distill (default in this guide)
docker exec ollama ollama run deepseek-r1:7b

# Llama 3.1 (Meta, 8B)
docker exec ollama ollama run llama3.1:8b

# Qwen 2.5 (Alibaba, 7B)
docker exec ollama ollama run qwen2.5:7b

# Mistral (7B)
docker exec ollama ollama run mistral:7b

# Larger reasoning model (needs g5.2xlarge or larger)
docker exec ollama ollama run deepseek-r1:32b
```

Tags follow a `<size>` or `<size>-<quantization>` pattern—`8b`, `8b-instruct-q4_K_M`, `8b-instruct-q8_0`. Q4 is the default and the right starting point; bump to Q8 only if you have spare VRAM and notice quality issues with Q4. Browse the full tag list for any model on its [Ollama library page](https://ollama.com/library).

### Cleaning up

When you're done, tear everything down:

```bash
pulumi destroy
```

## What are the next steps?

You now have a reproducible, IaC-managed deployment of any open-source LLM on AWS. The infrastructure is fixed; the model is a parameter. From here, the natural extensions are wiring this up to a real application, adding RAG over your own data, or moving the deployment behind an authenticated load balancer.

If you want to go further with AI on Pulumi, here are some related guides:

- [Deploy LangServe Apps with Pulumi on AWS (RAG & Chatbot)](/blog/easy-ai-apps-with-langserve-and-pulumi/) — Build a retrieval-augmented chatbot that could front-end this Ollama instance.
- [Deploy AI Models on Amazon SageMaker using Pulumi Python IaC](/blog/mlops-huggingface-llm-aws-sagemaker-python/) — A SageMaker alternative when you'd rather not manage the EC2 host yourself.
- [Build an AI Slack Bot on AWS Using Embedchain & Pulumi](/blog/ai-slack-bot-to-chat-using-embedchain-and-pulumi-on-aws/) — Wire an LLM into Slack as an internal assistant.
- [What is Infrastructure as Code?](/what-is/what-is-infrastructure-as-code/) — Background on the IaC approach used throughout this guide.

{{< blog/cta-button "Try Pulumi for Free" "/docs/get-started/" >}}

---

### Changelog

- **2026-04-30** — Broadened scope from DeepSeek-only to any Ollama-supported model (Llama, Qwen, Mistral). Added TL;DR, instance-type recommendation table, cost-vs-hosted-API comparison, and HowTo structured data. Restructured headings as user questions. Verified Ollama and cloud-init commands against current versions.
- **2025-03-10** — Minor edits and corrections.
- **2025-01-27** — Original post: Run DeepSeek-R1 on AWS EC2 Using Ollama.
