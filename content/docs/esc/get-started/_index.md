---
title: Get started
title_tag: Get Started with Pulumi ESC (Environments, Secrets, and Configuration)
h1: Get Started with Pulumi ESC (Environments, Secrets, and Configuration)
meta_desc: Learn how to manage secrets and hierarchical configuration with Pulumi
  ESC.
menu:
  esc:
    parent: esc-home
    identifier: esc-get-started
    weight: 2
aliases:
  - /docs/pulumi-cloud/esc/get-started/
search:
  keywords:
    - esc
    - learn
    - started
    - hierarchical
    - secrets
    - configuration
    - manage
---

In a typical application or infrastructure development workflow, there's often a need to maintain multiple environments such as development, staging, and production. Each of these environments might have its own set of configuration values: API endpoints, database connection strings, third-party secrets, and more.

Hardcoding these values or keeping them inside source code is a security risk and makes managing configurations complex. [Pulumi ESC (Environments, Secrets and Configuration)](/docs/esc/) offers a centralized store to manage configuration data, plain-text data, and secrets.

In this tutorial, we’ll demonstrate how to use Pulumi ESC as well as the power of this service in managing configuration and secrets.

Before you begin, you can watch the following video which provides a high level overview of how Pulumi ESC works:

<div class="rounded-md shadow border border-gray-300 w-3/4 mx-auto my-4" style="position: relative; padding-bottom: 40.25%; height: 0; overflow: hidden;">
    <iframe
        src="//www.youtube.com/embed/JY3Cm1UUIYE?rel=0"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border:0;"
        allowfullscreen=""
        title="Pulumi ESC: Centralized secrets manager for cloud infrastructure and applications">
    </iframe>
</div>

{{< get-started-stepper >}}
