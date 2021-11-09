---
title: FAQ
meta_desc: A collection of Frequently Asked Questions (FAQ) about Pulumi.
menu:
  troubleshooting:
    weight: 2
aliases: ["/docs/reference/faq/"]
---

## Automatic Rollbacks

### Does Pulumi support automatic rollback in the event of an error or failure?

No, Pulumi does not automatically rollback changes made during an update if an error or failure occurs. In the event that an error or failure occurs, Pulumi will complete any pending operations
currently in progress and then exit and report the error or failure.

To accomplish a _manual_ rollback after a failed deployment, revert the code and configuration changes of the failed deployment and run `pulumi up` to update your infrastructure to its previous state.

## Organizations

### How do I create a stack inside an Organization instead of my User account?

To create a stack in a different Pulumi organization, prefix the stack's
name with the organization name. For example:

```sh
$ pulumi stack init acme-corp/widget-server
```

## Pulumi Service

### How does Pulumi store state?

Pulumi needs to store the result of operations. On creation of a Pulumi resource, Pulumi makes a call to the cloud provider's API and then it stores the result of that API call. The place where Pulumi stores that result is called the "state" or "checkpoint". The state can be stored using the Pulumi Service or in files on Amazon S3, Azure Blob Storage, Google Cloud Storage Buckets, or as a file on your local machine that you manage yourself.

### How does Pulumi depend on the Pulumi Service?

Pulumi uses the Pulumi Service to store information about the current state of your application, which is used during updates, previews, and destroys as the source of truth for the current state of your cloud resources. We refer to this state as the "checkpoint" for your application. In addition, the Pulumi Service ensures that for a given stack, only a single update is running at once (so, if you and someone else are collaborating on a stack together, it ensures that you both don't update the same stack at the same time.) Once your stack has been deployed, it has no dependency on the Pulumi Service. To learn more about how the Pulumi engine uses pulumi.com, see [How Pulumi Works]({{< relref "/docs/intro/concepts/how-pulumi-works" >}}).

### What happens if app.pulumi.com is down?

Any infrastructure that you’ve deployed using Pulumi will continue working and can be managed with your cloud provider’s console or CLI. app.pulumi.com does not affect any runtime behavior of your application.

If app.pulumi.com is down, you'll be unable to preview, update, or destroy a stack using Pulumi. Some commands, like `pulumi logs`, use app.pulumi.com to find the correct log stream so will not function until pulumi.com recovers; however, your cloud provider will still produce logs that you can use for diagnostics, which you can view via your cloud console or CLI.

### Can I use Pulumi without depending on the Pulumi Service?

Using the Pulumi service with Pulumi provide a good combination of usability, safety, and security. However, for users with especially unique requirements, it is possible to use Pulumi apart from the Pulumi Service.

When you use Pulumi without the Pulumi Service, the checkpoint for your stack is stored locally or in your own external self-managed state storage. If that file is lost or outdated, Pulumi can no longer operate on your stack. To collaborate with others on your stack, you must host this file yourself and protect against conflicting updates to it. If you use your own checkpoint file, the Pulumi Service features, such as the deployment history and resource view, will not be available.

To use Pulumi without the Pulumi Service, log in using `pulumi login --local` or by logging in to an alternative backend. For more information, read more at [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).

### How can I go back to using the Pulumi Service?

Run `pulumi login`, and you’ll be back to using the Pulumi Service. You will need to migrate any existing stacks to the Service.

### How to migrate from a self-managed backend to the Pulumi Service?

The Pulumi CLI allows you to export and import checkpoints so you can do the following. Suppose the stack “my-app-production” has been managed with a local checkpoint file, and you want to migrate it to pulumi.com. If you are currently logged in to the local endpoint, run the following commands:

```sh
$ pulumi stack select my-app-production # switch to the stack we want to export
$ pulumi stack export --file my-app-production.checkpoint.json # export the stack's checkpoint to a local file
$ pulumi logout
$ pulumi login
$ pulumi stack init my-app-production # create a new stack with the same name on pulumi.com
$ pulumi stack import --file my-app-production.checkpoint.json # import the new existing checkpoint into pulumi.com
```

In addition, if you have any encrypted configuration in your stack, you'll need to re-run `pulumi config set --secret <key> <value>` because pulumi.com uses a different key to encrypt your secrets than the local endpoint does.

## Resource names

### Why do resource names have random hex character suffixes?

Pulumi resources have different logical names and physical names. The logical name is how your resource is known to Pulumi, and is part of the auto-assigned resource URN, while the physical name is how your resource is known to your cloud provider. The logical name only needs to be unique within a stack, while the physical name typically needs to be unique within a certain scope (sometimes even globally).

To ensure that as many logical Pulumi resources and stacks can be stood up side-by-side without them conflicting, Pulumi automatically creates each resource's name by combining the logical name with a random suffix appended afterwards. This approach to auto-naming also ensures Pulumi can replace resources with less downtime, by creating the replacement before needing to delete the old resource. In practice, both of these provide significant benefits. This means, however, that your resource's physical name will typically look like `my-bucket-d7c2fa0` instead of `my-bucket`.

You can disable this [auto-naming]({{< relref "/docs/intro/concepts/resources#autonaming" >}}) on a per-resource basis if this isn't right for you. Doing so lets you have precise physical names without random suffixes, but also means you lose the two benefits named above.

## Secrets

### Are my secrets ever visible?

Pulumi provides primitives so you can enforce your [secrets]({{< relref "/docs/intro/concepts/secrets#secrets" >}}) are stored in a secure manner in the CLI, state file and Pulumi Console. During an update, your secrets will be decrypted in memory and visible to your Pulumi program. It is your responsibility to ensure that you do not persist them outside of Pulumi without securing them.

### How does Pulumi manage secrets?

When you set a [configuration]({{< relref "/docs/intro/concepts/config" >}}) value, you may pass `--secret` to `pulumi config set` which causes the value to be encrypted so it can be safely persisted in `Pulumi.<stack-name>.yaml`. For every stack the Pulumi service manages a unique encryption key, which it uses to encrypt secrets for that stack (and this is configurable to use your own custom secrets provider). Because a different key is used for each stack, encrypting the same value across two different stacks will lead to different encrypted strings being stored in the `Pulumi.<stack-name>.yaml` files. This also means that you cannot copy an encrypted value from one file to another using a text editor. Instead, you must use `pulumi config set`.

When you run a preview, update or destroy, pulumi decrypts this data. It is plain text during the execution of your deployment, and any part of your Pulumi program may access it using the Pulumi config object.

## Supported clouds and languages

### How can I add support for my favorite cloud?

To enable a new cloud, you need to create a Pulumi Resource Provider. This provider requires a [gRPC](https://grpc.io/) interface and can be implemented directly; explore the [Pulumi Resource Provider Boilerplate](https://github.com/pulumi/pulumi-provider-boilerplate) to get started and [https://github.com/pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes) for a complete example of building out a provider.

If there is an existing Terraform Resource Provider for the target, you can also use [Terraform Bridge](https://github.com/pulumi/pulumi-terraform-bridge/blob/master/README.md) and [pulumi-aws resources.go](https://github.com/pulumi/pulumi-aws/blob/master/provider/resources.go) for a specific example.

### How can I add support for my favorite language?

Supported languages run out of process and communicate over gRPC with the Pulumi engine and resource providers. Check out the [protocol definitions](https://github.com/pulumi/pulumi/tree/master/sdk/proto) along with the language providers themselves. You can explore how we added [support for Go](https://github.com/pulumi/pulumi/pull/1456), which should help with scoping. There is also a summary of the core work items needed as part of adding support for a typical new language on the [New Language wiki page](https://github.com/pulumi/pulumi/wiki/New-Language-Bring-up).

## Understanding Pulumi

### Does Pulumi use Terraform?

Pulumi does not use the Terraform engine in any way. However, some Pulumi providers use the open-source [Terraform schemas](https://www.terraform.io/docs/extend/schemas/index.html) in order to know what resources and parameters are available, and to determine the return and response attributes. On the other hand, [Pulumi native providers](https://www.pulumi.com/blog/pulumiup-native-providers/) are mapped directly to the cloud provider APIs and do not use Terraform schemas.

### Is Pulumi imperative or declarative?

Pulumi is a declarative tool that uses imperative languages to define your end state. The language is used for authoring your program. It’s not used for talking to the cloud provider API.

### How will Pulumi make me more productive?

Pulumi uses strongly typed languages with programming languages that support [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) and the [Language Server Protocol](https://en.wikipedia.org/wiki/Language_Server_Protocol) which means when you are defining Pulumi programs, you rarely need to leave your IDE.
