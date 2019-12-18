---
title: "Managing F5 BIG-IP Systems with Pulumi"
date: "2019-02-07"
meta_desc: "In this post, we look at what's possible the F5 BIG-IP provider for Pulumi, as well as the power and the flexibility that Pulumi brings."
authors: ["cameron-stokes"]
tags: ["Infrastructure","Cloud-Native"]
---

The [Pulumi](/) ecosystem is continuously growing
and today we're excited to announce the F5 BIG-IP provider for Pulumi.

F5's [BIG-IP Local Traffic Managment (LTM) services](https://www.f5.com/products/big-ip-services/local-traffic-manager)
provides advanced traffic management, acceleration, security, and
analytics features to your applications. With the addition of our F5
BIG-IP Pulumi provider we are bringing *Cloud Native Infrastructure as
Code* to F5 BIG-IP devices with real programming languages and a
consistent programming model. This addresses a frequent use-case we've
heard from our customers for both on-premises and Cloud workloads.

Let's look at some examples to demonstrate what's capable with this
provider and the power and flexibility that Pulumi brings to working
with your F5 BIG-IP systems.
<!--more-->

## Simple Load Balancing

In the code below we create a handful of resources that allow us to use
our BIG-IP to load balance to two backend HTTP servers. It's omitted for
the sake of brevity, but we could easily create these HTTP servers
inline in the same code as our BIG-IP resources - managing them side by
side in the same Pulumi application.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as f5bigip from "@pulumi/f5bigip";

// The backend IP:Port we want to load balance to.
const backendInstance = "172.31.47.29:80";

// Create our health check monitor
const httpMonitor = new f5bigip.ltm.Monitor("www", {
    name: "/Common/www",
    parent: "/Common/http",
    send: "GET /",
    timeout: 5,
    interval: 10,
});

// Create our pool that we'll attach our HTTP servers to
const wwwPool = new f5bigip.ltm.Pool("www", {
    name: "/Common/www",
    monitors: [httpMonitor.name],
    allowNat: "yes",
    allowSnat: "yes",
});

// Create a pool attachment for our HTTP server
const wwwPoolAttachment = new f5bigip.ltm.PoolAttachment(`www`, {
    pool: wwwPool.name,
    node: pulumi.interpolate`/Common/${backendInstance}`,
});

// Create our LTM Virtual Server
const wwwVirtualServer = new f5bigip.ltm.VirtualServer("www", {
    pool: wwwPool.name,
    name: "/Common/www",
    destination: new pulumi.Config().require("f5PrivateIp"),
    port: 80,
    ipProtocol: "tcp",
    profiles: ["/Common/http"],
    sourceAddressTranslation: "automap",
});
```

## Managing iRules

*iRules* are one of the more powerful features within the BIG-IP Local
Traffic Management (LTM) system. iRules allow you to validate and
manipulate request and response data passing through your BIG-IP as well
as make decisions on such traffic such as directing traffic to different
backend server pools.

These rules are highly dependent on your application configuration and
requirements so we'll show a simple example here that logs connection
information within the BIG-IP system based on the presence of a query
parameter on the HTTP request - e.g. `?_debug=true`. Again we're
omitting some of the resources to keep the example short.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as f5bigip from "@pulumi/f5bigip";

// ...

const iRuleTcl = `
when HTTP_REQUEST {
    # initialize our connection-scoped variable
    set client_debug 0

    # if request query string contains _debug=true
    if {[URI::query [HTTP::uri] _debug] eq "true"} {
        set client_debug 1
    }
}
when SERVER_CONNECTED {
    # if our connection-scoped variable is true, log connection info
    if {$client_debug} {
        log local0. "Client debug info requested... [IP::client_addr]:[TCP::client_port] -> [clientside {IP::local_addr}]:[clientside {TCP::local_port}] -> [IP::remote_addr]:[TCP::remote_port]"
    }
}
when HTTP_RESPONSE {
    # add a response header so clients know their connection info was logged
    if {$client_debug} {
        HTTP::header insert "X-Client-Debug" "true"
    }
}
`;

// Create our iRule
const iRule = new f5bigip.ltm.IRule("www", {
    name: "/Common/www",
    irule: iRuleTcl,
});

// Create our LTM Virtual Server
const wwwVirtualServer = new f5bigip.ltm.VirtualServer("www", {
    pool: wwwPool.name,
    name: "/Common/www",
    destination: new pulumi.Config().require("f5PrivateIp"),
    port: 80,
    ipProtocol: "tcp",
    profiles: ["/Common/http"],
    sourceAddressTranslation: "automap",
    irules: [iRule.name],
});
```

## Dynamically Creating iRules

So far the BIG-IP resources we've created have been relatively static.
Let's leverage the full power of Pulumi by dynamically creating
resources based on an array of values. A common scenario when creating a
website is to provide versions of the website in various languages for
your audience. In this example we'll create a number of iRules to
redirect users to localized websites based on a user's language
preference.

We define the languages we currently support in an array called
supportedLanguages and then use this array to create an iRule for each
language.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as f5bigip from "@pulumi/f5bigip";

// ...

// The languages we currently support.
const supportedLanguages = [
    "es",
    "fr",
]

const iRules = supportedLanguages.map(languageCode => {
    const iRuleTcl = `
    when HTTP_REQUEST {
        # if request path equals '/'
        if {[HTTP::uri] eq "/"} {
            if { [HTTP::header "Accept-Language"] starts_with "${languageCode}" } {
                HTTP::respond 301 Location "/${languageCode}/"
            }
        }
    }
    `;

    // Create our iRule
    const iRule = new f5bigip.ltm.IRule(`www-${languageCode}`, {
        name: `/Common/www-${languageCode}`,
        irule: iRuleTcl,
    });
    return iRule;
});

// Create our LTM Virtual Server
const wwwVirtualServer = new f5bigip.ltm.VirtualServer("www", {
    pool: wwwPool.name,
    name: "/Common/www",
    destination: new pulumi.Config().require("f5PrivateIp"),
    port: 80,
    ipProtocol: "tcp",
    profiles: ["/Common/http"],
    sourceAddressTranslation: "automap",
    irules: iRules.map(irule => irule.name),
});
```

## Wrap Up

With the F5 BIG-IP Pulumi provider you can manage BIG-IP systems whether
they're in the cloud, as available on [Amazon Web Services](https://aws.amazon.com/marketplace/seller-profile?id=74d946f0-fa54-4d9f-99e8-ff3bd8eb2745),
[Microsoft Azure](https://azuremarketplace.microsoft.com/en-us/marketplace/apps?search=f5&page=1),
and [Google Cloud Platform](https://console.cloud.google.com/marketplace/partners/f5-7626-networks-public),
or in your on-premises data centers. In a matter of minutes you can
bring modern code and development practices to your BIG-IP-powered
applications.

To start managing your F5 BIG-IP systems with real programming
languages, please check out the following links:

- [Node.js documentation]({{< ref "/docs/reference/pkg/nodejs/pulumi/f5bigip" >}})
- [Python documentation]({{< ref "/docs/reference/pkg/python/pulumi_f5bigip" >}})
- [F5 BIG-IP Example using Pulumi](https://github.com/pulumi/examples/tree/master/f5bigip-ts-ltm-pool)
