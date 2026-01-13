---
title: "Introducing the new and improved ESC Editor"
date: 2026-01-14T13:00:00-03:00
draft: true
meta_desc: We’re introducing the new and improved Pulumi ESC Editor in the Console, designed to make managing secrets and configuration easier, faster, and more intuitive.
meta_image: meta.png
authors:
    - sean-yeh
    - vic-fernandez
    - pablo-terradillos
tags:
    - esc
schema_type: auto
social:
    twitter:
    linkedin:
---

Pulumi ESC is Pulumi Cloud’s centralized solution for managing secrets and configuration across every vault and cloud provider you use. It helps teams secure their configuration while adopting modern best practices like short-lived credentials with OIDC and automated secret rotation.

Whether you’re configuring Pulumi programs, powering applications and services, or managing credentials for tools like the AWS CLI, ESC provides a single, consistent way to do it safely and at scale.

Behind the scenes, ESC integrates with multiple cloud providers and secret managers, supports composable environments, and offers rich built-in functions, from simple value transformations to encoding files as Base64.

With this level of power, usability matters more than ever.
That’s why today we’re introducing the new and improved Pulumi ESC Web Editor, designed to make managing secrets and configuration easier, faster, and more intuitive.

<!--more-->

Today, you can create and manage your Pulumi ESC configuration in multiple ways—using the CLI `set` and `edit` commands, or through our [VS Code extension](/docs/esc/development/vs-code-extension/). For many users, however, their first experience with ESC happens in the Pulumi Cloud web console.

We know that most of our users are comfortable writing code and editing ESC YAML directly, and our previous Web Editor supported that workflow well. However, using ESC only as a place to store configuration and secrets means missing out on much of the power built into the platform. To address this, we introduced a Table View that allowed users to manage environments through a convenient UI, exposing a broader set of capabilities without requiring direct YAML edits.

While this abstraction made ESC more approachable, it also introduced its own drawbacks. In particular, it could be difficult to understand how UI actions mapped to the underlying YAML, and we heard clear feedback from users that this created confusion.

The new Pulumi ESC Editor brings these two approaches together. You can now freely switch between writing YAML and using rich UI elements to manipulate your environment—while always having clear, in-context information about what you’re doing and what’s possible.

Let’s explore some of these use cases!

## Adding and editing secrets

Adding secrets is now as simple as selecting **Secret** from the **Add new** menu.
!["Screenshot of add new menu"](menu.png)

The **Inspect** tab lets you view and edit your secret securely, automatically encrypting it as ciphertext in your environment definition. No more worrying about accidentally exposing sensitive values!

!["Screenshot of secret editor"](secrets.png)

## Using providers and built-in functions

ESC offers a large library of [providers](/docs/esc/integrations/) and [built-in functions](/docs/esc/environments/syntax/builtin-functions/) to use in your environment. The new editor makes discovering and using them effortless.

<div class="flex flex-col md:flex-row gap-4 my-4">
  <img src="providers.png" alt="Screenshot of adding providers" class="w-full" />
</div>

<div class="flex flex-col md:flex-row gap-4 my-4">
  <img src="functions.png" alt="Screenshot of adding functions" class="w-full" />
</div>

When you add a provider or function, the editor inserts it with example values to get you started quickly. The **Inspect** tab provides instant access to documentation, so you can more easily configure the integrations.

!["Screenshot of Provider documentation"](provider-docs.png)

## Exporting configurations

Consuming your configuration where you need it is now easier than ever. The **Export** menu in the **Inspect** sidebar lets you quickly expose values as Pulumi config for your stacks, or as environment variables in your shell.

!["Screenshot of Exporting configurations"](exports.png)

## Conclusion

The new Pulumi ESC Editor brings together the best of both worlds: the power of the YAML editor with the ease of UI controls. Try it out today in the Pulumi Cloud console and let us know what you think!
