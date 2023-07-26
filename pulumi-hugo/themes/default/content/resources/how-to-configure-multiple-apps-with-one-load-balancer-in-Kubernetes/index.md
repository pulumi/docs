---
title: "How to configure multiple apps with one load balancer in Kubernetes"
allow_long_title: true
meta_desc: "Use this Pulumi guide to configure multiple apps via a single Kubernetes load balancer. Enhance service management and traffic distribution."
type: ai-answers
date: 2023-07-24
---

To achieve this we configure an Ingress resource in Kubernetes to direct traffic to different services. This effectively treats the Ingress as a load balancer across multiple services.

Ingresses are split into rules, where each rule direct to a different service based on the path of the incoming request. Here, App1 and App2 represent the services backed by your different apps.

Let's assume that you want to direct all traffic with the path /app1 to App1 and all traffic with path /app2 to App2.

This is simplified so you'll have to modify to suit your actual setup.

Here is the Pulumi TypeScript program:

```typescript

import * as k8s from "@pulumi/kubernetes";

// Create the Ingress
const ingress = new k8s.networking.v1.Ingress("app-ingress", {
    metadata: { annotations: { "kubernetes.io/ingress.class": "nginx" } },
    spec: {
        rules: [
            {
                host: "your.host.com",
                http: {
                    paths: [
                        {
                            path: "/app1",
                            pathType: "Prefix",
                            backend: {
                                service: {
                                    name: "app1-service",
                                    port: {
                                        number: 80,
                                    }
                                }
                            }
                        },
                        {
                            path: "/app2",
                            pathType: "Prefix",
                            backend: {
                                service: {
                                    name: "app2-service",
                                    port: {
                                        number: 80,
                                    }
                                }
                            }
                        },
                    ]
                }
            }
        ]
    }
});


```

This program will create an Ingress that directs traffic based on the incoming path to the appropriate backend service. You still need to have these services app1-service and app2-service backed by your applications in Kubernetes.

For further details, you can reference the [kubernetesing.v1.Ingress](https://www.pulumi.com/registry/packages/kubernetes/api-docs/networking/v1/ingress/) from the Pulumi Registry documentation.
