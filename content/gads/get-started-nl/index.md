---
title: "Aan de slag met Pulumi | Pulumi"
meta_desc: Installeer Pulumi en deploy je eerste stack naar AWS, Azure, Google Cloud of Kubernetes. Open source infrastructure as code in TypeScript, Python, Go, C#, Java of YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Aan de slag"
install:
    title: "Installeer Pulumi"
    intro: "Download en installeer Pulumi voor jouw platform:"
    options_note: "Andere installatieopties [zijn beschikbaar](/docs/install/)."
    test_intro: "Test je nieuwe installatie door het commando `pulumi version` uit te voeren:"
    restart_note: "Als dit niet werkt, moet je mogelijk je terminal opnieuw opstarten zodat de map met het commando `pulumi` in je `PATH` staat."

heading: "Aan de slag met Pulumi"
subheading: |
    Installeer Pulumi en deploy je eerste stack in enkele minuten. Open source en werkt met elke grote cloud.

overview:
    title: Infrastructure as Code in elke taal, op elke cloud
    description: |
        Met Pulumi bouw, deploy en beheer je cloudinfrastructuur met de programmeertalen die je al kent — TypeScript, Python, Go, C#, Java en YAML — met meer dan 170 providers.

continue:
    title: Verder met jouw cloud
    description: |
        Kies je platform en volg de complete stapsgewijze handleiding om je eerste project te deployen.
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
    title: "Het vertrouwen van duizenden bedrijven"
    description: |
        De open source IaC-engine van Pulumi wordt gebruikt door meer dan 350.000 ontwikkelaars en meer dan 4.000 bedrijven in productie.
    community:
        number: "350.000+"
        description: "Communityleden"
    company:
        number: "4.000+"
        description: "Bedrijven in productie"
    integration:
        number: "170+"
        description: "Cloud- en service-integraties"
---

## Voordat je begint

Kies de taal die je wilt gebruiken. De vereisten hangen af van je keuze.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Een cloudaccount (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) of een Kubernetes-cluster
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> en <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> lokaal geïnstalleerd

{{% /choosable %}}

{{% choosable language "python" %}}

* Een cloudaccount (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) of een Kubernetes-cluster
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> en <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> of <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> lokaal geïnstalleerd

{{% /choosable %}}

{{% choosable language "go" %}}

* Een cloudaccount (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) of een Kubernetes-cluster
* <a href="https://go.dev/doc/install" target="_blank">Go</a> lokaal geïnstalleerd

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Een cloudaccount (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) of een Kubernetes-cluster
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> lokaal geïnstalleerd

{{% /choosable %}}

{{% choosable language "java" %}}

* Een cloudaccount (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) of een Kubernetes-cluster
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> en <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> lokaal geïnstalleerd

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Een cloudaccount (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) of een Kubernetes-cluster

{{% /choosable %}}

