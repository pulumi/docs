---
title: "Comienza con Pulumi | Pulumi"
meta_desc: Instala Pulumi y despliega tu primer stack en AWS, Azure, Google Cloud o Kubernetes. Infraestructura como código (open source) en TypeScript, Python, Go, C#, Java o YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Comienza"
install:
    title: "Instala Pulumi"
    intro: "Descarga e instala Pulumi para tu plataforma:"
    options_note: "Otras opciones de instalación [están disponibles](/docs/install/)."
    test_intro: "Verifica tu nueva instalación ejecutando el comando `pulumi version`:"
    restart_note: "Si esto no funciona, es posible que necesites reiniciar tu terminal para asegurar que el directorio con el comando `pulumi` esté en tu `PATH`."

heading: "Comienza con Pulumi"
subheading: |
    Instala Pulumi y despliega tu primer stack en minutos. Código abierto y funciona con todas las nubes principales.

overview:
    title: Infraestructura como código en cualquier lenguaje, en cualquier nube
    description: |
        Pulumi te permite construir, desplegar y administrar infraestructura en la nube con los lenguajes de programación que ya conoces — TypeScript, Python, Go, C#, Java y YAML — en más de 170 proveedores.

continue:
    title: Continúa con tu nube
    description: |
        Elige tu plataforma y sigue la guía completa paso a paso para desplegar tu primer proyecto.
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
    title: "Con la confianza de miles de empresas"
    description: |
        El motor IaC de código abierto de Pulumi es utilizado por más de 350.000 desarrolladores y más de 4.000 empresas en producción.
    community:
        number: "350.000+"
        description: "Miembros de la comunidad"
    company:
        number: "4.000+"
        description: "Empresas en producción"
    integration:
        number: "170+"
        description: "Integraciones de nube y servicios"
---

## Antes de empezar

Elige el lenguaje que quieres usar. Los requisitos previos dependen de tu elección.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Una cuenta de nube (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un clúster de Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> y <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> instalados localmente

{{% /choosable %}}

{{% choosable language "python" %}}

* Una cuenta de nube (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un clúster de Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> y <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> o <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> instalados localmente

{{% /choosable %}}

{{% choosable language "go" %}}

* Una cuenta de nube (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un clúster de Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> instalado localmente

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Una cuenta de nube (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un clúster de Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> instalado localmente

{{% /choosable %}}

{{% choosable language "java" %}}

* Una cuenta de nube (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un clúster de Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> y <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> instalados localmente

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Una cuenta de nube (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) o un clúster de Kubernetes

{{% /choosable %}}

