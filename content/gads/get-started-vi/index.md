---
title: "Bắt đầu với Pulumi | Pulumi"
meta_desc: Cài đặt Pulumi và triển khai stack đầu tiên của bạn lên AWS, Azure, Google Cloud hoặc Kubernetes. Hạ tầng dưới dạng mã nguồn mở bằng TypeScript, Python, Go, C#, Java hoặc YAML.
layout: gads-get-started
block_external_search_index: true
cta_label: "Bắt đầu"
install:
    title: "Cài đặt Pulumi"
    intro: "Tải xuống và cài đặt Pulumi cho nền tảng của bạn:"
    options_note: "Các tùy chọn cài đặt khác [hiện có](/docs/install/)."
    test_intro: "Kiểm tra cài đặt mới bằng lệnh `pulumi version`:"
    restart_note: "Nếu không hoạt động, bạn có thể cần khởi động lại terminal để đảm bảo thư mục chứa lệnh `pulumi` nằm trong `PATH`."

heading: "Bắt đầu với Pulumi"
subheading: |
    Cài đặt Pulumi và triển khai stack đầu tiên của bạn trong vài phút. Mã nguồn mở, hoạt động với mọi đám mây lớn.

overview:
    title: Hạ tầng dưới dạng mã trong bất kỳ ngôn ngữ nào, trên bất kỳ đám mây nào
    description: |
        Pulumi cho phép bạn xây dựng, triển khai và quản lý hạ tầng đám mây bằng các ngôn ngữ lập trình bạn đã biết — TypeScript, Python, Go, C#, Java và YAML — trên hơn 170 nhà cung cấp.

continue:
    title: Tiếp tục với đám mây của bạn
    description: |
        Chọn nền tảng và làm theo hướng dẫn từng bước đầy đủ để triển khai dự án đầu tiên của bạn.
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
    title: "Được hàng nghìn công ty tin dùng"
    description: |
        Engine IaC mã nguồn mở của Pulumi được hơn 350.000 nhà phát triển và hơn 4.000 công ty sử dụng trong môi trường production.
    community:
        number: "350.000+"
        description: "Thành viên cộng đồng"
    company:
        number: "4.000+"
        description: "Công ty dùng trong production"
    integration:
        number: "170+"
        description: "Tích hợp đám mây và dịch vụ"
---

## Trước khi bắt đầu

Chọn ngôn ngữ bạn muốn sử dụng. Yêu cầu phụ thuộc vào lựa chọn của bạn.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* Tài khoản đám mây (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) hoặc cluster Kubernetes
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> và <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> được cài đặt cục bộ

{{% /choosable %}}

{{% choosable language "python" %}}

* Tài khoản đám mây (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) hoặc cluster Kubernetes
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> và <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> hoặc <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> được cài đặt cục bộ

{{% /choosable %}}

{{% choosable language "go" %}}

* Tài khoản đám mây (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) hoặc cluster Kubernetes
* <a href="https://go.dev/doc/install" target="_blank">Go</a> được cài đặt cục bộ

{{% /choosable %}}

{{% choosable language "csharp" %}}

* Tài khoản đám mây (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) hoặc cluster Kubernetes
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> được cài đặt cục bộ

{{% /choosable %}}

{{% choosable language "java" %}}

* Tài khoản đám mây (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) hoặc cluster Kubernetes
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> và <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> được cài đặt cục bộ

{{% /choosable %}}

{{% choosable language "yaml" %}}

* Tài khoản đám mây (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) hoặc cluster Kubernetes

{{% /choosable %}}

