---
title: "My Pulumi: Managing My DNS"
date: 2022-03-29T10:00:00Z
draft: false
meta_desc: In this aritcle, Rawkode shows how he uses Pulumi to manage the DNS records for his many domains.
meta_image: meta.png
authors: ["david-flanagan"]
tags: ["Domains", "DNS"]
---

Hello, my name is David Flanagan, and I own more domains than I need. The problem is I have too many ideas; and as we all know, ideas don't become real until you buy the domain name. Unfortunately, more often than not, that's about as far as my ideas go---because, **life**. That being said, I do try to keep my DNS records under control in the event that life affords me the time to follow-up on one of these ideas. Today, I want to show you how I do that.

## Overview

Using Pulumi's ComponentResource API, we're able to provide a nice developer experience for manipulating DNS records through methods on an object---we call this object the "Domain Controller." I have a domain controller for every domain that I own. Through this controller I can add DNS records through helper methods that keep the interface as simple as can be.

So, let's explore this. First, I'll show you the consumer API and how you work with the `Controller`, then I'll show you how it was put together.

### Fetching the Controller

First, we need to request a controller for our domain name we want to manipulate. This creates a new object based on our `Controller` class.

```typescript
const rawkodeDev = new Controller("rawkode.dev");
```

### Creating Records

Now that we have a controller for the `rawkode.dev` domain, we can start to add records. As with pretty much every domain, there's a selection of things required out of the box:

- MX records for email configuration
  - or an SPF record to note that the domain will not be used for email
- TXT records for dmarc and other verification purposes
- A/CNAME records for any subdomains in-use

#### Configuring Apex

My website is delivered via [Vercel](https://vercel.com), so I need an A record configured with their BGP-advertised ingress address. While I prefer to host my website as [no-www](https://dropwww.com/), I do create a `www` record to redirect as required.

```typescript
zone.createRecord("@", "A", ["76.76.21.21"]);
zone.createRecord("www", "CNAME", [`${DOMAIN}`]);
```

#### Configuring for Email

I typically use GSuite for any of my domains that have email configured. The domain controller class we extend provides a `createMxRecord` method. We explicitly separate this from `createRecord` because we need some conveniences, such as a unique name for each record when there are multiple with the same priority.

```typescript
zone.createMxRecord("@", 1, "aspmx.l.google.com");
zone.createMxRecord("@", 5, "alt1.aspmx.l.google.com");
zone.createMxRecord("@", 5, "alt2.aspmx.l.google.com");
zone.createMxRecord("@", 10, "alt3.aspmx.l.google.com");
zone.createMxRecord("@", 10, "alt4.aspmx.l.google.com");
```

If we don't want email active for this domain, then we can also disable it:

```typescript
zone.disableEmail();
```

### Where is my DNS?

The thing I love about this approach is that you've no idea where I host my DNS. That's intentional. It's not important when I'm configuring records on my domains. In fact, I've moved my DNS several times over the last 18 months, and it's required very little change to my code, requiring only trivial changes to the underlying `Controller`. I like that.

For the record, I'm currently using [Cloudflare](https://cloudflare.com); though I have used [DNSimple](https://dnsimple.com), Route53, Google Cloud DNS, and others. I like to experiment. 😅

## How Does it Work?

We're going to dive into this `Controller` class in a bit more detail, but if you'd prefer to see my real-world code, [check it out here](https://github.com/rawkode/rawkode/tree/main/infrastructure/src/dns).

The first thing we need for our `Controller` is a skeleton of a `ComponentResource`.

```typescript
import { ComponentResource } from "@pulumi/pulumi";

export class Controller extends ComponentResource {
}
```

I have a few properties on this class that allow us to track some internal state, such as:

```typescript
readonly domainName: string;
readonly zone: cloudflare.Zone;
private emailDisabled: boolean = false;
private records: cloudflare.Record[];
private mxCounter = 0;
```

Quickly followed by the `constructor` that is responsible for creating the zone on our DNS provider and instantiating some of these initial properties:

```typescript
constructor(domainName: string) {
  super(`rawkode:DnsController`, `${domainName}`);

  this.domainName = domainName;
  this.records = [];

  this.zone = new cloudflare.Zone(
    domainName,
    {
      zone: domainName,
      type: "full",
      plan: "free",
    },
    {
      protect: true,
      parent: this,
    }
  );
}
```

Let's jump to something a bit more useful and look at record creation.

```typescript
public createRecord(name: string, type: string, values: string[]): void {
  values.forEach((value, index) => {
    const record = new cloudflare.Record(
      this.resourceName(`${name}-${index}`, type),
      {
        zoneId: this.zone.id,
        name: this.recordName(name),
        ttl: 300,
        type,
        value,
      },
      { parent: this.zone, protect: false, deleteBeforeReplace: true }
    );

    this.records.push(record);
  });

  return;
}
```

This function really only creates a new `cloudflare.Record`, but because we're using a `ComponentResource`, we can also leverage internal/private functions that remove duplication from our code and help us keep things DRY (Don't Repeat Yourself).

There are two examples above:`this.resourceName(`${name}-${index}`, type)` and `name: this.recordName(name),`. We have two functions, `resourceName()` and `recordName()` that help sanitize some of our inputs.

First, `resourceName` gives us a uniquely namespaced (by domain name) resource name for Pulumi. It has "DNS-knowledge" that if there's no subdomain name or we're using DNS notation of "@" for "root", that this should be named as such. We also include the record type into the name to allow multiple records on subdomains when the type is different, such as TXT and MX records. We pretty much do the same for `recordName`, only it returns a FQDN. `ComponentResource`s are amazing for encapsulating this type of internal knowledge into the resource and away from the consumer.

```typescript
private resourceName(name: string, type: string): string {
  if (name.length == 0) {
    return `${this.domainName}-${type}`;
  }

  if (name == "@") {
    return `${this.domainName}-${type}`;
  }

  return `${this.domainName}-${type}-${name}`;
}
```

OK. What about email records? Well, let's take a look at "disabling" email. I've said "disabling" because we can't actually stop people from using the domain when they're sending spammy emails, but the SPF record should provide enough knowledge to email companies that email shouldn't be expected from this domain.

The first thing we do inside `disableEmail()` is ensure that the consumer hasn't already set any MX records. If they have, then we'll issue an error. You can't configure email AND discourage it at the same time. We then set our boolean value to `true`, which will be used in our `createMxRecord` function later. Lastly, we can create the TXT record on our domain that tells Google et al. that email shouldn't be accepted from this domain.

```typescript
public disableEmail(): void {
  if (this.mxCounter > 0) {
    throw new Error(
      `Cannot disable email for ${this.domainName} if MX records exist.`
    );
  }

  this.emailDisabled = true;

  this.records.push(
    new cloudflare.Record(
      this.resourceName(`disable-email`, "txt"),
      {
        zoneId: this.zone.id,
        name: "@",
        ttl: 300,
        type: "TXT",
        value: `"v=spf1 -all"`,
      },
      { parent: this.zone, protect: false, deleteBeforeReplace: true }
    )
  );

  return;
}
```

We're being good email citizens here. 😃 Let's take a look at our `createMxRecord` function.

```typescript
public createMxRecord(name: string, priority: number, value: string): void {
  if (this.emailDisabled) {
    throw new Error(
      `Cannot add MX records if ${this.domainName} has email disabled.`
    );
  }

  const record = new cloudflare.Record(
    this.resourceName(`${name}-${this.mxCounter++}`, "MX"),
    {
      zoneId: this.zone.id,
      name: this.recordName(name),
      ttl: 300,
      type: "MX",
      priority,
      value,
    },
    { parent: this.zone, protect: false, deleteBeforeReplace: true }
  );

  this.records.push(record);

  return;
}
```

It's very similiar to our `createRecord` function, only this one has the `emailDisabled` check to ensure our consumers don't try to do the silly thing. We also increment our MX counter to keep track of how many MX records we've created, so that records with the same priority can be distinguished and have unique URNs when created.

## What's Next?

I rely on this code a lot, but it's far from finished. I try to improve it as often as time allowed, and next on my list is to support multiple DNS providers on the controller as well as "alias domains."

Multiple DNS providers on the controller would allow me to have backup DNS records on another provider in the event that one should be unavailable, or just to allow me to experiment and continue to try other providers without a bigger time commitment.

Alias domains would allow me to stop duplicating a lot of the code I use for domains that share the same behaviors, such as URL shorteners. Instead of:

```typescript
const rawkodeSh = new Controller("rawkode.sh");
const rawkoDe = new Controller("rawko.de");
const rawkodeLive = new Controller("rawkode.live");
```

I could hopefully do:

```typescript
const rawkodeShorts = new Controller("rawko.de", {
  aliasDomains: ["rawkode.sh", "rawkode.live"],
})
```

Pulumi facilitates all these abstractions that allow us to make our lives easier. This is what I do with my Pulumi programs, but what do you do with yours?

Drop me an [email](mailto:rawkode@pulumi.com) or [tweet](https://twitter.com/rawkode) and share what you're doing with Pulumi.

Speak soon.
