---
title: "Inizia con Pulumi | Pulumi"
meta_desc: Installa Pulumi e distribuisci il tuo primo stack su AWS, Azure, Google Cloud o Kubernetes. Infrastruttura come codice open source in TypeScript, Python, Go, C#, Java o YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Inizia ora"
install:
    title: "Installa Pulumi"
    intro: "Scarica e installa Pulumi per la tua piattaforma:"
    options_note: "Altre opzioni di installazione [sono disponibili](/docs/install/)."
    test_intro: "Verifica la nuova installazione eseguendo il comando `pulumi version`:"
    restart_note: "Se non funziona, potrebbe essere necessario riavviare il terminale per assicurarti che la directory contenente il comando `pulumi` sia nel tuo `PATH`."

heading: "Inizia con Pulumi"
subheading: |
    Installa Pulumi e distribuisci il tuo primo stack in pochi minuti. Open source e funziona con tutti i principali cloud.

overview:
    title: Infrastructure as Code in qualsiasi linguaggio, su qualsiasi cloud
    description: |
        Pulumi ti permette di creare, distribuire e gestire l'infrastruttura cloud con i linguaggi di programmazione che già conosci — TypeScript, Python, Go, C#, Java e YAML — su oltre 170 provider.

continue:
    title: Continua con il tuo cloud
    description: |
        Scegli la tua piattaforma e segui la guida completa passo dopo passo per distribuire il tuo primo progetto.
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
    title: "Adottato da migliaia di aziende"
    description: |
        Il motore IaC open source di Pulumi è utilizzato da oltre 350.000 sviluppatori e oltre 4.000 aziende in produzione.
    community:
        number: "350.000+"
        description: "Membri della community"
    company:
        number: "4.000+"
        description: "Aziende in produzione"
    integration:
        number: "170+"
        description: "Integrazioni cloud e servizi"
---

## Prima di iniziare

Scegli il linguaggio che vuoi usare. I prerequisiti dipendono dalla tua scelta.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Un account cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un cluster Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> e <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installati localmente

{{% /choosable %}}

{{% choosable language "python" %}}

* Un account cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un cluster Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> e <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> o <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installati localmente

{{% /choosable %}}

{{% choosable language "go" %}}

* Un account cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un cluster Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installato localmente

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Un account cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un cluster Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installato localmente

{{% /choosable %}}

{{% choosable language "java" %}}

* Un account cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un cluster Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> e <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installati localmente

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Un account cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un cluster Kubernetes

{{% /choosable %}}

