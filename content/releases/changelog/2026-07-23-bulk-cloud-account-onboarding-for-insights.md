---
title: "Bulk cloud account onboarding for Insights"
date: 2026-07-23
meta_desc: "Onboard AWS, Azure, and Google Cloud accounts to Pulumi Insights in bulk with the new Connect cloud accounts wizard, using OIDC with no long-lived secrets."
authors:
    - levi-blackstone
---

You can now connect your AWS, Azure, and Google Cloud accounts to [Pulumi Insights](/docs/insights/) in bulk. The new **Connect cloud accounts** wizard discovers the accounts in your AWS organization, Azure tenant, or Google Cloud organization and helps you connect them to Insights. With the recommended authentication options, no long-lived cloud secrets are stored in Pulumi Cloud.

Onboarding used to mean manual OIDC configuration and a hand-written [Pulumi ESC](/docs/esc/) environment for every account, which made complete coverage across hundreds of accounts, subscriptions, and projects hard to reach. The wizard takes a whole batch across all three clouds from disconnected to scanning in a few minutes.

Bulk onboarding is available now to organization admins and members with permission to connect cloud accounts. Read the [announcement blog post](/blog/connect-your-cloud-accounts-to-pulumi-in-minutes/) or the [Connect cloud accounts documentation](/docs/insights/discovery/connect-cloud-accounts/) to learn more.
