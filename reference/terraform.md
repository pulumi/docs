---
title: Terraform Providers
---

Pulumi is able to adapt [any Terraform Provider](https://github.com/terraform-providers) for use with Pulumi, enabling
management of any infrastructure supported by the Terraform Providers ecosystem using Pulumi programs.

Indeed, some of Pulumi's most interesting providers have been created this way, delivering access to robust,
tried-and-true infrastructure management.  The Terraform Providers ecosystem is mature and healthy, and enjoys
contributions from many cloud and infrastructure leaders across the industry, ourselves included.

Most Pulumi users don't need to know about this detail, however we are proud to be building on the work of others,
and contributing our own open source back to this vibrant ecosystem, and thought you should know.

In the event you'd like to add new providers, or understand how this integration works, please check out the
[Pulumi Terraform bridge repo](https://github.com/pulumi/pulumi-terraform).  This bridge is fully open source and
makes it easy to create new Pulumi providers out of existing Terraform Providers.
