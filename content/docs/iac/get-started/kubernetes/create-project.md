---
title_tag: Create a New Project | Kubernetes
title: Create a new project
h1: "Create a new project"
meta_desc: This page provides an overview of how to create a new Kubernetes + Pulumi project.
weight: 4
menu:
    iac:
        name: Create a project
        identifier: kubernetes-get-started.create-project
        parent: kubernetes-get-started
        weight: 4
aliases:
    - /docs/quickstart/kubernetes/create-project/
---

A [project](/docs/iac/concepts/projects) is a program written in your chosen language that defines a collection of cloud resources. Create a directory for your first one, change to it, and initialize the project with `pulumi new`:

{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-csharp
```

{{% /choosable %}}
{{% choosable language java %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-java
```

{{% /choosable %}}
{{% choosable language yaml %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-yaml
```

{{% /choosable %}}

{{< cli-note >}}

Pulumi walks you through creating the project and its first [stack](/docs/iac/concepts/stacks). A stack is an instance of your project and you may have many of them — like `dev`, `staging`, and `prod` — each with its own configuration settings. Hit Enter to accept the defaults.

{{% choosable language typescript %}}

After some dependency installations from `npm`, the project and stack will be ready.

{{% /choosable %}}
{{% choosable language "python,go,csharp,java,yaml" %}}

After the command completes, the project and stack will be ready.

{{% /choosable %}}

{{< get-started-stepper >}}
