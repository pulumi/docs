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

The first thing you'll want to do is install the Pulumi SDK package.  This is listed in the template's `requirements.txt` file.

> **Note:** As a next step, you'd normally just run `pip install -r requirements.txt`, however, because Pulumi is still in Private Beta, packages aren't publically available on PyPI yet.  As a result, a few extra gestures are required.  As soon as Pulumi is public, all packages will be too.

We recommend using [`virtualenv`](http://docs.python-guide.org/en/latest/dev/virtualenvs/) for repeatable installations that work no matter your operating system.  Pulumi will function just fine if you choose not to, however for the instructions immediately below assume you are using it.  From your Pulumi program root, simply run:

```
$ virtualenv .
$ . ./bin/activate
```

The only thing special while Pulumi is still private is that you must pass an `--extra-index-url` to `pip`, so that it knows how to download Pulumi packages:

```
$ pip install \
    --extra-index-url https://${PULUMI_ACCESS_TOKEN}@pypi.pulumi.com/simple \
    -r requirements.txt
```

The `PULUMI_ACCESS_TOKEN` is your access token from the Pulumi Console found on [your Account page](https://pulumi.com/account).  After running installing the packages, you're ready to go!

> **Note:** If you see an HTTP 403 Forbidden error, or you see an error that says "No matching distribution found for pulumi>=0.11.0", then you have not correctly specified the `--extra-index-url` and/or have used an incorrect Pulumi access token.  Double check both and try again.  If it still doesn't work, please let us know.

### Adding a new dependency {#packages}

The following Pulumi Python packages are available:

- `pulumi`: the core Pulumi JavaScript SDK package
- `pulumi_aws`: the AWS resource provider package, for programming AWS directly
- `pulumi_azure`: the Azure resource provider package, for programming Azure directly
- `pulumi_kubernetes`: the Kubernetes resource provider package, for programming Kubernetes directly

More packages are on their way, so please keep an eye out.  Please also let us know if there are specific packages you'd like to see sooner!
