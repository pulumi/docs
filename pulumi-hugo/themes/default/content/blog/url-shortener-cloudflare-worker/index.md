---
title: "Deploying a URL Shortener with Cloudflare Workers"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-06-29T23:00:09+01:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Need a URL shortener that responds is milliseconds from anywhere, delivered from over 250 edge locations? Let's deploy one with Pulumi to Cloudflare Workers.

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

You'll need a Pulumi project setup with the [Cloudflare package]({{< relref "/registry/packages/cloudflare" >}}) added to your Pulumi project and an [API token configured]({{< relref "registry/packages/cloudflare/installation-configuration" >}}).

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```shell
pulumi new typescript
npm install @pulumi/cloudflare
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
pulumi new python
pip install pulumi-cloudflare
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
pulumi new go
go get github.com/pulumi/pulumi-cloudflare/sdk/v4/go/...
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
pulumi new yaml
```

{{% /choosable %}}

Now that we've added the package, we need to configure it. You'll need your Cloudflare accountId and an API Token. The permissions you need for the API token are:

- All Accounts
  - Workers Tail:Read
  - Workers Scripts:Edit
  - Account Settings:Read
- All Zones
  - Zone Settings:Edit
  - Zone:Edit
  - Workers Routes:Edit
  - SSL and Certificates:Edit
  - DNS:Edit
- All Users
  - User Details:Read

You can reduce the scope of "All Zones", but this means you cannot create a Zone with Pulumi and instead would need to use `getZone`, described below.

```shell
pulumi config set --secret cloudflare:apiToken
pulumi config set cloudflare:accountId
```

## Our URL Shortener

We're going to use plain old JavaScript for our worker code, as this means we don't need to transpile anything down. Our URL Shortener will store domains, short tokens, and long URLs in a JavaScript object. We'll also provide a `DEFAULT_URL` in-case we can't match the `path` requested.

We need to keep our worker source code separate from our Pulumi code, so we'll be keeping this contained within a file called `worker.js`.

```javascript
// worker.js
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

Now on to our Pulumi code. We need to read our JavaScript code and send it to Cloudflare Workers via the `WorkerScript` resource.

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// index.ts
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";

const worker = new cloudflare.WorkerScript(
  "url-shortener",
  {
    name: "url-shortener",
    content: fs.readFileSync("worker.js").toString(),
  },
);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# __main__.py
import pulumi
import pulumi_cloudflare as cloudflare

worker_script_file = open("worker.js", "r")
worker_script = worker_script_file.read()
worker_script_file.close()

worker = cloudflare.WorkerScript("url-shortener",
    name="url-shortener",
    content=worker_script)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// main.go
package main

import (
	"fmt"
    "io/ioutil"

	"github.com/pulumi/pulumi-cloudflare/sdk/v4/go/cloudflare"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
		workerScriptFile, err := ioutil.ReadFile("worker.js")
		if err != nil {
			log.Fatal(err)
		}
		workerScript := string(workerScriptFile)

		worker, err := cloudflare.NewWorkerScript(ctx, "url-shortener", &cloudflare.WorkerScriptArgs{
			Content: pulumi.String(workerScript),
			Name:    pulumi.String("links"),
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Pulumi.yaml
name: url-shortener
runtime: yaml
description: url-shortener in Pulumi YAML
variables:
  workerScript:
    Fn::ReadFile: ./worker.js
resources:
  worker:
    type: cloudflare:index:WorkerScript
    properties:
      name: url-shortener
      content: ${workerScript}
```

{{% /choosable %}}

## Where's the Types?!

If you wanted to use TypeScript for the worker code for some guarantees around the short/long URL objects, you can definitely do so. This does require an additional step to transpile the TypeScript to JavaScript though. Remember to update the Pulumi code to read the `ts` extension.

```typescript
// worker.ts
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

You'll also need a `tsconfig.json`:

```json
{
  "compilerOptions": {
    "experimentalDecorators": true,
    "forceConsistentCasingInFileNames": true,
    "lib": ["ES2020"],
    "module": "ES2020",
    "moduleResolution": "node",
    "noFallthroughCasesInSwitch": true,
    "noImplicitReturns": true,
    "outDir": "dist",
    "pretty": true,
    "sourceMap": true,
    "strict": true,
    "target": "ES2020",
    "outDir": "dist",
    "types": ["@cloudflare/workers-types"]
  },
  "include": ["index.ts"]
}
```

Then we can transpile the code with a `local.Command` resource.

We need to add our command package and then add a local command to our code.

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```shell
npm install @pulumi/command
```

```typescript
// index.ts
import * as command from "@pulumi/command";

const compileWorker = new command.local.Command("compile-worker", {
  create:
    "yarn run tsc >/dev/null && cat ./dist/index.js",
  dir: "../worker",
});
```

You could then use the `stdout` output, `compileWorker.stdout`, from our local command resource for the `content` input on the `WorkerScript` resource, instead of `fs.readFileSync`.

{{% /choosable %}}

{{% choosable language python %}}

```shell
pip install pulumi_command
```

```python
# __main__.py
import pulumi_command as command

compile_worker = command.local.Command('compile-worker', create='yarn run tsc >/dev/null && cat ./dist/index.js')
```

You could then use the `stdout` output, `compile_worker.stdout`, from our local command resource for the `content` input on the `WorkerScript` resource, instead of `open` and `read` on the file.

{{% /choosable %}}

{{% choosable language go %}}

```shell
go get github.com/pulumi/pulumi-command/sdk/go/...
```

```go
// main.go
import (
	"github.com/pulumi/pulumi-command/sdk/go/command/local"
)

compileWorker, err := local.NewCommand(ctx, "compile-worker", &local.CommandArgs{
    Create: pulumi.String("yarn run tsc >/dev/null && cat ./dist/index.js"),
})

if err != nil {
    return err
}
```

You could then use the `stdout` output, `compileWorker.Stdout`, from our local command resource for the `content` input on the `WorkerScript` resource, instead of `ioutil.ReadFile`.

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Pulumi.yaml
resources:
  compileWorker:
    type: command:local:Command
    properties:
      create: yarn run tsc >/dev/null && cat ./dist/index.js
```

You could then use the `stdout` output, `${compileWorker.stdout}`, from our local command resource for the `content` input on the `WorkerScript` resource, instead of `Fn:ReadFile`.

{{% /choosable %}}

## Hooking Up a Domain

Cloudflare Workers allow us to connect a domain name, instead of using the generated `workers.dev` subdomain. To do so with Pulumi, we need to [create]({{< relref "/registry/packages/cloudflare/api-docs/zone/" >}}) or [fetch]({{< relref "registry/packages/cloudflare/api-docs/getzone/" >}}) a Cloudflare Zone.

### Create a Zone(s)

Once we create the `cloudflare.Zone` resource, we also need to create a `cloudflare.ZoneSettingsOverride` resource to ensure that we enable:

- `alwaysUseHttps: "on"`
- `automaticHttpsRewrites: "on"`
- `ssl: "strict"`
- `universalSsl: "on"`.

Without these settings, our traffic will be available over HTTP and ... come on, it's 2022 already.

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// index.ts
const zone = new cloudflare.Zone("pulumi.tv", {
    zone: "pulumi.tv",
    plan: "free",
});

const zoneSettings = new cloudflare.ZoneSettingsOverride("pulumi.tv", {
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

{{% /choosable %}}

{{% choosable language python %}}

```python
# __main__.py
zone = cloudflare.Zone("pulumi.tv", zone="pulumi.tv", plan="free")
zone_settings = cloudflare.ZoneSettingsOverride(
    "pulumi.tv",
    zone_id=zone.id,
    settings=cloudflare.ZoneSettingsOverrideSettingsArgs(
        always_use_https="on",
        automatic_https_rewrites="on",
        ssl="strict",
        min_tls_version="1.2",
        universal_ssl="on",
    ),
)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// main.go
zone, err := cloudflare.NewZone(ctx, "pulumi.tv", &cloudflare.ZoneArgs{
	Zone: pulumi.String("pulumi.tv"),
	Plan: pulumi.String("free"),
})
if err != nil {
	return err
}

_, err = cloudflare.NewZoneSettingsOverride(ctx, "pulumi.tv", &cloudflare.ZoneSettingsOverrideArgs{
	ZoneId: zone.ID(),
	Settings: &cloudflare.ZoneSettingsOverrideSettingsArgs{
		AlwaysUseHttps:         pulumi.String("on"),
		AutomaticHttpsRewrites: pulumi.String("on"),
		UniversalSsl:           pulumi.String("on"),
		Ssl:                    pulumi.String("strict"),
		MinTlsVersion:          pulumi.String("1.2"),
	},
})
if err != nil {
	return err
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Pulumi.yaml
resources:
  zone:
    type: cloudflare:index:Zone
    properties:
      zone: pulumi.tv
      plan: free
  zoneSettings:
    type: cloudflare:index:ZoneSettingsOverride
    properties:
      zoneId: ${zone.id}
      settings:
        alwaysUseHttps: "on"
        automaticHttpsRewrites: "on"
        universalSsl: "on"
        ssl: "strict"
        minTlsVersion: "1.2"
```

{{% /choosable %}}

### Fetch a Zone

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// index.ts
const zone = await cloudflare.getZone({
  name: "pulumi.tv",
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# __main__.py
zone = cloudflare.get_zone(name="pulumi.tv")
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// main.go
zone, err := cloudflare.LookupZone(ctx, &cloudflare.LookupZoneArgs{
    Name: pulumi.String("pulumi.tv"),
})
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Pulumi.yaml
variables:
 zoneId:
   Fn::Invoke:
     Function: cloudflare:index:getZone
     Arguments:
       name: pulumi.tv
     Return: id
 zoneName:
   Fn::Invoke:
     Function: cloudflare:index:getZone
     Arguments:
       name: pulumi.tv
     Return: name
```

{{% /choosable %}}

### Creating the Routes

In-order to actually send traffic to our workers from these zones, we need to setup the DNS records and create the routes. While Cloudflare does provide a web UI to "connect" a custom domain, in beta, this isn't yet available over the Cloudflare API.

Instead, we need to use a proxied DNS record on a subdomain, or domain apex, that points to `workers.dev`.

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// index.ts
const record = new cloudflare.Record(
  "pulumi.tv",
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

const route = new cloudflare.WorkerRoute(
  "pulumi.tv",
  {
    zoneId: zone.id,
    pattern: pulumi.interpolate`${zone.zone}/*`,
    scriptName: worker.name,
  }
);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# __main__.py
from pulumi import Output

record = cloudflare.Record("pulumi.tv",
    name="@", zone_id=zone.id, type="CNAME", value="workers.dev")

route = cloudflare.WorkerRoute("pulumi.tv", zone_id=zone.id, pattern=Output.concat(zone.zone, "/*"), script_name=worker.name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// main.go
_, err = cloudflare.NewRecord(ctx, "pulumi.tv", &cloudflare.RecordArgs{
	Name:   pulumi.String("@"),
	ZoneId: zone.ID(),
	Type:   pulumi.String("CNAME"),
	Value:  pulumi.String("workers.dev"),
})
if err != nil {
	return err
}

_, err = cloudflare.NewWorkerRoute(ctx, "pulumi.tv", &cloudflare.WorkerRouteArgs{
	ZoneId:     zone.ID(),
	Pattern:    pulumi.Sprintf("%s/*", zone.Zone),
	ScriptName: worker.Name,
})
if err != nil {
	return err
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Pulumi.yaml
resources:
  record:
    type: cloudflare:index:Record
    properties:
      name: "@"
      zoneId: ${zone.id}
      type: CNAME
      value: workers.dev
  route:
    type: cloudflare:index:WorkerRoute
    properties:
      # If you fetched a Zone, this would be ${zoneId}
      zoneId: ${zone.id}
      # If you fetched a Zone, this would be ${zoneName}
      pattern: ${zone.zone}/*
      scriptName: ${worker.name}
```

{{% /choosable %}}

## Fin

Lastly, we can run `pulumi up` and run a `curl` 😀

```shell
❯ pulumi up

     Type                                      Name                    Status
 +   pulumi:pulumi:Stack                       short-links-production  created
 +   ├─ cloudflare:index:Zone                  pulumi.tv               created
 +   ├─ cloudflare:index:WorkerScript          links                   created
 +   ├─ cloudflare:index:ZoneSettingsOverride  pulumi.tv               created
 +   ├─ cloudflare:index:Record                pulumi.tv               created
 +   └─ cloudflare:index:WorkerRoute           pulumi.tv               created

Resources:
    + 7 created

Duration: 27s

❯ curl -I https://pulumi.tv
HTTP/2 302
date: Wed, 29 Jun 2022 21:57:20 GMT
location: https://youtube.com/pulumitv

❯ curl -I https://pulumi.tv/modern-infrastructure
HTTP/2 302
date: Wed, 29 Jun 2022 21:57:20 GMT
location: https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw
```

That's it! Deploying your own URL Shortener with some JavaScript and Cloudflare Workers with Pulumi.

## Complete Code

{{% chooser language "typescript,python,go,yaml" / %}}

{{% choosable language typescript %}}

```typescript
// index.ts
import * as pulumi from "@pulumi/pulumi";
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";


const zone = new cloudflare.Zone("pulumi.tv", {
    "pulumi.tv",
    plan: "free",
});

const zoneSettings = new cloudflare.ZoneSettingsOverride("pulumi.tv", {
    zoneId: zone.id,
    settings: {
        alwaysUseHttps: "on",
        automaticHttpsRewrites: "on",
        ssl: "strict",
        minTlsVersion: "1.2",
        universalSsl: "on",
    },
});

const worker = new cloudflare.WorkerScript(
  "pulumi.tv",
  {
    name: "pulumi.tv",
    content: fs.readFileSync("worker.js").toString(),
  }
);

const record = new cloudflare.Record(
    "pulumi.tv",
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

const workerRoute = new cloudflare.WorkerRoute(
    "pulumi.tv",
    {
        zoneId: zone.id,
        pattern: pulumi.interpolate`${zone.zone}/*`,
        scriptName: worker.name,
    }
);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# __main__.py
import pulumi
from pulumi import Output
import pulumi_cloudflare as cloudflare

worker_script_file = open("worker.js", "r")
worker_script = worker_script_file.read()
worker_script_file.close()

worker = cloudflare.WorkerScript("url-shortener", name="url-shortener", content=worker_script)

zone = cloudflare.Zone("pulumi.tv", zone="pulumi.tv", plan="free")
zone_settings = cloudflare.ZoneSettingsOverride(
    "pulumi.tv",
    zone_id=zone.id,
    settings=cloudflare.ZoneSettingsOverrideSettingsArgs(
        always_use_https="on",
        automatic_https_rewrites="on",
        ssl="strict",
        min_tls_version="1.2",
        universal_ssl="on",
    ),
)

record = cloudflare.Record("pulumi.tv",
    name="@", zone_id=zone.id, type="CNAME", value="workers.dev")

route = cloudflare.WorkerRoute("pulumi.tv", zone_id=zone.id, pattern=Output.concat(zone.zone, "/*"), script_name=worker.name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// main.go
package main

import (
	"io/ioutil"
	"log"

	"github.com/pulumi/pulumi-cloudflare/sdk/v4/go/cloudflare"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		workerScriptFile, err := ioutil.ReadFile("worker.js")
		if err != nil {
			log.Fatal(err)
		}
		workerScript := string(workerScriptFile)

		worker, err := cloudflare.NewWorkerScript(ctx, "url-shortener", &cloudflare.WorkerScriptArgs{
			Content: pulumi.String(workerScript),
			Name:    pulumi.String("links"),
		}, pulumi.Protect(true))
		if err != nil {
			return err
		}

		zone, err := cloudflare.NewZone(ctx, "pulumi.tv", &cloudflare.ZoneArgs{
			Zone: pulumi.String("pulumi.tv"),
			Plan: pulumi.String("free"),
		})
		if err != nil {
			return err
		}

		_, err = cloudflare.NewZoneSettingsOverride(ctx, "pulumi.tv", &cloudflare.ZoneSettingsOverrideArgs{
			ZoneId: zone.ID(),
			Settings: &cloudflare.ZoneSettingsOverrideSettingsArgs{
				AlwaysUseHttps:         pulumi.String("on"),
				AutomaticHttpsRewrites: pulumi.String("on"),
				UniversalSsl:           pulumi.String("on"),
				Ssl:                    pulumi.String("strict"),
				MinTlsVersion:          pulumi.String("1.2"),
			},
		})
		if err != nil {
			return err
		}

		_, err = cloudflare.NewRecord(ctx, "pulumi.tv", &cloudflare.RecordArgs{
			Name:   pulumi.String("@"),
			ZoneId: zone.ID(),
			Type:   pulumi.String("CNAME"),
			Value:  pulumi.String("workers.dev"),
		})
		if err != nil {
			return err
		}

		_, err = cloudflare.NewWorkerRoute(ctx, "pulumi.tv", &cloudflare.WorkerRouteArgs{
			ZoneId:     zone.ID(),
			Pattern:    pulumi.Sprintf("%s/*", zone.Zone),
			ScriptName: worker.Name,
		})
		if err != nil {
			return err
		}

		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
# Pulumi.yaml
name: url-shortener
runtime: yaml
description: url-shortener in Pulumi YAML
variables:
  workerScript:
    Fn::ReadFile: ./worker.js
resources:
  worker:
    type: cloudflare:index:WorkerScript
    properties:
      name: url-shortener
      content: ${workerScript}
  zone:
    type: cloudflare:index:Zone
    properties:
      zone: rawkoded.link
      plan: free
  zoneSettings:
    type: cloudflare:index:ZoneSettingsOverride
    properties:
      zoneId: ${zone.id}
      settings:
        alwaysUseHttps: "on"
        automaticHttpsRewrites: "on"
        universalSsl: "on"
        ssl: "strict"
        minTlsVersion: "1.2"
  record:
    type: cloudflare:index:Record
    properties:
      name: "@"
      zoneId: ${zone.id}
      type: CNAME
      value: workers.dev
  route:
    type: cloudflare:index:WorkerRoute
    properties:
      zoneId: ${zone.id}
      pattern: ${zone.zone}/*
      scriptName: ${worker.name}
```

{{% /choosable %}}
