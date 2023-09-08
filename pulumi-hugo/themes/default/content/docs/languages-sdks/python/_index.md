---
title_tag: "Python | Languages & SDKs"
meta_desc: An overview of how to use Python with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Python
h1: Pulumi & Python
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  languages:
    identifier: python
    weight: 2
aliases:
- /docs/reference/python/
- /docs/intro/languages/python/
- /python/
---

<img src="/logos/tech/logo-python.svg" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports writing your infrastructure as code in the Python language running on any [supported version](https://devguide.python.org/versions/#versions).

{{< install-python >}}

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Concepts](/docs/intro/concepts) describes these concepts
with examples available in Python. These concepts are made available to you in the Pulumi SDK.

The Pulumi SDK is available to Python developers as a Pip package distributed on PyPI. To learn more,
[refer to the Pulumi SDK Reference Guide](/docs/reference/pkg/python/pulumi/).

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Python and Pulumi, and the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

## Using Pulumi PyPI Packages {#pypi-packages}

### Virtual Environments

It is not required, but we recommend using a virtual environment to isolate the dependencies of your projects and ensure reproducibility between machines.

As of Pulumi 2.4.0, new Python projects created with `pulumi new` will have a virtual environment created in a `venv` directory with required dependencies from `requirements.txt` installed in it, and Pulumi will automatically use this virtual environment when running the program.

This behavior is controlled by the following `virtualenv` `runtime` option in `Pulumi.yaml`:

```yaml
runtime:
  name: python
  options:
    virtualenv: venv
```

`virtualenv` is the path to a virtual environment to use.

Existing Python projects can opt-in to using the built-in virtual environment support by setting the `virtualenv` option. To manually create a virtual environment and install dependencies, run the following commands in your project directory:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ python3 -m venv venv
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os windows %}}

```bat
> python -m venv venv
> venv\Scripts\pip install -r requirements.txt
```

{{% /choosable %}}

{{< /chooser >}}

If you prefer to manage the virtual environment on your own (for example, using a tool like [Pipenv](https://github.com/pypa/pipenv)), you can delete the local `venv` directory and unset the `virtualenv` option in `Pulumi.yaml`:

```yaml
runtime: python
```

When managing the virtual environment on your own, you'll need to run any `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell (or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix any `pulumi` commands with `pipenv run pulumi ...`).

### Adding a new dependency {#packages}

There are many [Pulumi Python packages](/registry) available.

To install a new dependency in the virtual environment, add an entry to `requirements.txt`, and run the following in your project directory:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ venv/bin/pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable os windows %}}

```bat
> venv\Scripts\pip install -r requirements.txt
```

{{% /choosable %}}

{{< /chooser >}}

## Package Documentation

In addition to the standard packages the [Pulumi Registry](/registry/) houses 100+ Python packages.

### Standard Packages

<dl class="tabular">
    <dt>Pulumi SDK</dt>
    <dd><a href="/docs/reference/pkg/python/pulumi">pulumi</a></dd>
    <dt>Pulumi Policy</dt>
    <dd><a href="/docs/reference/pkg/python/pulumi_policy">pulumi_policy</a></dd>
    <dt>Pulumi Terraform</dt>
    <dd><a href="/docs/reference/pkg/python/pulumi_terraform">pulumi_terraform</a></dd>
</dl>
