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

This is enabled by skipping the default dependency installation step (under Advanced Settings in the UI), and setting a few pre-run commands and environment variables.
