---
title: "Aloita Pulumin käyttö | Pulumi"
meta_desc: Asenna Pulumi ja ota ensimmäinen stackisi käyttöön AWS:ssa, Azuressa, Google Cloudissa tai Kubernetesissä. Avoimen lähdekoodin infrastructure as code TypeScriptillä, Pythonilla, Golla, C#:lla, Javalla tai YAML:lla.
layout: gads-get-started
block_external_search_index: true
cta_label: "Aloita"
install:
    title: "Asenna Pulumi"
    intro: "Lataa ja asenna Pulumi omalle alustallesi:"
    options_note: "Muita asennusvaihtoehtoja [on saatavilla](/docs/install/)."
    test_intro: "Testaa asennus suorittamalla `pulumi version`:"
    restart_note: "Jos tämä ei toimi, sinun on ehkä käynnistettävä terminaali uudelleen varmistaaksesi, että `pulumi`-komennon sisältävä hakemisto on `PATH`-muuttujassa."

heading: "Aloita Pulumin käyttö"
subheading: |
    Asenna Pulumi ja ota ensimmäinen stackisi käyttöön muutamassa minuutissa. Avointa lähdekoodia ja toimii kaikkien suurten pilvipalveluiden kanssa.

overview:
    title: Infrastructure as Code millä tahansa kielellä, missä tahansa pilvessä
    description: |
        Pulumin avulla rakennat, otat käyttöön ja hallitset pilvi-infrastruktuuria ohjelmointikielillä, joita jo osaat — TypeScript, Python, Go, C#, Java ja YAML — yli 170 tarjoajan kanssa.

continue:
    title: Jatka oman pilvesi kanssa
    description: |
        Valitse alustasi ja seuraa kattavaa vaihe vaiheelta -opasta ensimmäisen projektisi käyttöönottoon.
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
    title: "Tuhannet yritykset luottavat meihin"
    description: |
        Pulumin avoimen lähdekoodin IaC-moottoria käyttää yli 350 000 kehittäjää ja yli 4 000 yritystä tuotannossa.
    community:
        number: "350 000+"
        description: "Yhteisön jäsentä"
    company:
        number: "4 000+"
        description: "Yritystä tuotannossa"
    integration:
        number: "170+"
        description: "Pilvi- ja palveluintegraatiota"
---

## Ennen kuin aloitat

Valitse kieli, jota haluat käyttää. Edellytykset riippuvat valinnastasi.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Pilvitili (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) tai Kubernetes-klusteri
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> ja <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> asennettuna paikallisesti

{{% /choosable %}}

{{% choosable language "python" %}}

* Pilvitili (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) tai Kubernetes-klusteri
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> sekä <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> tai <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> asennettuna paikallisesti

{{% /choosable %}}

{{% choosable language "go" %}}

* Pilvitili (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) tai Kubernetes-klusteri
* <a href="https://go.dev/doc/install" target="_blank">Go</a> asennettuna paikallisesti

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Pilvitili (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) tai Kubernetes-klusteri
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> asennettuna paikallisesti

{{% /choosable %}}

{{% choosable language "java" %}}

* Pilvitili (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) tai Kubernetes-klusteri
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> ja <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> asennettuna paikallisesti

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Pilvitili (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) tai Kubernetes-klusteri

{{% /choosable %}}

