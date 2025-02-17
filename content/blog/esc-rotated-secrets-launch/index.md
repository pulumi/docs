---
title: "Introducing Rotated Secrets in Pulumi ESC"
allow_long_title: true
date: 2025-02-18T00:00:00-04:00
draft: false
meta_desc: "Pulumi ESC's Rotated Secrets automates credential rotation, enhancing security, reducing manual effort, and ensuring compliance for long-lived secrets"
meta_image: "meta.png"
authors:
  - claire-gaestel
  - arun-loganathan
tags:
  - esc
  - secrets
  - features
---

Managing secrets effectively is no longer a "nice-to-have"—it's a must-have for any organization building and scaling applications in the cloud. Static, long-lived credentials like database passwords, API keys, and IAM user credentials are a major security vulnerability. They're often overexposed, residing in source code, configuration files, or other easily accessible locations. Manual rotation processes are tedious, error-prone, and infrequent, leaving a wide window of opportunity for potential breaches. Today, we're thrilled to announce a powerful new capability in [Pulumi ESC](/product/secrets-management/) that directly addresses this challenge: Rotated Secrets.

<!--more-->

## The Challenge with Static Secrets: A Ticking Time Bomb

Traditional secrets management often relies on static, long-lived credentials. This approach creates several critical problems:

- **Increased Attack Surface**: The longer a secret remains unchanged, the greater the chance it will be compromised through accidental exposure, phishing attacks, or insider threats.
- **Manual, Error-Prone Rotation**: Manual rotation processes are time-consuming and require significant coordination across teams. A single mistake can lead to application downtime or even data breaches.
- **Inconsistent Practices**: Ad-hoc scripts and manual procedures often lead to inconsistent rotation policies, making it difficult to enforce security best practices across the organization.
- **Compliance Headaches**: Many compliance regulations (like SOC 2, GDPR, and HIPAA) require regular secret rotation. Manual processes make it difficult to demonstrate compliance and can lead to costly penalties.

These challenges are amplified in complex, multi-cloud, hybrid, or on-premises environments where secrets are distributed across numerous systems. Organizations need a better way – a solution that automates the process, minimizes risk, and integrates seamlessly with their existing workflows.

## Introducing ESC Rotated Secrets

Pulumi ESC's new Rotated Secrets feature provides an elegant solution to the challenges of secret lifecycle management. It enables automated, seamless rotation of credentials, ensuring that your secrets are always up-to-date and secure. Here's how it solves the problems outlined above and more: 

- **Automated Rotation Schedules**: Define flexible rotation schedules (e.g., every 30 days, 60 days, or a custom interval) tailored to your security and operational requirements. This eliminates manual effort and ensures consistent, frequent rotations.
- **On-Demand Rotation**: Need to rotate a secret immediately due to a suspected breach or policy change? ESC allows you to trigger rotations on demand, giving you immediate control.
- **Seamless Integration with ESC Environments**: Rotated secrets are seamlessly integrated into your existing ESC environment definitions. This allows you to leverage the power of ESC's [composability](/docs/esc/environments/imports/), allowing you to manage rotated secrets alongside your other configuration values.
- **Two-secret strategy**: ESC Rotated secrets uses a two-secret strategy in which two secrets are active and valid at any point in time. This is especially useful when multiple instances of an application share a credential but not all instances pull in the latest credential at the same time, allowing you to rotate a secret without worrying about some instances being unavailable due to invalid credentials. 
- **Auditing and Tracking**: Gain complete visibility into credential usage, including a full history of generated credentials, active credentials, and the principals accessing them. This enhances governance and simplifies compliance.
- **Admin and Creator Control**: Admins and creators/writers of rotated secrets can configure rotations using privileged user credentials and keep those credentials private while ensuring the consumers can still consume the resulting rotated secrets. This provides a clear separate of concern for administration and individual usage. 
- **Configure [webhooks](/docs/esc/environments/webhooks/) for automation**: Notify teams, trigger custom workflows, or trigger a [Pulumi Deployment](/docs/pulumi-cloud/deployments/) to update your [IaC stacks](/docs/iac/concepts/stacks/) whenever rotations occur, ensuring dependent teams and systems are updated on a timely basis

With Today’s launch, we support AWS IAM user credential rotation with many more databases and cloud integrations on the way. 

## How to Use ESC Rotated Secrets

Here’s how to configure [AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) rotated secrets using best practices:

#### 1. Provision an AWS IAM User on your AWS Console 
[Create an AWS IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) whose access keys you want to rotate.

#### 2. Create a new environment with managing user credentials
In the example environment `credentials/aws-creds` below, we use the ESC’s [aws-login provider](/docs/esc/integrations/dynamic-login-credentials/aws-login/) using OIDC. This credential configured has the privileged access to be able to rotate the IAM user credentials. 

```yaml
# credentials/aws-creds

values:
 aws:
   login:
    fn::open::aws-login:
     oidc:
      duration: 1h
          roleArn: arn:aws:iam::012345678912:role/role-abcd123
          sessionName: pulumi-esc

```

#### 3. Create a new environment with the IAM user rotation configuration
Define the rotation using rotated secrets aws-iam provider. Below is an example definition. Notice how the managing user credentials created in step 2 is references in the rotation provider `input`. This credential will only be used during rotation and never be exposed to the consumers of the rotated IAM user credential. 

Providing current and previous credentials is optional. If you already have IAM user access keys that are being actively used, you can specify them in the `state` field as `current` and `previous`. If not, you can leave the state empty.

```yaml
values:
  rotated-creds:
    fn::rotate::aws-iam:
      inputs:
        region: us-west-1
        login: ${environments.credentials.aws-creds.aws.login}
        userArn: arn:aws:iam::{accountId}:user/{username}
      state:
        current:
          accessKeyId: AKIA...
          secretAccessKey:
            fn::secret: ASIA....
        previous:
          accessKeyId: AKIA...
          secretAccessKey:
            fn::secret: ASIA....
```

#### 4. Test the setup with a manual rotation 
In the Environment Editor screen,  open the triple-dot menu and select Rotate Secrets. Alternatively, you can perform the rotation from the ‘secrets rotation’ tab or use the rotate CLI command. Every rotation creates a new [revision](/docs/esc/environments/versioning/). 

If you did not provide current or precious credentials in step 3, rotation will generate new credentials automatically. 

#### 5. Monitor Rotations
Perform multiple rotations to observe how access keys move from current → previous → deleted. Use the Environment Revision History to track changes.

#### 6. Schedule Rotations
Now that you’ve correctly configured your rotated secrets, set up an automated rotation schedule from the Secrets Rotation tab. 

**Add GIF**

## Rotated Secrets vs. Dynamic Credentials: Choosing the Right Tool

Pulumi ESC offers both [Dynamic Secrets](/docs/esc/integrations/dynamic-login-credentials/) and Rotated Secrets. While both enhance security, they serve different purposes:

- **Dynamic Secrets**: These are short-lived, ephemeral credentials with a Time-To-Live (TTL) typically ranging from 1 to 8 hours. A new set of credentials is generated every time the environment is opened. This is ideal for minimizing the impact of compromised credentials, as they quickly become invalid.
- **Rotated Secrets**: These are longer-lived credentials, potentially lasting for days, weeks, or even months. The same, latest credential is returned every time the environment is opened until the next scheduled rotation occurs. This provides stability and predictability for applications that need consistent credentials over a longer period.


Here are scenarios where rotated secrets are the preferred choice:

- **Applications That Can Only Update Credentials During Restarts and Redeployments**: Some applications require credentials to be available at startup and cannot refresh them dynamically. Rotated Secrets works well for this scenario, providing rotations and ensuring applications always have a valid credential when restarted.
- **Applications Requiring Persistent Connections**: High-performance applications or applications that have a long-lived database connections cannot afford to fetch fresh credentials every few hours. Rotated Secrets ensure such applications continue to function as needed while boosting security.  
- **Gradual Migration from Static Credentials**: For teams transitioning from hardcoded credentials, Rotated Secrets provide a secure path by automating secret updates without requiring immediate application changes.
- **Third-Party API Keys (Support coming soon)**: Some external services cannot provision dynamic short-term credentials. Rotated Secrets provide a way to comply with periodic key rotation policies without requiring real-time credential generation.
- **Databases in Private Networks (Support coming soon)**: Many Enterprise databases are not connected to the internet, thereby requiring a proxy or an agent running in their internal network to perform the rotation. Rotated Secrets offer stability in such environments by reducing the number of external calls, even when routed through a proxy.

## What's Next?

This is just the beginning! We're committed to expanding the capabilities of Rotated Secrets. Here's a glimpse of what's on the roadmap:

- Database Secrets Rotation: Automated secrets rotation support for a wide range of databases including **PostgreSQL, Snowflake, MySQL**, and more!
- Secret rotations for databases running in private networks 
- 3rd party API key rotation (example: **Twilio**)
- Other cloud provider support: **Azure, GCP**

Want an integration not mentioned? Click [here](https://github.com/pulumi/esc/issues) to raise a request. 

## Conclusion

Pulumi ESC's Rotated Secrets feature represents a significant advancement in modern secrets management. By automating a traditionally manual and error-prone process, ESC reduces operational risks, strengthens your security posture, and helps you achieve compliance – all without slowing down development. 

We encourage you to explore the docs and try out Rotated Secrets. Share any feedback or open new issues in our [GitHub repository](https://github.com/pulumi/esc/issues). We're excited to see how you use this powerful new feature to build more secure and resilient applications!
