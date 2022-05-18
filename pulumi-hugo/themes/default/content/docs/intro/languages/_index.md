---
title: Languages
meta_desc: An overview of how to use Node.js, Python, Go, .NET Core, Java, and YAML when writing cloud applications for AWS, Azure, Google Cloud, Kubernetes, etc.
menu:
  intro:
    identifier: languages
    weight: 7

aliases: ["/docs/reference/languages/"]
---

{{< get-started-note >}}

Pulumi is a multi-language infrastructure as code tool. Each language is as capable as the
other and supports the entire surface area of all of the clouds available in [Pulumi Registry](
{{< relref "/registry" >}}).

The following language runtimes are currently supported by Pulumi. Select one to learn more:

<div class="tiles flex-wrap mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "./javascript" >}}">
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
        <a class="tile p-8 pb-16 text-center" href="{{< relref "./python" >}}">
            <p class="mx-auto text-xl font-semibold link">
                Python
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/python.svg" alt="Python">
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "./go" >}}">
            <p class="mx-auto text-xl font-semibold link">
                Go
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/go.svg" alt="Go">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "./dotnet" >}}">
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
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "./java" >}}">
            <p class="mx-auto text-xl font-semibold link">
                Java
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/java.svg" alt="Java">
        </a>
    </div>
    <div class="pb-4 md:w-1/2">
        <a class="tile p-8 pb-16 text-center" href="{{< relref "./yaml" >}}">
            <p class="mx-auto text-xl font-semibold link">
                Pulumi YAML
            </p>
            <img class="h-12 mx-auto inline" src="/logos/tech/yaml.svg" alt="Pulumi YAML">
        </a>
    </div>
</div>

If your favorite language isn't listed, it may be on its way soon. Pulumi is
[open source](https://github.com/pulumi/pulumi), and it is possible
[to add your own language]({{< relref "/docs/support/faq#how-can-i-add-support-for-my-favorite-language" >}}).
For further questions, [contact us]({{< relref "/docs/support/troubleshooting#contact-us" >}}) and let us
know what you're looking for.
