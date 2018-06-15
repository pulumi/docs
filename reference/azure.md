---
title: "Azure"
---

Pulumi supports deploying programs to Azure using any of the available services in Azure.

To configure Pulumi for Azure, please [head on over to the installation page](/install/azure.html).

At the moment, you must configure all Azure programs with the `azure:environment` configuration variable.  A
reasonable value is `public`, which will become the default soon:

```bash
$ pulumi config set azure:environment public
```

Alternative values include `usgovernment`, `german`, and `china`.

The Azure provider is open source and available in the [pulumi/pulumi-azure](https://github.com/pulumi/pulumi-azure)
repo.  Full API documentation is available at [here](./pkg/nodejs/@pulumi/azure/index.html).

We also have a few interesting examples of using Azure in our examples repo:

* [Azure VM Web Server](https://github.com/pulumi/examples/tree/master/azure-js-webserver)
* [Azure Function Apps](https://github.com/pulumi/examples/tree/master/azure-ts-functions)

> More detailed documentation for Azure is on its way! In the meantime, please don't hesitate to reach us on GitHub,
> Slack, or any of the usual means, if you have any questions or comments.
