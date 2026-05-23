---
title_tag: "Pulumi Cloud | Pulumi Concepts"
meta_desc: Pulumi Cloud is Pulumi's default state backend and adds access control, secrets, policy enforcement, and drift detection for teams operating at scale.
title: Pulumi Cloud
h1: Pulumi Cloud
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi Cloud
        parent: iac-concepts
        weight: 5
aliases:
    - /docs/iac/concepts/pulumi-cloud/
---

Pulumi Cloud is the default [state backend](/docs/iac/concepts/state-and-backends/) for the Pulumi CLI. It is also a managed platform that adds the capabilities teams need to operate Pulumi at scale: access control, reusable configuration and secrets, policy enforcement, cloud resource inventory, scheduled drift detection, managed deployments, and an AI agent. Using Pulumi Cloud is optional; Pulumi also works with a [self-managed (DIY) backend](/docs/iac/operations/stack-management/using-a-diy-backend/). Pulumi Cloud is the default because it removes the work of running, securing, and scaling a backend yourself.

On top of state, Pulumi Cloud adds:

- **[Role-based access control](/docs/administration/organizations-teams/teams/)** with SAML/SSO integration and fine-grained [access tokens](/docs/administration/access-identity/access-tokens/) for automation.
- **Reusable configuration and secrets** via [Pulumi ESC](/docs/esc/), so environments can be defined once and consumed across stacks.
- **[Policy as code](/docs/insights/policy/)** enforcement applied centrally to every update, with pre-built policy packs for common security, compliance, and cost rules.
- **[Cloud resource inventory](/docs/insights/)** that discovers resources across your cloud accounts, including resources not managed by Pulumi.
- **Scheduled [drift detection](/docs/deployments/deployments/drift/)** that alerts you or remediates automatically when deployed infrastructure diverges from its declared state.
- **Managed [deployments](/docs/deployments/deployments/)** that run Pulumi operations remotely, for example in response to Git pushes, and emit [webhooks](/docs/deployments/webhooks/) for event-driven workflows.
- **[Pulumi Neo](/docs/ai/)**, an AI agent that helps debug deployments, write infrastructure as code, and answer questions about your environment.
- **Ephemeral environments** such as Review Stacks and TTL Stacks.

Pulumi Cloud is available as a hosted SaaS and as a [self-hosted](/docs/pulumi-cloud/self-hosted/) edition you can run in your own environment. The Individual tier is free. [Sign up for a Pulumi account](https://app.pulumi.com/signup) to get started.

For a detailed, capability-by-capability comparison of Pulumi Cloud and open source Pulumi, including which features are available with each option and what operational concerns each one entails, see [Pulumi Cloud vs. OSS](/docs/iac/guides/basics/pulumi-cloud-vs-oss/).
