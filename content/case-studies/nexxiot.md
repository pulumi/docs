---
title_tag: Nexxiot | Case Studies
title: "Nexxiot: Infrastructure Management for IoT Operations"
description: |
    Nexxiot adopted Pulumi to streamline cloud infrastructure management, removing the burden of maintaining custom tooling while achieving zero infrastructure-related outages.
meta_desc: Learn how Nexxiot worked with Pulumi to transform their infrastructure management, saving engineering resources and improving reliability.
meta_image: "/images/case-studies/nexxiot.png"

customer_name: Nexxiot
customer_logo: /logos/customers/nexxiot.svg
customer_url: https://www.nexxiot.com/

quote_block:
  quote: >
        You will run into limits with Terraform. 
        
        You will run into limits with CDK. 
        
        Your biggest chance to not run into troubles and limitations is to use Pulumi. It is the most powerful and versatile tool out there.
  quote_attrib: Alexander Berger, Site Reliability Engineer, Nexxiot
  headline_stat: 100%
  headline: Infrastructure reliability since adoption

exec_summary: |
   Nexxiot, a Swiss IoT company managing the world's largest network of connected shipping containers and railcars, needed to modernize their infrastructure management to meet growing customer expectations for SaaS reliability. After experiencing limitations with Ansible, Terraform, and AWS CDK, they found Pulumi's programmatic approach transformed their ability to manage cloud infrastructure. By adopting Pulumi, they eliminated custom tooling maintenance - saving the equivalent of two full-time engineers - while achieving zero infrastructure-related outages. With Pulumi's strongly-typed approach and flexible state management, they now manage their multi-region AWS infrastructure efficiently, supporting critical IoT operations.

sections:
    - label: About Nexxiot
      anchor: about-nexxiot
    - label: Challenge
      anchor: challenge
    - label: Journey to Modern Infrastructure
      anchor: journey
    - label: Solution with Pulumi
      anchor: solution
    - label: Results and Benefits
      anchor: results
---

## About Nexxiot

{{< youtube "nNd4uxmNoA4?rel=0" >}}

Nexxiot is digitalizing freight asset management with technology that oversees the world's most extensive network of connected shipping containers and railcars. Based in Zurich, Switzerland, with operations across Europe and North America, their IoT platform provides real-time insights into shipping container and railcar events, from impacts and delays to security incidents and loading activities.

## Legacy Infrastructure Challenges

In 2017, Nexxiot's infrastructure team relied on Ansible to manage their growing cloud footprint. While Ansible excelled at traditional IT operations - SSHing into servers and running package managers - it was fundamentally misaligned with Nexxiot's cloud-native aspirations.

"Ansible is totally the wrong tool for this job," explains Alexander Berger, Site Reliability Engineer at Nexxiot. "If you have to spin up VMs, if you have to spin up something in cloud infrastructure on AWS, that's not what it's good at. It's good at creating an SSH connection into existing hosts and then applying package manager calls."

The team wanted to move away from traditional server maintenance where machines were updated in place. Instead, they envisioned an immutable infrastructure approach where VMs would be replaced every 30 days with fresh instances running the latest OS versions. This fundamental mismatch between their tooling and their infrastructure philosophy forced them to look for alternatives.

## Journey Through Terraform

After realizing Ansible couldn't meet their cloud-native needs, Nexxiot evaluated the infrastructure-as-code tools available in 2017. Terraform seemed like a natural choice - it was purpose-built for cloud infrastructure and offered a clean declarative approach to resource management.

However, the team quickly encountered fundamental limitations. "Whenever you need a loop, whenever you have something pre-existing and you want to apply something for each item that already exists, it becomes very tricky," explains Berger. "You can do it, but you often run into limitations."

To work around these constraints, the team built an increasingly complex toolchain. They developed Python scripts that used Jinja templating to generate Terraform configurations. This introduced new challenges - the team now had to maintain expertise across three different technologies: Terraform, Python, and the Jinja2 templating framework.

"We didn't like having to use Python and Jinja because there was no type safety, no compiler that tells us if something is wrong," Berger notes. "We really don't like to run stacks that after half an hour just tell you 'oh sorry there's a null pointer exception over there' after waiting 30 minutes."
The maintenance burden of this custom tooling became unsustainable, especially for a team that didn't consider themselves a Python shop. They needed a solution that would provide both the flexibility of a programming language and the safety of strong type checking.

## AWS CDK: Promise and Limitations

By 2018, Nexxiot's search for a better solution led them to evaluate AWS CDK in its early release. The imperative approach seemed promising - finally, a way to programmatically define infrastructure without complex templating workarounds.

"We already got a good feeling this is the right direction," says Berger. "It's imperative infrastructure as code, where we can program quite flexible things."
However, CDK's reliance on AWS CloudFormation as its underlying deployment engine introduced critical limitations. CloudFormation's state management proved particularly problematic for a 24/7 SaaS operation. When stacks entered a broken state, the only recourse was to delete and recreate them entirely.

"You cannot easily export, modify and import a broken state," Berger explains. "If a stack is in a broken state, you usually have to delete it. Just imagine if you have a database system owned by a CloudFormation stack and you have to delete the stack. You cannot afford to delete the database - you have data inside. You cannot afford the downtime this would cause."

The team found themselves questioning how other companies managed with these constraints. "We are quite surprised how many companies get away with using CloudFormation, given these kinds of limitations," notes Berger. "Maybe this is explaining why they sometimes have downtime."

## Solution: Modern Infrastructure with Pulumi

Then Nexxiot discovered Pulumi: "We immediately realized it has actually all the advantages of CDK - it's imperative, it supports TypeScript which is a strongly typed language, so we can profit from type checking of a compiler," explains Berger. Most critically, Pulumi's approach to state management solved their showstopper issues with CloudFormation. "The state is actually something that you can extract into a JSON file where you can manually edit it and fix it and then import again and work on."

The team took their implementation further by leveraging Pulumi's Automation API, moving beyond basic YAML configuration to manage their infrastructure entirely through TypeScript. This allowed them to share configuration across different stacks and environments programmatically, while maintaining type safety throughout their codebase.

## Results and Impact

The impact was immediate and sustained. "Since we started using Pulumi, we never had any kind of outage caused by infrastructure management," reports Berger. "It works, it gets the job done, and we never had an outage."

The financial benefits were equally clear - eliminating custom tooling maintenance saved the equivalent of two full-time engineers. "It was cheaper for us to pay the subscription fee than to have two people on the payroll who try to maintain and understand all the tooling that we would otherwise have built ourselves."

For teams considering infrastructure modernization, Berger offers clear advice: "I would recommend using Pulumi for everybody who starts on a Green Field approach with infrastructure as code because I'm quite sure and confident to be able to say that it is the most powerful and versatile tool out there. You will run into limits with Terraform, you will run into limits with CDK. Your biggest chance to not run into troubles and limitations is to use Pulumi."
