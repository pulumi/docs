---
title: "Announcing Team Access Tokens for the Pulumi Service"

date: 2022-08-16T14:00:00-07:00

meta_desc: We are launching Team Access Tokens, which allow Organization and Team Admins to create access tokens scoped to a Pulumi Team.

meta_image: meta.png

authors:
    - devon-grove
    - meagan-cojocar

tags:
    - features
    - pulumi-service
---

A few months ago we launched [Organization Access Tokens](/blog/organization-access-tokens/) for the [Pulumi Service](/product/pulumi-service/) and saw overwhelmingly fast adoption from our customer base. Based on this customer demand, and existing customer feedback, we prioritized improvements in the scoping of access tokens. Today, we are launching Team Access Tokens, which allow Organization and Team Admins to create access tokens scoped to a [Pulumi Team](/docs/pulumi-cloud/access-management/teams/). Pulumi Service customers on the Enterprise and Business Critical editions can use Pulumi Teams to set role-based access controls (RBAC) for stacks by enabling Organization administrators to assign a set of stack permissions to a group of users.

<!--more-->

Since Pulumi Teams are only available on these editions, Team Access Tokens are also only available to customers on the Enterprise and Business Critical editions of the Pulumi Service. See the [Team Access Tokens](/docs/pulumi-cloud/access-management/team-access-tokens/) documentation for more information on how to use the feature.

## See it in action!

![Team Access Tokens in the Pulumi Service](https://www.pulumi.com/uploads/team_tokens.gif)

## Hear from our customers

[Snowflake](/case-studies/snowflake/), a Pulumi customer, delivers the Data Cloud, a global network where thousands of organizations mobilize data with near-unlimited scale, concurrency, and performance. “Scoping down access tokens will help our Platform team manage Pulumi stacks at scale across multiple departments within Snowflake. When Organization Access Tokens came out we were quick to adopt them internally and intend to adopt Team Access Tokens now as well. Using Pulumi Teams and Team Access Tokens enables us to follow the principle of least privilege.” said Jonas-Taha El Sesiy, Senior Software Engineer at Snowflake.

## Feature overview

This feature is particularly useful for:

1. Scoping programmatic access for continuous integration and continuous delivery (CI/CD) tools and other automated processes to the Pulumi Team instead of the entire Organization
2. Enterprise customers using SSO/SAML/SCIM, as it enables them to set fine-grained stack permissions to the Pulumi Teams provisioned through their identity provider

Team Access Tokens scope token access down to the stacks a Pulumi Team has access to. Customers can use Team Access Tokens when they need more fine grained access than a Personal Access Token. Personal Access Tokens have full permissions the user has across Organizations, Teams and Stacks. Team Access Tokens have less privilege than Organization Access Tokens, which have access across the Pulumi Organization and across multiple Teams.

With the launch of Team Access Tokens, Pulumi users can now create the following access token types:

- **Personal Access Tokens**: access tokens tied to a user’s access
- **Organization Access Tokens**: access tokens tied to a Pulumi organization’s access
- **Team Access Tokens**: access tokens scoped to a Pulumi Team’s access

This feature is available to all Enterprise and Business Critical customers today, as well as those on our 14-day trial. You can [start a trial](https://app.pulumi.com/site/trial) or [Contact Us](https://www.pulumi.com/contact) about the Pulumi Enterprise Edition and Business Critical Edition to take it for a spin!
