---
title: "Начните работу с Pulumi | Pulumi"
meta_desc: Установите Pulumi и разверните свой первый stack в AWS, Azure, Google Cloud или Kubernetes. Open source инфраструктура как код на TypeScript, Python, Go, C#, Java или YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Начать"
install:
    title: "Установите Pulumi"
    intro: "Скачайте и установите Pulumi для вашей платформы:"
    options_note: "Другие варианты установки [доступны здесь](/docs/install/)."
    test_intro: "Проверьте установку, выполнив команду `pulumi version`:"
    restart_note: "Если команда не работает, возможно, нужно перезапустить терминал, чтобы каталог с командой `pulumi` оказался в `PATH`."

heading: "Начните работу с Pulumi"
subheading: |
    Установите Pulumi и разверните свой первый stack за минуты. Open source, работает с любым крупным облаком.

overview:
    title: Инфраструктура как код на любом языке, в любом облаке
    description: |
        Pulumi позволяет создавать и разворачивать облачную инфраструктуру и управлять ею на знакомых вам языках программирования — TypeScript, Python, Go, C#, Java и YAML — с более чем 170 провайдерами.

continue:
    title: Продолжите с выбранным облаком
    description: |
        Выберите платформу и следуйте полному пошаговому руководству, чтобы развернуть свой первый проект.
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
    title: "Нам доверяют тысячи компаний"
    description: |
        Open-source IaC-движок от Pulumi используют более 350 000 разработчиков и более 4 000 компаний в продакшене.
    community:
        number: "350 000+"
        description: "Участников сообщества"
    company:
        number: "4 000+"
        description: "Компаний в продакшене"
    integration:
        number: "170+"
        description: "Интеграций облаков и сервисов"
---

## Перед началом

Выберите язык, который хотите использовать. Требования зависят от выбора.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Облачный аккаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) или кластер Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> и <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a>, установленные локально

{{% /choosable %}}

{{% choosable language "python" %}}

* Облачный аккаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) или кластер Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> и <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> или <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a>, установленные локально

{{% /choosable %}}

{{% choosable language "go" %}}

* Облачный аккаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) или кластер Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a>, установленный локально

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Облачный аккаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) или кластер Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a>, установленный локально

{{% /choosable %}}

{{% choosable language "java" %}}

* Облачный аккаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) или кластер Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> и <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a>, установленные локально

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Облачный аккаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) или кластер Kubernetes

{{% /choosable %}}

