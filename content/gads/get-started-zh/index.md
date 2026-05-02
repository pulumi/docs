---
title: "开始使用 Pulumi | Pulumi"
meta_desc: 安装 Pulumi 并将您的第一个堆栈部署到 AWS、Azure、Google Cloud 或 Kubernetes。使用 TypeScript、Python、Go、C#、Java 或 YAML 的开源基础设施即代码。
layout: gads-get-started
block_external_search_index: true
cta_label: "立即开始"
install:
    title: "安装 Pulumi"
    intro: "为您的平台下载并安装 Pulumi："
    options_note: "[查看](/docs/install/) 其他安装选项。"
    test_intro: "运行 `pulumi version` 命令测试新安装："
    restart_note: "如果不起作用，您可能需要重新启动终端，以确保包含 `pulumi` 命令的目录已在您的 `PATH` 中。"

heading: "开始使用 Pulumi"
subheading: |
    安装 Pulumi 并在几分钟内部署您的第一个堆栈。开源，并支持所有主流云平台。

overview:
    title: 任何语言、任何云的基础设施即代码
    description: |
        Pulumi 让您可以使用已熟悉的编程语言（TypeScript、Python、Go、C#、Java 和 YAML）在 170 多个提供商上构建、部署和管理云基础设施。

continue:
    title: 继续您的云之旅
    description: |
        选择您的平台，按照完整的分步指南部署您的第一个项目。
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
    title: "受到数千家公司的信赖"
    description: |
        Pulumi 的开源 IaC 引擎已被超过 350,000 名开发者使用，4,000 多家公司将其用于生产环境。
    community:
        number: "350,000+"
        description: "社区成员"
    company:
        number: "4,000+"
        description: "生产环境中的用户"
    integration:
        number: "170+"
        description: "云和服务集成"
---

## 开始之前

选择您要使用的语言。前提条件取决于您的选择。

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* 云账户（<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>）或 Kubernetes 集群
* 本地安装 <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> 和 <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a>

{{% /choosable %}}

{{% choosable language "python" %}}

* 云账户（<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>）或 Kubernetes 集群
* 本地安装 <a href="https://www.python.org/downloads/" target="_blank">Python</a> 和 <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>、<a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> 或 <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a>

{{% /choosable %}}

{{% choosable language "go" %}}

* 云账户（<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>）或 Kubernetes 集群
* 本地安装 <a href="https://go.dev/doc/install" target="_blank">Go</a>

{{% /choosable %}}

{{% choosable language "csharp" %}}

* 云账户（<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>）或 Kubernetes 集群
* 本地安装 <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a>

{{% /choosable %}}

{{% choosable language "java" %}}

* 云账户（<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>）或 Kubernetes 集群
* 本地安装 <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> 和 <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a>

{{% /choosable %}}

{{% choosable language "yaml" %}}

* 云账户（<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>）或 Kubernetes 集群

{{% /choosable %}}

