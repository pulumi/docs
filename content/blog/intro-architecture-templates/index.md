---
title: "Introducing Pulumi Architecture Templates"
date: 2022-10-19T10:59:37-05:00
meta_desc: |
    Pulumi architecture templates provide basic building blocks for many
    different cloud scenarios.
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - templates
    - architecture
---

One of the most common needs when someone starts a new project on cloud infrastructure is a scaffold of initial infrastructure that follows best practices. We're pleased to share our new architecture templates that allow you to define that scaffold with a single command on Pulumi.

<!--more-->

## Best practices for common architectures

While Pulumi allows you to define any architecture for any cloud, we often get asked for opinionated architectures to get started with different cloud-based scenarios. To meet this need, we've started building templates around best-practice architectures like [a serverless architecture on Google Cloud](/templates/serverless-application/gcp/) or [a container service architecture on AWS](/templates/container-service/aws/). To give a sense of what these templates are like, let's explore the serverless template for Google Cloud, which uses Cloud Storage and Cloud Functions to deploy a small application that tells the current time.

{{< youtube "DaX8weCHO9A?rel=0" >}}

## An example: Google Cloud Functions

There are a lot of additional components to add to any infrastructure on modern clouds, including roles created through access management. The Google Cloud Serverless Application template defines a number of necessary components:

* A storage bucket
* An Identity Account Management (IAM) binding for the bucket
* A Google Cloud Folder custom component to sync a local folder to the bucket (so you don't have to create individual objects for each file in a directory!)
* Another storage bucket
* A bucket object to hold the function app code
* A Cloud Function
* Another IAM member to run the Function
* An object in the bucket to hold some configuration values

## Deployments made simpler

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

## Check them out yourself

There are already a number of templates built, and more are coming over the next weeks and months. We'll be exploring more templates in detail here on the blog and on [PulumiTV](https://www.youtube.com/channel/UC2Dhyn4Ev52YSbcpfnfP0Mw/) in the future. Review all the currently available architecture templates at [our templates page](/templates/). We'd love to hear what you think!
