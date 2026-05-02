---
title: "Get Started with Pulumi | Pulumi"
meta_desc: Install Pulumi and deploy your first stack to AWS, Azure, Google Cloud, or Kubernetes. Open source infrastructure as code in TypeScript, Python, Go, C#, Java, or YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Get Started"
install:
    title: "Install Pulumi"
    intro: "Download and install Pulumi for your platform:"
    options_note: "Other installation options [are available](/docs/install/)."
    test_intro: "Test your new installation by running the `pulumi version` command:"
    restart_note: "If this doesn't work, you may need to restart your terminal to ensure the directory containing the `pulumi` command is on your `PATH`."

heading: "Get Started with Pulumi"
subheading: |
    Install Pulumi and deploy your first stack in minutes. Open source, and works with every major cloud.

overview:
    title: Infrastructure as Code in any Language, on any Cloud
    description: |
        Pulumi lets you build, deploy, and manage cloud infrastructure with the programming languages you already know — TypeScript, Python, Go, C#, Java, and YAML — across 170+ providers.

continue:
    title: Continue with your cloud
    description: |
        Pick your platform and follow the full step-by-step guide to deploy your first project.
    items:
        - name: AWS
          icon_class: aws-40
          link: /docs/iac/get-started/aws/
          track: aws-get-started
        - name: Azure
          icon_class: azure-40
          link: /docs/iac/get-started/azure/
          track: azure-get-started
        - name: Google Cloud
          icon_class: google-cloud-40
          link: /docs/iac/get-started/gcp/
          track: google-get-started
        - name: Kubernetes
          icon_class: kubernetes-40
          link: /docs/iac/get-started/kubernetes/
          track: kubernetes-get-started

stats:
    title: "Trusted by thousands of companies"
    description: |
        Pulumi's open source IaC engine is used by 350,000+ developers and 4,000+ companies in production.
    community:
        number: "350,000+"
        description: "Community members"
    company:
        number: "4,000+"
        description: "Companies in production"
    integration:
        number: "170+"
        description: "Cloud and service integrations"
---

## Before you begin

Pick the language you want to use. The prerequisites depend on your choice.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* A cloud account (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) or a Kubernetes cluster
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> and <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installed locally

{{% /choosable %}}

{{% choosable language "python" %}}

* A cloud account (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) or a Kubernetes cluster
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> and <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a>, or <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installed locally

{{% /choosable %}}

{{% choosable language "go" %}}

* A cloud account (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) or a Kubernetes cluster
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installed locally

{{% /choosable %}}

{{% choosable language "csharp" %}}

* A cloud account (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) or a Kubernetes cluster
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installed locally

{{% /choosable %}}

{{% choosable language "java" %}}

* A cloud account (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) or a Kubernetes cluster
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> and <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installed locally

{{% /choosable %}}

{{% choosable language "yaml" %}}

* A cloud account (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) or a Kubernetes cluster

{{% /choosable %}}

