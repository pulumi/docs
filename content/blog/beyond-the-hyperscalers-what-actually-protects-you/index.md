---
title: "Beyond the Hyperscalers: What Actually Protects You"
date: 2026-09-16T06:00:00-07:00
meta_desc: "Three people who have priced leaving AWS spent an hour arguing about cloud sovereignty. Here is the recording, and the advice each of them gave."
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
---

*Recorded September 3, 2026. Quotes are lightly edited for clarity.*

<!--more-->

Maybe this sounds familiar. You run infrastructure at a company that isn't American. Your workloads are on AWS, Azure, or Google Cloud, probably more than one, because that is what everyone picked. Until recently nobody asked you where the data lives or who can reach it.

Now you're getting questions. Legal wants to know what NIS2 means for where your systems run. Someone on the leadership team read that the US government locked the cloud accounts of judges at the International Criminal Court and wants to know if that could happen to you. Finance wants to know why the bill went up again. A customer's security review asked, in writing, which country your data sits in.

So now you have questions of your own:

- If a US court or agency wants my data, can they get it from my provider without involving me?
- Does putting everything in an EU region change that?
- The big providers now sell "sovereign cloud" in Europe. Is that different, or a rename?
- If I encrypt everything and hold the keys myself, am I covered?
- Could my account be switched off one day? What would I do?
- Are Hetzner, OVH, and Scaleway usable for real workloads?
- How much cheaper are they once you count the migration?
- What should I be building on now so I can leave later if I need to?
- A migration like this used to be a multi-year project. Does Pulumi and agentic infrastructure change that?
- Is any of this worth the disruption, or should I leave what works alone?

I put those questions to three people who have each dealt with this for real. One of them helps EU companies work out their exposure and builds the tooling to leave. Another has spent fifteen years sizing what cloud actually costs, and thinks most people should stay put. The third moved his company off AWS and onto a European provider. They don't agree on how big the risk is. The full hour is below.

{{< youtube "XF_W6pCBS50" >}}

## Don't just default to the hyperscalers

**Waldemar Kindler** co-founded [Think Ahead Technologies](https://think-ahead.tech/en), where he helps EU companies assess their risk and exposure to the big clouds and builds tools for moving off them. The calls used to come mostly from critical infrastructure like energy, utilities, and telecoms. Now, he says, they increasingly come from ordinary mid-sized German companies that want more options, usually because the costs have gotten too high.

His advice was the practical one: go try another cloud.

{{< say author="waldemar-kindler" >}}
I think we've seen plenty of reasons why it makes sense to at least have a choice, right? Which cloud to use, and not to just default to the big hyperscalers because they are hyperscalers. And yeah, I would just highly suggest, make sure or think about how you can be portable, how you can at least get fewer dependencies, and just try other clouds out. It's definitely worth it. It's really, really fun having a look at Scaleway, Hetzner, OVH — all great services.
{{< /say >}}

## Know what business you are in

**Sarbjeet Johal** is a cloud economist and the panel's only US resident. He started doing cloud assessments at VMware, then moved to Rackspace, "Rackspace used to be number two cloud, believe me or not," and has sold and sized cloud for about fifteen years since. He's an economics major who has been a technologist since 1994, and he came at every question through the economics.

His answer came down to not moving what already works.

{{< say author="sarbjeet-johal" >}}
I think the key is that you have to know what business you are in. Are you an auto company, or an airline, like an aviation company, or a health care company, or are you a computing company? So you have to decide where you want to put most of your efforts in. Technology is a bigger and bigger part of the economy now. So can you rely on a technology partner which is not you yourself? So that means, can you rely on cloud? So that is the question which people are grappling with.

Another thing we did not talk about during this discussion is vendor rationalization. Most companies are trying to have fewer vendors so they can manage their spend, they can negotiate better, because they're spending a lot more money with them. So vendor rationalization is key, and the antithesis of that, the opposite of that, is best of breed — what Waldemar was saying, get the best of breed. And I think that works only if everything is portable, which is a very big assumption to make, which is hard to achieve.

So, all in all, I think if you have some workloads which are time tested and they're working, they can stay where they are. Keep them where they are, and then change only when you're rewriting that, or you're getting acquired, or you are acquiring somebody else and then there's a big change. Only then touch those systems. So keep those in house if they are there and they're good economics.

Go to cloud when you can, stay local when you need to.
{{< /say >}}

## Build for portability, or be a digital colony

**Jim Dowling** is co-founder and CEO of [Hopsworks](https://www.hopsworks.ai) in Stockholm, an AI lakehouse platform. He's the one on the panel who has actually done the migration: Hopsworks moved its SaaS platform off AWS to OVHcloud and its development infrastructure to Hetzner, cutting the bill by [62%](https://www.hopsworks.ai/post/migrating-from-aws-to-a-european-cloud-how-we-cut-costs-by-62). He says the move only worked because they had built on Kubernetes and hadn't written their code against the native cloud APIs.

He starts with blunt advice for developers, then turns to sovereignty itself.

{{< say author="jim-dowling" >}}
My advice for developers is build for portability. So, if you're building an app, build on Kubernetes. Do not build cloud native applications. You will get screwed. The price differential now is massive. If you have a workload that you want to move off a public US vendor to a European cloud, you can save a lot of money. We did that. For some workloads — other workloads we won't move.

And the main thing I would say is that the reason we're talking about sovereignty is because you cannot have sovereignty without digital sovereignty. So, if Europe aspires to be sovereign and to decide its own rules, we decide we want to be a democracy or whatever — unless we control our own digital infrastructure, we cannot, because you end up being a digital colony, and that's the moment we are at at this point in time. So I think that is beyond the technical decisions of cloud benefits, of costs, and analysis of your cloud.

I think that's why this discussion is interesting to many people, because they realize that we're at a position just like the US was in the 1850s. The US had invited in the British and said, please build our railways, our railroads. And the British said, yeah, we'll build them. And then the British said, we have these cars that drive on them, these train cars. And you go, great. And the Americans said, well, what can you do in the cars? And they said, well, you can sell coffee. Okay, great. And they said, give us 30%.

So that's currently where the rest of the world is, outside the US: we're allowed to sell coffee, but the providers keep 30%. So, will we be a digital colony in 20 years' time? I don't know. We are today. That's where we are.
{{< /say >}}

The recording above goes much deeper than these three answers do. It gets into whether an EU region or a European subsidiary of a US provider actually gets you out from under the US CLOUD Act, and who holds the encryption keys when a subpoena arrives. It also covers Kubernetes as a portability layer versus needing a marketplace of specialised European providers, and whether Europe could fund a cloud of its own with public money, the way it once built Airbus. And watch to find out how Pulumi and agentic infrastructure make moves like these easier than they have ever been.

If you want to hear about more sessions like this one, they all go up on the [events page](https://www.pulumi.com/events/).
