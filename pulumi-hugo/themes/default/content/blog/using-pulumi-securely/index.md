---
title: "Using Pulumi Securely"

date: 2022-10-13

meta_desc: See how to use organization access tokens, team access tokens, teams and managed federated identities to make your Pulumi usage more secure.

meta_image: meta.png

authors:
    - tushar-shah

tags:
    - security
    - pulumi-enterprise

---

Cloud computing’s greatest strength and weakness is the proliferation of a massive number of services globally. To adequately assess and mitigate the inherent risks for your company, customers, and employees, cloud architects are typically responsible for a vast surface area of potential endpoints and vectors of attack.

<!--more-->

## Cloud Security Posture

AWS likes to talk about a [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/), their friendly way of saying, “we’ve got our stuff covered, and if you’re compromised, it’s almost certainly your fault.”  They have built up practices and recommendations, like the AWS Well-Architected Framework. Their pillars of architecture philosophy give you your best chances to securely use their resources (following these recommendations is easy with [Crosswalk for AWS]({{< relref "/docs/guides/crosswalk/aws" >}}) from Pulumi). Increasing high-profile attacks against private and open-source software supply chains have developers increasingly on high alert and conscious of incorporating more security into their DevOps.

Risks associated with maintaining a good cloud security posture extend to your infrastructure as code with Pulumi and it’s important to leverage the features and capabilities of the Pulumi platform along with good industry practices to secure your code, configuration and secrets.

## Pulumi’s Hierarchy

Pulumi has three levels to consider access for: users, teams and organizations.

[Organizations]({{< relref "/docs/intro/pulumi-service/organizations" >}}) are a space for you to collaborate on shared projects and stacks.  You may have multiple cloud accounts from a single cloud provider or multiple cloud provider accounts tied to an organization in any combination.  It’s recommended that you segment organizations and cloud accounts to limit access and the “blast radius” of security or financial events that may occur within them.

[Teams]({{< relref "/docs/intro/pulumi-service/teams" >}}) are groups of users within an organization with specific permissions to stacks.  Consider using these to break up access to environments such as dev, staging and production.  You should look to mirror your code repository or IAM teams/groups as much as possible.

[Users]({{< relref "/docs/intro/pulumi-service/accounts" >}}) are tied to personal identities, often with an identity provider and should be used wherever a human is using Pulumi.  These identities should not be used for any systems, tools or pipeline-based provisioning.

## Security Best Practices with Pulumi

The following recommendations should help you get started and prepare you to scale your company, application and cloud engineering team long term.

### Manage Federated Identity

Connect your user and Pulumi organization with an [Identity Provider]({{< relref "/docs/intro/pulumi-service/organizations#organization-identity-providers" >}}) such as [Github]({{< relref "/docs/intro/pulumi-service/organizations#github-identity-provider" >}}), [Gitlab]({{< relref "/docs/intro/pulumi-service/organizations#gitlab-identity-provider" >}}) or [BitBucket]({{< relref "/docs/intro/pulumi-service/organizations#bitbucket-identity-provider" >}}), your [Single Sign On (SSO)]({{< relref "/docs/intro/pulumi-service/organizations#saml-single-sign-on-sso" >}}) system and/or another [System for Cross-Domain Identity Management]({{< relref "/docs/guides/scim" >}}) (SCIM).  Your code repositories hold your Infrastructure as Code, and most organizations are motivated to keep access tightly controlled.  SSO improves this process across tools and puts more control into your organization’s hands.  SCIM enables you to manage your users and groups centrally in your Identity Provider (IdP) and then synchronize those users and groups to the Pulumi Service.  Leveraging your existing onboarding and offboarding process will help limit the risk of bad actors in Pulumi itself.

### Build Pulumi Teams

[Teams]({{< relref "/docs/intro/pulumi-service/teams#creating-a-team" >}}) improve on basic role-based access control (RBAC) for administrators and users by allowing you to group users and their access to specific stacks in your organization.  For example, a team called `productionreadonly` could be created and scoped so that all members have only limited access to read the production stacks, while another team, `productionadmins`, would retain full privileges to those stacks.

### Import Manually Created Resources

Manually created cloud resources are error-prone and difficult to audit, iterate and improve on.  If you’ve created manual resources, consider [importing]({{< relref "/blog/changes-to-import" >}}) them to Pulumi programs.

### Tag your Stacks

We have previously covered [Tag Policies]({{< relref "/blog/automatically-enforcing-aws-resource-tagging-policies" >}}) as a best practice for the cloud resources themselves. Still, you can also tag your Pulumi stacks to help organize and visualize your application resources in logical groupings that will help you assess, respond and automate incident remediation. Here are two examples of using tagging your stacks automatically: in [Python](https://github.com/pulumi/examples/blob/master/aws-py-stackreference/team/__main__.py#L8-L13) and [TypeScript](https://github.com/pulumi/examples/blob/master/aws-ts-stackreference/team/index.ts#L17-L22).

### Deploy from Pipelines

Automate every step of your deployment process for anything beyond local development by creating CI/CD pipelines. Manual approval steps in your pipeline should be avoided. Consider creating automated checks to ensure your infrastructure is created only with approved [Pulumi Packages]({{< relref "/docs/guides/pulumi-packages" >}}) and automatically ensure your infrastructure is in compliance by using [CrossGuard]({{< relref "/docs/guides/crossguard" >}}).

Leveraging [Automation API]({{< relref "/docs/guides/automation-api" >}}) as the programmatic interface for running Pulumi programs without the Pulumi CLI is a strongly typed and safe way to use Pulumi in embedded contexts such as web servers without having to shell out to a CLI. For example, [Elkjop Nordic uses Automation API to provide a self-service portal]({{< relref "/blog/how-elkjop-nordic-enables-developers-to-self-serve-infrastructure" >}}) that serves as a secure IT vending machine full of their application and infrastructure building blocks.

### Log Everything

Track key system events such as user and pipeline activity, attempted and restricted activity, and identity and access control changes. Use Pulumi audit logs to simplify this process out of the box. If applicable, we would suggest automatically exporting [Pulumi Audit Logs]({{< relref "/docs/intro/pulumi-service/audit-logs#automated-export" >}}) to your systems.

### Use Tokens

Organization Access Tokens, Team Access Tokens and Personal Access Tokens securely connect your automation pipelines and development environments with Pulumi without the risks of association user/password combinations.  Machines talk to Pulumi with tokens of various types, and it is always advisable to use Tokens over Users where possible. More on the types of tokens is below.

#### Organizational Access Tokens

These are scoped to the entire Pulumi organization.  Use these for tooling with broad access across stacks and resources deployed in that organization.  For example, if your production environment runs in an isolated cloud account and organization, then an [Organization Access Token]({{< relref "/docs/intro/pulumi-service/organization-access-tokens" >}}) is likely appropriate for your CI/CD pipeline that deploys production.

#### Team Access Tokens

Scoped to the [stack access]({{< relref "/docs/intro/pulumi-service/team-access-tokens#stacks" >}}) of a Pulumi team.  Use these when resources associated with different environments or services are commingled within a single cloud account or organization.  In general, it is often recommended to create a [Team Access Token]({{< relref "/docs/intro/pulumi-service/team-access-tokens" >}}) for each CI/CD pipeline, for example, `dev` vs `production`.

#### Personal Access Tokens

Scoped to [individual users]({{< relref "/docs/intro/pulumi-service/accounts#access-tokens" >}}). Used whenever a developer deploys from their local machine.  Be sure your users are part of a Pulumi team to simplify their role-based access within the platform.

### Rotate the Tokens

Add Pulumi to your list of tokens to rotate on a regular basis.

### Assessing and Implementing

Even if you’ve been using Pulumi for a while, we recommend you regularly take these three steps to continuously audit and improve your cloud security posture as it relates to your infrastructure as code:

1. Confirm your users', teams', and organization access are in line with either or both your code access or cloud access policies; make any necessary updates to access, permissions or scope of privilege.
1. Audit any pipeline that uses Pulumi and ensure that they use fresh, rotated tokens.
1. Review your audit logs regularly, noting any abnormal or unexpected activity. It is advisable to export these audit logs and process them with a security event management system.

Some of the features mentioned, such as teams, SSO/SCIM and audit logs, are only available to Enterprise and/or Business Critical Edition users and those on our 14-day trial. If you would like to implement and/or test any of these features please [start a trial](https://app.pulumi.com/site/trial) or [contact us]({{< relref "/contact" >}}) for access.
