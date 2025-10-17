---
title: "New Pulumi ESC Onboarding and OIDC Provider Experience"
date: 2025-10-17T16:00:00-03:00
draft: false
meta_desc: Explore Pulumi ESC’s new onboarding and simplified OIDC setup for AWS, Azure & GCP. Securely manage environments with ease.
meta_image: meta.png
authors:
    - pablo-terradillos
    - sean-yeh
tags:
    - esc
schema_type: auto
---

Pulumi ESC (Environments, Secrets, and Configuration) provides centralized secrets management and configuration orchestration across your infrastructure and applications. Today, we’re excited to introduce a redesigned onboarding experience and a simpler, automated way to set up Pulumi ESC as an OpenID Connect (OIDC) provider.

<!--more-->

## A new and refreshed onboarding experience

Pulumi ESC helps you manage configuration for Pulumi programs, handle secret rotation, and centralize secrets stored across multiple providers.

We’ve now started simplifying these workflows from the moment you create a new Environment. The redesigned onboarding experience helps you get the most out of ESC. From the very moment you’re starting fresh or cloning existing environments.

![The new Pulumi ESC onboarding experience provides a stylish look](./esc-onboarding-1.png)

## Using Pulumi ESC as an OIDC Provider

Among its many uses, [Pulumi ESC can act as an OpenID Connect (OIDC) provider](/docs/esc/environments/configuring-oidc/), issuing short-lived, signed tokens that external systems can exchange for temporary cloud credentials. This eliminates hard-coded credentials and improves your security posture.

Other Pulumi offerings, such as [Pulumi Insights](/product/pulumi-insights/), use this mechanism to securely scan resources across your organization.

## A simpler way to setup OIDC for your cloud providers

Setting up an OIDC provider manually can involve multiple steps and be error-prone. To simplify this, Pulumi ESC now offers automated setup for AWS, Azure, and Google Cloud directly from the onboarding flow.

![The new Onboarding experience offers a Login Provider Setup for the most popular cloud providers](./esc-onboarding-2.png)

For each provider, we offer different options to adjust to your specific needs, you can just log in with your cloud credentials, and Pulumi Cloud handles the rest or you can create all resources from your own machine using Pulumi CLI.

![You can setup OIDC Providers via multiple options such as giving pulumi permissions through SSO or via executing a program on your local cli.](./esc-onboarding-3.png)

For example, for configuring OIDC for AWS, before you have to go to your AWS IAM Console, create an identity provider, configure the IAM Role, review the trust policy and finally setup your ESC Environment.

Now, you can just use SSO, give Pulumi Cloud permissions to create the necesary resources automatically.

![To setup AWS via SSO you need to provide the SSO start URL and SSO region](./esc-onboarding-4.png)

![AWS will prompt you for permissions to pulumi to create the necessary resources](./esc-onboarding-5.png)

After we have finished setting up the trust relationship with AWS, we'll setup a new ESC environment for you under the specified project.

![A new environment will be created under the project and name you specify](./esc-onboarding-6.png)

Once setup is complete, your new environment is ready to issue short-lived credentials.

```bash
esc run aws-login/tehsis-env -- aws s3 ls
```

You can now access your cloud resources securely. Without worrying about managing long-lived credentials.

## What's next?

This is just the beginning of our work to simplify Pulumi ESC setup and onboarding. We’re continuing to refine how teams configure, secure, and manage environments to make getting started with ESC as smooth as possible.

Try [Pulumi ESC](/docs/esc/environments/) today and see how it can streamline your secrets and configuration management.
