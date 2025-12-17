---
title: "Introducing Dark Mode for Pulumi Cloud"

date: 2025-12-17

meta_desc: Pulumi Cloud now features the ability to choose a dark or light theme.
meta_image: "meta.png"

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - kimberley-mackenzie

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - pulumi-service
    - user-experience

---
[Pulumi Cloud](/product/pulumi-cloud/) helps teams manage and operate their cloud infrastructure in one place, from state and secrets to deployments, visibility, and policy enforcement.

For a long time, one request has consistently come up from the Pulumi community: dark mode. Today, we’re announcing that this request is now available in Pulumi Cloud.

<!--more-->

## Light mode and dark mode

Pulumi Cloud supports light mode, dark mode, and a system default setting that follows your operating system preferences. You can switch themes at any time from your account settings.

### Below: Pulumi Cloud dashboard in light mode and dark mode

<div class="flex flex-col md:flex-row gap-4 my-4">
  <img src="dashboard-light.png" alt="Screenshot of Pulumi Cloud dashboard in light mode" class="w-full md:w-1/2" />
  <img src="dashboard.png" alt="Screenshot of Pulumi Cloud dashboard in dark mode" class="w-full md:w-1/2" />
</div>

Light mode remains the default experience. Dark mode uses lighter text and UI elements on a darker background, which many users prefer for extended sessions or low-light environments.

This update is enabled by recent work from our User Experience team to introduce a shared design system across Pulumi Cloud. With that foundation in place, theming can now be applied consistently across pages and features.

### Below: Pulumi Cloud resources page in light mode and dark mode

<div class="flex flex-col md:flex-row gap-4 my-4">
  <img src="resources-light.png" alt="Screenshot of Pulumi Cloud Resources page in light mode" class="w-full md:w-1/2" />
  <img src="resources.png" alt="Screenshot of Pulumi Cloud Resources page in dark mode" class="w-full md:w-1/2" />
</div>

Dark mode allows you to opt into a theme that uses lighter text and graphics on a darker background.  You can also choose to keep the current theme, now known as light mode, or follow your system preferences.

## How to enable dark mode

You can update your theme from your Account Settings at any time.

Select your profile image in the top-right corner of the Pulumi Cloud UI and navigate to **Account Settings**. In the **Preferences** section, choose the theme you want to use:

- Light mode
- Dark mode
- System default

!["Screenshot of Account Settings preferences"](preferences.png)

## Try out dark mode today

Want to try dark mode out for yourself? [Sign in](https://app.pulumi.com) to your Pulumi Cloud account, or if you are new to Pulumi, [create a free account](https://app.pulumi.com/signup).

We would love to hear your feedback. You can reach us in the [Pulumi Community Slack](https://slack.pulumi.com/?_gl=1*abbv2y*_ga*MTgxNzE0MTI3LjE2NDM3MzcwNTU.*_ga_FQHG5CVY2D*MTY1NzY0ODc4NC4xMzMuMC4xNjU3NjQ4Nzg0LjYw) or share requests in the [public GitHub repo](https://github.com/pulumi/pulumi-cloud-requests/issues).

We look forward to hearing what you think of these changes!
