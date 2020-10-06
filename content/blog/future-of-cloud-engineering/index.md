---
title: "The Future of Cloud Engineering"
date: 2020-10-07
meta_desc: "Cloud Engineering Summit keynote: Building the Cloud Operating System."
meta_image: meta.png
authors:
    - joe-duffy
tags:
    - cloud engineering
---

All modern software is cloud software. Modern applications interact with the cloud in some way, whether it's using cloud for storage, compute capabilities, or with cloud services that we no longer have to build. Some examples of this are cloud-native applications running on a distributed architecture, or a mobile or IoT application running on the edge, or a traditional n-tier application that uses cloud-based authentication.  It's safe to say that all developers today are cloud developers.

<!--more-->

The cloud changes the way we think about architecture, workflows, and teams. The Cloud Engineering Summit explores how we build architecture and how that impacts how we develop applications. Equally important is how we operate cloud architectures through workflows. What are the processes we need to build, deploy, and maintain infrastructure and applications? Finally, cloud engineering changes the way we work together and collaborate to deliver applications. A distributed infrastructure fosters breaking apart silos of application developers, security engineers, infrastructure engineers, and DevOps by forcing a holistic model for continuous delivery.

## Cloud Today

Today's cloud can be characterized as many cloud-service building blocks across a landscape of multiple cloud providers. This creates an unintentional complexity that leads to one-off solutions. If we were to reimagine cloud as a planet-scale supercomputer capable of globally delivering services, storage, and applications globally, what would be the operating system?

Some have suggested that Kubernetes is the operating system for the cloud. It's a combination of a kernel and scheduler but not much more. Operating systems are much larger than just a place to run an application. They provide a window into everything you do, such as the user experience, the developer experience, and the ways the tools we use are shaped.

What's the user interface to the world's largest supercomputer supposed to look like? What's the human experience of using that computer? We've extended our previous experience from desktop and Internet applications into the cloud, but it's just the start of how we interact with the cloud. For now, YAML is the current programming interface, but we're looking for the parts that we love about programming models from all the other operating systems. In the future, we'll have similar things for the cloud supercomputer.

The operating systems determine the application model - how do I install, version, secure, work with, and remove applications. Containers provide a building block for building and deploying applications in the cloud. Helm and CNAB provide an installation model, but it is a far cry from an IOS App Store experience or installing Windows or macOS applications. Without an operating system or an application model, the cloud supercomputer interface is at a very low level. Application models are top-down, unlike the current bottom-up model of configuring a cloud application.

This leads us to the inescapable fact that the cloud has broken the existing application model and broken how we approach architectures, workflows, and teams. When the cloud came along, we reused the application patterns we used on Internet 1.0, but the model shifted again with cloud services. We took the 1.0 patterns and automated them to hide behind APIs and microservices, and it's the current state of the cloud universe.

The cloud was incrementally breaking things over the past ten years, and we had to build tools and automation in real-time to respond. The result was DevOps. DevOps changed the way we worked together, the way we managed things, and the architectures we supported. It started from a place of collaboration, bringing engineers and operations people closer together.

We're still in the early days, and this is where cloud engineering enters the picture. Instead of fixing broken patterns, we need to build systems designed for the cloud instead of just coping with the previous model's transition to the one we have now.

Cloud engineering is taking the lessons learned from DevOps and making sure that application developers leverage the cloud in a first-class way by infusing the cloud into application development, especially with modern architectures and services.

We want to apply software engineering practices to infrastructure. As infrastructure becomes software, it becomes more programmable; and we can apply practices like testing, refactoring, security, continuous delivery, agile – all the things from application development that enabled us to ship software quickly and with confidence.

Finally, we want to unlock collaboration and let everyone bring their skill sets to the table to enable moving faster and deliver amazing software capabilities. The entire organization becomes a cloud engineering organization, including app-dev, devops, infrastructure, and security engineering.

## Architectures

Infrastructure used to be a tax and a cost center, but now infrastructure is a competitive advantage that can transform entire business models. For example, Zoom experienced a 10 to 20x increase in usage when COVID started. Because they architected their application for the cloud, they were able to scale and meet demand. Five to ten years ago, that wouldn't have been possible. Remember the Twitter fail whale?

Zoom massively scaling is a great example of the difference between using disruptive cloud technology like EC2 and fully embracing the technology stack and using it as a foundational piece of the application's design. The ability to scale up elastically is an immense competitive advantage when designing applications to run on a planet-scale computer.

The cloud is a superpower that gives capabilities to build innovative new experiences. These building blocks are readily available. And if we can figure out how to harness them, we can accomplish great outcomes and reshape how applications work.

In the 2010s, you had XML web services and SOA, which was the precursor to YAML, and now with modern programming languages, the shift to distributed architectures is a lot easier. We've taken async programming and implemented it in a first class way to build distributed systems. Systems are provisioning at a much faster rate but also in real-time response to demand.

## Workflows

How do we build, secure, test, deploy, and manage distributed architectures? Workflows are how we operationalize continuous delivery of cloud applications.

Infrastructure as code is focused on the artifact through the text or code. We have yet to apply all the engineering practices that are available to developers when building infrastructure. We've built infrastructure by copying and pasting text in a declarative model, but we can treat infrastructure as software when we bring software engineering techniques.  With infrastructure as code, we have real patterns and best practices.

Software provides a real sharing and package reuse model and lets you develop new infrastructure as productively as we can develop applications. We can test infrastructure using all the tried and true methodologies from software development. And we can secure infrastructure using best practices. Infrastructure is programmable, and we need to treat it like one during the development and run-time lifecycle and across its entire life.

Among the many things the cloud broke is the inner loop dev cycle. Developers don't have the tools for infrastructure development, like an IDE for applications. Infrastructure testing is also broken. Unit testing and integration testing are not currently part of the infrastructure programming model. However, these industry-standard practices can be applied to the cloud with infrastructure with code. We can write tests that occur before infrastructure is deployed or even spin up ephemeral environments to run a battery of tests. This also enables advanced forms of testing, such as chaos testing, where applications are tested during a service outage, or fuzz testing, where the environment is randomized to see how the application performs. Treating infrastructure as software allows you to do all of this, and it's game-changing.

Security is a key component but often overlooked part of cloud infrastructure. Infrastructure built on a cloud infrastructure provider does offer a level of protection, but infrastructure should be validated through scanning software components and applying policies that prevent unintended ingress or egress. For example, we want to make sure that ports are not unintentionally open to the Internet or that you have exposed unprotected S3 buckets. One security model is the principle of least privilege, where resources only have the minimum amount of privilege to complete a task. In the cloud, the security perimeter and attack surface for both applications and infrastructure are much larger. Policies that enforce the principle of least privilege across that perimeter limit the blast zone of incidents and are key to moving quickly and with confidence in the cloud engineering world.

Once you've shipped an application to production is when the game really starts. Infrastructure operators need to monitor and react to what's going on through an OODA (Observe, Orient, Decide, Act) loop. The OODA loop is a decision making framework that allows for rapid decision making with the context of a situation. It's a good analogy on how we maintain our cloud applications in the real world. How do we know something is wrong? How do we react? The old model of having simple performance counters, e.g., CPU or memory utilization, doesn't help detect anomalies and react to them in modern cloud architectures. The big change is collecting all the data into an observability system that gives you the capacity to orient yourself and quickly make decisions when things go wrong.

Continuous delivery is not a new idea. However, the cloud extends that model to continuous integration, where infrastructure undergoes acceptance testing before application delivery. Continuous delivery lets application and infrastructure teams work closer together, which is how teams go from shipping quarterly, to monthly, to every week, to daily, shipping features on every git commit.  Delivery and workflow are related, and our current way of delivering applications and infrastructure will change with cloud engineering.

## Teams

Teams are trying to centralize on cloud-agnostic workflows that work for the organization. It's about taking application developers, infrastructure teams, and devops teams and having them work together to produce more than they can individually. Let application developers focus on what they're great at – delivering functionality to end-users. And let the infrastructure and DevOps teams engineer scalable. reliable, and cost-effective foundations that the organization runs on. But don't forget security engineers who make security a first-class concern and not an afterthought. Make them a core part of the cloud engineering team.

Teams reflect the infrastructure they build and support. Distributed infrastructure can lead to distributed teams. Cloud infrastructure and applications are global, and the teams must reflect this distributed reality. As we have seen recently,  the ability to quickly transition to an all-remote team is an advantage.

## Future

So what does the future of cloud engineering look like? We see an infusion of cloud in application development. The cloud won't just be a place to run an application. It will inform how we interface with applications and the services behind them. This transformation is possible because we will apply software engineering practices to infrastructure. Testing, refactoring, the use of software tools will change how to build and deliver applications and infrastructure. Ultimately, these advances will unlock team collaboration and increase velocity when delivering applications.

As cloud engineers, we are building the operating system for the cloud. We've already made great progress over the past five years by creating the foundational pieces that make up the world's biggest supercomputer operating system. All of us are playing a part in building a programming model based on intents instead of low-level configuration. That programming model will infuse the application model with cloud principles to the point that cloud applications are readily packaged and transparently installed by users.

The big vision of cloud engineering is to deliver cloud-native, secure, and up-to-date applications on stable and adaptive infrastructure on any cloud. We invite you to join us, our partners, and speakers to build the future of the cloud.

Cloud engineering about the operating system for the cloud, the programming model, and the application model coming into fruition. It's about going beyond building blocks to structured solutions and lovable programming models.
