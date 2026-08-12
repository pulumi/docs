---
title_tag: "Telemetry | Self-Hosting Pulumi"
meta_desc: Export metrics and traces from a self-hosted Pulumi Cloud installation via OpenTelemetry, and scrape or remote-write them into Prometheus.
title: Telemetry
h1: Self-Hosted Pulumi Cloud Telemetry
menu:
  administration:
    name: Telemetry
    parent: administration-self-hosting-operations
    weight: 7
    identifier: administration-self-hosting-operations-telemetry
pulumi_cloud_feature: self-hosting
---

{{< self-hosting-trial-note />}}

Getting metrics and traces out of a self-hosted installation. For what to alert
on once they are flowing, see [Monitoring](/docs/administration/self-hosting/operations/monitoring/).

## Configuring the exporter

The API service is configured to export OpenTelemetry metrics and traces to the vendor of your choice via the OpenTelemetry collector. You will need to manage your own OpenTelemetry collector.

The following environment variables are needed to configure OpenTelemetry in the service:

| Variable name | Description |
| --- | --- |
| OTEL_EXPORTER_OTLP_ENDPOINT | (Required) Used to configure the OTLP exporter. The base URL to which all telemetry will be sent. If not set, the API service will use no-op metrics and traces. |
| OTEL_EXPORTER_OTLP_PROTOCOL | (Optional) Used to configure the OTLP exporter. Valid values are `http` or `grpc`. Defaults to `grpc`. |
| PULUMI_ENABLE_DEPRECATED_METRICS | (Optional) Whether to continue emitting API service metrics in a log-based format. Defaults to `true`. |
| METRICS_WEBHOOK_SECRET | Required to successfully authenticate to the `/metrics` endpoint. The Authorization header should be set as follows: `Authorization: webhook-token <METRICS_WEBHOOK_SECRET>`. |

OpenTelemetry is not yet available for the [console service](/docs/administration/self-hosting/components/console/).

### Metrics endpoint

The API service exposes a metrics endpoint (`https://api.pulumi.com/metrics`) that is secured by a bearer token. This token is configured using the environment variable `METRICS_WEBHOOK_SECRET`.

{{% notes type="info" %}}
The token type is `webhook-token`, not `Bearer`.
{{% /notes %}}

```sh
curl -s GET https://api.pulumi.com/metrics -H 'Authorization: webhook-token <METRICS_WEBHOOK_SECRET>
```

### Prometheus

The API service provides two options to get metrics into Prometheus:

1. From the OpenTelemetry collector via a [Prometheus remote write exporter](#prometheus-remote-write-exporter). This is a push-based exporter.
1. From a [Prometheus exporter](#prometheus-exporter) by scraping the `/metrics` endpoint. This is a pull-based exporter.

#### Prometheus remote write exporter

This option does not use the `/metrics` endpoint. Instead, it exports metrics from the collector to a [Prometheus remote write compatible backend](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/prometheusremotewriteexporter/README.md).

Example OpenTelemetry collector configuration for a service using AWS and the AWS Distro for OpenTelemetry Collector:

```yaml
extensions:
  sigv4auth:

receivers:
  otlp:
    protocols:
      grpc:
        endpoint: localhost:4317

processors:
  memory_limiter:

  batch:

exporters:
  logging:

  prometheusremotewrite:
    endpoint: https://aws-managed-prometheus-endpoint/v1/api/remote_write
    auth:
      authenticator: sigv4auth

service:
  telemetry:
    logs:

  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [logging]

    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [prometheusremotewrite]

  extensions: [sigv4auth]
```

#### Prometheus exporter

This option requires configuring the environment variable `METRICS_WEBHOOK_SECRET` to successfully authenticate to the [`/metrics` endpoint](#metrics-endpoint).

Example OpenTelemetry collector configuration:

```yaml
extensions:
  bearertokenauth:
    scheme: webhook-token
    token: ${env:METRICS_WEBHOOK_SECRET}

receivers:
  otlp:
    protocols:
      grpc:
        endpoint: localhost:4317

processors:
  memory_limiter:

  batch:

exporters:
  debug:

  prometheus:
    endpoint: api.pulumi.com:443
    auth:
      authenticator: bearertokenauth
    namespace: pulumi
    resource_to_telemetry_conversion:
      enabled: true

service:
  telemetry:
    logs:

  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [debug]

    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [prometheus]

  extensions: [bearertokenauth]
```

The bearer token also needs to be included in the Prometheus server configuration:

```yaml
scrape_configs:
  - job_name: pulumi
    scrape_interval: 15s
    authorization:
      type: webhook-token
      credentials: <METRICS_WEBHOOK_SECRET>
    scheme: https
    static_configs:
      - targets: ["api.pulumi.com"]
```
