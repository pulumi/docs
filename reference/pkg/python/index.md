---
title: Python Packages
---

The Pulumi Python SDK package is used for accessing the core programming model around resources, configuration, etc.
directly:

* [Pulumi SDK (`pulumi`)](pulumi)

### Cloud Providers

Each cloud vendor has a dedicated package for deploying resources to it:

* [Amazon Web Services (`pulumi_aws`)](pulumi_aws)
* [Microsoft Azure (`pulumi_azure`)](pulumi_azure)
* [Google Cloud Platform (`pulumi_gcp`)](pulumi_gcp)

### Helper Libraries

These libraries help with common cloud programming patterns and practices:

* [Random (`pulumi_random`)](pulumi_random): utilities for generating random values within Pulumi's object model
