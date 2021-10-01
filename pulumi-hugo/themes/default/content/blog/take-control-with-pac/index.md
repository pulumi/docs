---
title: "Empower Your Team with Policy as Code"
date: 2021-03-08T18:12:25-07:00
meta_desc: "Policy as Code provides control, clarity, version control, automation, and the use of IDEs to manage your infrastructure."
meta_image: control_with_pac.png
authors:
    - sophia-parafina
tags:
    - Policy as Code
---

Policies set the guardrails for your applications and infrastructure. They define many aspects of how your company manages its applications and infrastructure. Security, safe use of resources, and compliance with external standards are just a few examples of what a policy can define.

<!--more-->

Historically, policies were written and enforced by compliance and security teams who set down the rules as  text documents. More recently, teams often use a cloud provider’s GUI to set policies. Both of these approaches are error-prone and far too slow to keep up with complex, rapidly changing infrastructure and automated systems. They also can’t take advantage of the accepted best practices for software development.

Instead, just as you define infrastructure as code, so too should you define policies as code.

## What Do You Gain with Policy as Code?

The short answer to this question is that you can apply software engineering principles and approaches to your policies, just as you do with your applications and with infrastructure as code. Here are some of the specific benefits:

### Clarity

Policies written as code are unambiguous pieces of logic. They can be read both by humans and by machines. There’s no way to misinterpret them, which is a real problem with text documents.

### Version control

When policies are described as code, they can be checked into source control, versioned, and code-reviewed. They become a part of your automated pipelines.

### Testing

As any critical system grows in complexity, people can start to feel nervous about making changes. When policies are written as code, they can be tested, just as you test your applications and infrastructure. You can integrate your policies into your automated testing system as easily as any other code you write.

### Familiar tools such as IDEs

When policy is code, you can use familiar tools, such as the IDEs you use to write other pieces of code to develop new policies, refactor existing policies, and catch errors early.

### Automation

As we mentioned, policy as code can be sent through your automated CI/CD pipelines for fast testing and deployment. For most companies, their infrastructure has become too large and complex to use manual procedures such as documents and GUIs to make changes.

## Common Use Cases

Policies can encompass many areas. Here are just a few.

- **Authorization control**. You can implement fine-grained access control for applications. For example, a service can make an API call to a policy engine to determine whether a request is authorized or not.
- **Infrastructure provisioning**. You can create policies that require tagging, provisioning certain types of resources, and secure network settings.
- **Kubernetes control**. You can manage Kubernetes resources such as pods, namespaces, and nodes. You can ensure container images come from trusted registries.
- **Cost control**. One way to control your cloud costs is to set policies based on pricing. You can calculate the cost of a resource ahead of time and create a policy limiting the amount you spend to deploy it. For an example of how tagging on AWS can control costs, take a look at [Automatically Enforcing AWS Resource Tagging Policies]({{< relref "/blog/automatically-enforcing-aws-resource-tagging-policies" >}}).

There can be many other uses. Use your imagination. Another benefit of policy as code is that it makes experimentation easy.

## Learn More

Ready to learn more? With [Pulumi](https://www.pulumi.com), you can create and manage infrastructure and policies with the languages and tools you already know. To help you implement policy as code, check out this [short video about CrossGuard]({{< relref "/events-workshops/intro-to-policy-as-code" >}}), our product that uses policies to enforce gated deployments. With it, administrators can apply policies to particular stacks. Any violation will gate or block an update from proceeding. Give Pulumi a try and [get started]({{< relref "/docs/get-started" >}}) for free today.
