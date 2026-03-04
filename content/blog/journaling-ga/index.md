---
title: "Now GA: Up to 20x Faster Pulumi Operations for Everyone"
allow_long_title: true
date: 2026-02-27
draft: false
meta_desc: "A major performance enhancement is now on by default for all Pulumi Cloud organizations. Faster operations, less network traffic, no opt-in required."
meta_image: meta.png
authors:
    - thomas-gummerer
    - pat-gavlin
tags:
    - performance
    - pulumi-cloud
    - features
    - releases
social:
    twitter: |
        Now GA: Up to 20x Faster Pulumi Operations for Everyone

        - Up to 92% faster state updates (p99)
        - 60% median improvement for large stacks (100+ resources)
        - 25% median improvement for smaller stacks
        - Zero config required — just upgrade to CLI v3.225.0+

        Your deploys just got a whole lot faster. https://www.pulumi.com/blog/journaling-ga/
    linkedin: |
        Now GA: Up to 20x Faster Pulumi Operations for Everyone

        In January we introduced a new state management approach that sends incremental changes instead of full snapshots. Today, it's enabled by default for every Pulumi Cloud organization. No environment variables, no feature flags, no opt-in. Just faster deploys.

        ## The numbers

        Since the opt-in launch, we've processed thousands of state updates across many organizations. Here's what we're seeing in production:

        - Stacks with &lt;100 resources: 25.3% median improvement, up to 92.6% faster at p99
        - Stacks with 100+ resources: 60.2% median improvement
        - p90 improvement: 75.2% for smaller stacks

        ## What changed

        Previously, Pulumi serialized full state snapshots at every step. For large stacks, this was a bottleneck. The new approach sends incremental entries in parallel; Pulumi Cloud reconstructs the full snapshot server-side.

        ## What you need to do

        Nothing. If you're on Pulumi CLI v3.225.0 or later, you're already getting the faster experience.

        Read more: https://www.pulumi.com/blog/journaling-ga/
---

In January, we [introduced a major performance enhancement for Pulumi Cloud](/blog/journaling/) through a fundamental change to how Pulumi manages state that speeds up operations by up to 20x. After a staged rollout across many organizations, **it is now enabled by default for every Pulumi Cloud operation**. No opt-in required—just use Pulumi CLI v3.225.0+ with Pulumi Cloud. The improvement applies to `pulumi up`, `pulumi destroy`, and `pulumi refresh`; `pulumi preview` does not modify state, so it is unchanged.

<!--more-->

## What this means for you

First and foremost, nothing about how you work with `pulumi` needs to change. Your updates now benefit from better parallelism and should thus complete faster. Before this change, `pulumi` always saved a full snapshot to the cloud, so the current state could always be recovered if something goes wrong. With journaling, we now only send the state of each operation, which allows us to send these updates in parallel, as long as resources are not related to each other. For the full deep dive, see the blog post linked above.

## Production results

Since January, we've had many early adopters of journaling. This helped us shake out one final bug on the server side, and journaling has been stable since then.  With that we feel confident in rolling this out to all our users.

We've also gathered some real-world data on how journaling is performing.  Unfortunately this data is quite noisy. Many updates, especially on smaller stacks are dominated by the time it takes to update Cloud resources, rather than the time `pulumi` takes.

Regardless, the data we do have shows some significant improvements for update times.  For stacks with fewer than 100 resources, the median improvement is 25.3%, while the p90 improvement is 75.2%, and we've seen a p99 improvement of up to 92.6%  Meanwhile, for larger stacks, the median improvement is 60.2%. Unfortunately we don't have as many stacks with more than 100 resources yet, so the p90 time there is not very significant.

This data already shows the expected significant improvement in update times, especially for larger stacks, though the improvements strongly depend on the shape and type of resources that are being set up. Stacks with many resources, that are quick to update benefit more than smaller stacks with slower to set up resources. For more numbers see also the [Benchmarks section in the previous blog post](/blog/journaling/#benchmarks)

## What you need to do

While this was an opt-in process using the `PULUMI_ENABLE_JOURNALING` environment variable, this opt-in is no longer required. Just upgrade your Pulumi CLI to v3.225.0+ and use the Pulumi Cloud backend, and journaling will automatically speed up your updates.

If you encounter any issues, reach out on the [Pulumi Community Slack](https://slack.pulumi.com/) or through [Pulumi Support](https://support.pulumi.com/hc/en-us).  You can also set the `PULUMI_DISABLE_JOURNALING=true` env variable to opt out of journaling.
