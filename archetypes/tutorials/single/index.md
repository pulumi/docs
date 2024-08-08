---
title: "{{ replace .Name "-" " " | title }}"
title_tag: "{{ replace .Name "-" " " | title }}"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Here is a brief description of what this tutorial's all about.

# A similar description used for search results and social-media previews.
meta_desc: Here is a brief description of what this tutorial's all about.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: meta.png

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    This is the tutorial summary. It should describe the overall goal of the tutorial and briefly cover what
    the reader will know how to do by the end of it.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to do X
    - When to do Y
    - Why X is more preferable than Y

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - Familiarity with JavaScript, TypeScript, or Python

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
collections:
    - some-non-existent-collection
---

This is the actual content of the tutorial.
