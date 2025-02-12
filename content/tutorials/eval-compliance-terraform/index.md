---
title: "Evaluate Compliance of Terraform Resources"
title_tag: "Evaluate Compliance of Terraform Resources"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Learn how to use Pulumi Insights to evaluate compliance of resources deployed with Terraform.

# A similar description used for search results and social-media previews.
meta_desc: Learn how to use Pulumi Insights to evaluate compliance of resources deployed with Terraform.

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
    In this tutorial, you will learn how to use Pulumi Insights to evaluate compliance of resources, specifically resources that have been deployed using Terraform.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to do X
    - When to do Y
    - Why X is more preferable than Y

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud Team, Enterprise, or Business Critical account](https://app.pulumi.com/signup)
    - A Pulumi Cloud [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - An [ESC environment and cloud credentials created and configured](/docs/insights/get-started/begin/)
    - A [Pulumi Insights account](/docs/insights/get-started/create-accounts/)

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - some-non-existent-collection
---

This is the actual content of the tutorial.

1. Deploy Terraform resources (optional, Note that one of the resources will be out of compliance later)
2. Deploy Compliance policies
3. Run Insights scan
