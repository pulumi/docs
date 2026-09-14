---
title: "Beyond the Hyperscalers: What Actually Protects You"
date: 2026-09-10T06:00:00-07:00
draft: true
meta_desc: "Three people who have priced leaving AWS, on what cloud sovereignty actually means, which escape hatches work, and what is worth doing even if you never move."
feature_image: feature.png
authors:
    - waldemar-kindler
    - jim-dowling
    - sarbjeet-johal
    - adam-gordon-bell
author_roles:
    adam-gordon-bell: "as told to"
tags:
    - kubernetes
    - aws
    - platform-engineering
    - migration
category: customers
social:
    twitter: |
        Sovereign cloud regions, encrypted buckets, a European subsidiary. Which of these actually protects you from a US subpoena? A panel of three who have priced the switch, and don't agree on when it's worth it.
    linkedin: |
        Most teams outside the US run on a US hyperscaler and have never had to think about it. The signals are changing: new regulation at home, a bill that keeps climbing, and a few well-publicised account shutoffs.

        Waldemar Kindler, Jim Dowling and Sarbjeet Johal joined me to argue it out. They agreed on more than I expected, and the places they didn't are the useful part.
    bluesky: |
        Which cloud "sovereignty" measures actually protect you? Three people who have priced leaving AWS, arguing it out.
---

*Adapted from a Pulumi panel recorded September 3, 2026. Waldemar Kindler is co-founder of [Think Ahead Technologies](https://think-ahead.tech/en) in Stuttgart, where he helps companies assess their exposure to the hyperscalers and plan a way out. Jim Dowling is co-founder and CEO of [Hopsworks](https://www.hopsworks.ai) in Stockholm, which moved its platform from AWS to OVHcloud and cut the bill by 62%. Sarbjeet Johal is a cloud economist, theCUBE analyst, and founder of [StackPane](https://stackpane.com), and spent years selling cloud at VMware and Rackspace. Quotes are lightly edited for length.*

<!--more-->

{{< youtube "XF_W6pCBS50?rel=0" >}}

Years ago I worked at a company selling software to Canadian municipalities. Tax records, zoning: it had to stay in Canada. No AWS region existed, so we ran on a Canadian provider with an OpenStack-style API for provisioning VMs. It worked, with a lot of care and feeding. Then AWS opened Montreal, we moved, and never thought about it again. Residency was the problem; a region setting solved it.

Same job today, and the signals are different, whether the desk is in Toronto, Stockholm, or Copenhagen. Canada: three US companies hold [85% of the public cloud market](https://antimonopoly.ca/parting-clouds-creating-a-competitive-marketplace-for-compute/), Ottawa is [procuring a sovereign cloud](https://www.canada.ca/en/shared-services/corporate/about-us/transparency/departmental-plan/2026-27/shared-services-canada-2026-27-departmental-plan.html) from providers outside foreign access laws, and the law firms say the CLOUD Act turns on [who controls the provider, not where the server sits](https://www.blg.com/en/insights/2026/04/data-sovereignty-and-the-cloud-act-what-canadian-organizations-should-know). Sweden: NIS2 has critical-infrastructure operators accounting for where systems run and who runs them, and the bill climbs regardless. Denmark: [Copenhagen and Aarhus are phasing out Microsoft](https://therecord.media/denmark-digital-agency-microsoft-digital-independence) over cost, dominance, and politics. The region setting stopped being the answer.

The question isn't "should I leave." Most of us won't. It's: what am I exposed to, what would leaving cost, and what's worth doing either way?

Three people who have each priced the switch, and don't agree on when it's worth it. Here's where they agreed, and where they didn't.

## 1. Figure out which problem you actually have

Three different problems get filed under "sovereignty." Residency: a law says where the data sits. Compulsion: a court, or a switch, reaches your data regardless of where it sits. Cost: the bill. They have different fixes, and the panel split on which one is actually sending people to the door.

{{< say author="waldemar-kindler" >}}
There's an EU law like NIS2 requiring you to operate your infrastructure in the European Union. But there are conversations of, okay, is it enough to have the data center be in Europe? Or do we need to go further, and does it mean no US company?

There's more and more of a switch from mainly critical infrastructure companies and government-close companies to the average German or European company.
{{< /say >}}

{{< say author="jim-dowling" >}}
One of the problems with AWS is we had user growth and we had service growth. We were enabling people to download more data quicker, by improving our platform, and that increased our costs, particularly with network egress. And we said, okay, what do we need to do to get off AWS?
{{< /say >}}

{{< say author="sarbjeet-johal" >}}
When statements are made that cloud is expensive, or cloud is cheaper, or innovation velocity is very high in cloud, all those are true, actually. It's a very contextual discussion. Cloud is cheap to operate when you are building a startup and you don't have that much CAPEX.
{{< /say >}}

I tried a fourth problem on them: public pressure, the customer who won't buy from a US supplier on principle. Waldemar didn't think it reaches infrastructure.

{{< say author="waldemar-kindler" >}}
Nobody will switch clouds just for political reasons, unless they have to. It's compliance regulations that we're seeing emerging in the EU more and more: the Cyber Resilience Act, NIS2, the AI Act, the Data Act. But I think cost is still the biggest driver.
{{< /say >}}

If a regulator names you, that's residency or compulsion, and you'll know which. If nobody has, it's cost, and cost is a spreadsheet, not a sovereignty question.

{{< notes type="info" size="large" >}}
**NIS2** is the EU's 2024 network and information security directive. It puts supplier-risk and incident-reporting obligations on operators of critical services, such as energy, telecoms, health, and transport, and on their major suppliers. **The Cyber Resilience Act** applies to products with digital elements sold in the EU; its vulnerability-reporting duties start in September 2026, with full obligations in 2027. Neither one orders you off a US cloud. Both make you account for what runs where, and under whose control.
{{< /notes >}}

## 2. Measure the lock-in before deciding anything

Your exposure is not "we're on AWS." It's the pile of things you run that only run on AWS. Jim's move to OVHcloud was a backup and a restore because that pile was empty, and it was empty on purpose.

> "We minimized dependencies when we built our platform. We'd rewritten everything for Kubernetes, so now we could move to any other cloud provider that had Kubernetes. We did have a dependency on an S3-compatible storage layer, and we did use a container registry at AWS."
>
> "We deploy the platform using Terraform. We weren't using cloud native, like CloudFormation. Again, why would you be using CloudFormation? That would be crazy."

{{< panel-quote author="jim-dowling" >}}
"Not locking yourself into a cloud by writing against the native APIs is the best way to keep your optionality, to be able to migrate your workloads with lower costs."
{{< /panel-quote >}}

That was not foresight, and he was clear about it. Hopsworks started with a managed platform built on AWS-native services, then rewrote for Kubernetes years later because customers were asking for it. "We did have some cost in our managed platform, but we ate it."

Sarbjeet's point was that the lock-in nobody measures is people:

> "People work in your company as a developer, sysadmin. They have to earn money. They have to decide which certification I want to get, this or that. They think about their livelihood, and if their skills are not transferable from one company to another, they will not go for that skill."

Jim's reply, in full: "I think that's kind of amusing in the age of Kubernetes, to be honest."

For the audit, sort what you run into three piles. **Portable:** Kubernetes, S3-compatible storage, Postgres-compatible databases, plain VMs. **Swappable with effort:** queues, caches, managed Redis. **Stuck:** Cognito, DynamoDB, Lambda wired into Step Functions and EventBridge, keys in KMS, everything that only exists as IAM policy. The stuck pile is your exposure. Until it's in code, you can't even see it.

## 3. Cheap insurance, whether or not you ever leave

Three things the panel agreed are worth doing if you stay.

**Put everything in code, because agents can now move code.** This was the closest the panel came to unanimity. Engin read a chat question asking whether migrations, which used to be multi-year projects, had gotten easier. Jim: "Yeah. I migrated all dev infra to Proxmox and it was very little effort, using code." Waldemar went further:

{{< panel-quote author="waldemar-kindler" >}}
"AI is the thing that drives portability, or significantly improves it. If I have my infrastructure as code and then I throw an agent on that, I can move so quickly it's insane."
{{< /panel-quote >}}

This is the part I care about professionally, so take it with the appropriate salt. At Pulumi we publish skills for moving from Terraform or CDK to Pulumi, and we watch people point a coding agent at that work and finish it in an afternoon. The same mechanism applies to moving between clouds: scan the account, let the agent write the infrastructure as code, and now it's code, and code moves. Easy is in air quotes. Our professional services group does these migrations for a living and would object to the word. But the projects you wouldn't have attempted because the cost was absurd are now projects, and that changes the math even if you never run them.

Sarbjeet turned it around on me: "Because refactoring is easy and migration is easy now, people will hop onto the cloud more?" Probably yes. Portability cuts both ways, and that's fine.

**Hold your own keys.** A chat question from Paul: we're in eu-central-1, S3 and RDS encrypted with KMS, does that stop a US subpoena? Jim: "No, it won't stop a subpoena, no."

> "You can of course encrypt your own data with your own keys and keep them off the cloud. But if your keys are stored there as well and somebody really wants to get it, you need to keep your keys off the cloud. And there's not many who do that, I guess."

{{< notes type="info" size="large" >}}
**Bring your own key** means you generate the key and import it into the provider's key service. The provider still holds a copy and can still decrypt on a lawful order. **Hold your own key** means the key never leaves hardware you control and the provider calls out to you to decrypt. Only the second changes the subpoena answer, and only for data at rest. A running database has to decrypt to work, so it stays reachable either way.
{{< /notes >}}

**Build on Kubernetes.** All three said it. They don't agree it's enough.

> **Jim:** "Ten years ago Kubernetes wasn't there. Now it's there, and if you don't choose Kubernetes now, you really need to justify that decision. It should be the de facto framework for people building applications and services in the cloud."
>
> **Waldemar:** "Kubernetes is not enough as an abstraction. We need that marketplace of small specialized providers who have great services, and an abstraction layer over that. This will be a huge push, and the European Union and many companies within the EU are working on exactly that."
>
> **Sarbjeet:** "You can't avoid vendor lock-in even in the open source world. If you take a distribution of Kubernetes from vendor A versus B, there are minor differences. You still have to do some work to port those things."

## 4. What the escape hatches actually cost

Three doors. The panel was unanimous on the first, split on the second, and Sarbjeet owned the third.

**Door one: the hyperscalers' own sovereign clouds.** AWS, Microsoft, and Google each now sell a European sovereign offering, from a data boundary inside the same cloud, to a separate partition run by an EU subsidiary, to a partner company operating their stack under its own name. I asked whether any of that helps.

> **Jim:** "The problem is not technical, it's judicial. Where does the parent company reside, and under what law is it covered? Microsoft said in the French parliament, if we're asked to transfer data, we will do it. If you're an American parent company with a subsidiary in Europe that you say is only staffed by Europeans, only run by Europeans, you're still subject to the CLOUD Act."

Sarbjeet, playing devil's advocate, suggested the providers will spin up genuinely independent companies and hold a financial stake instead. Jim: "We have a term for that. It's called sovereign washing."

{{< panel-quote author="waldemar-kindler" >}}
"The question is easy: which problem does it solve? Does it cost less? Absolutely not, it's usually more expensive. Does it solve sovereignty? Also not really."
{{< /panel-quote >}}

{{< notes type="info" size="large" >}}
**Three rungs of "sovereign cloud."** A *data boundary* keeps your data and support traffic inside a region of the same cloud, run by the same company. A *sovereign region* is a separate partition, like GovCloud, operated by a European subsidiary with European staff. A *trusted partner* is a separate company, such as Bleu in France or Delos in Germany, running the hyperscaler's technology under its own ownership. Only the third moves the operator out of US jurisdiction, and it costs the most and offers the least.
{{< /notes >}}

**Door two: a smaller, non-US cloud.** This was the live disagreement of the hour. Waldemar's warning:

> "One aspect people extremely underestimate is the cost of compliance. Of course you can go to Hetzner and it's probably ten times cheaper. But good luck achieving ISO 27001 certification on that. You have to recertify everything because you're changing your processes and your execution environment. You will not get single sign-on. You have to rebuild everything from scratch."

Jim, immediately: "But Waldemar, we're both ISO 27001 and SOC 2 compliant, and we moved, and it was no problem."

Then Jim's case that OVHcloud wasn't just cheaper. It was better, because AWS prices local disk to protect S3:

> "All system software in my space has been rewritten to store the data on S3. I can buy an NVMe for my server here with 20 gigabytes per second, but I go to the cloud and I can't even get a gigabyte per second in AWS. They keep this differentiation because it benefits them. In OVH we get much better disks and much better prices, so we actually run the platform better."

What broke: the managed database behind OVHcloud's Kubernetes control plane was capped at half a gigabyte at the time, since raised. What you lose, in his words: "If you're running on OVH and you need some sort of content management system, you probably need Cloudflare or someone in front of that to protect against DDoS. Smaller clouds won't have that."

Sarbjeet's counter is the one every CTO will hear from their board: "Their base of innovation lags US providers. If you are a big corporation and you want to tap into the latest developments, especially now when it comes to AI, who can give you GPUs faster?"

**Door three: stay, and stop pretending you're leaving.** Sarbjeet's, and he made it without apology:

> "If you have some workloads which are time-tested and working, keep them where they are. Change only when you're rewriting, or you're getting acquired, or you're acquiring somebody else and there's a big change. Only then touch those systems."

His evidence is from a decade of utilization audits at EMC and VMware, across more than a million servers: storage under 20% utilized on-prem, compute under 30%, rising to 50 to 70% in the cloud. Jim's reply was that on the ground it's worse, "15% or something, it still hasn't changed, it's lift and shift," which is an argument for Sarbjeet's door, not against it.

## 5. The part that isn't about your bill

The reason this panel exists. Compulsion is not hypothetical, and the organizations acting on it are not companies.

{{< panel-quote author="jim-dowling" bg="2" >}}
"Copenhagen, Aarhus, they've all moved, they're moving off Microsoft. All the schools, the hospitals, they're all running Microsoft. And they did an analysis and said, if the US wants to take Greenland, they turn off Azure. In 30 minutes Denmark shuts down."
{{< /panel-quote >}}

> **Jim:** "There is a massive concern in Europe that tech is a kill switch. If you're building on this technology and it can be turned off at any second, then you can't have your own laws. Even though companies, as Waldemar said, won't make that decision, it's happening at government level, at defense level."
>
> **Waldemar:** "The risk is pretty real. We've seen that the US government has locked down accounts for judges from the International Criminal Court. And the legal frameworks that were built to even allow using US clouds, they're also breaking up."

{{< notes type="info" size="large" >}}
**The CLOUD Act** (2018) lets US authorities compel a US-controlled company to hand over data in its "possession, custody, or control," wherever in the world that data is stored. Residency does not enter into it. The Microsoft Ireland case that prompted the law was about email on a server in Dublin.
{{< /notes >}}

Then the exchange that set the room's temperature:

> **Jim:** "We consider the world to be a world of laws, and I think that's no longer the case. We're at the end of the rule-based global order, and this whole digital sovereignty thing is part of that."
>
> **Adam:** "I feel like your takes are so dark."
>
> **Jim:** "This is a fact. I mean, come on."
>
> **Sarbjeet:** "I don't think the rule-based world order is gone. It's more like injured. It's not dead."

## 6. Write down what would make you move

I asked each of them for a closing thought. Three answers to the same question, and they don't reconcile, because your answer depends on which problem from section 1 you actually have.

> **Waldemar:** "We've seen plenty of reasons why it makes sense to at least have a choice, and not to just default to the big hyperscalers because they are hyperscalers. Think about how you can be portable, how you can get fewer dependencies, and just try other clouds out. It's really fun having a look at Scaleway, Hetzner, OVH."
>
> **Jim:** "Build for portability. If you're building an app, build on Kubernetes. Do not build cloud native applications. You will get screwed. The price differential now is massive. We did that. For some workloads. Other workloads we won't move."

{{< panel-quote author="sarbjeet-johal" >}}
"You have to know what business you are in. Are you an auto company, an airline, a healthcare company, or are you a computing company? Go to cloud when you can, stay local when you need to."
{{< /panel-quote >}}

My version: write down what would make you move. A named regulator, a named customer, a specific number on a bill. If none of them fires, stay, with the insurance from section 3 in place. The failure mode isn't staying on AWS. It's staying without knowing what it would take to leave.

Jim got the last word on the panel, and he gets it here.

> "You cannot have sovereignty without digital sovereignty. If Europe aspires to decide its own rules, then unless we control our own digital infrastructure, we cannot, because you end up being a digital colony. We're at the position the US was in the 1850s. The US invited in the British and said, please build our railroads. And the British said, we have these train cars. And the Americans said, great, what can we do in the cars? And they said, you can sell coffee. Give us 30%. That's where the rest of the world is today, outside the US: we're allowed to sell coffee, but the providers keep 30%. Will we be a digital colony in 20 years' time? I don't know. We are today."
