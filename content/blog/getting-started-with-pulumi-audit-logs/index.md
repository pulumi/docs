---
title: "Getting Started with Pulumi Audit Logs"
date: "2020-02-10"
meta_desc: "Get started with audit logs"
meta_image: "pulumi-webhooks.png"
authors: ["sean-holung"]
tags: []
---

We are excited to announce the release of Audit Logs on
[Pulumi](https://app.pulumi.com) for enterprise organizations.
Audit logs enable you to track the activity of users within an
organization. Audit logs attempt to answer who did what, when
they did it and where. Pulumi audit logs help answer these questions
by recording entries for activities invoked by users.

Pulumi's audit logs allow you to account for the activity your
users are taking within your organization. These logs are available to
organizations with an Enterprise level subscription. Pulumi audit logs are
recorded whenever a user invokes an action. This allows the activity
of members in an organization to be traced. Our Audit logs are immutable.
They are recorded with the UNIX timestamp of the event, the user
who invoked the action, the event, and the source IP of the call being made.

## Using Pulumi Audit Logs

Audit logs are available to organizations with an "Enterprise" subscription
only. You can view the audit logs for your organization given that you
are an organization admin, by selecting your organization from the
organization drop down in the organization settings menu. Then clicking on
the settings tab. On the left nav-bar you should see a tab called Audit Logs.
Clicking here will allow you to view the most recent audit logs for your
organization.

![auditlogs](./auditlogs.png)

It will show the most recent events in decending order. You can
also filter logs by a particular user by clicking on the user's avatar. This will
filter out the events by the user you selected. You can also filter by user by
adding a query param to the url with the user's login name.