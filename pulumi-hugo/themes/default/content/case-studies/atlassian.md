---
title: Atlassian
description: |
    Atlassian Bitbucket used Pulumi to make it easier and faster for its developers to use
    cloud infrastructure and reduced developers' time spent on maintenance by 50%.
meta_desc: |
    Atlassian Bitbucket used Pulumi to make it easier for its developers to use cloud infrastructure
    and reduced developers' time spent on maintenance by 50%.

customer_name: Atlassian
customer_logo: /logos/customers/atlassian-wordmark.svg
customer_url: https://www.atlassian.com/

exec_summary: |
    Atlassian’s Bitbucket DevSpeed team is responsible for improving developer productivity through better workflows
    and tooling. Because the team wanted to make it easier and faster for developers to access cloud infrastructure,
    they moved from a legacy DSL-based infrastructure as code tool to the Pulumi Cloud Engineering Platform, which
    let them define and deploy infrastructure in general purpose languages that Bitbucket developers already used,
    such as Python. Using a familiar language like Python also made it easy for them to  add cross-regional support
    to their CI/CD pipeline for deploying development environments for over 100 Bitbucket developers around the world.
    They also built a self-service dashboard that allows any developer to deploy and configure instances for feature
    development. The results were dramatic increases in developer productivity: It reduced the time developers spent
    maintaining their instances by more than 50%.



sections:
    - label: Exec Summary
      anchor: executive-summary
    - label: About Bitbucket Cloud
      anchor: about-bitbucket-cloud
    - label: "First Challenge: Enabling the Sydney Developers"
      anchor: first-challenge-enabling-the-sydney-developers
    - label: "Second Challenge: Improving Developer Productivity with Self-Service Cloud Infrastructure"
      anchor: second-challenge-improving-developer-productivity-with-self-service-cloud-infrastructure
    - label: Summary
      anchor: summary
---

## About Bitbucket Cloud

Bitbucket Cloud is a Git-based code hosting and collaboration tool designed for teams and is built by Atlassian. Bitbucket's integrations with other Atlassian products like Jira allow the entire software team to work together on projects. With Bitbucket, teams have one place to collaborate on code from its concept, through automated testing, all the way to its deployment to the cloud.

## First Challenge: Enabling the Sydney Developers

Mike Corsaro is a Senior Software Engineer at Bitbucket. He works on the DevSpeed team, whose mission is to improve developer productivity at Bitbucket. His team helps about 100 Bitbucket developers located all over the world.

### Speeding up the Sydney team

Mike was the founding member of the DevSpeed team. His first task was to add cross-regional support to the pipeline that deployed instances on AWS for Bitbucket developers. Developers have private instances of Bitbucket, which they can use to develop new features. The existing pipeline deployed only to the US West (Oregon) region, but it needed to also deploy to the Asia Pacific (Sydney) region.

### Evaluating the Existing Tools

Mike first examined the existing toolset to see if it would solve his problem. He found that the team used an Infrastructure-as-Code tool, Terraform, that required users to learn its domain-specific language (DSL), which was not intuitive to Mike and most developers. A developer would go to the repo containing a YAML template written in the DSL, run the Bitbucket CI/CD pipeline, and the tool would spin up a self-contained version of Bitbucket in AWS.

Because of the DSL’s limitations, it would not be straightforward to codify infrastructure deployments for the Sydney team. Mike would need to learn the complicated DSL to complete his task, which would be unproductive and time-consuming. On top of that, he was relatively new to using AWS and the cloud.

He cited an example, saying, “We have three databases. With the old tool, that was 20 lines of code. And of course, coming from a C# background, I had no idea what any of it meant. It would take me hours to figure out how any of it worked and what each property name was and what it did. Another confusion I had was, defining a variable “name” in multiple places, and I had no idea which one was correct. So many things were unclear.”

Mike wanted a general and elegant solution that would let him quickly and easily manage infrastructure in AWS while using familiar languages and tools.

### Pulumi to the Rescue

Mike says, “I knew about Pulumi because I followed Joe Duffy on Twitter. I come from the C# world, where he's a well-known figure. I saw that he’d started a company called Pulumi and its mission really appealed to me.”

Pulumi allows developers to build, deploy, and manage cloud infrastructure and applications using the programming language of their choice. That means they can use standard programming constructs and standard tools to author and manage infrastructure code.

Mike chose Python to build cloud infrastructure since Bitbucket developers already used it. He said, “Because all the developers on Bitbucket write Python, they can use all the skills they already have from their day-to-day job to write infrastructure code. There are also safety features you’d expect from a standard programming language. For example, you know if you're referencing something that isn't declared or if you're trying to use a property that doesn't exist.”

Instead of discarding all the code written with the old tool, Mike used [Pulumi's conversion tool]({{< relref "/tf2pulumi/" >}}) to assist with the transition. Mike says, “I knew that Pulumi provided an automatic conversion tool, and that helped a lot. I spent one day using the automatic conversion tool and then just spent some time making sure everything looked right. In two days, I was all set.”

As an example of how Pulumi made formerly complex tasks straightforward, Mike says, “With the old tool, spinning up our databases meant we had to have about 20 blocks of code and do a lot of copy and pasting. But with Pulumi, it's Python. So you have a for statement and then you define the names of the databases you want. It's five lines of code. If you want to add a new database, add one line, and you're good to go.”

Pulumi also simplified cloud infrastructure management and provided clear visibility into all active resources. Mike said, “Before Pulumi, we had a manager for state files that was a complete pain. We ran into weird issues and errors, and it was difficult to ask questions, such as how many developer instances were running. Now, Pulumi manages all the state files for us and gives us that visibility.""

Mike also gave an example of how easy it was to deploy changes across all instances with confidence. He says, “Subnets have a maximum number of IP addresses associated with them. We ran into an issue where there would be failures because addresses were selected randomly. I corrected the issue and could confidently deploy it by just writing a test to make sure that select logic worked. And because we're using Python, I was able to just use the AWS Python API to figure out which subnets were full! That's simply not possible using a DSL.”

### Result

Using Pulumi, with its support for general-purpose languages like Python, Mike quickly and easily built a repeatable pipeline that deploys development environments for the Sydney team despite having limited knowledge of AWS. He also now understood how useful Pulumi could be in improving the developer experience at Bitbucket and how easy it was to use. He began to look for other ways to use Pulumi.

## Second Challenge: Improving Developer Productivity with Self-Service Cloud Infrastructure

Shortly afterward, Mike reviewed a survey sent to the Bitbucket developers, asking them how they spent their time. He was surprised to learn that developers were spending 20% of their workweek maintaining their private Bitbucket development environments.

Again, part of the problem rested with the old tool, whose DSL was unfamiliar to most developers. Because it lacked standard programming capabilities, it made the code verbose and difficult to understand. Mike knew that he could streamline the entire workflow with Pulumi and make infrastructure more accessible and simpler to use for developers who understand Python.

To make things simple and turnkey for developers, the DevSpeed team built a self-service dashboard that created and configured new instances. Developers enter a few pieces of information, such as what they want to call the instance, what region to use, and an SSH key. Then, a CI/CD pipeline using Bitbucket Pipelines and Bamboo calls Pulumi to deploy a complete developer environment.

Once the instance is ready, the developer simply SSH’s into it, and it will look exactly like Bitbucket. The developer can make the changes they want and then create a pull request to merge their work into a main branch. Developers can also share the URL of the instance with teammates to see the changes when they review the code.

Here is what an instance, spun up with Pulumi, looks like:

<img class="block mx-auto md:max-w-4xl my-8"
src="/images/case-studies/bitbucket-cloud-diagram.png" alt="Bitbucket Cloud and Pulumi">

### Using the Automation API

The [Pulumi Automation API]({{< relref "/docs/guides/automation-api" >}}) exposes the full power of infrastructure as code through a programmatic interface instead of CLI commands. It exposes Pulumi programs and stacks as strongly-typed and composable building blocks, enabling developers to automate deployments directly from their code at run-time. (A Pulumi program, which is written in your chosen programming language, describes how your cloud infrastructure should be composed.)

Mike and the rest of the DevSpeed team have found many creative ways to use the Automation API to make changes to their infrastructure easily. One example is that they wanted to update the address of their primary database across all developer environments, which was using a raw address from AWS. Instead, they wanted to update the addresses with something more readable. They used the Automation API to write Python code that would automatically select every running instance and make the change. Next, Mike’s team is looking to use Automation API to automatically deploy and run Bitbucket developer environments as a full integration test.

### Results

Using Pulumi with its existing CI/CD process, the DevSpeed team built a self-service dashboard that enables any Bitbucket developer to quickly and easily provision a cloud-based development environment. Compared to the DSL-based tool they previously used, Pulumi significantly reduced the number of lines of code needed and made it much easier to read and understand. In terms of user satisfaction, the new dashboard meant that developers went from spending one day a week maintaining their environment to less than four hours per week. Mike’s team also receives significantly fewer infrastructure questions from developers on their Slack help channel.

## Summary

Here is a summary of how Pulumi helped Bitbucket and the DevSpeed team.

- Allowed developers to use general purpose programming languages like Python and familiar software tools to deliver and manage infrastructure
- Enabled Bitbucket developers to easily provision approved cloud infrastructure using a self-service dashboard built with Pulumi
- Reduced the time Bitbucket developers spent maintaining their instances from 8 hours per week to fewer than four.
- Boosted productivity of developers in Sydney by extending cloud deployments into another AWS region using Infrastructure as Code in Python
- Reduced the size and complexity of codebase for managing infrastructure while increasing its clarity
