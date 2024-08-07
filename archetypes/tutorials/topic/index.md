---
title: "{{ replace .Name "-" " " | title }}"
title_tag: "{{ replace .Name "-" " " | title }}"
layout: topic

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

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

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

# If you's like to add this tutorial to a collection, add a collection ID here. Collections
# are optional and are defined in data/tutorials/collections.yaml.
collections:
    - some-collection
---

This is the content that will appear at the top of the topic page. It should describe the overall goal of the module and briefly summarize what the reader will know how to do by the end of it.

## This is a heading

## This is another heading

```typescript
let bucket = new aws.s3.Bucket("stuff");
...
```

## Images

![Placeholder Image](meta.png)

## Videos

{{< youtube "kDB-YRKFfYE?rel=0" >}}

Note the `?rel=0` param, which tells YouTube to suggest only videos from same channel.
