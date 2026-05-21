---
title: What is a Cloudflare Secret?
meta_desc: "Cloudflare secrets are encrypted variables bound to Workers and Pages projects at runtime. Learn Workers secrets, Pages env vars, Secrets Store, and Wrangler."
meta_image: /images/what-is/what-is-a-cloudflare-secret-meta.png
type: what-is
page_title: "What is a Cloudflare Secret?"
authors: ["diana-esteves"]
---

**A Cloudflare secret is an encrypted variable bound to a [Cloudflare Workers](https://developers.cloudflare.com/workers/) script, a [Cloudflare Pages](https://developers.cloudflare.com/pages/) project, or the account-level [Cloudflare Secrets Store](https://developers.cloudflare.com/secrets-store/), and exposed to the runtime as a property of the `env` object.** Secrets keep API tokens, database credentials, and signing keys out of your worker source and your Git history while still being available to the code at request time.

Cloudflare offers a few overlapping mechanisms depending on what you're building: **Workers Secrets** for individual Workers scripts, **Pages environment variables** for preview and production builds of a Pages project, and the newer **Cloudflare Secrets Store** for account-level secrets that can be bound to many Workers at once. All three encrypt values at rest, deliver them only to the runtime that needs them, and expose them through the same `env.<NAME>` programming model. The `wrangler` CLI is the canonical way to create and update secrets from a developer machine or a CI pipeline.

In this article, we'll cover the key questions about Cloudflare secrets:

* What is a Cloudflare secret used for?
* What are the Cloudflare secret types?
* How do Workers access secrets at runtime?
* How do you create a Cloudflare secret with Wrangler?
* How does Cloudflare protect secrets?
* What are the limits of Cloudflare secrets?
* What are best practices for Cloudflare secrets?
* How does Pulumi manage Cloudflare secrets?
* Frequently asked questions about Cloudflare secrets

## What is a Cloudflare secret used for?

A Cloudflare secret is the right place for any sensitive value a Worker or Pages function needs at request time. Typical uses:

* API tokens for third-party services the Worker calls (Stripe, OpenAI, Slack).
* Database and KV/D1 credentials.
* Signing keys for JWT issuance or webhook verification.
* OAuth client secrets for redirect flows.
* Provider credentials for outbound integrations (AWS access keys, GCP service-account JSON).

For non-sensitive configuration (feature flags, environment names, region settings), use plain text **variables** (`vars` in `wrangler.toml`) instead. Variables aren't encrypted but are visible in the dashboard, which is often what you want for non-sensitive values.

## What are the Cloudflare secret types?

Cloudflare exposes secrets through a few different surfaces, each with a slightly different scope.

| Type | Scope | Created with | Available to |
|---|---|---|---|
| **Workers Secrets** | A single Workers script | `wrangler secret put` | One Worker's `env.<NAME>` |
| **Cloudflare Pages env vars** | A Pages project (preview or production) | Dashboard or `wrangler pages` | Pages Functions and build steps |
| **Cloudflare Secrets Store** | Account-level | Dashboard or API | Any Worker bound to the store |
| **Plain text vars** (not a secret) | Workers or Pages, set in `wrangler.toml` | `wrangler.toml` `[vars]` | Same as the surface, but visible in dashboard |

Workers Secrets are the oldest and most common path. Pages env vars are the Pages-specific equivalent, with separate values per preview and production environment. The newer [Secrets Store](https://developers.cloudflare.com/secrets-store/) is account-level and lets the same secret be bound to many Workers without per-Worker duplication, which makes rotation much easier in large estates.

## How do Workers access secrets at runtime?

Inside a Worker, a secret named `MY_API_KEY` appears as a property on the `env` object that's passed to the handler:

```typescript
export default {
    async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
        const apiKey = env.MY_API_KEY;
        // use apiKey to call an upstream service ...
        return new Response("ok");
    },
};
```

Where `Env` is a TypeScript interface you declare yourself (or generate with `wrangler types`):

```typescript
interface Env {
    MY_API_KEY: string;
}
```

The value lives only in the isolate that handles the request. It doesn't appear in `wrangler` output, the Worker's source bundle, or the Cloudflare dashboard once it's set. For Pages Functions, the same `env` model applies; environment variables and secrets are merged into a single `context.env` object.

## How do you create a Cloudflare secret with Wrangler?

The canonical workflow is `wrangler secret put`, which prompts for the value interactively (so it never lives in shell history):

```bash
$ wrangler secret put MY_API_KEY
? Enter a secret value: › ****************
🌀 Creating the secret for the Worker "my-worker"
✨ Success! Uploaded secret MY_API_KEY

$ wrangler secret list
[
  {
    "name": "MY_API_KEY",
    "type": "secret_text"
  }
]
```

To rotate, run `wrangler secret put` again with the same name; Cloudflare overwrites the existing value and redeploys the Worker. To remove, `wrangler secret delete MY_API_KEY`.

For CI environments, the API token itself (`CLOUDFLARE_API_TOKEN`) should be a CI secret in GitHub Actions, CircleCI, or [Pulumi ESC](/product/esc/) rather than a static value committed to the pipeline.

## How does Cloudflare protect secrets?

Cloudflare encrypts secrets at rest and only exposes them to the isolates that need them.

| Stage | Protection |
|---|---|
| Submission | TLS to the Cloudflare API or dashboard |
| Storage | Encrypted at rest in Cloudflare's storage |
| Delivery to isolate | Decrypted only when an isolate is spun up to handle a request |
| In the isolate | Available as a property on `env`; not readable from source code or build output |
| In logs | Cloudflare doesn't print secret values to standard log streams |
| Across deploys | Persisted through Worker deploys; not bundled into the script source |

Secrets Store adds an account-level encryption layer and shared access controls, so a single secret can be bound to many Workers without duplicating the encrypted blob per script.

## What are the limits of Cloudflare secrets?

* **No native rotation.** Cloudflare doesn't expire or refresh values for you. Rotation means re-running `wrangler secret put` (or the API equivalent) and redeploying.
* **No first-class versioning.** A secret has one current value; the previous value is overwritten on update.
* **Per-Worker scope (without Secrets Store).** Workers Secrets are tied to a single Worker. Sharing the same secret across many Workers traditionally meant uploading it once per Worker; Secrets Store fixes this.
* **Pages env vars are scoped per environment.** Preview and production are independent; setting a value in preview doesn't propagate to production.
* **No fine-grained access within a Worker.** Any code in the Worker can read any of its bound secrets.
* **Limited audit detail.** Audit logs cover secret-management events (create, update, delete) but not per-request reads from the runtime.

## What are best practices for Cloudflare secrets?

* **Use `wrangler secret put`, not `wrangler.toml`.** Secrets entered through the CLI are encrypted at rest and never written to your config file. Anything you put in `[vars]` is plain text.
* **Use Secrets Store for shared values.** For credentials used by many Workers (a single Stripe API key, a single internal token), bind a Secrets Store entry instead of duplicating it per script.
* **Separate preview and production.** Pages env vars and Workers Secrets can take different values per environment; production credentials should never live in a preview environment.
* **Rotate on a schedule.** Even without native rotation, document a cadence and update secrets via `wrangler` or the API.
* **Brokerage over duplication.** When credentials need to live in many places (Cloudflare Workers, a Kubernetes cluster, a CI pipeline), keep the source of truth in [Pulumi ESC](/product/esc/), [HashiCorp Vault](/what-is/what-is-hashicorp-vault/), [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/), or [Google Cloud Secret Manager](/what-is/what-is-google-cloud-secret-manager/) and project values into Cloudflare from there.
* **Don't log `env` objects.** Treat `env` like any other credential vector; serializing it in a debug log is a leak.

## How does Pulumi manage Cloudflare secrets?

The [Pulumi Cloudflare provider](/registry/packages/cloudflare/) treats Workers, Pages projects, and secret bindings as first-class resources, and [Pulumi ESC](/product/esc/) is the natural source of truth for the values.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";

const config = new pulumi.Config();
const accountId = config.require("accountId");
const apiKey = config.requireSecret("apiKey");

const script = new cloudflare.WorkerScript("my-worker", {
    accountId: accountId,
    name: "my-worker",
    content: fs.readFileSync("./worker.js", "utf8"),
    secretTextBindings: [{
        name: "MY_API_KEY",
        text: apiKey,
    }],
});
```

What you get from this pattern:

* The plaintext value lives in [Pulumi ESC](/product/esc/) (or stack-level encrypted config), not in Git or the Pulumi state file in plaintext.
* The Worker script, its secret bindings, and any Pages or Secrets Store resources sit in the same program; refactoring or rolling new credentials is a single PR.
* For estates where the same credential needs to land in Cloudflare, Kubernetes, and a SaaS API, the same ESC environment can broker values into all three.

[Get started with Pulumi for Cloudflare](/registry/packages/cloudflare/) to manage Workers, Pages, DNS, and secrets as code in TypeScript, Python, Go, C#, Java, or YAML.

## Frequently asked questions about Cloudflare secrets

### Are Cloudflare secrets encrypted?

Yes. Workers Secrets, Pages env vars marked as secrets, and Secrets Store entries are all encrypted at rest, transmitted over TLS, and delivered only to the runtime isolate that needs them. Plain text variables defined under `[vars]` in `wrangler.toml` are not encrypted — those are for non-sensitive configuration.

### What's the difference between a Workers Secret and an env var?

Both end up as properties on `env` at runtime, but a **secret** (created with `wrangler secret put`) is encrypted at rest and hidden from the dashboard, while an **env var** (declared under `[vars]` in `wrangler.toml`) is stored as plain text and visible in the dashboard. Use secrets for sensitive values, vars for everything else.

### How do I rotate a Cloudflare secret?

Run `wrangler secret put MY_NAME` again with the new value (or update via API/dashboard). Cloudflare overwrites the previous value and redeploys the Worker. For Pages projects, update the environment variable from the dashboard or `wrangler pages`.

### What is Cloudflare Secrets Store?

[Cloudflare Secrets Store](https://developers.cloudflare.com/secrets-store/) is an account-level secrets store that holds a value once and binds it to many Workers, eliminating the need to upload the same secret per script. It's the recommended path for credentials shared across multiple Workers and for rotating values across an estate.

### Can multiple Workers share the same secret?

With the traditional `wrangler secret put` flow, no — each Worker has its own copy. With **Secrets Store**, yes — define the secret once at the account level and bind it to as many Workers as you need. Rotating then means updating one value.

### Are Pages environment variables the same as Workers Secrets?

They use the same mental model (encrypted variables exposed through `env`) but are scoped to a Pages project rather than a Worker, with separate values for preview and production. The mechanism is the same; the scope is different.

### Can I read a Cloudflare secret value from the dashboard?

No. Once a value is uploaded via `wrangler secret put` or marked as a secret in Pages, it can be updated or deleted but not read back. For debugging, log into the upstream system to verify the value.

### How do I store a multi-line value (like a TLS key) as a Cloudflare secret?

`wrangler secret put` accepts multi-line input through stdin: `wrangler secret put MY_KEY < private-key.pem`. The value is uploaded as a single string; your Worker code reads it back through `env.MY_KEY` and can parse it as needed.

### Should I integrate Cloudflare secrets with an external vault?

For estates beyond a single Cloudflare account, yes. Keep the source of truth in [HashiCorp Vault](/what-is/what-is-hashicorp-vault/), [AWS Secrets Manager](/what-is/what-is-aws-secrets-manager/), [Google Cloud Secret Manager](/what-is/what-is-google-cloud-secret-manager/), or [Pulumi ESC](/product/esc/), and project values into Cloudflare at deploy time. That keeps rotation and audit consistent across providers.

### How do I avoid storing `CLOUDFLARE_API_TOKEN` in plain text in CI?

Treat it as any other CI secret: store it in GitHub Actions secrets, CircleCI contexts, or [Pulumi ESC](/product/esc/), and reference it as an env var in the pipeline. For higher assurance, use Cloudflare's [scoped API tokens](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/) so the CI credential can only do what the pipeline actually needs.

## Learn more

Pulumi puts Cloudflare Workers, Pages, and their secrets into the same IaC workflow as the rest of your stack. Values come from [Pulumi ESC](/product/esc/), `wrangler secret put` is replaced by a reviewable Pulumi diff, and the same program can broker the same credential into Kubernetes or a CI pipeline. [Get started today](/docs/get-started/).

Related reading:

* [What is Secrets Management?](/what-is/what-is-secrets-management/)
* [What is a GitHub Actions Secret?](/what-is/what-is-a-github-action-secret/)
* [What is a CircleCI Secret?](/what-is/what-is-a-circleci-secret/)
* [What is HashiCorp Vault?](/what-is/what-is-hashicorp-vault/)
* [What is AWS Secrets Manager?](/what-is/what-is-aws-secrets-manager/)
* [What is Google Cloud Secret Manager?](/what-is/what-is-google-cloud-secret-manager/)
