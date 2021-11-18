---
title: "Python"
meta_desc: An overview of how to use Python for infrastructure as code
           on any cloud (AWS, Azure, GCP, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/docs/reference/python/"]
---

<img src="/logos/tech/logo-python.svg" align="right" width="150" style="padding:8px; margin-top: -64px">

Pulumi supports programs written in Python 3. Python version 3.6 or later is required.

{{< install-python >}}

## Getting Started

The fastest way to get up and running is to choose from one of the following Getting Started guides:

<div class="tiles mt-4">
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/aws" >}}?language=python">
            <img class="h-8 mx-auto" src="/logos/tech/aws.svg" alt="AWS">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/azure" >}}?language=python">
            <img class="h-8 mx-auto" src="/logos/tech/azure.svg" alt="Azure">
        </a>
    </div>
    <div class="flex-1 pb-4 md:mr-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/gcp" >}}?language=python">
            <img class="h-8 mx-auto" src="/logos/tech/gcp.svg" alt="Google Cloud">
        </a>
    </div>
    <div class="flex-1 pb-4">
        <a class="tile p-4" href="{{< relref "/docs/get-started/kubernetes" >}}?language=python">
            <img class="h-8 mx-auto" src="/logos/tech/k8s.svg" alt="Kubernetes">
        </a>
    </div>
</div>

## Pulumi Programming Model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using
Pulumi. [Architecture & Concepts]({{< relref "/docs/intro/concepts" >}}) describes these concepts
with examples available in Python. These concepts are made available to you in the Pulumi SDK.

The Pulumi SDK is available to Python developers as a Pip package distributed on PyPI. To learn more,
[refer to the Pulumi SDK Reference Guide]({{< relref "/docs/reference/pkg/python/pulumi" >}}).

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Python and Pulumi, and the [Inputs and Outputs]({{< relref "/docs/intro/concepts/inputs-outputs" >}}) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

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

There are many [Pulumi Python packages]({{< relref "/docs/reference/pkg" >}}) available.

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
