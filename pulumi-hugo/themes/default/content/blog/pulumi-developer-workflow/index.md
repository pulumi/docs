---
title: "Pulumi ESC + Devcontainer Developer Workflow"
date: 2024-01-10T19:41:13Z
draft: false
meta_desc: "What does Github, Devcontainers, VSCode, Pulumi, and Pulumi ESC bring to DevOps? Everything you need to orchestrate the cloud!"
meta_image: image-vscode-codespaces-blank.png
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

Have you ever felt like every 'get started' guide promises an easy path to success and then slams you with a long requirements list? I want to share Pulumi with you, and better than fighting with installing python or jodejs, or meeting any number of other requirements. Wouldnt it be nice if everything you need was just ready to grab and go?

Dive into this short "batteries included" DevOps developer workflow demonstration and see how Pulumi, ESC, and Devcontainers are a match made in heaven for your cloud ops productivity.

<!--more-->

## Intro

Below, we are going to cover a few different topics regarding how to easily get started with Pulumi, other technologies that pair well with Pulumi during the development process, and conclude with a demonstration of how to use these tools together to quickly get comfortable in a complete cloud developer environment.

At just over six months into the quest to conquer DevOps and GitOps with Pulumi, I have come across a commonly shared question, most recently brought up during a great customer conversation at AWS re:Invent.

>
> "What should be inside of a DevOps git repository?"
>

Unlike many other programs, Pulumi is not just a single tool, but rather an cloud developer ecosystem of tools, SDK packages, and services wrapped in Pulumi Cloud which work together as a complete developer experience.

Many cloud native tools and platforms require a plethora of dependencies and accompanying tooling. Pulumi can feel a bit daunting with it's support of many general purpose programming languages, SDK packages, and cloud providers offering many forks in the road on the path to success.

If you've ever struggled to choose a flavor of ice cream among the dizying number of choices on offer then if you are anything like me you may easily recognize the concept of being "paralized by choices".

Freezing, while great for ice cream, does not offer quite as much satisfaction while attacking an engineering or developer problem.

In the DevOps world, whether you are Paladin, Wizard, or Warlock (*cough* DnD nerds) Pulumi's powerful toolset is both a worthy endeavor, and a rewarding challenge to master.

Pulumi has been a part of my tool belt for over 3 years now, however it was not a consistent or core responsibility prior to joing Pulumi so I have uncovered many of my own eureka moments.

In true DevOps fassion, the work leading up to this blog post alone included a roller coaster of chronic scope creep, pushing deadlines, learning things that changed my entire approach, and sent me back to the drawing board. Frankly, 10 days ago I was on the verge of questioning the idea of turn key developer environments. the entire plan was on the rocks.

Was I doing too much? Had the spirit of the project exceeded it's deliverable reality? I was teetering on the cliff weighing my resolve when in the middle of a demo hacking session with a colleague all of these new tools and skills came together in a vision for making this your batteries included Pulumi developer workflow.

All you have to do is "turn the key" or hit that git clone button and you are a step away from your first  `pulumi up` command.

Without further delay, I could not be more excited to share with you the best way to dive in with with Pulumi for yourself.

## Pulumi Developer Day 0

>
> What's in a Day 0?
>

Day zero is going to be your planning and design phase. Sometimes this includes various stages of research, and other times it is a matter of just getting started with hands on investigation.

For us, we have just a few requirements to get started, and I bet you are already at least half of the way there.

## Prerequisites

Before we dive in, make sure you are prepared with the following:

- Web Browser
- Github Account
- 10 minutes (aprox.)
- Pulumi Cloud Personal Access Token (PAT)

### Requirements

Remembering that our goal is to setup an all inclusive developer environment, let's take a moment and consider what we need at the starting line of our "Day 0" for this project.

#### Commandline Utilities:

|      Tool              | Description                     |
|:----------------------:|:-------------------------------:|
| Pulumi CLI             | Infrastructure as Code          |
| Pulumi ESC             | Secrets and Configuration Store |
| Kubectl                | Kubernetes CLI                  |
| Direnv                 | Automatic Environment Variables |
| KinD                   | Kubernetes Local Cluster        |
| Github CLI             | Github & Git Repository CLI     |
| Other: (jq, curl, etc) | Other useful tools              |

#### Github Codespaces

Okay, so we have a few tools to install, but what if we could skip that step and just get started right away? That's where the Pulumi Devcontainer, and Github Codespaces comes in.

Alright, let's jump in and get started by launching a new [Github Codespaces].

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pulumi/devcontainer?devcontainer_path=.devcontainer%2Fdevcontainer.json)

You can the 'Open in Github Codespaces' button to directly launch a new codespaces session from here, or you can go directly to the [Pulumi Devcontainer] repo and launch a new codespaces session from there with more customization options in the click through menues to launch your new session.

[Pulumi Devcontainer]:https://github.com/pulumi/devcontainer

> Note:
> This demonstration focuses on using the Web based VSCode environment offered in Github Codespaces. Alternatively you choose to launch the [Pulumi Devcontainer](#pulumi-devcontainer) in your own local VSCode editor with Docker.
>

With a new codespaces session launched, you should see a new VSCode editor window open in your browser. If you are not already familiar with VSCode, you can learn more about it here: https://code.visualstudio.com/docs

![Alt text](image.png)

Contratulations! Your new developer environment is ready to to start coding Pulumi.

For our final Day 0 step, we need an idea of what we are going to build with our Infrastructure-as-Code (IaC) program.

For this, why dont we deploy a Minecraft server on Kubernetes? It's a fun way to get started with Pulumi, and a great way to show off your new developer environment to friends and maybe even a gateway to DevOps for young gamers and future engineers.

# Pulumi Developer Day 1

Okay, we have an environment, we have a plan, all we need now is to hammer out some code. ... Or do we?

More than just hype, here at Pulumi the big brains in Engineering have been turning caffeine to code at a break neck pace to release some amazing results to help you along with your IaC development as well. Powered by ChatGPT, Pulumi's "[Pulumi AI](https://www.pulumi.com/ai)" is augmented by our Pulumi Cloud Providers, Docs, and SDKs ready to be your cloud ninja sidekick.

Better experienced than just as been working on some pretty cool AI tools to help developers get started with Pulumi, which brings us to the next step in our journey.

## Pulumi AI

Pulumi AI is available as a web based tool much like the now familiar ChatGPT console, however it is also built into the `pulumi` cli tool, which means you can use it right from your terminal in your new codespaces developer environment.

```bash
pulumi new --ai
```

![Alt text](image-1.png)

Okay, so we select the ai option with the arrow and enter keys, and then we are prompted to enter a description of what we want to build. Let's try something like this:

```bash
Write a program using pulumi kubernetes helm v3 Release to deploy the itzg/minecraft-server helm chart on Kubernetes, and include a pulumi output to show the helm release status."
```

Now, we should remember that we are working with very new experimental technology but if we are feeling bold enough let's see how it does with writing the code.

![pulumi ai](image-2.png)

It's looking pretty good for a simple deployment. We cant get too confident yet but since we are brave let's proceed. I have a kind cluster deployed with codespaces docker-in-docker so let's use that to try the deployment. Proceed through the prompts and we will come to our next steps.

![python venv ready to rock and roll](image-3.png)

I chose python for this project, but you can choose any of the supported languages. We can see that `pulumi new` has created a new python virtual environment for us programatically. In addition to the boilerplate to support our new project, Pulumi AI wrote the first iteration of our Python Minecraft Deployment IaC! The next steps are printed on screen. Assuming your kind cluster and kubeconfig are ready to roll we just have one step left.

```bash
pulumi up -y
```

And because no hero's journey can be documented without the gruesome account of what came before, I have included many of the manual steps required to get to this point below by hand.

<details>

#### Git Code Repository

Now create a git code repository to version control this project infrastructure code in Github.

```bash
# Authenticate with Github before proceeding.
gh auth login --web --git-protocol https --scopes "repo,gist,read:packages,admin:org,delete_repo,codespace"

# Create new Git Repository
gh repo create workshop --public \
  --gitignore Python --license apache-2.0 \
  --description "pulumi iac developer workflow workshop"

# Initialize the git repository
git clone --recurse-submodules https://github.com/${GITHUB_USER}/workshop .

# Configure `git` cli to use the `gh` cli for authentication with Github
gh auth setup-git

# Configure the username and email associated with your Github account.
git config --global user.email ${GIT_COMMITTER_EMAIL}
git config --global user.name ${GITHUB_USER}

# List files being tracked by git and their current status.
git status
```

#### Direnv: Automatic Environment Variables

Various non-secret environment variables may be worth maintaining in code locally as well. There are many ways to do this, but here we are going to use Direnv to automatically load environment variables from a .envrc file.

```bash
# Add environment variables useful during development to .envrc
cat <<EOF >> .envrc
export NO_COLOR=true
export PULUMI_HOME=\${HOME}/.pulumi
export PULUMI_SKIP_UPDATE_CHECK=true
export PULUMI_SKIP_CONFIRMATIONS=true
export KUBECONFIG=\${PWD}/.kube/config
source venv/bin/activate 2>/dev/null || true
EOF
```

Now you can enable direnv on this directory.

```bash
# Enable direnv in this directory.
direnv allow
```

> Note:
>
> Env variables shown are for educational purposes only and should be used with care.
> Read more about available Pulumi Environment variables here:
> https://www.pulumi.com/docs/cli/environment-variables

#### Pulumi Devcontainer

Now, to make sure we have all of our cli dependencies, let's grab the [Pulumi Devcontainer].

```bash
# Add the Pulumi Devcontainer git submodule
git submodule add https://github.com/pulumi/devcontainer .devcontainer
git submodule update --init --recursive .devcontainer

# Copy the devcontainer config of your choice into the top level of your project
# so it will auto select by default when you open Codespaces in the future.
cp -f .devcontainer/devcontainer.json .devcontainer.json

# Rebuild the codespaces using the newly added Pulumi Devcontainer
gh codespace rebuild --codespace ${CODESPACE_NAME}
```

#### Pulumi Cloud

Let's login to Pulumi Cloud and initialize a new ESC environment to store our environment variables, secrets, and configuration which should be preserved and distributed securely from your Pulumi Cloud account.

```bash
# Login to Pulumi Cloud
pulumi login

# Create a new ESC Environment (optionally use another already existing environment)
pulumi env init workshop
```

#### KinD: Kubernetes-in-docker

We are going to use Kubernetes to demonstrate our Pulumi IaC. Let's go ahead and create a new cluster now.

```bash
# Create the directory for your new kind kubeconfig
mkdir .kube

# Create a Kind Cluster
kind create cluster

# Let's make sure our kubeconfig works and pods are starting up
kubectl get pods -A

# Load Kubeconfig into Pulumi ESC as an encrypted secret for safe keeping.
# This is an example use case for storing kubeconfig which would not usually be practical
# for disposable kind kubernetes clusters like this however the approach is practical in many
# other scenarios which you may come across.
pulumi env set workshop secrets.kubeconfig.kind --secret "$(jq . -R -s < $KUBECONFIG)"
pulumi env set workshop files.KUBECONFIG --plaintext \${secrets.kubeconfig.kind}
```

In our environment, we maintain our secrets including api personal access tokens, kubeconfigs, and such all with Pulumi's Environments, Secrets, and Configuration cloud service.

```bash
# Load the newly updated Pulumi ESC Environment in the local shell
eval $(pulumi env open workshop --format shell)
```

#### Now let's create the deployment code!

If fortune favors the bold, let's be bold on this next step and let AI write our sample code on the fly!

As this is a "hello world" style demonstration intended to showcase the developer workflow more than any specific cloud technologies, let's deploy something fun like a Minecraft server! Be sure to watch for the video demonstration of this exercise on Pulumi's PulumiTV YouTube channel for an extra easter egg bonus step!

```bash
# Write a new Pulumi Python IaC program to deploy Minecraft on Kubernetes
pulumi new \
  --ai "Write a program using pulumi kubernetes helm v3 Release to deploy the itzg/minecraft-server helm chart on Kubernetes, and include a pulumi output to show the helm release status." \
  --description "A pulumi infrastructure as code (iac) program for deploying and serving minecraft on kubernetes" \
  --name "minecraft-on-kubernetes" \
  --language python \
  --stack "workshop" \
  --force \
  --dir .
```

Now let's see if our new Infrastructure as Code Pulumi Python Codebase will deploy!

```bash
# Deploy your new Pulumi IaC on Kubernetes
pulumi stack select workshop
pulumi up
```

#### Conclusion

```bash
# Check for your new Minecraft pod
kubectl get po
```

</details>

#### Cleanup

```bash
pulumi destroy -y --skip-preview
pulumi stack rm workshop
kind delete cluster --name kind
gh repo delete ${GITHUB_USER}/workshop
```

#### Videos

{{< youtube "kDB-YRKFfYE?rel=0" >}}

[Github Codespaces]:https://github.com/features/codespaces
[Github's Codespaces Console]:https://github.com/codespaces
[Pulumi Devcontainer]:https://github.com/pulumi/devcontainer
