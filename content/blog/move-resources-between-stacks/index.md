---
title: "Move Resources Between Stacks Or Projects"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-07-11T15:47:21+02:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Introducing the new pulumi state move command that allows moving resources between stacks and projects

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - thomas-gummerer

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - announcement
    - CLI


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Today we're announcing the [`pulumi state move`](https://www.pulumi.com/docs/cli/commands/pulumi_state_move/) command, which can be used to move resources that are managed by Pulumi between different stacks and/or projects.  No matter in which stack/project the resource was created in, it can now be moved with a single commmand.

<!--more-->

When refactoring a Pulumi project from a [monolithic](https://www.pulumi.com/docs/using-pulumi/organizing-projects-stacks/#monolithic) structure to [micro stacks](https://www.pulumi.com/docs/using-pulumi/organizing-projects-stacks/#micro-stacks), you might need to move resources between different projects or stacks, without recreating them. While this has been possible with some major surgery (our users came up with [automated solutions](https://github.com/pulumi/pulumi/issues/3389#issuecomment-679020482)), it's fairly error prone and difficult.  This makes refactoring Pulumi programs quite cumbersome, and having a simpler, integrated solution for this problem was a [much requested feature](https://github.com/pulumi/pulumi/issues/3389).

The `pulumi state move` command works as follows:

```
$ pulumi state move --help
Move resources from one stack to another

This command can be used to move resources from one stack to another. This can be useful when
splitting a stack into multiple stacks or when merging multiple stacks into one.

Usage:
  pulumi state move [flags] <urn>...

Flags:
      --dest string       The name of the stack to move resources to
  -h, --help              help for move
      --include-parents   Include all the parents of the moved resources as well
      --source string     The name of the stack to move resources from
  -y, --yes               Automatically approve and perform the move
```

Both `dest` and `source` can be either stacks in the current project, or stacks in a different project, using the fully qualified stack names.  Note that this works only for stacks within the same backend, it is currently not possible to move a resource between different backends.

The resources being moved have to be specified by their full URN, and multiple URNs can be passed at once.  For each resource being moved, all the children of that resource will also be moved, and the relationships between all resources being moved is preserved.  Resources with other types of dependencies will however not be moved to the target stack by default.

The command will make no attempt to adjust the users program.  Inputs and outputs from broken dependencies will have to be adjusted in the program where the resource is being managed after being moved.  This can be done either by using stack references, or recreating the inputs in the program.

The `pulumi state move` command is available in Pulumi v3.124.0 and later.

As always, we would love to hear your feedback in the [community slack](https://www.pulumi.com/community/).  If you encounter any issues with the command, please open an [issue](https://github.com/pulumi/pulumi/issues).
