---
title: Cloud SDKs (AWS Boto, etc)
---

The cloud providers offer SDKs in multiple languages. This includes AWS Boto (Python), in addition to a multitude
of SDKs -- usually without specific names -- across languages like JavaScript, Java, Go, etc. There are also many
community-driven libraries that attempt to abstract over these underlying libraries.

An important thing to realize is that these are fundamentally different in their aim. These libraries give direct
access to the cloud APIs and, though they can be used to provision resources, it is done in an ad-hoc and imperative
way, rather than an infrastructure-as-code approach like Pulumi that robustly manages the resources. In particular,
should a sequence of these API calls fail, it is usually a manual effort to recover.

In fact, Pulumi internally uses such libraries when interfacing with the different cloud providers. It's all the
things on top -- the language runtime, the ability to diff updates, the robust tracking of state -- that makes
Pulumi different. If you wanted repeatable and robust deployments in a team environment, you'd need to build all
of this yourself on top of these cloud SDKs. And multi-cloud would require a considerable amount of effort,
and would be tantamount to building another Pulumi by hand.
