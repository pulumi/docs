---
title: "Kom godt i gang med Pulumi | Pulumi"
meta_desc: Installer Pulumi og deploy din første stack til AWS, Azure, Google Cloud eller Kubernetes. Open source infrastructure as code i TypeScript, Python, Go, C#, Java eller YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Kom i gang"
install:
    title: "Installer Pulumi"
    intro: "Download og installer Pulumi til din platform:"
    options_note: "Andre installationsmuligheder [er tilgængelige](/docs/install/)."
    test_intro: "Test din nye installation ved at køre kommandoen `pulumi version`:"
    restart_note: "Hvis det ikke virker, skal du muligvis genstarte din terminal for at sikre, at mappen med kommandoen `pulumi` er i din `PATH`."

heading: "Kom godt i gang med Pulumi"
subheading: |
    Installer Pulumi og deploy din første stack på få minutter. Open source og fungerer med alle de store cloud-platforme.

overview:
    title: Infrastructure as Code på ethvert sprog, på enhver cloud
    description: |
        Med Pulumi kan du bygge, deploye og administrere cloud-infrastruktur med de programmeringssprog, du allerede kender — TypeScript, Python, Go, C#, Java og YAML — på tværs af mere end 170 udbydere.

continue:
    title: Fortsæt med din cloud
    description: |
        Vælg din platform og følg den komplette trin-for-trin guide for at deploye dit første projekt.
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
    title: "Tusindvis af virksomheder stoler på Pulumi"
    description: |
        Pulumis open source IaC-motor bruges af over 350.000 udviklere og over 4.000 virksomheder i produktion.
    community:
        number: "350.000+"
        description: "Community-medlemmer"
    company:
        number: "4.000+"
        description: "Virksomheder i produktion"
    integration:
        number: "170+"
        description: "Sky- og serviceintegrationer"
---

## Før du går i gang

Vælg det sprog, du vil bruge. Forudsætningerne afhænger af dit valg.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* En cloud-konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> og <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installeret lokalt

{{% /choosable %}}

{{% choosable language "python" %}}

* En cloud-konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> og <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> eller <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installeret lokalt

{{% /choosable %}}

{{% choosable language "go" %}}

* En cloud-konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installeret lokalt

{{% /choosable %}}

{{% choosable language "csharp" %}}

* En cloud-konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installeret lokalt

{{% /choosable %}}

{{% choosable language "java" %}}

* En cloud-konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> og <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installeret lokalt

{{% /choosable %}}

{{% choosable language "yaml" %}}

* En cloud-konto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge

{{% /choosable %}}

