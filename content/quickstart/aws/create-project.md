---
title: Create a New Project
weight: 5
menu:
  quickstart:
    parent: aws
    identifier: aws-create-project
---

Let's get started with a new project in a new directory.

{{< langchoose nogo >}}

<div class="language-prologue-javascript"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-javascript
```

<div class="language-prologue-typescript"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-typescript
```

<div class="language-prologue-python"></div>

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new aws-python
```

> If this is your first time running `pulumi new` (or most other `pulumi` commands), you will be prompted to login to the [Pulumi service](https://app.pulumi.com). The CLI works in tandem with the Pulumi service to deliver a reliable experience, and is free for individual use, with [additional features available for teams](https://www.pulumi.com/pricing/). Hitting enter at the prompt will open a web browser allowing you to sign in or sign up. Alternatively, you may [login]({{< relref "/reference/cli/pulumi_login.md" >}}) or [logout]({{< relref "/reference/cli/pulumi_logout.md" >}}) explicitly if you prefer. See the [FAQ]({{< relref "/reference/faq.md#can-i-use-pulumi-without-depending-on-pulumi-com" >}}) for more information.

After logging in, the CLI will proceed with walking you through creating a new project.

```
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal AWS Pulumi program)
Created project 'quickstart'

stack name: (dev)
Created stack 'dev'

aws:region: The AWS region to deploy into: (us-east-1)
Saved config
```

First, you will be asked for a project name and description. You can hit enter to accept the default values or enter a new values.

Next, you will be asked for the name of a stack. You can hit enter to accept the default value of `dev`.

> What are [projects]({{< relref "/reference/project.md" >}}) and [stacks]({{< relref "/reference/stack.md" >}})? Pulumi projects and stacks are a way to organize Pulumi code. You can consider a Pulumi Project to be analogous to a GitHub repo: a single place for code — and a Stack to be an instance of that code which has separate configuration. For instance, Project Foo may have multiple stacks for Dev, Test, Prod, or perhaps for different cloud configurations (e.g. geographic region). Please [see this guide]({{< relref "/reference/organizing-stacks-projects.md" >}}) for some best practices on organizing your Pulumi projects and stacks.

Next, you will be prompted for some configuration values for the stack.

For AWS projects, you will be prompted for the AWS region. For this guide, be sure to accept the default value of `us-east-1`.

{{% lang nodejs %}}
After some dependency installations from `npm`, you'll see some files have been generated:
{{% /lang %}}

{{% lang python %}}
After the command completes, you'll see some files have been generated:
{{% /lang %}}

- `Pulumi.yaml` defines the [project]({{< relref "/reference/project.md" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/reference/config.md" >}}) values for the [stack]({{< relref "/reference/stack.md" >}}) we initialized.
- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< langchoose nogo >}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const aws = require("@pulumi/aws");
const awsx = require("@pulumi/awsx");

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");

// Export the name of the bucket
exports.bucketName = bucket.id;
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as awsx from "@pulumi/awsx";

// Create an AWS resource (S3 Bucket)
const bucket = new aws.s3.Bucket("my-bucket");

// Export the name of the bucket
export const bucketName = bucket.id;
```

```python
import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket')

# Export the name of the bucket
pulumi.export('bucket_name',  bucket.id)
```

This Pulumi program creates an S3 bucket and exports the name of the bucket.

{{% lang python %}}
Finally, for Python, run the following commands to create a virtual environment, activate it, and install dependencies:

```bash
$ virtualenv -p python3 venv
```

```bash
$ source venv/bin/activate
```

```bash
$ pip3 install -r requirements.txt
```
{{% /lang %}}

Next, we'll deploy the stack.

{{< get-started-stepper >}}
