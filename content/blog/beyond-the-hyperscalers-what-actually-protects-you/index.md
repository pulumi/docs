---
title: "Beyond the Hyperscalers: What Actually Protects You"
date: 2026-09-17T06:00:00-07:00
draft: true
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
social:
    twitter: |
        Sovereign cloud regions, encrypted buckets, a European subsidiary. Which of these actually protects you from a US subpoena? A panel of three who have priced the switch, and don't agree on when it's worth it.
    linkedin: |
        Most teams outside the US run on a US hyperscaler and have never had to think about it. The signals are changing: new regulation at home, a bill that keeps climbing, and a few well-publicised account shutoffs.

        Waldemar Kindler, Jim Dowling and Sarbjeet Johal joined me to argue it out. They agreed on more than I expected, and the places they didn't are the useful part.
    bluesky: |
        Which cloud "sovereignty" measures actually protect you? Three people who have priced leaving AWS, arguing it out.
---

*Recorded September 3, 2026. Quotes are lightly edited for clarity.*

<!--more-->

Picture someone who runs infrastructure at a company that isn't US-based — maybe in Canada, like me, or somewhere in the EU. They're on AWS, or Azure, or GCP, or all of them, and they've never really had to think about it. Now the signals are coming from a few directions at once: regulations shifting at home, bills going up, geopolitical risk, maybe even social pressure in their own country.

That person is really asking three things. What does running on a US hyperscaler actually expose a non-US company to. Which of the usual answers change that exposure at all: an EU data center, a European subsidiary, encrypting your own buckets. And when is moving worth what it costs. I spent an hour on those with three people who don't always agree on what the risks are, or how big they are. The whole discussion is in the recording. Below is where each of them landed, and what they'd tell that person to do.

{{< youtube "XF_W6pCBS50" >}}

## Don't just default to the hyperscalers

**Waldemar Kindler** co-founded [Think Ahead Technologies](https://think-ahead.tech/en), where he helps EU companies assess their risk and exposure to the big clouds and builds tools for moving off them. The calls used to come mostly from critical infrastructure like energy, utilities, and telecoms. Now, he says, they increasingly come from ordinary mid-sized German companies that want more options, usually because the costs have gotten too high.

His advice was the practical one: go try another cloud.

{{< say author="waldemar-kindler" >}}
I can try. Yeah. So I think we've seen plenty of reasons why it makes sense to at least have a choice, right? Which cloud to use, and not to just default to the big hyperscalers because they are hyperscalers. And yeah, I would just highly suggest, make sure or think about how you can be portable, how you can at least get fewer dependencies, and just try other clouds out. It's definitely worth it. It's really, really fun having a look at Scaleway, Hetzner, OVH — all great services.
{{< /say >}}

## Know what business you are in

**Sarbjeet Johal** is a cloud economist and the panel's only US resident. He started doing cloud assessments at VMware, then moved to Rackspace, "Rackspace used to be number two cloud, believe me or not," and has sold and sized cloud for about fifteen years since. He's an economics major who has been a technologist since 1994, and he came at every question through the economics.

His answer came down to not moving what already works.

{{< say author="sarbjeet-johal" >}}
Yeah, I think the key is that you have to know what business you are in. Are you an auto company, or an airline, like an aviation company, or a health care company, or are you a computing company? So you have to decide where you want to put most of your efforts in. Technology is a bigger and bigger part of the economy now. So can you rely on a technology partner which is not you yourself? So that means, can you rely on cloud? So that is the question which people are grappling with.

Another thing we did not talk about during this discussion is vendor rationalization. Most companies are trying to have fewer vendors so they can manage their spend, they can negotiate better, because they're spending a lot more money with them. So vendor rationalization is key, and the antithesis of that, the opposite of that, is best of breed — what Waldemar was saying, get the best of breed. And I think that works only if everything is portable, which is a very big assumption to make, which is hard to achieve.

So, all in all, I think if you have some workloads which are time tested and they're working, they can stay where they are. Keep them where they are, and then change only when you're rewriting that, or you're getting acquired, or you are acquiring somebody else and then there's a big change. Only then touch those systems. So keep those in house if they are there and they're good economics.

The number one reason why people flock to cloud — I usually say that when so many people flock to cloud, they're not stupid. There's something there, that's why they're going there. I have done data center utilization audits of more than a million servers in many countries, when I was in EMC and VMware, that 10 years. The utilization rate of storage is below 20%. Utilization of compute is below 30% in most of the companies if you take the average. I think I'm being lenient when I say 30 and 20, it's even below that. So you're wasting so much infrastructure, and when you go to cloud, the utilizations go to 50, 60, sometimes 70% ranges. And consistency breeds smoothness, and that gives you good operations.

Go to cloud when you can, stay local when you need to.
{{< /say >}}

## Build for portability, or be a digital colony

**Jim Dowling** is co-founder and CEO of [Hopsworks](https://www.hopsworks.ai) in Stockholm, an AI lakehouse platform. He's the one on the panel who has actually done the migration: Hopsworks moved its SaaS platform off AWS to OVHcloud and its development infrastructure to Hetzner, cutting the bill by [62%](https://www.hopsworks.ai/post/migrating-from-aws-to-a-european-cloud-how-we-cut-costs-by-62). He says the move only worked because they had built on Kubernetes and hadn't written their code against the native cloud APIs.

He starts with blunt advice for developers, then turns to sovereignty itself.

{{< say author="jim-dowling" >}}
I mean, I don't disagree with anything in particular. But utilization levels are way lower on the ground, I think. If you look at companies, it's 15% or something, it still hasn't changed, it's lift and shift.

But my advice for developers is build for portability. So, if you're building an app, build on Kubernetes. Do not build cloud native applications. You will get screwed. The price differential now is massive. If you have a workload that you want to move off a public US vendor to a European cloud, you can save a lot of money. We did that. For some workloads — other workloads we won't move.

And the main thing I would say is that the reason we're talking about sovereignty is because you cannot have sovereignty without digital sovereignty. So, if Europe aspires to be sovereign and to decide its own rules, we decide we want to be a democracy or whatever — unless we control our own digital infrastructure, we cannot, because you end up being a digital colony, and that's the moment we are at at this point in time. So I think that is beyond the technical decisions of cloud benefits, of costs, and analysis of your cloud.

I think that's why this discussion is interesting to many people, because they realize that we're at a position just like the US was in the 1850s. The US had invited in the British and said, please build our railways, our railroads. And the British said, yeah, we'll build them. And then the British said, we have these cars that drive on them, these train cars. And you go, great. And the Americans said, well, what can you do in the cars? And they said, well, you can sell coffee. Okay, great. And they said, give us 30%.

So that's currently where the rest of the world is, outside the US: we're allowed to sell coffee, but the providers keep 30%. So, will we be a digital colony in 20 years' time? I don't know. We are today. That's where we are.
{{< /say >}}

The recording above goes much deeper than these three answers do. It gets into whether an EU region or a European subsidiary of a US provider actually gets you out from under the US CLOUD Act, and who holds the encryption keys when a subpoena arrives. It also covers Kubernetes as a portability layer versus needing a marketplace of specialised European providers, and whether Europe could fund a cloud of its own with public money, the way it once built Airbus. Worth the hour if any of that is live for you.

If you want to hear about more sessions like this one, they all go up on the [events page](https://www.pulumi.com/events/).
