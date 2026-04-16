---
title_tag: "Google Cloud & Pulumi"
meta_desc: Pulumi offers full support for Google Cloud, with a dedicated provider and multiple templates.
title: "Google Cloud"
meta_image: /images/docs/meta-images/docs-clouds-google-cloud-meta-image.png
h1: Google Cloud & Pulumi
menu:
  iac:
    name: Google Cloud
    identifier: google-clouds
    parent: iac-clouds
    weight: 1
cloud_overview: true
description: Build infrastructure on Google Cloud using TypeScript, Python, Go, C#, Java or YAML. Pulumi supports all Google Cloud APIs and stays up-to-date with all Google Cloud features.
get_started_guide:
  link: /docs/iac/get-started/gcp/
  icon: google-cloud
providers:
  description: The Google Cloud provider manages Google Cloud resources with Pulumi.
  provider_list:
  - display_name: Google Cloud
    description: The Google Cloud provider manages a broad set of Google Cloud resources with Pulumi.
    recommended: true
    content_links:
    - display_name: Overview
      icon: page-small-black
      url: gcp/
    - display_name: Install & config
      icon: gear-small-black
      url: gcp/installation-configuration/
    - display_name: API docs
      icon: book-small-black
      url: gcp/api-docs/
    - display_name: How-to guides
      icon: question-small-black
      url: gcp/how-to-guides/
templates:
- display_name: Container service on Google Cloud
  url: container-service/gcp/
- display_name: Google Cloud Serverless application
  url: serverless-application/gcp/
- display_name: Google Cloud static website
  url: static-website/gcp/
- display_name: Virtual machine on Google Cloud
  url: virtual-machine/gcp/
- display_name: Kubernetes cluster on Google Cloud
  url: kubernetes/gcp/
aliases:
  - /docs/clouds/gcp/
  - /docs/clouds/gcp/guides/
  - /docs/clouds/gcp/guides/providers/
  - /docs/iac/clouds/gcp/guides/
  - /docs/iac/clouds/gcp/guides/providers/
---
