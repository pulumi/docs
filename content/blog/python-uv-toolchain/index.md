---
title: "Pulumi + uv: Fast Python Package and Project Management"
date: 2024-11-27T12:43:45+01:00
draft: false
meta_desc: Learn how to use uv, an ultra-fast Python package manager, now fully integrated
  with Pulumi
meta_image: meta.png
authors:
  - adam-gordon-bell
  - julien-poissonnier
tags:
  - python
  - infrastructure-as-code
social:
  twitter: "Pulumi + uv: Announcing fast Python package management with uv, now fully
    integrated with Pulumi. See Adam and Julien discuss the new functionality in this
    video, or read our blog: www.pulumi.com//blog/python-uv-toolchain"
  linkedin: "We're thrilled to announce built-in support for uv in Pulumi!\nuv is
    an ultra-fast Python package manager written in Rust that can install dependencies
    up to 100x faster than traditional tools. Now fully integrated with Pulumi, it
    provides one of the fastest ways to manage your Python dependencies and virtual
    environments.\nLearn more in our blog post: www.pulumi.com//blog/python-uv-toolchain"

search:
  keywords:
    - uv
    - Python
    - Python package
    - virtual environments
    - package manager
---

Continuing our work to bring [the best of modern Python to Infrastructure as Code](/blog/pulumi-loves-python/), we are excited to announce built-in support for [uv](https://docs.astral.sh/uv/) in Pulumi. uv is an extremely fast Python package manager that can install dependencies up to 100x faster than traditional tools, providing one of the fastest ways to manage your Python dependencies and virtual environments.

<!--more-->

## Why uv?

Listen in on this discussion between [Adam Gordon Bell](/blog/author/adam-gordon-bell/) and [Julien Poissonnier](/blog/author/julien-poissonnier/) as they discuss Pulumi + uv and why uv is so fast!
{{< youtube "hxi7ZL9H0IU?rel=0" >}}

uv brings several key advantages to your Python development workflow:

- **Blazing Fast Performance**: Written in Rust, uv can install packages 10-100x faster than pip
- **Reliable Dependency Resolution**: Advanced resolution algorithm ensures consistent environments
- **Drop-in Replacement**: Works seamlessly with existing requirements.txt and pyproject.toml files
- **Built-in Virtual Environment Management**: Simplified environment handling out of the box

## Using uv in Pulumi

To use uv to manage your Python virtual environment and dependencies, set the `toolchain` option to `uv` in your `Pulumi.yaml` file:

```yaml
name: uv-goes-brrrr
runtime:
  name: python
  options:
    toolchain: uv
    virtualenv: .venv
```

If you have uv installed, you can run `pulumi new python` and select uv as the toolchain to use for installing dependencies and running the program.

You can find more information on how to use uv in Pulumi in our [Python documentation](/docs/iac/languages-sdks/python/#uv).
