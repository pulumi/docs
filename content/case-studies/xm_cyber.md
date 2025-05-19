---
title_tag: XM Cyber | Case Studies
title: "XM Cyber: Multi-Cloud Infrastructure Management with AWS and Pulumi"
description: |
    XM Cyber used Pulumi to transform their multi-cloud infrastructure management, focusing on AWS EKS clusters, Python reusability, and an internal developer platform to enable faster, more consistent deployments.
meta_desc: Learn how XM Cyber partnered with Pulumi to create a modern multi-cloud infrastructure management strategy centered on AWS EKS, Python reusability, and an internal developer platform.

customer_name: XM Cyber
customer_logo: /logos/customers/xm-cyber-logo.svg
customer_url: https://www.xmcyber.com/

quote_block:
  quote: |
      "When implementing Pulumi, we noticed also by using the Pulumi Cloud that we can easily see what's going on, we can easily find what resources are up and what are down. We can easily manage our stacks and everything is very, very comfortable."
  quote_attrib: Tech Lead, DevOps Team, XM Cyber
  # Note: The transcript doesn't mention specific deployment time metrics

exec_summary: |
    XM Cyber, a leading cybersecurity platform specializing in vulnerability management and attack path management, needed to transform their infrastructure management to support complex multi-cloud environments. With a mix of manual and infrastructure-as-code deployments, they faced challenges with resource visibility, reusability, and developer accessibility. After evaluating options, XM Cyber selected Pulumi to manage their diverse cloud environments, including AWS, GCP, and Stack IT. Using Pulumi's Python support, they created reusable infrastructure packages, standardized EKS deployments, and built an internal developer platform. This approach significantly improved infrastructure consistency, reduced resource sprawl, and enabled better collaboration between DevOps and development teams.

sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: About XM Cyber
      anchor: about-xm-cyber
    - label: Challenges Faced
      anchor: challenges-faced
    - label: "Solution: Pulumi as the Multi-Cloud Orchestrator"
      anchor: solution-pulumi-as-the-multi-cloud-orchestrator
    - label: Technical Implementation
      anchor: technical-implementation
    - label: Results
      anchor: results
    - label: Future Plans
      anchor: future-plans
---

## Multi-Cloud Infrastructure Management with AWS and Pulumi

### About XM Cyber

XM Cyber is a leading cybersecurity platform based in Israel in Tel Aviv. Founded in 2016, the company specializes in vulnerability management and attack path management solutions, positioning itself as a leader in this area. Now part of Schwarz Group, a large retail company based in Germany, XM Cyber provides critical cybersecurity solutions to organizations worldwide. Their DevOps team manages the infrastructure and deployments of the entire organization, with 14 DevOps engineers working across all teams.

## Challenges Faced

Before implementing Pulumi, XM Cyber's infrastructure management faced significant challenges that were affecting their ability to scale and maintain their cloud operations:

- **Limited agility with existing tools**: "When starting to adopt complex situations in our infrastructure called environments, we figured out we do not have the agility we wanted from them."
- **Inconsistent resource management**: A mix of infrastructure-as-code and manual deployments created inconsistency across environments.
- **Resource sprawl and visibility issues**: "Our biggest problem before Pulumi was that we created environments with infrastructure as code and also manually. This created a lot of out of state resources, a lot of dangling resources, a lot of resources that were not managed and this has affected our cost a lot."
- **Poor reusability**: "We had a lot of challenges in the areas of reusability."
- **Collaboration barriers**: "We had a lot of challenges of how do we engage the platform, how do we give access and make others understand—other people that are not DevOps—understand what's going on, like developers."
- **Limited programming capabilities**: They needed to "use the entire ecosystem of the programming language that we can in Python or in TypeScript or whatever, and also to write modules that we can with object-oriented programming."

As a multi-cloud organization supporting AWS, GCP, and Stack IT (a European cloud provider developed by Schwarz Group), XM Cyber needed a solution that could work consistently across all their environments while providing the flexibility and power of a full programming language.

## Solution: Pulumi as the Multi-Cloud Orchestrator

After evaluating their needs, XM Cyber adopted Pulumi as their comprehensive infrastructure-as-code solution:

### AWS EKS Infrastructure Transformation

The core of XM Cyber's infrastructure relies heavily on AWS EKS clusters:

"We are using of course Pulumi to manage our infrastructure as code and also our entire EKS infrastructure, AWS, GCP infrastructure and also our Stack IT infrastructure."

This allowed them to manage their Kubernetes infrastructure more effectively, as indicated in the transcript:

"We need to create EKS clusters with a lot of installations. We need to create YAML files with Pulumi."

### Reusable Python Infrastructure Packages

One of the most innovative aspects of XM Cyber's implementation was their approach to packaging and reusability:

"We actually took it, I think, to the next level by leveraging the Python packaging modules. And we are creating a Python library of every Pulumi resources we create for internal use. So others can also take them and use them and write code from them."

This approach enabled them to:
- Create standardized infrastructure components
- Package them as Python libraries in a PYPI server
- Allow developers across the organization to reuse these components
- Ensure consistency in deployments
- Reduce duplication of effort

"Basically, all they need to do is install the package and they have entire Pulumi EKS cluster they can have with installations already inside with a networking enabled with a lot of internal features that we took Pulumi with and made it a lot, a lot larger."

### Internal Developer Platform

XM Cyber implemented a Git-based internal developer platform with Pulumi as the backend:

"Our internal developer platform is managed in Git, so it's not like a platform. It's a way that we created to allow developers to create resources that are common through Pulumi. So we're using it in like a GitHub's way where they create a pull request and they add a value to some YAML file. And behind the scenes, Pulumi runs that value and creates an ECR from it or a bucket for it or whatever they need."

## Technical Implementation

XM Cyber's Pulumi implementation stands out for its approach:

### Language Evolution

XM Cyber's journey with Pulumi started with JavaScript/TypeScript and evolved to Python:

"First, we started writing in OJS in TypeScript, our Pulumi programs. And then as our team grew, we moved to Python and we're writing Pulumi ever since in Python and we're loving every minute of it."

### Multi-Cloud Strategy

Using Pulumi allowed XM Cyber to implement a consistent approach across different cloud providers:

"We run multi-cloud, we support AWS, we will support soon GCP, and also we support Stack IT, which is a European cloud provider, which is developed by Schwarz Group."

The team uses the platform for both customer-facing and internal infrastructure:

"We are using it both for customer-facing infrastructure and both for internal infrastructure. So also when we deploy in customer environments, we use Pulumi. And also when deploying internal resources, like ECR repositories, or also when using internal developer platforms, we are using Pulumi behind the scenes to actually create those resources for us."

### Infrastructure as Software

Pulumi enabled XM Cyber to apply software engineering principles to infrastructure:

"And also we wanted to use the entire ecosystem of the programming language that we can in Python or in TypeScript or whatever, and also to write modules that we can with object-oriented programming and use the entire ecosystem of the said language to support us in this scenario."

## Results

Since adopting Pulumi about three years ago, XM Cyber has experienced numerous benefits:

- **Significantly improved resource visibility**: "When implementing Pulumi, we noticed also by using the Pulumi Cloud that we can easily see what's going on, we can easily find what resources are up and what are down. We can easily manage our stacks and everything is very, very comfortable."
- **Enhanced cost control**: Better resource management reduced waste and eliminated dangling resources.
- **Better tagging and organization**: "Every time we create an environment, we make sure to also label it and tag it in a way that will make sense for us to later in the cloud see what's going on. So it'll be easier for us to find it, to see what resources it depends on, to see what resources depend on it. And Pulumi Incense really came in out there."
- **Improved developer experience**: "We are wrapping a lot of internal logic into those packages and we're creating resources from them. We actually store them in a PYPI server so we can give the packages to developers so they can use them as well."
- **Better resource management**: "It helps us a lot with the filtering. It helps us a lot with us being in need to control what we have and what we don't have and what is deployed and where."
- **Consistency in deployments**: The consistent approach helps prevent creating resources manually or with inadequate tools.

## Future Plans

XM Cyber's vision for Pulumi includes:

- Creating a more comprehensive internal developer platform: "We have actually some plans in the future to create an actual developer platform and use it. And of course, Pulumi will be the backbone of this."
- Implementing a multi-cloud "infrastructure factory": "Basically, we want to leverage Pulumi to take us to the next level in a way that we want our entire multi-cloud infrastructure to be managed in a single point of truth... we want a Pulumi project, a single factory, if you want an infrastructure factory to manage our multi-cloud resources."
- Standardizing outputs: "We wanted to be able to output a single output every time it runs, no matter the cloud. And that being, you know, a cube config, some maybe network names and stuff like that."
- Creating cloud-agnostic solutions: "What we want is to take the entire ecosystem that Pulumi gives us and create something very, very cloud agnostic, very, very big, very large, but still that can be manageable by separating it into projects and not creating a single project with 1000 resources, but creating stack references."
- Base infrastructure project: "This is an ongoing project at the moment, creating an entire, we call it base infrastructure project. So every time someone wants to create an infrastructure for our environment or resources, they will leave from the same Pulumi project and we will separate them by stacks and then we will migrate all of the existing resources to this project as well. This is the vision."

XM Cyber's journey with Pulumi demonstrates how a sophisticated infrastructure-as-code approach can transform multi-cloud management, particularly in AWS environments. By leveraging Pulumi's programming capabilities and the Python ecosystem, they've created a more maintainable, visible, and cost-effective infrastructure strategy that supports both their internal operations and customer-facing services.
