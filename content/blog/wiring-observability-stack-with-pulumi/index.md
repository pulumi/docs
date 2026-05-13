---
title: "Wire Datadog, New Relic, and PagerDuty with Pulumi"
date: 2026-06-11
meta_desc: "Use Pulumi to connect Datadog, New Relic, and PagerDuty as an observability baseline with monitors, alerts, escalation, and incident routing."
meta_image: meta.png
feature_image: feature.png
authors: ["pablo-seibelt"]
tags: ["datadog", "new-relic", "pagerduty"]
social:
    twitter: |
        Observability tools fail when monitors, alerts, and escalation live in separate clickops islands.

        Wire Datadog, New Relic, and PagerDuty with Pulumi.
    linkedin: |
        Observability stacks are only useful when telemetry, alerting, and escalation are connected.

        This guide shows how to wire Datadog, New Relic, and PagerDuty with Pulumi so monitors, alerts, and incident routing stay repeatable.
    bluesky: |
        Wire Datadog, New Relic, and PagerDuty with Pulumi so monitors, alerts, and escalation do not drift apart.

        Learn more in the post.
---

SRE teams often face a "telemetry gap" where critical incidents fall between disconnected monitoring tools. A [Datadog](https://www.datadoghq.com/) monitor might trigger, but if the corresponding [PagerDuty](https://www.pagerduty.com/) service is missing the correct runbook link or escalation path, the on-call engineer is left flying blind. Manually wiring these tools together for every new service is a recipe for inconsistent alerting, leading to missed signals or alert fatigue from misconfigured thresholds that no longer match service behavior.

The cost of an uncoordinated observability stack is measured in Mean Time to Resolution (MTTR). When your [New Relic](https://newrelic.com/) monitoring, logging, and incident response tools are managed as separate "islands" of configuration, you lose the consistent tagging and context needed for rapid triage. Using Pulumi to wire your observability stack ensures that every service starts with a complete, validated incident response path, reducing the risk of critical failures going unnoticed.

<!--more-->

## What you'll build

In this post, you will learn how to wire Datadog, New Relic, and PagerDuty together using Pulumi. You will build:

1. **PagerDuty services routed to an existing escalation policy** to define who gets paged and when.
2. **Datadog monitors** that automatically route alerts to the correct PagerDuty service.
3. **New Relic alert conditions** with consistent tags and runbook context.
4. **Unified tagging** across all three providers to ensure fast navigation during an incident.

By the end, you will have a cohesive observability stack that eliminates the telemetry gap and provides your on-call engineers with the context they need to resolve incidents faster.

## Managing Credentials with [Pulumi ESC](/docs/esc/)

Before we dive into the code, we need to handle our provider credentials. Using [Pulumi ESC](/docs/esc/), we can securely manage API keys for Datadog, New Relic, and PagerDuty without hardcoding them or passing them as environment variables manually.

```yaml
# observability-env.yaml
values:
  datadog:
    apiKey:
      fn::secret: datadog-api-key
    appKey:
      fn::secret: datadog-app-key
  newrelic:
    apiKey:
      fn::secret: newrelic-api-key
  pagerduty:
    token:
      fn::secret: pagerduty-token
  environmentVariables:
    DATADOG_API_KEY: ${datadog.apiKey}
    DATADOG_APP_KEY: ${datadog.appKey}
    NEW_RELIC_API_KEY: ${newrelic.apiKey}
    PAGERDUTY_TOKEN: ${pagerduty.token}
```

## The Implementation

Here is a TypeScript program that wires these three providers together. We'll create a PagerDuty service, a Datadog monitor that notifies that service, and a New Relic alert policy with a notification channel.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as datadog from "@pulumi/datadog";
import * as newrelic from "@pulumi/newrelic";
import * as pagerduty from "@pulumi/pagerduty";

// Create a PagerDuty service for the application
const appService = new pagerduty.Service("app-service", {
    name: "My Application Service",
    autoResolveTimeout: 14400,
    acknowledgementTimeout: 1800,
    escalationPolicy: "P123456", // Replace with your escalation policy ID
});

// Create a Datadog monitor that notifies PagerDuty
const cpuMonitor = new datadog.Monitor("cpu-monitor", {
    name: "High CPU Usage",
    type: "metric alert",
    query: "avg(last_5m):avg:system.cpu.idle{host:host0} < 20",
    message: pulumi.interpolate`CPU usage is high on {{host.name}}. Notify: @pagerduty-${appService.name}`,
    tags: ["service:my-app", "env:prod"],
});

// Create a New Relic alert policy
const policy = new newrelic.AlertPolicy("app-policy", {
    name: "My Application Policy",
});

const notificationChannel = new newrelic.AlertChannel("on-call-email", {
    name: "On-call Email",
    type: "email",
    config: {
        recipients: "on-call@example.com",
        includeJsonAttachment: "1",
    },
});

const policyChannel = new newrelic.AlertPolicyChannel("app-policy-channel", {
    policyId: policy.id,
    channelIds: [notificationChannel.id],
});

// Create a New Relic alert condition routed through the policy channel
const condition = new newrelic.NrqlAlertCondition("high-error-rate", {
    policyId: policy.id,
    name: "High Error Rate",
    nrql: {
        query: "SELECT count(*) FROM TransactionError WHERE appName = 'My App'",
    },
    critical: {
        operator: "above",
        threshold: 5,
        thresholdDuration: 300,
        thresholdOccurrences: "ALL",
    },
});
```

## Validation

After running `pulumi up`, you can validate your observability stack:

1. **PagerDuty Integration**: Check the "Integrations" tab of your PagerDuty service to confirm that the Datadog integration key is correctly configured.
2. **Monitor Test**: Manually trigger a test alert in Datadog and verify that a PagerDuty incident is created with the correct service and tags.
3. **New Relic Routing**: Trigger the NRQL condition and verify that New Relic sends a notification through the configured policy channel.

By wiring your observability stack as code, you ensure that every service is monitored from day one and that your on-call engineers always have the context they need to resolve incidents quickly.
Pulumi allows you to promote these configurations across environments. You can have a "staging" observability stack that notifies a Slack channel and a "production" stack that triggers PagerDuty.

By treating your monitors and dashboards with the same rigor as your infrastructure, you eliminate "monitoring debt" and ensure that your team is always ready for the next incident.

## Conclusion

Wiring Datadog, New Relic, and PagerDuty with Pulumi gives you a unified, version-controlled view of your entire observability posture. Whether you're managing a small service or a large fleet, Pulumi provides the scale and flexibility needed for modern operations.
