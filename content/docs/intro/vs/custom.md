---
title: Pulumi vs. Custom Solutions
meta_desc: This page gives an overiew of the major differences between Pulumi
           and custom infrastructure as code solutions.
linktitle: Custom Solutions
menu:
  intro:
    parent: vs
    weight: 8

aliases: ["/docs/reference/vs/custom/"]
---

Many organizations start out by manually managing their infrastructure. This often begins by pointing and clicking in
your cloud's web console, and then evolve by encoding provisioning and logic in simple scripts (Bash, Python, etc).

This approach works in the early days, but this home-grown solution begins to break down over time

* Provisioning multiple copies of an app is difficult (or impossible)
* The logic in scripts grow non-linearly with respect to your infrastructure's complexity
* Failure modes require manual intervention to repair environments, often leading to downtime
* As cloud providers evolve, it becomes hard to keep up and adopt the latest innovations

The maintenance cost of solutions like this often grows to consume multiple team members; it, in fact, usually ties
up your best and brightest engineers. Many teams find that they spend more time managing their home-grown
infrastructure scripts than they do writing business logic, and still can't move as fast as they want to.

Pulumi was designed to address these problems out of the box. It gives a real programming model, with familiar
languages, for expressing your cloud infrastructure and application needs. By expressing them using Pulumi, you
get a robust and repeatable deployment model, that works in a team environment. Pulumi was also designed to
make provisioning multiple copies of your infrastructure of application trivial, whether this is to bring up
new regions for your existing system, new environments (staging, prod, and test), or to ease testing.

Finally, Pulumi is [open source](https://github.com/pulumi/pulumi) and community-driven. So, to the extent that there
are custom needs, it is possible to make those customizations required, just like it would be with home-grown solutions.
For most customers, Pulumi replaces their custom solutions without any customizations necessary, but knowing that this
is an option should help know that Pulumi will be available in the long-term, and can evolve to meet your growing needs.
