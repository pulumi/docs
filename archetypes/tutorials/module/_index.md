---
title: "{{ replace .Name "-" " " | title }}"
title_tag: "{{ replace .Name "-" " " | title }}"
layout: module

# The description summarizes the tutorial. It appears on the Learn home and module index pages.
description: Here is a brief description of what this module's all about.

# The meta_desc property is used for targeting search results or social-media previews.
meta_desc: Here is a brief description of what this module's all about.

# The order in which the module appears on the Tutorials home page. Higher numbers appear further
# down the list. Only positive integers are valid.
weight: 999

# The meta_image appears in social-media previews and on the Learn Pulumi home page.
# A placeholder image representing the recommended format, dimensions and aspect ratio
# has been provided for reference.
meta_image: meta.png

# A list of things the reader will know how to do by the end of this this tutorial. There
# should be at least three of these.
youll_learn:
    - How to do things
    - When to do things (and when not to)
    - Why it's better to do some things and not others

# A list of prerequisites. Markdown is acceptable.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts#access-tokens)
    - Familiarity with JavaScript, TypeScript, or Python

# If you'd like to add this tutorial to a collection, add a collection ID here. Collections
# are optional and are defined in data/tutorials/collections.yaml.
collections:
    - some-collection
---

This is the content that will appear at the top of the module index page. It should describe the overall goal of the module and briefly summarize what the reader will know how to do by the end of it.
