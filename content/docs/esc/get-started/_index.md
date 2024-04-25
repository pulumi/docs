---
title: Get started
title_tag: Get Started with Pulumi ESC (Environments, Secrets, and Configuration)
h1: Get Started with Pulumi ESC (Environments, Secrets, and Configuration)
meta_desc: Learn how to manage secrets and hierarchical configuration with Pulumi.
menu:
  pulumiesc:
    identifier: esc-get-started
    weight: 1
aliases:
  - /docs/pulumi-cloud/esc/get-started/
---

In a typical application or infrastructure development workflow, there's often a need to maintain multiple environments such as development, staging, and production. Each of these environments might have its own set of configuration values: API endpoints, database connection strings, third-party secrets, and more.

Hardcoding these values or keeping them inside source code is a security risk and makes managing configurations complex. [Pulumi ESC (Environments, Secrets and Configuration)](/docs/esc/) offers a centralized store to manage configuration data, plain-text data, and secrets.

In this tutorial, we’ll demonstrate how to use Pulumi ESC as well as the power of this service in managing configuration and secrets.

{{< get-started-stepper >}}
