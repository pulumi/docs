---
title: Webhooks
meta_desc: An overview of how to use Webhooks within the Pulumi Cloud Service.
aliases:
- /docs/reference/service/webhooks/
- /docs/console/extensions/webhooks/
---

> Pulumi Webhooks is a feature available on the Pulumi Team and Enterprise editions.
> If you’re keen to try it out, start a [Team Edition trial](https://app.pulumi.com/site/organizations/add) now.

Pulumi Webhooks allow you to notify external services of events
happening within your Pulumi organization or stack. For example,
you can trigger a notification whenever a stack is updated or a team is modified.
Whenever an event occurs, Pulumi will send an HTTP `POST` request to
all registered webhooks. The webhook can then be used to emit some
notification, start running integration tests, or even update additional stacks.

Webhooks can be used for pretty much anything you want, and are the foundation
of most _ChatOps_ workflows.

## Management

Webhooks can be attached to either a stack or an organization. Stack webhooks
will be notified whenever a stack is updated or changed. Organization
webhooks will be notified for events happening within each of the organization's
stacks and organization-specific events like team or membership
changes.

> There are some restrictions for the number of webhooks that can be registered
> when using the Pulumi Team editions. [Contact us]({{< relref "/about#contact-us" >}})
> if you need the limit increased.

The Webhooks management page is on the Stack or Organization Settings tab.

![Organization webhooks](/images/docs/reference/service/webhooks/org-webhooks.png)

### Creating a Webhook

To create a new webhook, provide a _display name_, _webhook
URL_, and an optional _shared secret_.

![Stack webhooks](/images/docs/reference/service/webhooks/stack-webhooks.png)

If a shared secret is provided, webhook deliveries will contain a signature
in the HTTP request header that can be used to authenticate messages as coming from
the Pulumi Console.

For details on how to verify payload signatures, see the _Headers_ section below.

## Event Notifications

The following events will be emitted to webhooks registered to a stack or an organization.
Organization-level webhooks will be sent webhook events from all of the stacks within
that organization.

| Event Kind | Triggered |
| --- | --- |
| `stack_update` | Whenever a stack is updated. |
| `stack_preview` | Whenever a stack update is previewed. |

<p></p>

The following events are only delivered to organization-based webhooks.

| Event Kind | Triggered |
| --- | --- |
| `stack` | Whenever a stack is created or deleted within an organization. |
| `team`  | Whenever a team is created, updated, or deleted. |

## Payloads

Each webhook payload has a format specific to the payload being emitted. Every payload will contain a sender, organization,
and stack reference as appropriate. For examples of specific payloads, see _Payload Reference_ below.

Each webhook will contain a `user` field, which is the user who requested the action, an `organization` which is
the organization name, and a URL for the event. It will also contain the `stackName` for the stack which was modified when applicable.

### Headers

Payloads contain several headers.

| Header | Description |
|--------|-------------|
| `Pulumi-Webhook-ID` | Unique ID for each webhook sent which you can reference when looking at delivery logs in the Pulumi Console. |
| `Pulumi-Webhook-Kind` | The kind of webhook event, e.g. `stack_update`. |
| `Pulumi-Webhook-Signature` | Only set if the webhook has a shared secret. HMAC hex digest of the request payload, using the `sha256` hash function and the webhook secret as the HMAC key. |

<p></p>

The following snippets show how to compute and verify the webhook signature.
For examples in other languages, see [danharper/hmac-examples](https://github.com/danharper/hmac-examples).

{{< langchoose >}}

```javascript
var crypto = require('crypto');

const sharedSecret = ...
const payload = req.body.toString();

var hmacAlg = crypto.createHmac('sha256', sharedSecret);
var expectedSignature = hmac.update(payloadBody).digest('hex');
```

```typescript
import * as crypto from "crypto";

const sharedSecret = ...
const payload = req.body.toString();

const hmacAlg = crypto.createHmac("sha256", stackConfig.sharedSecret);
const hmac = hmacAlg.update(payload).digest("hex");

const result = crypto.timingSafeEqual(Buffer.from(webhookSig), Buffer.from(hmac));
```

```python
import hashlib
import hmac
import base64

message = bytes('...', 'utf-8')
secret = bytes('...', 'utf-8')

hash = hmac.new(secret, message, hashlib.sha256)
hash.hexdigest()

expected_signature = base64.b64encode(hash.digest())
```

```go
func computeSignature(payload []byte, secret string) string {
	mac := hmac.New(sha256.New, []byte(secret))
	_, err := mac.Write(payload)
	contract.AssertNoErrorf(err, "computing HMAC digest")
	return fmt.Sprintf("%x", mac.Sum(nil))
}
```

## Payload Examples

Most payloads contain `user` and `organization` fields. `user` contains the
identity of the user who triggered the webhook. For example, the person who initiated
the stack update or performed the action.

> The Pulumi Webhook payloads are under development, and may be changed from
> time to time. See the [Pulumi Community Slack](https://slack.pulumi.com/) for
> any announcements or changes.

### Stack Creation

```
{
	"user": {
		"name": "Morty Smith",
		"githubLogin": "morty",
		"avatarUrl": "https://crazy-adventures.net/morty.png"
	},
	"organization": {
		"name": "Crazy Adventures",
		"githubLogin": "crazy-adventures",
		"avatarUrl": "https://crazy-adventures.net/logo.png"
	},
	"action": "created",
	"projectName": "website",
	"stackName": "website-prod"
}
```

### Team Stack Update

```
{
	"user": {
		"name": "Morty Smith",
		"githubLogin": "morty",
		"avatarUrl": "https://crazy-adventures.net/morty.png"
	},
	"organization": {
		"name": "Crazy Adventures",
		"githubLogin": "crazy-adventures",
		"avatarUrl": "https://crazy-adventures.net/logo.png"
	},
	"action": "updated",
	"stackName": "website-prod",
	"team": {
		"kind": "github",
		"name": "Adventurers",
		"members": [
			{
				"name": "Morty Smith",
				"githubLogin": "morty",
				"avatarUrl": "https://crazy-adventures.net/morty.png"
			}
		],
		"stacks": [
			{
				"stackName": "website-prod",
				"permission": 3
			}
		]
	}
}
```

### Stack Update

```
{
	"user": {
		"name": "Morty Smith",
		"githubLogin": "morty",
		"avatarUrl": "https://crazy-adventures.net/morty.png",
	},
	"organization": {
		"name": "Crazy Adventures",
		"githubLogin": "crazy-adventures",
		"avatarUrl": "https://crazy-adventures.net/logo.png"
	},
	"projectName": "website",
	"stackName": "website-prod",
	"updateUrl": "https://app.pulumi.com/crazy-adventures/website-prod/42",
	"kind": "refresh",
	"result": "succeeded",
	"resourceChanges": {
		"update": 3,
		"delete": 1,
		"update-replace": 2
	}
}
```

### `stack_preview` event

```
{
	"user": {
		"name": "Morty Smith",
		"githubLogin": "morty",
		"avatarUrl": "https://crazy-adventures.net/morty.png",
	},
	"organization": {
		"name": "Crazy Adventures",
		"githubLogin": "crazy-adventures",
		"avatarUrl": "https://crazy-adventures.net/logo.png"
	},
	"projectName": "website",
	"stackName": "website-prod",
	"updateUrl": "https://app.pulumi.com/crazy-adventures/website-prod/11bf162b-d9d5-4715-8f88-20dcd0e0b167",
	"kind": "update",
	"result": "failed",
	"resourceChanges": {
		"update": 3,
		"delete": 1,
		"update-replace": 2
	}
}
```

## Next Steps

- ["Deploy with Pulumi" Button]({{< relref "pulumi-button" >}})
