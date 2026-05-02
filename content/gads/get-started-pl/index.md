---
title: "Zacznij korzystać z Pulumi | Pulumi"
meta_desc: Zainstaluj Pulumi i wdroż swój pierwszy stack na AWS, Azure, Google Cloud lub Kubernetes. Infrastruktura jako kod open source w TypeScript, Python, Go, C#, Java lub YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Rozpocznij"
install:
    title: "Zainstaluj Pulumi"
    intro: "Pobierz i zainstaluj Pulumi dla swojej platformy:"
    options_note: "Dostępne są również [inne opcje instalacji](/docs/install/)."
    test_intro: "Przetestuj nową instalację, uruchamiając polecenie `pulumi version`:"
    restart_note: "Jeśli to nie działa, może być konieczne ponowne uruchomienie terminala, aby katalog zawierający polecenie `pulumi` znalazł się w zmiennej `PATH`."

heading: "Zacznij korzystać z Pulumi"
subheading: |
    Zainstaluj Pulumi i wdroż swój pierwszy stack w kilka minut. Open source, działa z każdą wiodącą chmurą.

overview:
    title: Infrastruktura jako kod w dowolnym języku, w dowolnej chmurze
    description: |
        Pulumi pozwala tworzyć i wdrażać infrastrukturę chmurową oraz nią zarządzać w językach programowania, które już znasz — TypeScript, Python, Go, C#, Java i YAML — u ponad 170 dostawców usług.

continue:
    title: Kontynuuj z wybraną chmurą
    description: |
        Wybierz swoją platformę i postępuj zgodnie z pełnym przewodnikiem krok po kroku, aby wdrożyć swój pierwszy projekt.
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
    title: "Zaufały nam tysiące firm"
    description: |
        Silnik IaC Pulumi (open source) jest używany przez ponad 350 000 deweloperów i ponad 4 000 firm w środowisku produkcyjnym.
    community:
        number: "350 000+"
        description: "Członkowie społeczności"
    company:
        number: "4 000+"
        description: "Firmy w środowisku produkcyjnym"
    integration:
        number: "170+"
        description: "Integracje z chmurami i usługami"
---

## Zanim zaczniesz

Wybierz język, którego chcesz użyć. Wymagania zależą od wyboru.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Konto w chmurze (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) lub klaster Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> i <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> zainstalowane lokalnie

{{% /choosable %}}

{{% choosable language "python" %}}

* Konto w chmurze (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) lub klaster Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> oraz <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> lub <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> zainstalowane lokalnie

{{% /choosable %}}

{{% choosable language "go" %}}

* Konto w chmurze (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) lub klaster Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> zainstalowane lokalnie

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Konto w chmurze (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) lub klaster Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> zainstalowany lokalnie

{{% /choosable %}}

{{% choosable language "java" %}}

* Konto w chmurze (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) lub klaster Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> i <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> zainstalowane lokalnie

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Konto w chmurze (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) lub klaster Kubernetes

{{% /choosable %}}

