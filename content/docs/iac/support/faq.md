---
title_tag: Pulumi IaC FAQ
meta_desc: A collection of Frequently Asked Questions (FAQ) about Pulumi IaC.
title: FAQ
h1: Pulumi IaC FAQ
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: FAQ
        parent: iac-support
        weight: 1
        identifier: iac-support-faq
    support:
        weight: 2
        identifier: all-faqs

aliases:
    - /docs/reference/faq/
    - /docs/troubleshooting/faq/
    - /docs/support/faq/
---

## Automatic Rollbacks

### Does Pulumi support automatic rollback in the event of an error or failure?

No, Pulumi does not automatically rollback changes made during an update if an error or failure occurs. In the event that an error or failure occurs, Pulumi will complete any pending operations
currently in progress and then exit and report the error or failure.

To accomplish a _manual_ rollback after a failed deployment, revert the code and configuration changes of the failed deployment and run `pulumi up` to update your infrastructure to its previous state.

## Resource names

### Why do resource names have random hex character suffixes?

Pulumi resources have different logical names and physical names. The logical name is how your resource is known to Pulumi, and is part of the auto-assigned resource URN, while the physical name is how your resource is known to your cloud provider. The logical name only needs to be unique within a stack, while the physical name typically needs to be unique within a certain scope (sometimes even globally).

To ensure that as many logical Pulumi resources and stacks can be stood up side-by-side without them conflicting, Pulumi automatically creates each resource's name by combining the logical name with a random suffix appended afterwards. This approach to auto-naming also ensures Pulumi can replace resources with less downtime, by creating the replacement before needing to delete the old resource. In practice, both of these provide significant benefits. This means, however, that your resource's physical name will typically look like `my-bucket-d7c2fa0` instead of `my-bucket`.

You can disable this [auto-naming](/docs/concepts/resources/names/#autonaming) on a per-resource basis if this isn't right for you. Doing so lets you have precise physical names without random suffixes, but also means you lose the two benefits named above.

You can also use project or stack configuration to customize or disable auto-naming globally, per provider, or per resource type. See [Auto-naming Configuration](/docs/concepts/resources/names/#autonaming-configuration) for more information.

## Secrets

### Are my secrets ever visible?

Pulumi provides primitives so you can enforce your [secrets](/docs/concepts/secrets#secrets) are stored in a secure manner in the CLI, state file and Pulumi Cloud. During an update, your secrets will be decrypted in memory and visible to your Pulumi program. It is your responsibility to ensure that you do not persist them outside of Pulumi without securing them.

### How does Pulumi manage secrets?

When you set a [configuration](/docs/concepts/config/) value, you may pass `--secret` to `pulumi config set` which causes the value to be encrypted so it can be safely persisted in `Pulumi.<stack-name>.yaml`. For every stack Pulumi Cloud manages a unique encryption key, which it uses to encrypt secrets for that stack (and this is configurable to use your own custom secrets provider). Because a different key is used for each stack, encrypting the same value across two different stacks will lead to different encrypted strings being stored in the `Pulumi.<stack-name>.yaml` files. This also means that you cannot copy an encrypted value from one file to another using a text editor. Instead, you must use `pulumi config set`.

When you run a preview, update or destroy, pulumi decrypts this data. It is plain text during the execution of your deployment, and any part of your Pulumi program may access it using the Pulumi config object.

## Supported clouds and languages

### How can I add support for my favorite cloud?

To enable a new cloud, you need to create a Pulumi Resource Provider. This provider requires a [gRPC](https://grpc.io/) interface and can be implemented directly; explore the [Pulumi Resource Provider Boilerplate](https://github.com/pulumi/pulumi-provider-boilerplate) to get started and [https://github.com/pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes) for a complete example of building out a provider.

If there is an existing Terraform Resource Provider for the target, you can also use [Terraform Bridge](https://github.com/pulumi/pulumi-terraform-bridge/blob/master/README.md) and [pulumi-aws resources.go](https://github.com/pulumi/pulumi-aws/blob/master/provider/resources.go) for a specific example.

### How can I add support for my favorite language?

Supported languages run out of process and communicate over gRPC with the Pulumi engine and resource providers. Check out the [protocol definitions](https://github.com/pulumi/pulumi/tree/master/sdk/proto) along with the language providers themselves. You can explore how we added [support for Go](https://github.com/pulumi/pulumi/pull/1456), which should help with scoping. There is also a summary of the core work items needed as part of adding support for a typical new language on the [New Language wiki page](https://github.com/pulumi/pulumi/wiki/New-Language-Bring-up).

## Understanding Pulumi

### Does Pulumi use Terraform?

Pulumi does not use the Terraform engine in any way. However, some Pulumi providers use the open-source [Terraform schemas](https://www.terraform.io/docs/extend/schemas/index.html) in order to know what resources and parameters are available, and to determine the return and response attributes. On the other hand, [Pulumi native providers](/blog/pulumiup-native-providers/) are mapped directly to the cloud provider APIs and do not use Terraform schemas.

### Is Pulumi imperative or declarative?

Pulumi is a declarative tool that uses imperative languages to define your end state. The language is used for authoring your program. It’s not used for talking to the cloud provider API.

### How will Pulumi make me more productive?

Pulumi uses strongly typed languages with programming languages that support [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) and the [Language Server Protocol](https://en.wikipedia.org/wiki/Language_Server_Protocol) which means when you are defining Pulumi programs, you rarely need to leave your IDE.

## More FAQ

- [Pulumi ESC FAQ](/docs/esc/faq/)
- [Pulumi Cloud FAQ](/docs/pulumi-cloud/faq/)
- [Pulumi Cloud SCIM FAQ](/docs/pulumi-cloud/access-management/scim/faq/)
- [Kubernetes guides FAQ](/docs/clouds/kubernetes/guides/faq/)
- [Pulumi CrossGuard FAQ](/docs/using-pulumi/crossguard/faq/)
