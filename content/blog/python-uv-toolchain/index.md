---
title: "Pulumi + uv: Fast Python Package and Project Management"
date: 2024-11-25T12:43:45+01:00
draft: false
meta_desc: Uv is an extremely fast Python package and project manager that is now fully integrated into Pulumi
meta_image: meta.png
authors:
    - adam-gordon-bell
    - julien-poissonnier
tags:
    - python
social:
    twitter:
    linkedin:

---

Continuing our work to bring [the best of modern Python to Infrastructure as Code](/blog/pulumi-loves-python/), we are excited to announce builtin support for [uv](https://docs.astral.sh/uv/) in Pulumi. uv is an extremely fast Python package and project manager that is now fully integrated into Pulumi, and provides one of the fastest ways to manage your Python dependencies and virtual environments.

<!--more-->

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

You can find more information on how to use uv in Pulumi in our [Python documentation](/docs/iac/languages-sdks/python/#uv).

## What Makes uv so Fast?

If you are  curious about how uv is so fast, listen in on this discussion between [Adam Gordon Bell](/blog/author/adam-gordon-bell/) and [Julien Poissonnier](/blog/author/julien-poissonnier/) as they discuss uv:

{{< youtube "hxi7ZL9H0IU?rel=0" >}}
