---
title_tag: Pulumi IaC FAQ
meta_desc: A collection of Frequently Asked Questions (FAQ) about Pulumi IaC.
title: Infrastructure FAQ
h1: Infrastructure as Code FAQ
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        parent: support-faq
        name: Infrastructure FAQ
        weight: 1
        identifier: support-faq-infrastructure
aliases:
    - /docs/support/faq/infrastructure/
    - /docs/reference/faq/
    - /docs/troubleshooting/faq/
    - /docs/support/faq/
    - /docs/iac/support/faq/
    - /docs/iac/support/version-support/
    - /docs/iac/faq/
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

## Understanding Pulumi

### Does Pulumi use Terraform?

Pulumi does not use the Terraform engine in any way. However, some Pulumi providers use the open-source [Terraform schemas](https://www.terraform.io/docs/extend/schemas/index.html) in order to know what resources and parameters are available, and to determine the return and response attributes. On the other hand, [Pulumi native providers](/blog/pulumiup-native-providers/) are mapped directly to the cloud provider APIs and do not use Terraform schemas.

### Is Pulumi imperative or declarative?

Pulumi is a declarative tool that uses imperative languages to define your end state. The language is used for authoring your program. It’s not used for talking to the cloud provider API.

### How will Pulumi make me more productive?

Pulumi uses strongly typed languages with programming languages that support [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) and the [Language Server Protocol](https://en.wikipedia.org/wiki/Language_Server_Protocol) which means when you are defining Pulumi programs, you rarely need to leave your IDE.

## Provider Version Support

### What is Pulumi's policy on provider version support?

Pulumi focuses on actively supporting the latest released version of the providers we maintain.
While we do not formally designate older versions for long term support, we are committed to helping our users succeed and continuously improve our providers based on community feedback and contributions. We encourage users to update to the latest versions to benefit from the most recent features, bug fixes, and security enhancements. You can find the current version for all providers maintained by Pulumi in the [Pulumi Registry](https://www.pulumi.com/registry/).

### What are the best practices for maintaining provider versions?

**When a major version is released, that is a signal to begin planning a provider version update.** Major versions typically include significant changes such as deprecations, new resources and new functionality, which may require some additional migration steps. Planning ahead allows teams to assess the impact of these changes, allocate resources for migration, and test compatibility thoroughly, minimizing disruption to existing infrastructure.

**At least quarterly, consider updating to the latest minor version on the current major, and minimally review provider release notes.** Minor versions typically include new resources and features, as well as performance improvements, and bug fixes without introducing breaking changes. Regular updates ensure access to these benefits and prevent falling too far behind, making future updates easier. The release notes for each provider release summarize the new capabilities or fixes so you can identify changes relevant to your usage.

**Always allow patch updates on the current minor, for example, using the tilde operator in npm: \~1.2.3**.  Patch versions are primarily for bug fixes and security updates and are designed to be fully backward compatible. Automatically applying these updates ensures that known vulnerabilities are addressed and critical bugs are resolved without requiring manual intervention, improving the stability and security of your deployments.

**Never be 2 major versions behind, as it is inadvisable to jump a major version due to the number of potential breaking changes across the major versions.** Major versions typically include significant changes which may require some additional migration steps. Each major version of the provider includes migration logic to smooth the upgrade from the immediately previous major version, but these migrations do not always work across multiple major versions. Being two or more major versions behind can accumulate a significant number of changes and may require a multi-step upgrade, making the upgrade process more complex, time-consuming, and prone to errors.

## More FAQ

- [Pulumi ESC FAQ](/docs/support/faq/secrets-config/)
- [Pulumi Cloud FAQ](/docs/support/pulumi-cloud-faq/)
- [Pulumi Cloud SCIM FAQ](/docs/administration/access-identity/scim/faq/)
- [Pulumi Policies FAQ](/docs/support/faq/policies)
