---
title: "Introducing the Latest ESC Editor Enhancements for Improved Authoring"
allow_long_title: true
date: 2024-02-22T00:00:00-07:00
draft: false
meta_desc: "The new enhancements to Pulumi ESC Editor streamlines the authoring experience of environments for developers"
meta_image: "meta.png"
authors:
  - pat-gavlin
  - arun-loganathan
tags:
  - esc
  - secrets
---

With [Pulumi ESC](/product/esc), our goal is to not only create a tool that simplifies the development process but also one that developers love. In pursuit of this goal, we're excited to announce enhancements to the Pulumi ESC environment editor. These enhancements are focused on addressing common challenges encountered when authoring environments: syntax errors, type errors, frequent context switches to and from documentation, and more. Our aim is to make the process of authoring environments as straightforward as possible by removing common hurdles.

<!--more-->

## Highlights

- **Auto-complete**: This feature provides suggestions for code snippets and resource properties, easing the need to reference documentation. It is engineered to accelerate and refine the coding process, enabling developers to concentrate on innovation and problem-solving.
- **Enhanced Diagnostics**: These diagnostics go beyond basic syntax checks by providing in-depth, as-you-type insights into errors.
- **Hover Documentation**: Hover over any piece of code to see a detailed tooltip with relevant documentation and examples. This instant access to information reduces the need to context switch, streamlining the development process and minimizing disruptions.

Tap 'Ctrl+Space' in the editor reveal the list of functions and properties. 

{{< video title="Pulumi ESC editor enhancements demo" src="./esc-editor-enhancements-demo.mp4" autoplay="true" loop="true" >}}

## Contextual Information to your environments

We have also added support for accessing contextual information from within an ESC environment such as the current user, organization, and environment name. You can use this information to enrich audit logs, refine OIDC claims for more granular access, and more! This information is available by accessing the `context` property, and contains the following information:

* `context.rootEnvironment.name`: the name of the root environment being evaluated
* `context.currentEnvironment.name`: the name of the current environment being evaluated
* `context.user.login`: the login of the user evaluating the environment
* `context.organization.login`: the name of the user's organization

```yaml
values:
  rootEnv: ${context.rootEnvironment.name}
  currentUser: ${context.user.login}
```

## A Seamless Authoring Experience Awaits

The updated editor experience is designed to minimize friction, boost productivity, and transform cloud development into a more enjoyable and effective journey. We are eager for you to explore these new features and see firsthand how they enhance your development process.

Discover more about the capabilities of Pulumi ESC and how it can support your projects by checking out our [documentation](/docs/esc).
