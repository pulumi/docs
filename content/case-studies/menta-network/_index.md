---
title: Menta Network
type: page
layout: case-study

meta_desc: |
    Learn how Menta Network used Pulumi to lower its operating costs by automating the
    deployment, scale and decommissioning of its cloud infrastructure.

customer_name: Menta Network
customer_logo: /logos/customers/menta_logo.svg
customer_url: https://www.menta.com.mx/

exec_summary: |
    [Menta Network](https://www.menta.com.mx/) was looking for the right tools to build a
    robust, scalable, and cost-effective load testing service for their clients in the
    retail sector. They needed cloud infrastructure that could be quickly deployed,
    scaled, and decommissioned while evaluating the unique traits of each e-commerce site
    that they worked with. The team also wanted tools that were familiar to engineering
    and fit within their existing tooling and CI/CD workflow. After evaluating multiple
    options, Menta Network chose Pulumi as their Infrastructure as Code solution because it made
    defining and provisioning infrastructure on Amazon Web Services far easier than other
    tools.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Customer Challenge
      anchor: customer-challenge
    - label: Solution Overview
      anchor: solution-overview
    - label: Results
      anchor: results
---

## About Menta Network

Menta Network is a professional services company located in Mexico City that provides
quality and performance assurance and monitoring for their clients' applications and
infrastructure. They regularly need to spin up, scale, and destroy new cloud environments
as part of their managed load testing solution, which helps clients to evaluate their web
services and applications.

## Customer Challenge

In Menta Network's local market, there are multiple 'Black Friday'-style retail events
including El Buen Fin ("The Good Weekend") in November, and "Hot Sale" in May. Together,
these events capture a significant share of the [$22.6B total e-commerce revenue in
Mexico](https://www.jpmorgan.com/merchant-services/insights/reports/mexico) and drive
extremely high traffic to retailers' websites during sale events.

For Menta Network's retail clients, having a responsive and performant digital experience
is the key to success during these sales. This is especially critical as Mexico has one of
the fastest-growing e-retail markets --- growing 35% last year.

To ensure that these services are scalable and ready to survive the crush of sale-driven
traffic, clients turn to Menta Network's managed load testing service to identify and
correct issues before big sales weeks begin.

For Menta Network, the challenges came from managing these tests across their client base
throughout the year and were both technical and financial. They needed infrastructure for
periodic testing that could scale quickly to mimic peak traffic. Then, automation was
needed to decommission test resources to minimize the cost of running regular tests at
scale. Finally, each client required their own unique configuration and load-tests
tailored to their specific web services.

The combination of Pulumi and Amazon Web Services presented the ideal solution to Menta
Network's challenge.

## Solution Overview

Menta Network's team had experience with a variety of legacy and modern configuration
management tools; however, previous tools would not allow Menta Network's engineering team
to define infrastructure using their language of choice: Python. Managing each client's
configuration using domain-specific languages (DSLs) proved to be too onerous of a task
for both initial implementation and ongoing maintenance.

> "At Menta Network we have a lot of experience with Ansible and Puppet but wanted to
shift to more modern tools to manage our infrastructure. We tried Terraform but found that
Pulumi was far easier to use given its Python support. Ultimately, Pulumi is just as
robust as Terraform and has the added benefit of reducing the complexity of managing many
configurations and environments."

> --- Ernesto Mendoza, CTO

Menta Network has also standardized on [GitLab](https://gitlab.com/) for managing their
entire development lifecycle, container registry and continuous integration / continuous
deployment (CI/CD) process. Pulumi provided a unique alternative that allowed engineers to
define both their load testing application and associated infrastructure in the same
language and tooling --- perfectly fitting infrastructure into their existing [GitLab CI/CD
pipeline]({{< relref "/docs/guides/continuous-delivery/gitlab-ci" >}}). [Support for
GitLab login]({{< relref "/blog/welcoming-gitlab-users-to-pulumi" >}}) further simplified
engineering workflows.

> "Using Pulumi and GitLab provides the Menta team with a simple and robust platform for
developing, managing and deploying our managed load testing solution from infrastructure
to application."

> --- Ernesto Mendoza, CTO

The Menta Network team chose AWS because they wanted the most mature and robust public
cloud, trusted by private and public companies in the Mexican e-commerce market and used
by the majority of Menta Network's customers. On top of that, their strategic partners for
monitoring and SIEM solutions, [New Relic](https://newrelic.com/) and [Sumo
Logic](https://www.sumologic.com/) provided integrations that were easy to deploy with
AWS.

Menta Network's managed load testing solution employed Amazon EC2 for creating scalable
load testing clusters across multiple availability zones, Amazon CloudWatch for telemetry,
and Amazon Virtual Private Cloud, Internet Gateways and VPN features for secure networking
for their service. The team also chose to use [AWS Lambda](https://aws.amazon.com/lambda/)
to automate delivery of mission-critical KPIs to customers' executive dashboards. Pulumi
made configuring and deploying all of these resources across each customer's environment a
snap.

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/menta-architecture.png" alt="Menta architecture">

## Results

Adopting Pulumi for one project took an engineer just a couple of days, given that the
codebase and architecture were already planned for AWS. In the process the team learned
that it's safe to bet on Infrastructure as Code with Pulumi from a very early stage in the
engineering process because its abstractions are clear and simple but do not omit
important architectural aspects of the underlying cloud services such as AWS Lambda, EC2
and Networking features.

Compared to their previous load testing platform, Menta Network lowered their operating
costs by 60% by adopting Pulumi and AWS. They achieved this while leveraging new
efficiency afforded by Pulumi to reduce delivery times and increasing features for their
customers.

Overall they were pleasantly surprised by the low barrier to entry and ease of use of
Pulumi on AWS and plan to adopt Pulumi across all of their AWS projects.
