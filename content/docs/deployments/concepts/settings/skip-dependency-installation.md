---
title_tag: "Skipping Automatic Dependency Installation | Pulumi Deployments"
meta_desc: Take control of the dependency installation step in a Pulumi Deployment instead of relying on the default dependency manager
title: "Skipping Automatic Dependency Installation"
h1: "Skipping Automatic Dependency Installation"
menu:
  deployments:
    name: Skipping Dependency Installation
    parent: deployments-concepts-settings
    identifier: deployments-concepts-settings-skip-dependency-installation
    weight: 60
---

By default, the deployment executor will attempt to install dependencies for your project by using the default dependency manager for the language (i.e. `npm` for nodejs or `virtualenv` for python). However, there may be scenarios where you may want to have more control over the dependency installation step (e.g. you are using `yarn` and/or a different version of `node` than the one that is installed by default).

To do this, turn on **Skip package manager dependency installation** under **Advanced settings** on the stack's **Settings** → **Deploy** page, and then install dependencies yourself with a few [pre-run commands](/docs/deployments/concepts/settings/pre-run-commands/) and [environment variables](/docs/deployments/concepts/settings/environment-variables/).

This setting is separate from [dependency caching](/docs/deployments/concepts/settings/dependency-caching/). Skipping installation means the project's package manager doesn't run at all, while caching only makes the installation step faster when it does run.
