---
title: "Keeping Your Secrets Secret"
date: 2021-03-23
meta_desc: "Passwords, tokens, and environmental variables are secrets needed to for infrastructure to run. Learn how to protect them and your infrastructure."
meta_image: secrets.png
authors:
    - sophia-parafina
tags:
    - security
    - secrets

---

Companies that have suffered data breaches are, unfortunately, frequently in the news. A data breach is when information that should be private, such as credit card numbers or even trade secrets, is stolen. These thefts can be because of an actual cyber-attack, but they can also be due to simple carelessness, such as disposing of computer equipment without taking proper precautions.

<!--more-->

As an example, Bitcoin miners have perpetrated many data breaches. Suppose you accidentally push a dotfile with an **aws_access_key_ID** to GitHub.  Bitcoin miners have a host of tools that automatically scrape GitHub for exactly that sort of information. Once they have your AWS credentials, they lock you out, spin up machines and start mining. This isn’t as common as it once was since cloud providers are better at detecting these sorts of incursions, but you can see how catastrophic (and costly) such a data breach can be.

Of course, you can protect yourself and your company. In this blog post, we’re going to give a quick rundown of some actions you can take to make sure your secrets stay secret.

## What Is a Secret?

We’re going to define secrets as small, critical pieces of information. They’re no larger than a few KBs, and they’re necessary to run your infrastructure. If they're leaked, your infrastructure is compromised and bad things can happen. Some examples of secrets are passwords, API keys, and SSH keys.

## Remove All Plaintext Secrets

Step one is to search through your existing codebase and remove any secrets that are in plaintext. A simple approach is to manually **grep or search** through your files, looking for words such as `username` and `password`. However, there are also tools available that will comb through your Git history and commits, looking for sensitive information. Many of these tools are open source.

### Build detection into your CI/CD pipeline

Making secrets detection a part of your CI/CD pipeline is a great way to ensure you’re not pushing confidential information to a public repo. There are tools that integrate into your automated workflow. You can configure those tools to stop the pipeline if they detect secrets such as keys or passwords.

### Don’t Forget about Git Commits

It’s easy to forget that Git commits can contain sensitive information. For example, someone might talk about a security issue and how they fixed it. Instead, give a link to your ticketing system and document the problem there.

## Encrypt and Manage Your Secrets

After you’ve stripped out your plaintext secrets from your codebase, you still need to to store and manage them securely. Encrypting secrets rather than storing them as plaintext is a good start.

### Manual encryption

There are command-line tools for encrypting secrets, such as GPG (also called GnuPG) and PGP, which stands for Pretty Good Privacy. These are free, but many people find them difficult to use, and standard security practices such as rotating your keys can be challenging to implement.

### Secret servers

There are many servers that store secrets securely available on the market. Secret servers encrypt your secrets and usually have many other features that encourage best security practices, such as access control lists and the ability to audit who’s accessing your keys.

## Cloud-provided services

Given that many companies have their infrastructure in the cloud, it makes sense to consider using the secrets services that your cloud provider offers. To mention a few, Google Cloud has [Secret Manager](https://cloud.google.com/secret-manager), AWS has the [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), which relies on the [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/), and Microsoft Azure has [Key Vault](https://azure.microsoft.com/en-us/services/key-vault/). These services have many built-in capabilities that enable you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

## Have a Plan

Mistakes happen and, even if you’re careful, leaks can occur. It’s important to have a plan already in place if you’ve detected a data breach. Here are some of the things you should do.

- Reset passwords and create new keys.
- Monitor your systems to find anomalies and unusual usage.
- Destroy as many machines as you can and spin up new instances with new credentials.
- Keep track of what you’ve done so that you can have a meaningful post-mortem once you’ve put out the fires.

If you haven’t done so already, consider installing intrusion-detection systems. There are many on the market, including open-source tools.  There’s no single answer for what to do when leaks happen, but it’s important that all the stakeholders get together and put a process in place.

### Practice makes perfect

Once you have a plan, consider staging a data breach and follow that plan to see how well it works. For example, you might simulate a spoofing attack or have someone “steal” a laptop and see how much damage they can do.

## Move Security to the Left

Security should be as much a part of your workflow as any other phase of the development process. Just as you start testing your code early to find bugs, you should test early to find security problems. Security shouldn’t come at the end of the development cycle when you think you’re production-ready. Just as with any other problem, security issues are much easier to fix early in development.

## Learn More

Pulumi takes security risks seriously. That’s why our platform is secure by default. It protects all secret data using Pulumi’s built-in secret storage, a secret store that “just works.” We also support all the major cloud-provided secret services. Want to learn more? Visit [pulumi.com](https://www.pulumi.com/) or [get started](/docs/get-started/) for free today.
