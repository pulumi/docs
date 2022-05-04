---
title: Pulumi CrossCode
type: page
layout: crosscode
meta_title: Pulumi CrossCode
meta_desc: |
    Pulumi CrossCode is the underlying technology of Pulumi, providing universal infrastructure and policy as code to cloud developers and infrastructure experts.

description: |
    Pulumi CrossCode is the underlying technology of Pulumi that provides universal infrastructure and policy as code to all cloud builders, developers and infrastructure experts. CrossCode provides the universal translation layer to the Pulumi infrastructure as code engine.

    CrossCode is composed of Pulumi's open source code generation, program generation, schema, and packages software. [View on GitHub](https://github.com/pulumi/pulumi/tree/master/pkg/codegen).

capabilities:
    title: Capabilities of Pulumi CrossCode
    items:
        - title: Build infrastructure in all popular programming languages
          icon: rocketship
          icon_color: salmon
          description: |
            CrossCode enables a polyglot world where one team can write infrastructure as code components in one language and another team can consume them from another language. CrossCode supports any JVM language (Java, Scala, Kotlin, Clojure), .NET (C#, F#, PowerShell), Node.js (JavaScript, TypeScript), Go, Python, and markup languages (YAML, JSON, CUE). CrossCode components enable the sharing and reuse of well-architected building blocks that can be consumed across the organization.
          more:
            label: Read more
            href: "/docs/intro/languages"

        - title: Convert from any infrastructure as code format
          icon: gear
          icon_color: violet
          description: |
            CrossCode can translate existing infrastructure as code, such as Terraform HCL, AWS CloudFormation templates, Azure Resource Manager templates, and Kubernetes YAML, to Pulumi. This helps organizations preserve existing infrastructure as code assets but carry them forward into the future.
          more:
            label: Read more
            href: "/docs/converters"

        - title: Import infrastructure directly from any cloud
          icon: abstract-shapes
          icon_color: blue
          description: |
            CrossCode can import existing infrastructure and generate the infrastructure as code in any supported Pulumi language. This works for any infrastructure no matter if it was provisioned manually or by another infrastructure as code system.
          more:
            label: Read more
            href: "/docs/guides/adopting/import"

        - title: Enforce policy in all popular programming languages
          icon: shield
          icon_color: yellow
          description: |
            CrossCode enables Pulumi CrossGuard policy as code to be written in all popular programming languages (Java, .NET, TypeScript, Go, Python) and markup languages (YAML, JSON, CUE). Policy as code empowers organizations to enforce resource compliance through programmable guardrails.
          more:
            label: Read more
            href: "/docs/guides/crossguard"

questions:
    title: Questions?
    description: |
        Questions about Pulumi CrossCode? We're happy to help.
---
