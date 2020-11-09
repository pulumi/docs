---
title: Snowflake
description: |
    Snowflake uses Pulumi to allow their application and infrastructure teams to truly treat their infrastructure as software.
meta_desc: |
    Snowflake uses Pulumi to allow their application and infrastructure teams to truly treat their infrastructure as software.

customer_name: Snowflake
customer_logo: /logos/customers/snowflake-logo.svg
customer_url: https://www.snowflake.com/

exec_summary: |
    The [Snowflake](https://www.snowflake.com/) platform powers the Data Cloud. With Snowflake, thousands of organizations have seamless access to explore, share, and unlock the true value of their data. To enable its rapid growth, Snowflake made some bold decisions. The first was to shift the paradigm for the new service from VMs to containers. The second was not only to complete the platform itself but to move all their deployments, on multiple cloud vendors, to that platform, all in three months. The goal was to unveil the completed project at its annual company meeting. The problem was that the tools they were using didn't allow them to easily develop infrastructure that was repeatable, testable and scalable. Snowflake switched to Pulumi and met all their goals.


sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: Challenges Faced
      anchor: challenges-faced
    - label: "Solution: Testable, Repeatable Infrastructure with Pulumi"
      anchor: solution-testable-repeatable-infrastructure-with-pulumi
    - label: Results
      anchor: results
    - label: Next Steps
      anchor: next-steps
---

## About Snowflake

Snowflake, the Data Cloud, was founded in 2012. Snowflake enables many critical data workloads including data warehousing, data lakes, data engineering, data science, data application development, and data sharing. Its success is evident. Snowflake now has more than 3,100 customers, including 146 of the Fortune 500 firms. The company's initial public offering (IPO) sold 28 million shares and raised nearly $3.4 billion. This makes Snowflake the largest software IPO in history.

Snowflake is a fully-managed service that can power a near-unlimited number of concurrent workloads. Its architecture allows multiple teams to work from a single copy of data, whether structured and semi-structured. Data Sharing is fully governed and secure, so users can safely discover data, share it and collaborate.

## Challenges Faced

Snowflake’s success meant they needed to make some large-scale changes to their platform so they could support their ever-growing customer base. To that end, they decided to move from a VM-based platform to a Kubernetes-based architecture. That platform had to work across AWS, Azure, and Google Cloud Platform (GCP), for every Snowflake region. Customers of the Virtual Private Snowflake (VPS) service also had to be supported. Additionally, the platform had to be available to over 20 engineering and product teams within Snowflake itself.

The complexity and scale of this change were daunting. Each cloud provider does things differently and Snowflake’s architecture is made up of more than a dozen components that must seamlessly support those differences and work in concert with each other. There is a great deal of intraservice communication and the requirements for data security are high.

However, to make life even more interesting, all deployments had to be completed in three months because Snowflake wanted to unveil the platform at its company-wide annual conference.

The complexity of the project, along with the tight deadline, meant that the Snowflake cloud engineering team had to ask themselves if the tools they were currently using could do the job or whether it was time for a change.

The team was using an HCL-based Infrastructure as Code tool to provision most of their infrastructure but they were running into limitations that threatened to derail the project. To succeed, the team decided they had to move away from a domain-specific language (DSL) and use a standard programming language. The benefits of that change would be far reaching. Not only would they gain the flexibility of a full-fledged language, but it meant they could use existing testing frameworks, SDKs, and other standard tools that would make it easy to adopt best practices for software development.

The Snowflake team knew they needed more than a tool. They needed a platform that allows developers to use the languages and libraries they already know. They decided they needed Pulumi.

## Solution: Testable, Repeatable Infrastructure with Pulumi

Snowflake chose Pulumi for many reasons but a primary one was that developers could use a familiar programming language rather than a DSL. In Snowflake’s case the language of choice was Go. Pulumi could act as the vendor-neutral infrastructure platform and developers could write their infrastructure code like any other software. They no longer felt hampered by the limitations imposed by a DSL and they could take advantage of the Go SDKs and the many testing frameworks for Go. With Pulumi, their infrastructure became testable, repeatable and scalable. “Ultimately, I think what really excited us about Pulumi was that we could use languages that we already know for cloud infrastructure and we knew we could solve for future use cases that we hadn’t even thought of yet --- all because the languages and tools are general-purpose,” said Jonas-Taha El Sesiy, Senior Software Engineer.

Raman Hariharan, Director of Cloud Platform Engineering, said, “For us, Pulumi is infrastructure as code in the true sense. We don’t need to rely on an intermediary to give us the capabilities we need. We can write any code and seamlessly integrate with it.”

Pulumi’s first-class support for Kubernetes was an additional benefit. According to Raman, “Kubernetes lets us treat all the public clouds like a single utility --- it’s AC power for cloud computing. If Kubernetes is AC power, Pulumi is like the universal travel adapter that lets us plug into all these resources and abstract away the complexities of each individual platform. With Pulumi, Kuberenetes just works.”

Snowflake also liked Pulumi’s approach to managing secrets and its support for the Vault  key-management service. Another feature was the Pulumi concept of a stack, which made managing multiple configurations much simpler than before. Because a stack supports inheritance of the most common elements, developers only have to change a few variables to get a deployment up and running. Finally, developers found the Pulumi providers for the different cloud services to be extremely easy to use.

The responsiveness of the Pulumi engineering team also helped ensure that Snowflake met their goals. Whether the question was about Pulumi’s support for Go or an implementation issue such as support for charts, Snowflake knew the Pulumi team would back them up.

## Results

The immediate result was that Pulumi helped Snowflake meet their short-term goals. They deployed to their top cloud providers and internal users in time for the company meeting and were able to expand the platform to support GCP shortly afterwards. However, there are more pervasive results that have improved Snowflake’s development efforts for the long term.

With Pulumi, the Snowflake developers can now truly treat their infrastructure as code. They no longer need to rely on bespoke tools to determine their capabilities. Instead, they’re free to write whatever code they need and to follow accepted software lifecycle best practices. They’ve also decreased their deployment times dramatically.

Raman said, “There’s no question that, if we had gone down the traditional infrastructure automation route, it would have taken us a week or a week and a half to do one deployment of the cluster, end to end. Plus, that deployment wouldn’t be repeatable, testable or scalable. It would have been a mad scramble to meet our deadline. When we demonstrated to people that what used to take a week and a half now, with Pulumi, took under a day, they were shocked.”

Changing what you use to write your software is a big decision but Snowflake found that ramping up with Pulumi happens quickly. For one, developers are using a language they already know. Brian Nutt, Senior Software Engineer, said, “I had a lot of experience with other infrastructure as code solutions but I found switching over to Pulumi incredibly easy. It was a fun experience to just hop into Go and use the Pulumi SDKs to fulfill the requirements we needed for the cluster. It was very freeing to, for example, not have to depend on upstream modules to be updated to actually make progress. It was great. And I don't think I could go back to the old way of operating after that. NO.”

## Next Steps

Snowflake has big plans for the future and Pulumi is a part of them. One initiative is to leverage Pulumi to expand their support for GCP. Given the scale of their multi-cloud, multi-region environments, security and automation are two strategic investment areas. Snowflake plans to  use Pulumi to help manage this complexity and streamline deployments: “We’re looking forward to using Pulumi CrossGuard to apply security policies to protect our stacks and the new ‘nextgen’ Pulumi Azure Provider is going to be a huge timesaver for us as well because it automatically supports all the latest Azure features,” said Jonas. “Beyond that, we’re investing a lot in testability and using the Automation API for infrastructure so we can move to more of a GitOps model, and Pulumi will play a huge role in enabling that too.”
