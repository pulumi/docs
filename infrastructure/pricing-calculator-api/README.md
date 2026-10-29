# Pricing calculator API

A Lambda that estimates a Pulumi Cloud monthly bill from usage, using the same formula as the `/pricing/` cost calculator. Intercom's Fin calls it through a data connector to answer "how much will this cost?" questions. It's served at `https://www.pulumi.com/api/pricing` once the site stack is wired to it (see [Rollout](#rollout)).

This is its own Pulumi program, separate from the site stack in `infrastructure/index.ts`. The site stack reaches it only by stack reference.

## API

`GET` with query parameters, or `POST` with a JSON body using the same field names.

| Field | Meaning |
|---|---|
| `edition` | Required. `essentials`, `pro`, or `enterprise`. Case, surrounding spaces, and quotes are ignored. |
| `iac_resources` | IaC resources held for the whole month. |
| `iac_resource_hours` | IaC resource-hours, for resources that existed part of the month. Pooled with `iac_resources` before the included resources apply. |
| `esc_secrets`, `esc_secret_hours` | ESC secrets, as a monthly count or as secret-hours. |
| `insights_resources`, `insights_resource_hours` | Pulumi Discovery resources, as a monthly count or as resource-hours. |
| `workflow_minutes` | Deployment workflow minutes. |
| `neo_million_tokens` | Pulumi Neo usage, in millions of tokens. |

Every number defaults to 0, and an empty value counts as 0. Unknown fields are rejected, so a misspelled name fails loudly instead of being ignored.

```
$ curl "https://www.pulumi.com/api/pricing?edition=essentials&iac_resources=1000"
{"ok":true,
 "estimate":{"edition":"essentials","creditsUsed":131.25,"includedCredits":40,"baseUsd":40,
             "overageUsd":91.25,"totalUsd":131.25,"volumePricingLikely":false},
 "disclaimer":"Estimate at list prices. ...",
 "rates":{"source":"live","refreshedAt":"2026-10-29T17:00:00.000Z"}}
```

A 400 response is `{"ok": false, "error": "validation_failed", "fields": {...}}`, with one message per bad field. A bad `edition` message includes the value received, which is the quickest way to debug a caller.

Whoever shows an estimate to a customer should pass `disclaimer` along with it. The rates are list prices: Pro and Enterprise get volume discounts, so large estimates are an upper bound. `volumePricingLikely` is true above 4,750 IaC resources, where volume pricing usually applies.

## Where the rates come from

pulumi/marketing-web owns the prices. The API reads them from `https://www.pulumi.com/pricing.md` in two places:

- **At deploy:** `pulumi preview` and `pulumi up` parse the page and compare it with `src/pricing.ts`. By default (`pricingCheck: update`) the deploy uses the page's rates and warns about any difference. It fails if the page can't be read or parsed.
- **While running:** the Lambda re-reads the page at most once an hour (`rateRefreshSeconds`). If that fails, it keeps serving the last good rates and raises the `refresh-failed` alarm.

A price change on `/pricing/` therefore reaches callers within the hour, with no deploy. Update `src/pricing.ts` when the deploy warns, so the built-in fallback stays current.

The parser depends on the wording of the page's "Cost estimation" section and the hourly rate rows in its comparison tables. If marketing-web reformats them, the refresh and deploys both fail until `src/livePricing.ts` is updated. `src/testdata/pricing.md` is the snapshot its tests run against; refresh it at the same time.

## Configuration

| Key | Default | |
|---|---|---|
| `aws:region` | | `us-west-2` |
| `pricingCheck` | `update` | `update`, `error`, `warn`, or `off`. See `index.ts`. |
| `pricingUrl` | `https://www.pulumi.com/pricing.md` | |
| `rateRefreshSeconds` | `3600` | `0` turns the runtime refresh off. |
| `reservedConcurrency` | `10` | Caps concurrent invocations; requests beyond it get a 429. |
| `alarmEmail` | | Subscribes an address to the alarm topic. AWS emails it a confirmation link first. |

## Rollout

1. Deploy this stack: `yarn install && pulumi stack select pulumi/pricing-calculator-api/testing && pulumi up`. Use AWS credentials for the testing account.
1. Point the site's testing stack at it with `www.pulumi.com:pricingApiStack: pulumi/pricing-calculator-api/testing` in `infrastructure/Pulumi.www-testing.yaml`, and deploy that. Check `https://www.pulumi-test.io/api/pricing?edition=essentials&iac_resources=1000` returns `totalUsd: 131.25`.
1. Repeat both steps with the `production` stacks, then update the Fin data connector's URL to `https://www.pulumi.com/api/pricing`.

The site stack only reads this stack's `url` output, so the pricing stack has to exist before a site stack names it. Remove `pricingApiStack` from the site stack before destroying a pricing stack.

## Connecting Intercom Fin

Create a data connector with a `GET` request to:

```
https://www.pulumi.com/api/pricing?edition={{edition}}&iac_resources={{iac_resources}}&iac_resource_hours={{iac_resource_hours}}&esc_secrets={{esc_secrets}}&esc_secret_hours={{esc_secret_hours}}&insights_resources={{insights_resources}}&insights_resource_hours={{insights_resource_hours}}&workflow_minutes={{workflow_minutes}}&neo_million_tokens={{neo_million_tokens}}
```

Each `{{...}}` has to be the connector's data input, inserted with Intercom's picker. Typed text is sent as written. Fin's guidance should tell it to quote the API's totals rather than calculating its own, and to include the `disclaimer`.

## Operating

Every request is logged as one `pricing_request` line, holding the method, query string, and the first 500 characters of any body (usage numbers only, no personal data). Logs are kept 30 days in `/aws/lambda/pricing-calculator-api-<stack>`. When a caller gets an unexpected 400, its request line shows what it actually sent.

Alarms publish to the SNS topic in the `alarmTopicArn` output:

| Alarm | Fires when | What to do |
|---|---|---|
| `errors` | The handler threw | A bug. The log group has the stack trace. |
| `throttles` | 10+ requests in 5 minutes hit `reservedConcurrency` | Check the request log for abuse; otherwise raise the limit. |
| `refresh-failed` | The pricing page couldn't be read or parsed | The API is serving its last good rates. Usually the page changed format: update `src/livePricing.ts` and the test snapshot. |

## Development

```
yarn install
yarn test   # compiles, checks every suite is compiled, runs them
yarn lint
```

`pricing-calculator-api-tests.yml` runs both on every PR that touches this directory. The handler is shipped through Pulumi's closure serialization, which doesn't preserve every value it captures (a `Set` arrives as a plain object). `handler.test.ts` runs the serialized handler for that reason; keep captured state to plain objects and arrays.
