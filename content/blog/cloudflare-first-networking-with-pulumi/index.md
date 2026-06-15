---
title: "Cloudflare-First Networking as Code with Pulumi"
date: 2026-06-16
meta_desc: "Build a Cloudflare-first edge baseline with Pulumi, including DNS, WAF rules, Workers, Zero Trust Access policies, and repeatable validation."
meta_image: meta.png
feature_image: feature.png
authors:
    - pablo-seibelt
tags:
    - cloudflare
    - networking
    - zero-trust
categories:
    - best-practices
social:
    twitter: |
        Move Cloudflare edge config out of clickops.

        DNS, WAF rules, Workers, and Zero Trust Access policies can all live in a repeatable Pulumi baseline.
    linkedin: |
        Cloudflare often becomes the real front door for apps: DNS, WAF rules, Workers, and Zero Trust Access.

        This guide shows how to turn that edge layer into a reusable Pulumi baseline with validation built in.
    bluesky: |
        Cloudflare edge config does not need to live in clickops.

        Build DNS, WAF, Workers, and Access policies as a Pulumi baseline.
---

Platform teams managing multi-cloud applications face a dangerous visibility gap. While origin infrastructure is tightly controlled, the edge configuration often drifts through manual console tweaks. DNS records point to stale origins, WAF rules are inconsistent across environments, and Zero Trust policies fail to keep pace with team changes. This edge drift leads to application exposure or routing failures that origin teams only notice after users report them.

As applications span multiple clouds, the edge often becomes the most consistent layer for enforcing security and traffic policies. The cost of waiting for a unified edge strategy is high. Every manual change is a potential security hole or a performance bottleneck that bypasses your standard CI/CD rigor.

<!--more-->

## What you'll build

In this post, you will build a standardized Cloudflare edge baseline. You'll use Pulumi to define:

1. **DNS records** to point to your multi-cloud origins.
1. **WAF custom rules** to block malicious traffic before it hits your network.
1. **A Worker canary** to handle edge logic and header validation.
1. **Zero Trust Access policies** to secure internal tools and origin access.

By the end, you will have a version-controlled edge that you can validate and deploy across any environment.

## The Pulumi program

We'll build a Pulumi program that sets up a complete edge environment. This approach ensures that your edge security and routing are always in sync with your application code.

### Setting up the provider

First, ensure you have the `@pulumi/cloudflare` package installed and your credentials configured. The examples below are checked against `@pulumi/cloudflare@6.15.0`, the current v6 Pulumi Registry API at the time of writing.

```bash
npm install @pulumi/cloudflare@6.15.0
pulumi config set --secret cloudflare:apiToken "$CLOUDFLARE_API_TOKEN"
```

### Defining the infrastructure

Here is the complete Pulumi program in TypeScript. If your zone already has a custom WAF ruleset for the same phase, import that ruleset or add the rule to your existing ruleset instead of creating another phase-level ruleset that may fail or conflict.

```typescript
import * as cloudflare from "@pulumi/cloudflare";

const accountId = "<your-cloudflare-account-id>";
const trustedAdminIp = "198.51.100.10";

const zone = new cloudflare.Zone("my-zone", {
    account: {
        id: accountId,
    },
    name: "example.com",
});

const www = new cloudflare.DnsRecord("www", {
    zoneId: zone.id,
    name: "www",
    content: "1.2.3.4",
    ttl: 1,
    type: "A",
    proxied: true,
});

const admin = new cloudflare.DnsRecord("admin", {
    zoneId: zone.id,
    name: "admin",
    content: "1.2.3.4",
    ttl: 1,
    type: "A",
    proxied: true,
});

const wafRule = new cloudflare.Ruleset("waf-rule", {
    zoneId: zone.id,
    name: "Block suspicious traffic",
    description: "Custom WAF rule to block specific patterns",
    kind: "zone",
    phase: "http_request_firewall_custom",
    rules: [{
        action: "block",
        expression: `(http.request.uri.path contains "/admin" and not ip.src in {${trustedAdminIp}})`,
        description: "Block unauthorized admin access",
    }],
});

const worker = new cloudflare.WorkersScript("canary-worker", {
    accountId: accountId,
    scriptName: "edge-canary",
    compatibilityDate: "2026-01-01",
    mainModule: "worker.js",
    content: `
        export default {
            async fetch(request) {
                return new Response("Edge Baseline Validated", {
                    headers: { "x-edge-baseline": "active" },
                });
            },
        };
    `,
});

const workerRoute = new cloudflare.WorkersRoute("canary-route", {
    zoneId: zone.id,
    pattern: "www.example.com/*",
    script: worker.scriptName,
});

const adminGroup = new cloudflare.ZeroTrustAccessGroup("admin-group", {
    accountId: accountId,
    name: "Administrators",
    includes: [{
        email: {
            email: "admin@example.com",
        },
    }],
});

const accessApp = new cloudflare.ZeroTrustAccessApplication("internal-tool", {
    accountId: accountId,
    name: "Internal Admin Tool",
    domain: "admin.example.com",
    type: "self_hosted",
    policies: [{
        name: "Allow administrators",
        precedence: 1,
        decision: "allow",
        includes: [{
            group: {
                id: adminGroup.id,
            },
        }],
    }],
});
```

## Validation

Once you run `pulumi up`, you can validate your edge baseline with these steps:

1. **DNS check**: Run `dig www.example.com` to confirm the record points to Cloudflare's proxied IPs.
1. **WAF test**: Attempt to access `www.example.com/admin` from an unauthorized IP and verify you receive a 403 Forbidden response.
1. **Worker canary**: Use `curl -I https://www.example.com` and check for the `x-edge-baseline: active` header.
1. **Access policy**: Navigate to `admin.example.com` and verify you are redirected to the Cloudflare Access login page.

By managing these resources as code, you eliminate the risk of manual drift and ensure that every environment starts with a secure, validated edge baseline.
