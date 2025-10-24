---
title: "Component Usage Tracking in Pulumi IDP"
date: 2025-10-21T09:00:00-07:00
draft: false
meta_desc: "Track which stacks use components from your private registry to understand adoption and manage updates."
meta_image: meta.png
authors:
    - idp-team
tags:
    - idp
    - features
    - platform-engineering
---

Platform teams can now see which stacks are using components from the private registry, helping you understand adoption and plan updates.
<!--more-->

When you publish components to the private registry, tracking their usage across your organization becomes important. The new usage tracking feature shows which stacks depend on each component, including version information and last update times.

## What you get

Each component in the private registry includes a usage tab that displays:

- Stacks using the component
- Component versions in use
- Last update timestamps for each stack

This visibility helps platform teams make informed decisions about component updates and understand which teams have adopted standardized building blocks.

## Why it matters

Before updating a component version, you can see exactly which stacks will be affected. When deprecating an older version, you know which teams need to migrate. When measuring the success of your platform engineering efforts, you can track component adoption across the organization.

The feature respects existing access controls, showing only stacks you have permission to view.

## Getting started

Usage tracking is automatically available for components in your private registry. Visit any component detail page to see the usage tab.

For more information, see the [private registry documentation](/docs/idp/get-started/private-registry/).
