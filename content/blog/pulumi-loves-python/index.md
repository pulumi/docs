---
title: "Pulumi Loves Python"
date: 2024-06-28T16:17:38+02:00
draft: false
meta_desc: First-class Python support with Poetry, Pythonic input types and built-in type checking.
meta_image: meta.png
authors:
    - julien-poissonnier
tags:
    - python
social:
    twitter:
    linkedin:

---

Pulumi has first-class support for Python, and it is one of our most popular languages. We are always working to improve the Python experience, and we are excited to announce some new features that make it even easier to use Python with Pulumi, including support for Poetry, built-in type checking, and more Pythonic input types.

<!--more-->

<!-- expand on the introduction here -->

## Poetry

Pulumi has long had support to create and manage virtual environments using Python's builtin package manager [pip](https://pip.pypa.io/en/stable/). With the [latest release of Pulumi](https://github.com/pulumi/pulumi/releases/tag/v3.121.0), we are excited to announce that we now support [Poetry](https://python-poetry.org) as well. Poetry is a popular Python dependency management tool that allows you to declare your dependencies in a simple and concise way and manage your virtual environment with ease.

When creating a new Pulumi project, the Pulumi CLI will now ask you if you want to use Poetry to manage your dependencies. If you choose to use Poetry, the Pulumi CLI will automatically create a new Poetry project for you and install the necessary dependencies. To opt-in to using Poetry for an existing Pulumi project, set the [`toolchain` runtime option](https://www.pulumi.com/docs/concepts/projects/project-file/#runtime-options) to `poetry` and run `pulumi install`.

## Built-in type checking

Pulumi Python SDKs include type hints compatible with type checkers such as [MyPy](https://www.mypy-lang.org) and [Pyright](https://microsoft.github.io/pyright/#/). In the latest release of Pulumi, you can ask Pulumi to run your typechecker of choice for you as part of Pulumi operations and fail if there are any type errors. This can help you catch type errors earlier and ensure that your Pulumi programs are type-safe.

Set the [`typechecker` runtime option](https://www.pulumi.com/docs/concepts/projects/project-file/#runtime-options) in your project file to `mypy` or `pyright` to enable automatic type checking.

```yaml
name: python-with-poetry-and-typechecking
runtime:
  name: python
  options:
    toolchain: poetry
    typechecker: pyright
```

## Pythonic input types

Pulumi has always had a focus on making infrastructure as code feel like idiomatic code and the latest release of Pulumi makes it easier to work with input types in Python.

Pulumi supports two ways of specifying inputs for resources in Python. You can use strongly typed, but verbose, argument classes, or you can use dictionaries, which are more idiomatic, but lack type hints. Now get the best of both worlds, leveraging Python's [TypedDict types](https://peps.python.org/pep-0589/), dictionary inputs now have type hints, providing you with type safety and the flexibility of dictionaries.

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

The new Pythonic input types are available in the latest release of the Pulumi SDKs for [Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/) and [AWS](https://www.pulumi.com/registry/packages/aws/), with more providers SDKs to follow soon.

{{% notes type="info" %}}
Due to a performance issue, TypedDict based inputs are not yet available when using MyPy as type checker. We recommend you use Pyright as type checker while we work on resolving [this issue](https://github.com/python/mypy/issues/17231).
{{% /notes %}}

## Summary

We hope you enjoy using these new features and we look forward to hearing your feedback. If you have any questions or need help, please don't hesitate to reach out to us on [Slack](https://pulumi-community.slack.com/) or [GitHub](https://github.com/pulumi/pulumi).
