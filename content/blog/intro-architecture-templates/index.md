---
title: "Introducing Pulumi Architecture Templates"
date: 2022-10-19T10:59:37-05:00
updated: 2025-03-05
meta_desc: "Accelerate cloud infrastructure deployments with Pulumi’s architecture templates. Get prebuilt, best-practice templates for AWS, GCP, Azure, and more."
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - templates
    - architecture
---

🚀 Deploying cloud infrastructure is hard. Getting the architecture right from the start can be time-consuming. What if you could skip the hassle and start with prebuilt, best-practice templates?

📢 Pulumi Architecture Templates let you scaffold cloud infrastructure instantly with a single command. Whether you’re launching a serverless app on AWS, a container service on GCP, or a Kubernetes cluster on Azure, Pulumi gives you ready-to-use templates to get started faster.

➡️ Let’s dive in and see how these templates simplify cloud deployments.

<!--more-->

## Best Practices for Common Architectures

While Pulumi allows you to define any architecture for any cloud, we often get asked for opinionated architectures to get started with different cloud-based scenarios. To meet this need, we've started building templates around best-practice architectures like a [serverless architecture on Google Cloud](/templates/serverless-application/gcp/) or a [container service architecture on AWS](/templates/container-service/aws/). To give a sense of what these templates are like, let's explore the serverless template for Google Cloud, which uses Cloud Storage and Cloud Functions to deploy a small application that tells the current time.

{{< youtube "DaX8weCHO9A?rel=0" >}}

## Google Cloud Functions Example

There are a lot of additional components to add to any infrastructure on modern clouds, including roles created through access management. The Google Cloud Serverless Application template defines a number of necessary components:

* A storage bucket
* An Identity Account Management (IAM) binding for the bucket
* A Google Cloud Folder custom component to sync a local folder to the bucket (so you don't have to create individual objects for each file in a directory!)
* Another storage bucket
* A bucket object to hold the function app code
* A Cloud Function
* Another IAM member to run the Function
* An object in the bucket to hold some configuration values

## Deployments Made Simpler

Using this template (or any of the other templates, for that matter), you can create a new Pulumi project with the `pulumi new` command. The template's creation steps will now ask for all of the necessary configuration values for this template. No more deployment errors because you forgot to define your Google Cloud project with `pulumi config set`!

```bash
$ pulumi new serverless-gcp-python
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (serverless-app)
project description: (A serverless web application on Google Cloud Platform)
Created project 'serverless-app'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'

gcp:project: The Google Cloud project to deploy into: fake-proj-1
gcp:region: The Google Cloud region to deploy into: (us-central1)
appPath: The path to the folder containing the functions to be deployed: (./app)
errorDocument: The file to use for error pages: (error.html)
indexDocument: The file to use for top-level pages: (index.html)
```

### Pulumi Templates vs Manual Setup

| Feature                      | Pulumi Architecture Templates | Manual Setup |
|------------------------------|------------------------------|--------------|
| **Preconfigured Best Practices** | ✅ Yes  | ❌ No |
| **Multi-Cloud Support**       | ✅ AWS, GCP, Azure  | ❌ Typically single-cloud |
| **Faster Deployments**        | ✅ One command setup | ❌ Manual coding required |
| **Scalability**               | ✅ Easily extensible  | ⚠️ Needs custom scripts |
| **Infrastructure-as-Code (IaC)** | ✅ Pulumi-native  | ❌ Requires manual IaC setup |

## Test Templates Yourself

There are already a number of templates built, and more are coming over the next weeks and months. We'll be exploring more templates in detail here on the blog and on [PulumiTV](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw/) in the future. Review all the currently available architecture templates at [our templates page](/templates/). We'd love to hear what you think!
