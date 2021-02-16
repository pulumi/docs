---
title: Enforcing a Policy Pack Across an Organization
meta_desc: This page provides an overview of how to enforce a Policy Pack across an organization.
linktitle: Enforcing a Policy Pack
weight: 2
menu:
  getstarted:
    parent: pac
aliases: ["/docs/get-started/policy-as-code/enforcing-a-policy-pack/"]
---

Once you’ve validated the behavior of your policies, an organization administrator can publish them to the Pulumi Console to be enforced across your organization. Any Pulumi client (a developer’s workstation, CI/CD tool, etc) that interacts with a stack via the Pulumi Console will have policy enforcement during the execution of `preview` and `update`. Policy Packs are versioned by the Pulumi Console so that updated policies can be published and applied as ready and also reverted to previous versions as needed.

1. From within the Policy Pack directory, run the following command to publish your pack:

    ```sh
    $ pulumi policy publish <org-name>
    ```

    The output will tell you what version of the Policy Pack you just published. The Pulumi service provides a monotonic version number for Policy Packs.

    ```
    Obtaining policy metadata from policy plugin
    Compressing policy pack
    Uploading policy pack to Pulumi service
    Publishing my-policy-pack to myorg
    Published as version 1.0.0
    ```

    The Policy Pack version is specified in the `package.json` file for TypeScript/JavaScript (Node.js) packs and in the `PulumiPolicy.yaml` file for Python packs. A version can only be used one time and once published the version can never be used by that Policy Pack again.

<!-- markdownlint-disable ul -->
1. You can enable this Policy Pack to your organization’s default Policy Group by running:

    ```sh
    $ pulumi policy enable <org-name>/<policy-pack-name> <latest|version>
    ```

    For example, to enable the Policy Pack created in the previous step:

    ```sh
    $ pulumi policy enable myorg/my-policy-pack latest
    ```

    The CLI by default enables the Policy Pack to your default Policy Group. If you would like to add the Policy Pack to a different Policy Group, you can use the `--policy-group` flag.

## Next Steps

Now that you have published your first Policy Pack, you now have all the tools needed to enforce compliance amongst your organization. For more example Policy Packs, you can check out the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). You can also find more documentation in the [CrossGuard guide]({{< relref "/docs/guides/crossguard" >}}).
