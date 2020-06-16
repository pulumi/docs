---
title: "Spinnaker"
meta_desc: "This page provides an overview of how to use Pulumi plugin for Spinnaker to run Pulumi apps."

menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

This page provides an overview of how to use the Pulumi plugin for Spinnaker to run Pulumi apps.

Pulumi doesn't require any particular arrangement of stacks or workflow to work in a
continuous integration / continuous deployment system. So the steps described here can be
altered to fit into any existing type of deployment setup.

## Prerequisites

### Spinnaker installation

> For a full overview of Spinnaker Plugins, please see the official plugin creator's [guide](https://www.spinnaker.io/guides/developer/plugin-creators/overview/).

Plugins are a recent addition to Spinnaker and as such require a more recent version to use plugins as well as the Pulumi plugin for Spinnaker, which this guide will show you how to use. 

* Spinnaker v1.19.4+
* Halyard 1.34+

The Pulumi plugin for Spinnaker has been tested with 1.20.4, but should work with 1.19.x (specifically 1.19.4+ as per above requirement for plugins in general) installations as well.

### Pulumi

This guide walks-through a setup that uses the default Pulumi Managed Backend 

### Required secrets

* `PULUMI_ACCESS_TOKEN`

## Installing The Spinnaker Plugin

> While using the Pulumi plugin is optional, doing so will help reduce the maintenance of the manual steps required to run Pulumi in Spinnaker.

Installing the plugin is comprised of two steps. First, you'll need to add the relevant plugin repository to your Halyard configration using the `hal` CLI. Then, you can add the plugin itself.

```
# Add the Pulumi plugins repository for Spinnaker
hal plugins repository add pulumi --url https://raw.githubusercontent.com/pulumi/spinnaker-plugins-repository/master/repositories.json

# Add the plugin itself
hal plugins add Pulumi.PreConfiguredJobPlugin --enabled true --version 0.0.1 --extensions pulumi.PreConfiguredJobStage

# Apply the updates
hal deploy apply
```

> Depending on your Spinnaker installation you might have to run the above commands using `sudo`. 

## Using The Plugin

Navigate to your Spinnaker instance's Deck UI, and configure the pipeline with the `Pulumi` stage. Here's an example of the stage with its values filled-in.


