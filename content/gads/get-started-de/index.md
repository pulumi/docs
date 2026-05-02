---
title: "Loslegen mit Pulumi | Pulumi"
meta_desc: Installieren Sie Pulumi und stellen Sie Ihren ersten Stack auf AWS, Azure, Google Cloud oder Kubernetes bereit. Open-Source-Infrastructure-as-Code in TypeScript, Python, Go, C#, Java oder YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Loslegen"
install:
    title: "Pulumi installieren"
    intro: "Laden Sie Pulumi für Ihre Plattform herunter und installieren Sie es:"
    options_note: "Weitere Installationsoptionen sind [verfügbar](/docs/install/)."
    test_intro: "Testen Sie Ihre neue Installation mit dem Befehl `pulumi version`:"
    restart_note: "Falls dies nicht funktioniert, müssen Sie möglicherweise Ihr Terminal neu starten, damit das Verzeichnis mit dem Befehl `pulumi` in Ihrem `PATH` enthalten ist."

heading: "Loslegen mit Pulumi"
subheading: |
    Installieren Sie Pulumi und stellen Sie Ihren ersten Stack in wenigen Minuten bereit. Open Source und funktioniert mit jeder großen Cloud.

overview:
    title: Infrastructure as Code in jeder Sprache, auf jeder Cloud
    description: |
        Mit Pulumi erstellen, deployen und verwalten Sie Cloud-Infrastruktur mit den Programmiersprachen, die Sie bereits kennen – TypeScript, Python, Go, C#, Java und YAML – über mehr als 170 Anbieter hinweg.

continue:
    title: Mit Ihrer Cloud fortfahren
    description: |
        Wählen Sie Ihre Plattform und folgen Sie der vollständigen Schritt-für-Schritt-Anleitung, um Ihr erstes Projekt bereitzustellen.
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
    title: "Tausende Unternehmen vertrauen Pulumi"
    description: |
        Die Open-Source-IaC-Engine von Pulumi wird von über 350.000 Entwicklern und über 4.000 Unternehmen im Produktivbetrieb eingesetzt.
    community:
        number: "350.000+"
        description: "Community-Mitglieder"
    company:
        number: "4.000+"
        description: "Unternehmen im Produktivbetrieb"
    integration:
        number: "170+"
        description: "Cloud- und Service-Integrationen"
---

## Bevor Sie beginnen

Wählen Sie die gewünschte Sprache aus. Die Voraussetzungen hängen von Ihrer Wahl ab.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Ein Cloud-Konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) oder ein Kubernetes-Cluster
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> und <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> lokal installiert

{{% /choosable %}}

{{% choosable language "python" %}}

* Ein Cloud-Konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) oder ein Kubernetes-Cluster
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> und <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> oder <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> lokal installiert

{{% /choosable %}}

{{% choosable language "go" %}}

* Ein Cloud-Konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) oder ein Kubernetes-Cluster
* <a href="https://go.dev/doc/install" target="_blank">Go</a> lokal installiert

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Ein Cloud-Konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) oder ein Kubernetes-Cluster
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> lokal installiert

{{% /choosable %}}

{{% choosable language "java" %}}

* Ein Cloud-Konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) oder ein Kubernetes-Cluster
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> und <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> lokal installiert

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Ein Cloud-Konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) oder ein Kubernetes-Cluster

{{% /choosable %}}

