---
title: "Pulumi 시작하기 | Pulumi"
meta_desc: Pulumi를 설치하고 AWS, Azure, Google Cloud 또는 Kubernetes에 첫 번째 스택을 배포하세요. TypeScript, Python, Go, C#, Java 또는 YAML로 작성하는 오픈소스 코드형 인프라.
layout: gads-get-started
block_external_search_index: true
cta_label: "시작하기"
install:
    title: "Pulumi 설치"
    intro: "사용하는 플랫폼에 맞는 Pulumi를 다운로드하여 설치하세요:"
    options_note: "다른 설치 옵션도 [확인하실 수 있습니다](/docs/install/)."
    test_intro: "`pulumi version` 명령을 실행하여 설치가 제대로 되었는지 확인하세요:"
    restart_note: "작동하지 않으면 터미널을 재시작하여 `pulumi` 명령이 있는 디렉터리를 `PATH`에 포함시켜야 할 수 있습니다."

heading: "Pulumi 시작하기"
subheading: |
    Pulumi를 설치하고 몇 분 안에 첫 번째 스택을 배포하세요. 오픈소스이며 모든 주요 클라우드를 지원합니다.

overview:
    title: 모든 언어, 모든 클라우드를 위한 코드형 인프라
    description: |
        Pulumi를 사용하면 이미 익숙한 프로그래밍 언어(TypeScript, Python, Go, C#, Java, YAML)로 170개 이상의 프로바이더에서 클라우드 인프라를 구축, 배포 및 관리할 수 있습니다.

continue:
    title: 사용하시는 클라우드로 계속하기
    description: |
        플랫폼을 선택하고 전체 단계별 가이드에 따라 첫 번째 프로젝트를 배포하세요.
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
    title: "수천 개 기업이 신뢰하는 Pulumi"
    description: |
        Pulumi의 오픈소스 IaC 엔진은 350,000명 이상의 개발자와 4,000개 이상의 기업이 프로덕션에서 사용하고 있습니다.
    community:
        number: "350,000+"
        description: "커뮤니티 멤버"
    company:
        number: "4,000+"
        description: "프로덕션에서 사용 중인 기업"
    integration:
        number: "170+"
        description: "클라우드 및 서비스 통합"
---

## 시작하기 전에

사용할 언어를 선택하세요. 사전 요구 사항은 선택에 따라 다릅니다.

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language "typescript" %}}

* 클라우드 계정 (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) 또는 Kubernetes 클러스터
* 로컬에 <a href="https://nodejs.org/en/download" target="_blank">Node.js</a>와 <a href="https://www.npmjs.com/package/npm" target="_blank">npm</a> 설치

{{% /choosable %}}

{{% choosable language "python" %}}

* 클라우드 계정 (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) 또는 Kubernetes 클러스터
* 로컬에 <a href="https://www.python.org/downloads/" target="_blank">Python</a>과 <a href="https://pip.pypa.io/en/stable/installation/" target="_blank">pip</a>, <a href="https://python-poetry.org/docs/" target="_blank">Poetry</a> 또는 <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a> 설치

{{% /choosable %}}

{{% choosable language "go" %}}

* 클라우드 계정 (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) 또는 Kubernetes 클러스터
* 로컬에 <a href="https://go.dev/doc/install" target="_blank">Go</a> 설치

{{% /choosable %}}

{{% choosable language "csharp" %}}

* 클라우드 계정 (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) 또는 Kubernetes 클러스터
* 로컬에 <a href="https://dotnet.microsoft.com/en-us/download/dotnet" target="_blank">.NET</a> 설치

{{% /choosable %}}

{{% choosable language "java" %}}

* 클라우드 계정 (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) 또는 Kubernetes 클러스터
* 로컬에 <a href="https://www.oracle.com/java/technologies/downloads/" target="_blank">Java 11+</a>와 <a href="https://maven.apache.org/install.html" target="_blank">Maven 3.6.1+</a> 설치

{{% /choosable %}}

{{% choosable language "yaml" %}}

* 클라우드 계정 (<a href="https://aws.amazon.com/free" target="_blank">AWS</a>, <a href="https://azure.microsoft.com/free" target="_blank">Azure</a>, <a href="https://cloud.google.com/free" target="_blank">Google Cloud</a>) 또는 Kubernetes 클러스터

{{% /choosable %}}

