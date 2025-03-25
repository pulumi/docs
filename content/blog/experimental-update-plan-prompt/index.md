---
title: New CLI prompt to use Update Plans
date: 2022-11-23T06:00:00-07:00
meta_desc: Pulumi up will now prompt for users to try using update plans.
meta_image: meta.png
authors:
  - fraser-waters
  - mikhail-shilkov
tags:
  - features
  - plans
search:
  keywords:
    - plans
    - prompt
    - update
    - cli
    - try
    - new
    - use
---

Earlier this year we announced the experimental introduction of Update Plans as we heard from many of you that you need a strong guarantee about exactly which changes an update will make to your infrastructure, especially in critical and production environments. We have been making steady progress on this feature and are excited to further integrate it into your workflows. In the latest release of the Pulumi CLI ([v3.48.0](https://github.com/pulumi/pulumi/releases/tag/v3.48.0)), there’s a new prompt to use experimental Update Plans when running an update.

## Why use Update Plans

Update Plans help catch any unexpected changes that might happen between when you preview a change and when you apply that change. Update Plans work by saving the results of a `pulumi preview` to a plan file, which enables you to restrict subsequent `pulumi up` operations to only the actions saved in the plan file. ​​This helps you ensure that what you saw in the `pulumi preview` is what will actually happen when you run `pulumi up`.

With Update Plans, this same workflow is now possible with infrastructure managed by Pulumi. Assuming you already have CI set up for your pull/merge requests, you can run `pulumi preview --save-plan PLAN-FILENAME` and output the resulting plan file as a CI artifact. Then, update the CI workflow that runs when changes are merged to run `pulumi up --plan PLAN-FILENAME`.

Until now to leverage Update Plans users had to pass `--save-plan <file>` and `--plan <file>` options while using non-interactive CLI commands `preview` and `up` respectively with the `PULUMI_EXPERIMENTAL=true` environment variable. This restriction limited the feature discoverability, while enabling us to scale gradually. The `--save-plan <file>` and `--plan <file>` options continue to be available and still require a `PULUMI_EXPERIMENTAL=true` environment variable.

## New option in CLI interactive prompt

We believe that Update Plans have matured to be evaluated by our larger community. To make it more visible, we are introducing a new option to the update confirmation prompt. If you run a `pulumi up` command interactively, you will now see the following choice:

```bash
Do you want to perform this update?  [Use arrows to move, type to filter]
> [experimental] yes, using Update Plans (https://pulumi.com/updateplans)
  yes
  no
  details
```

The `no` option is still the default choice, and the `yes` option is still immediately above it, so the change will hopefully align with user habits. However, there is a top option added, which suggests running an update with a plan built during the preview.

Each interactive preview now calculates an Update Plan. If you choose the `yes, using Update Plans` option, the Update Plan will be automatically passed to the update command and applied during the deployment. Any inconsistencies between the preview and the update will be reported back to the user.

## Try Update Plans

{{% notes type="info" %}}
Update Plans are in public preview. We recommend using it only in non-critical, non-production scenarios during the preview period.
{{% /notes %}}

We’re eager for you to try the public preview of Update Plans and let us know what you think. To try out the new interactive option, make sure you’ve updated to Pulumi 3.48.0 or higher.

We’d love to hear your thoughts on the Update Plans feature! Feel free to ask questions in our [Slack](https://slack.pulumi.com/) or open an issue on [GitHub](https://github.com/pulumi/pulumi).
