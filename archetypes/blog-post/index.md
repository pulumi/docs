---
title: "{{ replace .Name "-" " " | title }}"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: {{ .Date }}

# Draft posts are visible in development, but excluded from production builds.
# Set this property to `false` before submitting your post for review.
draft: true

# Use the optional meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. If omitted or left blank, the content preceding the `<!--more-->` token
# will be used in its place.
meta_desc:

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - joe-duffy

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - change-me

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

What you put here will appear on the index page. In most cases, you'll also want to add a Read More link after this paragraph (though technically, that's optional). To do that, just add an HTML comment like the one below.

<!--more-->

And then everything _after_ that comment will appear on the post page itself.

Either way, avoid using images or code samples [in the first 70 words](https://gohugo.io/content-management/summaries/#automatic-summary-splitting) of your post, as these may not render properly in summary contexts (e.g., on the blog home page or in social-media previews).

## Writing the Post

For help assembling the content of your post, see [BLOGGING.md](https://github.com/pulumi/docs/blob/master/BLOGGING.md). For general formatting guidelines, see the Style Guide section of [CONTRIBUTING.md](https://github.com/pulumi/docs/blob/master/CONTRIBUTING.md#style-guide).

## Code Samples

```typescript
let bucket = new aws.s3.Bucket("stuff");
...
```

## Images

![Placeholder Image](meta.png)

## Videos

{{< youtube "kDB-YRKFfYE?rel=0" >}}

Note the `?rel=0` param, which tells YouTube to suggest only videos from same channel.

## Tweets

{{< tweet 1147203941609984002 >}}
