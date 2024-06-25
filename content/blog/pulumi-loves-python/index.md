---
title: "Pulumi Loves Python"
date: 2024-06-28T16:17:38+02:00
draft: false
meta_desc: First class Python support with Poetry, Pythonic input types and builtin type checking.
meta_image: meta.png
authors:
    - julien-poissonnier
tags:
    - python
social:
    twitter:
    linkedin:

---

Pulumi has first-class support for Python, and it is one of our most popular languages. We are always working to improve the Python experience, and we are excited to announce some new features that make it even easier to use Python with Pulumi, including support for Poetry, builtin type checking, and more Pythonic input types.

<!--more-->

<!-- expand on the introduction here -->

## Poetry

Pulumi has long had support to create and manage virtual environments using Python's builtin package manager [pip](https://pip.pypa.io/en/stable/). With the [latest release of Pulumi](https://github.com/pulumi/pulumi/releases/tag/v3.121.0), we are excited to announce that we now support [Poetry](https://python-poetry.org) as well. Poetry is a popular Python dependency management tool that allows you to declare your dependencies in a simple and concise way and manage your virtual environment with ease.

When creating a new Pulumi project, the Pulumi CLI will now ask you if you want to use Poetry to manage your dependencies. If you choose to use Poetry, the Pulumi CLI will automatically create a new Poetry project for you and install the necessary dependencies. You can also opt-in to using Poetry for an existing Pulumi project by setting the [`toolchain` runtime option](https://www.pulumi.com/docs/concepts/projects/project-file/#runtime-options) to `poetry` and running `pulumi install`.

## Builtin Type Checking

Pulumi Python SDKs include type hints and you can manually run a type checker when developing with Pulumi to make use of these type hints. Now with the latest release of Pulumi, you can enable automatic type checking when running your program. When you run `pulumi up` or `pulumi preview`, Pulumi will automatically run a type checker on your program and fail if there are any type errors. To enable automatic type checking set the [`typechecker` runtime option](https://www.pulumi.com/docs/concepts/projects/project-file/#runtime-options) in your project file to `mypy` or `pyright`.

```yaml
name: python-with-poetry-and-typechecking
runtime:
  name: python
  options:
    toolchain: poetry
    typechecker: pyright
```

## Pythonic Input Types

Pulumi has always had a focus on making infrastructure as code feel like idiomatic code. With the latest release of Pulumi, we have made it easier to work with input types in Python. Previously you had to chose between using strongly typed, but verbose, argument classes, or more idomatic dictionaries, at the cost of type hints. With the latest release of Pulumi, you now get the best of both worlds. Leveraging Python's [TypedDict types](https://peps.python.org/pep-0589/), dictionary inputs now have type hints, providing you with type safety and the flexibility of dictionaries.

This is particularly useful when working with complex data structures, such as those used in Kubernetes resources. For example, when creating a Kubernetes Deployment, you can now use a dictionary with type hints to define the spec of the deployment.

Previously, you would have had to define the deployment spec like this:

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

Now you can define a deployment using concise dictionary syntax, while still benefiting from type hints, giving you the same developer experience with auto-completion, and type-checking, but less boilerplate code:

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

The new Pythonic input types are available in the latest release of the Pulumi SDKs for [Kubernets](https://www.pulumi.com/registry/packages/kubernetes/) and [AWS](https://www.pulumi.com/registry/packages/aws/), with more providers SDKs to follow soon.

{{% notes type="info" %}}
Due to a performance issue, TypedDict based inputs are not yet available when using MyPy as the type checker. We recommend you use Pyright as the type checker while we work on resolving [this issue](https://github.com/python/mypy/issues/17231).
{{% /notes %}}

## Summary

We hope you enjoy using these new features and we look forward to hearing your feedback. If you have any questions or need help, please don't hesitate to reach out to us on [Slack](https://pulumi-community.slack.com/) or [GitHub](https://github.com/pulumi/pulumi).
