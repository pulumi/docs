---
title: "From ingress-nginx to Gateway API: A Modern Approach with kgateway"
date: 2026-01-02T11:35:51+01:00
draft: false
meta_desc: With ingress-nginx retiring in 2026, this post explores the technical shift to Gateway API and evaluates kgateway as a production-grade successor.
meta_image: meta.png
authors:
    - engin-diri
tags:
    - kubernetes
    - gateway-api
    - kgateway
    - ingress
    - networking
schema_type: auto
social:
    twitter:
    linkedin:
---

The upcoming retirement of **ingress-nginx** in early 2026 presents infrastructure teams with a deadline, but also a rare opportunity to rethink traffic management. For years, the standard approach involved stringing together annotations to force a controller to behave. The Gateway API offers a cleaner, standardized alternative. This post investigates the practical reality of this migration and explores why **kgateway** emerges as a robust solution for the future.

<!--more-->

With **ingress-nginx** entering its sunset phase in early 2026, the Kubernetes community faces a decision point. While the controller served as the default standard for a decade, its architecture now struggles to meet modern requirements. The transition to the Gateway API represents more than a forced migration; it offers a chance to adopt a standard designed for the complexity of contemporary traffic patterns.

The Ingress API relied heavily on controller-specific annotations, creating a fragmented ecosystem where configurations were rarely portable. The Gateway API addresses this by establishing a standardized, expressive approach that behaves consistently across implementations. A technical evaluation of the available options points to **kgateway** as a particularly strong candidate for production workloads.

## Why ingress-nginx is retiring

The Kubernetes SIG Network and Security Response Committee was direct in its [announcement regarding the project's future](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/). After March 2026, **ingress-nginx** will cease to receive releases, bug fixes, or security patches. The repositories will become read-only, leaving existing deployments functional but unmaintained.

This decision stems from both resource constraints and technical debt. The project relied on a very small group of maintainers working primarily in their spare time. Furthermore, features that once provided flexibility, such as "snippets" for arbitrary NGINX configuration injection, are now recognized as significant security liabilities. With no viable path to modernization within the existing codebase, retirement became the necessary conclusion.

It is worth noting that the Ingress API itself remains supported. The retirement affects only the **ingress-nginx** controller. NGINX as a web server continues unchanged. However, clusters relying on this specific controller must prepare for a transition.

To identify affected resources, checking the cluster for specific pods can reveal the scope of the dependency:

```bash
kubectl get pods --all-namespaces --selector app.kubernetes.io/name=ingress-nginx
```

## Understanding the Gateway API

The Gateway API represents a fundamental shift in traffic management concepts. While some elements may look familiar to those used to Ingress, the underlying philosophy addresses the "baggage" that the previous standard accumulated.

The core improvement lies in expressiveness. Advanced routing requirements—header matching, weighted traffic splitting, and traffic policies—are now native parts of the specification. This eliminates the need for the non-portable annotations that plagued the Ingress ecosystem.

The API also introduces a role-oriented structure that mirrors actual organizational workflows.

* **GatewayClass** resources are managed by infrastructure teams to define the underlying controller.
* **Gateway** resources are created by platform teams to specify entry points and listeners.
* **HTTPRoute** resources are owned by application teams to define service traffic rules.

This separation allows for genuine self-service. Application teams can manage their routing logic without requiring broad cluster privileges.

The relationship between these resources defines the traffic flow:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: GatewayClass
metadata:
  name: kgateway
spec:
  controllerName: kgateway.dev/kgateway
```

A Gateway references this class to establish the entry point:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: my-gateway
  namespace: default
spec:
  gatewayClassName: kgateway
  listeners:
    - name: http
      port: 8080
      protocol: HTTP
      allowedRoutes:
        namespaces:
          from: All
```

An HTTPRoute then attaches to the gateway:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: my-route
  namespace: default
spec:
  parentRefs:
    - name: my-gateway
  hostnames:
    - "example.com"
  rules:
    - matches:
        - path:
            type: PathPrefix
            value: /api
      backendRefs:
        - name: api-service
          port: 8080
```

Beyond standard HTTP, the API supports GRPCRoute, TCPRoute, UDPRoute, and TLSRoute, offering a protocol diversity that the original Ingress spec lacked.

### Cross-namespace routing and ReferenceGrant

The Gateway API enables a security model where routes can cross namespace boundaries, but only with explicit permission. The **ReferenceGrant** resource controls these connections. Without a grant, an HTTPRoute in one namespace cannot reference a Service in another.

```yaml
apiVersion: gateway.networking.k8s.io/v1beta1
kind: ReferenceGrant
metadata:
  name: allow-routes-from-apps
  namespace: gateway-system
spec:
  from:
    - group: gateway.networking.k8s.io
      kind: HTTPRoute
      namespace: my-app
  to:
    - group: ""
      kind: Service
```

This mechanism allows platform teams to strictly control which namespaces are authorized to attach to shared gateways.

## Evaluating Gateway API implementations

Several implementations have emerged to support the new standard, each with a distinct philosophy.

**NGINX Gateway Fabric** leverages NGINX as the data plane, offering continuity for teams already deep in the F5 ecosystem. It provides impressive throughput and integrates with enterprise security tools, making it a logical choice for existing NGINX shops.

**Traefik** focuses on simplicity. As a single binary with no external dependencies, it aligns well with environments that prioritize developer experience and rapid iteration. Its declarative configuration is particularly friendly to GitOps workflows.

**Envoy Gateway** is built on the Envoy Proxy and operates under a community-driven governance model. It appeals to those seeking strong conformance to the Gateway API spec without vendor lock-in. Its companion project, Envoy AI Gateway, adds support for LLM routing.

**kgateway**, formerly Gloo Gateway, brings seven years of production history to the table. Donated to the CNCF in early 2025, it combines an Envoy data plane with a control plane optimized for scale. Its internal architecture uses the "krt" framework to handle massive route tables efficiently, avoiding the performance bottlenecks often seen in snapshot-based systems.

| Aspect | NGINX Gateway Fabric | Traefik | Envoy Gateway | **kgateway** |
|--------|---------------------|---------|---------------|----------|
| **Base Technology** | NGINX (C) | Custom Go | Envoy Proxy (C++) | Envoy Proxy (C++) |
| **Maturity** | Production Ready | Mature | GA (v1.0+) | **Battle-tested (7+ years as Gloo)** |
| **Setup Complexity** | Medium | Low | Low | Low |
| **Commercial Support** | F5 Enterprise | Traefik Labs | Multiple vendors | Solo.io |
| **AI/LLM Support** | No | No | Via Envoy AI Gateway | **Native (Agentgateway)** |
| **Learning Curve** | Familiar for NGINX users | Gentle | Moderate | Moderate |
| **Community Size** | Growing | Large | Large | Established |
| **Best For** | Teams with NGINX expertise, high-throughput requirements | Teams prioritizing simplicity and rapid deployment | Standards-focused teams, multi-vendor environments | **Enterprise scale, AI workloads, Istio integration** |

### Decision framework

* **NGINX Gateway Fabric** suits teams needing F5 support or deep NGINX tuning.
* **Traefik** fits best where simplicity and operational ease are paramount.
* **Envoy Gateway** works for those valuing community governance and strict standards adherence.
* **kgateway** is the choice for enterprise scale, native AI gateway needs, and Istio integration.

For this exploration, **kgateway** was selected due to its proven track record and its native handling of both traditional microservices and AI traffic.

## Migrating from Ingress to Gateway API

The [official migration guide](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress/) outlines the transition process. It is less about a direct translation and more about restructuring intent.

The process typically involves:

1. **Defining a Gateway resource:** Unlike Ingress, listeners must be explicitly defined. This provides granular control over ports and protocols.
1. **Creating HTTPRoute resources:** These replace Ingress routing rules. Complex Ingress resources can be split into multiple HTTPRoutes for better management.
1. **Configuring filters:** Annotations for headers or redirects are replaced by standardized filters within the HTTPRoute spec.

The **[ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway)** tool can automate much of the initial conversion, providing a baseline of resources to review and refine.

### Migration planning

A successful migration requires scoping the effort:

**1. Assessment**
Identify the volume and complexity of existing resources.

```bash
# Count your Ingress resources across all namespaces
kubectl get ingress -A | wc -l

# List all Ingress resources with their hosts
kubectl get ingress -A -o jsonpath='{range .items[*]}{.metadata.namespace}/{.metadata.name}: {.spec.rules[*].host}{"\n"}{end}'
```

**2. Parallel Operations**
Running **kgateway** alongside **ingress-nginx** allows for incremental migration. Services can be moved one by one, validating the new configuration without risking the entire cluster's traffic.

**3. Rollback Strategy**
Keeping the original Ingress manifests ensures that traffic can be quickly reverted to the old controller if issues arise during the transition.

## Why kgateway stands out

**kgateway** distinguishes itself through its maturity and architectural decisions. Having started as Gloo Gateway in 2018, it has undergone years of hardening in production environments.

Its control plane uses the krt framework, originally developed for Istio. This allows it to track dependencies precisely and recalculate only the parts of the configuration that have changed. In large clusters where pods churn constantly, this incremental approach prevents the control plane from becoming a bottleneck, enabling it to [handle over 10,000 routes](https://kgateway.dev/blog/design-kgateway-for-scalability/) efficiently.

For teams managing AI workloads, **kgateway** includes the Agentgateway component. This Rust-based data plane is built for LLM traffic, supporting the Model Context Protocol (MCP) and providing token-based rate limiting. It unifies the management of AI and traditional traffic under a single control plane.

Additional features include:

* **Route Delegation:** Allows large routing tables to be split across teams with clear inheritance.
* **Security Integration:** Seamless mTLS with Istio ambient mesh and external authorization support.
* **Traffic Management:** Advanced capabilities like traffic mirroring and session affinity are available without complex Envoy configuration.

## Putting it all together with Pulumi

Seeing these concepts in code clarifies the architecture. The following Pulumi program demonstrates a complete setup: a DigitalOcean Kubernetes cluster, the **kgateway** installation via Helm, Gateway API resources, and an httpbin application to validate the configuration.

The program provisions infrastructure in a specific sequence. The cluster comes first, followed by the Gateway API CRDs, then **kgateway** itself. Once the control plane is running, the program creates a GatewayClass, a Gateway listener, and an HTTPRoute that directs traffic to the sample application. A ReferenceGrant permits the cross-namespace reference between the HTTPRoute and the backend Service.

{{< chooser language "typescript" >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as digitalocean from "@pulumi/digitalocean";
import * as k8s from "@pulumi/kubernetes";

// Configuration
const config = new pulumi.Config();
const clusterName = config.get("clusterName") || "kgateway-demo-cluster";
const region = config.get("region") || "fra1";
const nodeSize = config.get("nodeSize") || "s-2vcpu-4gb";
const nodeCount = config.getNumber("nodeCount") || 2;
const k8sVersion = config.get("k8sVersion") || "1.32.10-do.2";

// Create a DigitalOcean Kubernetes cluster
const cluster = new digitalocean.KubernetesCluster(clusterName, {
  name: clusterName,
  region: region,
  version: k8sVersion,
  nodePool: {
    name: "default-pool",
    size: nodeSize,
    nodeCount: nodeCount,
  },
});

// Create a Kubernetes provider using the cluster's kubeconfig
const k8sProvider = new k8s.Provider("k8s-provider", {
  kubeconfig: cluster.kubeConfigs[0].rawConfig,
});

// Install Gateway API CRDs (standard channel)
const gatewayApiCrds = new k8s.yaml.ConfigFile("gateway-api-crds", {
  file: "https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.4.0/standard-install.yaml",
}, { provider: k8sProvider });

// Create kgateway-system namespace
const kgatewayNamespace = new k8s.core.v1.Namespace("kgateway-system", {
  metadata: {
    name: "kgateway-system",
  },
}, { provider: k8sProvider });

// Install kgateway CRDs via Helm
const kgatewayCrds = new k8s.helm.v3.Release("kgateway-crds", {
  chart: "oci://cr.kgateway.dev/kgateway-dev/charts/kgateway-crds",
  version: "v2.1.2",
  namespace: kgatewayNamespace.metadata.name,
  createNamespace: false,
}, { provider: k8sProvider, dependsOn: [gatewayApiCrds, kgatewayNamespace] });

// Install kgateway control plane via Helm
const kgateway = new k8s.helm.v3.Release("kgateway", {
  chart: "oci://cr.kgateway.dev/kgateway-dev/charts/kgateway",
  version: "v2.1.2",
  namespace: kgatewayNamespace.metadata.name,
  createNamespace: false,
}, { provider: k8sProvider, dependsOn: [kgatewayCrds] });

// Create hello-world namespace
const helloWorldNamespace = new k8s.core.v1.Namespace("hello-world", {
  metadata: {
    name: "hello-world",
  },
}, { provider: k8sProvider });

// Deploy hello world application (using httpbin as shown in kgateway docs)
const helloWorldLabels = { app: "httpbin" };

const helloWorldDeployment = new k8s.apps.v1.Deployment("httpbin", {
  metadata: {
    name: "httpbin",
    namespace: helloWorldNamespace.metadata.name,
  },
  spec: {
    replicas: 1,
    selector: {
      matchLabels: helloWorldLabels,
    },
    template: {
      metadata: {
        labels: helloWorldLabels,
      },
      spec: {
        containers: [{
          name: "httpbin",
          image: "mccutchen/go-httpbin:v2.15.0",
          ports: [{
            containerPort: 8080,
            name: "http",
          }],
        }],
      },
    },
  },
}, { provider: k8sProvider, dependsOn: [helloWorldNamespace] });

const helloWorldService = new k8s.core.v1.Service("httpbin", {
  metadata: {
    name: "httpbin",
    namespace: helloWorldNamespace.metadata.name,
  },
  spec: {
    selector: helloWorldLabels,
    ports: [{
      port: 8000,
      targetPort: 8080,
      name: "http",
    }],
  },
}, { provider: k8sProvider, dependsOn: [helloWorldDeployment] });

// Create GatewayClass for kgateway
const gatewayClass = new k8s.apiextensions.CustomResource("kgateway-gateway-class", {
  apiVersion: "gateway.networking.k8s.io/v1",
  kind: "GatewayClass",
  metadata: {
    name: "kgateway",
  },
  spec: {
    controllerName: "kgateway.dev/kgateway",
  },
}, { provider: k8sProvider, dependsOn: [kgateway] });

// Create Gateway with LoadBalancer service (matching kgateway docs pattern)
const gateway = new k8s.apiextensions.CustomResource("http-gateway", {
  apiVersion: "gateway.networking.k8s.io/v1",
  kind: "Gateway",
  metadata: {
    name: "http",
    namespace: kgatewayNamespace.metadata.name,
  },
  spec: {
    gatewayClassName: "kgateway",
    listeners: [{
      name: "http",
      port: 8080,
      protocol: "HTTP",
      allowedRoutes: {
        namespaces: {
          from: "All",
        },
      },
    }],
  },
}, { provider: k8sProvider, dependsOn: [gatewayClass] });

// Create HTTPRoute for httpbin application
const httpRoute = new k8s.apiextensions.CustomResource("httpbin-route", {
  apiVersion: "gateway.networking.k8s.io/v1",
  kind: "HTTPRoute",
  metadata: {
    name: "httpbin",
    namespace: helloWorldNamespace.metadata.name,
  },
  spec: {
    parentRefs: [{
      name: "http",
      namespace: kgatewayNamespace.metadata.name,
    }],
    hostnames: [
      "*.nip.io",
    ],
    rules: [{
      backendRefs: [{
        name: "httpbin",
        port: 8000,
      }],
    }],
  },
}, { provider: k8sProvider, dependsOn: [gateway, helloWorldService] });

// Create a reference grant to allow the HTTPRoute to reference the service cross-namespace
const referenceGrant = new k8s.apiextensions.CustomResource("httpbin-reference-grant", {
  apiVersion: "gateway.networking.k8s.io/v1beta1",
  kind: "ReferenceGrant",
  metadata: {
    name: "allow-gateway-to-httpbin",
    namespace: helloWorldNamespace.metadata.name,
  },
  spec: {
    from: [{
      group: "gateway.networking.k8s.io",
      kind: "HTTPRoute",
      namespace: helloWorldNamespace.metadata.name,
    }],
    to: [{
      group: "",
      kind: "Service",
    }],
  },
}, { provider: k8sProvider, dependsOn: [gatewayApiCrds] });

// Create a LoadBalancer Service for the Gateway proxy
const gatewayProxyService = new k8s.core.v1.Service("gateway-proxy", {
  metadata: {
    name: "gateway-proxy",
    namespace: kgatewayNamespace.metadata.name,
  },
  spec: {
    type: "LoadBalancer",
    selector: {
      "gateway.networking.k8s.io/gateway-name": "http",
    },
    ports: [{
      name: "http",
      port: 8080,
      targetPort: 8080,
      protocol: "TCP",
    }],
  },
}, { provider: k8sProvider, dependsOn: [gateway] });

// Extract the LoadBalancer IP from our managed Service
const gatewayIP = gatewayProxyService.status.apply(status => {
  const ingress = status?.loadBalancer?.ingress;
  if (ingress && ingress.length > 0) {
    return ingress[0].ip || ingress[0].hostname || "pending";
  }
  return "pending";
});

// Exports
export const clusterNameOutput = cluster.name;
export const clusterEndpoint = cluster.endpoint;
export const kubeconfig = pulumi.secret(cluster.kubeConfigs[0].rawConfig);

// Export the LoadBalancer IP and nip.io URL
export const gatewayLoadBalancerIP = gatewayIP;
export const httpbinUrl = gatewayIP.apply(ip =>
  ip !== "pending" ? `http://httpbin.${ip}.nip.io:8080/get` : "Waiting for LoadBalancer IP..."
);
```

{{% /choosable %}}

{{< /chooser >}}

> [!INFO]
> The demo uses [nip.io](https://nip.io), a wildcard DNS service that resolves `*.IP.nip.io` hostnames to the specified IP address. This eliminates the need to configure separate DNS records during testing. Once deployed, the `httpbinUrl` output provides a ready-to-use endpoint for validating the gateway configuration.

## The short-term option: Chainguard's ingress-nginx fork

For organizations that cannot immediately migrate to the Gateway API, there is another path forward. Chainguard has [forked ingress-nginx](https://www.chainguard.dev/unchained/keeping-ingress-nginx-alive) as part of their EmeritOSS program, providing continued maintenance after the upstream project's retirement.

This fork is not about adding new features. Chainguard is explicit that they are maintaining stability, not continuing development. Their commitment includes keeping dependencies updated, addressing CVEs on a best-efforts basis, and providing commercial container images with low vulnerability counts and SLAs. FIPS-compliant versions are also available for regulated environments.

The [chainguard-forks/ingress-nginx](https://github.com/chainguard-forks/ingress-nginx) repository on GitHub provides the maintained codebase. For teams running `ingress-nginx` in production, this fork offers a viable bridge while evaluating the Gateway API or other alternatives. However, this should be viewed as buying time rather than a permanent solution. The architectural limitations of the Ingress API remain, and the eventual move to a more expressive standard like the Gateway API is still the recommended path forward.

## Looking ahead

The retirement of **ingress-nginx** marks the end of an era and the beginning of a more structured approach to Kubernetes networking. The Gateway API offers a robust framework that reflects how teams actually build and secure applications today.

While March 2026 provides a comfortable runway, early planning prevents rushed decisions. Setting up a test environment with **kgateway** to validate the new API constructs is a prudent next step.

The shift to the Gateway API is not just about keeping the lights on; it is about building a networking foundation ready for the next decade of infrastructure challenges.

{{< get-started >}}

## Resources

* [Gateway API Documentation](https://gateway-api.sigs.k8s.io/) – Comprehensive guides and examples.
* [Migration Guide](https://gateway-api.sigs.k8s.io/guides/getting-started/migrating-from-ingress/) – Official steps for transitioning from Ingress.
* [ingress2gateway](https://github.com/kubernetes-sigs/ingress2gateway) – Tooling to automate resource conversion.
* [kgateway Documentation](https://kgateway.dev/) – Installation and configuration details.
* [Designing kgateway for Scalability](https://kgateway.dev/blog/design-kgateway-for-scalability/) – Deep dive into the krt framework.
* [Kubernetes Blog: ingress-nginx Retirement](https://kubernetes.io/blog/2025/11/11/ingress-nginx-retirement/) – Full context on the deprecation.
