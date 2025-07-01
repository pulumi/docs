---
title_tag: "Functions"
meta_desc: Learn about the three types of functions available in Pulumi programs - provider functions, get functions, and resource methods.
title: Functions
h1: Functions
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Functions
        parent: iac-concepts
        weight: 60
        identifier: iac-concepts-functions
    concepts:
        name: Functions
        parent: Overview
        weight: 6
---

Pulumi provides three types of functions that you can use in your programs to interact with cloud resources and retrieve data from cloud providers. Understanding these different function types and when to use them is essential for writing effective Pulumi programs.

## Provider functions

**[Provider functions](/docs/iac/concepts/functions/provider-functions/)** are functions exposed in Pulumi providers that allow you to query cloud APIs to retrieve data that is not part of a resource. These functions are often used to look up information about existing cloud resources that you need in your Pulumi program.

For example, you might use a provider function to get the latest virtual machine image ID for a specific operating system.

## Get functions

**[Get functions](/docs/iac/concepts/functions/get-functions/)** are static functions available on all Pulumi resource types that allow you to reference an existing resource that is not managed by Pulumi. Unlike the `pulumi import` command which brings resources under Pulumi management, get functions simply allow you to read the properties of existing resources.

Get functions are useful when you know an unmanaged resource's identity and need to reference properties of the unmanaged resource in resources that _are_ managed by Pulumi.

For example, you might want to get a virtual network by ID and use its CIDR block in a firewall rule.

Resources accessed via get functions will never be updated or deleted by Pulumi.

## Resource methods

**[Resource methods](/docs/iac/concepts/functions/resource-methods/)** are functions attached to specific resource types that return computed values from resources you are managing with Pulumi. These methods are called on resource instances and typically provide additional derived information about that resource.

For example, some managed Kubernetes cluster resources have a resource method to return the generate Kubeconfig file.

## Choosing the right function type

- Use **provider functions** when you need to query cloud provider APIs for data or configuration
- Use **get functions** when you need to reference existing resources that aren't managed by Pulumi
- Use **resource methods** when you need to get computed values from resources you're managing with Pulumi

Understanding these distinctions will help you write more effective Pulumi programs.
