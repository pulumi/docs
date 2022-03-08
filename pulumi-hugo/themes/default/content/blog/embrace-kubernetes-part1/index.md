---
title: "It’s Time to Embrace Kubernetes! Really? (Part 1)"
date: 2020-12-09
meta_desc: "How to evaluate your choices when choosing Kubernetes as your application platform"
meta_image: embrace-k8s.png
authors:
    - lee-briggs
tags:
    - kubernetes

---

When you’re considering whether or not to implement Kubernetes, perhaps the first question to ask yourself is do you need it at all?

The point of any technology isn’t the technology itself. When done right, Kubernetes can reduce the barrier of entry for application developers so they can get features from their machines to your customers as quickly and easily as possible. But do you already have a solution that works well? If you do, why do you want to change it? Making such a radical change in your technology is potentially quite dangerous so what’s your motivation?

It very well might be that sticking with and improving the solution you already have offers a better cost/benefit tradeoff. It's easy to fall into the trap of believing that simply adopting a new technology like Kubernetes will instantly solve your hard organizational or technical problems, however, we know that is seldom true.

In this blog post we’ll share some tips and tricks for evaluating your own situation to see if Kubernetes is a good fit. We've learned these from helping hundreds of customers adopt Kubernetes &mdash; in addition to not, when there was a better solution available. We’ll see that the question isn’t that simple to answer and there are a lot of variables to consider. In the next blog post, we’ll talk about a situation where Kubernetes can be a good fit and how to start your first Kubernetes project.

Note that these blog posts assume you already have some familiarity with Kubernetes. If you are just starting to learn, [our Getting Started with Kubernetes blog series](https://www.pulumi.com/blog/getting-started-with-k8s-part1/) is a good place to start.

<!--more-->

## Why is Kubernetes So Popular?

[Kubernetes](https://kubernetes.io), an open-source system for deploying, scaling, and managing containerized applications, is currently the last step in an evolutionary chain that began with private data centers and, from there, went to cloud VMs, then to containers and then to container orchestrators. If you are looking to ship applications to the cloud continuously, containers are a great way to do that, and Kubernetes is the technology responsible for running them. Kubernetes was initially developed by Google and has since had an enormous community grow up around it well beyond its Google roots. Version 1.0 was released in 2015 and the latest version was released in October 2020.

Kubernetes has become increasingly possible over the last few years. In the ZDNet article, [“Kubernetes jumps in popularity”](https://www.zdnet.com/article/kubernetes-jumps-in-popularity/), published on March 6, 2020, Steven J. Vaughan-Nichols cites a [Cloud Native Computing Foundation](https://www.cncf.io/) (CNCF) survey about containers and Kubernetes. Of the companies that responded, 84% were using containers and, of those companies, 78% were using Kubernetes to manage them. The survey also found that there were over 109 tools to manage containers and 89% of them use various versions of Kubernetes.

There are several reasons why Kubernetes is so widely adopted. Here are some of them:

- **Extensibility**. While Kubernetes comes with a large set of existing resources such as Pods and Secrets, developers can also create their own with custom resource definitions (CRD). They can also write their own Operators, with which they can automate the management of CRDs.
- **Community support**. The Kubernetes community is large and there are many special interest groups. Also, Kubernetes is housed on a vendor-neutral platform run by the CNCF. The CNCF sponsors CloudNativeCon/KubeCon, which is one of the largest open-source events in the world.
- **Third-party vendor support**. There are also many third-party vendors that repackage Kubernetes. These are called Kubernetes distributions. They provide opinionated implementations of production-ready Kubernetes. Examples include [Openshift](https://www.openshift.com/), [Rancher](https://rancher.com/) and [VMWare Tanzu](https://tanzu.vmware.com/tanzu).
- **Frequent releases**. Kubernetes releases often, with a new significant release every three or four months. Each release adds many new features and innovations.

## Is Kubernetes the Right Choice for You?

Given its widespread popularity, its many features, and its community support, it seems that selecting Kubernetes is a given. “Everyone else is using it so our company should use it, too.” But is that the case? In the rest of this article, we’re going to propose some questions that you, your peers and management can use as a basis for discussion. These questions are meant to help your organization come to an informed choice about Kubernetes.

### Is Your Organization Ready for Kubernetes?

The first question to ask yourself is if your organization has the DNA required to support a broad-scale Kubernetes implementation. By “DNA,” we don’t mean only technical know-how. Bringing Kubernetes into an organization is a major effort that can affect many groups. For that effort to succeed, there must be good communication between those groups, trust, and a willingness to take on new challenges together. In particular, the relationship between the applications teams and the operations teams needs to be healthy. People must be willing to set aside rivalries and politics so they can collaborate with each other towards a common business goal.

As you can imagine, this can become a heated topic. If you’re interested in what others in the community are saying, here are a couple Tweets to get you started:

{{< tweet id="978758781805895681" user="whereistanya" >}}

{{< tweet id="1021012140675813376" user="0xfraq" >}}

Another way to look at this question is to ask yourself where your organization sits in terms of its adoption of DevOps. To quote the [2020 State of DevOps](https://puppet.com/resources/report/2020-state-of-devops-report/) report:

> *We still see that most organizations are struggling to expand DevOps beyond a few pockets of success. One reason DevOps often fails to expand further is that most enterprises are structured in ways that create misaligned incentives and lack of accountability or ownership over the outcomes they’re supposed to be driving.*

We have seen a greater likelihood of success within our own customers that have experience practicing "Cloud Engineering", "DevOps", "Site Reliability Engineering", and/or other more collaborative and engineering-oriented approaches to infrastructure. You might want to evaluate your own organization. A good guide is [DevOps Maturity Model](https://www.atlassian.com/solutions/devops/maturity-model).

### What Are Your Motivations?

We often make decisions for personally motivated reasons and that’s as true of technologies as it is of what car you buy. Kubernetes has a lot of appeal right now. It’s well publicized and companies with a lot of cloud engineering credibility, such as Netflix, use it. That alone might persuade some managers to make a top-down adoption decision, thinking that if it’s right for Netflix it must be right for their own companies. There are tutorials, YouTube videos and conferences that all say they’ll make it easy for you to adopt Kubernetes, and expertise in Kubernetes is a great way to build your resume. There is no question that success stories from leading edge companies and a fast-growing community are significant benefits &mdash; however, this alone is insufficient. As we’ll see, there’s no easy road to success with Kubernetes so, to make the right decision, you need to ask yourself some tough questions and evaluate more deeply whether it’s in the best interests of your company to use it.

### Do You Have the Resources?

The next question to ask is if your company has the engineering resources to support a Kubernetes initiative. Implementing Kubernetes is complex and takes a long time. Companies such as Netflix have very large operations departments but most other companies don’t. It is typically better to start by identifying an isolated project to prove out the expected benefits of Kubernetes before betting the entire farm on it. That said, don't underestimate how much effort even these smaller projects will take, especially when it comes to getting up to speed.

#### Do you have the people?

Kubernetes will demand a team of people who are dedicated to its implementation and support. The implementation itself is quite complex. The Kubernetes architecture is complex with many core concepts, including execution, security, and data models, distributed components to install and manage like etcd, and many additional layers on top. A robust implementation demands a deep understanding of that multi-layer architecture. This complexity is somewhat mitigated by the managed services many cloud providers now offer, but it’s still important to understand what’s going on.

Secondly, the actual interface required to deploy something with Kubernetes is also complex. It can be many thousands of lines of YAML, which often needs to be templated and manipulated with mechanisms that YAML was never designed to use. Take a look at [Why the **** are we templating YAML?](https://leebriggs.co.uk/blog/2019/02/07/why-are-we-templating-yaml.html) for a strong opinion by the author on this matter. Furthermore, as an infrastructure team, you are almost certainly going to want a better interface for your application developers to ship code without needing to learn the complex parts of Kubernetes including writing so much YAML. Eventually you will want to set up CI/CD to ship continuously.

Finally, when something goes wrong, you need a subject matter expert to fix it. Because Kubernetes gives you such a high degree of abstraction, it can be difficult to debug and most people will be unfamiliar with what’s going on under the hood. You need someone who’s really knowledgeable when there’s trouble. In fact, you probably need two people. You’re too vulnerable if that person leaves the company and you’re completely unreasonable if you can’t even let that person take a vacation. If you aren't yet practicing observability, you will quickly want to.

#### Can you afford the technical debt?

Because you’re dedicating several people to Kubernetes, you may be increasing your technical debt in other areas. Do you still have people available to handle bugs and other support issues? The costs here can be seriously mitigated by adopting a managed Kubernetes service from a major cloud vendor, but the opportunity cost is real either way.

#### Can you afford the migration costs?

As with any large migration, moving from your current system to Kubernetes needs to happen cautiously and gradually over time. You’re not simply going to destroy your existing infrastructure. Instead, you’ll probably want to adopt a side-by-side approach and slowly move your applications across. In other words, for quite a while, you’ll need to support two infrastructures rather than one. This can cost real dollars in addition to engineering time.

### What Are We Trying to Achieve, Again?

At the end of the day, it is worth taking a step back to ask ourselves, what were we trying to accomplish and did Kubernetes help us get there. Most likely the motivation for even asking this question included things like: we want to accelerate public cloud adoption (or adopt more public cloud-like technologies on-premises), we want to ship faster, and we want to empower our developers. It is true that, done well and done right, Kubernetes can achieve all of these things. But Kubernetes alone will not &mdash; it takes so much more than just that &mdash; and these can all very well be accomplished without Kubernetes, sometimes quicker and more cheaply.
Many companies, and startups in particular, have big dreams. They want an infrastructure, such as Kubernetes, that can scale infinitely to support their fast growing user base of their future. It is good to dream big and plan for the future, but it is also often better to start with a simpler solution today and evolve more incrementally over time.

For instance, maybe a simpler, native container orchestrator like Amazon's Elastic Container Service (ECS) will be easier to adopt and manage. Or perhaps a PaaS like Heroku, Google AppEngine, or Azure Service Fabric, that is more opinionated and less extensible, but far simpler to get up and running on, is a better, cheaper first step. If you have an event-driven architecture, then one of the many serverless compute technologies may be a better fit.

Architectures have to be shaped over time. It's never the case that was just create our infrastructure once and then we're done. Whatever infrastructure you adopt, you need to be able to change and adapt as your requirements change and evolve. In five years time, who knows what the world will look like? Betting the farm on Kubernetes too soon and too big could turn out to be an unwise decision in hindsight after you've spent many precious dollars deploying it.

## Learn More

This blog post talked about the many issues to consider before you dive headlong into a Kubernetes project. However, there are just as many reasons to choose Kubernetes for deploying your modern applications. Stay tuned for part 2 where we'll dive deeper into that topic. If you’re curious about just what a small project might look like (using your favorite programming language, whatever that is), check out Pulumi’s [Get Started with Kubernetes]({{< relref "/docs/get-started/kubernetes" >}}) and [Pulumi Crosswalk for Kubernetes]({{< relref "/docs/guides/crosswalk/kubernetes" >}}), playbooks with built in best practices that make Kubernetes accessible to everyone.
