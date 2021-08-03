---
title: "Cloud Engineering on the Rise"
date: 2021-08-03
meta_desc: "Infrastructure as Code case studies with Pulumi, Atlassian, SANS, and Skai"
meta_image: pulumi.png
authors:
    - george-huang
tags:
    - cloud engineering

---

One of the most fulfilling aspects of working at Pulumi is learning how customers and the community practice cloud engineering in their teams. It’s exciting to see how they use cloud engineering and Pulumi to implement best practices that enable leveraging the cloud to accelerate innovation and enable better business outcomes.

<!--more-->

Pulumi is born from the experiences and needs of teams practicing cloud engineering every day. When we [announced]({{< relref "/blog/pulumi-3-0" >}}) the Pulumi Cloud Engineering Platform in April, CEO & Founder Joe Duffy [talked about](https://www.youtube.com/watch?v=Zko70KVGcgo) bringing cloud engineering to everyone. Over the past year we have seen significant growth in cloud engineering and usage of Pulumi across companies of all industries and sizes, and spanning a diverse spectrum of teams and engineering disciplines. We’re also seeing growing numbers of job postings with “cloud engineer” in the title or which have Pulumi as a requirement or desired skill set.

Recently, we published several case studies about how teams are applying cloud engineering best practices. Cloud engineers apply standard software engineering practices and tools uniformly across infrastructure management, application development, and security to tame the complexity of delivering and managing modern cloud applications. We’ve published on our [website]({{< relref "/cloud-engineering" >}}) and in this [blog]({{< relref "/blog/infrastructure-testing-concepts" >}}) some of the key cloud engineering best practices that we see broadly across the community, and encourage you to read further to see three stories of cloud engineering in action.

These three case studies highlight a small sampling of the many types of companies and teams representing cloud engineers. Some are platform teams at large organizations, like Atlassian, who are responsible for empowering the rest of their developer teams. We also see DevOps teams using cloud engineering, such as at Skai and SANS Institute. There are other types of teams, like full-stack engineers or SREs, which we will share in future posts. All of these teams share a software engineering mindset and make a leveraged impact on the business by increasing speed, automation, reliability, and agility through cloud infrastructure innovation.
<br>
<br>

![Atlassian](./atlassian-wordmark.png)

<!-- ## Atlassian -->

Atlassian’s Bitbucket DevSpeed team is responsible for improving developer productivity through better workflows and tooling. It used Pulumi to make it easier and faster for its developers to use cloud infrastructure and reduced developers' time spent on maintenance by 50%. DevSpeed originally needed a way to expand regional support for its deployment pipeline, which deploys instances on AWS for more than one hundred team members around the world. The team also wanted to build a self-service platform that provisions cloud infrastructure for Bitbucket’s developers, without having to learn a complex domain specific language (DSL). They moved from a legacy DSL-based infrastructure as code tool to the Pulumi Cloud Engineering Platform, which let them define and deploy infrastructure in general-purpose languages that Bitbucket developers already used, such as Python. Using a familiar language like Python also made it easy for them to add cross-regional support to their deployment pipeline. They also built a self-service dashboard that allows any developer to deploy and configure private Bitbucket instances for feature development.

### Atlassian's Key Practices

- Builds infrastructure as code with Python.
- Makes infrastructure code readable and accessible to all developers in the organization by using a common language like Python.
- Created a self-service platform that deploys and configures private Bitbucket instances for any Bitbucket developer. Underneath, everything runs through a CI/CD pipeline with Pulumi, Bitbucket Pipelines, and Bamboo.
- Manages and deploys updates to all developer instances in the organization using features like the Pulumi Automation API.

### Atlassian's Results

- Allowed developers to use general-purpose programming languages like Python and familiar software tools to deliver and manage infrastructure.
- Enabled Bitbucket developers to easily provision approved cloud infrastructure using a self-service dashboard built with Pulumi.
- Reduced the time Bitbucket developers spent maintaining their instances from 8 hours per week to fewer than four.
- Reduced the size and complexity of its infrastructure code compared to its previous infrastructure tool while increasing the code’s clarity.

[Read the full case study→]({{< relref "/case-studies/atlassian" >}})
<br>
<br>

![SANS Institute](./sans-wordmark.png)

<!-- ## SANS Institute -->

SANS Institute is the global leader in cybersecurity training. Using Pulumi, the organization adopted cloud engineering practices that enabled it to reduce deployment times by 70%. Its DevOps team needed a more consistent and reliable way to build, deploy, and manage the SANS virtual training environments used in labs. It had previously used legacy infrastructure tools which require inflexible DSLs that aren’t suited to modern cloud applications. The limitations of the DSLs meant the team needed to use AWS Lambda functions and Bash scripts to fill in gaps. The team needed a cleaner solution built for the modern cloud that would be more scalable and easier to manage. By adopting Pulumi, SANS increased delivery speed, quality, and consistency using cloud engineering practices such as building infrastructure as code with TypeScript and software tools, and deploying cloud applications with Git and automated delivery pipelines. It plans to use Pulumi to help other SANS business units modernize their practices and tools.

### SANS Institute's Key Practices

- Builds infrastructure as code with TypeScript.
- Deploys infrastructure through a GitOps and CI/CD process while managing its Git branches using a GitFlow pattern.
- Production deployments can be initiated through an API call through a self-service platform that deploys an application instance.
- Manages infrastructure configuration through Policy as Code which checks for compliance.

### SANS Institute's Results

- Reduced deployment times for game servers by up to 70%.
- Simplified their deployment process by eliminating the need to “glue together” several infrastructure as code tools, scripts, and functions. This let them remove a manual ticketing step.
- Enabled developers to use familiar programming languages and tools, which also helped make their code cleaner and - more uniform, resulting in streamlined pipelines.
- Helped to identify opportunities in other SANS departments where Pulumi can streamline operations.

[Read the full case study→]({{< relref "/case-studies/sans-institute" >}})
<br>
<br>

![Skai](./skai-logo.png)

Skai is an independent, global marketing platform for strategy, measurement, and best-of-breed activation across all of the world’s most influential digital channels. Skai possesses a highly technical engineering organization with over 350 software engineers, data experts, and DevOps engineers.  Skai’s microservices run on AWS, but its core monolith service was hosted in a data center running private cloud infrastructure. Skai’s DevOps group needed to migrate the service to the cloud because demand increased. Skai’s DevOps team decided to transition from using its legacy infrastructure tool because its domain-specific language (DSL) wouldn’t be suited to the demands of the newly migrated modern cloud architectures. Instead, Skai sought a solution that enabled it to use familiar languages and software engineering best practices to manage its infrastructure. That’s why Skai chose the Pulumi Cloud Engineering Platform to build, deploy, and manage its infrastructure with Python.

### Skai's Key Practices

- Builds infrastructure as code in Python.
- Leverages reusable infrastructure components.
- Multiple teams collaborate on cloud infrastructure, including an architect, application development teams, and a core platform/DevOps team.
- Teams use a “loosely-coupled, tightly-aligned” approach to create component classes for different infrastructure elements, with each team working on a different element.
- Uses Python code to integrate infrastructure processes with internal metadata and IT systems.

### Skai's Results

- Migrated a core monolith service with hundreds of terabytes of data from a data center to AWS.
- Refactored the service’s infrastructure from being managed with a legacy infrastructure configuration tool to Pulumi, using Python as the language of choice.
- Created modular infrastructure components that enable different teams to collaborate and work on different parts of the infrastructure in parallel.
- Streamlined the registration and deregistration process for new application instances by integrating Pulumi with its internal IT systems.

[Read the full case study→]({{< relref "/blog/kenshoo-migrates-to-aws-with-pulumi">}})

## Summary

Cloud engineers are a fast-growing community made of tens of thousands of members and thousands of companies. They apply standard software engineering practices and tools uniformly across infrastructure management, application development, and security to tame the complexity of delivering and managing modern cloud applications. To illustrate cloud engineering in action, we shared three case studies of teams using cloud engineering in their organizations. Pulumi’s Cloud Engineering Platform was built to enable any organization to adopt cloud engineering best practices out-of-the-box. If you’re starting your cloud engineering journey, try Pulumi for free today with this [Getting Started guide]({{< relref "/docs/get-started">}}).
