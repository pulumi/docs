# Pricing API (`/api/pricing`)

A Lambda that estimates a Pulumi Cloud monthly bill from usage, using the same formula as the `/pricing/` cost calculator. Intercom's Fin calls it through a data connector to answer "how much will this cost?" questions.

It's part of the www.pulumi.com site stack, built the same way as the support form's `/api/support`: `infrastructure/pricingApi.ts` declares the Lambda, Function URL, and log group, and `infrastructure/index.ts` routes `/api/pricing*` to it. The `enablePricingApi` stack config turns it on; it's set in `Pulumi.www-testing.yaml` and `Pulumi.www-production.yaml`, so the normal site deploys create and update it.

| Environment | URL |
|---|---|
| Production | `https://www.pulumi.com/api/pricing` |
| Testing | `https://www.pulumi-test.io/api/pricing` |

The Function URL itself rejects direct calls with a 403: only CloudFront sends the `x-origin-verify` secret the handler requires, so every request goes through the site's WAF rate limit.

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

pulumi/marketing-web owns the prices. The Lambda starts from the copy in `pricing.ts` and re-reads `https://www.pulumi.com/pricing.md` at most once an hour (`liveRates.ts`). If that fails, it keeps serving the last good rates and logs `pricing_rates_refresh_failed`. A price change on `/pricing/` therefore reaches callers within the hour, with no deploy. `rates.source` in each response says whether the estimate used `live` or `built-in` rates.

The site deploy never reads the pricing page, so an unreachable or reformatted page can't block a website deploy. When the refresh logs `pricing_rates_refreshed`, update `pricing.ts` to match, so the built-in fallback stays current.

The parser (`livePricing.ts`) depends on the wording of the page's "Cost estimation" section and the hourly rate rows in its comparison tables. If marketing-web reformats them, the refresh fails until the parser is updated. `testdata/pricing.md` is the snapshot its tests run against; refresh it at the same time.

`PricingApiArgs` in `pricingApi.ts` takes `pricingUrl`, `rateRefreshSeconds` (default 3600; 0 turns the refresh off), and `reservedConcurrency` (default 10), though `index.ts` uses the defaults.

## Connecting Intercom Fin

Create a data connector with a `GET` request to:

```
https://www.pulumi.com/api/pricing?edition={{edition}}&iac_resources={{iac_resources}}&iac_resource_hours={{iac_resource_hours}}&esc_secrets={{esc_secrets}}&esc_secret_hours={{esc_secret_hours}}&insights_resources={{insights_resources}}&insights_resource_hours={{insights_resource_hours}}&workflow_minutes={{workflow_minutes}}&neo_million_tokens={{neo_million_tokens}}
```

Each `{{...}}` has to be the connector's data input, inserted with Intercom's picker. Typed text is sent as written. Fin's guidance should tell it to quote the API's totals rather than calculating its own, and to include the `disclaimer`.

## Operating

There are no alarms: failures are logged, and nothing notifies anyone. Logs are kept 30 days in `/aws/lambda/pricing-api-<stack>` (the `pricingApiFunctionName` stack output names the function). Every request through CloudFront is logged as one `pricing_request` line holding the method, query string, and the first 500 characters of any body (usage numbers only, no personal data). When a caller gets an unexpected 400, its request line shows what it actually sent.

| Log line | Means | What to do |
|---|---|---|
| `Invoke Error` | The handler threw, and the caller got a 500 | A bug. The line has the stack trace. |
| `pricing_rates_refresh_failed` | The pricing page couldn't be read or parsed | The API is serving its last good rates. Usually the page changed format: update `livePricing.ts` and the test snapshot. |
| `pricing_rates_refreshed` | The page's rates changed and the API picked them up | Nothing urgent; update `pricing.ts` to match. |

Requests beyond the reserved concurrency are rejected with a 429 before they reach the handler, so they don't appear in the log group. The Lambda's `Throttles` metric in CloudWatch counts them.

## Development

From `infrastructure/`:

```
yarn test-pricing-api   # compiles the program, checks every suite is compiled, runs them
```

`support-form-tests.yml` runs it on every PR that touches `infrastructure/`. The handler is shipped through Pulumi's closure serialization, which doesn't preserve every value it captures (a `Set` arrives as a plain object). `handler.test.ts` runs the serialized handler for that reason; keep captured state to plain objects and arrays.
