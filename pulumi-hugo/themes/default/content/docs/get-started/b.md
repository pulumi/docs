---
title_tag: Get Started with Pulumi
meta_desc: Step-by-step guides for creating, deploying, and managing infrastructure with
           Pulumi on the cloud using your favorite language.
title: Start
h1: Get started with Pulumi
no_on_this_page: true
meta_image: /images/docs/meta-images/docs-meta.png
block_external_search_index: true
---

Welcome! We're glad you chose Pulumi to help you automate your cloud infrastructure. Follow the steps below to get started with your first Pulumi project.

## Install the CLI

{{< install-pulumi >}}
{{% notes "info" %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

## Set up state management

For Pulumi to know when and how to create, read, delete, or update your cloud resources, it needs metadata called state. State needs to be stored so that the CLI can coordinate updates and read/write state when applicable.

The default experience is to use the hosted Pulumi Cloud, which takes care of the state and backend details for you and provides you with additional functionality to make managing your cloud resources easier.

<div class="note note-info">
    <div class="icon-and-line">
        <i class="fas fa-info-circle"></i>
        <div class="line"></div>
    </div>
    <div class="content">
        <p>
            You can also manage state with a manually managed object store, including AWS S3, Azure Blob Storage, Google Cloud Storage, any AWS S3 compatible server such as Minio or Ceph, or your local filesystem. For more information on self managed backends, visit our <a href="/docs/concepts/state/">managing state & backend options</a> documentation.
        </p>
    </div>
</div>

To create a Pulumi Cloud account run the `login` command, which will direct you to <a href="https://app.pulumi.com" target="_blank" rel="noopener noreferrer">https://app.pulumi.com</a> to create an account:

<div class="highlight">
    <pre class="chroma"><code class="language-bash" data-lang="bash">$ pulumi login</code></pre>
</div>

And that's it! The Pulumi Cloud backend requires no additional configuration after [installing the CLI](/docs/install/) and logging in. Pulumi offers this backend hosted online free for individuals, with [advanced tiers](/pricing/) available for teams and enterprises.

Pulumi Cloud is designed to not require your cloud credentials. Later in the guide you will configure your cloud credentials locally before creating your first resources.

> To learn more about the Pulumi Cloud backend's design, including why it doesn't need your cloud credentials, see [Pulumi Cloud Architecture](#/pulumi-cloud/-architecture).

## Install Language Runtime

Select your language:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "javascript,typescript" %}}
{{< install-node >}}
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< install-go >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

{{% choosable language "java" %}}
{{< install-java >}}
{{% /choosable %}}

{{% choosable language "yaml" %}}
{{< install-yaml >}}
{{% /choosable %}}

## Choose a starter project

Choose from a list of starter projects below to start creating infrastructure with Pulumi:

<div class="tiles flex-wrap justify-center items-stretch mt-4">
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a href="/docs/clouds/aws/get-started/create-project-b/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col text-center">
                <img class="h-10 my-3" src="/logos/tech/aws.svg" alt="AWS" />
                <p class="my-6">
                    Create, modify, and destroy infrastructure on AWS.
                </p>
                <div class="flex flex-grow justify-center align-center">
                    <div class="btn btn-secondary">Create your project &rarr;</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a href="/docs/clouds/azure/get-started/create-project-b/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col text-center">
                <img class="h-10 my-3" src="/logos/tech/azure.svg" alt="AWS" />
                <p class="my-6">
                    Create, modify, and destroy infrastructure on Azure.
                </p>
                <div class="flex flex-grow justify-center align-center">
                    <div class="btn btn-secondary">Create your project &rarr;</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a href="/docs/clouds/gcp/get-started/create-project-b/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col text-center">
                <img class="h-10 my-3" src="/logos/tech/gcp.svg" alt="AWS" />
                <p class="my-6">
                    Create, modify, and destroy infrastructure on Google Cloud.
                </p>
                <div class="flex flex-grow justify-center align-center">
                    <div class="btn btn-secondary">Create your project &rarr;</div>
                </div>
            </div>
        </a>
    </div>
    <div class="pb-4 md:pr-4 md:w-1/2">
        <a href="/docs/clouds/kubernetes/get-started/create-project-b/" class="tile h-full">
            <div class="block rounded shadow border border-gray-300 p-3 h-full flex flex-col text-center">
                <img class="h-10 my-3" src="/logos/tech/k8s.svg" alt="AWS" />
                <p class="my-6">
                    Create, modify, and destroy infrastructure on Kubernetes.
                </p>
                <div class="flex flex-grow justify-center align-center">
                    <div class="btn btn-secondary">Create your project &rarr;</div>
                </div>
            </div>
        </a>
    </div>
</div>
