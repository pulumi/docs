---
title: "Python"
---

> **Note:** Pulumi currently only supports Python 2.7.  This is a temporary limitation and Pulumi has been authored to support Python 3.  We just haven't tested it enough to feel good telling people to try it out.  If this is important to you, shoot us a note, and we'd be happy to get it ready for you.

## Getting Started

The fastest way to get started with Pulumi Python is by using a template.  From the directory in which you'd like to create a new project:

```
$ pulumi new python
Your project was created successfully.
```

This will leave behind a `Pulumi.yaml` file, containing some minimal metadata about your project (including a name and description which you may wish to change), a `requirements.txt` file, where you will specify your dependencies (see #pypi-packages below), and a `__main__.py` file, containing your program.

> **Note:** Although the template uses a very simple package structure, by placing `__main__.py` in the root directory, Pulumi fully supports [properly modularized Python programs](http://docs.python-guide.org/en/latest/writing/structure/) and `setup.py` files.  This is important if you ever decide to turn your Pulumi program into a library.

## Using Pulumi PyPI Packages {#pypi-packages}

It is not required, but we recommend using [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for repeatable installations that work no matter your operating system.

```
$ virtualenv .
$ . ./bin/activate
```

The first thing you'll want to do is install the Pulumi SDK package, which is listed in the template's `requirements.txt` file.

### Adding a new dependency {#packages}

The following Pulumi Python packages are available:

- [pulumi](https://pypi.org/project/pulumi/): the core Pulumi JavaScript SDK package
- [pulumi_aws](https://pypi.org/project/pulumi_aws/): the AWS resource provider package, for programming AWS directly
- [pulumi_azure](https://pypi.org/project/pulumi_azure/): the Azure resource provider package, for programming Azure directly
- [pulumi_gcp](https://pypi.org/project/pulumi_gcp/): the Google Cloud resource provider package, for programming Google Cloud directly

More packages are on their way, so please keep an eye out.  Please also let us know if there are specific packages you'd like to see sooner!
