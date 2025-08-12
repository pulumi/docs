---
title_tag: "Pulumi Provider Version Support"
meta_desc: "Learn best practices for maintaining up-to-date pulumi applications"
title: Pulumi Provider Version Support
h1: Pulumi Provider Version Support
meta_image: /images/docs/meta-images/docs-meta.png
weight: 6
menu:
    iac:
        name: Version Support
        parent: iac-support
        weight: 6
---


Pulumi focuses on actively supporting the latest released version of the providers we maintain.
While we do not formally designate older versions for long term support,
we are committed to helping our users succeed and continuously improve our providers based on community feedback and contributions.
We encourage users to update to the latest versions to benefit from the most recent features, bug fixes, and security enhancements.
You can find the current version for all providers maintained by Pulumi in the [Pulumi Registry](https://www.pulumi.com/registry/)

## Recommendations for provider version maintenance

**When a major version is released, that is a signal to begin planning a provider version update.**
Major versions typically include significant changes such as deprecations, new resources and new functionality, which may require some additional migration steps.
Planning ahead allows teams to assess the impact of these changes, allocate resources for migration, and test compatibility thoroughly, minimizing disruption to existing infrastructure.

**At least quarterly, consider updating to the latest minor version on the current major, and minimally review provider release notes.**
Minor versions typically include new resources and features, as well as performance improvements, and bug fixes without introducing breaking changes.
Regular updates ensure access to these benefits and prevent falling too far behind, making future updates easier.
The release notes for each provider release summarize the new capabilities or fixes so you can identify changes relevant to your usage.

**Always allow patch updates on the current minor, for example, using the tilde operator in npm: \~1.2.3**
Patch versions are primarily for bug fixes and security updates and are designed to be fully backward compatible.
Automatically applying these updates ensures that known vulnerabilities are addressed and critical bugs are resolved without requiring manual intervention,
improving the stability and security of your deployments.

**Never be 2 major versions behind, as it is inadvisable to jump a major version due to the number of potential breaking changes across the major versions.**
Major versions typically include significant changes which may require some additional migration steps.
Each major version of the provider includes migration logic to smooth the upgrade from the immediately previous major version,
but these migrations do not always work across multiple major versions.
Being two or more major versions behind can accumulate a significant number of changes and may require a multi-step upgrade,
making the upgrade process more complex, time-consuming, and prone to errors.
