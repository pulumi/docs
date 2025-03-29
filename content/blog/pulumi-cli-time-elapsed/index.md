---
title: "Pulumi CLI now displays time elapsed per resource"
date: 2022-11-03T11:19:51-06:00
draft: false
meta_image: meta.png
meta_desc: See deployment times across different types of cloud provider resources.
authors:
  - kyle-dixler
tags:
  - pulumi
  - features
search:
  keywords:
    - CLI
    - resources
    - deployment times
    - cloud provider
---

If you’ve deployed resources to your favorite cloud provider, you have probably found yourself sitting in the console thinking: “I don’t know how long this is going to take.” Then you deploy the resource and think: “When did I even start this?” When using Pulumi, the CLI prints out how long the update took after it ran, but while you’re in the moment, it feels like ages.

## We’re excited to announce a CLI usability enhancement

**You can now see how long each of your resources are taking to deploy.**

When you run `pulumi up`, you’ll see that individual resources have the time taken displayed during updates including up, destroy, import, and refresh.

{{< asciicast id="5Qf4oLoYOWvUHUMUXcPjHvXxL" >}}

## Comparing resource deployment times

I have a contrived Pulumi program that deploys comparable resources in AWS and GCP and you can see the differences in deployment times between them. It provides a rough idea of the orders of magnitude in deployment time between different resource classes.

Here’s a screenrecording of the output of the program (it took fairly long):

{{< asciicast id="8ZZe6iegHnahrPt8PpXSJtEnr" >}}

For those interested, the code is located [here](https://gist.github.com/dixler/d54883b399d31d934188a36f08ae9e77).

This is far from a perfect example. These numbers have many sources of error, including the load on the cloud provider, the chosen availability zone, quotas and throttling, whether the resource is ready for requests, inefficient resource options, and size of the images (for compute resources). Nonetheless, it provides more perspective as instead of a feeling short or long, we now see concrete numbers to help us quantify it.

Thanks for reading. If you have any feedback on how we can further improve our CLI experience, let us know by commenting or upvoting open issues tracking enhancements on [GitHub](https://github.com/pulumi/pulumi). If you can’t find an existing issue, feel free to open a new one!
