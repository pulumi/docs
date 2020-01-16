---
title: FAQ
meta_desc: A collection of Freduently Asked Questions (FAQ) about the Pulumi CLI and Cloud Services.
menu:
  troubleshooting:
    weight: 2
aliases: ["/docs/reference/faq/"]
---

## Why do resource names have random hex character suffixes?

Pulumi resources have different logical names and physical names. The logical name is how your resource is known to Pulumi, and is part of the auto-assigned resource URN, while the physical name is how your resource is known to your cloud provider. The logical name only needs to be unique within a stack, while the physical name typically needs to be unique within a certain scope (sometimes even globally).

To ensure that as many logical Pulumi resources and stacks can be stood up side-by-side without them conflicting, Pulumi automatically creates each resource's name by combining the logical name with a random suffix appended afterwards. This approach to auto-naming also ensures Pulumi can replace resources with less downtime, by creating the replacement before needing to delete the old resource. In practice, both of these provide significant benefits. This means, however, that your resource's physical name will typically look like `my-bucket-d7c2fa0` instead of `my-bucket`.

You can disable this "auto-naming" on a per-resource basis if this isn't right for you. Doing so lets you have precise physical names without random suffixes, but also means you lose the two benefits named above. To learn more, see [the product documentation about auto-naming]({{< relref "programming-model" >}}#autonaming).

## How can I add support for my favorite cloud?

To enable a new cloud, you need to create a Pulumi Resource Provider.  This requires a gRPC interface, and can be implemented directly; see [https://github.com/pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes) for an example of this.

If there is an existing Terraform Resource Provider for the target, you can also use Terraform Bridge;  see [https://github.com/pulumi/pulumi-terraform/blob/master/README.md](https://github.com/pulumi/pulumi-terraform/blob/master/README.md) for a description of the overall structure and process of adding a new provider using the bridge and [https://github.com/pulumi/pulumi-aws/blob/master/resources.go](https://github.com/pulumi/pulumi-aws/blob/master/resources.go) for a specific example.

## How can I add support for my favorite language?

Supported languages run out of process and communicate over gRPC with the Pulumi engine and resource providers.  The protocol definitions can be found at [https://github.com/pulumi/pulumi/tree/master/sdk/proto](https://github.com/pulumi/pulumi/tree/master/sdk/proto) along with the language providers themselves.  You can look at how we added support for Go at [https://github.com/pulumi/pulumi/pull/1456](https://github.com/pulumi/pulumi/pull/1456), which should help with scoping.

## Does Pulumi support automatic rollback in the event of an error or failure?

No, Pulumi does not automatically rollback changes made during an update if an error or failure occurs. In the event that an error or failure occurs, Pulumi will complete any pending operations
currently in progress and then exit and report the error or failure.

To accomplish a _manual_ rollback after a failed deployment, revert the code and configuration changes of the failed deployment and run `pulumi up` to update your infrastructure to its previous "good" state. This is also known as a _roll forward_.

There is an issue related to the idea of automatic rollbacks on GitHub at <https://github.com/pulumi/pulumi/issues/96> if you would like to add to the discussion.

## How does Pulumi manage secrets?

When you set a configuration value, you may pass `--secret` to `pulumi config set` which causes the value to be encrypted so it can be safely persisted in `Pulumi.<stack-name>.yaml`. For every stack, pulumi.com manages a unique encryption key, which it uses to encrypt secrets for that stack. Because a different key is used for each stack, encrypting the same value across two different stacks will lead to different encrypted strings being stored in the `Pulumi.<stack-name>.yaml` files. This also means that you can not copy an encrypted value from one file to another using a text editor. Instead, you must use `pulumi config set`.

When you run a preview, update or destroy, pulumi decrypts this data. It is plain text during the execution of your deployment, and any part of your Pulumi program may access it using the Pulumi config object. To learn more, see [Configuration]({{< relref "/docs/intro/concepts/config" >}}).

## Are my secrets ever visible?

As noted above, Pulumi provides primitives so you can enforce your secrets are stored in a secure manner in the CLI UI, State file and Pulumi Web Console. During an update, your secrets will be unencrypted in memory and visible to your Pulumi program. It is your responsibility to ensure that you do not persist them outside of Pulumi without securing them. To learn more, see [Secrets]({{< relref "/docs/intro/concepts/programming-model#secrets" >}}).

## How do I create a stack inside an Organization instead of my User account?

To create a stack in a different Pulumi organization, simply prefix the stack's
name with the organization's login. For example:

```sh
$ pulumi stack init acme-corp/widget-server
```

## How does Pulumi depend on pulumi.com?

Pulumi uses pulumi.com to store information about the current state of your application, which is used during updates, previews and destroys as the source of truth for the current state of your cloud resources. We refer to this state as the "checkpoint" for your application. In addition, pulumi.com ensures that for a given stack, only a single update is running at once (so, if you and someone else are collaborating on a stack together, pulumi.com ensures that you both don't update the same stack at the same time.) Once your stack has been deployed, it has no dependency on pulumi.com. To learn more about how the Pulumi engine uses pulumi.com, see [How Pulumi Works]({{< relref "/docs/intro/concepts/how-pulumi-works" >}}).

## What happens if pulumi.com is down?

Any infrastructure that you’ve deployed using Pulumi will continue working and can be managed with your cloud provider’s console or CLI, that is, pulumi.com should not affect any runtime behavior of your application.

If pulumi.com is down, you'll be unable to preview, update or destroy a stack using Pulumi.  Some commands, like `pulumi logs`, use pulumi.com to find the correct log stream, so will not function until pulumi.com recovers; however, your cloud provider will still produce logs that you can use for diagnostics and you can view these via your cloud console or CLI.

## Can I use Pulumi without depending on pulumi.com?

We think that using the Pulumi service and the Pulumi tool together provides the right combination of usability, safety, and security for most users. However, for users with especially unique requirements, it is possible to use the Pulumi tool apart from the service.

When you use Pulumi without pulumi.com, the checkpoint for your stack is stored locally. If that file is lost or outdated, Pulumi can no longer operate on your stack. To collaborate with others on your stack, you must host this file yourself and protect against conflicting updates to it. If you use your own checkpoint file, the pulumi.com features, such as the deployment history and resource view, will not be available.

To use Pulumi without pulumi.com, log in using `pulumi login --local`. For more information, read more at [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).

## How can I go back to using the Pulumi service?

Just run `pulumi login` and you’ll be back to using pulumi.com. If you have any existing stacks, see the instructions below for migrating them to pulumi.com.

## I've been using the local endpoint, can I migrate to Pulumi.com?

Yes, you can! The Pulumi CLI allows you to export and import checkpoints so you can do the following.  Suppose the stack “my-app-production” has been managed with a local checkpoint file, and you want to migrate it to pulumi.com. If you are currently logged in to the local endpoint, run the following commands:

```sh
$ pulumi stack select my-app-production # switch to the stack we want to export
$ pulumi stack export --file my-app-production.checkpoint.json # export the stack's checkpoint to a local file
$ pulumi login
$ pulumi stack init my-app-production # create a new stack with the same name on pulumi.com
$ pulumi stack import --file my-app-production.checkpoint.json # import the new existing checkpoint into pulumi.com
```

In addition, if you have any encrypted configuration in your stack, you'll need to re-run `pulumi config set --secret <key> <value>` because pulumi.com uses a different key to encrypt your secrets than the local endpoint does.
