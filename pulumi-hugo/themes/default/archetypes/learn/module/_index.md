---
title: "{{ replace .Name "-" " " | title }}"
layout: module

# The date represents the date the course was created. Posts with future dates are visible
# in development, but excluded from production builds. Use the time and timezone-offset
# portions of of this value to schedule posts for publishing later.
date: {{ .Date }}

# Draft posts are visible in development, but excluded from production builds.
# Set this property to `false` before submitting the module for review.
draft: true

# The description summarizes the course. It appears on the Learn home and module index pages.
description: Here is a brief description of what this module's all about.

# The meta_desc property is used for targeting search results or social-media previews.
meta_desc: Here is a brief description of what this module's all about.

# The order in which the module appears on the home page.
index: 0

# The meta_image appears in social-media previews and on the Learn Pulumi home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for reference.
meta_image: meta.png

youll_learn:
    - Stuff
    - Things
    - Whatnot

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - change-me

# At least one provider is required.
providers:
    - aws
---

This is the content that will appear at the top of the module index page. It should
describe the overall goal of the module and briefly summarize what the reader will know
how to do by the end of it.
