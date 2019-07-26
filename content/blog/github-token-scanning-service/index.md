---
title: "GitHub And Pulumi Join Forces To Ensure Your Pulumi Tokens Are Not Exposed"
authors: ["praneet-loke"]
tags: ["Security", "GitHub", "Token Scanning", "Exposed Token", "Leaked Token"]
date: "2019-08-01"

meta_image: "feature.jpg"
---

We are very excited to announce that we have partnered with GitHub to offer our users better protection for their Pulumi Access Tokens.

## How It Works

GitHub scans each commit you push up to a **public repo** on github.com for any files containing these tokens. When GitHub's [Token Scanning Service](https://developer.github.com/partnerships/token-scanning/) thinks that there is a potential match for one their partner's tokens, their service will call ours to have us verify the token. Only Pulumi [Access Tokens](https://app.pulumi.com/account/tokens) generated after 6/28 will contain the prefix `pul-`.

During the processing of the requests from the Token Scanning Service, if we find that the token belongs to a Pulumi account, we will send the user an email notifying of the incident. We will not, however, revoke the token automatically. Ensure that your account's email address is up-to-date by going to your [profile](https://app.pulumi.com/account/profile) in the Pulumi Console.

Then whole process, from the "fateful" check-in to the email notification, typically just takes a few seconds. So you would likely get notified before you even use the exposed token.

## Avoid Checking-In In The First Place

Pulumi Access Tokens give you access to your stacks. They allow you to login into the CLI non-interactively. This is typically used inside CI/CD environments. So you should never have to check-in a token to your source tree (public or otherwise.)

Most CI/CD services have a way for you to specify secret environment variables that allow you to safely inject them into your build environment. We have written-up quite a few guides on [how to integrate Pulumi into your CI/CD](https://www.pulumi.com/docs/reference/cd/). If you don't see a guide for a CI/CD system that you are using, feel free to create an issue [here](https://github.com/pulumi/docs), or even better, raise a PR for it. We love community contributions. :)
