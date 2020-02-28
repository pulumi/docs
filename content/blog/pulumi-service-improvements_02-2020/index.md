---
title: "Pulumi Console Improvements, February 2020"
authors: ["chris-smith"]
tags: ["pulumi","new-features"]
date: "2020-02-28"
meta_desc: "Recent improvements to the Pulumi Console: stack tags, audit logs, CI/CD integration, downloadable checkpoint files"
meta_image: "pretty-print-multiline-json.gif"
---

Hello! Many posts here on the [Pulumi blog]({{< relref "/blog" >}}) describe new features in our core libraries or
command-line client. But in this post, we'll highlight some of the recent improvements to the [Pulumi Console](https://app.pulumi.com).

We've been hard at work making it easier to manage stacks, permissions, and organizations. So we're super-excited to showcase
what's new!

<!--more-->

## First-class Support for Tags

Pulumi has had support for [stack tags]({{< relref "/docs/intro/concepts/stack#stack-tags" >}}) for a while, enabling
you to add attributes to your stacks with custom data such as the `account-id` or `environment`. But previously the data was
only available on the command-line, via the `pulumi stack tag` command ([documentation]({{< relref "/docs/reference/cli/pulumi_stack_tag" >}})).

We've now added first-class support for stack tags in the Pulumi Console as well. You can create, update, and delete tags from within the console.

![Updating stack tags within the Pulumi Console](./update-tags-in-console.png)

But making it easier to create and edit tag data is just the beginning. We've started to add new search/filtering capabilities
based on stack tags. For example, you can now use filters to more quickly add stacks to [Pulumi teams]({{< relref "/docs/intro/console/collaboration/teams" >}}).

![Filtering stacks by their tags](./filter-stacks-by-tag.png)

We will continue wiring stack tags throughout other parts of the Pulumi Console, so stay tuned! Also, this new feature was
added by Pulumi's first (and extremely awesome) intern, Tasia (👋)!

## Deep Linking into CI/CD Systems

We've also added deep links from the Pulumi Console to the CI/CD job or task that performed an update. So depending on
how you practice [continuous delivery using Pulumi]({{< relref "/docs/guides/continuous-delivery" >}}), you’ll now see
links to things like the [Circle CI job](http://circleci.com) or [Travis CI build](http://travis-ci.com) as appropriate.

![Link to the Travis CI Build from the Pulumi Console](./deep-linking-cicd-providers.png)

> Pulumi supports a variety of CI/CD providers, but if yours isn't listed in [our CI/CD guide]({{< relref "/docs/guides/continuous-delivery" >}})
> [let us know](https://slack.pulumi.com) or [contribute it](https://github.com/pulumi/pulumi/tree/master/pkg/util/ciutil)
> on your own.

## Pretty Printing JSON / Multi Configuration

We now pretty print configuration values that look like JSON, and have much better support for viewing multi-line data.

![JSON and mutiline configuration values](./pretty-print-multiline-json.gif)

## Download Earlier Checkpoints

The most important job of the Pulumi Console is to maintain a durable, accurate snapshot of your cloud resource data.
While in most cases your [stack's checkpoint data]({{< relref "/docs/intro/concepts/state" >}}) is a low-level detail
you don't need to worry about, in some advanced scenarios you may need to inspect or edit it manually.

You can now download a stack’s checkpoint file directly from the Pulumi Console. You can also access the
same data from the command-line, using `pulumi stack export` ([documentation]({{< relref "/docs/reference/cli/pulumi_stack_export" >}})),
which now supports a `--version` flag to export older checkpoint files too.

![Download stack checkpoints from the Pulumi Console](./download-checkpoint-file.png)

## Reverse Stack Permissions View

The Team Pro and Enterprise editions support [role-based access control]({{< relref "/docs/intro/console/collaboration/stack-permissions" >}})
using [teams]({{< relref "/docs/intro/console/collaboration/teams" >}}). But a common problem we've heard from people in large organizations
is that it can be difficult to review exactly *_what_* access someone has to a stack and *_why_*.

That's why the recent feature I'm personally the most excited about, is the ability for organization administrators to drill into their
members and review stack permissions.

You can see what stacks a member has access to.

![Stacks an organization member has access to](./list-of-accessible-stacks.png)

And also see what sources are granting that access.

![Sources granting stack permissions](./stack-access-grants.png)

## Log Rendering Performance

Sadly, there isn't a useful screen shot to go along with this improvement. But we've made some changes that dramatically
improve the Pulumi Console's performance when rendering update logs for large stacks.

## Audit Logs

Users of Pulumi Enterprise typically have a lot of stacks and teams. This can make it difficult to review what's currently in-motion
and to understand a sequence of events a few days or few weeks in the past.

[As we announced earlier]({{< relref "/blog/auditing-your-organizations-infrastructure-as-code-activity" >}}) we launched the ability to view
and download audit logs with all the changes within an organization.

![Audit logs of recent changes within an organization](./audit-logs.png)

Phew! Like I said, we've been busy this month working on the Pulumi Console. And there is plenty more awesomeness still in the pipe!
If you want to get a peek at other things in-development, check out the [Pulumi 2.0 Roadmap]({{< relref "/blog/pulumi-2-0-roadmap" >}}).

As always, we love to hear if you have any feedback, suggestions, or ideas for other improvements we could make to the
Pulumi Console. Just let us know on the [Pulumi Community Slack](https://slack.pulumi.com), Twitter [@PulumiCorp](https://twitter.com/pulumicorp),
or [on GitHub](https://github.com/pulumi/pulumi).
