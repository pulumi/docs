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

        See how to connect monitors, alert policies, and on-call routing as code.
---

SRE teams often face a "telemetry gap" where critical incidents fall between disconnected monitoring tools. A [Datadog](https://www.datadoghq.com/) monitor might trigger, but if the corresponding [PagerDuty](https://www.pagerduty.com/) service is missing the correct runbook link or escalation path, the on-call engineer is left flying blind. Manually wiring these tools together for every new service is a recipe for inconsistent alerting, leading to missed signals or alert fatigue from misconfigured thresholds that no longer match service behavior.

The cost of an uncoordinated observability stack is measured in Mean Time to Resolution (MTTR). When your [New Relic](https://newrelic.com/) monitoring, logging, and incident response tools are managed as separate "islands" of configuration, you lose the consistent tagging and context needed for rapid triage. Using Pulumi to wire your observability stack ensures that every service starts with a complete, validated incident response path, reducing the risk of critical failures going unnoticed.

<!--more-->

## What you'll build

In this post, you will learn how to wire Datadog, New Relic, and PagerDuty together using Pulumi. You will build:

1. **PagerDuty services routed to an existing escalation policy** to define who gets paged and when.
1. **Datadog monitors** that route alerts through an explicit Datadog-to-PagerDuty service object.
1. **New Relic alert conditions** routed through modern notification destinations, channels, and workflows.
1. **Shared incident context** across providers to ensure fast navigation during an incident.

By the end, you will have a cohesive observability stack that eliminates the telemetry gap and provides your on-call engineers with the context they need to resolve incidents faster.

## Managing credentials with Pulumi ESC

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
    subdomain: my-pagerduty-subdomain
    scheduleUrl: https://my-pagerduty-subdomain.pagerduty.com/schedules/P123456
  environmentVariables:
    DATADOG_API_KEY: ${datadog.apiKey}
    DATADOG_APP_KEY: ${datadog.appKey}
    NEW_RELIC_API_KEY: ${newrelic.apiKey}
    PAGERDUTY_TOKEN: ${pagerduty.token}
  pulumiConfig:
    observability:pagerDutySubdomain: ${pagerduty.subdomain}
    observability:pagerDutyScheduleUrl: ${pagerduty.scheduleUrl}
    observability:pagerDutyApiToken: ${pagerduty.token}
```

## The implementation

Here is a TypeScript program that wires these three providers together. We'll create a PagerDuty service, configure Datadog to route monitor notifications to that service, and create a New Relic alert policy routed through notification destinations, channels, and workflows. The Datadog PagerDuty integration is account-wide, so import it instead of creating it if your Datadog account already has PagerDuty configured.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as datadog from "@pulumi/datadog";
import * as newrelic from "@pulumi/newrelic";
import * as pagerduty from "@pulumi/pagerduty";

const config = new pulumi.Config("observability");
const pagerDutySubdomain = config.require("pagerDutySubdomain");
const pagerDutyScheduleUrl = config.require("pagerDutyScheduleUrl");
const pagerDutyApiToken = config.requireSecret("pagerDutyApiToken");
const serviceName = "my-application-service"; // Must be unique in the Datadog organization.
const datadogVendor = pagerduty.getVendor({
    name: "Datadog",
});

// Create a PagerDuty service for the application.
const appService = new pagerduty.Service("app-service", {
    name: "My Application Service",
    autoResolveTimeout: "14400",
    acknowledgementTimeout: "1800",
    escalationPolicy: "P123456", // Replace with your escalation policy ID.
});

const datadogIntegration = new pagerduty.ServiceIntegration("app-service-datadog", {
    name: datadogVendor.then(vendor => vendor.name),
    service: appService.id,
    vendor: datadogVendor.then(vendor => vendor.id),
});

const datadogPagerDutyIntegration = new datadog.pagerduty.Integration("pagerduty", {
    subdomain: pagerDutySubdomain,
    apiToken: pagerDutyApiToken,
    schedules: [pagerDutyScheduleUrl],
});

const datadogPagerDutyService = new datadog.pagerduty.ServiceObject("app-service-datadog", {
    serviceName,
    serviceKey: datadogIntegration.integrationKey,
}, {
    dependsOn: [datadogPagerDutyIntegration],
});

// Create a Datadog monitor that notifies PagerDuty.
const cpuMonitor = new datadog.Monitor("cpu-monitor", {
    name: "High CPU Usage",
    type: "metric alert",
    query: "avg(last_5m):avg:system.cpu.idle{service:my-app,env:prod} < 20",
    message: pulumi.interpolate`CPU usage is high for my-app. Notify: @pagerduty-${datadogPagerDutyService.serviceName}`,
    tags: ["service:my-app", "env:prod", "runbook:https://example.com/runbooks/my-app"],
});

// Create a New Relic alert policy and route issues through a workflow.
const policy = new newrelic.AlertPolicy("app-policy", {
    name: "My Application Policy",
});

const emailDestination = new newrelic.NotificationDestination("on-call-email-destination", {
    name: "on-call-email",
    type: "EMAIL",
    active: true,
    properties: [{
        key: "email",
        value: "on-call@example.com",
    }],
});

const emailChannel = new newrelic.NotificationChannel("on-call-email", {
    name: "on-call-email",
    destinationId: emailDestination.id,
    product: "IINT",
    type: "EMAIL",
    properties: [{
        key: "subject",
        value: "{{issueTitle}}",
    }],
});

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

const workflow = new newrelic.Workflow("app-policy-workflow", {
    name: "My Application Workflow",
    mutingRulesHandling: "NOTIFY_ALL_ISSUES",
    issuesFilter: {
        name: "my-application-policy-filter",
        type: "FILTER",
        predicates: [{
            attribute: "accumulations.policyName",
            operator: "EXACTLY_MATCHES",
            values: [policy.name],
        }],
    },
    destinations: [{
        channelId: emailChannel.id,
    }],
});
```

If the Datadog PagerDuty integration already exists in your Datadog account, import the account-wide resource before running `pulumi up`:

```bash
pulumi import datadog:pagerduty/integration:Integration pagerduty my-pagerduty-subdomain
```

## Validation

After running `pulumi up`, you can validate your observability stack:

1. **PagerDuty integration:** Check the "Integrations" tab of your PagerDuty service to confirm that the Datadog integration exists.
1. **Datadog service object:** In Datadog, open **Integrations > PagerDuty** and confirm the `my-application-service` service object exists and points to the PagerDuty integration key.
1. **Monitor test:** Manually trigger a test alert in Datadog and verify that a PagerDuty incident is created with the correct service and tags.
1. **New Relic routing:** Trigger the NRQL condition and verify that New Relic routes the issue through the configured workflow and email channel.

By wiring your observability stack as code, you ensure that every service is monitored from day one and that your on-call engineers always have the context they need to resolve incidents quickly.

Pulumi allows you to promote these configurations across environments. You can have a "staging" observability stack that notifies a Slack channel and a "production" stack that triggers PagerDuty.

By treating your monitors and dashboards with the same rigor as your infrastructure, you eliminate "monitoring debt" and ensure that your team is always ready for the next incident.

## Conclusion

Wiring Datadog, New Relic, and PagerDuty with Pulumi gives you a unified, version-controlled view of your observability posture. Whether you're managing a small service or a large fleet, start with one service, codify its monitor and escalation path, then promote that baseline across the rest of your applications.

{{< blog/cta-button "Explore Pulumi ESC" "/docs/esc/" >}}
