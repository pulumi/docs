---
title: "New Provider Resource Option: Environment Variable Remapping"
date: 2026-02-12
draft: false
meta_desc: "Remap provider environment variables to custom keys using the new resource option, pulumi.EnvVarMappings"
meta_image: meta.png
authors:
    - guinevere-saenger
tags:
    - features
    - packages
schema_type: auto

# Optional: Social media promotional copy (for reference only, does not auto-post)
social:
    twitter:
    linkedin:
---

Pulumi is excited to introduce environment variable remapping as a provider resource option.
From Pulumi version (TODO: version), you can now define your own environment variables and remap them to existing provider
environment variables, allowing you to set them to multiple different values when running multiple providers in the same process.

<!--more-->

When configuring a Pulumi provider to authenticate against a cloud provider, there are two main options available.
You can set authentication values as secrets in your Pulumi.yaml config.

```bash
$ pulumi config set azure-native:clientSecret <clientSecret> --secret
```

Alternately, you can also use the terminal environment of where you're running your Pulumi commands.

```bash
export ARM_CLIENT_SECRET=1234567`
```

Using environment variables in this manner is especially useful in CI environments, or when you'd rather not write that auth token to state, even encrypted.
But there's currently several use cases where this breaks down, due to the hard-coded nature of the environment variables that a given provider expects.

## Multiple providers or provider instances that expect different authentication values

For example,  the Azure Native provider as well as the Azure Classic provider expect `ARM_CLIENT_SECRET` to be set.
But if you're using both providers in the same process, you're limited to using the same value for `ARM_CLIENT_SECRET`.

Similarly, multiple explicit providers targeting different AWS regions were up until now not able to set their configuration via environment variable.
Users had to set these values in the provider config, which not only writes secrets to state, but also results in a noisy diff on an otherwise no-op upgrade when token rotation is used.

For these and similar scenarios, we have a new solution for you: setting mappings of environment variable keys on your provider.
The concept is as follows:

"For any environment variable that my provider expects, I want to be able to tell Pulumi to use the value of a custom-defined environment variable instead."

Example (make it in all languages)
TODO: give example code

You can now customize each value your provider sees by defining a new environment variable, and then mapping your provider's defined variable to yours.

Available in Pulumi version 1.250.awesome and higher.

Main content goes here. Everything after the <!--more--> comment appears only on the full post page.

Avoid using images or code samples in the first 70 words, as they may not render properly in summaries.

For more guidance, see [BLOGGING.md](https://github.com/pulumi/docs/blob/master/BLOGGING.md).
