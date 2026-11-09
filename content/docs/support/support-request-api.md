---
title_tag: "Support request API for agents"
meta_desc: "File a Pulumi support request with a single JSON POST to /api/support, without driving the web form. Fields, limits, and status codes."
title: Support request API
h1: Support request API
menu:
    support:
        name: Support request API
        parent: support-home
        weight: 4
        identifier: support-request-api
---

<!--
The contract on this page mirrors infrastructure/support-form/validation.ts and
infrastructure/support-form/handler.ts. Change one and change the other in the
same PR, or this page documents an API that no longer exists.
-->

AI agents and scripts can open a ticket with the Pulumi support team by posting JSON to `https://www.pulumi.com/api/support`, without driving the [web form](/support/new/). The endpoint needs no authentication and no cookies. Replies come by email to the address in the request, so give one that a person reads.

{{% notes type="warning" %}}
**Never send a `leave_blank` key.** The rendered web form carries a hidden `leave_blank` input, which is a spam trap. A request that sets it is discarded behind a response indistinguishable from success, so no ticket is ever filed. Post the six fields below rather than scraping the HTML form for its inputs.
{{% /notes %}}

## Request

Send a `POST` with `Content-Type: application/json` and exactly these six fields. Any other top-level key except `leave_blank` is rejected with a `422`. The one exception is `leave_blank`, which is accepted and silently discarded; see the warning above.

```bash
curl -X POST https://www.pulumi.com/api/support \
  -H "Content-Type: application/json" \
  -d '{
    "email": "you@example.com",
    "name": "Your Name",
    "organization": "your-pulumi-org",
    "priority": "Normal",
    "subject": "Stack update stuck in progress",
    "description": "What you expected, what actually happened, and any relevant code or CLI output."
  }'
```

## Fields

All fields are required strings.

| Field | Rules |
|-------|-------|
| `email` | 254 characters or fewer, in the form `name@domain.tld`. Whitespace, `<`, `>`, `"`, `,`, and `;` are rejected. |
| `name` | 200 characters or fewer. |
| `organization` | The bare organization name from `https://app.pulumi.com/<org>`. Starts with a letter or number, followed by letters, numbers, hyphens, and underscores, 40 characters or fewer. A pasted Pulumi Cloud console URL is reduced to the organization name for you. |
| `priority` | `Normal` or `Urgent`, matched case-insensitively. |
| `subject` | 200 characters or fewer. |
| `description` | Between 10 and 20,000 characters. Markdown and line breaks are kept. |

Every field is trimmed, and control characters (except tab and newline) and bidirectional text overrides are stripped before the limits apply. The whole request body must be 256 KB or smaller.

## Responses

A successful request returns `200`:

```json
{"ok": true, "id": "3f1c...", "conversationId": "215475836771541"}
```

A validation failure returns `422` with a `fields` object keyed by field name, so each error maps back to its input without parsing prose. A problem with the payload as a whole, such as an unknown key or a body that isn't a JSON object, is reported under `_form`:

```json
{"ok": false, "error": "validation_failed", "fields": {"email": "Enter a valid email address."}}
```

| Status | Meaning |
|--------|---------|
| `200` | The request was filed. |
| `400` | The `Content-Type` isn't `application/json` (`unsupported_content_type`), the body is empty (`empty_body`), or the body isn't valid JSON (`invalid_json`). |
| `404` | The request was blocked before it reached the endpoint. This is an HTML page, not JSON. |
| `405` | The method wasn't `POST` (`method_not_allowed`). |
| `413` | The body is larger than 256 KB (`payload_too_large`). |
| `422` | One or more fields failed validation (`validation_failed`). |
| `429` | The request was rate limited. Back off rather than retrying immediately. |
| `502` | The ticket couldn't be created (`conversation_creation_failed`). The response includes an `id` to quote if you contact support another way. |

A `429`, a `404`, and a `413` for a body large enough to exceed the platform's invocation limit can all arrive without the JSON `ok`/`error` envelope, so check the status code before parsing the body.

## Next steps

- [Getting support](/docs/support/getting-support/)
- [Filing GitHub issues](/docs/support/filing-issues/)
