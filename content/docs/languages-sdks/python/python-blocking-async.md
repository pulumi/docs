---
title_tag: "Blocking and Async Python with Pulumi | Languages & SDKs"
meta_desc: An overview of how to use Python with Pulumi for infrastructure as code on any cloud (AWS, Azure, Google Cloud, Kubernetes, etc.).
title: Blocking and Async
h1: Blocking and Async Python with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  languages:
    parent: python
    weight: 5
aliases:
- /python/async/
---

A Python Pulumi program runs an
[`asyncio`](https://docs.python.org/3/library/asyncio.html)) event loop to
create the resources that the Pulumi program describes---this isn't directly
visible to the Python program.

A consequence of this is that blocking calls prevent progress from being made by
the Pulumi runtime by preventing the event loop from processing asynchronous
tasks.  

The `pulumi.Output` object can be used to pass the output from both synchronous
and asynchronous calls without blocking the event loop.

For synchronous or blocking code, this should be executed on another thread
with the future result captured as a `pulumi.Output`---using `asyncio.to_thread`
and `pulumi.Output.from_input` respectively.

For asynchronous code the coroutine or other awaitable result can also be passed to `pulumi.Output.from_input` to create a `pulumi.Output` object.

## Background

As covered in [Concepts](/docs/intro/concepts), when a Pulumi program is run it creates resources and the dependencies or
connections between them. Consider the following example (taken from the Pulumi
blog article [Programming the Cloud with Python](/blog/programming-the-cloud-with-python)):

```python
import mimetypes
import os

from pulumi import export, FileAsset
from pulumi_aws import s3

web_bucket = s3.Bucket('s3-website-bucket', website={
    "index_document": "index.html"
})

content_dir = "www"
for file in os.listdir(content_dir):
    filepath = os.path.join(content_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = s3.BucketObject(file,
        bucket=web_bucket.id,
        source=FileAsset(filepath),
        content_type=mime_type)
```

Here the resources are an S3 Bucket and some number of S3 BucketObjects---one
for each file in the `www` directory. The bucket objects are told which bucket
they will be put in using the id of the bucket. This establishes the dependency
between the BucketObject and the Bucket.

The type of the bucket id is `Output[str]`. The
[`pulumi.Output`](/docs/reference/pkg/python/pulumi/#pulumi.Output) type holds a
piece of data, in this case the id of the bucket, this is not necessarily known
during the execution of the program, and is held internally within the output
object as a future---the awaitable result of an asynchronous operation.

In this way the Pulumi program can proceed and build the graph of resources
without having to wait for each resource in turn. When Pulumi is previewing a
stack the value of an output may never be known. When resources are then created
that can be done concurrently according to the dependency graph that the Pulumi
program defines.

## Blocking and Asynchronous Code

The example above, and many or most Python Pulumi programs, contains no explicit
asynchronous code. While the resources are connected using futures, the
asynchronous evaluation all happens behind the scenes.

This can cause problems both with blocking code and with explicitly asynchronous code

- Blocking code will prevent the event loop on the Pulumi program’s thread from
  pumping while the blocking code is executing
- Asynchronous code may not be executed unless it is explicitly scheduled. For example, it is
  not possible to call `asyncio.run` from within a Pulumi program because there is already an event loop running.

### Blocking Code

A Pulumi program is a single threaded Python program. This means that the
asynchronous operations on resources cannot happen while blocking code is
evaluating. For simple Pulumi programs this is not consequential, but for more
complex programs it is possible to be waiting on blocking code that causes all
progress to be stalled waiting for that blocking code to complete.

Examples of this might include calls to `requests.get`, or `subprocess.run` that are
used to collect information needed to configure the Pulumi program or provide
input from external sources.

If the result from the blocking code is used to provide the input for a
resource, then the blocking call can be wrapped into a future---in the form of a
`pulumi.Output` object---using [`pulumi.Output.from_input`](/docs/reference/pkg/python/pulumi/#pulumi.Output.from_input). This allows the following
pattern:

```python
import asyncio
import subprocess

def blocking_operation(foo: str) -> str:
  """
  An example function that calls a subprocess and captures its output
  """
  res = subprocess.run(['my-cli', foo], encoding='utf-8', capture_output=True)
  if res.returncode is not 0:
    raise Error(f'my-cli returned {res.returncode}: {res.stderr}')
  return res.stdout

# Use asyncio to call the blocking_operation function on another thread
# This returns a coroutine
mycli_coro = asyncio.to_thread(blocking_operation, 'bar')
# The coroutine is awaitable and can be converted into a pulumi.Output
mycli_output = pulumi.Output.from_input(mycli_coro)
```

If an output needs to be transformed, for example if a blocking call returns a
complex object from which a value needs to be extracted (itself as a
`pulumi.Output`) then
[`pulumi.Output.apply`](/docs/reference/pkg/python/pulumi#pulumi.Output.apply) can
be used to transform an output value

### Asynchronous Code

Explicitly async code can be used in exactly the same way---`pulumi.Output.from_input` can convert any awaitable value into a `pulumi.Output`.
To use the same example as above with an equivalent asynchronous implementation:

```python
import asyncio
import shlex

async def async_operation(foo: str) -> str:
  """
  An example async function that calls a subprocess and captures its output
  """
  proc = await asyncio.create_subprocess_shell(
    f'my-cli {shlex.quote(foo)}',
    stdout=asyncio.subprocess.PIPE
    stderr=asyncio.subprocess.PIPE)

  stdout, stderr = await proc.communicate()
		
  if proc.returncode is not 0:
    raise Error(f'my-cli returned {proc.returncode}: {stderr.decode()}')
  return stdout.decode

# Calling an async function directly (without the await keyword) returns a
# coroutine
mycli_coro = async_operation('bar')
# The coroutine is awaitable and can be converted into a pulumi.Output
mycli_output = pulumi.Output.from_input(mycli_coro)
```

## Alternatives

The examples above both use calling a local process to demonstrate a pattern that is useful in Python Pulumi programs. This applies to other blocking and async requirements too, for example if you need to call a REST API you might use `requests.get` or an async equivalent such as `httpx.AsyncClient.get`

For running other processes, you can stay entirely within the Pulumi programming model by using the [Command](/registry/packages/command) package. With this package both of the examples above can be
simplified to the following:

```python
import shlex
from pulumi_command import local

def call_my_cli(foo: str) -> Output[str]:
    """
    As example function that uses the Command package to run a local process
    """
    my_cli = local.Command('my-cli', create=f'my-cli {shlex.quote(foo)})')
    return my_cli.stdout

# The return from call_my_cli is already a pulumi.Output
mycli_output = call_my_cli('bar')
```

If the input to the function needs to be a `pulumi.Output` itself---_i.e._ if it is the result of creating another resource, or calling another command, then we can use [`pulumi.Output.concat`](/docs/reference/pkg/python/pulumi#pulumi.Output.concat) as follows:

```python
import shlex
from pulumi_command import local
import pulumi_random as random

def call_my_cli(foo: Output[str]) -> Output[str]:
    """
    As example function that uses the Command package to run a local process
    """
    my_cli = local.Command('my-cli',
        create=pulumi.Output.concat('my-cli ', foo))
    return my_cli.stdout

# Create a random value
random_string = random.RandomString("random-value")
# random_string.result is a pulumi.Output[str]
# The return from call_my_cli is already a pulumi.Output
mycli_output = call_my_cli(random_string.result)
```
