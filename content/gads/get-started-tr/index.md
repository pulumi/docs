---
title: "Pulumi ile başlayın | Pulumi"
meta_desc: Pulumi'yi kurun ve ilk stack'inizi AWS, Azure, Google Cloud veya Kubernetes'e dağıtın. TypeScript, Python, Go, C#, Java veya YAML ile açık kaynak, kod olarak altyapı.
layout: gads-get-started
block_external_search_index: true
cta_label: "Hemen başlayın"
install:
    title: "Pulumi'yi kurun"
    intro: "Pulumi'yi platformunuza indirip kurun:"
    options_note: "Diğer kurulum seçenekleri [burada mevcuttur](/docs/install/)."
    test_intro: "`pulumi version` komutunu çalıştırarak yeni kurulumu test edin:"
    restart_note: "Bu çalışmazsa, `pulumi` komutunu içeren dizinin `PATH` içinde olduğundan emin olmak için terminalinizi yeniden başlatmanız gerekebilir."

heading: "Pulumi ile başlayın"
subheading: |
    Pulumi'yi kurun ve ilk stack'inizi dakikalar içinde dağıtın. Açık kaynak ve tüm büyük bulutlarla çalışır.

overview:
    title: Her dilde, her bulutta kod olarak altyapı
    description: |
        Pulumi, zaten bildiğiniz programlama dilleriyle (TypeScript, Python, Go, C#, Java ve YAML) 170'ten fazla sağlayıcıda bulut altyapısını oluşturmanıza, dağıtmanıza ve yönetmenize olanak tanır.

continue:
    title: Bulutunuzla devam edin
    description: |
        Platformunuzu seçin ve ilk projenizi dağıtmak için kapsamlı adım adım kılavuzu izleyin.
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
    title: "Binlerce şirket tarafından tercih ediliyor"
    description: |
        Pulumi'nin açık kaynak IaC motoru, 350.000'den fazla geliştirici ve üretimde 4.000'den fazla şirket tarafından kullanılıyor.
    community:
        number: "350.000+"
        description: "Topluluk üyesi"
    company:
        number: "4.000+"
        description: "Üretimde kullanan şirket"
    integration:
        number: "170+"
        description: "Bulut ve hizmet entegrasyonları"
---

## Başlamadan önce

Kullanmak istediğiniz dili seçin. Ön koşullar seçiminize bağlıdır.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Bir bulut hesabı (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) veya bir Kubernetes kümesi
* Yerel olarak kurulmuş <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> ve <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a>

{{% /choosable %}}

{{% choosable language "python" %}}

* Bir bulut hesabı (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) veya bir Kubernetes kümesi
* Yerel olarak kurulmuş <a href="https://www.python.org/downloads/" target="_blank">Python</a> ve <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> veya <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a>

{{% /choosable %}}

{{% choosable language "go" %}}

* Bir bulut hesabı (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) veya bir Kubernetes kümesi
* Yerel olarak kurulmuş <a href="https://go.dev/doc/install" target="_blank">Go</a>

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Bir bulut hesabı (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) veya bir Kubernetes kümesi
* Yerel olarak kurulmuş <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a>

{{% /choosable %}}

{{% choosable language "java" %}}

* Bir bulut hesabı (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) veya bir Kubernetes kümesi
* Yerel olarak kurulmuş <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> ve <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a>

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Bir bulut hesabı (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) veya bir Kubernetes kümesi

{{% /choosable %}}

