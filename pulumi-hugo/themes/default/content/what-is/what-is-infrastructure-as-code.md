---
title: What Is Infrastructure as Code?
meta_desc: |
    Understand what is infrastructure as code, along with the main benefits and importance
    for modern application development.

type: what-is
page_title: What is Infrastructure as Code?

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

Infrastructure as code (IaC) means using code to define and manage infrastructure. **Infrastructure as code is about bringing software engineering principles and approaches into the cloud infrastructure space.**

Infrastructure as code is the latest step in the evolving process of defining and managing infrastructure. Before infrastructure as code, infrastructure was (and in some cases still is!) provisioned by many methods such as pointing and clicking in a user interface, batch scripts, and configuration management tools that may not have been designed by the cloud. Today, modern approaches use platforms, such as [Pulumi](/), which embrace and support the full software engineering lifecycle.

The term “infrastructure as code” or IaC has become commonplace, but there are important questions attached to it. What is infrastructure as code really? What are the benefits of infrastructure as code?  How do you integrate infrastructure as code into your organization? In this article, we’re going to touch on all these points and discuss why infrastructure as code matters for modern application development.

## Why Has Infrastructure as Code Become Important?

Infrastructure as code matters because of three significant trends, all of them happening at the same time.

### The transition to the cloud

One trend, of course, is the ongoing transition to the cloud. More and more companies are shifting workloads from on-premises infrastructure to cloud environments. Cloud-based infrastructure is provisioned via APIs, and, as a result, can be easily managed with infrastructure as code tools.

### Cloud modernization

The second trend is cloud modernization. After organizations migrate to the cloud, they tend to look for opportunities to maximize the value they get from their cloud environment. This frequently involves adopting technologies such as serverless, containers and Kubernetes, which, when applied correctly, these technologies enable teams to deliver value more quickly, and uses managed services to offload some of the heavy lifting to the cloud provider. These technologies and services generally require a more granular management of infrastructure. Stitching together all the primitives that the cloud provider offers into solutions that serve the business is a great fit for infrastructure as code.

### Frequent infrastructure changes

Finally, the rate at which a company’s infrastructure changes is increasing. Cloud adoption and cloud modernization are two of the reasons this is happening. The third is that organizations are finding that they can move faster if they take advantage of the fundamental elasticity of the cloud.

For teams managing tens or hundreds of cloud resources that change once every few months, it may still be possible to manage infrastructure with point-and-click or scripts. But the more common situation today is that teams are managing thousands or tens of thousands of resources that change daily or even hourly. Infrastructure as code is how you take control of that kind of complexity.

## What Benefits Does Infrastructure as Code Provide?

Infrastructure as code tames the complexity of cloud infrastructure because it uses the same software engineering principles that have enabled other software-based systems to scale up. Here are some of the principles infrastructure as code enables.

### Version control

When infrastructure is described as code, it can be checked into source control, versioned and code-reviewed using existing software engineering practices. Changes to infrastructure can be deployed using existing CI/CD tools.

### Testing

As any critical system grows in complexity, people can start to feel nervous about making changes. With infrastructure as code, teams can write tests for their infrastructure to ensure its correctness.  They can encode policies so that all provisioned infrastructure and its configurations [are compliant](/docs/guides/testing/property-testing/). Once they’re tested, infrastructure components can be reusable pieces of code that capture best practices and that can be shared across teams. No more reinventing the wheel.

### Use of IDEs

Most developers have an IDE that they use all the time. When infrastructure is code, you can take advantage of all the features that an IDE offers, such as autocompletion and the ability to look up methods and their parameters.

### DevOps

Infrastructure as code enables infrastructure teams and software development teams to adopt DevOps principles and work together more closely.  When infrastructure is code and is integrated into your company’s software lifecycle, there’s a common language and a common set of practices that stakeholders already understand. That common understanding fosters cross-team collaboration, which is fundamental to DevOps

## How Do I Get Started with Infrastructure as Code

Bringing infrastructure as code into a startup or a company with many greenfield applications may not be difficult. For most companies, however, it’s not so straightforward. Many companies, both large and small, have a lot of infrastructure that was created by pointing and clicking in the console of a cloud provider. That’s how many new projects get started. Then, one day, an ops engineer wakes up and realizes that the new project is now production infrastructure. To make it more “official,” they write a run book or a wiki that describes what buttons to click when someone wants to do some common task. Another common situation is that there are Bash or PowerShell scripts floating around that only one or two people know about. What do you do if that’s your situation?

Here are steps you can take to adopt infrastructure as code.

### Define “Good”

The first step, even before you begin to [evaluate tools and approaches](/blog/configuring-your-dev-environment/), is to define what “good” looks like to your company. Achieving that ideal doesn’t depend on which technology you use. It depends on understanding what assumptions will remain true regardless of the tools you use.  For many companies those assumptions are:

- The amount of infrastructure is going to be high.
- The number of interconnections between managed services will be high.
- The rate of change should be high, in order to take maximum advantage of what your cloud provider(s) offer.
- The number of people who have access to your cloud’s capabilities should grow.
- Infrastructure code should be integrated into your continuous delivery system.

A team made up of all the stakeholders is one way to define what your company wants to achieve with its cloud infrastructure.

### Import Existing Infrastructure

You probably already have a lot of existing infrastructure.  Make sure you can [import that existing infrastructure](/blog/adopting-existing-cloud-resources-into-pulumi/) into your new world. For example, you might have a production database that you want to manage as infrastructure as code. Your tool should let you reliably manage state changes, let you make changes without any downtime, let you test and version those changes, preview the changes, and get pull requests.

### Integrate with existing engineering practices

Assuming your infrastructure code is integrated with your continuous delivery pipeline, you can start instituting the same best practices you use with your application software. For example, to understand your infrastructure’s correctness, [you’ll need tests](/blog/testing-your-infrastructure-as-code-with-pulumi/). Some tests should run before delivering the infrastructure to ensure that the program is logically correct and that it provisions the infrastructure correctly. Other tests should run when you deploy your infrastructure to ensure that the deployment was successful.

### Think about policies and security

Next, you’ll want to enforce policy for the entire organization. That way, you’ll have a standard that applies to everyone who builds infrastructure. [Those policies should run against everything anyone does](/blog/benefits-of-policy-as-code/).

It’s important to plan policies and security because one of the goals of Infrastructure as Code is to empower the development teams and give them as much flexibility as possible. Without planning, you may find that you’ll create an interface that’s so restrictive, teams find ways to go around the platforms. It’s a balancing act that requires input from everyone.

### Start Small

Any time you make a significant change in technology, you want to do it incrementally. You might start with a new service so you don’t disrupt existing ones. Once you've figured out what successful patterns look like, go back and figure out how to transform some existing infrastructure. Pick a project where you’ll start seeing value early and then iterate.

## Learn More

Pulumi offers a truly modern approach to infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).
