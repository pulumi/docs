---
title: Learning Machine
description: |
    Learning Machine used Pulumi and TypeScript to streamline its DevOps processes
    and eliminate several hundred thousand lines of configuration code.
meta_desc: |
    Learning Machine used Pulumi and TypeScript to streamline its DevOps processes
    and eliminate several hundred thousand lines of configuration code.

customer_name: Learning Machine
customer_logo: /logos/customers/learning-machine_logo.svg
customer_url: https://www.learningmachine.com

exec_summary: |
    [Learning Machine](https://www.learningmachine.com/) provides a secure platform, using the
    blockchain, to issue records in a format that is tamperproof, recipient owned, and
    independently verifiable. They are witnessing opportunities in several key industries ---
    Public Sector, Healthcare and Education --- and need to maximize their resources in order to
    quickly capitalize on the explosive growth opportunities in front of them. Pulumi offered
    them a solution which would both simplify existing cloud configurations and help Learning
    Machine to easily adopt AWS serverless technologies such as AWS Lambda and Amazon ECS and
    AWS Fargate. This enabled Learning Machine to expedite customer deployments and scale at
    lower cost.

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

## About Learning Machine

Learning Machine partners with governments, companies, and school systems to deploy secure
credentialing systems that leverage the blockchain as a secure anchor of trust. To ensure
the longevity and interoperability of these records, they are leading contributors to
standards communities, including Blockcerts, IMS Global, and the W3C.

## Challenges Faced

Like many Software as a Service companies, Learning Machine started off with a basic
infrastructure and a simple development process. They selected Amazon Web Services as
their public cloud partner, and began using Cloud Formation to specify their
infrastructure. Most of the development team was focused on higher-level business logic,
and very quickly, the task of infrastructure specification became specialized. As a
result, few folks on the development team had the time to jump in and understand the
hundreds of lines of JSON and ad-hoc scripts used to get their SaaS up and running. The
team was able to make progress for several months, before it was clear that there were
some showstopper issues with their initial approach.

First, their configuration had become too complex. What had started as a few hundred lines
of JSON quickly grew to thousands. At its peak, their CloudFormation templates grew to
over 25,000 lines of code making updates time-consuming as few technical staff felt
comfortable modifying configurations or deploying new applications. This was compounded by
the fact that some configuration changes were happening in the AWS console, creating
"drift" between the specification they thought they were running and the actual
infrastructure that was provisioned in production.

Second, the company was growing. The CEO of Learning Machine, Chris Jagers, realized that
much of their growth for the next few years would come from international clients, which
would necessitate their core product being replicated in data centers across multiple
geographies while keeping their SaaS costs under control. He huddled with his COO, Dan
Hughes, and CTO, Kim Hamilton, to brainstorm about how to solve the dilemma they were
facing.

## Moving from Complicated to Simple

The team realized that in order to grow they needed to transition away from their
first-generation tooling to an offering that more team members could understand and
allowed more rapid customer deployments. They wanted their development team to be
immediately productive, using their existing skill sets and they needed a solution that
could be adopted incrementally, rather than shutting down with a full "lift and shift."
Fortunately, they were able to meet with the Pulumi team and describe the issues facing
them and what they wanted to see in a next-generation solution.

Together Learning Machine and Pulumi worked to develop a solution. Learning Machine chose
to standardize JavaScript and TypeScript as their primary programming languages. Once the
team realized that they would be able to stamp out copies of their infrastructure on
demand, they also decided to enhance their CI/CD pipeline to include infrastructure
configuration alongside application code. This gave the engineering team the freedom to
try new approaches, while maintaining engineering discipline with their core staging and
production roll out processes.

As part of this new approach, Learning Machine began using Pulumi to incorporate Amazon
Elastic Container Service (Amazon ECS) to run and scale their containerized applications,
and AWS Fargate, a compute engine for Amazon ECS. This has enabled Learning Machine to run
their containers without having to manage servers or clusters. As part of this new
"serverless" strategy, Learning Machine also used Pulumi to incorporate AWS Lambda ---
removing additional complexity from their service architecture while making it easier to
scale.

<img class="block mx-auto md:max-w-4xl my-8" src="/images/case-studies/learning-machine-architecture.png" alt="Learning machine architecture">

## Results

The initial project took one month and transformed thousands of lines of templates into
just a few hundred lines of code. Everyone on the team was able to clearly see the
resources that their solution was using, why they were being used and who was responsible
for their maintenance and configuration. Pulumi truly delivered a new way for the team to
work.

By simplifying configuration with Pulumi, Amazon ECS, AWS Fargate and AWS Lambda, Learning
Machine not only realized a 50x reduction in the amount of configuration that they had to
manage but were also able to add new customers faster.  Before the project, provisioning a
new customer could take up to 3 weeks due to the complexity of configuration while their
new approach reduced provisioning time to one hour.

The impact of serverless capabilities was also transformative for the Learning Machine
business. Pulumi enabled a rapid shift to Amazon ECS, AWS Fargate and AWS Lambda --- the
net effect of which was a 67% reduction in AWS charges. This enabled the team to spend
less time focused on maintaining existing infrastructure and more time deploying new
applications on AWS and adding new customers.

"Pulumi is the foundational technology that allowed us to transform our organization,"
said Hughes. The entire DevOps process was streamlined and in addition to realizing better
productivity and higher quality, the team has new insight into their SaaS offering that
they never thought possible.

<img class="block mx-auto md:max-w-2xl my-8" src="/images/case-studies/learning-machine-loc.png">

## New Opportunities

With the adoption of Pulumi, Learning Machine created new opportunities not just for the
technical staff, but for the business as a whole. In addition to supporting new
geographies for their public cloud, they now have the option to offer private cloud
support as well: "Initially, we focused on cost and developer efficiency," said Hughes,
"Now, we realize that this is in fact a strategic choice, and that we can use this work to
deliver the speed, flexibility, value and business outcomes that are so vital to our
company."

Hamilton offers this advice to her peers in key CTO roles. "Jump in with both feet --- the
sooner the better. The payback is immediate and the confidence you gain from having a
predictable development pipeline is immeasurable. Our industry moves with incredible speed
and using tools like Pulumi are absolutely essential to providing teams with the agility
that they require."
