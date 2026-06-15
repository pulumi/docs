---
title: "Introducing OTel Tracing in the Pulumi CLI"
date: 2026-04-01
draft: false
meta_desc: "The Pulumi CLI now supports OpenTelemetry tracing, replacing the deprecated OpenTracing integration. Learn how to export traces via gRPC or to a file."
meta_image: meta.png
feature_image: feature.png
authors:
    - thomas-gummerer
tags:
    - features
    - pulumi-cli
categories:
    - product-launches
schema_type: auto

# Social media copy — auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter: Introducing OTel Tracing in the Pulumi CLI
    linkedin: |
        Introducing OTel Tracing in the Pulumi CLI

        We've recently introduced OTel tracing in the pulumi CLI, to replace our current OpenTelemetry setup. Read the blog post to find out how we did it, and how you can use it.
    bluesky: Introducing OTel Tracing in the Pulumi CLI
---

Tracing is an important part of our CLI observability story. So far we've relied on (the now deprecated) [OpenTracing](https://opentracing.io/) for this. We have now added OTel tracing to the CLI, which is more future-proof, and should in most cases give you a better view over what the CLI is doing.

<!--more-->

## Background

We introduced tracing using [OpenTracing](https://opentracing.io) [all the way back in 2017](https://github.com/pulumi/pulumi/pull/521), before [OpenTelemetry](https://opentelemetry.io/) was a thing. This served us well over the years, but as OpenTracing was deprecated, and OTel emerged as the new and maintained thing, it got harder and harder to justify further investment in a tracing infrastructure that was deprecated. Last year we started focusing more on performance, and it became more and more clear that we'd either have to enhance our current OpenTracing setup, or do the work to switch to OTel.

In the end it was a relatively easy decision to move to the more modern and fully supported OTel, especially as more and more tooling around it starts emerging.

## Enter OTel

With the decision to move to OTel made, the only thing left to decide was how to implement it. There were a couple of constraints we faced here. First, we wanted to make sure that traces are easily shareable. This means ideally a text file in whatever format, that can be shared easily. Second, pulumi's plugin system works by spawning a new process per plugin. We want to get traces from each of these plugins to make sure we have as much coverage as possible. And third, ideally we also want to get traces from plugins that only implement OpenTracing, but not OTel yet, since someone can upgrade the CLI, but not the plugins for example.

Given these constraints, we decided to implement an OTel collector in the CLI, that could then forward the traces to whatever output format we want. This means that plugins only ever need to send traces back to the CLI over [gRPC](https://grpc.io/), and the CLI will do any further processing. This means only one process will write to the file, if requested.

For plugins we always request both OpenTracing and OTel traces. If both are requested and OTel is supported by the plugin, the plugin is expected to only send the OTel version of the traces. For OpenTracing traces, we collect them in the collector in the CLI, and then translate them internally to OTel traces. This way we can still get the traces from older plugins, without them needing to change anything.

## Try it out

Currently the OTel exporter supports both exporting the traces directly via gRPC to a collector, or to a file, where the traces are JSON encoded. This file can then be shared and imported into a trace viewer at a later time. To do this, you can use the `--otel-traces <file://<filename>|grpc://<exporter-address>>` flag, using pulumi version v3.226 or newer. For further documentation see [our performance tracing docs](https://www.pulumi.com/docs/support/debugging/performance-tracing/#opentelemetry-tracing).

To view the traces, you can use one of the various exporters that exist. Popular options include [Jaeger](https://www.jaegertracing.io/), [OTel Desktop Viewer](https://github.com/CtrlSpice/otel-desktop-viewer), or [OTel TUI](https://github.com/ymtdzzz/otel-tui) if you prefer not leaving your terminal. Once you've ingested the logs there either by uploading the trace file, or sending them directly by giving pulumi the exporter address, look for the `pulumi-cli: pulumi` root span.

All further spans will be parented to that root span, and you should thus be able to see a nice flow diagram in the viewer of your choice.

As always, we would love any feedback either in the [Community Slack](https://slack.pulumi.com/), or through a [GitHub issue](https://github.com/pulumi/pulumi/issues).
