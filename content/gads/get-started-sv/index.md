---
title: "Kom igång med Pulumi | Pulumi"
meta_desc: Installera Pulumi och distribuera din första stack till AWS, Azure, Google Cloud eller Kubernetes. Öppen källkod för infrastructure as code i TypeScript, Python, Go, C#, Java eller YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Kom igång"
install:
    title: "Installera Pulumi"
    intro: "Ladda ner och installera Pulumi för din plattform:"
    options_note: "Andra installationsalternativ [finns tillgängliga](/docs/install/)."
    test_intro: "Testa din nya installation genom att köra kommandot `pulumi version`:"
    restart_note: "Om det inte fungerar kan du behöva starta om terminalen så att katalogen med kommandot `pulumi` finns i din `PATH`."

heading: "Kom igång med Pulumi"
subheading: |
    Installera Pulumi och distribuera din första stack på några minuter. Öppen källkod och fungerar med alla större moln.

overview:
    title: Infrastructure as Code på valfritt språk, i valfritt moln
    description: |
        Med Pulumi bygger, distribuerar och hanterar du molninfrastruktur med programmeringsspråken du redan kan — TypeScript, Python, Go, C#, Java och YAML — med över 170 leverantörer.

continue:
    title: Fortsätt med ditt moln
    description: |
        Välj din plattform och följ den fullständiga steg-för-steg-guiden för att distribuera ditt första projekt.
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
    title: "Tusentals företag litar på Pulumi"
    description: |
        Pulumis IaC-motor med öppen källkod används av över 350 000 utvecklare och över 4 000 företag i produktion.
    community:
        number: "350 000+"
        description: "Communitymedlemmar"
    company:
        number: "4 000+"
        description: "Företag i produktion"
    integration:
        number: "170+"
        description: "Moln- och tjänsteintegrationer"
---

## Innan du börjar

Välj språket du vill använda. Förutsättningarna beror på ditt val.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Ett molnkonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller ett Kubernetes-kluster
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> och <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> installerade lokalt

{{% /choosable %}}

{{% choosable language "python" %}}

* Ett molnkonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller ett Kubernetes-kluster
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> och <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> eller <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> installerade lokalt

{{% /choosable %}}

{{% choosable language "go" %}}

* Ett molnkonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller ett Kubernetes-kluster
* <a href="https://go.dev/doc/install" target="_blank">Go</a> installerat lokalt

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Ett molnkonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller ett Kubernetes-kluster
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> installerat lokalt

{{% /choosable %}}

{{% choosable language "java" %}}

* Ett molnkonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller ett Kubernetes-kluster
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> och <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> installerade lokalt

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Ett molnkonto (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) eller ett Kubernetes-kluster

{{% /choosable %}}

