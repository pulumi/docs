---
title: "Getting Started on DigitalOcean with Pulumi"
authors: ["paul-stack"]
tags: ["DigitalOcean", "TypeScript"]
date: "2019-07-18"

meta_image: "Feature.jpg"
---

Pulumi recently added support for managing [DigitalOcean](https://www.digitalocean.com/) resources. This article will
show you how to deploy some load balanced Droplets on DigitalOcean using Pulumi.

To get started, let's create a new Pulumi program written in TypeScript:

```bash
 $ mkdir infra && cd infra
 $ pulumi new typescript
```

Now we should install the latest Pulumi DigitalOcean provider:

```bash
 $ npm install @pulumi/digitalocean
```

At the top of our application, we can add the resource imports:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as digitalocean from "@pulumi/digitalocean";
```

We can now start to build the infrastructure. To get started, we will declare two constants:

```typescript
const dropletCount = 3;
const region = digitalocean.Regions.NYC3;
```

Now, let's create our web servers. Since our Pulumi application is written in TypeScript, we can use a loop, as follows:

```typescript
const dropletTypeTag = new digitalocean.Tag("demo-app");
const userData =
  `#!/bin/bash
  sudo apt-get update
  sudo apt-get install -y nginx`;

const droplets = [];
for (let i = 0; i < dropletCount; i++) {
    let nameTag = new digitalocean.Tag(`web-${i}`);

    droplets.push(new digitalocean.Droplet(`web-${i}`, {
        image: "ubuntu-18-04-x64",
        region: region,
        privateNetworking: true,
        size: digitalocean.DropletSlugs.Droplet512mb,
        tags: [nameTag.id, dropletTypeTag.id],
        userData: userData,
    }));
}
```

Let's take a closer look at what we've programmed. First, we declared a `dropletTypeTag`; we'll come back to what this
tag signifies later. Next, we have a `userData` constant that we can pass to all the instances, so that we can
see they are running a web server. Then, we are declaring a `nameTag` constant. This allows us to use the interpolation
in the loop to ensure that each of our Droplets is tagged with the appropriate name. We can also see that the region
constant is being used in the Droplet declaration and we are adding the meta-information back to the Droplets array for
later use.

Our next piece of infrastructure is our load balancer. We are going to create a public load balancer that will accept
connections on port 80 and forward those connections to the Droplets that are attached on port 80. The infrastructure
block looks like this:

```typescript
const lb = new digitalocean.LoadBalancer("public", {
    dropletTag: dropletTypeTag.name,
    forwardingRules: [{
        entryPort: 80,
        entryProtocol: digitalocean.Protocols.HTTP,
        targetPort: 80,
        targetProtocol: digitalocean.Protocols.HTTP,
    }],
    healthcheck: {
        port: 80,
        protocol: digitalocean.Protocols.TCP,
    },
    region: region,
});

export const endpoint = lb.ip;
```

The configuration is made up of an array of forwarding rules. Here, we forward traffic from the load balancer to
the Droplets. Then we have a health check that makes sure that port 80 is actually available and we deploy
the load balancer into the region that we declared as a constant earlier. The interesting thing about load balancers in
DigitalOcean is that you can attach instances by Droplet tag without knowing the Droplet IDs. Here, we configure
all Droplets that have the tag `demo-app`, in this region, to be attached to the load balancer.

Running this gives us:

```bash
Updating (dev):

     Type                                Name                     Status
 +   pulumi:pulumi:Stack                 do-ref-architecture-dev  created
 +   ├─ digitalocean:index:Tag           web-0                    created
 +   ├─ digitalocean:index:Tag           web-1                    created
 +   ├─ digitalocean:index:Tag           web-2                    created
 +   ├─ digitalocean:index:Tag           demo-app                 created
 +   ├─ digitalocean:index:Droplet       web-0                    created
 +   ├─ digitalocean:index:Droplet       web-1                    created
 +   ├─ digitalocean:index:LoadBalancer  public                   created
 +   └─ digitalocean:index:Droplet       web-2                    created

Outputs:
    endpoint: "45.55.120.64"

Resources:
    + 9 created

Duration: 3m5s
```

You should be able to take the endpoint address and put it into the browser or you should be able to curl it as follows:

```bash
curl "$(pulumi stack output endpoint)"
```

We are constantly working on ways to make Pulumi more productive to use with DigitalOcean. Pulumi is free and open
source. You can get started with Pulumi today at [https://www.pulumi.com](https://www.pulumi.com).
