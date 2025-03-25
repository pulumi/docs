---
title: "Pulumi + Python: Bringing the Best of Modern Python to IaC"
date: 2024-07-03T14:17:38+02:00
draft: false
meta_desc: A big step forward for Python + Pulumi, with new Pythonic input types,
  built in type checking and support for Poetry.
meta_image: meta.png
authors:
  - julien-poissonnier
tags:
  - python
social:
  twitter:
  linkedin:
search:
  keywords:
    - pythonic
    - modern
    - iac
    - python
    - poetry
    - bringing
    - checking

---

One of our most important goals at Pulumi is to bring the very best of software engineering tools and practice to your cloud infrastructure. Pulumi embraces existing popular programming languages as a way to tap into everything that these language ecosystems offer developers -- rich programming models, familiar syntax, IDE productivity, package management and versioning, componentization and reuse, testing, and so much more.

Python in particular has been one of the most popular languages used across the Pulumi platform, and the fastest growing over the last 2 years. Over the last few months, we've worked on a set of improvements that allow Pulumi users to take advantage of the latest and greatest tooling and features from the Python ecosystem.  The key new features include:

* __More Pythonic resource APIs__: A new dictionary-based API design which embraces a simple and familiar Pythonic API design along with access to great type checking and tooling building on recent enhancements to `TypedDict` support in the Python programming language and tools.
* __Native support for Poetry__: Built-in support for working with Poetry in place of `pip`, making it easy to integrate Pulumi into projects and repositories leveraging the popular Poetry package management toolchain for Python.
* __Type checker integration__: New ability to run your favorite Python type checkers directly within the Pulumi deployment process.

<!--more-->

## Pulumi + Python

Python was one of the first languages we ever supported in Pulumi, and has grown rapidly for defining and building Infrastructure as Code across any cloud. This growth has accelerated over the last year, driven by a few different trends:

1. DevOps practitioners with existing Python scripting experience who can naturally extend that experience into their IaC development
2. AI and Data-focused organizations with deep Python focus broadly within their organization leaning on IaC development which leverages the same language and tools
3. Broad growth in the Python developer ecosystem

The result has been strong and steady growth of Python Pulumi usage.  This has been especially pronounced among some of the largest and most advanced Pulumi users, who are pushing the boundaries on managing complexity at scale using the best of the Python ecosystem.

## New Features for Pulumi Python Users

### Native Support for Poetry

Pulumi has long had support to create and manage virtual environments using Python's builtin package manager [pip](https://pip.pypa.io/en/stable/). With the [latest release of Pulumi](https://github.com/pulumi/pulumi/releases/tag/v3.121.0), we are excited to announce that we now support [Poetry](https://python-poetry.org) as well. Poetry is a popular Python dependency management tool that allows you to declare your dependencies in a simple and concise way and manage your virtual environment with ease.

When creating a new Pulumi project, the Pulumi CLI will now ask you if you want to use Poetry to manage your dependencies. If you choose to use Poetry, the Pulumi CLI will automatically create a new Poetry project for you and install the necessary dependencies. To opt-in to using Poetry for an existing Pulumi project, set the [`toolchain` runtime option](https://www.pulumi.com/docs/concepts/projects/project-file/#runtime-options) to `poetry` and run `pulumi install`.

```yaml
name: python-and-poetry-are-best-friends
runtime:
  name: python
  options:
    toolchain: poetry
```

### Built-in type checking

Pulumi Python SDKs include type hints compatible with type checkers such as [MyPy](https://www.mypy-lang.org) and [Pyright](https://microsoft.github.io/pyright/#/). In the latest release of Pulumi, you can ask Pulumi to run your typechecker of choice for you as part of Pulumi operations and fail if there are any type errors. This can help you catch type errors earlier and ensure that your Pulumi programs are type-safe.

Add the typechecker of your choice to [your dependencies](https://www.pulumi.com/docs/languages-sdks/python/#packages) and set the [`typechecker` runtime option](https://www.pulumi.com/docs/concepts/projects/project-file/#runtime-options) in your project file to `mypy` or `pyright` to enable automatic type checking.

```yaml
name: python-with-typechecking
runtime:
  name: python
  options:
    typechecker: pyright
```

To enable live type checking in Visual Studio Code set the `typeCheckingMode` setting of the [Pylance extension](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance) to `basic` or higher.

```json
"python.analysis.typeCheckingMode": "basic"
```

[Extensions](https://plugins.jetbrains.com/plugin/24146-pyright-language-server) [for other editors](https://github.com/emacs-lsp/lsp-pyright) [typically have](https://github.com/fannheyward/coc-pyright) [this already](https://zed.dev/docs/languages/python) [enabled](https://github.com/sublimelsp/LSP-pyright).

We have updated the [NGINX on AWS ECS Fargate example](https://github.com/pulumi/examples/blob/master/aws-py-fargate/Pulumi.yaml) to use builtin typechecking and Poetry to manage dependencies. Check it out to see how you can use these new features in your Pulumi projects.

### Pythonic input types

Pulumi has always had a focus on making Infrastructure as Code feel like idiomatic code and the latest release of Pulumi makes it easier to work with input types in Python.

Pulumi supports two ways of specifying inputs for resources in Python. You can use strongly typed, but verbose, argument classes, or you can use dictionaries, which are more idiomatic, but lack type hints. Leveraging improvements to Python's [TypedDict types](https://peps.python.org/pep-0589/), we can offer the best of both worlds -- dictionary inputs now have type hints, providing you with type safety and the flexibility and simplicity of dictionaries.

This really pays off with large nested data structures, such as those you might use when configuring Kubernetes resources. Consider this program that uses argument classes to configure a deployment specification:

```python
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs

app_labels = {"app": "nginx"}
deployment = Deployment(
    "nginx",
    spec=DeploymentSpecArgs(
        selector=LabelSelectorArgs(match_labels=app_labels),
        replicas=1,
        template=PodTemplateSpecArgs(
            metadata=ObjectMetaArgs(labels=app_labels),
            spec=PodSpecArgs(containers=[ContainerArgs(name="nginx", image="nginx")]),
        ),
    ),
)
```

With type hinted dictionaries, we can write the following, which is much more concise and just as type safe!

```python
from pulumi_kubernetes.apps.v1 import Deployment

app_labels = {"app": "nginx"}

deployment = Deployment(
    "nginx",
    spec={
        "selector": {"match_labels": app_labels},
        "replicas": 1,
        "template": {
            "metadata": {"labels": app_labels},
            "spec": {"containers": [{"name": "nginx", "image": "nginx"}]},
        },
    },
)
```

The new Pythonic input types are available in the latest release of the Pulumi SDKs for [Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/), [AWS](https://www.pulumi.com/registry/packages/aws/) and [GCP](https://www.pulumi.com/registry/packages/gcp/), with more provider SDKs to follow soon.

{{% notes type="info" %}}
Due to a performance issue in MyPy, type checking of TypedDict-based inputs is currently disabled when using MyPy as a type checker.  We are working on helping resolve [this issue](https://github.com/python/mypy/issues/17231). In the meantime, we recommend using Pyright as a type checker to get the most complete type checking possible for Dict-based Pulumi Python programs.
{{% /notes %}}

## Summary

We hope you enjoy using these new features and we look forward to hearing your feedback. If you have any questions or need help, please don't hesitate to reach out to us on [Slack](https://pulumi-community.slack.com/) or [GitHub](https://github.com/pulumi/pulumi).
