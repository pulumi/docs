---
title_tag: Nexxiot | Case Studies
title: "Nexxiot: Infrastructure Management for IoT Operations"
description: |
    Nexxiot adopted Pulumi to streamline their cloud infrastructure management, eliminating custom tooling maintenance while achieving zero infrastructure-related outages.
meta_desc: Learn how Nexxiot worked with Pulumi to transform their infrastructure management, saving engineering resources and improving reliability.

customer_name: Nexxiot
customer_logo: /logos/customers/nexxiot.svg
customer_url: https://www.nexxiot.com/

quote_block:
  quote: |
        "I would recommend using Pulumi for everybody who starts on a Green Field approach with infrastructure as code because I'm quite sure and confident to be able to say that it is the most powerful and versatile tool out there. You will run into limits with Terraform, you will run into limits with CDK mostly because it's based on CloudFormation. Your biggest chance to not run into troubles and limitations is to use Pulumi."
  quote_attrib: Alexander Berger, Site Reliability Engineer, Nexxiot
  headline_stat: 2
  headline: Engineering headcount saved by eliminating custom tooling maintenance

exec_summary: |
   Nexxiot, a Swiss IoT company managing the world's largest network of connected shipping containers and railcars, needed to modernize their infrastructure management to meet growing customer expectations for SaaS reliability. After experiencing limitations with Ansible, Terraform, and AWS CDK, they found Pulumi's programmatic approach transformed their ability to manage cloud infrastructure. By adopting Pulumi, they eliminated custom tooling maintenance - saving the equivalent of two full-time engineers - while achieving zero infrastructure-related outages. Using Pulumi's strongly-typed approach and flexible state management, they successfully manage their multi-region AWS infrastructure supporting critical IoT operations.

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

{{< youtube "IIz0YBFxTEg?rel=0" >}}

Nexxiot is digitalizing freight asset management with technology that oversees the world's most extensive network of connected shipping containers and railcars. Based in Zurich, Switzerland, with operations across Europe and North America, their IoT platform provides real-time insights into shipping container and railcar events, from impacts and delays to security incidents and loading activities.

## The Infrastructure Challenge

As an AWS-native organization operating across multiple regions, Nexxiot faced growing pressure to maintain reliable infrastructure for their IoT services. "We really don't like to run stacks that after half an hour just tell you 'oh sorry there's a null pointer exception over there' after waiting 30 minutes," explains Alexander Berger, Site Reliability Engineer at Nexxiot. "That's not what we do - not just because we don't want to face the risk of infrastructure being broken, but because we want to make sure we make optimal use of our precious time."

Their journey through different infrastructure tools revealed increasing complexity at each step. With Terraform, they encountered fundamental limitations. "Whenever you need a loop, whenever you have something pre-existing and you want to apply something for each item that already exists, it becomes very tricky," notes Berger. The team found themselves building elaborate workarounds: "We had to maintain three things - Terraform know-how, Python know-how, and Jinja templating framework know-how. We didn't like having to use Python and Jinja because there was no type safety, no compiler that tells us if something is wrong."

## Finding the Right Solution

Attempting to solve these challenges with AWS CDK and CloudFormation introduced new problems. The breaking point came when they realized the implications of CloudFormation's state management limitations. "You cannot afford to delete the database - you have data inside. You cannot afford the downtime this would cause, but you can also not afford the data loss," Berger emphasizes. "In a 24/7 SaaS business, you cannot just tear down your infrastructure."

The team needed a solution that would provide the benefits of modern infrastructure as code without compromising their ability to maintain continuous operations. They found their answer in Pulumi.

## Programming with Pulumi

"We immediately realized it has actually all the advantages of CDK - it's imperative, it supports TypeScript which is a strongly typed language, so we can profit from type checking of a compiler," says Berger. The ability to manage state was transformative: "The state is actually something that you can extract into a JSON file where you can manually edit it and fix it and then import again and work on."

Using TypeScript for both infrastructure code and configuration management simplified their entire toolchain. As Berger explains, "Having it in a shared place but with full control over who can access this state - which of my team members are actually entitled to deploy to this environment or change it - these are the key benefits."

## Results

The impact of adopting Pulumi was immediate and sustained. "Since we started using Pulumi, we never had any kind of outage caused by infrastructure management," reports Berger. "It works, it gets the job done, and we never had an outage."

The financial benefits were equally clear: "In our case, things became much cheaper. It was cheaper for us to pay the subscription fee than to have two people on the payroll who try to maintain and understand all the tooling that we would otherwise have built ourselves."

For others considering the move to Pulumi, Berger offers this advice: "Take your time to understand the essence and the concepts of Pulumi before you go all in. I'm quite sure and confident to be able to say that it is the most powerful and versatile tool out there. You will run into limits with Terraform, you will run into limits with CDK mostly because it's based on CloudFormation. Your biggest chance to not run into troubles and limitations is to use Pulumi."
