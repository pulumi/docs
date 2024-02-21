---
title: "Pulumi ESC Enhanced Editor: Elevating the Authoring Experience"
allow_long_title: true
date: 2024-02-22T00:00:00-07:00
draft: false
meta_desc: "Enhanced Pulumi ESC Editor streamlines the authoring experience of environments for developers"
meta_image: "meta.png"
authors:
  - pat-gavlin
  - arun-loganathan
tags:
  - esc
  - secrets
---

With [Pulumi ESC](/product/esc), our goal is to not only create a tool that simplifies the development process but also one that developers love. Building on this goal, we're excited to unveil the new Enhanced Pulumi ESC Editor, a big leap forward designed to improve the authoring experience for developers everywhere. This upgrade is focused on addressing the common challenges encountered during coding such as syntax errors and the need for frequent documentation lookups. Our aim is to make the process of authoring environments straightforward and remove the common hurdles for a smoother workflow.

<!--more-->

## Highlights of the Enhanced Editor

- **Auto-complete**: This feature provides suggestions for code snippets and resource properties, eliminating the constant need to reference documentation. It's engineered to accelerate and refine the coding process, enabling developers to concentrate on innovation and problem-solving
- **Enhanced Diagnostics**: This goes beyond basic syntax checks by providing in-depth insights into potential errors, coupled with real-time fix recommendations. It serves as your personal coding assistant
- **Hover Documentation**: Simply hover over any piece of code to see a detailed tooltip with relevant insights and examples. This instant access to information reduces manual documentation lookups, streamlining the development process and minimizing disruptions

Tap 'Ctrl+Space' on the Editor reveal the list of functions and properties. 

{{< video title="Pulumi ESC Enhanced Editor Demo" src="./esc-enhanced-editor-demo.mp4" autoplay="true" loop="true" >}}

## Contextual Information to your environments

We also added support for getting rich contextual information such as current user, organization, environment name to the environments. You can use it to enrich audit logs, refine OIDC subject for granualar access and more! You can use the `context` attribute along with the following options to get contextual information:

* `context.rootEnvironment.name`: the name of the root environment being evaluated
* `context.currentEnvironment.name`: the name of the current environment being evaluated
* `context.user.login`: the user login identifier
* `context.organization.login`: the organization login identifier

```yaml
values:
  rootEnv: ${context.rootEnvironment.name}
  currentUser: ${context.user.login}
```

## A Seamless Authoring Experience Awaits

The updated editor experience is designed to minimize friction, boost productivity, and transform cloud development into a more enjoyable and effective journey. We are eager for you to explore these new features and see firsthand how they enhance your development process.

Discover more about the capabilities of Pulumi ESC and how it can support your projects by checking out our [documentation](/docs/esc).
