---
title: "Pulumi adoption made easy with the new Migration Hub"
allow_long_title: True
authors: ["joe-duffy"]
tags: ["opensource", "migration", "import"]
meta_desc: "Introducing the Pulumi Migration Hub, your one stop shopping for migrating to Pulumi. It's never been so easy to adopt Pulumi."
date: "2023-08-22"
meta_image: "migration_hub.png"
---

Today we are launching Pulumi's new [Migration Hub]({{< relref "/migrate" >}}), a comprehensive guide to help you
seamlessly adopt Pulumi no matter where you are coming from, whether that's Terraform, CloudFormation, ... or even
manually provisioned resources not yet governed by an infrastructure as code solution. Our new Expert Services group is
ready to roll up their sleeves to help you adopt Pulumi faster. The Migration Hub also features many commercial offers
for open source foundations, startups, and complementary migration, to minimize switching costs and risks. It's never
been easier to adopt Pulumi.

<!--more-->

## Why Pulumi?

Nearly 2,000 customers and over 100,000 practitioners have chosen Pulumi for their infrastructure as code needs. About
half the time, these end users have an existing infrastructure as code solution that has stopped meeting their needs.
The other half of the time, infrastructure may have been created in the cloud console ("click-ops"), using a cloud CLI,
or some other manual provisioning tool, but now needs to become repeatable and scalable using infrastructure as code.

The most common reasons teams prefer Pulumi include:

* Best-in-class productivity
* Accessible to the entire organization, thanks to industry standard languages
* Ability to deal with complexity at scale, thanks to stacks, config, sharing and reuse, and more
* Perfect confidence thanks to policies and testing
* Highly programmable engine can be embedded anywhere, to build custom platforms and tools
* Instant collaborative bridge between developers and infrastructure experts

Thanks to Pulumi, teams are able to do more with less, ship faster with confidence, tackle very challenging cloud
infrastructure projects and scale with them, empower more of the team to be self-serve and collaborate more closely,
and ultimately turn the cloud into a competitive advantage.

Pulumi is also [true Apache 2.0 open source]({{< relref "/blog/pulumi-hearts-opensource" >}}) and we welcome anyone who
wishes to build atop it.

## Migration

Of course, it's one thing to choose Pulumi, but another thing entirely to adopt it and get all of your infrastructure
under its management, especially if you have existing infrastructure. That might include converting existing code, or
even just importing existing manually provisioned cloud resources.

There are two major approaches to this challenge.

### Self-Serve Migration

Pulumi offers many tools and techniques should you want to perform a migration on your own.

In the most general form, Pulumi provides [an import command]({{< relref "/docs/using-pulumi/adopting-pulumi/import" >}})
which can import any existing infrastructure no matter how it was originally created, click-ops included.

Pulumi also offers conversion tools for other popular infrastructure as code solutions, including
[HashiCorp Terraform]({{< relref "/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform" >}}),
[AWS CloudFormation]({{< relref "/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-aws" >}}),
[Azure Resource Manager (ARM)]({{< relref "/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-azure" >}}), or
[Kubernetes YAML]({{< relref "/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-kubernetes" >}}).

Although the time to migrate existing infrastructure varies wildly based on the size and complexity of your scenario,
migrating a single cloud environment can often take as little as a few hours. And thanks to Pulumi being multi-language
at its core, these tools will support you the same no matter which language you choose, JavaScript, TypeScript, Python,
Go, C#, Java, and YAML alike.

To learn more about performing your own migration, please
[read this user guide]({{< relref "/docs/using-pulumi/adopting-pulumi" >}}).

### Let Us Help You Out with Expert Services!

Although self-serve is an option, there can often still be uncertainty around this approach.

It may not be clear how much time a full migration will take, leaving the possibility that you'll be left with multiple
infrastructure as code solutions -- either temporarily or even permanently. Although the tools are a huge help, they
don't always get you 100% of the way there. We also often hear that skilling yourself up on a one-time migration
activity takes away from critical time spent on business initiatives.

All of this adds friction, risk, and uncertainty to the Pulumi adoption decision. The last thing we want is for the
one-time migration to prevent you from adopting Pulumi. Thankfully, we are here to help!

_Today we are announcing the formation of Pulumi's **Expert Services** group_. This team of industry and
infrastructure as code experts is on standby and ready to roll up their sleeves to help you with migration,
training, and other services efforts. No project is too small: we are currently working with customers with
100KLOCs of legacy infrastructure as code that needs to be migrated, for example.

_Today we are also announcing an extension to
[our **Terraform Migration Offer**]({{< relref "/blog/tf-migration-offer" >}})_, in which we will bundle migration of
your Terraform projects with your [Pulumi Enterprise or Business Critical]({{< relref "/pricing" >}}) subscription.
Today we are excited to announce that this same package is now available for all migration efforts, including AWS
CloudFormation, Azure Resource Manager (ARM), ..., or even infrastructure that was manually provisioned. We are also prepared
to scale up from there depending on your needs.

## Success Stories

Over time, Pulumi is becoming a more comprehensive platform, with new services like
[Pulumi Deployments]({{< relref "/blog/pulumi-deployments" >}}) for multi-cloud deployment workflows and
[Pulumi Insights]({{< relref "/blog/pulumi-insights" >}}) for search, analytics, and AI for your cloud infrastructure.
Pulumi also offers [policies]({{< relref "/crossguard" >}}) and [secrets]({{< relref "/docs/concepts/secrets" >}}) as
core features of the platform. [Enterprises]({{< relref "/enterprise" >}}) are increasingly betting on Pulumi for
their entire cloud management and platform needs.

By moving to Pulumi's platform, many customers have seen considerable benefits:

_[Atlassian **significantly increased developer velocity**]({{< relref "/case-studies/atlassian" >}})_, increasing
productivity by more than 2X and substantially decreasing the amount of time spent on maintenance tasks.

_[Mercedes-Benz **got the whole team shipping faster and with more confidence**]({{<
relref "/case-studies/mercedes-benz" >}})_ by building a platform that helped developers be self-serve with
infrastructure while scaling up to 100s of Kubernetes clusters worldwide.

_[Snowflake **rapidly improved time to market**]({{< relref "/case-studies/snowflake" >}})_ by betting on Pulumi,
empowering their engineers, and delivering the Data Cloud. Snowflake ultimately beat their IPO deadlines and knew legacy
infrastructure as code wouldn't do it.

_[Washington Trust Bank **modernized their cloud infrastructure and practices**](
{{< relref "/blog/how-a-bank-modernized-its-software-engineering-with-infrastructure-as-code-automation" >}})_,
speeding up internal delivery, while also increasing their confidence thanks to policy as code guardrails.

_[Fauna **adopted a born in the cloud mindset**]({{< relref "/case-studies/fauna" >}})_ and was able to build a
multi-cloud, highly scalable, modern SaaS application, actually increasing reliability even in the face of growing
complexity.

In each of these cases, the customer evaluated Pulumi against alternative infrastructure as code solutions, but
ultimately chose Pulumi due to the aforementioned benefits.

## Special Offers

In addition to migration services, Pulumi offers two programs to help get up and running quickly:

* [Open Source]({{< relref "/pricing/open-source-free-tier" >}}): Any open source foundation or project can use
  Pulumi Team Edition free of charge.

* [Startup Discount]({{< relref "/pulumi-for-startups" >}}): Any early stage startup gets $10,000 free credits and
  access to Pulumi Enterprise.

## Calling All Partners!

As Pulumi's market adoption has skyrocketed, we've begun to build out our official partner program. Although
we don't have anything major to announce (yet), we'd love to talk to you if infrastructure as code is an important
part of your own customers' needs. That includes ISV product integrations, global and regional systems integrators and
consultants, and more. Note that Pulumi is already available in the
[AWS](https://aws.amazon.com/marketplace/pp/prodview-dwn22batkhsyg) and
[Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/pulumicorporation1618431130005.pulumi_e1)
marketplaces. If you are interested in discussing a partnership, please [contact us]({{< relref "/contact" >}}).

## Get Started Today

Migrating from an existing solution can seem like a daunting task, but with Pulumi's new Migration Hub and Expert
Services, it has never been easier to adopt Pulumi than it is today. To learn more, visit the
[Migration Hub]({{< relref "/migrate" >}}) or simply [contact us]({{< relref "/contact" >}}) -- we would love to hear
from you.
