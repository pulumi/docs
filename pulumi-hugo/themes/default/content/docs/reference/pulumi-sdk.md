---
title: Pulumi SDK Reference
linktitle: SDK Reference
meta_desc: Documentation and examples for working with cloud providers and other services.
menu:
  reference:
    name: Pulumi SDK
    weight: 3
---

The Pulumi SDK defines the core types and functions you will use in your programs
common to all cloud provider libraries. The SDK works in tandem with the Pulumi CLI
and engine to perform its infrastructure as code duties, and is available as a library
in your chosen language. In addition to the core Pulumi SDK, there are additional
helper libraries for features such as policy as code.

> For a conceptual overview of how to use the primitives available in these libraries,
> please see [Architecture & Concepts]({{< relref "/docs/intro/concepts" >}}).

Choose your language runtime to view the API documentation for the Pulumi SDK:

<div class="tiles flex-wrap mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "/docs/reference/pkg/nodejs/pulumi/pulumi" >}}">
            <p class="mx-auto text-xl font-semibold link">
                Node.js
                <span class="text-xs font-light">(JavaScript, TypeScript)</span>
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/node.svg" alt="Node.js">
            <img class="h-12 mx-auto inline" src="/logos/tech/javascript.svg" alt="JavaScript">
            <img class="h-12 mx-auto inline" src="/logos/tech/typescript.svg" alt="TypeScript">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "/docs/reference/pkg/python/pulumi" >}}">
            <p class="mx-auto text-xl font-semibold link">
                Python
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/python.svg" alt="Python">
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi">
            <p class="mx-auto text-xl font-semibold link">
                Go
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/go.svg" alt="Go">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.html">
            <p class="mx-auto text-xl font-semibold link">
                .NET Core
                <span class="text-xs font-light">(C#, F#, VB)</span>
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/dot-net.svg" alt=".NET Core">
            <img class="h-12 mx-auto inline" src="/logos/tech/c-sharp.svg" alt="C#">
            <img class="h-12 mx-auto inline" src="/logos/tech/f-sharp.svg" alt="F#">
            <img class="h-12 mx-auto inline" src="/logos/tech/visual-basic.svg" alt="Visual Basic">
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="/docs/reference/pkg/java/">
            <p class="mx-auto text-xl font-semibold link">
                Java
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/java.svg" alt="Java">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="https://github.com/pulumi/pulumi-yaml/#spec">
            <p class="mx-auto text-xl font-semibold link">
                YAML
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/yaml.svg" alt="Yaml">
        </a>
    </div>
</div>
