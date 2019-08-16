---
title: Pulumi Cloud Console
menu:
  intro:
    parent: concepts
    weight: 8

aliases: [/docs/reference/service]
---

The [Pulumi Cloud Console](https://app.pulumi.com) allows you to manage your stacks online. It enables
you to to collaborate with multiple developers, protect against concurrent updates, store resource and
update history, integrate with your CI/CD system, and more!

## Getting Started

To get started using the Pulumi Cloud Console, simply navigate to [app.pulumi.com](https://app.pulumi.com)
and sign up. The [Pulumi Community Edition]({{< relref "editions#community-edition" >}}) is free forever
for unlimited individual use.

<a class="btn" href="https://app.pulumi.com/signup" target="_blank">
    GET STARTED
</a>

## Stack Management

The Pulumi Cloud Console manages stacks, providing safe locking so that your resource state can never
get corrupted by a concurrent update.

Navigate to previous stack updates, and see who applied what change and when. Or see the point-in-time history if an individual cloud resource.

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/reference/service/stack-resource-visualization.png" alt="Stack Resource Visualization">

## Collaboration

The Pulumi Cloud Console enables you to Work with other developers and coordinate on updates.

You can use fine-grained [stack permissions]({{< relref "stack-permissions" >}}) to control who has access to stacks,
or use [teams]({{< relref "teams" >}}) for role-based access control.

## Integrations and Extensions

Pulumi is integrated with popular 3rd party services such as [GitHub]({{< ref "/docs/intro/console/continuous-delivery/github-app" >}}).
You can integrate Pulumi into your current [continuous delivery]({{< relref "continuous-delivery" >}}) pipeline.

<img class="shadow-2xl lg:max-w-xl" src="/images/docs/github-app/pr-comment.png" alt="Pulumi GitHub App">

You can also build your own extensions, such trigger a custom workflow in response to a
[webhook]({{< relref "webhooks" >}}) from the Pulumi Cloud Console.
