---
preview_image:
hero:
  image: /icons/containers.svg
  title: "Best Practices:  Code Placement and Stacks"
title: "Best Practices:  Code Placement and Stacks"
meta_desc: |
    The first in a series of videos, we'll use a fictional company named Zephyr to explore common questions that users ask when working with Pulumi.
url_slug: best-practices-code-placement-stacks
featured: false
pre_recorded: true
pulumi_tv: false
unlisted: false
gated: false
type: webinars
external: false
no_getting_started: true
block_external_search_index: false
main:
  title: "Best Practices:  Code Placement and Stacks"
  description: |
    The first in a series of videos, we'll use a fictional company named Zephyr to explore common questions that users ask when working with Pulumi. Zephyr wants to increase development velocity and flexibly scale different aspects of its online store. The demo will show deploying Zephyr's application, their online store.
     ► Read the related blog article: https://www.pulumi.com/blog/iac-recommended-practices-code-organization-and-stacks/
     ✅Get Started with Pulumi: https://pulumip.us/Get-Started
     ✅ Create a Pulumi account. It's free: https://pulumip.us/Sign-Up-OpenSource
  sortable_date: 2023-02-22T17:00:38Z
  youtube_url: https://www.youtube.com/embed/rDs_Dzl36vw
transcript: |
    Welcome to another episode of Modern Infrastructure Wednesday. We are gonna dive into a fictional company called Zephyr. Zephyr is gonna serve as a reference architecture uh for the best practices of how to do infrastructures code and how to use Polu to explore common questions that users ask us selling our K OCH and its facsimile has been extremely profitable for Zephyr. Um They're in fact on their second generation of their online store, their first generation was a monolith that was deployed manually. Um But as Zephyr prepares for its next phase of growth, Zephyr evaluated a number of different architectures intended to help them scale their online presence. In the end, they settled on a containerized architecture deployed to Kubernetes because some of the existing team was already familiar with those technologies as part of the switch to containerized micro services. They're also using Pulumi. Uh Zephyr's team knew that adopting infrastructure's code would help them with repeatable deployments and being able to use a programming language they already knew was appealing to them as well. For this video. I'm gonna show you the Zephyr Online store and how to deploy it. Here is the code for the Zephyr online store, it's all stored in a get repot. There are a few different options for code placement and in the blog post upon which this video is based, we discuss some of these options. Um We also discuss what are the advantages and disadvantages of each option. In the case of Zephyr, they've decided to go with what we call a mono repo, meaning they're storing their application code and associated Pulumi code in the same repository. Let's take a quick look at the Pulumi program. So while this program may look long and complex, even standard Kubernetes gamble is nearly 1000 lines long. Switching to Pulumi didn't actually add a great deal of complexity and gave them a lot of benefits over standard gamble. So let's deploy the Zephyr online store and see what it looks like. OK? We're gonna clone the Rio. OK? OK. Let's go into the distribution and the Pulumi folder specifically. OK. So there is a Pulumi folder in here. Um And we're gonna do Pulumi stack and knit and call it dove. Mhm. Run into them. Install real quick to get everything up. Girl. Let's run fund. OK, great then um let's Plumy config set, set the AWS region to us was two and with that, we should be able to issue a pulling it up. Let's take a look here. OK? Um Here's take a look at the preview here. So Eks cluster, a bunch of the internals of ECs IM roles, these uh security group rules of E PC with a bunch of different route tables. Um You know, uh then uh using the provider name, space service counts, config maps deployments um and all that. So 100 and seven resources to create, we're gonna hit yes, to perform this update and let it rotten and we'll be right back. OK. Pulumi up has finished. Uh so I exported the coup config and the VPC ID. Um OK. We're gonna retrieve the um DNS of the load balancer. Now, let's see. Uh So we're gonna just dump out this output to a file called Cobe config. And then let's see, see if that works excellent. So here is the load balancer and then let's see if this works. All right, the Zephyr Archeo Tech Emporium um and you know, selling a lot of great things um fine arcane artifacts. Uh So here is the website um and you know, there's shopping cart and catalog and home and all that. So there you have it, the Archeo Tech Emporium Online Store. Even though I've only deployed a single stack here in this video, Zephyr will be using multiple stacks, each stack corresponds to a different environment like development or production. This easily enables Zephyr's team to spin up multiple independent environments from the same Pulumi program. This is something we discuss in more detail in the associated blog post. That is it for today's modern infrastructure Wednesday. See y'all next time.

---
