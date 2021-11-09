---
title: "Kubecon NA 2021 Roundup"

date: 2021-11-08T22:50:38Z

draft: false

meta_desc: Kat Cosgrove's recording roundup of the trends, updates, and gems from Kubecon NA 2021!

meta_image: meta.jpg

authors:
    - kat-cosgrove

tags:
    - kubecon
    - kubernetes
    - conferences
---

KubeCon North America 2021 is over, but the recordings are now online! Every talk you wanted to attend and couldn’t is available on YouTube, so here’s some highlights&mdash;cloud native trends, updates from projects and SIGs, and a few of my favorite talks!

<!--more-->

#### SBOM is Coming: Why You Should Care and How You Can Help - Frederick Kautz & Allan Friedman

{{< youtube "4wUejdZ6KHM?rel=0" >}}

A major trend throughout the conference was supply chain security and software bill of materials (SBOMs). There were quite a few talks on these subjects, but Frederick Kautz and Allan Friedman give a great overview of exactly what an SBOM is, and why it’s important.

#### Notary: State of the Container Supply Chain - Justin Cormack, Docker & Steve Lasker, Microsoft

{{< youtube "hpcQJ21mn_g?rel=0" >}}

On supply chain security, Steve Lasker presents updates to Notary v2. It’s changed quite a bit since v1 and there are more changes on the horizon. With the rising concerns surrounding supply chain security, I expect Notary and tools like it to be increasingly important. No worries if you aren’t already familiar with Notary&mdash;Steve explains it well.

#### A Vulnerable Tale About Burnout - Julia Simon, CloudOps

{{< youtube "lpiXbfOTNYw?rel=0" >}}

Taking things to a more human place, burnout was a common theme this year. It’s something that we don’t talk about as much as we should, but close to two years of isolation is forcing us all to confront it in ways we may not have expected. This talk by Julia Simon is important to watch not just so that you can learn to recognize these problems in yourself, but so that you can recognize them in your peers.

#### PodSecurityPolicy Replacement: Past, Present, and Future - Tabitha Sable & Tim Allclair

{{< youtube "HsRRmlTJpls?rel=0" >}}

PodSecurityPolicy (PSP) has been deprecated. Many of you may be relying on this, and deprecations frequently sound scary, but Tabitha Sable and Tim Allclair are here to soothe your fears. They go to great lengths explaining what PSP is, why it was deprecated, what exactly this means for people relying on it, and where we’re going next.

#### SIG Contributor Experience Deep Dive - Alison Dowdney, Weaveworks & Christoph Blecker, Red Hat

{{< youtube "QOiyWWFjG5Q?rel=0" >}}

An open source project lives or dies by its contributors, both technical and non-technical. Kubernetes is huge and requires a lot of contributors to keep it growing, so we have SIG Contributor Experience to make sure they stay happy and the community stays healthy. Alison Dowdney and Christoph Blecker go into just how SIG Contributor Experience operates, plus updates. If you’re in a leadership position for an open source project, there are some lessons to be learned from this talk.

#### Kubernetes Exposed! Seven of Nine Hidden Secrets That Will Give You... Ian Coldwater & Brad Geesaman

{{< youtube "JBbVTmrZ45E?rel=0" >}}

No Kubecon is complete without Ian Coldwater, this time joined by Brad Geesaman (and, briefly, a second Ian Coldwater) to go into some not-so-obvious but oh-so-important pitfalls and hidden security concerns within Kubernetes. Even if you caught this talk live, it’s worth watching again to make sure you’re secured against these issues, or you might find a goose haunting your cluster.

#### Beyond Kubernetes Security - Ellen Körbes, Tilt & Tabitha Sable, Datadog

{{< youtube "-4W3ChRVeLI?rel=0" >}}

Finally, it would be remiss of me to not mention Ellen and Tabitha’s cinematic contribution to this year’s Kubecon North America. Beyond Kubernetes Security is the spiritual successor to their talk from the last Kubecon Europe, once again going into how some security concepts and exploits work in Kubernetes, but presented as a short film involving crime, time travel, breakups, and Ellen’s collection of old electronics.

The quality of the content was incredible across the board this year, whether the speakers were live or presenting virtually, forcing some difficult decisions around selecting my schedule for talks to attend and how many I could feasibly put in this blog before it got way too long. Fortunately, all of them are on the [CNCF YouTube channel](https://www.youtube.com/c/cloudnativefdn/videos) now, including talks from the various co-located events. Dig through!

Kubecon North America was simultaneously a strange and familiar event. It’s been nearly two years since most of us have been at a conference, and while that certainly made things awkward at times while we all readjusted to seeing other humans in the flesh, our slow return to something vaguely familiar seems to have been a success. I sincerely hope to see you all in person at the next Kubecon EU in Valencia.

Honk <3,

Kat
