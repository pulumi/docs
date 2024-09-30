---
title: "Creating Resources on Azure"
title_tag: "Creating Resources on Azure"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to define and provision resources on Azure using Pulumi.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to define and provision resources on Azure using Pulumi.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: meta.png

# An optional video for the tutorial. When present, it appears at the top of the page, replacing
# the meta image. YouTube and HTML5 video sources are supported.
# video:
#     url: /blog/drift-detection/drift.mp4
#     youtube: Q8tw6YTD3ac

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
   In Pulumi, resources represent the fundamental units that make up your infrastructure, such as virtual machines, networks, storage, and databases. A resource is used to define and manage an infrastructure object in your Pulumi configuration.

   In this tutorial, you will create a simple Nginx web server. You will then refer to documentation in the Pulumi Registry to create a TBD to make the server publicly accessible.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a new resource
    - How to update an existing resource
    - How to reference resource definitions in the Pulumi documentation

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - An [Azure account](https://azure.microsoft.com/en-us/pricing/purchase-options/azure-account)
    - The [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
    - Familiarity with one of [Pulumi's supported languages](/docs/iac/languages-sdks/)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

This is the actual content of the tutorial.
