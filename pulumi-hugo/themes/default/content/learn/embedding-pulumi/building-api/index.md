---
title: "Building a Custom API"
layout: topic
date: 2021-12-15
draft: false
description: |
    Build your first encapsulation of the Pulumi CLI with Pulumi's Automation
    API.
meta_desc: |
    Build your first encapsulation of the Pulumi CLI with Pulumi's Automation
    API.
index: 1
estimated_time: 10
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - learn
block_external_search_index: false
---

The Automation API allows us to create an API for our current infrastructure. Having a basic set of commands that we can invoke programmatically via an interface is a nice touch, but it may not seem like much of an improvement. However, this kind of interface enables uses like a self-service web portal for others to provision infrastructure, a set of happy-path infrastructure that can all be deployed via chatbot or via other programs, or even as part of automated responses to an incident page. As engineers, we love to provision our stacks via a quick call, and we also like to make it easy for others to provision the same infrastructure with a simpler interface. Our program here is a placeholder for these more advanced uses. Let's build the custom API for our tiny program.

## Scaffolding

Let's start out with scaffolding the code by importing the right libraries and doing a bit of conversion of our basic Pulumi commands (create, configure, refresh, destroy, and update) to code with the automation API library. We'll be working in the `infra` directory at this point.

First, clear out the {{< langfile >}} file in the `infra` directory; from here on out, it's just there as a placeholder for the module itself in Python.

Next, add a file called `basic.py` into the `infra` directory with this code in it:

{{< code-filename file="learn-auto-api/infra/basic.py" >}}

```python {.line-numbers}
"""A Python Pulumi program"""
import json
import os.path
import subprocess
import sys
from pulumi import log
from pulumi import automation as auto


def set_context(org, project, stackd, dirname, req):
    config_obj = {
        'org': org,
        'project': project,
        'stack': stackd,
        'stack_name': auto.fully_qualified_stack_name(org, project, stackd),
        'dirname': dirname,
        'request': req
    }
    return config_obj


def find_local(dirname):
    return os.path.join(os.path.dirname(__file__), dirname)


def spin_venv(dirname):
    work_dir = find_local(dirname)
    try:
        log.info("Preparing a virtual environment...")
        subprocess.run(
            ["python3", "-m", "venv", "venv"],
            check=True,
            cwd=work_dir,
            capture_output=True
        )
        subprocess.run(
            [os.path.join("venv", "bin", "python3"), "-m", "pip", "install", "--upgrade", "pip"],
            check=True,
            cwd=work_dir,
            capture_output=True
        )
        subprocess.run(
            [os.path.join("venv", "bin", "pip"), "install", "-r", "requirements.txt"],
            check=True,
            cwd=work_dir,
            capture_output=True
        )
        log.info("Successfully prepared virtual environment")
    except Exception as e:
        log.error("Failure while preparing a virtual environment:")
        raise e


def set_stack(context_var):
    try:
        log.info("Initializing stack...")
        stackd = auto.create_or_select_stack(
            stack_name=context_var['stack_name'],
            project_name=context_var['project'],
            work_dir=find_local(context_var['dirname'])
        )
        log.info("Successfully initialized stack")
        return stackd
    except Exception as e:
        log.error("Failure when trying to initialize the stack:")
        raise e


def configure_project(stackd, context_var):
    try:
        log.info("Setting project config...")
        stackd.set_config("request", auto.ConfigValue(value=f"{context_var['request']}"))
        log.info("Successfully set project config")
    except Exception as e:
        log.error("Failure when trying to set project configuration:")
        raise e


def refresh_stack(stackd):
    try:
        log.info("Refreshing stack...")
        stackd.refresh(on_output=print)
        log.info("Successfully refreshed stack")
    except Exception as e:
        log.error("Failure when trying to refresh stack:")
        raise e


def destroy_stack(stackd, destroy=False):
    if destroy:
        try:
            log.info("Destroying stack...")
            stackd.destroy(on_output=print)
            log.info("Successfully destroyed stack")
            return
        except Exception as e:
            log.error("Failure when trying to destroy stack:")
            raise e
    else:
        log.info("You need to set destroy to true. Stack still up.")
        return


def update_stack(stackd):
    try:
        log.info("Updating stack...")
        up_res = stackd.up(on_output=print)
        log.info("Successfully updated stack")
        log.info(f"Summary: \n{json.dumps(up_res.summary.resource_changes, indent=4)}")
        for output in up_res.outputs:
            val_out = up_res.outputs[f'{output}'].value
            log.info(f"Output: {val_out}")
        return up_res.outputs
    except Exception as e:
        log.error("Failure when trying to update stack:")
        raise e


if __name__ == "__main__":
    args = sys.argv[1:]
    context = set_context(
        org="<org>",
        project="burner-program-2",
        stackd="dev",
        dirname="api",
        request="timezone"
    )
    spin_venv(context["dirname"])
    stack = set_stack(context_var=context)
    configure_project(stackd=stack, context_var=context)
    refresh_stack(stackd=stack)
    if len(args) > 0:
        if args[0] == "destroy":
            destroy_stack(stackd=stack, destroy=True)
    update_stack(stackd=stack)
```

{{< /code-filename >}}

In that file, change the `<org>` value on line 122 to your own personal org on Pulumi (it should be your username).

We've made the most simple program you can make with the Automation API: a procedure for creating, updating, or deleting a specific stack. It's taking each step that the Pulumi CLI would take into its own function using the Automation API to define the actual actions. We'll use this scaffolding to ensure we can log at each step and raise errors properly (more on that later).

Here's your new directory structure:

```
learn-auto-api/
    api/
        time/
            time_me.py
        venv/
            ...
        .gitignore
        __main__.py
        burner.py
        Pulumi.yaml
        requirements.txt
    infra/
        venv/
            ...
        .gitignore
        __main__.py
        basic.py
        Pulumi.yaml
        requirements.txt
```

### Considerations with Destroy

The basics of such an API is taking the commands we call in the CLI and generalizing them to an interface that can be easily programmed. We also, however, would like to have the ability to destroy a stack locally as we'd like any future work locally to go through the API as well, but we really don't want any automation to be able to destroy a stack without human approval (unless perhaps it's an ephemeral stack for smoke testing). That's the part on lines 90 and 133 that defines a `destroy` variable, or flag, that can enable the destroy workflow.

## Automating Commands

Now that we have that basic layout, let's make our API and set it up to run! In the root of the project, add the following file as `infra_api.py`:

{{< code-filename file="learn-auto-api/infra_api.py" >}}

```python {.line-numbers}
import json
import os.path
import falcon
from wsgiref.simple_server import make_server
from infra import basic as infra

api = application = falcon.App()
api_path = os.path.abspath("api")


def spin_up_program(requested):
    context = infra.set_context(
        org='<org>',
        project='burner-program-2',
        stackd='dev',
        dirname=f'{api_path}',
        req=f'{requested}'
    )
    infra.spin_venv(context['dirname'])
    stack = infra.set_stack(context_var=context)
    infra.configure_project(stackd=stack, context_var=context)
    infra.refresh_stack(stackd=stack)
    results = infra.update_stack(stackd=stack)
    infra.destroy_stack(stackd=stack, destroy=True)
    return results


# Home resource
class Home(object):
    def on_get(self, req, resp):
        payload = {
            "response": "OK"
        }
        resp.text = json.dumps(payload)
        resp.status = falcon.HTTP_200


# Check things resource
class Checker(object):
    def on_get(self, req, resp):
        payload = {
            "response": "hello, world"
        }
        resp.text = json.dumps(payload)
        resp.status = falcon.HTTP_200

    def on_get_time(self, req, resp):
        time_zone = spin_up_program('timezone')
        payload = {
            'response': f'{time_zone}'
        }
        resp.text = json.dumps(payload)
        resp.status = falcon.HTTP_200

    def on_get_location(self, req, resp):
        location = spin_up_program('location')
        payload = {
            'response': f'{location}'
        }
        resp.text = json.dumps(payload)
        resp.status = falcon.HTTP_200

    def on_get_weather(self, req, resp):
        pass


# Instantiation
home = Home()
checker = Checker()

# Routes
api.add_route('/', home)
api.add_route('/weather', checker, suffix='weather')
api.add_route('/time', checker, suffix='time')
api.add_route('/location', checker, suffix='location')


if __name__ == '__main__':
    with make_server('', 8000, api) as httpd:
        print('Serving on port 8000...')
        # Serve until process is killed
        httpd.serve_forever()
```

{{< /code-filename >}}

Change the `<org>` value on line 13 to your personal org on Pulumi (it should be your username).

Here's what the directory structure is now:

```
learn-auto-api/
    api/
        time/
            time_me.py
        venv/
            ...
        .gitignore
        __main__.py
        burner.py
        Pulumi.yaml
        requirements.txt
    infra/
        venv/
            ...
        .gitignore
        __main__.py
        basic.py
        Pulumi.yaml
        requirements.txt
    infra_api.py
```

Lines 28 on in `infra_api.py` is all Falcon, a lightweight WSGI framework for REST APIs. But the part that we're really interested in from a Pulumi standpoint is on lines 11 to 25. Each endpoint that returns data from our "datacenter" calls that function and returns the data to the endpoint.

Now we've got some endpoints we can call. We've got a few considerations to take into account in the next module before we can start building with this code.
