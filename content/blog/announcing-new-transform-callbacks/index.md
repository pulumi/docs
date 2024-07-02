---
title: "Announcing new transform callbacks"
date: 2024-05-15
meta_desc: Transform callbacks are a rebuild of the transformations system to work for Multi-Language Components
meta_image: meta.png
authors:
    - fraser-waters
tags:
    - features
---

Pulumi has supported a [transformations](/docs/concepts/resources#transformations) system for a number of years now. This has proved to be a powerful and flexible escape hatch for editing resource properties across your entire program. 

However it was written before the advent of Multi-Language Components (MLCs) and functioned entirely on in-memory data structures, a sensible choice at the time but impossible to extend to work with the cross process nature of MLCs.

We've now written a new system based on a new "callback" system which allows the Pulumi engine to call back into your user program to answer requests.

<!--more-->

This new system is intended to fully replace the old transformations system. We've written up some guides on the differences between the two systems in the new [docs](/docs/concepts/options/transforms/#transforms-vs-transformations).

We'll continue supporting the current transformations system going forward, but given the expected growth in MLCs and the soon to be released Programs as Components feature users will want to prefer using the new system. Only the new system will work correctly with resources created in MLCs and Programs as Components.

