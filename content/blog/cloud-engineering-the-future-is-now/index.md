---
title: "Cloud Engineering: The Future Is Now"
date: 2021-04-29
meta_desc: "The PulumiUP event featured industry leaders discussing the current state
  of cloud engineering and its future impacts on DevOps."
meta_image: pulumiup_recap.png
authors:
  - sophia-parafina
tags:
  - cloud-engineering
search:
  keywords:
    - Cloud
    - Engineering
    - Infrastructure
    - Cloud Engineering
    - Software Engineering
    - DevOps
---

Thank you for joining the PulumiUP event. We had a stellar set of speakers and panelists discussing the future of DevOps and how Cloud Engineering is providing the tools and processes that enable faster delivery, the right mix of architecture, and foster collaboration among teams in an organization. Here are some of the highlights and takeaways from our speakers.

<!--more-->

## Putting Cloud Engineering in Practice

Our speakers all commented on how the cloud is speeding up development. Applications are dynamic, and your infrastructure should also be dynamic, according to Adrian Cockcroft, VP of Sustainability Architecture at Amazon. The future of infrastructure is a mixture of lightweight, scalable services combined with event-driven architecture. Furthermore, composing infrastructure should take advantage of well-architected frameworks such as those published by AWS and Liberty Mutual.

Underscoring this, Justin Fitzhugh, VP of Cloud Engineering at Snowflake, cited the need to disaggregate compute and storage to scale independently. Moreover, Snowflake needed to scale across three public clouds with self-managed infrastructure. In Snowflake's experience, scaling with manual processes was not a viable option. They codified actions by following the software engineering process of code commits, tests, CI processes, and a CD pipeline for execution.

Keith Redmond, VP of SaaS Engineering at Fernergo share a perspective from the financial services industry. He reiterated the need for a deployment framework that bridged dev and ops teams and an automated build and release process to maintain integrity and reliability. He noted that this required a change in culture from teams handing off tasks to each other without input from the other to a completely integrated team where all actions with infrastructure begin with a code commit. The culture shift to an engineering-managed process also changed hiring patterns from operators and system administrators with some coding skills to software engineers interested in infrastructure.

In the current cloud engineering landscape, we will continue to see movement towards heterogeneous architectures, an increase in the use of software engineering methodologies to deploy infrastructure, and more automation for building and deploying in the cloud. This segues into the future of cloud engineering with a focus on tooling, process, and teams.

## The Future of Cloud Engineering

The cloud engineering panel included Justin Fitzhugh, Dana Lawson, VP of Engineering at GitHub, Charity Majors, CTO at Honeycomb, and was moderated by Kat Cosgrove, Developer Advocate at JFrog. The session, titled "Your Peers," discussed the future of cloud engineering.

When planning for the future of modern cloud applications, the panel agreed that the industry would continue to iterate and evolve away from domain specific languages, DSLs, and towards software engineering practices for infrastructure. They also agreed that while **Go** would be the most popular language for Infrastructure as Code, Ruby and JavaScript will also continue to be key languages.

Cloud engineering personas will change as new technologies such as the Internet of Things, availability of 5G, orchestration, edge computing, and future network APIs roll out. Cloud engineers should continue to focus on containers and what goes into applications. Knowing the entire lifecycle of their application from development to production is a must for cloud engineers. It underlies the concept of a single persona that can use services to compose development and services. Ultimately, the job of the cloud engineer is to reduce complexity and reduce friction in the pipeline by using patterns as needed and building platforms and tools consistently.

The panel discussed the reality of testing in production. Charity Majors highlighted that you have no choice, whether you admit it or not; there will always be known unknowns because devs or operators cannot test everything. Software will always have bugs, but the problem can be managed by having more ways to separate problems and test them in a small and controlled way. Testing in production begins with observability, starting with usual tools such as `strace` and other enhanced toolsets to inspect your code. Also, feature flags and deployment models help find bugs and limit their impact when applications go into production.

Finally, the panel looked backward at the impact and legacy of devops. The panel agreed that devops brought both sides to the table. Operations learned about code and applications while developers learned about infrastructure. Practitioners are software engineers, but each with a different focus. Implementing infrastructure is similar to creating a new feature. However, there is a concern for losing deep systems knowledge, and software engineers are unlikely to have a deep understanding of networking, system administration, or storage. The solution is to train people cross-functionally, i.e., software engineers on systems and operators on coding and application. Teamwork is the key to breaking down operational and knowledge silos in an organization.

## Summary

Thank you for attending PulumiUP! Your response to the [Pulumi 3.0 release](/blog/pulumi-3-0/) was overwhelming. If you didn't have the chance to catch PulumiUP on launch day, you can watch the entire event.

{{< youtube "Zko70KVGcgo?rel=0" >}}
