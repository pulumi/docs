---
title: "Use Your GPU for Your Agents: Self-Host Gemma 4 with Pulumi and Tailscale"
allow_long_title: true
date: 2026-06-02
draft: false
meta_desc: |
    Self-host Gemma 4 on a Mac with Pulumi, llama.cpp, and Tailscale, using a 26 B A4B MXFP4 GGUF at about 50 output tokens per second.
meta_image: meta.png
feature_image: feature.png
authors:
- pablo-seibelt
tags:
- ai
- kubernetes
- tailscale
- python
social:
  twitter: |
    Local AI agents usually mean tradeoffs: cloud bills, data leaving your machine, or awkward offline workflows.

    Pablo Seibelt rebuilt the setup around Gemma 4, llama.cpp, k3d, Pulumi, and Tailscale. Here's where the pieces fit.
  linkedin: |
    Local AI agents come with awkward tradeoffs: data leaves your network, offline work gets harder, and usage-based billing follows every token.

    Pablo Seibelt tested a different shape on a Mac: host-native inference, Kubernetes for the UI layer, and Tailscale for private access.

    The post walks through why the model runs outside the cluster, what Pulumi manages, and where the setup still needs credentials to finish the route.
  bluesky: |
    Local AI agents usually mean cloud bills, data leaving your machine, or awkward offline workflows.

    Pablo Seibelt rebuilt the setup around Gemma 4, llama.cpp, k3d, Pulumi, and Tailscale.
---

If you run AI tools and agents, you've probably accepted three tradeoffs: your data leaves your network, you can't work offline, and your bill scales with usage.

Open-weight models now run well on consumer hardware. Once the model is on your machine, your data stays local, inference works offline, and tokens cost nothing. If you own a modern Mac, you can run a high-quality model yourself.

<!--more-->

[Gemma 4](https://blog.google/technology/ai/google-gemma-4/) is an open-weights model family from Google. This post focuses on the 26 B A4B mixture-of-experts variant quantized as `MXFP4_MOE` by Unsloth. Thanks to the [GGUF](https://huggingface.co/docs/hub/en/gguf) format, this model fits on a modern Mac while leaving enough headroom for a local server and chat UI.

We'll use `llama.cpp` for host-native inference, `k3d` for a local Kubernetes cluster, Pulumi for infrastructure as code, and Tailscale for secure access.

## Prerequisites

This setup was validated on the following hardware:
- macOS 26.5
- MacBook Pro with Apple M3 Max
- 36 GB RAM

On this machine, `llama.cpp` reported about **53 output tokens per second** for a short validation response with `unsloth/gemma-4-26B-A4B-it-GGUF`, `gemma-4-26B-A4B-it-MXFP4_MOE.gguf`, and an 8,192-token context. In round numbers, this GGUF reached about **50 output tokens per second** on this class of Mac. Sustained throughput varies by prompt length, thermal state, and how much of the response is reasoning content.

You'll need `brew`, `docker`, `pulumi`, and `tailscale` installed. We'll also install `k3d` during the process.

## Create a disposable validation folder

Before we start, create a clean workspace to avoid cluttering your system.

```bash
scratch="$(mktemp -d "${TMPDIR:-/tmp}/pulumi-gemma4-blog-qa.XXXXXX")"
mkdir -p "$scratch"/{home,cache,logs,models,repo,stacks,evidence}
cd "$scratch"
```

## Run Gemma 4 with host-native llama.cpp

We use `llama.cpp` directly on macOS to leverage Apple Metal acceleration. Running the LLM on the host is more efficient than trying to pass GPU access into a local Kubernetes VM.

Download and run the model with this command:

```bash
llama-server \
  --hf-repo unsloth/gemma-4-26B-A4B-it-GGUF \
  --hf-file gemma-4-26B-A4B-it-MXFP4_MOE.gguf \
  --host 127.0.0.1 \
  --port 18080 \
  --ctx-size 8192
```

We used port `18080` because the default `8080` was occupied by an existing SSH tunnel. If your port `8080` is free, you can use it and adjust the Pulumi config later.

The model file is about 16.55 GB. With an 8,192-token context, it leaves more headroom than the dense 31 B Q4 model while still providing a strong local Gemma 4 experience.

### Verify the LLM API

Open a new terminal and check if the server is responding:

```bash
curl http://127.0.0.1:18080/v1/models
```

The `/v1/models` endpoint should return the model ID `unsloth/gemma-4-26B-A4B-it-GGUF`. Now try a chat completion:

```bash
curl http://127.0.0.1:18080/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "unsloth/gemma-4-26B-A4B-it-GGUF",
    "messages": [{"role": "user", "content": "Reply with exactly: OK"}],
    "temperature": 0,
    "max_tokens": 256
  }'
```

The chat prompt `Reply with exactly: OK` should return content `OK` with `max_tokens=256`. In validation, `llama.cpp` reported an output token velocity of about 53 tokens per second for this response.

## Deploy Open WebUI with Pulumi and k3d

Now we'll deploy Open WebUI into a local Kubernetes cluster. This provides a polished chat interface that connects to our host-native LLM.

First, install `k3d` if you haven't already:

```bash
brew install k3d
```

Create a new cluster for this project:

```bash
k3d cluster create pulumi-gemma4-blog-qa
```

We'll use the Pulumi program in [`pulumi/examples`](https://github.com/pulumi/examples/tree/master/kubernetes-py-self-host-gemma4-llm). This program defaults to `runtimeMode=host`, which creates a Kubernetes `ExternalName` service pointing to your host machine.

Clone the examples repo, navigate to the program directory, and initialize a new stack:

```bash
git clone https://github.com/pulumi/examples.git
cd examples/kubernetes-py-self-host-gemma4-llm
pulumi stack init gemma4-local
```

Configure the program to match your local setup:

```bash
pulumi config set hostLlmPort 18080
pulumi config set llmBaseUrl http://llm-server:18080/v1
```

The `llm-server` service in Kubernetes maps to `host.k3d.internal`. In our validation, we confirmed that a disposable k3d pod could reach the host LLM at `http://llm-server:18080/v1/models` after a CoreDNS restart.

```bash
kubectl rollout restart deployment coredns -n kube-system
```

Finally, run `pulumi up` to deploy the stack:

```bash
pulumi up
```

In our validation environment, this command successfully reached the resource synthesis phase but stopped at the Tailscale provider step because we hadn't configured the required credentials.

## Access Open WebUI through Tailscale

Tailscale allows you to access your private Open WebUI instance from any device on your tailnet. Note that we only expose the web interface, not the raw LLM API, to keep the system secure.

As mentioned, our validation was blocked by missing Pulumi Tailscale provider credentials. It requires an explicit `api_key` or an OAuth/identity token.

To finish the setup, you'll need to provide these credentials to Pulumi:

```bash
pulumi config set tailscale:apiKey YOUR_API_KEY --secret
```

Once configured, Pulumi will create a Tailscale device or proxy that routes traffic to your Open WebUI service.

## Use the model with Pi

Open WebUI gives you a browser-based chat interface, but local models are also useful from coding agents. Pi can point at the same OpenAI-compatible `llama.cpp` endpoint and use the model running on your Mac.

![Pi connected to local Gemma 4 through llama.cpp](pi.png)

## MLX benchmark on Apple Silicon

We also tested [MLX](https://github.com/ml-explore/mlx), Apple's dedicated machine learning framework. Using `mlx-community/gemma-4-31b-4bit`, we observed useful performance:

- **Generation speed**: 14.955 tokens/sec
- **Peak memory**: 17.538 GB

However, we found that the MLX server warned it wasn't production-ready and lacked some security features. The model also struggled with following short prompts during our tests. For these reasons, we recommend `llama.cpp` with the Unsloth Gemma 4 26 B A4B MXFP4 GGUF as the default for now.

## Advanced: Linux GPU in-cluster serving

If you're running on a Linux server with an NVIDIA or AMD GPU, you can run the LLM directly inside the Kubernetes cluster. This requires the NVIDIA or ROCm device plugins.

The Pulumi program supports this through `runtimeMode=cluster`. In this mode, it deploys a `LlmServer` pod that manages the `llama.cpp` process within the cluster, using GPU resource requests to ensure hardware acceleration.

## Cleanup

When you're done, you can tear down the resources:

```bash
pulumi destroy
k3d cluster delete pulumi-gemma4-blog-qa
# Stop the llama-server process using the PID from your terminal
kill <PID>
```
