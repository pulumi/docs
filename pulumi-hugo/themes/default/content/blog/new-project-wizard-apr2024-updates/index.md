---
title: "Org-only Template Gallery and Setting Default Repositories: Streamline Your Development"
allow_long_title: True
date: 2024-04-19
draft: false
meta_desc: Pulumi Cloud adds new usability improvements that give more control to platform teams and streamline the New Project Wizard flow to deploy infrastructure 
meta_image: meta.png
authors:
    - arun-loganathan
tags:
    - features
    - new-project-wizard
    - developer-portals
    - platform-engineering

---

We're constantly evolving the [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard/) to make it the preferred choice for platform teams to empower their internal teams to deploy resources quickly and in adherence to organizational standards. In January, we launched the [Developer Portal Gallery](/blog/developer-portal-gallery/) to boost development velocity and reduce operational friction.  Since then, we have seen strong adoption from our customers and received several new requests. We are excited to share the latest improvements we've made. 

<!--more-->

## Primer on New Project Wizard and Developer Portal Gallery

### The New Project Wizard
The New Project Wizard is a core component of [Pulumi for Developer Portal](/blog/building-developer-portals/) that guides users through a structured process to deploy infrastructure resources through Pulumi. It allows users to select from pre-defined templates or generate new programs through Pulumi AI, configure, and deploy them without leaving the browser. This wizard significantly reduced the time and effort required to get projects off the ground, enabling developers to concentrate more on their development tasks and less on initial setup. Platform teams using the New Project Wizard do not have to custom-build and maintain complex tooling.

### Overview of the Developer Portal Gallery
The Developer Portal Gallery allows platform teams to curate and distribute approved project templates within their organization. This feature supports compliance and standardization by ensuring that all projects adhere to organizational policies and best practices right from the start. The gallery not only facilitates the discovery and use of these templates but also makes it easy for developers to start new projects with templates that are pre-vetted and ready to deploy. 

Using the Developer Portal Gallery can enhance collaboration across teams by standardizing the tools and processes used for creating and deploying projects. This alignment helps in maintaining a high level of governance as projects scale and ensures consistency across the development lifecycle. Platform teams can oversee template usage and configurations, making sure that each project conforms to the required security, architecture, and performance standards.

## What's New?

Here’s a breakdown of the latest enhancements:

### Org-only Template Sources
Previously, the Developer Portal Gallery included both the Organization's custom templates as well as Pulumi-authored templates. With this update, you can now add or remove the Pulumi-authored templates, ensuring that users only deploy organizationally approved templates. This simplifies template discovery and selection, reinforcing governance and compliance across development projects.

{{< video title="Org-only Template Sources" src="./org-only-templates.mp4" width=600 height=420 autoplay="true" loop="true" >}}

### Default Repository Locations
We heard from customers they want their developers to not even have to worry about what repo their Pulumi code lives in. Starting today, admins can set default repository locations for each template source within the gallery. This eliminates the need for developers to select a repository, automatically using predetermined locations and streamlining their deployment process. 

{{< video title="Org-only Template Sources" src="./default-repos.mp4" width=600 height=420 autoplay="true" loop="true" >}}

### Auto-generated Project Names
Another improvement is the auto-generation of project names. Previously, users had to specify a project name, requiring additional input and sometimes leading to naming conflicts. Now, we automatically generate unique project names, further reducing friction and simplifying the project creation process.

## Wrapping up

We're continuously striving to make your experience with Pulumi Cloud as seamless and efficient as possible. Your feedback, big or small, is valuable to us, please feel free to share it in the [Pulumi Cloud Requests repository](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose).

Happy building!