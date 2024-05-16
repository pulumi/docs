---
title: "Announcing Slack and Deployment Notifications for Pulumi Cloud"
allow_long_title: true
date: 2023-05-30
meta_desc: Pulumi Cloud now has an easy to set up Slack integration, Pulumi Deployments notifications and event filtering.

meta_image: meta.png
authors:
    - meagan-cojocar
    - komal-ali
tags:
    - features
    - pulumi-cloud
---

Today, we are excited to introduce a set of improvements to [Pulumi Cloud Webhooks](/docs/pulumi-cloud/webhooks) designed to deliver your deployment notifications to where you already spend your time, enabling faster response times to critical issues. Getting your deployment notifications into Slack is now easier than ever on Pulumi Cloud with our new Slack integration. We are also announcing two new improvements to our webhooks feature: Pulumi Deployments events and fine-grained event filtering.

<!--more-->

Teams using Pulumi Cloud have been setting up Slack notifications for their stacks using Pulumi Cloud Webhooks. Webhooks can attach to a Pulumi organization or a Pulumi stack. Starting today, customers can set up a Slack integration, for organization or stack notifications, with fewer steps and without needing to host the infrastructure themselves. We have also expanded the types of event notifications and the filtering options on both Pulumi Cloud Webhooks and for the Slack integration.

Pulumi Cloud Webhooks, including the Slack integration, are available to all Pulumi Cloud organizations.

## Slack integration

![Example of the notifications in Slack](slack.png)

Pulumi Slack notifications enable central visibility for your team. In addition to getting the notification of a successful or failed update, you will have links to take you directly to the stack and directly to the update itself. You can see what Pulumi operation was being run, which user initiated it and the number of resouces changed and unaffected. All of this information in one place lets you spend less time context switching and more time collaborating.


### Setting up the Slack Integration


Before today Pulumi customers used Pulumi Cloud Webhooks to set up generic JSON webhooks. When events occur, we send a HTTP POST request to any registered listeners. Webhooks can then be used to send notifications to an app (like Slack), start running automated tests, or even to update another stack! We have now built support for Slack-formatted webhooks, which allow you to quickly enable notifications about your Pulumi stacks and organizations into your Slack workspace by simply providing a [Slack incoming webhook URL](https://api.slack.com/messaging/webhooks).

You can either create your own Slack app (or use an existing one you may already have installed in your workspace) or you can use the link below to quickly get started with a predefined Slack app manifest.

{{< blog/cta-button "Create a Slack app from manifest" "https://api.slack.com/apps?new_app=1&manifest_yaml=display_information%3A%0A%20%20name%3A%20pulumi-slack-notifications%0A%20%20description%3A%20Funnel%20Pulumi%20webhooks%20to%20Slack%0A%20%20background_color%3A%20%22%238a3391%22%0Afeatures%3A%0A%20%20bot_user%3A%0A%20%20%20%20display_name%3A%20pulumi-slack-notifications%0A%20%20%20%20always_online%3A%20false%0Aoauth_config%3A%0A%20%20scopes%3A%0A%20%20%20%20bot%3A%0A%20%20%20%20%20%20-%20incoming-webhook%0Asettings%3A%0A%20%20org_deploy_enabled%3A%20false%0A%20%20socket_mode_enabled%3A%20false%0A%20%20token_rotation_enabled%3A%20false" "_blank" >}}

By following these steps, which can also be found in [our webhooks documentation](/docs/pulumi-cloud/webhooks), in a few clicks you will have a Slack incoming webhook URL which you can use to set up a webhook in [Pulumi Cloud](https://app.pulumi.com), as shown in the GIF below.

![Setting it up in the UI](https://www.pulumi.com/uploads/content/blog/slack-integration/webhooks_2.gif)

There are Pulumi customers with hundreds to thousands of stacks, making setting up webhooks for each via the UI a time consuming task. In order to enable Pulumi notifications at scale, we have added Pulumi Cloud REST API endpoints for creating webhooks as well as [Pulumi Service Provider](https://www.pulumi.com/registry/packages/pulumiservice) support.

### Pulumi Cloud REST API

Create a webhook via the Pulumi Cloud REST API formatted for Slack, as shown in the example below.

```bash

curl \
  -H "Accept: application/vnd.pulumi+8" \
  -H "Content-Type: application/json" \
  -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
  --request POST \
  --data '{
      "organizationName":"{organization}",
      "projectName":"{project}",
      "stackName":"{stack}",
      "displayName":"#some-slack-channel",
      "payloadUrl":"https://hooks.slack.com/services/...",
      "format": "slack",
      "active":true
  }' \
  https://api.pulumi.com/api/orgs/{organization}/{project}/{stack}/hooks
```

### Pulumi Service Provider

The Pulumi Service provider allows you to create Pulumi Cloud resources via Pulumi. You can provision and manage webhooks, including Slack-formatted webhooks, using this provider.

{{< chooser language "typescript,python,go,csharp,java,yaml" />}}

{{% choosable language typescript %}}

```ts
import * as pulumi from "@pulumi/pulumi";
import { Webhook, WebhookFormat, WebhookFilters } from "@pulumi/pulumiservice";

const orgName = "my-org";

const orgWebhook = new Webhook("org-webhook", {
    active: true,
    displayName: "#my-org-activity-channel",
    organizationName: orgName,
    payloadUrl: "https://hooks.slack.com/services/...",
    format: WebhookFormat.Slack,
    filters: [
        WebhookFilters.StackCreated,
        WebhookFilters.StackDeleted,
        WebhookFilters.DeploymentSucceeded,
        WebhookFilters.DeploymentFailed,
    ],
});

const stackWebhook = new Webhook("stack-webhook", {
    active: true,
    displayName: "#my-stack-activity-channel",
    organizationName: orgName,
    projectName: pulumi.getProject(),
    stackName: pulumi.getStack(),
    payloadUrl: "https://hooks.slack.com/services/...",
    format: WebhookFormat.Slack,
});

export const orgWebhookName = orgWebhook.name;
export const stackWebhookName = stackWebhook.name;

```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml

name: webhook-examples
runtime: yaml
description: An example of provisioning a Pulumi Cloud Webhook via Pulumi Service Provider

resources:
  orgWebhook:
    type: pulumiservice:index:Webhook
    properties:
      active: true
      displayName: "#my-org-activity-channel"
      organizationName: my-org
      payloadUrl: "https://hooks.slack.com/services/..."
      format: slack
      filters:
        - stack_created
        - stack_deleted
        - deployment_succeeded
        - deployment_failed
  stackWebhook:
    type: pulumiservice:index:Webhook
    properties:
      active: true
      displayName: "#my-stack-activity-channel"
      organizationName: my-org
      projectName: webhook-examples
      stackName: dev
      payloadUrl: "https://hooks.slack.com/services/..."
      format: slack

outputs:
  # export the name of the webhooks
  orgWebhookName: ${orgWebhook.name}
  stackWebhookName: ${stackWebhook.name}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_pulumiservice as pulumiservice

org_webhook = pulumiservice.Webhook("orgWebhook",
    active=True,
    display_name="#my-org-activity-channel",
    organization_name="my-org",
    payload_url="https://hooks.slack.com/services/...",
    format=pulumiservice.WebhookFormat.SLACK,
    filters=[
        pulumiservice.WebhookFilters.STACK_CREATED,
        pulumiservice.WebhookFilters.STACK_DELETED,
        pulumiservice.WebhookFilters.DEPLOYMENT_SUCCEEDED,
        pulumiservice.WebhookFilters.DEPLOYMENT_FAILED,
    ])

stack_webhook = pulumiservice.Webhook("stackWebhook",
    active=True,
    display_name="#my-stack-activity-channel",
    organization_name="my-org",
    project_name="webhook-examples",
    stack_name="dev",
    payload_url="https://hooks.slack.com/services/...",
    format=pulumiservice.WebhookFormat.SLACK)

pulumi.export("orgWebhookName", org_webhook.name)
pulumi.export("stackWebhookName", stack_webhook.name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-pulumiservice/sdk/go/pulumiservice"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		orgWebhook, err := pulumiservice.NewWebhook(ctx, "orgWebhook", &pulumiservice.WebhookArgs{
			Active:           pulumi.Bool(true),
			DisplayName:      pulumi.String("#my-org-activity-channel"),
			OrganizationName: pulumi.String("my-org"),
			PayloadUrl:       pulumi.String("https://hooks.slack.com/services/..."),
			Format:           pulumiservice.WebhookFormatSlack,
			Filters: pulumiservice.WebhookFiltersArray{
				pulumiservice.WebhookFiltersStackCreated,
				pulumiservice.WebhookFiltersStackDeleted,
				pulumiservice.WebhookFiltersDeploymentSucceeded,
				pulumiservice.WebhookFiltersDeploymentFailed,
			},
		})
		if err != nil {
			return err
		}
		stackWebhook, err := pulumiservice.NewWebhook(ctx, "stackWebhook", &pulumiservice.WebhookArgs{
			Active:           pulumi.Bool(true),
			DisplayName:      pulumi.String("#my-stack-activity-channel"),
			OrganizationName: pulumi.String("my-org"),
			ProjectName:      pulumi.String("webhook-examples"),
			StackName:        pulumi.String("dev"),
			PayloadUrl:       pulumi.String("https://hooks.slack.com/services/..."),
			Format:           pulumiservice.WebhookFormatSlack,
		})
		if err != nil {
			return err
		}
		ctx.Export("orgWebhookName", orgWebhook.Name)
		ctx.Export("stackWebhookName", stackWebhook.Name)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using System.Linq;
using Pulumi;
using PulumiService = Pulumi.PulumiService;

return await Deployment.RunAsync(() =>
{
    var orgWebhook = new PulumiService.Webhook("orgWebhook", new()
    {
        Active = true,
        DisplayName = "#my-org-activity-channel",
        OrganizationName = "my-org",
        PayloadUrl = "https://hooks.slack.com/services/...",
        Format = PulumiService.WebhookFormat.Slack,
        Filters = new[]
        {
            PulumiService.WebhookFilters.StackCreated,
            PulumiService.WebhookFilters.StackDeleted,
            PulumiService.WebhookFilters.DeploymentSucceeded,
            PulumiService.WebhookFilters.DeploymentFailed,
        },
    });

    var stackWebhook = new PulumiService.Webhook("stackWebhook", new()
    {
        Active = true,
        DisplayName = "#my-stack-activity-channel",
        OrganizationName = "my-org",
        ProjectName = "webhook-examples",
        StackName = "dev",
        PayloadUrl = "https://hooks.slack.com/services/...",
        Format = PulumiService.WebhookFormat.Slack,
    });

    return new Dictionary<string, object?>
    {
        ["orgWebhookName"] = orgWebhook.Name,
        ["stackWebhookName"] = stackWebhook.Name,
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package generated_program;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.pulumiservice.Webhook;
import com.pulumi.pulumiservice.WebhookArgs;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var orgWebhook = new Webhook("orgWebhook", WebhookArgs.builder()
            .active(true)
            .displayName("#my-org-activity-channel")
            .organizationName("my-org")
            .payloadUrl("https://hooks.slack.com/services/...")
            .format("slack")
            .filters(
                "stack_created",
                "stack_deleted",
                "deployment_succeeded",
                "deployment_failed")
            .build());

        var stackWebhook = new Webhook("stackWebhook", WebhookArgs.builder()
            .active(true)
            .displayName("#my-stack-activity-channel")
            .organizationName("my-org")
            .projectName("webhook-examples")
            .stackName("dev")
            .payloadUrl("https://hooks.slack.com/services/...")
            .format("slack")
            .build());

        ctx.export("orgWebhookName", orgWebhook.name());
        ctx.export("stackWebhookName", stackWebhook.name());
    }
}
```

{{% /choosable %}}

## Pulumi Deployment Notification Events

Pulumi Deployments is a fully managed platform for managing infrastructure at scale. With Pulumi Deployments, you can run a Pulumi infrastructure as code action (a preview, update, destroy or refresh) inside Pulumi Cloud. Pulumi provides scalability, observability and security for deployments. Both Slack-formatted and generic JSON webhooks in Pulumi Cloud now send notifications events on Pulumi Deployments statuses: when a deployment is queued, started, succeeds and fails.

![Deploy notifications](deploy_notifications.png)

## Filtering Notification Events

Event filtering allows you to select which events should be delivered to each webhook. You may want to receive
all events, or filter to specific events (only failures, only deployment events, etc.). The following table describes the various event filters available and the context in which they are relevant.

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

## Wrapping up

We hope you and your team can streamline deployment related notifications to where you spend your time. Our webhooks improvements enable ChatOps workflows and more visibility into your infrastructure. As always, please let us know if you have feedback on the feature by opening an issue in the [Pulumi Cloud requests repository](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) or if you have other features you would like to see in Pulumi Cloud.

Happy building! 👷
