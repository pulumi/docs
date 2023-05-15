---
title: "Simpler configuration management with project level config"
date: 2022-11-02T06:00:00-07:00
meta_desc: The introduction of project level config makes infrastructure configuration even easier with Pulumi.
meta_image: meta.png
authors:
    - fraser-waters
    - zaid-ajaj
tags:
    - features
    - config
---

One of our most up-voted feature requests (with 78 thumbs ups) is to [support hierarchical config](https://github.com/pulumi/pulumi/issues/2307). We're happy to announce that we've now released the first part of plans to support this feature.

Pulumi will now allow you to set configuration values in your `Pulumi.yaml` file, using the given value as a default for all stacks in the project. While we expect even this first level of support will be incredibly useful to many people we also want to assure you that we have many more plans in place to make this feature even better.

### Project level configuration values

Pulumi has always had the concept of [configuration per stack](/docs/concepts/config/), and the changes for project level configuration haven't fundamentally changed that. You can still set config for stacks via the `pulumi config` CLI command, or by editing the `Pulumi.<stack>.yaml` file. Project level config just gives you the ability to set default values for all stacks in your `Pulumi.yaml`.

A common request we get for this is making sure that all stacks use the same AWS region, or don't have default providers enabled. You can now do this by setting these in your `Pulumi.yaml`.

```yaml
name: project
runtime: go
config:
    pulumi:disable-default-providers: [“*”]
    aws:region: us-east-1
```

As you can see this allows setting default configuration values per-stack for configuring the engine or providers, but you can also set default values for project configuration. For example maybe you have a default count of the number of virtual machines to create:

```yaml
name: project
runtime: go
config:
    vm-count: 2
```

The only caveat to mention about this system is that if you have object values they must be nested under a key `value`. So if you want to set the key `obj` to the object value `{ foo: "bar" }` you would need to write it as such:

```yaml
name: project
runtime: go
config:
    obj:
        value:
            foo: bar
```

This allows the engine to distinguish between values and schemas, which we will show below.

### Configuration specification

A related feature to defining values for config at the project level is [being able to define a schema for the config](https://github.com/pulumi/pulumi/issues/1052). This allows you to define what configuration settings you expect in your `Pulumi.yaml` so that the engine can use that information to validate configuration for every stack.

This is done using a very similar declaration to JSON schema, or our Pulumi JSON schema (the schemas from resource providers that drive our code generators). Below is a small example of some of the things you can declare:

```yaml
config:
    vm-count:
        type: integer
        description: the number of virtual machines to create
        default: 2
    subnets:
        type: array
        description: an array of subnets to create
        items:
            type: string
    vaultKey:
        type: string
        description: which vault key to use for this stack
        secret: true
```

These are declared in the same config block as the other project level config shown through this post. You can combine the two by declaring your project settings and defining defaults for providers together:

```yaml
config:
    aws:region: us-east-2
    createVpc:
        type: boolean
        default: false
```

### Deprecation of 'configuration' in YAML

When we released our support for simple Pulumi programs in YAML we added some support for configuration with it. This was done via the [`configuration` key](https://www.pulumi.com/docs/languages-sdks/yaml/yaml-language-reference/#configuration) in the `Pulumi.yaml` file. We'll be deprecating support for that key now, as YAML will instead use the new standard project configuration.

### Future plans

This is just the start of our support for better config. We posted [a long comment to GitHub](https://github.com/pulumi/pulumi/issues/2307#issuecomment-1225592223) earlier this year to explain some of our future plans, and we do intend to continue improving this part of the Pulumi system as described in that comment.

## Feedback

We'd love to hear how you plan on using these new configuration features, and if you have questions or concerns about this change let us know in our community [Slack](https://slack.pulumi.com/) or [in GitHub Discussions](https://github.com/pulumi/pulumi/discussions).
