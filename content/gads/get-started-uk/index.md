---
title: "Почніть із Pulumi | Pulumi"
meta_desc: Встановіть Pulumi та розгорніть перший stack у AWS, Azure, Google Cloud чи Kubernetes. Open source інфраструктура як код на TypeScript, Python, Go, C#, Java або YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Почати"
install:
    title: "Встановіть Pulumi"
    intro: "Завантажте та встановіть Pulumi для вашої платформи:"
    options_note: "Інші варіанти встановлення [доступні тут](/docs/install/)."
    test_intro: "Перевірте встановлення, виконавши команду `pulumi version`:"
    restart_note: "Якщо команда не працює, можливо, потрібно перезапустити термінал, щоб каталог із командою `pulumi` опинився у `PATH`."

heading: "Почніть із Pulumi"
subheading: |
    Встановіть Pulumi та розгорніть перший stack за кілька хвилин. Open source, працює з будь-якою великою хмарою.

overview:
    title: Інфраструктура як код будь-якою мовою, у будь-якій хмарі
    description: |
        Pulumi дозволяє створювати, розгортати хмарну інфраструктуру та керувати нею мовами програмування, які ви вже знаєте — TypeScript, Python, Go, C#, Java та YAML — із понад 170 провайдерами.

continue:
    title: Продовжте з обраною хмарою
    description: |
        Оберіть платформу та дотримуйтесь повного покрокового посібника, щоб розгорнути перший проєкт.
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
    title: "Нам довіряють тисячі компаній"
    description: |
        Open source IaC-рушій від Pulumi використовують понад 350 000 розробників і понад 4 000 компаній у продакшені.
    community:
        number: "350 000+"
        description: "Учасників спільноти"
    company:
        number: "4 000+"
        description: "Компаній у продакшені"
    integration:
        number: "170+"
        description: "Інтеграцій хмар і сервісів"
---

## Перед початком

Оберіть мову, яку хочете використовувати. Вимоги залежать від вибору.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Хмарний акаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) або кластер Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> та <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a>, встановлені локально

{{% /choosable %}}

{{% choosable language "python" %}}

* Хмарний акаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) або кластер Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> та <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> або <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a>, встановлені локально

{{% /choosable %}}

{{% choosable language "go" %}}

* Хмарний акаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) або кластер Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a>, встановлений локально

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Хмарний акаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) або кластер Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a>, встановлений локально

{{% /choosable %}}

{{% choosable language "java" %}}

* Хмарний акаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) або кластер Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> та <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a>, встановлені локально

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Хмарний акаунт (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) або кластер Kubernetes

{{% /choosable %}}

