---
title: "Testing Your Pulumi Programs"
layout: topic
date: 2021-09-30T08:18:13-05:00
draft: false
description: Explore how to test your Pulumi programs with standard tooling.
meta_desc: Explore how to test your Pulumi programs with standard tooling.
index: 5
estimated_time: 10
meta_image: meta.png
authors:
    - matt-stratton
    - laura-santamaria
tags:
    - testing
block_external_search_index: false
---

Pulumi programs are authored in a general-purpose language like TypeScript,
Python, Go, or C#. The full power of each language is available, including
access to tools and libraries for that runtime. As it happens, that includes
testing frameworks. For this activity, we're going to talk specifically about
unit tests, the bottom or foundation of the testing pyramid. In the future,
we'll add in integration tests and end-to-end tests, but we're sticking with a
simple demonstration of testing for now.

<!-- See previous note -->

When running an update, your Pulumi program talks to the Pulumi CLI to
orchestrate the deployment. The idea of unit tests is to cut this communication
channel and replace the Pulumi CLI with mocks. The mocks respond to the commands
from within the same OS process and return dummy data for each call that your
Pulumi program makes. Because mocks don’t execute any real work, unit tests run
very fast. Also, they can be made deterministic because tests don't depend on
the behavior of any external system.

The Pulumi runtime includes a mocking interface to make testing easier. It works
with the majority of our resource providers natively. For a couple others,
including Docker, we need to mock the provider itself along with the runtime. As
that's a bit more complex than we'd like to get for this unit, we're going to
pretend we're shipping our app to AWS, which doesn't require mocking of the AWS
CLI.

## Break up our code

In general, best practices for Python use the `__main__.py` file as an
entrypoint, and so we're going to break up our program into smaller files.

Since we're going to ship our app to AWS, we're going to have to do a lot more
to wire up our app for a cloud provider. We need virtual gateways and subnets,
security groups, access roles... In short, there's a lot to do. We can use
[_test-driven development
(TDD)_]({{< relref "docs/guides/testing#unit-testing">}}) to build it out slowly
without necessarily having an AWS account ready to go. As such, we're going to
start with a stub and build from there.

Create a new file called `my_first_app.py` and copy the following code into it:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
import json
import pulumi
import pulumi_aws as aws

stack = pulumi.get_stack()
config = pulumi.Config()
registry_org = "pulumi"
registry_stub = "tutorial-pulumi-fundamentals"
frontend_port = config.require_int("frontend_port")
backend_port = config.require_int("backend_port")
mongo_port = config.require_int("mongo_port")
mongo_host = config.require("mongo_host")
database = config.require("database")
node_environment = config.require("node_environment")

######################
# Set up your images #
######################

# grab our backend image
backend_image_name = "backend"
backend_image_path = f'{registry_org}/{registry_stub}-{backend_image_name}:main'

# grab our frontend image
frontend_image_name = "frontend"
frontend_image_path = f'{registry_org}/{registry_stub}-{frontend_image_name}:main'

# grab the database image
database_image_name = "database"
database_image_path = f'{registry_org}/{registry_stub}-{database_image_name}:main'

#####################################
# Set up some overall AWS resources #
#####################################

# Create an ECS cluster to run container-based services.
cluster = aws.ecs.Cluster('my-cluster')

# Create a VPC and a public subnet
# Create a gateway to the web for the VPC
# Associate our gateway with our VPC to allow our app to communicate with the
# greater internet
# Create a SecurityGroup that permits HTTP ingress and unrestricted egress.
# Add the proper roles and role policies for the tasks
# 1. IAM Role for Fargate for service execution
# 2. IAM Role for Fargate to manage tasks

#############################
# Set up MongoDB resources. #
#############################

# Create Mongo's target group
# Create a load balancer for MongoDB
# Create a task definition for the mongo instance.
# Launch our Mongo service on Fargate, using our configs and load balancers
# Create a special endpoint for the Mongo backend

###################################################
# Set up our application, front-end and back-end. #
###################################################

# Create a load balancer to listen for HTTP traffic.
# Create the Target Group
# And add the listeners for the Load Balancer

#########################################
# Add some exports for us to use later. #
#########################################
```

{{% /choosable %}}

In this code, we've got a lot of comments that indicate what will eventually get
built. We've got a couple things in there we can test, though, which is what we
will focus on here.

Replace the contents of {{% langfile %}} with the following code:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
import pulumi
import my_first_app
```

{{% /choosable %}}

When we run our test framework, we run it against the {{% langfile %}} file, so
adding our code as an import allows us to ensure it's tested. Let's go write
some unit tests!

## Add mocks

The `pytest` library is one of the most popular libraries for Python unit
testing, so we're going to use that library here. If you're trying to reduce
dependencies, you can also use the built-in `unittest` library, which will be
fairly similar to this code.

Before you go too far, install `pytest`:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```shell
$ pip install pytest
```

{{% /choosable %}}

Let’s add the following code to mock the external calls to the Pulumi CLI. In
the interest of time for this tutorial, we're going to only mock one resource
that we'll need for the eventual application deployment: the ECS cluster.

Create a file for the test code called `test_my_first_app.py`. Add the following
code to it:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
import pulumi


class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        outputs = args.inputs
        return [args.name + '_id', outputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}


pulumi.runtime.set_mocks(MyMocks())
```

{{% /choosable %}}

We need to set the configuration the mocked Pulumi calls expect since we set
them as required. Add this code after the declaration of the `MyMocks()` class:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
pulumi.runtime.set_all_config({
  "project:backend_port": "3000",
  "project:database": "cart",
  "project:frontend_port": "3001",
  "project:mongo_host": "mongodb://mongo:27017",
  "project:mongo_port": "27017",
  "project:node_environment": "development"
})
```

{{% /choosable %}}

<!-- TODO: This absolutely violates PEP 8. We need to explain this better. -->
Then, we need to import our `my_first_app` module. Since the Pulumi CLI needs to
be mocked before the main module can run, we have to import it partway through
the test file. Add this line after the configuration details:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
import my_first_app
```

{{% /choosable %}}

## Write tests

Now, we're going to create a testing class and populate some tests. Add the
following code after the import of our main module:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
# Note that this test is testing inputs, not outputs.
@pulumi.runtime.test
def test_myfirstapp_tags():
    def check_tags(args):
        urn, tags = args
        assert tags, f'instance {urn} must have tags'
        assert 'Name' in tags, f'instance {urn} must have a name tag'

    return pulumi.Output.all(my_first_app.cluster.urn, my_first_app.cluster.tags).apply(check_tags)
```

{{% /choosable %}}

So now your overall `test_my_first_app.py` file should match this code:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
import pulumi


class MyMocks(pulumi.runtime.Mocks):
    def new_resource(self, args: pulumi.runtime.MockResourceArgs):
        outputs = args.inputs
        return [args.name + '_id', outputs]

    def call(self, args: pulumi.runtime.MockCallArgs):
        return {}


pulumi.runtime.set_mocks(MyMocks())

pulumi.runtime.set_all_config({
  "project:backend_port": "3000",
  "project:database": "cart",
  "project:frontend_port": "3001",
  "project:mongo_host": "mongodb://mongo:27017",
  "project:mongo_port": "27017",
  "project:node_environment": "development"
})

import my_first_app


# Note that this test is testing inputs, not outputs.
@pulumi.runtime.test
def test_myfirstapp_tags():
    def check_tags(args):
        urn, tags = args
        assert tags, f'instance {urn} must have tags'
        assert 'Name' in tags, f'instance {urn} must have a name tag'

    return pulumi.Output.all(my_first_app.cluster.urn, my_first_app.cluster.tags).apply(check_tags)
```

{{% /choosable %}}

To run your tests, run the following command:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```bash
$ pytest
```

{{% /choosable %}}

You will get output like this:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```bash
============================ test session starts =============================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/<user>/my-first-app
collected 1 item

test_my_first_app.py F                                                   [100%]

================================== FAILURES ==================================
____________________________ test_myfirstapp_tags ____________________________

args = ['urn:pulumi:stack::project::pulumi:pulumi:Stack$aws:ecs/cluster:Cluster::my-cluster', None]

    def check_tags(args):
        urn, tags = args
>       assert tags, f'instance {urn} must have tags'
E       AssertionError: instance urn:pulumi:stack::project::pulumi:pulumi:Stack$aws:ecs/cluster:Cluster::my-cluster must have tags
E       assert None

test_my_first_app.py:40: AssertionError
=============================== short test summary info ======================
FAILED test_my_first_app.py::test_myfirstapp_tags - AssertionError: instance urn:pulumi:stack::project::pulumi:pulumi:Stack$aws:ecs/cluster:Cluster::my-cluster must have tags
============================ 1 failed, 0 warnings in 1.66s ===================
```

{{% /choosable %}}

That's exactly what we want! If you examine the code in `my_first_app.py`,
you'll find that we don't actually have any tags defined on the cluster. Let's
go back and add some. Add the following code to the `Cluster` instantiation:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
cluster = aws.ecs.Cluster('my-cluster',
                          tags={
                              'usecase': 'tag',
                          })
```

{{% /choosable %}}

There were two tests we declared, though. If we rerun our tests, we'll get a new
error:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```bash
FAILED test_my_first_app.py::test_myfirstapp_tags - AssertionError: instance urn:pulumi:stack::project::pulumi:pulumi:Stack$aws:ecs/cluster:Cluster::my-cluster must have a name tag
```

{{% /choosable %}}

So let's make a name tag:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```python
cluster = aws.ecs.Cluster('my-cluster',
                          tags={
                              'Name': 'tag',
                          })
```

{{% /choosable %}}

Note that we capitalize the term `Name` because that's AWS's standard.

Now run your tests with `pytest`. You'll get the following output:

{{< chooser language "python" / >}}

{{% choosable language python %}}

```bash
============================ test session starts =============================
platform darwin -- Python 3.9.6, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /Users/<user>/my-first-app
collected 1 item

test_my_first_app.py .                                                   [100%]

============================ 1 passed, 0 warnings in 0.22s ===================
```

{{% /choosable %}}

And there we go! Our first test that we've written helped us adjust our new AWS
Pulumi code for our cloud-based deployment. We'll eventually build out this
application to explore more about testing with Pulumi, but this tutorial should
help you get down the road on this pathway.

---

Congratulations! You've finished the Pulumi in Practice pathway! In this
pathway, you learned all about stacks, outputs, and stack references so you can
work in multiple environments. You also learned about secrets in Pulumi and
testing with standard third-party frameworks.

Go build new things, and watch this space for more learning experiences on
Pulumi!
