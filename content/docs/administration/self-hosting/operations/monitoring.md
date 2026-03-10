---
title_tag: "Monitoring and Alerting | Self-Hosting Pulumi"
meta_desc: Best practices for monitoring, alerting, and anomaly detection for self-hosted Pulumi Cloud deployments.
title: Monitoring
h1: Monitoring and Alerting
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  administration:
    name: Monitoring
    parent: administration-security-compliance-self-hosted-operations
    weight: 6
    identifier: administration-security-compliance-self-hosted-operations-monitoring
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the self-hosted Pulumi Cloud, sign up for the [30-day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).
{{% /notes %}}

Effective monitoring is critical for maintaining a reliable self-hosted Pulumi Cloud deployment. This page covers a recommended alerting strategy and the key metrics to watch.

The API service exposes Prometheus metrics and supports OpenTelemetry for tracing. See [OpenTelemetry configuration](/docs/administration/self-hosting/components/api/#opentelemetry) for setup details.

## Three-tier alerting strategy

Implement alerts at three severity levels:

| Tier | Purpose | Action | Examples |
| :-- | :-- | :-- | :-- |
| Alert (page) | Service-impacting issues requiring immediate response | Pages on-call engineer | 5xx error rate > 5%, unhealthy hosts, container crash loops |
| Notification (Slack/email) | Degradation that needs attention during business hours | Notifies team channel | High CPU, replication lag, storage warnings |
| Information (dashboard) | Anomaly detection and capacity planning | Logged for review | Traffic pattern changes, signup anomalies |

## Key metrics to monitor

### Application health

- HTTP 5xx error rate as a percentage of total requests (not just raw count)
- Target group unhealthy host count (alert if > 0 for 3+ minutes)
- Container restart count (alert on repeated restarts)
- Request latency percentiles (p50, p95, p99)

### Database

- CPU utilization - different thresholds for writer vs reader instances
- Replication lag - alert if > 1 second
- Freeable memory - alert when < 10% remaining
- Storage space remaining - alert at 50 GB (notify) and 20 GB (page)
- Total IOPS (read + write combined)
- Connection count vs maximum connections

### Object storage

- Request error rate (4xx, 5xx)
- Replication lag (if cross-region replication is enabled)
- Bucket size growth rate

### Compute

- CPU and memory utilization per service
- Auto-scaling group desired vs running instance count
- NAT gateway connection/bandwidth utilization

## Anomaly detection

Where your monitoring platform supports it, use anomaly detection (dynamic thresholds) rather than static thresholds for:

- Traffic volume (requests per minute)
- User signup rates
- API latency

This reduces alert noise from expected traffic variation while catching genuine anomalies.
