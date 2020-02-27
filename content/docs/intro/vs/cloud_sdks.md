---
title: Pulumi vs. Cloud SDKs (AWS Boto, etc.)
meta_desc: This page gives an overview of the major differences between Pulumi and
           Cloud SDKs (AWS Boto, etc.).
linktitle: Cloud SDKs
menu:
  intro:
    parent: vs
    weight: 4

aliases: ["/docs/reference/vs/cloud_sdks/"]
---

The cloud providers offer SDKs in multiple languages, including AWS Boto (Python), and many unnamed libraries for
JavaScript, C#, Java, Go, and others. There are also many community-driven libraries that abstract over these
underlying libraries, either for cloud-specific or multi-cloud scenarios.

It's important to realize that these libraries are fundamentally different in their aim, compared to Pulumi. These
libraries give direct access to the cloud APIs and, though they can be used to provision resources, they leave it to
the programmer to do so reliably. Because these are imperative libraries, attempting to open code provisioning and
updates using them are error-prone (usually devolving into a [custom, homegrown provisioning system]({{< relref "custom" >}})).

Pulumi uses a true infrastructure-as-code to ensure robust management of resources. In particular, should an update
fail, your system is always in a well defined, recoverable state, compared to ad-hoc and manual recovery.

In fact, Pulumi internally uses such libraries when interfacing with the different cloud providers. It's all the
things on top -- the language runtime, the ability to diff updates, the concurrency management and robust checkpointing
of state -- that makes Pulumi different. If you wanted repeatable and robust deployments in a team environment, you'd
need to build all of this yourself on top of these cloud SDKs. And multi-cloud would require a considerable amount of
effort, and would be tantamount to building another Pulumi by hand.
