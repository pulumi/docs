---
title: "AI/ML on Kubernetes: Deploying Models with Pulumi on Google Cloud"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-03-24T07:32:19Z

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Run AI/ML workloads on Kubernetes with Pulumi and Google Cloud. Automate model training, deployment, and scaling with Infrastructure as Code for seamless ML ops

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: ai-ml-kubernetes-gcp-blog-article.png


# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - sara-huddleston

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - kubernetes
    - ai
    - llm
    - google-cloud
    - gke
    - k8s

# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Kubernetes has transformed cloud infrastructure by enabling scalable, containerized applications. While it initially gained traction for managing web applications and microservices, its capabilities now extend to AI/ML workloads, making it the go-to platform for data scientists and machine learning engineers.

Running AI/ML workloads on Kubernetes presents unique challenges, including:

- **Specialized hardware** requirements (e.g., GPUs, TPUs)
- **Scalability** for model training and inference
- **Complex data pipelines** that integrate various cloud services
- **Infrastructure automation** for seamless deployment

Google Cloud Kubernetes (GKE) provides a robust foundation for AI/ML workloads, but managing infrastructure manually can be cumbersome. This is where Pulumi comes in—enabling Infrastructure as Code (IaC) to automate and simplify AI/ML infrastructure on Kubernetes.

<!--more-->


## Pulumi: Automating AI/ML Infrastructure on Google Cloud

Pulumi is a modern Infrastructure as Code (IaC) tool that allows teams to define and manage cloud infrastructure using general-purpose programming languages like Python, TypeScript, and Go. This approach is particularly beneficial for AI/ML teams, as Python is already the dominant language in data science and machine learning.

With Pulumi, you can:

- **Provision and scale Kubernetes clusters** on [Google Cloud](https://www.pulumi.com/docs/iac/clouds/gcp/) automatically.
- **Define AI/ML environments as code**, making deployments repeatable and version-controlled.
- **Integrate infrastructure with machine learning pipelines**, reducing operational overhead.

{{% notes "info" %}}
Want to geek out and get the inside scoop on AI/ML using Kubernetes? Meet us at:

- **KubeCon Europe Booth S450** - [Request a 1:1 Demo](https://www.pulumi.com/kubecon-europe/)
- **Google Next'25 booth 1589** - [Join us for a Happy House and/or Request your 1:1 Demo](https://www.pulumi.com/google-next/)

Don’t miss the chance to see Pulumi in action, ask questions, and explore AI/ML innovations on Kubernetes.🚀
{{% /notes %}}

## Deploying AI/ML Workloads on Kubernetes

Below, we explore two use cases for running AI/ML workloads on [Google Kubernetes Engine (GKE)](https://www.pulumi.com/templates/kubernetes/gcp/) using Pulumi.

{{< youtube "CoZM9BCJcJ4?rel=0" >}}

### Use Case 1: Deploying a Large Language Model (LLM) with Retrieval Augmented Generation (RAG)

Large Language Models (LLMs) like **GPT-3, Whisper, and DALL-E** require significant infrastructure for training and inference. **Retrieval Augmented Generation (RAG)** enhances LLMs by integrating external knowledge sources, improving accuracy and relevance.

Using Pulumi, you can **automate the deployment of an open-source [LLM with RAG](https://www.pulumi.com/blog/codegen-learnings/)** on Kubernetes.

#### Step 1: Set Up a Kubernetes Cluster on Google Cloud

```python
import pulumi
import pulumi_gcp as gcp

# Create a GKE cluster for AI/ML workloads
cluster = gcp.container.Cluster("ml-cluster",
    location="us-central1",
    initial_node_count=3,
    node_version="1.23",
    min_master_version="1.23")

# Create a node pool optimized for ML workloads
node_pool = gcp.container.NodePool("ml-node-pool",
    cluster=cluster.name,
    node_config=gcp.container.NodePoolNodeConfigArgs(
        machine_type="n1-standard-4",
        oauth_scopes=[
            "https://www.googleapis.com/auth/devstorage.read_only",
            "https://www.googleapis.com/auth/logging.write",
        ],
        labels={"team": "ml"},
        shielded_instance_config=gcp.container.NodePoolNodeConfigShieldedInstanceConfigArgs(
            enable_secure_boot=True,
            enable_integrity_monitoring=True,
        ),
    ),
    initial_node_count=2,
    location="us-central1",
    version="1.23")
...
```

This Pulumi script:

- Provisions a **Kubernetes cluster** on Google Cloud.
- Creates a **dedicated node pool** optimized for AI/ML workloads.
- Ensures **security best practices** for machine learning environments.

#### Step 2: Deploy the LLM with RAG Model

Once the cluster is set up, we can deploy the **LLM with RAG model** using Pulumi’s [Kubernetes provider](https://www.pulumi.com/blog/pko-2-0-ga/):

1. Define **Kubernetes Deployments** for the LLM and RAG model.
2. Package models as **Docker containers** and deploy them to the cluster.
3. Configure **Kubernetes Services** to expose APIs for model inference.
4. Use **ConfigMaps and Secrets** to manage parameters and credentials.

By defining these resources in Pulumi, deployments become **fully automated, repeatable, and scalable**.

### Use Case 2: Training and Serving Custom Machine Learning Models

Beyond pre-trained LLMs, [Kubernetes](https://www.pulumi.com/docs/iac/clouds/kubernetes/) is ideal for **training and serving custom AI/ML models**. Pulumi can help automate every stage of the ML lifecycle.

#### Step 1: Set Up the Model Training Environment

Using Pulumi, we define a training environment with:

- A **Kubernetes Deployment** for training jobs (GPU-enabled).
- **Persistent Volume Claims (PVCs)** for storing training data and model artifacts.
- **Monitoring tools** for tracking performance.

#### Step 2: Deploy and Serve the Trained Model

Once the model is trained, Pulumi can be used to:

- Deploy the trained model as a **Kubernetes Deployment**.
- Expose the model via a **Kubernetes Service** (REST API or gRPC).
- Add **autoscaling rules** for dynamic inference scaling.

Pulumi allows teams to **manage the entire AI/ML pipeline** in a structured and automated way.

Try Jay’s demo code on [Creating an AI Training Platform on GKE with Pulumi](https://github.com/jasonsmithio/pulumi-experiments/tree/main/ai-ml-platform/gke-training).

## Why Use Pulumi for AI/ML on Kubernetes?

Pulumi provides several advantages for AI/ML teams running workloads on Kubernetes:

### 1. Use General-Purpose Languages for Infrastructure as Code

- Most AI/ML engineers already work with **Python** or **Go**, and Pulumi lets them manage infrastructure using the same language.
- No need to learn YAML or Kubernetes manifests—define everything programmatically.

### 2. Automate AI/ML Workflows

- Define infrastructure, training jobs, and model serving in **[one unified IaC framework](https://www.pulumi.com/blog/unified-programmatic-approach-infrastructure-management-bmw-using-pulumi/)**.
- Ensure **consistency** across development, staging, and production environments.

### 3. Improve Scalability and Cost Efficiency

- Pulumi integrates with **Google Cloud AI services** for optimized compute resources.
- Automate **autoscaling and resource allocation** for AI/ML workloads.

### 4. Increase Security and Compliance

- Manage credentials and secrets securely with **[Pulumi ESC (Secrets Management)](https://www.pulumi.com/docs/esc/)**.
- Apply **[policy-as-code](https://www.pulumi.com/docs/iac/using-pulumi/crossguard/)** to enforce security best practices.

## Get Started with AI/ML on Kubernetes with Pulumi
Pulumi makes it easy to deploy, scale, and manage AI/ML workloads on Kubernetes, leveraging Google Cloud's AI infrastructure. Whether you're serving LLMs, training custom models, or automating ML pipelines, Pulumi provides a developer-friendly, scalable, and secure solution.

- [Explore AI/ML Projects using Pulumi](https://www.pulumi.com/blog/tag/ml/)
- [Discover Essential Kubernetes Best Practices](https://www.pulumi.com/blog/kubernetes-best-practices-i-wish-i-had-known-before/)
- [Get Started with Pulumi on Google Cloud](https://www.pulumi.com/docs/iac/clouds/gcp/)
- [Sign up for Pulumi ➡️](https://app.pulumi.com/signup)

By combining Kubernetes, Google Cloud, and Pulumi, you can accelerate AI/ML innovation while reducing infrastructure complexity.
