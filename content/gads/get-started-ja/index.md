---
title: "Pulumi をはじめる | Pulumi"
meta_desc: Pulumi をインストールして、AWS、Azure、Google Cloud、または Kubernetes に最初のスタックをデプロイ。TypeScript、Python、Go、C#、Java、または YAML で書けるオープンソースの Infrastructure as Code。
layout: gads-get-started
block_external_search_index: true
cta_label: "はじめる"
install:
    title: "Pulumi をインストール"
    intro: "お使いのプラットフォーム用の Pulumi をダウンロードしてインストールします："
    options_note: "その他のインストール方法は [こちら](/docs/install/) で確認できます。"
    test_intro: "`pulumi version` コマンドを実行してインストールを確認します："
    restart_note: "コマンドが動作しない場合は、`pulumi` コマンドを含むディレクトリが `PATH` に含まれていることを確認するため、ターミナルを再起動してください。"

heading: "Pulumi をはじめる"
subheading: |
    Pulumi をインストールして、数分で最初のスタックをデプロイできます。オープンソースで、あらゆる主要クラウドに対応しています。

overview:
    title: あらゆる言語、あらゆるクラウドで Infrastructure as Code
    description: |
        Pulumi なら、すでに使い慣れた TypeScript、Python、Go、C#、Java、YAML などのプログラミング言語で、170 を超えるプロバイダーに対応し、クラウドインフラの構築・デプロイ・管理が可能です。

continue:
    title: お使いのクラウドで続ける
    description: |
        プラットフォームを選択し、詳細なステップバイステップのガイドに従って最初のプロジェクトをデプロイしましょう。
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
    title: "数千社に信頼されています"
    description: |
        Pulumi のオープンソース IaC エンジンは、350,000 人以上の開発者と、本番環境で利用する 4,000 社以上の企業に採用されています。
    community:
        number: "350,000+"
        description: "コミュニティメンバー"
    company:
        number: "4,000+"
        description: "本番環境で利用中の企業"
    integration:
        number: "170+"
        description: "クラウドおよびサービス連携"
---

## はじめる前に

使用する言語を選択してください。前提条件は選択した言語によって異なります。

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* クラウドアカウント (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) または Kubernetes クラスター
* <a href="https://nodejs.org/en/download" target="_blank">Node.js</a> と <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> をローカルにインストール

{{% /choosable %}}

{{% choosable language "python" %}}

* クラウドアカウント (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) または Kubernetes クラスター
* <a href="https://www.python.org/downloads/" target="_blank">Python</a> と <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>、<a href="https://python-poetry.org/docs/" target="_blank">Poetry</a>、または <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> をローカルにインストール

{{% /choosable %}}

{{% choosable language "go" %}}

* クラウドアカウント (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) または Kubernetes クラスター
* <a href="https://go.dev/doc/install" target="_blank">Go</a> をローカルにインストール

{{% /choosable %}}

{{% choosable language "csharp" %}}

* クラウドアカウント (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) または Kubernetes クラスター
* <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> をローカルにインストール

{{% /choosable %}}

{{% choosable language "java" %}}

* クラウドアカウント (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) または Kubernetes クラスター
* <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a> と <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> をローカルにインストール

{{% /choosable %}}

{{% choosable language "yaml" %}}

* クラウドアカウント (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>、<a href="https://azure.microsoft.com/free" target="_blank">Azure</a>、<a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) または Kubernetes クラスター

{{% /choosable %}}

