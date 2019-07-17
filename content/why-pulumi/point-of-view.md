---
title: Toward a Cloud Native Programming Model
description: Cloud innovation has delivered limitless capabilities that promise to transform all aspects of software development.
meta_desc: Pulumi provides a cloud native programming model for containers, Lambdas, and infrastructure, to get code to the cloud faster than ever before.
---

This radical democratization is thanks to containers, serverless (lambda) computing, and opinionated data and infrastructure services, leveling the playing field, lowering barriers to entry, and delivering the closest thing to an "operating system for the cloud" that we've ever seen.

>To a first approximation, all developers have become cloud developers.

However, cloud developers lack a consistent programming model to provide the productivity gains for application development harnessing these capabilities. Pulumi aims to provide that programming model.

<h3>Transforming to Cloud Native</h3>

The set of capabilities, and cloud native architecture, derived from containers, lambda, and data (CoLaDa) services are promising the delivery of new applications at high velocity, that are delivered on-demand at any scale and freed from the constraints of traditional data center infrastructure.

The leading Developers and DevOps teams will want tools, frameworks, and automation that is specific to this programming model, and works the way they want, to maximize their velocity for software delivery. "Infrastructure" requirements -- the set of services that apps are built upon -- are increasingly being decided by Developers and DevOps teams, who are making extensive use of automation to manage the available portfolio for their enterprises.

The programming models, however -- the lingua franca developers use to express themselves -- have not kept pace.  This is no surprise: we are still transitioning from past generations of cloud compute, which mainly entailed gluing together virtual machines with configuration files managed by operators, and not developers.  We have come a long way, and yet we are still very early on the journey towards our future cloud-oriented distributed programming nirvana.

<h4 >Beyond Lift and Shift</h4>

To put this transition into perspective, until just recently "getting code to the cloud" meant "lift and shift": taking aging n-tier web apps, dusting them off with minimal changes, and rehosting them in the public cloud.  This may yield significant cost savings, allowing organizations to reduce or retire their own data center expenditures, while also improving agility.  For many organizations, much of the promise behind containers is to increase the scope of this approach.

Because of the nature of lift and shift, however, the tools developers use to create and manage cloud software have progressed slowly.  One of the benefits of containers has been giving developers simpler tools and workflows to package up their code to deploy into the cloud.  But operating such programs at scale and in production -- and architecting these programs in a truly cloud native way -- is still the domain of cutting edge experts.  And containers, while a powerful abstraction, say nothing about serverless computing or opinionated cloud services.

<h3>A Programming Model for the Cloud</h3>

We now have an opportunity to reimagine what the next generation of cloud native software development will look like.  This software will leverage the increasingly sophisticated public cloud capabilities: AI, machine learning, large scale data storage and science, and reimagined SaaS product architectures.  Such software will not use the cloud as an afterthought.  The winners will be those who enable new, compelling experiences, at dramatically lower cost structures, by using the core capabilities of the cloud in fundamental and intrinsic ways.  The cloud will become an ever-present part of the application design, not an entirely separable layer, authored using a different suite of tools and techniques, managed by a distinct operations team operating at an arm's length.

<h4>Emerging CoLaDa Architectures</h4>

In developing for the cloud, the question is not one of traditional infrastructure versus containers versus serverless versus hosted services.  We believe in using the best tool for the job.  Serverless functions can infinitely and rapidly scale event-driven systems with a low cost and ease of programming, while containers are great for bringing stateful apps to the cloud and scaling them out using your favorite container scheduler.  The key is in getting all of these technologies to seamlessly interoperate with one another in harmony, using consistent programming models and management practices.

<h4>Code is the Best Config</h4>

As a case in point, consider configuration languages.  They are unfamiliar to most developers and lack the same rigor developers apply to application code (such as code reusability, unit tests, and linting and static analysis).  This almost always takes the form of JSON or YAML templating languages or, best case, special purpose DSLs that lack the full expressiveness of real languages.  There remains a cultural divide between developers and DevOps that is in large part created by the fragmentation in programming tools.  But it goes deeper than that.  Most of us still think of gluing together virtual machines when we hear the word "infrastructure."

Despite increasing the level of abstraction in cloud software, "infrastructure" will in fact rise in importance to developers, just as developers care deeply about their target operating system's process and thread scheduling, memory and disk storage, and management and UI capabilities.  It's easy to assume infrastructure goes away -- and indeed, for some programmers it will -- but a holistic approach must not try to hide its presence.

<h4>Finding a Lingua Franca for the Cloud</h4>

Newer cloud architectures are already resulting in a dramatic shift from coarse-grained cloud infrastructure -- virtual machines, for instance -- to a vast array of finer-grained CoLaDa resources -- containers, serverless functions, various data stores, security roles, and so on -- each of which is composed together to build larger systems out of smaller pieces.  Because of this explosion, the approach to configuration languages that prevails to this day -- one of developers asking operators to glue together virtual machines and databases -- simply will not scale.

The key missing piece to taming this complexity is having lovable abstractions that allow for abstraction, reuse, and componentization.

> Infrastructure must become programmable just like our code.

A true cloud programming platform will offer a clear path to finally realizing the DevOps vision that our industry has made so much progress towards in the past decade.   As with all software skills, practitioners will specialize in operational areas they know best and become industry influencers in their areas of expertise.  The tools, however, will allow them to share their best practices in a reusable form, the same way thought leaders in, for example, machine learning have shared frameworks they have built.  This allows us all to stand on the shoulders of giants, and to remove the hard divide between developers and operators that has discouraged collaboration, sharing of knowledge, and innovation.  A common lingua franca is within our grasp.

<h3>Spin up CoLaDa with Pulumi</h3>

It is the dawn of a new age for all aspects of the software development lifecycle: cloud programs at every developer's fingertips. We look forward to playing our part in what promises to be one of largest industry transformations in our lifetimes.
