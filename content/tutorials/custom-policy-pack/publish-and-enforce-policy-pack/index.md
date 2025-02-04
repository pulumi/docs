---
title_tag: Publish and Enforce a Custom Policy Pack | Pulumi Crossguard
title: Publish and Enforce a Custom Policy Pack
layout: topic
description: Publish and enforce a custom policy pack using Pulumi Crossguard.
meta_desc: Publish and enforce a custom policy pack using Pulumi Crossguard.
weight: 3
estimated_time: 5
---

{{% notes type="info" %}}
Server-side enforcement of policy packs across an organization is only available in **Pulumi Business Critical**. See [pricing](/pricing/) for more details.
{{% /notes %}}

Now that we've validated the behavior of our custom policy pack, publishing it to Pulumi Cloud will allow the policies to be enforced across your organization. Any time you run `pulumi preview` or `pulumi up` on a stack, Pulumi Cloud will ship the policy to the client to enable policy enforcement. Policy Packs are versioned by the Pulumi Cloud so that updated policies can be published and applied incrementally, and also reverted to previous versions as needed.

### Publish the policy pack

Navigate back to the policy pack directory, and run the following command to publish your policy pack:

```sh
$ pulumi policy publish <org-name>
```

The output will tell you what version of the policy pack you just published.

```
Obtaining policy metadata from policy plugin
Compressing policy pack
Uploading policy pack to Pulumi Cloud
Publishing custom-policy-pack to myorg
Published as version 1.0.0
```

{{% notes type="info" %}}
**Policy Versions**: Pulumi Cloud tracks published policy packs by *version*. When a policy pack is published, it will automatically receive a monotonically-increasing version number by Pulumi Cloud. The policy pack version can be specified in the `package.json` file for TypeScript/JavaScript (Node.js) packs and in the `PulumiPolicy.yaml` file for Python packs. Published policy packs are immutable, meaning that a version number can only be published to one time. Once published, the version can never be used by that policy pack again.
{{% /notes %}}

### Enforce the policy pack

You can enable the policy pack organization-wide by running:

```sh
$ pulumi policy enable myorg/custom-policy-pack latest
```

The `latest` parameter indicates that the most recent version of the policy should be enabled. You could use a version number instead, to enable a previous version.

{{% notes type="info" %}}
**Policy Groups**: Pulumi Crossguard also has a concept of *[policy groups](/docs/iac/using-pulumi/crossguard/core-concepts/#policy-groups)*, which allow you to apply certain policies only to certain stacks within the group. The `pulumi policy enable` command, by default, turns on a published policy pack to your default policy group, which applies it to all stacks. If you would like to add the policy pack to a different policy group, you can use the `--policy-group` flag. Read more about how to manage groups with `[pulumi policy group](/docs/iac/cli/commands/pulumi_policy_group/)` commands in the [Crossguard docs](/docs/iac/using-pulumi/crossguard/core-concepts/#policy-groups).
{{% /notes %}}

## Next Steps

Congratulations! Now that you have published your first custom policy pack, all the pieces are in place to enforce compliance across your organization. For more example policy packs, you can check out the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). You can also find more documentation in the [CrossGuard guide](/docs/using-pulumi/crossguard/).

{{< tutorials/stepper >}}
