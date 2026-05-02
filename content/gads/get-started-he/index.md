---
title: "מתחילים עם Pulumi | Pulumi"
meta_desc: התקינו את Pulumi ופרסו את הסטאק הראשון שלכם ב-AWS, Azure, Google Cloud או Kubernetes. תשתית כקוד בקוד פתוח ב-TypeScript, Python, Go, C#, Java או YAML.
layout: gads-get-started
block_external_search_index: true
dir: rtl
cta_label: "להתחיל"
install:
    title: "התקנת Pulumi"
    intro: "הורידו והתקינו את Pulumi עבור הפלטפורמה שלכם:"
    options_note: "אפשרויות התקנה נוספות [זמינות](/docs/install/)."
    test_intro: "בדקו את ההתקנה החדשה על ידי הרצת הפקודה `pulumi version`:"
    restart_note: "אם זה לא עובד, ייתכן שתצטרכו להפעיל מחדש את הטרמינל כדי לוודא שהתיקייה שמכילה את הפקודה `pulumi` נמצאת ב-`PATH` שלכם."

heading: "מתחילים עם Pulumi"
subheading: |
    התקינו את Pulumi ופרסו את הסטאק הראשון שלכם תוך דקות. קוד פתוח, ועובד עם כל ענן מרכזי.

overview:
    title: תשתית כקוד בכל שפה, בכל ענן
    description: |
        Pulumi מאפשר לכם לבנות, לפרוס ולנהל תשתית ענן באמצעות שפות התכנות שאתם כבר מכירים — TypeScript, Python, Go, C#, Java ו-YAML — ביותר מ-170 ספקים.

continue:
    title: המשך עם הענן שלך
    description: |
        בחרו את הפלטפורמה שלכם ועקבו אחר המדריך השלם שלב אחר שלב כדי לפרוס את הפרויקט הראשון שלכם.
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
    title: "אלפי חברות סומכות עלינו"
    description: |
        מנוע ה-IaC בקוד פתוח של Pulumi משמש למעלה מ-350,000 מפתחים ולמעלה מ-4,000 חברות בפרודקשן.
    community:
        number: "350,000+"
        description: "חברי קהילה"
    company:
        number: "4,000+"
        description: "חברות בפרודקשן"
    integration:
        number: "170+"
        description: "שילובי ענן ושירותים"
---

## לפני שמתחילים

בחרו שפה. הדרישות המוקדמות תלויות בבחירתכם.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* חשבון ענן (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) או קלאסטר Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> ו-<a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> מותקנים מקומית

{{% /choosable %}}

{{% choosable language "python" %}}

* חשבון ענן (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) או קלאסטר Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> ו-<a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> או <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> מותקנים מקומית

{{% /choosable %}}

{{% choosable language "go" %}}

* חשבון ענן (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) או קלאסטר Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> מותקן מקומית

{{% /choosable %}}

{{% choosable language "csharp" %}}

* חשבון ענן (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) או קלאסטר Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> מותקן מקומית

{{% /choosable %}}

{{% choosable language "java" %}}

* חשבון ענן (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) או קלאסטר Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> ו-<a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> מותקנים מקומית

{{% /choosable %}}

{{% choosable language "yaml" %}}

* חשבון ענן (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) או קלאסטר Kubernetes

{{% /choosable %}}

