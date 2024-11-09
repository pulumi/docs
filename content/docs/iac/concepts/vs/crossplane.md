---
title_tag: "Crossplane"
meta_desc: Learn about the major differences between Pulumi and configuration management tools like Chef, Puppet, Ansible, Salt, and more.
title: Crossplane
h1: Crossplane vs Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Crossplane
        parent: iac-concepts-compare
        weight: 9
    concepts:
        parent: vs
        weight: 10
aliases:
- /docs/reference/vs/crossplane/
- /docs/intro/vs/crossplane/
- /docs/concepts/vs/crossplane/
---

<style>
    main table {
        font-size: 0.94em;
    }

    main table th,
    main table td {
        width: 33.3%;
    }
</style>

Choosing the right infrastructure as code tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We've created this document to help you understand how Pulumi compares with Crossplane.

## What is Crossplane?

## Pulumi vs. Crossplane: Similarities {#similarities}

## Pulumi vs. Crossplane: Key Differences {#differences}

### Feature Comparisons

| Feature | Pulumi | Crossplane |
| ------- | ------ | -------------- |
| [State Management](#state) | Uses state file to manage resources. | State stored as custom Kubernetes resources in the ETCO of a cluster. |
| [Multi-Language Support](#language) | supports multiple general purpose languages. | YAML only |
| [Drift Protection](#drift-detection) | Can automatically detect and remediate with the use of Deployments | Can do automatic drift detection and remediation |
| [Preview Changes](#preview-changes) | Yes | No |
| [Platform Flexibility](#platform-flexibility) | Platform agnostic | Kubernetes only |

{{< get-started >}}

### State Management {#state}

For more information on how Pulumi manages state, or using alternative backends, see [State and Backends](/docs/concepts/state/).

### Multi-Language Support {#language}

With Pulumi, you're able to use general-purpose programming languages like Python, Go, TypeScript, and C#, which not only allows you to manage complexity by using familiar programming constructs like loops, conditionals, functions, and classes, but also simplifies common configuration tasks like string interpolation or array manipulation that are awkward to express with CloudFormation intrinsic functions. First-class support for languages also means you can take full advantage of the entire ecosystem of your language of choice. For more information, see [Languages](/docs/languages-sdks/).

### Drift Detection {#drift-detection}

### Preview Changes {#preview-changes}

### Platform Flexibility {#platform-flexibility}
