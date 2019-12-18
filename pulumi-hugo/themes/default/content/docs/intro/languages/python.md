---
title: "Python"
meta_desc: An overview of how to use Python when writing cloud applications for any
           Cloud Provider (AWS, Azure, GCE, Kubernetes, etc.).
menu:
  intro:
    parent: languages
    weight: 2

aliases: ["/docs/reference/python/"]
---

Pulumi supports programs written in Python 3.

> **Note:** As of Pulumi 0.16.4, we have removed support for Python 2.7, and only support Python 3.6 or greater. You must
> have installed Python 3.6 prior to running Pulumi programs, or you will likely see syntax errors - Pulumi makes use of
> new Python syntax that is not backwards-compatible with Python 2. Older Pulumi versions did support Python 2.7.

<a href="https://www.python.org/downloads/" target="_blank"><button class="button primary small">INSTALL PYTHON</button></a>

## Getting Started

The fastest way to get started with Pulumi Python is by using a template.  From an empty directory in which you'd like to create a new project:

```
$ mkdir myproject && cd myproject
$ pulumi new python
```

This will leave behind a `Pulumi.yaml` file, containing some minimal metadata about your project (including a name and description which you may wish to change), a `requirements.txt` file, where you will specify your dependencies (see #pypi-packages below), and a `__main__.py` file, containing your program.

> **Note:** Although the template uses a very simple package structure, by placing `__main__.py` in the root directory, Pulumi fully supports [properly modularized Python programs](http://docs.python-guide.org/en/latest/writing/structure/) and `setup.py` files.  This is important if you ever decide to turn your Pulumi program into a library.
<br />
> **Note:** Pulumi currently expects the `python` executable to refer to a Python of version 3.6 or above. This is
> usually not the case when running outside of a virtual environment. To work around around this and explicitly ask
> Pulumi to run your program using `python3` you can set the `PULUMI_PYTHON_CMD` environment variable to `python3`. This
> will be addressed in future versions of Pulumi.

## Using Pulumi PyPI Packages {#pypi-packages}

It is not required, but we recommend using [`pipenv`](https://pipenv.readthedocs.io/en/latest/) for repeatable installations that work no matter your operating system.

```
$ pipenv --python 3
$ pipenv install
$ pipenv shell
```

`pipenv shell` launches a subshell with your virtual environment already activated. We highly recommend using virtual
environments to isolate the dependencies of your projects and ensure reproducibility between machines.

### Adding a new dependency {#packages}

The following Pulumi Python packages are available:

- [pulumi](https://pypi.org/project/pulumi/): the core Pulumi Python SDK package
- [pulumi_aws](https://pypi.org/project/pulumi_aws/): the AWS resource provider package, for programming AWS directly
- [pulumi_azure](https://pypi.org/project/pulumi_azure/): the Azure resource provider package, for programming Azure directly
- [pulumi_gcp](https://pypi.org/project/pulumi_gcp/): the Google Cloud resource provider package, for programming Google Cloud directly
- [pulumi_kubernetes](https://pypi.org/project/pulumi_kubernetes/): The Kubernetes resource provider package, for programming Kubernetes directly.
- [pulumi_vsphere](https://pypi.org/project/pulumi-vsphere/): The VSphere resource provider package, for programming VSphere directly.
- [pulumi_openstack](https://pypi.org/project/pulumi-openstack/): The OpenStack resource provider package, for programming OpenStack directly.
- [pulumi_random](https://pypi.org/project/pulumi-random/): The Random resource provider package, for generating random strings, numbers, and other things while integrating nicely with the Pulumi programming model.

More packages are on their way, so please keep an eye out.  Please also let us know if there are specific packages you'd like to see sooner!
