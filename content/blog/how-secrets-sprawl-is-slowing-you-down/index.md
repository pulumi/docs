---
title: "How Secrets Sprawl is Slowing You Down—And What to Do About It."
allow_long_title: true
date: 2024-10-28T12:40:10+02:00
draft: false

meta_desc: "Secrets sprawl is a real problem that can slow down our teams and impact
  our productivity. But it also affects how fast an organization can scale its development
  and operations teams. Learn how to overcome secrets sprawl and regain your productivity."

meta_image: meta.png

authors:
  - engin-diri

tags:
  - esc
  - secrets-management
  - secrets-sprawl
  - pulumi


social:
  twitter: |
    Get rid of secrets sprawl and regain your productivity. 
    Learn how to overcome secrets sprawl and regain your productivity with Pulumi ESC. 
  linkedin: |
    Secrets sprawl is a real problem that can slow down our teams and impact our productivity. 
    But it also affects how fast an organization can scale its development and operations teams. 
    Learn how to overcome secrets sprawl and regain your productivity.
search:
  keywords:
    - Secrets
    - Management
    - Productivity
    - Secrets sprawl
    - Centralized management
---

Only a few things are certain in the lives of developers and DevOps engineers: taxes, yearly performance reviews, and secret sprawl. While the first two are inevitable, the last one is something that can be managed.

As we keep adding new cloud resources and releasing new applications, the number of secrets we need to manage keeps growing: passwords, API keys, certificates, and more. And as if this isn't enough, we need to manage secrets across different systems and environments with different teams that need to access them; we end up with duplicates.

Let's have a look at a typical environment and see what teams use: Everything container-related may use Docker secrets or Kubernetes secrets. There is also a high chance that they might use cloud-specific secrets managers like Azure Key Vault, AWS Secrets Manager, or Google Secret Manager. In addition to these, there is a high chance that they might use HashiCorp Vault or some enterprise-grade secrets manager like CyberArk.

There are still a lot of organizations that store their secrets (like the API key for a cloud service) in environment variables to configure their applications on virtual machines, containers, or serverless functions. And as if that weren’t risky enough, some developers still hardcode sensitive information in their application code. Or use plain unencrypted text files such as .env files and share them inside the team. To be fair, this is not something that is done on purpose, and most teams realize the risks of these practices. But the problem is that they have not found a better way to manage their secrets that won't slow them down and impact their productivity.

As the IT infrastructure grows, it becomes increasingly challenging for organizations to secure, organize, and distribute their secrets. This is where secrets sprawl comes into play. Secrets sprawl is the uncontrolled and unmanaged distribution of secrets across different systems and environments.

Modern architectures are adding to the problem of secret sprawl as modern applications are more distributed and consist of smaller building blocks with a growing number of different technologies.

While teams are ensuring that each of their applications has everything it needs to run, it's also easy for them to lose track of the secrets they are using. Everything can be fine until they need to rotate a secret or revoke a compromised one. Then they need to go through all the systems and environments to find and update the secret. Tracking down all the places where a secret is used can be a time-consuming and error-prone process with a high risk of missing some places.

So what are some of the pain points of secret sprawl, and how can we overcome them to regain our productivity?

### Pain Points of Secrets Sprawl

With secrets sprawled all across our teams (development and operations) and infrastructure, we face several points:

1. It is challenging to keep track of all the secrets and where they are used. When we need, for example, to find a specific secret, we need to go through different secret managers, code, and, in the worst case, the local files of one of the developers.

   Do we need to rotate a secret? Now we need to go through all the systems and environments to find and update every duplicated secret.

1. Security risk is another pain point to mention. When a secret is spread throughout the organization, it's hard to manage access control and enforce specific access policies.

   Security best practices also recommend that secrets should be rotated regularly. But with secrets sprawled all over the place, it makes it a lot of work to rotate them. Time we could spend on more important tasks like developing new features.

1. Secrets sprawl makes it extremely challenging to distribute secrets. Having a secret, for example, in a cloud provider's secret manager is cool and great, but what if we need to use it in a Kubernetes cluster? What is the process for that?

   Also, having secrets in multiple places means there are different owners for them. These secrets are now some kind of gatekeeping by the team that owns them. This makes it hard for other teams to access them when they need them. And even if they get access, they will then be mostly shared in plain text as the other team does not have access to the secret manager itself.

As we can see, secret sprawl is a real problem that can slow down our teams and impact our productivity. But it also affects how fast an organization can scale its development and operations teams.

With an "organic" way of managing secrets and no real transparency, it's hard to keep up with the pace of the business, and secret sprawl becomes a major bottleneck. Additionally, that growth means a whole bunch of new secrets that need to be managed.

> Rinse and repeat.

But behold, there is a solution to this problem. And it's called centralized secrets management.

### Centralized Secrets Management against Secrets Sprawl

The cure for secrets sprawl is centralized secrets management. When you centralize your secrets in one place, you know where they are and who has access to them.

This makes it easier to manage access control and enforce specific access policies. It also makes it easier to rotate secrets as you only need to do it in one place.

Have a look at an example scaling of an organization or team:

When the company is small, the team decides to use Kubernetes to deploy their applications, and they store their secrets in Kubernetes secrets. This first step is already a centralization of secrets as it tightens access to the secrets and makes it easier to audit them. Maintaining an encrypted secrets store and centralizing the secrets in one place is a good start and ensures the organization is following a consistent threat protection policy.

As the company grows, one DevOps engineer is responsible for multiple Kubernetes clusters. In these cases, individual users can't enforce their own application-wide policies, meaning secrets are better managed and controlled.

But what if the company grows even more and the team decides to use multiple cloud providers? There are many reasons for this, like costs, different service offerings, and better disaster recovery when using multiple cloud providers.

Sticking to the built-in secrets managers of the cloud providers is not a good idea as it will lead to secrets sprawl.

{{< related-posts >}}

### Why Pulumi ESC is the right choice for centralized multi-cloud secrets management

Pulumi ESC is the right choice for centralized multi-cloud capable secrets management as it reduces secrets sprawl by centralizing secrets storage with a lot of integrations for a wide range of platforms.

Pulumi ESC delivers a seamless integration so you can still use your existing secrets managers like Azure Key Vault, AWS Secrets Manager, Google Secret Manager, or HashiCorp Vault. Secrets are automatically synced to Pulumi ESC, saving developers a lot of time so they can focus on their main tasks like developing and building new products and features.

Pulumi ESC is a completely managed service that again saves time and resources for the organization as they don't need to worry about the infrastructure, maintenance, and support of their self-hosted secrets manager.

### Wrapping Up

Every organization faces the risk of secrets sprawl as they grow and add more cloud resources and applications, which they may not even be aware of.

Multi-cloud scenarios make it even more challenging to manage secrets across different systems and environments.

As teams have to juggle between delivering and building new products and features, managing secrets in a secure and efficient way becomes a major bottleneck on productivity and a major security risk. A ticking time bomb that can explode at any time.

Secrets managers can help you reduce secrets sprawl by centralizing secrets storage and providing a seamless way to use, change, and distribute secrets across different systems and environments. Independent of the size of your organization, a startup or a large enterprise, it's never too late to start managing your secrets in a secure and efficient way.

Pulumi ESC is on the way to becoming the best choice to solve the problem of secrets sprawl. Making both developers and security teams happy by providing a secure and efficient way to manage secrets across different systems and environments.

Start using Pulumi ESC and ESO today by creating an account on the Pulumi Cloud Console and begin managing your secrets in a secure and efficient way.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>
