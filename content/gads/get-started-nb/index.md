---
title: "Kom i gang med Pulumi | Pulumi"
meta_desc: Installer Pulumi og distribuer din første stack til AWS, Azure, Google Cloud eller Kubernetes. Åpen kildekode infrastructure as code i TypeScript, Python, Go, C#, Java eller YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Kom i gang"
install:
    title: "Installer Pulumi"
    intro: "Last ned og installer Pulumi for plattformen din:"
    options_note: "Andre installasjonsalternativer [er tilgjengelige](/docs/install/)."
    test_intro: "Test den nye installasjonen ved å kjøre kommandoen `pulumi version`:"
    restart_note: "Hvis det ikke virker, må du kanskje starte terminalen på nytt for å sikre at mappen med kommandoen `pulumi` ligger i `PATH`."

heading: "Kom i gang med Pulumi"
subheading: |
    Installer Pulumi og distribuer din første stack på minutter. Åpen kildekode, fungerer med alle store skyer.

overview:
    title: Infrastructure as Code på alle språk, i alle skyer
    description: |
        Med Pulumi bygger, distribuerer og administrerer du skyinfrastruktur med programmeringsspråkene du allerede kjenner — TypeScript, Python, Go, C#, Java og YAML — på tvers av mer enn 170 leverandører.

continue:
    title: Fortsett med din sky
    description: |
        Velg plattformen din og følg den fullstendige trinnvise guiden for å distribuere ditt første prosjekt.
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
    title: "Tusenvis av selskaper stoler på Pulumi"
    description: |
        Pulumis IaC-motor med åpen kildekode brukes av mer enn 350 000 utviklere og over 4 000 selskaper i produksjon.
    community:
        number: "350 000+"
        description: "Fellesskapsmedlemmer"
    company:
        number: "4 000+"
        description: "Selskaper i produksjon"
    integration:
        number: "170+"
        description: "Sky- og tjenesteintegrasjoner"
---

## Før du starter

Velg språket du vil bruke. Kravene avhenger av valget ditt.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* En skykonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> og <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installert lokalt

{{% /choosable %}}

{{% choosable language "python" %}}

* En skykonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> og <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> eller <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installert lokalt

{{% /choosable %}}

{{% choosable language "go" %}}

* En skykonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installert lokalt

{{% /choosable %}}

{{% choosable language "csharp" %}}

* En skykonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installert lokalt

{{% /choosable %}}

{{% choosable language "java" %}}

* En skykonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> og <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installert lokalt

{{% /choosable %}}

{{% choosable language "yaml" %}}

* En skykonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller en Kubernetes-klynge

{{% /choosable %}}

