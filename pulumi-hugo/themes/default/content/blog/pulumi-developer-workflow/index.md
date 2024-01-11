---
title: "Pulumi ESC + Devcontainer Developer Workflow"
date: 2024-01-10T19:41:13Z
draft: false
meta_desc: "Batteries Included: A hands on Pulumi IaC Developer Workflow experience."
meta_image: meta.png
authors:
    - kat-morgan
tags:
    - pulumi
    - environments
    - secrets
    - configuration
    - iac
    - developer
    - workflow
    - devcontainer
    - github
    - codespaces
---

Have you ever felt like every 'get started' guide starts out with the obligatory prerequisites task list? Want to try Pulumi without the headache or just elevate your current DevOps workflow? Dive into this short "batteries included" workflow demonstration and see how Pulumi, ESC, and Devcontainers are a match made in heaven for your orchestration productivity, or share with a friend and confidently colaborate without falling into the infamous "works on my machine" cope.

<!--more-->

## Intro

Getting started with new tools and projects can be exciting and fun, however it is also common to pick up something new and feel like the getting started experience would be better if all the prerequisites and starting effort was just solved already.

In this blog post we are going to explore a few new things from Pulumi to make getting started, and even well established workflows easier to reproduce, maintain, and share with others so that you can invest brain power into getting the important things done without distractions.

## Prerequisites

Before we dive in, make sure you are prepared with the following:

- Web Browser
- Github Account
- 10 minutes (aprox.)

## Requirements

Remembering that our goal is to setup an all inclusive developer environment, let's take a moment and consider the requirements for this project.

#### Commandline Utilities:
  1. Pulumi CLI
  2. Pulumi ESC
  3. Kubectl
  4. Direnv
  5. KinD
  6. Github CLI
  7. Git CLI
  8. Other tools like jq, etc

#### Safe Secrets Handling:
  - Pulumi Auth
  - Github Auth
  - Kubeconfig

## Diving In

Alright, let's jump in and get started!

#### Github Codespaces

Go ahead and launch a new [Github Codespaces].

[![Blank GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/github/codespaces-blank)

Click the button to launch a blank codespaces session to build your new project in or create a new one directly on [Github's Codespaces Console].

> Note:
>
> This demonstration focuses on using the Web based VSCode environment offered in Github Codespaces.
> Alternatively you can skip directly to the [Pulumi Devcontainer](#pulumi-devcontainer) section to follow along in your own local VSCode editor.

![New Blank Github Codespaces](image-vscode-codespaces-blank.png)


#### Pulumi Devcontainer

First, we need to make sure we have all of our cli dependencies by pulling in the [Pulumi Devcontainer].

```bash
# Initialize the git repository
git init --initial-branch=main

# Add the Pulumi Devcontainer git submodule
git submodule add https://github.com/pulumi/devcontainer .devcontainer
git submodule update --init --recursive .devcontainer
cp -f .devcontainer/devcontainer.json .devcontainer.json

gh codespace rebuild
```


#### Pulumi Cloud

let's login to Pulumi and initialize a new ESC Environment.

```bash
# Login to Pulumi Cloud
pulumi login

# Create a new ESC Environment (optionally use another already existing environment)
pulumi env init workshop
```

In our environment, we maintain our secrets including api personal access tokens, kubeconfigs, and such all with Pulumi's Environments, Secrets, and Configuration cloud service.

Before we initialize our new Git repository, let's setup our Github credentials in Pulumi ESC for safe keeping and use later.

```bash
# Load your Github Personal Access Token into the Pulumi ESC Environment for safe keeping to use later.
# https://github.com/settings/tokens
pulumi env set workshop secrets.GITHUB_TOKEN --secret ghp_6b9XXXXXXXXXXXXXXXXXXXXXXXXflAj

# Set the secrets.GITHUB_TOKEN key path as a Pulumi ESC environment variable.
pulumi env set workshop environmentVariables.GITHUB_TOKEN --plaintext \${secrets.GITHUB_TOKEN}

#pulumi env set workshop files.GITHUB_TOKEN_FILE --plaintext \${secrets.GITHUB_TOKEN}

# Load the newly updated Pulumi ESC Environment in the local shell
eval $(pulumi env open workshop --format shell)
```


#### Direnv: Automatic Environment Variables

Various non-secret environment variables may be worth maintaining in code locally as well. There are many ways to do this, but here we are going to use Direnv to automatically load environment variables from a .envrc file.

```bash
echo 'export KUBECONFIG=${PWD}/.kube/config' >> .envrc && direnv allow
direnv allow
```


#### KinD: Kubernetes-in-docker

We are going to use Kubernetes to demonstrate our Pulumi IaC. Let's go ahead and create a new cluster now.

```bash
# Create a Kind Cluster
mkdir .kube
kind create cluster

# Let's make sure our kubeconfig works
kubectl get pods -A

# Broken steps:
pulumi env set workshop kubeconfig.kind (kubectl config view --raw --output json | jq . -c)
pulumi env set workshop secrets.kubeconfig.kind --secret "(kubectl config view --raw --output json | jq . -c)"
pulumi env set workshop files.KUBECONFIG --plaintext \${secrets.kubeconfig.kind}
```


#### Minecraft: Now let's create the deployment code!

If fortune favors the bold, let's be bold on this next step and let AI write our sample code on the fly!

```bash
# Write a new Pulumi Python IaC program to deploy Minecraft on Kubernetes
pulumi new \
  --ai "Write a program using pulumi kubernetes helm v3 Release to deploy the itzg/minecraft-server helm chart on Kubernetes." \
  --language python \
  --name pulumi-minecraft-kubernetes \
  --stack pulumi-iac-workshop \
  --description "A pulumi infrastructure as code (iac) program for deploying and serving minecraft on kubernetes" \
  --force \
  --dir .;

# Deploy Minecraft on Kubernetes!
pulumi up -y --skip-preview
```


#### Git Code Repository

Now with our github token saved and exported in our environment, let's initialize our git code repository.

```bash
# Create new Git Repository
gh repo create workshop --public --description "pulumi iac developer workflow workshop" --gitignore Python --license apache-2.0 --source .

# Configure `git` cli to use the `gh` cli as an authentication helper
gh auth setup-git
git config --global user.email usrbinkat@braincraft.io
git config --global user.name usrbinkat
```


## Videos

{{< youtube "kDB-YRKFfYE?rel=0" >}}

[Github Codespaces]:https://github.com/features/codespaces
[Github's Codespaces Console]:https://github.com/codespaces
[Pulumi Devcontainer]:https://github.com/pulumi/devcontainer