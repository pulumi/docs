---
title_tag: "Google Cloud & Pulumi"
meta_desc: Pulumi offers full support for Google Cloud, with two providers, 2 components, and multiple templates.
title: "Google Cloud"
h1: Google Cloud & Pulumi
notitle: true
h1_gradient_width: 317
h1_gradient_name: google-cloud
menu:
  clouds:
    identifier: google-cloud
    weight: 1
cloud_overview: true
description: Build infrastructure on Google Cloud using TypeScript, Python, Go, C#, Java or YAML. Pulumi supports all Google Cloud APIs and stays up-to-date with all Google Cloud features.
get_started_guide:
  link: get-started/
  icon: google-cloud
providers:
  description: The Google Cloud Classic provider can provision many Google Cloud resources. Use the Google Cloud Native provider for same-day access to Google Cloud resources.
  provider_list:
  - display_name: Google Cloud Classic
    description: The AWS Classic provider can provision many AWS cloud resources. Use the AWS Native provider for same-day access to all AWS resources.
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
  - display_name: Google Cloud Native
    public_preview: true
    content_links:
    - display_name: Overview
      icon: page-small-black
      url: google-native/
    - display_name: Install & config
      icon: gear-small-black
      url: google-native/installation-configuration/
    - display_name: API docs
      icon: book-small-black
      url: google-native/api-docs/
    - display_name: How-to guides
      icon: question-small-black
      url: google-native/how-to-guides/
components:
- display_name: Google Cloud Global CloudRun
  url: gcp-global-cloudrun/
  description:
- display_name: Google Cloud static website
  url: google-cloud-static-website
  description:
templates:
- display_name: Container service on Google Cloud
  url: container-service/gcp/
- display_name: Google Cloud Serverless application
  url: serverless-application/gcp/
- display_name: Google Cloud static website
  url: static-website/gcp/
- display_name: Virtual machine on Google Cloud
  url: virtual-machine/gcp/
---
