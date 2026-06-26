---
title_tag: "Python | Languages & SDKs"
meta_desc: Learn to use Python with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Python
h1: Pulumi & Python
menu:
    iac:
        name: Python
        parent: iac-languages
        weight: 2
        identifier: iac-languages-python
    languages:
        identifier: python
        weight: 2
aliases:
    - /docs/reference/python/
    - /docs/intro/languages/python/
    - /python/
    - /docs/languages-sdks/python/
---

Pulumi supports writing your infrastructure as code in Python. Using a general-purpose language for infrastructure as code provides several key advantages:

- **Familiar syntax**: Write infrastructure code using the same language and patterns you already know
- **Rich ecosystem**: Leverage the vast [PyPI](https://pypi.org/) package ecosystem in your infrastructure code
- **Native tooling**: Use your existing IDE, linters, test frameworks such as `pytest` and `unittest`, and other development tools without requiring plugins or extensions
- **Type safety**: Pulumi's Python libraries ship with type hints, and Pulumi has first-class support for the `mypy` and `pyright` type checkers

## Installation requirements

### Python runtime

Pulumi supports any [currently supported version](https://devguide.python.org/versions/#versions) of Python. We recommend using a recent release for the best experience.

To use the Python runtime, set `runtime: python` in your `Pulumi.yaml`:

```yaml
runtime: python
```

Install [Python](https://www.python.org/downloads/). To reduce potential issues with setting up your Python environment on Windows or macOS, you should install Python through the official Python installer.

{{% notes type="info" %}}
Either `pip`, `poetry` or `uv` is required to install dependencies. If you installed Python from source, with an installer from [python.org](https://python.org/), or via [Homebrew](https://brew.sh/) you should already have `pip`. If Python is installed using your OS package manager, you may have to install `pip` separately, see [Installing pip/setuptools/wheel with Linux Package Managers](https://packaging.python.org/guides/installing-using-linux-tools/). For example, on Debian/Ubuntu you must run `sudo apt install python3-venv python3-pip`. To install `poetry` follow the [installation instructions](https://python-poetry.org/docs/#installation). To install `uv` follow the [installation instructions](https://docs.astral.sh/uv/getting-started/installation/).
{{% /notes %}}

### Package managers

Pulumi supports the following Python package managers:

- **pip**: Fully supported (default)
- **Poetry**: Fully supported (requires Poetry 1.8.0 or later)
- **uv**: Fully supported

You choose a package manager when you run `pulumi new`, and you can change it at any time with the `toolchain` option in `Pulumi.yaml`. See [Managing Python dependencies](#pypi-packages) below for configuration details.

## Getting started

The fastest way to get started with Pulumi and Python is to use a template:

```bash
$ pulumi new python
```

You can discover additional templates by running `pulumi new` with no arguments, or you can initialize a Pulumi program by supplying a specific URL to the `pulumi new` command. For example:

```bash
$ pulumi new https://github.com/pulumi/templates/tree/master/aws-python
```

See the [`pulumi new` documentation](/docs/iac/cli/commands/pulumi_new/) for full details.

### Program entrypoint

By default, Pulumi runs your program from the `__main__.py` file (or a `setup.py` file) in the project directory. Alternatively, you can set the top-level `main` attribute in your `Pulumi.yaml` to point at a different module file, and Pulumi will pass it to `python`:

```yaml
name: my-project
runtime: python
main: app.py
```

## Defining resources

Writing a Pulumi program in Python involves declaring infrastructure resources using resource constructors. Here are the key concepts:

- **Declare resources**: Create infrastructure resources by instantiating resource classes from provider packages. For example, `aws.s3.Bucket("my-bucket")` creates an S3 bucket.
- **Inputs and outputs**: The Pulumi programming model uses `Input` and `Output` types to track dependencies between resources. Understanding how to work with inputs and outputs is essential for building infrastructure. See the [Inputs and Outputs](/docs/concepts/inputs-outputs/) documentation for details.
- **Immutable infrastructure**: Once declared, resource properties are immutable within your program. Changes to resource definitions result in updates during the next deployment.
- **Stack outputs**: Export values from your program with `pulumi.export(...)` to make them accessible from the CLI or to other Pulumi programs.

The Pulumi SDK provides constructs for working with key Pulumi concepts. For more information, see:

- [Pulumi Concepts](/docs/iac/concepts/)
- [How Pulumi Works](/docs/iac/guides/basics/how-pulumi-works/)

### Resource identity

Every Pulumi resource exposes four forms of identity — its logical name, physical name, physical ID (`resource.id`), and URN (`resource.urn`) — and each form is appropriate for a different context. Passing the wrong form is the most common source of type errors when wiring Python resources together.

For example, the `parent` and `depends_on` fields in `ResourceOptions` expect the **resource object itself**, not a string ID or URN. Conversely, most resource input properties that reference other resources (such as `vpc_id` on a subnet) expect the upstream resource's **`id` output** — an `Output[str]` — not the URN or the variable.

See [Resource identity in Python](/docs/iac/languages-sdks/python/resource-identity/) for a complete guide to each identity form, common type-mismatch pitfalls, and debugging advice.

## Program execution

Pulumi programs are most commonly executed using the Pulumi CLI commands such as `pulumi up`, `pulumi preview`, and `pulumi destroy`. The CLI handles authentication, state management, and orchestrating resource operations.

Alternatively, you can use the [Automation API](/docs/iac/concepts/automation-api/) to programmatically control the Pulumi engine from within your Python code. The Automation API allows you to:

- Embed Pulumi operations in regular Python applications
- Build custom deployment tools and workflows
- Create self-service infrastructure platforms

With Automation API, your Python code controls Pulumi, rather than Pulumi controlling your code.

### Asynchronous code

A Python Pulumi program is single threaded, and the Pulumi runtime creates an event loop to enable the runtime to be asynchronous. Given these constraints, [Blocking and Async Python with Pulumi](/docs/iac/languages-sdks/python/python-blocking-async/) gives some recommendations on using blocking and asynchronous code within Python Pulumi programs.

## Managing Python dependencies {#pypi-packages}

### Virtual environments

It is not required, but we recommend using a [virtual environment](https://docs.python.org/3/tutorial/venv.html) to isolate the dependencies of your projects and ensure reproducibility between machines.

When creating a new Python project with `pulumi new`, you are offered the choice between `pip` (default), `poetry` and `uv` to manage your dependencies. You can also change this at any time by updating the `toolchain` option in `Pulumi.yaml`. Existing Python projects that do not use a virtual environment can opt-in to using the built-in virtual environment support by setting the option and then running `pulumi install` to create the virtual environment and install dependencies.

{{< chooser pythontoolchain "pip,uv,poetry" >}}

{{% choosable pythontoolchain pip %}}

When using `pip` Pulumi will create a virtual environment and install the required dependencies from `requirements.txt`. The `virtualenv` option is required for `pip` and controls the name of the virtual environment directory.

```yaml
runtime:
  name: python
  options:
    toolchain: pip
    virtualenv: venv
```

{{% /choosable %}}

{{% choosable pythontoolchain uv %}}

When using `uv` Pulumi will create a virtual environment in the `.venv` directory and install the required dependencies from `pyproject.toml`. When no `pyproject.toml` file is present, Pulumi will look for a `requirements.txt` file and convert it to a `pyproject.toml` file. The `virtualenv` option controls the name of the virtual environment directory. This is optional for `uv` and defaults to `.venv`.

```yaml
runtime:
  name: python
  options:
    toolchain: uv
    virtualenv: .venv
```

{{% /choosable %}}

{{% choosable pythontoolchain poetry %}}

When using `poetry` Pulumi will run Poetry to create a virtual environment in its [default location](https://python-poetry.org/docs/basic-usage/#using-your-virtual-environment) and install the required dependencies from `pyproject.toml`. When no `pyproject.toml` file is present, Pulumi will look for a `requirements.txt` file and convert it to a `pyproject.toml` file.

Pulumi requires Poetry version 1.8.0 or later.

```yaml
runtime:
  name: python
  options:
    toolchain: poetry
```

To further configure `poetry`, you can provide a [`poetry.toml` configuration file](https://python-poetry.org/docs/configuration/#local-configuration) in the project directory.

{{% /choosable %}}

{{< /chooser >}}

#### Self-managed virtual environments

If you prefer to manage the virtual environment on your own (for example, using a tool like [Pipenv](https://github.com/pypa/pipenv)), you can delete the local `venv` directory and unset the `virtualenv` option in `Pulumi.yaml`:

```yaml
runtime: python
```

When managing the virtual environment on your own, you'll need to run any `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell (or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix any `pulumi` commands with `pipenv run pulumi ...`).

### Adding a dependency {#packages}

There are many [Pulumi Python packages](/registry) available.

{{< chooser pythontoolchain "pip,uv,poetry" >}}

{{% choosable pythontoolchain pip %}}

To install a new dependency in the virtual environment when using `pip`, add an entry to `requirements.txt`, and run the following in your project directory:

```bash
pip install -r requirements.txt
```

{{% /choosable %}}

{{% choosable pythontoolchain poetry %}}

To add a new dependency when using `poetry`, run the `poetry add` command in your project directory. The dependency will be added to the `pyproject.toml` file and installed in the virtual environment:

```bash
poetry add ${PACKAGE_NAME}
```

{{% /choosable %}}

{{% choosable pythontoolchain uv %}}

To add a new dependency when using `uv`, run the `uv add` command in your project directory. The dependency will be added to the `pyproject.toml` file and installed in the virtual environment:

```bash
uv add ${PACKAGE_NAME}
```

{{% /choosable %}}

{{< /chooser >}}

### Type checking

Pulumi Python libraries ship with type hints. You can manually run a type checking system of your choice when developing with Pulumi to make use of these type hints. As of 3.113.0 Pulumi also has first class support for `mypy` and `pyright` when running your program.

This behavior is controlled by the following `typechecker` `runtime` option in `Pulumi.yaml`:

```yaml
runtime:
  name: python
  options:
    typechecker: mypy
```

When set, Pulumi will invoke the type checker before running your program. This can be used to ensure your program is always type safe when running `pulumi up` without you having to remember to run a separate checking command beforehand.

## Documentation and resources

### Pulumi SDK

The [Pulumi SDK (`pulumi`)](/docs/reference/pkg/python/pulumi/) is distributed on PyPI and contains the core constructs for working with Pulumi, including resources, configuration, stack outputs, and more. You will need to reference it in most Pulumi programs.

### Provider SDKs

For managing resources in a Pulumi program, you can find the relevant SDK reference documentation for each provider in [the Pulumi Registry](/registry/).

### Policy SDK

The [Pulumi Policy SDK (`pulumi_policy`)](/docs/reference/pkg/python/pulumi_policy) allows you to author Pulumi Policy as Code policies for validating resource configurations.

### Dev versions

Pulumi SDKs also publish pre-release versions that include all the latest changes from the main development branch. If you would like to install a pre-release version, you can use the `--pre` flag with `pip`, the `--allow-prereleases` flag with `poetry`, or the `--prerelease=allow` flag with `uv`. For example:

```bash
pip install --pre -r requirements.txt
poetry add --allow-prereleases ${PACKAGE_NAME}
uv add --prerelease=allow ${PACKAGE_NAME}
```

For more information on when and how to use dev builds, see [Using dev builds for unreleased fixes](/docs/iac/operations/debugging/using-dev-builds/).

### Testing

- [Unit testing](/docs/iac/concepts/testing/unit/): Test your infrastructure code in isolation
- [Integration testing](/docs/iac/concepts/testing/integration/): Test your infrastructure deployments end-to-end
