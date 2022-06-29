---
title: "Deploying a URL Shortener with Cloudflare Workers"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-06-30T11:00:09+01:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: In this article, David shows you how to build a URL Shortener and deploy it to a Cloudflare Worker with Pulumi.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - david-flanagan

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - cloudflare
    - serverless

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Cloudflare Workers provides a serverless execution environment that allows you to create entirely new applications or augment existing ones without configuring or maintaining infrastructure. They support NodeJS and WebAssembly (WASM), as well as any language that can compile to WASM.

Delivered from over 250 locations worldwide, Cloudflare could be the best way to bring down that latency that's plaguing your customers. Claiming 0ms for cold starts, automatic scaling, 100k free requests per day, and edge storage built-in: Cloudflare offers a pretty compelling edge compute platform for serverless workloads.

Let's see how we can deploy a low-latency serverless URL shortener to Cloudflare Workers with Pulumi.

<!--more-->

## Setting Up

You'll need the Cloudflare package added to your Pulumi project and an API token configured.

```shell
yarn add @pulumi/cloudflare
pulumi config set --secret cloudflare:apiToken
```

## Our URL Shortener

We're going to use plain old JavaScript for our worker code, as this means we don't need to transpile anything down.

Our URL Shortener will store domains, short tokens, and long URLs in a JavaScript object. Though we'll show you an example of deploying these to Cloudflare Workers via the KV service too.

```javascript
const DEFAULT_URL = "https://youtube.com/pulumitv"

const redirects = {
  "pulumi.tv": {
    "modern-infrastructure": {
        to: "https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw"
    }
  },
};

addEventListener("fetch", async (event) => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const requestUrl = new URL(request.url);
  const domain = requestUrl.host;
  const path = requestUrl.pathname.substring(1);

  console.log(`Handling request on domain ${domain} for ${path}`);

  if (!(domain in redirects)) {
    console.log(`Domain '${domain}' not found`);
    return Response.redirect(DEFAULT_URL);
  }

  if (path === "") {
    return Response.redirect(DEFAULT_URL);
  }

  const paths = redirects[domain];

  if (path in paths) {
    console.log(`Redirecting too ${paths[path].to}`);
    return Response.redirect(paths[path].to);
  }

  console.log(`Path '${path}' not found`);
  return Response.redirect(DEFAULT_URL);
}
```

## Deploying Our Worker

```typescript
const worker = new cloudflare.WorkerScript(
  "url-shortener",
  {
    name: "url-shortener",
    content: fs.readFileSync("worker.js").toString(),
  },
);
```

## Where's the Types?!

If you wanted to use TypeScript for some guarantees around the short/long URL objects, you could store them as such:

```typescript
interface Redirect {
  to: string;
}

interface Redirects {
  [domain: string]: {
    [path: string]: Redirect;
  };
}

const redirects: Redirects = {
  "pulumi.tv": {
    "/": {
      to: "https://youtube.com/pulumitv",
    },
    "modern-infrastructure": {
        to: "https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw"
    }
  },
};
```

Then, using local commands, transpile them into CommonJS:

```typescript
const compileWorker = new command.local.Command("compile-worker", {
  create:
    "yarn run tsc >/dev/null && cat ./dist/index.js",
  dir: "../worker",
});
```

You could then use `compileWorker.stdout` as instead of `fs.readFileSync` within the worker script.

## Hooking Up a Domain

Cloudflare Workers allow us to connect a domain name, instead of using the generated `workers.dev` subdomain. To do so with Pulumi, we need to create or fetch a Zone.

### Create a Domain(s)

Once we create the `cloudflare.Zone` resource, we also need to create a `cloudflare.ZoneSettingsOverride` resource to ensure that we enable `alwaysUseHttps: "on"`, `automaticHttpsRewrites: "on"`, `ssl: "strict"`, and `universalSsl: "on"`.

Without these settings, our traffic will be available over HTTP and ... come on, it's 2022 already.

```typescript
const linkZoneNames = ["pulumi.tv"];

const linkZones = linkZoneNames.map((zone) => {
  const z = new cloudflare.Zone(zone, {
    zone,
    plan: "free",
  });

  new cloudflare.ZoneSettingsOverride(zone, {
    zoneId: z.id,
    settings: {
      alwaysUseHttps: "on",
      automaticHttpsRewrites: "on",
      ssl: "strict",
      minTlsVersion: "1.2",
      universalSsl: "on",
    },
  });

  return z;
});
```

### Fetch a Domain

```typescript
const zone = await cloudflare.getZone({
  name: "pulumi.tv",
});

new cloudflare.ZoneSettingsOverride(zone, {
  zoneId: z.id,
  settings: {
    alwaysUseHttps: "on",
    automaticHttpsRewrites: "on",
    ssl: "strict",
    minTlsVersion: "1.2",
    universalSsl: "on",
  },
});
```

### Creating the Routes

In-order to actually send traffic to our workers from these zones, we need to setup the DNS records and create the routes.

```typescript
linkZones.forEach((zone) => {
  zone.zone.apply((zoneName) => {
    new cloudflare.Record(
      zoneName,
      {
        zoneId: zone.id,
        name: "@",
        type: "CNAME",
        value: "workers.dev",
        proxied: true,
      },
      {
        deleteBeforeReplace: true,
      }
    );

    new cloudflare.WorkerRoute(
      zoneName,
      {
        zoneId: zone.id,
        pattern: pulumi.interpolate`${zone.zone}/*`,
        scriptName: worker.name,
      },
      { dependsOn: [worker] }
    );
  });
});
```

## Fin

That's it! Deploying your own URL Shortener with some JavaScript and Cloudflare Workers.
