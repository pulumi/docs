---
title: "Managing AWS Credentials on CI/CD"
date: 2020-03-12
meta_desc: "Best practices for managing AWS credentials on CI/CD"
meta_image: meta.png
authors:
    - chris-smith
    - sophia-parafina
tags:
    - CI/CD
---

Continuous delivery requires providing highly sensitive credentials to your
deployment pipeline. Understanding the risks, mitigations, and best practices
for handling those credentials can be difficult. In this guide, we describe the
best practices for providing AWS credentials to a CI/CD system and to securely
automate updating your cloud infrastructure using Pulumi.

<!--more-->

You’ve heard about *Infrastructure as Code* and decided to try your hand at using Pulumi to manage cloud infrastructure using real programming languages. Naturally, you’re curious and eager to start updating your cloud infrastructure in your CI/CD pipeline – but then panic hits... Is updating your cloud infrastructure secure? If you start doing cloud deployments in your CI/CD system, doesn’t that mean you need to give it your production credentials? Aren’t those the most sensitive things your company has?!?

**Take a deep breath**. It’s going to be OK. You _can_ securely provide AWS credentials to your CI/CD system and practice continuous delivery. This is the first post
in a series going in-depth on how to do just that.

The goal of this article series is to give you a clear understanding of AWS credential management and how that relates to using Pulumi within a CI/CD environment.
Once you have the AWS credentials in-place, you can then follow our [Continuous Delivery](https://www.pulumi.com/docs/guides/continuous-delivery/) guide for
configuring your specific CI/CD service, whether you want to use [CircleCI](https://circleci.com), [GitLab CI](https://about.gitlab.com/product/continuous-integration/), or
[Travis CI](https://travis-ci.org).

> **NOTE:** These recommendations do not apply if you are running your own CI/CD system within your
> AWS account, e.g., running a Jenkins server on EC2 or using [AWS CodeDeploy](https://aws.amazon.com/codedeploy/).
> In those cases, please refer to AWS's documentation for how to
> [assume IAM Roles when running on an EC2 instance](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)
> instead.

## Overview

The recommendations in this series describe a general "one-size fits most" approach for credential
management, which requires a minimal amount of work to configure and maintain. Depending on your
specific environment, needs, and constraints, there may be a better alternative for your use case.

Here's the full set of steps in our series, walking through the creation of a secure CI/CD environment
to deploy AWS resources using Pulumi:

- [Create a dedicated IAM User for your CI/CD](#create-new-iam-user)
- Provide the IAM User’s credentials to your CI/CD system
- Comparison with using hosted secret managers
- Automate Rotating and Revoking AWS Credentials
- _Assuming IAM Roles for performing updates_ (coming soon!)
- _Securing sensitive data using Pulumi_

## Create a dedicated IAM User for your CI/CD {#create-new-iam-user}

The first step for securely automating CI/CD is to create a dedicated IAM User for use in your CI/CD
pipelines. (Sometimes referred to as a "robot account.")

The following code snippet shows how to create a new AWS IAM User using Pulumi. (The code is in TypeScript,
but you could another language like Python, C#, or Go as well.)

```ts
const user = new aws.iam.User("cicdUser", {
    name: "cicd-bot",
    tags: {
        "purpose": "Account used to perform Pulumi stack updates on CI/CD.",
    }
});
```

By default, that IAM User doesn't have permissions to do anything. The recommended best practice
is to [use groups to assign permissions to IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#use-groups-for-permissions).
So next, we will create a "Pulumi Stack updaters" IAM Group, and add our robot account as a member.

```ts
const group = new aws.iam.Group("pulumiStackUpdaters", {
    name: "PulumiStackUpdaters",
});

const groupMembership = new aws.iam.GroupMembership("cicdUserMembership", {
    group: group.name,
    users: [ user.name ],
});
```

### Group Permissions

The next part is where things start to get tricky. We now need to grant permissions to this IAM
Group's members so they can access various APIs and resources. (For example, if your Pulumi program
will need to create or update EC2 instances, then you will need to provide AWS credentials that
contain the `ec2:StopInstances` or `ec2:StartInstances` action.)

But rather than grant the newly created `cicd-bot` IAM User those permissions, we will
instead only grant them access to the `sts:AssumeRole` action. This is an AWS API that allows an IAM
User to gain temporary credentials that have a different set of permissions associated with them.
(That is, the permissions associated with an _IAM Role_.)

We'll go into more detail about the exact difference between an IAM User and an IAM Role in the next
post in the series since it isn't entirely obvious why one would be more secure than the other.

```ts
const currentAwsIdentity = aws.getCallerIdentity();

const groupPolicy = new aws.iam.GroupPolicy("pulumiStackUpdatersPolicy", {
    group: group.name,
    policy: {
        Version: "2012-10-17",
        Statement: [{
            Action: [
                // Allow anybody (i.e., members of the group) to call the sts:AssumeRole API.
                // This allows them to "assume the role" of a more permissive IAM Role
                // when they go to update a stack later.
                "sts:AssumeRole",
            ],
            Effect: "Allow",
            // This is the set of resources that the "sts:AssumeRole" operation could be
            // performed on, which is to say any IAM role in the current AWS account.
            Resource: pulumi.interpolate `arn:aws:iam::${currentAwsIdentity.accountId}:role/*`,
            Sid: ""
        }],
    },
});
```

That's it for the first post in our series. We've taken the first step and created an IAM User specifically for performing updates to AWS resources using Pulumi.

In the next post, we will review over the security concerns when passing AWS credentials to your CI/CD provider, as well as show a Pulumi program that you can use to rotate the AWS credentials for a user automatically.
