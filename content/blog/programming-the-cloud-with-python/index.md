---
title: "Programming the Cloud with Python"
date: "2019-04-04"
meta_desc: "Python is an incredible tool for task automation, and it's rapidly pervading the industry. See how to use Pulumi and Python to automate provisioning of cloud infrastructure and delivery of applications."
authors: ["sean-gillespie"]
tags: ["Serverless","AWS","Python"]
---

Across the industry, the popularity of Python is exploding. Amongst our
own customers at Pulumi, who automate their infrastructure using Python,
we've seen the same. Stack Overflow wrote about the astounding growth
of Python in 2017:

> The term "fastest-growing" can be [hard to define
> precisely](https://xkcd.com/1102/), but we make the case that **Python
> has a solid claim to being the fastest-growing major programming
> language**.
>
> -- [David Robinson, Stack Overflow](https://stackoverflow.blog/2017/09/06/incredible-growth-python/)

TIOBE, the maintainers of a popular index of programming language
popularity, crowned Python as "[Programming Language of the Year](https://www.tiobe.com/tiobe-index/)" for 2018, based on its
meteoric rise in its index. Since Python is not a new language, what
could be driving this incredible adoption curve?

Python is, and always has been, particularly amenable to the automation
of previously-manual tasks. So much so, in fact, that books have been
written on how to [automate common tasks with Python](https://automatetheboringstuff.com/). In recent years, Python's
penchant for task automation have led to its use at the foundation of
tools now ubiquitous in the DevOps space: tools like
[Ansible](https://www.ansible.com/),
[SaltStack](https://www.saltstack.com/), and
[OpenStack](https://www.openstack.org/) are all authored primarily in
Python. It would not be a stretch to claim that Python is the language
of automation.

At Pulumi we are passionate about automating cloud infrastructure.
However, we see a major open opportunity to leverage our most powerful,
fundamental tool - the programming language - to automate our
infrastructure tasks. We love the idea of "infrastructure of code", but
we struggle with the industry's definition of "code"; it's hardly code
at all, often consisting of YAML documents, DSLs, or other,
domain-specific solutions to the task at hand. Since Python is such an
incredible tool for task automation and since its use is rapidly
pervading the industry, wouldn't it make sense to use code, to use
Python, to automate tasks as critical as the provisioning of our cloud
infrastructure and delivery of our applications?

> Delivery is not a detail, it is our job. Now is the time to apply our
> core skills to our own work. Now is the time to *engineer* our
> delivery. We divide our work between ourselves and computers: humans
> for decisions, and automation for tasks.
>
> -- [The Software Defined Delivery Manifesto](https://sdd-manifesto.org/)

## That sounds great, but what is this "Pulumi" thing?

Pulumi is an infrastructure as code tool for provisioning cloud
infrastructure and deploying applications. The key difference between
Pulumi and other tools in this space (such as Ansible, Terraform, and
AWS CloudFormation) is that Pulumi aggressively reclaims the word
"code": users of Pulumi write programs in *general purpose programing languages*
that, when run, deploy and run applications in cloud
environments, while still retaining all the known benefits of
infrastructure as code that our industry has grown accustomed to
(repeatability, resilience to failure, history and auditing, and so
on).

Pulumi is a rebellion against YAML and domain-specific
non-Turing-complete languages. We firmly believe that your
infrastructure isn't just code: *your infrastructure is software.* By
applying the same engineering discipline to your infrastructure code
that you apply to your application code, we can iterate quickly and with
confidence, leaning on things such as automated tests, code analysis
tools, and a common language. Pulumi does not generate YAML; it instead
brings the full API surface area of your cloud environment into Python,
powered by an infrastructure as code engine.

It is hard to overstate how liberating it is to write infrastructure as
code with a full general-purpose programming language at your disposal.
Below is a code snippet of a Pulumi program, written in Python, that
deploys a static website to S3:

```typescript
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

There are only 18 lines of Python code here, but this program does a
ton!

- First, we create an AWS S3 Bucket that we'll use to host our
  website from, setting the index document to
  be "index.html".
- Next, we iterate over all files in the "www" directory (using the
  standard Python for loop!
- Finally, for every file in the "www" directory, we guess its MIME
  type using the Python standard library and then create an S3
  BucketObject inside the website bucket, which uploads the file to
  S3.

This is a simple example, but it's hard to overstate how awesome it is to be able to reach into
Python's deep standard library whenever we need to. In this example we're using both the “os” and
“mimetypes” packages in the Python standard library: the first to list the files in a particular
directory and the second to guess a particular file's MIME type based on its extension and contents,
which we eventually pass directly to S3.

Remember, this code isn't performing imperative commands — like, say, your cloud provider's Python
SDK or Boto would — and instead creates a declarative resource graph that the Pulumi engine understands
how to act upon. This works for the first deployment, but more importantly, for all subsequent
incremental updates too. If we were to change the contents of one of the files on disk, Pulumi would
recognize that one of the files has changed and re-upload it, without changing the bucket or any of
the other already existing bucket objects!

## Where can I learn more?

If you'd like to try the above example out for yourself, we've put the [full code on GitHub](https://github.com/pulumi/examples/tree/master/aws-py-s3-folder).
Full instructions for installing Pulumi and deploying your own static website on S3 are in the `README`.
Don't take our word for it, though! We'd love for you to check it out and see for yourself how
great it is to reclaim the “code” in “infrastructure as code”. If you want to know more about
Pulumi and the things it can do for you, check out our [Getting Started]({{< ref "/docs/get-started" >}}) page and our Documentation for more information.

Python is the language of automation today and the future. Pulumi is the infrastructure as
code automation tool of the future. Using them both together is an incredible way to automate a
crucial job while staying entirely within a language you already know and love!
