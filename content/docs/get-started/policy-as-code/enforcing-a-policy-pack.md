---
title: Enforcing a Policy Pack Across an Organization (Preview)
linktitle: Enforcing a Policy Pack
weight: 2
menu:
  getstarted:
    parent: pac
    identifier: pac-enforcing-a-policy-pack
---
{{% pac-preview %}}

Once you’ve validated the behavior of your policies, an organization administrator can publish them to the Pulumi Console to be enforced across your organization. Any Pulumi client (a developer’s workstation, CI/CD tool, etc) that interacts with a stack via the Pulumi Console will have policy enforcement during the execution of `preview` and `update`. Policy Packs are versioned by the Pulumi Console so that updated policies can be published and applied as ready and also reverted to previous versions as needed.

1. From within the Policy Pack directory, run the following command to publish your pack:

    ```sh
    $ PULUMI_DEBUG_COMMANDS=true pulumi policy publish [org-name]
    ```

    The `[org-name]` is optional. If not specified, the pack will be published to your user account.

    The `<policy-pack-name>` is the name you’d like to see used to reference the pack in the Pulumi Console.

    The output will tell you what version of the Policy Pack you just published. The Pulumi service provides a monotonic version number for Policy Packs.

    ```sh
    $ PULUMI_DEBUG_COMMANDS=true pulumi policy publish myorg
    Obtaining policy metadata from policy plugin
    Compressing policy pack
    Uploading policy pack to Pulumi service
    Publishing policy-pack-typescript to myorg
    Published as version 1
    ```

1. You can apply this Policy Pack to your organization’s default Policy Group by running:

    ```sh
    $ PULUMI_DEBUG_COMMANDS=true pulumi policy apply <org-name>/<policy-pack-name> <version>
    ```

    For example, to apply the Policy Pack created in the previous step:

    ```sh
    $ PULUMI_DEBUG_COMMANDS=true pulumi policy apply pulumi/policy-pack-typescript 1
    ```

    The CLI can only be used to apply the Policy Pack to your default Policy Group. If you would like to add the Policy Pack to a different Policy Group, you can do so via the Pulumi Console.

## Next Steps

Now that you have published your first Policy Pack, you now have all the tools needed to enforce compliance amongst your organization. For more example Policy Packs, you can check out the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs).
