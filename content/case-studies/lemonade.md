---
title: Lemonade
description: |
    Lemonade's Ops team supports a much larger group of developers by using Pulumi to
    standardize infrastructure components and enforce best practices.
meta_desc: |
    Lemonade's Ops team supports a much larger group of developers by using Pulumi to
    standardize infrastructure components and enforce best practices.

customer_name: Lemonade
customer_logo: /logos/customers/lemonade.svg
customer_url: https://www.lemonade.com/

exec_summary: |
    [Lemonade](https://www.lemonade.com/) is a full-stack insurance carrier that uses
    artificial intelligence and behavioral economics to offer homeowners and renters
    insurance in the US, and contents and liability insurance in Europe. Starting with
    legacy Hashicorp Terraform for configuring their infrastructure on AWS, Lemonade
    wanted to take advantage of Pulumi's building-blocks approach to serverless computing
    and provide self-service tools to help their engineering teams to move faster. Pulumi
    helped Lemonade deploy more modern infrastructure features while empowering their
    workforce with scalable infrastructure libraries. With Pulumi, Lemonade's people-first
    approach to insurance can now accelerate innovation --- bringing disruptive products
    and services to a highly-competitive market.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: challenges
    - label: Solution
      anchor: solution
    - label: Results
      anchor: results
    - label: Next Steps
      anchor: conclusion
---

## About Lemonade {#about}

Lemonade was founded in 2015 to provide renters and homeowners with fast, affordable, and
delightful insurance policies powered by AI and behavioral economics. The company reverses
the traditional insurance model by charging a flat fee and giving back leftover money to
charities selected by its customers. Getting a policy is fast and requires zero paperwork,
as is the transparent claim process. Treating insurance as a social good, rather than a
necessary evil, Lemonade has been designed to be socially responsible, donating parts of
unclaimed premiums and company revenue to nonprofit charities in its annual Giveback. The
startup takes its social good seriously and is registered as both a Public Benefit
Corporation and a Certified B-Corp.

## Challenges Faced {#challenges}

Originally a HashiCorp Terraform customer, Lemonade's infrastructure demands changed
rapidly --- placing the infrastructure team in the critical path for new features. Their
team tried to build workarounds with these legacy tools but found that each iteration
increased configuration complexity and wasted finite resources. Their opportunities to
scale were also impacted as the team was unable to integrate business logic into their
original infrastructure due to a lack of programming language support. Lemonade developers
struggled to create more sophisticated infrastructure-as-code deployments and needed a
more complete solution to support both existing and new services.

## Solution: Infrastructure from Repeatable Building Blocks {#solution}

Lemonade chose Pulumi for its ability to deploy infrastructure with reusable libraries
that could be shared between developers, using their preferred language and cloud. Pulumi
also empowers its users to create and deploy serverless components like AWS Lambda and AWS
EKS --- features Lemonade needed to scale in order to support its growing customer base.

Pulumi enabled Lemonade to centralize its processes, managing all AWS components and
automating infrastructure for every environment. Embedded business logic helped ensure
that resources get appropriately sized for each environment --- keeping costs low and
allowing maximum reuse of infrastructure code.

> "With Pulumi, we can utilize our infrastructure much better because we have the ability to
> embed business logic. We're not limited to one-size-fits-all configurations, but can
> actually implement environment-specific customizations for our infrastructure."
>
> --- Igor Shapiro, Principal Engineer at Lemonade

In addition to providing the infrastructure features that Lemonade was looking for,
Pulumi's platform improved Lemonade's CI/CD process via out-of-the-box integration with
Jenkins. By empowering their service owners with the ability to self-provision and deploy
resources alongside their application code, Pulumi helped Lemonade engineers be more agile
when developing, testing, deploying, and scaling new applications and services.

## Results {#results}

Pulumi provided Lemonade with the ability to provision faster and more efficiently, giving
them an opportunity to introduce much-needed features to their network and support
infrastructure. Since Lemonade employs only a handful of infrastructure engineers to
support dozens of its service side engineers, the demands on the service side could easily
exceed the infrastructure team’s capacity - leading to long wait times for new
capabilities when using Terraform. With  Pulumi, the infrastructure team was able to share
libraries that the services engineers could understand and re-use while codifying best
practices in those libraries to enforce company standards. For example, the infrastructure
team used Pulumi to define organizational policies like mandating the use of AWS
CloudTrail, and automated credential rotation for increased security.

> "Pulumi supercharged our infrastructure team by helping us create reusable building blocks
> that developers can leverage to provision new resources and enforce organizational
> policies for logging, permissions, resource tagging, and security. This empowered our
> developer teams to self-provision resources and ship new capabilities faster without
> having to wait for the infrastructure team to deploy new resources on their behalf."
>
> --- Igor Shapiro, Principal Engineer at Lemonade

Lemonade's infrastructure team was able to simplify tasks like automatically computing
CIDR blocks, correctly connecting their networks to the VPC transit gateway and handling
production traffic differently from other environments --- something that simply can't be
done with Terraform.

Using Pulumi to automatically manage its infrastructure has allowed Lemonade’s leadership
to rest easy about the efficiency and security of its infrastructure and ensure that
automated processes are in place for disaster recovery. More than that, Pulumi gave
Lemonade an automatic way to track changes and deploy new features and services at scale.

## Next Steps {#conclusion}

Lemonade is continuing to use Pulumi to uplevel existing infrastructure and provide new
building blocks for its developers and service teams. Its next target is infrastructure
optimization, including the implementation of environment-specific business logic to
structure data management and infrastructure deployment. As Lemonade's engineering team
grows, they also plan to roll out policies for resource provisioning, and further
automating application testing.
