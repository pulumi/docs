---
title: Credijusto
description: |
    Credijusto used Pulumi to help its development team scale to support rapid growth
    while enforcing best practices for their infrastructure.
meta_desc: |
    Credijusto used Pulumi to help its development team scale to support rapid growth
    while enforcing best practices for their infrastructure.

customer_name: Credijusto
customer_logo: /logos/customers/credijusto_logo.svg
customer_url: https://www.credijusto.com

exec_summary: |
    Founded in 2015, [Credijusto](https://credijusto.com/) provides asset-backed loans and
    equipment leases to small and medium-sized enterprises (SMEs). With approximately 300
    employees, it has launched several new financial products at better rates, faster
    delivery, and peerless customer experience when compared to traditional lenders. Its
    operations are supported by an AWS-based hybrid cloud architecture. Pulumi enabled the
    company to migrate quickly and easily from Hashicorp Terraform and other legacy
    configuration tools, which limited their teams' ability to scale. Using Pulumi has
    helped Credijusto to migrate from Amazon ECS to Amazon EKS, and to make use of [AWS
    Lambda](https://aws.amazon.com/lambda/) using real programming languages. This enables
    the company to modernize its infrastructure quickly and cleanly, ensuring reliability
    and accelerating recovery times when needed. Beyond infrastructure configuration and
    deployment, Credijusto is going one step further in using the new Pulumi CrossGuard
    "Policy as Code" capabilities to ensure that engineering teams stand up new services
    that comply with company standards.


sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges
      anchor: challenges-faced
    - label: Results
      anchor: results
    - label: Conclusion
      anchor: new-opportunities
---

## About Credijusto

Credijusto is a new generation of credit for emerging markets. It evaluates the financial
situation of SMEs and provides personalized service to enable clients to access funding
quickly. With national coverage, it has served thousands of companies in Mexico and is
growing at a monthly rate of 15%. Through the Credijusto platform, millions of companies
can obtain access to credit in a fraction of the time and effort required with traditional
banks. Its credit models are focused on the health of each business, focusing on overall
performance, rather than considering only the owner's personal credit history.

## Challenges Faced

Credijusto's high-growth model and accelerated success have led to the rapid expansion of
its IT team over time, with many of its solution architects having developed key projects
and then moved to other positions. This led to the development of a highly-complex, hybrid
cloud model to support its rapidly-growing customer base. Extensive use of [Amazon Elastic
Container Service](https://aws.amazon.com/ecs/) (Amazon ECS) preceded a wholesale shift to
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS), requiring
additional skill sets and development of new processes. To meet compliance and security
requirements, the team needed to manage an [Amazon Virtual Private
Cloud](https://aws.amazon.com/vpc/) with multiple subnets and ACLs to isolate services and
environments. Finally, legacy deployments needed to be assessed and either retired or
updated, adding additional complexity to the environment. For legacy infrastructure slated
for replacement, Credijusto needed a solution to standardize the creation of new
infrastructure and simplify tracking and reporting for new cloud resources.

## Streamlining Version Control, Ensuring Consistency

One of the key benefits Credijusto found when moving from Terraform to Pulumi was the
ability to version everything while increasing visibility into precisely what is changing
in every update. From changing labels and tags to updating Helm charts, Pulumi empowered
IT to keep track of every resource, whether on-premises or in the cloud, for every change
they implemented. The fact that Pulumi enabled teams to use their favorite languages
instead of domain-specific tools to manage configuration was a game-changer for
Credijusto:

> "I think it's even unfair to Terraform to compare Terraform with Pulumi because once you
> use a real programming language to tackle a problem, you see that you can do way more in
> less time. So, Pulumi was a natural choice based on the background and skills of our
> people in DevOps."
>
> &mdash; Fernando Carlietti, Lead DevOps Engineer, Credijusto.

Pulumi fits perfectly with Credijusto's dynamic IT environment, enabling developers to
build new infrastructure from the ground up rather than "lifting and shifting" legacy
configurations. Pulumi also streamlined updates. For example, Credijusto had five legacy
ECS clusters defined in [AWS CloudFormation](https://aws.amazon.com/cloudformation/), with
four production clusters and one staging cluster, and each required a different template.
Rather than having to update each Amazon Machine Image (AMI) separately, the team was able
to update one and apply it to each stack for all clusters. The team also found that Pulumi
facilitates and is well-integrated with AWS best practices, ensuring consistency,
scalability, and reliability across teams and infrastructure.

With Pulumi CrossGuard, Credijusto was also able to enforce policies for consistent
tagging, naming, and metadata for new resources.

> "With Pulumi CrossGuard we can provide reusable infrastructure components to our
> application teams and ensure that their implementations adhere to company standards."
>
> &mdash; Fernando Carlietti, Lead DevOps Engineer, Credijusto.

## Solution

Pulumi made network configurations extremely simple and easy to replicate across
environments at Credijusto. Below is an example of how Credijusto used Pulumi to configure
multiple subnets per availability zone and environment.

<img class="block mx-auto md:max-w-4xl my-8" src="/images/case-studies/credijusto-architecture.png" alt="Credijusto architecture">

## Results

Adopting Pulumi enabled Credijusto to migrate to managed Kubernetes with EKS.  This
improved scalability and reduced costs. It also helped the Credijusto team to tame the
complexity of their network configurations across environments. **Using Pulumi resulted in
a 90% reduction in the amount of network configuration that the team had to manage
compared to Terraform or CloudFormation-defined configurations.** By simplifying
configuration and providing engineering with visibility into exactly what will change in
each version, the team benefited from increased confidence in their infrastructure
updates.

> "By using stack references, we ensure that all the dependencies for an application that
> we deploy in Pulumi are up to date. If I have any changes in a VPC, it's very easy to
> cascade that through all the other projects that we manage with Pulumi. When I started
> using Pulumi for this it was love at first sight."
>
> &mdash; Fernando Carlietti, Lead DevOps Engineer, Credijusto.

Pulumi also helped Credijusto to accelerate the adoption of EKS across the organization,
further simplifying their configuration while improving scalability.  Finally, Pulumi
CrossGuard greatly improves their process of reporting and project cost allocation as new
updates are deployed.

## Next Steps

Credijusto plans to expand its use of Pulumi to modernize more of its infrastructure and
will use it to create abstractions from its current applications. Its target is to have
standardized applications (based on language and framework) deployed in a standardized
way, meaning that similar resources (Deployment, Service, Ingress, ServiceMonitor, RDS,
IAM Roles) will be created in Kubernetes (on-premises) and AWS. Creating modular
abstractions will give the company a faster, easier way to bootstrap new applications,
lowering the amount of code that teams need to maintain, and ensuring that standards are
followed across the organization.

Pulumi makes it easy to configure AWS VPCs and Amazon EKS. Check out the following
articles to get started:

* [AWS Virtual Private Cloud with Pulumi](https://www.pulumi.com/docs/guides/crosswalk/aws/vpc/):
* [Amazon EKS with Pulumi](https://www.pulumi.com/docs/guides/crosswalk/aws/eks/):
