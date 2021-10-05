---
title: "Reflections of a Pulumi Intern"
meta_image: meta.png
authors: ["albert-zhong"]
meta_desc: "A reflection on my Pulumi intern experiences (summer 2020 edition)"
tags: ["pulumi-interns"]
date: "2020-09-18"
---

Hi everyone! I'm Albert, a soon-to-be sophomore studying computer science at the University of Washington. Today marks my last day as a Pulumi intern, so I figure I'd reflect on my experiences up until this point.

## Joining Pulumi

I heard of Pulumi for the first time when they visited my school's career fair in January. As I rounded the corner into the [CSE1 atrium](https://www.cs.washington.edu/building), I saw a banner titled "Modern Infrastructure as Code," with some lines of TypeScript of what appeared to be the creation of an S3 bucket. I found it interesting because it looked so simple and modular. In contrast, when I had played around with AWS in the past to deploy the occasional Django web app, it had always involved following a series of exact instructions (usually go to this dashboard, copy this YAML file, run this command, and pray it works).

I walked up to the banner's adjacent booth and chatted with [Sean](/blog/author/sean-holung/), a software engineer at Pulumi. He explained how Pulumi was building an open-source platform that allows developers to manage cloud infrastructure using familiar programming languages. To be honest, I didn't have too much experience with the cloud, but I did sympathize with the pain of wrangling with YAML files. The concept sounded compelling, so I told him I was interested in interning there. He gave me the Pulumi recruiter's email, who I later emailed that day with my resume and a brief bit about my background. After a few email and phone exchanges, I came over to the Pulumi office for an in-person interview (which was unfortunately also the only time I ever saw it, due to [COVID-19]({{< relref "/blog/coronavirus-plan" >}})).

A couple of weeks later the recruiter called me and extended an offer for the summer intern role! I was incredibly excited about the opportunity to work at such an interesting startup, and especially one working with the cloud, an industry that seemingly dominates my hometown of Seattle. I accepted it a few weeks later since I believed Pulumi had the most fascinating technical challenges to work on relative to the other companies I applied to. From then until summer, I was nervous that my position would be canceled since the coronavirus was forcing many companies to reconsider their budgets. Thankfully Pulumi confirmed that it would shift to a virtual setting, and I started in late June.

## The First Week

I had very little idea of what the internship would look like. In addition to it being virtual, it was my first software engineering gig, so I had no prior experience to base it off. I wasn't sure what my role would be—would I just be assigned a single project and be told to work on it? Would I have a mentor? How does the process of submitting code look like? Fortunately, these questions were answered fairly quickly.

For the first week, the other interns and I converted Pulumi [examples](https://github.com/pulumi/examples/) from one language to another. TypeScript seemed to be the most common language, so I converted a few from that language to some of the relatively less popular languages, such as Python and Go. I thought that this was an excellent way to help us interns ramp up since it allowed us to get some baseline experience with Pulumi and the various cloud providers and programming languages it supports. By Friday, I was pretty familiar with how to navigate the various Pulumi repositories and documentation, which was a huge benefit as I launched into my project.

## My Project: `crd2pulumi`

On the following Monday, I joined a Zoom meeting with [Levi](/blog/author/levi-blackstone/) and my mentor [Justin](/blog/author/justin-vanpatten/). They had written up a preliminary design doc on generating SDK types for Kubernetes CustomResources, which would be my project for the summer. I had a minimal background with Kubernetes, so I couldn't fully conceptualize what the end product would look like until a few days later.

You can define custom fields of a Kubernetes CustomResource using [CustomResourceDefinitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) (CRDs). Pulumi already allows you to create CustomResources using the [apiextensions]({{< relref "/registry/packages/kubernetes/api-docs/apiextensions" >}}) package. However, there's no way to inherently know the exact fields of a CustomResource, since it's set by some CRD. Therefore we have to set the CustomResource fields to some generic type, such as `map[string]interface{}` in Go or `pulumi.Input<any>` in TypeScript. This makes filling out the fields for complex CRDs such as cert-manager or Istio very cumbersome since they contain thousands of nested properties. Being able to leverage IDE type-checking and auto-complete makes the process much quicker and less error-prone.

Throughout the summer, I progressively built [`crd2pulumi`](https://github.com/pulumi/crd2pulumi), a CLI tool that generates a typed CustomResource from a CRD. I then leveraged this tool to generate libraries for various Kubernetes Operators, which you can find [here](https://github.com/pulumi/pulumi-kubernetes-crds/). I still feel like there are additional features to build out in this area though, so I plan to submit a PR here and there even after today.

## School vs. Work

Before joining Pulumi, all my programming experiences had come from either school projects or practicing coding challenge type problems. So far, these scenarios have been fairly [atomic](https://wiki.osdev.org/Atomic_operation), in the sense that they are self-contained and started and finished in a relatively discrete chunk of time. A typical coding project at school is straightforward—I sit down, read the instructions, code everything, and don't think about it until my grade comes back. Most problems (not relating to the difficulty of the course content itself) can usually be resolved by looking more closely at the instructions or consulting the Piazza board.

In contrast, real software development at Pulumi was far more multi-person, rich, and dynamic. It was challenging, but also far more rewarding. In the first couple of weeks, I was seemingly running into issues at all layers—with the `pulumi/pulumi` codegen, with the Go compiler, with the Pulumi CLI, with the Python SDKs, or with my Macbook overheating and crashing whenever I tried opening up the `examples` repository in VSCode. Getting stuff to "just work" often required fixing many nested sub-problems until the root problem could finally be resolved. After a while, I internalized a lot of general debugging heuristics, and developed better skills in squashing bugs and getting code to "just work."

I thought that Pulumi gave me an excellent balance between guidance and autonomy. My co-workers gave me an outline of what my project should achieve, and some pointers on how which tools to use, but other than that it was up to me to implement it.

One aspect that I liked about Pulumi was that its main audience is, of course, developers, so it was easier to design `crd2pulumi` since I am a developer. Being able to directly interact with other programmers that use my tool and hear their feedback was immensely satisfying. I loved the energy that came from working with a fast-growing startup that provided real value to real people. It was exciting to come to Monday's team meeting and see Pulumi's user count continuously rise, and hear about the latest deal that the sales team had just closed.

## Pros of the Virtual Life

I hugely appreciated the flexibility of virtual work-from-home. In conjunction with the two summer classes I was taking, this allowed me to occasionally optimize my schedule. For example, if I had stayed up late on Tuesday night submitting a problem set and I knew I had no meetings tomorrow, I could wake up later on Wednesday morning, but just work a few more hours in the evening to compensate. However, I tried my best to avoid this to keep in sync with the majority of Pulumi employees that are on from 9 am to 5   pm PST.

After a few days, I settled into a routine of:

- Wake up around 9-10 am and drink some water
- Fire up my Macbook, check Slack and emails, attend meetings if scheduled, read through the reviews to my PR, and write some code
- Eat brunch around 1-2 pm (almost always a double-wrapped Chipotle burrito with brown rice and chicken)
- Write some more code, fix some bugs, push some changes until 5-6 pm

I feel that the quality of the technical practice I received would have been the same, had the internship been in-person. I usually knew which feature or fix to accomplish, and could troubleshoot most technical errors along the way. If I did run into a bug with my code or had questions on how to implement some function, I could always message a co-worker or set up a meeting to resolve it pretty quickly. I also picked up on a lot of knowledge regarding Pulumi, our tech stack, and best practices by just listening in on meetings and browsing the company Slack channel.

## Cons of the Virtual Life

For me, the largest drawback to work-from-home was diminished social opportunities. Everybody I met at Pulumi was so interesting, talented, and kind, so I'm disappointed that I couldn't meet them in person. There's no online replacement for actually seeing a person for 8 hours a day and 5 days a week. I feel that so much of life is disproportionately formed via one-off, chance encounters with people, so not being able to go down to a city such as Seattle and work in an office limited my [exposure to the envelope of serendipity](https://nevalalee.wordpress.com/2011/10/16/nassim-nicholas-taleb-on-maximizing-serendipity/). Looking back, I should've set up more 1-1 meetings with people at Pulumi, just to chat with them and learn from their experiences over lunch.

Nevertheless, it was still enjoyable, and Pulumi tried its hardest to keep us engaged with remote social activities. For example, [Lee](/blog/author/lee-zen/) set up a couple of virtual escape room games which were entertaining.

## Wrapping Up

In my view, one of the best lessons I got was that now I know how much I don't know, which is far better than *not* knowing how much I don't know. I was exposed to many different areas of tech—Kubernetes, code generation, TypeScript, Go, infrastructure as code, AWS, GCP, and so much more. I've only begun to scratch the huge surface area of the cloud ecosystem, and I'll always be grateful to the awesome people at Pulumi who helped me get started.

In two weeks I'll start (also remote) fall quarter at college. If you want to chat, feel free to reach out to me via any of the links on my [website](https://albertzhong.com/). Thanks for reading!
