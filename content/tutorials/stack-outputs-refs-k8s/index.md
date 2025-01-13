---
title: "Reference Kubernetes Resources Across Stacks"
title_tag: "Reference Kubernetes Resources Across Stacks"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Here is a brief description of what this tutorial's all about.

# A similar description used for search results and social-media previews.
meta_desc: Here is a brief description of what this tutorial's all about.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: k8s-stack-ref-meta.png

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
    In this tutorial, you will learn how to work with stack outputs, specifically how to export values from a stack and how to reference those values from another stack. You will do this by creating simple Azure Resource Group, Storage Account, and Blob Container resources in one stack. You will then create a Blob resource in a second project/stack that will upload a file to the Blob Storage defined in the first stack.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a stack output
    - How to view the stack output
    - How to reference the output from a different stack

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - Familiarity with JavaScript, TypeScript, or Python

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 15

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - kubernetes
---

This is the actual content of the tutorial.
