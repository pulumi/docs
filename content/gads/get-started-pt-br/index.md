---
title: "Comece com Pulumi | Pulumi"
meta_desc: Instale o Pulumi e faça o deploy da sua primeira stack na AWS, Azure, Google Cloud ou Kubernetes. Infraestrutura como código (IaC) open source em TypeScript, Python, Go, C#, Java ou YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Comece agora"
install:
    title: "Instale o Pulumi"
    intro: "Baixe e instale o Pulumi para sua plataforma:"
    options_note: "Outras opções de instalação [estão disponíveis](/docs/install/)."
    test_intro: "Teste a nova instalação executando o comando `pulumi version`:"
    restart_note: "Se não funcionar, pode ser necessário reiniciar o terminal para garantir que o diretório com o comando `pulumi` esteja no seu `PATH`."

heading: "Comece com Pulumi"
subheading: |
    Instale o Pulumi e faça o deploy da sua primeira stack em minutos. Open source e compatível com todas as principais nuvens.

overview:
    title: Infraestrutura como código em qualquer linguagem, em qualquer nuvem
    description: |
        O Pulumi permite que você crie, faça o deploy e gerencie infraestrutura em nuvem com as linguagens de programação que você já conhece — TypeScript, Python, Go, C#, Java e YAML — em mais de 170 provedores.

continue:
    title: Continue com sua nuvem
    description: |
        Escolha sua plataforma e siga o guia passo a passo completo para implantar seu primeiro projeto.
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
    title: "Com a confiança de milhares de empresas"
    description: |
        A engine de IaC open source do Pulumi é usada por mais de 350.000 desenvolvedores e mais de 4.000 empresas em produção.
    community:
        number: "350.000+"
        description: "Membros da comunidade"
    company:
        number: "4.000+"
        description: "Empresas em produção"
    integration:
        number: "170+"
        description: "Integrações de nuvem e serviços"
---

## Antes de começar

Escolha a linguagem que deseja usar. Os pré-requisitos dependem da sua escolha.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Uma conta em nuvem (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou um cluster Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> e <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> instalados localmente

{{% /choosable %}}

{{% choosable language "python" %}}

* Uma conta em nuvem (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou um cluster Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> e <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> ou <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> instalados localmente

{{% /choosable %}}

{{% choosable language "go" %}}

* Uma conta em nuvem (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou um cluster Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> instalado localmente

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Uma conta em nuvem (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou um cluster Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> instalado localmente

{{% /choosable %}}

{{% choosable language "java" %}}

* Uma conta em nuvem (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou um cluster Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> e <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> instalados localmente

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Uma conta em nuvem (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou um cluster Kubernetes

{{% /choosable %}}

