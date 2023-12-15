---
title: "Introducing the Pulumi Cloud Team Edition Cost Calculator"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-12-15T15:54:54-08:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Introducing the new Pulumi Cloud Team edition pricing calculator to make estimating new costs for prospective customers easier than ever.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: pricing-calc-meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features
    - pricing

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Pulumi Cloud pricing is straightforward- a charge per resource hour for every resource managed by Pulumi Cloud and a charge for every deployment minute (only applicable if using Pulumi Deployments). However, when prospective customers first look at Pulumi Cloud costs it can be overwhelming to determine what your workload will look like and then do the math.

Today we are making available a simple tool for estimating your cost on the Team Edition of Pulumi Cloud to get prospective customers to the information as quickly as possible.
<!--more-->

Just input the number of resources in all your cloud accounts and the percentage of time they will be up (12 hours a day would be 50% of the time) and you have an estimate of your costs! If you are already using Pulumi for your Infrastructure as Code (IaC) you can run a `pulumi preview` to see the resource count in a stack. Add your estimated deployment minutes to see Pulumi Deployments costs included. The amount of time it takes to run an update on a stack locally is a good starting place for estimating deployment costs. Toggle from Per Month to Per Day to see your daily cost estimate instead of monthly.

{{< blog/cta-button "Calculate Pulumi Cloud Costs" "/pricing/#calculator" "_blank" >}}

![Screenshot of the pricing calculator](pricing_calc.png)

What inputs are required:

- Number of resources
- Utilization
- Deployment minutes (optional)

The pricing calculator then provides:

- Estimated cost per month or day
- Free credits included
- Cost per credit

And just like that you have your estimate! For customers who will be spending over $20,000 a year, please [contact sales](https://www.pulumi.com/contact) to see what bulk discount options are available for your organization.
