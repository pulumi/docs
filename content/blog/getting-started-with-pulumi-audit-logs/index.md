---
title: "Getting Started with Pulumi Audit Logs"
date: "2020-02-10"
meta_desc: "Get started with audit logs"
meta_image: "pulumi-webhooks.png"
authors: ["sean-holung"]
tags: []
---

We are excited to announce the release of Audit Logs on
[Pulumi](https://app.pulumi.com) for Enterprise organizations.
Audit logs enable you to track the activity of users within an
organization. Audit logs attempt to answer who did what, when
they did it and where. They help answer these questions
by recording entries for activities invoked by users.

Pulumi's audit logs allow you to account for the activity your
users are taking within your organization. These logs are available to
organizations with an Enterprise level subscription. The logs are immutable and
are recorded whenever a user invokes an action. This allows the activity
of members in an organization to be traced.
The logs are recorded with the UNIX timestamp of the event, the user
who invoked the action, the event that took place, and the source IP 
of the call being made.

## Using Pulumi Audit Logs

Audit logs are available to organizations with an "Enterprise" level subscription
only. You can view the audit logs for your organization if you
are an organization admin, by selecting your organization from the
organization drop down. Then click on the settings tab. On the left nav-bar 
you should see a tab called Audit Logs. Clicking here will allow you to view 
the most recent audit logs for your organization.

![auditlogs](./auditlogs.png)

This will show the most recent events in decending order. You can
also filter logs by a particular user by clicking on the user's avatar. This will
filter out the events performed by the user you selected.

We are excited to make this feature available to our users. 
Get started with audit logs on [Pulumi](https://app.pulumi.com) today.
