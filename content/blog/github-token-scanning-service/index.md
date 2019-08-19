---
title: "GitHub And Pulumi Join Forces To Ensure Your Pulumi Tokens Are Not Exposed"
authors: ["praneet-loke"]
tags: ["Security", "GitHub", "Token Scanning", "Exposed Token", "Leaked Token", "Pulumi Token Scanning"]
date: "2019-08-19"

meta_image: "feature.png"
---

We are very excited to announce that we have partnered with GitHub to offer our users better protection for their Pulumi Access Tokens.

## Pulumi Access Tokens

Pulumi users by default manage the state of their cloud infrastructure deployments at https://app.pulumi.com. This provides state storage, concurrency control, auditable history and access controls for both individuals and teams working with Pulumi.  Each user and service account can generate one or more Pulumi Access Tokens to be used to authenticate with this service.  These access tokens can be used on both local development machines, as well as in CI/CD systems for automated infrastructure deployments.  These access tokens are sensitive secrets which should never be shared publicly, and in particular should never be committed to source control.

## How GitHub Token Scanning Works for Pulumi Users

With the recent changes to integrate Pulumi with GitHub Token Scanning, GitHub now scans each commit you push to a **public repo** on github.com for any files containing these tokens. When GitHub's [Token Scanning Service](https://developer.github.com/partnerships/token-scanning/) finds a potential match for our tokens, the service will call ours to have us verify the token. Only Pulumi [Access Tokens](https://app.pulumi.com/account/tokens) generated after 6/28 that contain the prefix `pul-` will be matched by the scanning service.

During the processing of the requests from the Token Scanning Service, if we find that the token belongs to a Pulumi account, we will use the primary email on the account to notify the user. We will not, however, revoke the token automatically. So ensure that your account's email address is up-to-date by going to your [profile](https://app.pulumi.com/account/profile) in the Pulumi Console.

The whole process, from the check-in to the email notification, typically takes just a few seconds. So you would likely get notified before you even use the exposed token.

## Avoid Checking-In The Token In The First Place

Pulumi Access Tokens grant access to your stacks. They allow you to login into the CLI non-interactively and thus allow the CLI to access a stack’s configuration, which may in-turn [contain other secrets](https://www.pulumi.com/blog/managing-secrets-with-pulumi/). The token is typically used inside CI/CD environments. So you should never have to check-in a token to your source tree (public or otherwise.)

Most CI/CD services have a way for you to specify secret environment variables that allow you to safely inject them into your build environment. We have written-up quite a few guides on [how to integrate Pulumi into your CI/CD](https://www.pulumi.com/docs/reference/cd/). If you don't see a guide for a CI/CD system that you are using, feel free to create an issue [here](https://github.com/pulumi/docs), or even better, raise a PR for it. We love community contributions. :)
