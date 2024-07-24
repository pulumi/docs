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

The Pulumi SDK is available to Python developers as a package distributed on PyPI. To learn more,
[refer to the Pulumi SDK Reference Guide](/docs/reference/pkg/python/pulumi/).

### Inputs and Outputs

The Pulumi programming model includes a core concept of `Input` and `Output` values, which are used to track how outputs of one resource flow in as inputs to another resource.  This concept is important to understand when getting started with Python and Pulumi, and the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation is recommended to get a feel for how to work with this core part of Pulumi in common cases.

In Python, inputs that are objects, that is inputs that group multiple values together, can be represented either as classes or as dictionary literals. The types for the argument classes have the suffix `Args`, whereas the types for the dictionaries have the suffix `ArgsDict`. Both types take the same arguments, but the dictionary types are often more concise.

{{% notes type="info" %}}
The types with the suffix `ArgsDict` for dictionary literals were introduced in July 2024. You can still use dictionary literals with [providers](/docs/concepts/how-pulumi-works/#resource-providers) that have not been updated yet with this change, but you will not benefit from the type checking that the new types provide.
{{% /notes %}}

This example shows two ways to create an `s3.Bucket` resource in Python, once using a dictionary literal and once using a class:

```python
import pulumi_aws as aws

bucket1 = aws.s3.Bucket(
    "my-bucket-with-dictionary-literals",
    website={
        "error_document": "error.html",
        "index_document": "index.html",
    },
)

bucket2 = aws.s3.Bucket(
    "my-bucket-with-args",
    website=aws.s3.BucketWebsiteArgs(
        error_document="error.html",
        index_document="index.html",
    ),
)
```

### Blocking and Asynchronous Code

A Python Pulumi program is single threaded and the Pulumi runtime creates an
event loop to enable the runtime to be asynchronous.

Given these constraints, [Blocking and Async Python with
Pulumi](python-blocking-async) gives some recommendations on using blocking and
asynchronous code within Python Pulumi programs.

## Using Pulumi PyPI Packages {#pypi-packages}

### Virtual Environments

It is not required, but we recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to isolate the dependencies of your projects and ensure reproducibility between machines.

When creating a new Python project with `pulumi new`, you are offered the choice between `pip` (default) and `poetry` to manage your dependencies. If you choose `pip`, Pulumi will create a virtual environment in a `venv` directory with required dependencies from `requirements.txt` installed in it. If you choose `poetry`, Pulumi will create a `pyproject.toml` file and run Poetry to create a virtual environment in its [default location](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment). Pulumi requires Poetry version 1.8.0 or later. Pulumi will automatically use this virtual environment when running the program.

This behavior is controlled by the `toolchain` and `virtualenv` `runtime` options in `Pulumi.yaml`.

To use pip, set the `toolchain` option to `pip`, along with the `virtualenv` option:

```yaml
runtime:
  name: python
  options:
    toolchain: pip
    virtualenv: venv
```

`virtualenv` is the path to a virtual environment to use.

To use Poetry, set the `toolchain` option to `poetry`:

```yaml
runtime:
  name: python
  options:
    toolchain: poetry
```

To further configure `poetry`, you can provide a [`poetry.toml` configuration file](https://python-poetry.org/docs/configuration/#local-configuration) in the project directory.

Existing Python projects that do not use a virtual environment can opt-in to using the built-in virtual environment support by setting the above options. After updating the options, run `pulumi install` to create the virtual environment and install dependencies.

#### Self managed virtual environments

If you prefer to manage the virtual environment on your own (for example, using a tool like [Pipenv](https://github.com/pypa/pipenv)), you can delete the local `venv` directory and unset the `virtualenv` option in `Pulumi.yaml`:

```yaml
runtime: python
```

When managing the virtual environment on your own, you'll need to run any `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell (or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix any `pulumi` commands with `pipenv run pulumi ...`).

### Type Checking

Pulumi Python libraries ship with type hints. You can manually run a type checking system of your choice when developing with Pulumi to make use of these type hints. As of 3.113.0 Pulumi also has first class support for `mypy` and `pyright` when running your program.

This behavior is controlled by the following `typechecker` `runtime` option in `Pulumi.yaml`:

```yaml
runtime:
  name: python
  options:
    typechecker: mypy
```

When set, Pulumi will invoke the type checker before running your program. This can be used to ensure your program is always type safe when running `pulumi up` without you having to remember to run a separate checking command beforehand.

### Adding a new dependency {#packages}

There are many [Pulumi Python packages](/registry) available.

#### Pip

To install a new dependency in the virtual environment when using `pip`, add an entry to `requirements.txt`, and run the following in your project directory:

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

#### Poetry

To add a new dependency when using `poetry`, run the `poetry add` command in your project directory:

{{< chooser os "macos,windows,linux" >}}

{{% choosable os macos %}}

```bash
$ poetry add ${PACKAGE_NAME}
```

{{% /choosable %}}

{{% choosable os linux %}}

```bash
$ poetry add ${PACKAGE_NAME}
```

{{% /choosable %}}

{{% choosable os windows %}}

```bat
> poetry add ${PACKAGE_NAME}

```

{{% /choosable %}}

{{< /chooser >}}

### Dev Versions

Pulumi SDKs also publish pre-release versions that include all the latest changes from the main development branch.  If you would like to install a pre-release version, you can use the `--pre` flag with `pip` or the `--allow-prereleaases` flag with `poetry`. For example:

```bash
pip install --pre -r requirements.txt
poetry add --allow-prereleases ${PACKAGE_NAME}
```

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
