---
title_tag: "Performance Tracing in Pulumi"
meta_desc: "Learn how to trace Pulumi deployments to understand performance bottlenecks and optimize your infrastructure deployments."
title: Performance and tracing
h1: Performance and tracing
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        name: Performance and Tracing
        parent: support-debugging
        weight: 30
        identifier: support-debugging-performance-tracing
---

If you are seeing unexpectedly slow performance, you can gather a trace to understand what operations are being performed throughout the deployment and what the long poles are for your deployment. In most cases, the most time-consuming operations will be the provisioning of one or more resources in your cloud provider, however, there may be cases where Pulumi itself is doing work that is limiting the performance of your deployments, and this may indicate an opportunity to further improve the Pulumi deployment orchestration engine to get the maximal parallelism and performance possible for your cloud deployment.

## Tracing

To collect a trace:

```
$ pulumi up --tracing=file:./up.trace
```

To view a trace locally using [AppDash](https://github.com/sourcegraph/appdash):

```
$ PULUMI_DEBUG_COMMANDS=1 pulumi view-trace ./up.trace
Displaying trace at http://localhost:8008
```

Pulumi also supports [Zipkin](https://zipkin.io) compatible tracing. To collect a trace to a local [Jaeger](https://www.jaegertracing.io/docs/1.22/getting-started/) server:

```
$ docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -p 16686:16686 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.22

$ pulumi up --tracing http://localhost:9411/api/v1/spans
```

To view a trace locally navigate to the [Jaeger UI](http://localhost:16686/search).
