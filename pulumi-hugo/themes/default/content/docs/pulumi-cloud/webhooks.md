---
title_tag: "Pulumi Cloud Webhooks"
meta_desc: Pulumi Webhooks allow you to notify external services of events happening within your Pulumi organization. Learn how to create and manage webhooks here.
title: "Webhooks"
h1: Pulumi Cloud webhooks
menu:
  pulumicloud:
    weight: 8
aliases:
- /docs/reference/service/webhooks/
- /docs/console/extensions/webhooks/
- /docs/intro/console/extensions/webhooks/
- /docs/intro/console/webhooks/
- /docs/intro/pulumi-service/webhooks/
- /docs/intro/pulumi-cloud/webhooks/
---

{{% notes "info" %}}
Pulumi Webhooks is a feature available on the Pulumi Team, Enterprise and Business Critical editions.
To try it out, start a [trial](https://app.pulumi.com/site/trial) now.
{{% /notes %}}

Pulumi Webhooks allow you to notify external services of events
happening within your Pulumi organization. For example,
you can trigger a notification whenever a stack is updated.
Whenever an event occurs, Pulumi will send an HTTP `POST` request to
all registered webhooks. The webhook can then be used to emit a
notification, start running integration tests, or even update additional stacks.

Webhooks can be used for pretty much anything you want, and are the foundation
of most _ChatOps_ workflows.

## Management

Webhooks can be attached to either a stack or an organization. Stack webhooks
will be notified of events specific to the stack. Organization
webhooks will be notified for events happening within each of the organization's
stacks.

The Webhooks management page is on the Stack or Organization Settings tab.

![Organization webhooks](/images/docs/reference/service/webhooks/org-webhooks.png)

### Create a Webhook

Pulumi Webhooks may be created through the UI using the steps outlined below, or by using the
[Webhook resource](https://www.pulumi.com/registry/packages/pulumiservice/api-docs/webhook/) from the Pulumi provider,
or by [using the API](/docs/pulumi-cloud/cloud-rest-api/#create-webhook) directly.

#### Create an Organization Webhook

1. Navigate to **Settings** > **Webhooks**.
2. Select **Create webhook**.
3. Select between a slack-formatted or generic JSON webhooks.
4. If you selected `Slack`, you will be prompted to provide a Slack webhook URL and a display name.
5. If you selected `Webhook`, provide a display name, payload URL, and optionally a secret.
6. Choose between receiving all events or only receiving specific events using the filters menu.

#### Create a Stack Webhook

1. Navigate to the stack.
2. Then navigate to **Settings** > **Webhooks**
3. Select **Create webhook**.
4. Select between a slack-formatted webhook or generic JSON webhooks.
5. If you selected `Slack`, you will be prompted to provide a Slack webhook URL and a display name.
6. If you selected `Webhook`, provide a display name, payload URL, and optionally a secret.
7. Choose between receiving all events or only receiving specific events using the filters menu.

## Event Filtering

Event filtering allows you to choose which events should be delivered to each webhook. You may choose to receive
all events, or filter to specific events (only failures, only deployment events, etc.).
The following table describes the various event filters available and the context in which they are relevant.

| Filter                 | Event Kind      | Webhook Type               | Triggered                         |
|------------------------|-----------------|----------------------------|-----------------------------------|
| `stack_created`        | `stack`         | Organization webhooks only | When a stack is created.          |
| `stack_deleted`        | `stack`         | Organization webhooks only | When a stack is deleted.          |
| `preview_succeeded`    | `stack_preview` | Both                       | When a stack `preview` succeeds.  |
| `preview_failed`       | `stack_preview` | Both                       | When a stack `preview` fails.     |
| `update_succeeded`     | `stack_update`  | Both                       | When a stack `update` succeeds.   |
| `update_failed`        | `stack_update`  | Both                       | When a stack `update` fails.      |
| `destroy_succeeded`    | `stack_update`  | Both                       | When a stack `destroy` succeeds.  |
| `destroy_failed`       | `stack_update`  | Both                       | When a stack `destroy` fails.     |
| `refresh_succeeded`    | `stack_update`  | Both                       | When a stack `refresh` succeeds.  |
| `refresh failed`       | `stack_update`  | Both                       | When a stack `refresh` fails.     |
| `deployment_queued`    | `deployment`    | Both                       | When a deployment is queued.      |
| `deployment_started`   | `deployment`    | Both                       | When a deployment starts running. |
| `deployment_succeeded` | `deployment`    | Both                       | When a deployment succeeds.       |
| `deployment_failed`    | `deployment`    | Both                       | When a deployment fails.          |

## Webhook Formats

When creating a webhook, you can choose between the generic JSON webhook payload or `slack`
formatted events.

### Slack-formatted Webhooks

Slack-formatted webhooks allow you to seamlessly integrate notifications about your Pulumi stacks and organizations
into your Slack workspace by simply providing a [Slack incoming webhook URL](https://api.slack.com/messaging/webhooks)
and optionally choosing which events you want delivered using [event filters](#event-filtering).

You can either create your own Slack app (or use an existing one you may already have installed in your workspace), or
follow the link below to quickly get started with a pre-defined Slack app manifest.

<div class="btn btn-secondary"><a target="_blank" href="https://api.slack.com/apps?new_app=1&manifest_yaml=display_information%3A%0A%20%20name%3A%20pulumi-slack-notifications%0A%20%20description%3A%20Funnel%20Pulumi%20webhooks%20to%20Slack%0A%20%20background_color%3A%20%22%238a3391%22%0Afeatures%3A%0A%20%20bot_user%3A%0A%20%20%20%20display_name%3A%20pulumi-slack-notifications%0A%20%20%20%20always_online%3A%20false%0Aoauth_config%3A%0A%20%20scopes%3A%0A%20%20%20%20bot%3A%0A%20%20%20%20%20%20-%20incoming-webhook%0Asettings%3A%0A%20%20org_deploy_enabled%3A%20false%0A%20%20socket_mode_enabled%3A%20false%0A%20%20token_rotation_enabled%3A%20false" class="tile h-full">Create a Slack app from manifest</a></div>

### Generic JSON Webhooks

When using generic JSON webhooks, Pulumi will send an HTTP `POST` request to
all registered webhooks. The webhook can then be used to emit a
notification, start running integration tests, or even update additional stacks.

{{% notes "info" %}}
If a secret is provided, webhook deliveries will contain a signature in the HTTP request header that can be used
to authenticate messages as coming from the Pulumi Cloud.
{{% /notes %}}

#### Payload Examples

Each webhook payload has a format specific to the payload being emitted. Every payload will contain a sender, organization,
and stack reference as appropriate. For examples of specific payloads, see _Payload Reference_ below.

Each webhook will contain a `user` field, which is the user who requested the action, an `organization` which is
the organization name, and a URL for the event. It will also contain the `stackName` for the stack which was modified when applicable.

##### Stack Creation

```json
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

##### Stack Update

```json
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
	"projectName": "website",
	"stackName": "website-prod",
	"updateUrl": "https://app.pulumi.com/crazy-adventures/website/website-prod/updates/42",
	"kind": "refresh",
	"result": "succeeded",
	"resourceChanges": {
		"update": 3,
		"delete": 1,
		"update-replace": 2
	},
    "isPreview": false
}
```

##### Stack Preview

```json
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
	"projectName": "website",
	"stackName": "website-prod",
	"updateUrl": "https://app.pulumi.com/crazy-adventures/website/website-prod/previews/11bf162b-d9d5-4715-8f88-20dcd0e0b167",
	"kind": "update",
	"result": "failed",
	"resourceChanges": {
		"update": 3,
		"delete": 1,
		"update-replace": 2
	},
    "isPreview": true
}
```

##### Deployment

```json
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
	"projectName": "website",
	"stackName": "website-prod",
	"deploymentUrl": "https://app.pulumi.com/crazy-adventures/website/website-prod/deployments/127",
    "version": 127,
	"operation": "update",
	"status": "running"
}
```

#### Headers

Payloads contain several headers.

| Header                     | Description                                                                                                                                                   |
|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Pulumi-Webhook-ID`        | Unique ID for each webhook sent which you can reference when looking at delivery logs in the Pulumi Cloud.                                                    |
| `Pulumi-Webhook-Kind`      | The kind of webhook event, e.g. `stack_update`.                                                                                                               |
| `Pulumi-Webhook-Signature` | Only set if the webhook has a shared secret. HMAC hex digest of the request payload, using the `sha256` hash function and the webhook secret as the HMAC key. |

The following snippets show how to compute and verify the webhook signature.
For examples in other languages, see [danharper/hmac-examples](https://github.com/danharper/hmac-examples).

{{< chooser language "javascript,typescript,python,go" >}}

{{% choosable language javascript %}}

```javascript
var crypto = require('crypto');

const sharedSecret = ...
const payload = req.body.toString();

var hmacAlg = crypto.createHmac('sha256', sharedSecret);
var expectedSignature = hmac.update(payloadBody).digest('hex');
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as crypto from "crypto";

const sharedSecret = ...
const payload = req.body.toString();

const hmacAlg = crypto.createHmac("sha256", stackConfig.sharedSecret);
const hmac = hmacAlg.update(payload).digest("hex");

const result = crypto.timingSafeEqual(Buffer.from(webhookSig), Buffer.from(hmac));
```

{{% /choosable %}}
{{% choosable language python %}}

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

{{% /choosable %}}
{{% choosable language go %}}

```go
func computeSignature(payload []byte, secret string) string {
	mac := hmac.New(sha256.New, []byte(secret))
	_, err := mac.Write(payload)
	contract.AssertNoErrorf(err, "computing HMAC digest")
	return fmt.Sprintf("%x", mac.Sum(nil))
}
```

{{% /choosable %}}

{{< /chooser >}}

## Additional Resources

* [Managing Github Webhooks with Pulumi](/blog/managing-github-webhooks-with-pulumi/)
* [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api/)
