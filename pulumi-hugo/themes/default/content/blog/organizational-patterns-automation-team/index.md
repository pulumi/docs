---
title: "Organizational Patterns - An Automation Team"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2021-12-22T11:49:08-06:00

# Draft posts are visible in development, but excluded from production builds.
# Set this property to `false` before submitting your post for review.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: In this continuing series, we explore an organizational pattern of using Pulumi - a specialized automation team.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - matt-stratton

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - development-environment

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---
Using Pulumi is more than just writing code and components. In addition to common software development practices, there are also a number of success patterns related to how your company or team builds and deploys Pulumi programs to successfully build, deploy, and manage your infrastructure and applications. In this continuation of a series, I will explore one of these patterns - a specialized automation team.

<!--more-->
I want to approach this pattern with a bit of caution - there are patterns and anti-patterns related to having a single central team focused on automation.

The anti-pattern is to have an "automation team" within your organization who is tasked with creating all infrastructure as code for the entire organization. This is a common pattern, but it is generally rife with issues.

Understanding how to build and deploy a service or application requires a certain amount of domain knowledge of that service. If you have a single set of people across your entire company who need to write Pulumi programs for each and every application or service, you are now expecting that small group to not only be experts in Pulumi, but also every bit of infrastructure and software applications (both third party and created internally) across your organization.

A more successful pattern is to have the automation team act as enablers and providers for the other groups within the company. This is a team of subject matter experts in using Pulumi, and not only do they have the knowledge to build and deploy infrastructure, but they are familiar with various patterns and good practices for how to build and deploy infrastructure.

There are different mechanisms for how this automation team can enable others. One way is to embed them temporarily within a product team to work alongside them to build their automation. Then, when the product team is done, the automation team member can go and help another squad.

Depending upon the size and skills of the company and this group, they may also be responsible for creating training materials for the other groups. These are usually based upon existing Pulumi training materials, but customized for the specific needs and culture of the company.

## Reusable components

This central automation team also often provides reusable components that might be shared across multiple development teams. This helps the individual teams to not have to "reinvent the wheel" and to bring in these components for their own particular needs.

As a simple example, a component could be created (and published as a library to be consumed by product teams) that defines a Kubernetes deployment.

```javascript
import * as deploy from "@mycorp/deploy";

const kuard = new deploy.Deployment("kuard", {
    image: "gcr.io/kuard-project/kuard:latest",
    replicas: 1,
});

```

What's happened here in our (incomplete!) example is that the published package only exposes the parts that the team needs to change; the rest is provided by the automation team.

The application team don’t need to duplicate values (such as ports) because the abstractions cater for them. The application team also didn’t need to apply any metadata, health checks, and environment variables because it can be inferred through convention, increasing velocity across the organization. When values are provided by the application team, they override convention and they can still iterate and experiment, providing feedback to the automation team.

## Final tips

One of the more important recommendations for this pattern is to avoid trying to create a "mandate" for all teams for adoption. The automation team provides capabilities, such as templated CI/CD pipelines, reusable components, and training materials, but it is still up to the individual teams to decide how to use them.

## Conclusion

This is a pattern that works well at a larger organization, where it would be beyond the scope of a single group to be able to wrap their understanding around hundreds of services. However, it is a pattern that can be applied to smaller organizations as well!

Watch for the next post in this series, where we will dig into some other patterns! Or revist the first post, [Organizational Patterns - A Single Infra Repo](https://www.pulumi.com/blog/organizational-patterns-infra-repo/).
