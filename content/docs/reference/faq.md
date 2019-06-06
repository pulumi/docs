---
title: "FAQ"
aliases: ["faq.html"]
menu:
  reference:
    weight: 10
---

## How can I add support for my favorite cloud?

To enable a new cloud, you need to create a Pulumi Resource Provider.  This requires a gRPC interface, and can be implemented directly; see see https://github.com/pulumi/pulumi-kubernetes for an example of this.  

If there is an existing Terraform Resource Provider for the target, you can also use Terraform Bridge;  see https://github.com/pulumi/pulumi-terraform/blob/master/README.md for a description of the overall structure and process of adding a new provider using the bridge and https://github.com/pulumi/pulumi-aws/blob/master/resources.go for a specific example.

## How can I add support for my favorite language?

Supported languages run out of process and communicate over gRPC with the Pulumi engine and resource providers.  The protocol definitions can be found at https://github.com/pulumi/pulumi/tree/master/sdk/proto along with the language providers themselves.  You can look at how we added support for Go at https://github.com/pulumi/pulumi/pull/1456, which should help with scoping.

## How does Pulumi manage secrets?

When you set a configuration value, you may pass `--secret` to `pulumi config set` which causes the value to be encrypted so it can be safely persisted in `Pulumi.<stack-name>.yaml`. For every stack, pulumi.com manages a unique encryption key, which it uses to encrypt secrets for that stack. Because a different key is used for each stack, encrypting the same value across two different stacks will lead to different encrypted strings being stored in the `Pulumi.<stack-name>.yaml` files. This also means that you can not copy an encrypted value from one file to another using a text editor. Instead, you must use `pulumi config set`.

When you run a preview, update or destroy, pulumi decrypts this data. It is plain text during the execution of your deployment, and any part of your Pulumi program may access it using the Pulumi config object. To learn more, see [Configuration]({{< relref "config.md" >}}).

## Are my secrets ever visible?

Depending on how you use your secrets, they may be visible in parts of your application at deployment time. For example, if you capture the value of a secret with a Lambda, which backs some serverless function, the secret would appear in the program text. Since the checkpoint retains information about all inputs to resources it created, they may also be visible in parts of the checkpoint. You can use `pulumi stack export` to inspect the checkpoint of the current stack and see exactly what data is present.

## If I don't want my secret to end up in the checkpoint, what can I do?

We are actively looking for ways to improve pulumi's secret management, see [pulumi/pulumi#1547](https://github.com/pulumi/pulumi/issues/1547) and [pulumi/pulumi#397](https://github.com/pulumi/pulumi/issues/397). In the meantime we recommend you manually use some third party key management (e.g. Amazon KMS). 

## How do I create a stack inside an Organization instead of my User account?

To create a stack in a different Pulumi organization, simply prefix the stack's
name with the organization's login. For example:

```sh
$ pulumi stack init acme-corp/widget-server
```

## How does Pulumi depend on pulumi.com?

Pulumi uses pulumi.com to store information about the current state of your application, which is used during updates, previews and destroys as the source of truth for the current state of your cloud resources. We refer to this state as the "checkpoint" for your application. In addition, pulumi.com ensures that for a given stack, only a single update is running at once (so, if you and someone else are collaborating on a stack together, pulumi.com ensures that you both don't update the same stack at the same time.) Once your stack has been deployed, it has no dependency on pulumi.com. To learn more about how the Pulumi engine uses pulumi.com, see [How Pulumi Works]({{< relref "how.md" >}}).

## What happens if pulumi.com is down?

Any infrastructure that you’ve deployed using Pulumi will continue working and can be managed with your cloud provider’s console or CLI, that is, pulumi.com should not affect any runtime behavior of your application.  

If pulumi.com is down, you'll be unable to preview, update or destroy a stack using Pulumi.  Some commands, like `pulumi logs`, use pulumi.com to find the correct log stream, so will not function until pulumi.com recovers; however, your cloud provider will still produce logs that you can use for diagnostics and you can view these via your cloud console or CLI. 

## Can I use Pulumi without depending on pulumi.com?

We think that using the Pulumi service and the Pulumi tool together provides the right combination of usability, safety, and security for most users. However, for users with especially unique requirements, it is possible to use the Pulumi tool apart from the service.

When you use Pulumi without pulumi.com, the checkpoint for your stack is stored locally. If that file is lost or outdated, Pulumi can no longer operate on your stack. To collaborate with others on your stack, you must host this file yourself and protect against conflicting updates to it. If you use your own checkpoint file, the pulumi.com features, such as the deployment history and resource view, will not be available.

To use Pulumi without pulumi.com, log in using `pulumi login --local`. For more information, read more at [State and Backends]({{< relref "state.md" >}}).

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
