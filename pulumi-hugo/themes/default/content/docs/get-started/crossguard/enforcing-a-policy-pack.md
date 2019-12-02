---
title: Enforcing a Policy Pack Across an Organization
linktitle: Enforcing a Policy Pack
weight: 2
menu:
  getstarted:
    parent: pac
aliases: ["/docs/get-started/policy-as-code/enforcing-a-policy-pack/"]
---
{{% crossguard-preview %}}

Once you’ve validated the behavior of your policies, an organization administrator can publish them to the Pulumi Console to be enforced across your organization. Any Pulumi client (a developer’s workstation, CI/CD tool, etc) that interacts with a stack via the Pulumi Console will have policy enforcement during the execution of `preview` and `update`. Policy Packs are versioned by the Pulumi Console so that updated policies can be published and applied as ready and also reverted to previous versions as needed.

1. From within the Policy Pack directory, run the following command to publish your pack:

    {{< oschoose >}}

    <div class="os-prologue-macos"></div>
    <div class="mt-4">
{{% md %}}
```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy publish [org-name]
```
{{% /md %}}
    </div>

    <div class="os-prologue-linux"></div>
    <div class="mt-4">
{{% md %}}
```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy publish [org-name]
```
{{% /md %}}
    </div>

    <div class="os-prologue-windows"></div>
    <div class="mt-4">
{{% md %}}
**Windows cmd.exe**

```bat
set PULUMI_EXPERIMENTAL=true
pulumi policy publish [org-name]
```

**Windows PowerShell**

```powershell
$env:PULUMI_EXPERIMENTAL = 'true'
pulumi policy publish [org-name]
```
{{% /md %}}
    </div>

    The `[org-name]` is optional. If not specified, the pack will be published to your user account.

    The output will tell you what version of the Policy Pack you just published. The Pulumi service provides a monotonic version number for Policy Packs.

    ```
    Obtaining policy metadata from policy plugin
    Compressing policy pack
    Uploading policy pack to Pulumi service
    Publishing policy-pack-typescript to myorg
    Published as version 1
    ```

1. You can apply this Policy Pack to your organization’s default Policy Group by running:

    {{< oschoose >}}

    <div class="os-prologue-macos"></div>
    <div class="mt-4">
{{% md %}}
```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy apply <org-name>/<policy-pack-name> <version>
```
{{% /md %}}
    </div>

    <div class="os-prologue-linux"></div>
    <div class="mt-4">
{{% md %}}
```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy apply <org-name>/<policy-pack-name> <version>
```
{{% /md %}}
    </div>

    <div class="os-prologue-windows"></div>
    <div class="mt-4">
{{% md %}}
**Windows cmd.exe**

```bat
set PULUMI_EXPERIMENTAL=true
pulumi policy apply <org-name>/<policy-pack-name> <version>
```

**Windows PowerShell**

```powershell
$env:PULUMI_EXPERIMENTAL = 'true'
pulumi policy apply <org-name>/<policy-pack-name> <version>
```
{{% /md %}}
    </div>

    For example, to apply the Policy Pack created in the previous step:

    {{< oschoose >}}

    <div class="os-prologue-macos"></div>
    <div class="mt-4">
{{% md %}}
```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy apply pulumi/policy-pack-typescript 1
```
{{% /md %}}
    </div>

    <div class="os-prologue-linux"></div>
    <div class="mt-4">
{{% md %}}
```sh
$ PULUMI_EXPERIMENTAL=true pulumi policy apply pulumi/policy-pack-typescript 1
```
{{% /md %}}
    </div>

    <div class="os-prologue-windows"></div>
    <div class="mt-4">
{{% md %}}
**Windows cmd.exe**

```bat
set PULUMI_EXPERIMENTAL=true
pulumi policy apply pulumi/policy-pack-typescript 1
```

**Windows PowerShell**

```powershell
$env:PULUMI_EXPERIMENTAL = 'true'
pulumi policy apply pulumi/policy-pack-typescript 1
```
{{% /md %}}
    </div>

    The CLI can only be used to apply the Policy Pack to your default Policy Group. If you would like to add the Policy Pack to a different Policy Group, you can do so via the Pulumi Console.

## Next Steps

Now that you have published your first Policy Pack, you now have all the tools needed to enforce compliance amongst your organization. For more example Policy Packs, you can check out the [examples repo](https://github.com/pulumi/examples/tree/master/policy-packs). You can also find more documentation in the [CrossGuard guide]({{< relref "/docs/guides/crossguard" >}}).
