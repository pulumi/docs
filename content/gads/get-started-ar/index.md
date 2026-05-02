---
title: "ابدأ مع Pulumi | Pulumi"
meta_desc: ثبّت Pulumi وانشر أول stack لك على AWS أو Azure أو Google Cloud أو Kubernetes. بنية تحتية ككود مفتوحة المصدر بـ TypeScript أو Python أو Go أو C# أو Java أو YAML.
layout: gads-get-started
block_external_search_index: true
dir: rtl
cta_label: "ابدأ الآن"
install:
    title: "ثبّت Pulumi"
    intro: "نزّل Pulumi لمنصتك وثبّته:"
    options_note: "خيارات التثبيت الأخرى [متاحة هنا](/docs/install/)."
    test_intro: "اختبر التثبيت الجديد بتشغيل الأمر `pulumi version`:"
    restart_note: "إذا لم ينجح ذلك، فقد تحتاج إلى إعادة تشغيل نافذة الطرفية للتأكد من أن المجلد الذي يحتوي على الأمر `pulumi` ضمن `PATH`."

heading: "ابدأ مع Pulumi"
subheading: |
    ثبّت Pulumi وانشر أول stack لك خلال دقائق. مفتوح المصدر، ويعمل مع كل سحابة كبرى.

overview:
    title: البنية التحتية ككود بأي لغة، على أي سحابة
    description: |
        يتيح لك Pulumi بناء البنية التحتية السحابية ونشرها وإدارتها بلغات البرمجة التي تعرفها بالفعل — TypeScript و Python و Go و C# و Java و YAML — عبر أكثر من 170 مزوّدًا.

continue:
    title: تابع مع سحابتك
    description: |
        اختر منصتك واتبع الدليل الكامل خطوة بخطوة لنشر مشروعك الأول.
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
    title: "تثق به آلاف الشركات"
    description: |
        محرك IaC مفتوح المصدر من Pulumi يستخدمه أكثر من 350,000 مطور وأكثر من 4,000 شركة في الإنتاج.
    community:
        number: "350,000+"
        description: "أعضاء المجتمع"
    company:
        number: "4,000+"
        description: "شركات في الإنتاج"
    integration:
        number: "170+"
        description: "تكاملات مع السحابات والخدمات"
---

## قبل أن تبدأ

اختر اللغة التي تريد استخدامها. تعتمد المتطلبات على اختيارك.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* حساب سحابي (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>، <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>، <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) أو عنقود Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> و <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> مثبتان محليًا

{{% /choosable %}}

{{% choosable language "python" %}}

* حساب سحابي (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>، <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>، <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) أو عنقود Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> و <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a> أو <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> أو <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> مثبتة محليًا

{{% /choosable %}}

{{% choosable language "go" %}}

* حساب سحابي (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>، <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>، <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) أو عنقود Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> مثبت محليًا

{{% /choosable %}}

{{% choosable language "csharp" %}}

* حساب سحابي (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>، <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>، <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) أو عنقود Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> مثبت محليًا

{{% /choosable %}}

{{% choosable language "java" %}}

* حساب سحابي (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>، <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>، <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) أو عنقود Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> و <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> مثبتان محليًا

{{% /choosable %}}

{{% choosable language "yaml" %}}

* حساب سحابي (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>، <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>، <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) أو عنقود Kubernetes

{{% /choosable %}}

