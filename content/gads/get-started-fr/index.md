---
title: "Commencer avec Pulumi | Pulumi"
meta_desc: Installez Pulumi et déployez votre première stack sur AWS, Azure, Google Cloud ou Kubernetes. Infrastructure as code open source en TypeScript, Python, Go, C#, Java ou YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Commencer"
install:
    title: "Installer Pulumi"
    intro: "Téléchargez et installez Pulumi pour votre plateforme :"
    options_note: "D'autres options d'installation [sont disponibles](/docs/install/)."
    test_intro: "Testez votre nouvelle installation en exécutant la commande `pulumi version` :"
    restart_note: "Si cela ne fonctionne pas, vous devrez peut-être redémarrer votre terminal pour vous assurer que le répertoire contenant la commande `pulumi` est dans votre `PATH`."

heading: "Commencer avec Pulumi"
subheading: |
    Installez Pulumi et déployez votre première stack en quelques minutes. Open source et compatible avec tous les principaux clouds.

overview:
    title: Infrastructure as Code dans n'importe quel langage, sur n'importe quel cloud
    description: |
        Pulumi vous permet de créer, déployer et gérer une infrastructure cloud avec les langages de programmation que vous connaissez déjà — TypeScript, Python, Go, C#, Java et YAML — sur plus de 170 fournisseurs.

continue:
    title: Choisissez votre cloud
    description: |
        Choisissez votre plateforme et suivez le guide complet, étape par étape, pour déployer votre premier projet.
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
    title: "Adopté par des milliers d'entreprises"
    description: |
        Le moteur IaC open source de Pulumi est utilisé par plus de 350 000 développeurs et plus de 4 000 entreprises en production.
    community:
        number: "350 000+"
        description: "Membres de la communauté"
    company:
        number: "4 000+"
        description: "Entreprises en production"
    integration:
        number: "170+"
        description: "Intégrations cloud et services tiers"
---

## Avant de commencer

Choisissez votre langage. Les prérequis dépendent de votre choix.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Un compte cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou un cluster Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> et <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installés localement

{{% /choosable %}}

{{% choosable language "python" %}}

* Un compte cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou un cluster Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> et <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> ou <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installés localement

{{% /choosable %}}

{{% choosable language "go" %}}

* Un compte cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou un cluster Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installé localement

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Un compte cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou un cluster Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installé localement

{{% /choosable %}}

{{% choosable language "java" %}}

* Un compte cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou un cluster Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> et <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installés localement

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Un compte cloud (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) ou un cluster Kubernetes

{{% /choosable %}}

