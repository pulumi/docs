
---
title: "PolicyVM"
block_external_search_index: true
---



Manages an Azure Backup VM Backup Policy.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

const exampleResourceGroup = new azure.core.ResourceGroup("example", {
    location: "West US",
});
const exampleVault = new azure.recoveryservices.Vault("example", {
    location: exampleResourceGroup.location,
    resourceGroupName: exampleResourceGroup.name,
    sku: "Standard",
});
const examplePolicyVM = new azure.backup.PolicyVM("example", {
    backup: {
        frequency: "Daily",
        time: "23:00",
    },
    recoveryVaultName: exampleVault.name,
    resourceGroupName: exampleResourceGroup.name,
    retentionDaily: {
        count: 10,
    },
    retentionMonthly: {
        count: 7,
        weekdays: [
            "Sunday",
            "Wednesday",
        ],
        weeks: [
            "First",
            "Last",
        ],
    },
    retentionWeekly: {
        count: 42,
        weekdays: [
            "Sunday",
            "Wednesday",
            "Friday",
            "Saturday",
        ],
    },
    retentionYearly: {
        count: 77,
        months: ["January"],
        weekdays: ["Sunday"],
        weeks: ["Last"],
    },
    timezone: "UTC",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/backup_policy_vm.markdown.



## Create a PolicyVM Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/backup/#PolicyVM">PolicyVM</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/backup/#PolicyVMArgs">PolicyVMArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">PolicyVM</span><span class="p">(resource_name, opts=None, </span>backup=None<span class="p">, </span>name=None<span class="p">, </span>recovery_vault_name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>retention_daily=None<span class="p">, </span>retention_monthly=None<span class="p">, </span>retention_weekly=None<span class="p">, </span>retention_yearly=None<span class="p">, </span>tags=None<span class="p">, </span>timezone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewPolicyVM<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMArgs">PolicyVMArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVM">PolicyVM</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Backup.PolicyVM.html">PolicyVM</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Backup.PolicyVMArgs.html">PolicyVMArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Policy<wbr>VMRetention<wbr>Daily<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Policy<wbr>VMRetention<wbr>Monthly<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Policy<wbr>VMRetention<wbr>Weekly<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Policy<wbr>VMRetention<wbr>Yearly<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">*Policy<wbr>VMRetention<wbr>Daily</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">*Policy<wbr>VMRetention<wbr>Monthly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">*Policy<wbr>VMRetention<wbr>Weekly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">*Policy<wbr>VMRetention<wbr>Yearly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Policy<wbr>VMRetention<wbr>Daily?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Policy<wbr>VMRetention<wbr>Monthly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Policy<wbr>VMRetention<wbr>Weekly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Policy<wbr>VMRetention<wbr>Yearly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Dict[Policy<wbr>VMBackup]</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>recovery_<wbr>vault_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Dict[Policy<wbr>VMRetention<wbr>Daily]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Dict[Policy<wbr>VMRetention<wbr>Monthly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Dict[Policy<wbr>VMRetention<wbr>Weekly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Dict[Policy<wbr>VMRetention<wbr>Yearly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## PolicyVM Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Policy<wbr>VMRetention<wbr>Daily?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Policy<wbr>VMRetention<wbr>Monthly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Policy<wbr>VMRetention<wbr>Weekly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Policy<wbr>VMRetention<wbr>Yearly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">*Policy<wbr>VMRetention<wbr>Daily</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">*Policy<wbr>VMRetention<wbr>Monthly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">*Policy<wbr>VMRetention<wbr>Weekly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">*Policy<wbr>VMRetention<wbr>Yearly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Policy<wbr>VMRetention<wbr>Daily?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Policy<wbr>VMRetention<wbr>Monthly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Policy<wbr>VMRetention<wbr>Weekly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Policy<wbr>VMRetention<wbr>Yearly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Dict[Policy<wbr>VMBackup]</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recovery_<wbr>vault_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention_<wbr>daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Dict[Policy<wbr>VMRetention<wbr>Daily]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention_<wbr>monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Dict[Policy<wbr>VMRetention<wbr>Monthly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention_<wbr>weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Dict[Policy<wbr>VMRetention<wbr>Weekly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention_<wbr>yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Dict[Policy<wbr>VMRetention<wbr>Yearly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing PolicyVM Resource

Get an existing PolicyVM resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/backup/#PolicyVMState">PolicyVMState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/backup/#PolicyVM">PolicyVM</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>backup=None<span class="p">, </span>name=None<span class="p">, </span>recovery_vault_name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>retention_daily=None<span class="p">, </span>retention_monthly=None<span class="p">, </span>retention_weekly=None<span class="p">, </span>retention_yearly=None<span class="p">, </span>tags=None<span class="p">, </span>timezone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPolicyVM<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMState">PolicyVMState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVM">PolicyVM</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Backup.PolicyVM.html">PolicyVM</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Backup.PolicyVMState.html">PolicyVMState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Policy<wbr>VMRetention<wbr>Daily<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Policy<wbr>VMRetention<wbr>Monthly<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Policy<wbr>VMRetention<wbr>Weekly<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Policy<wbr>VMRetention<wbr>Yearly<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">*Policy<wbr>VMBackup</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">*Policy<wbr>VMRetention<wbr>Daily</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">*Policy<wbr>VMRetention<wbr>Monthly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">*Policy<wbr>VMRetention<wbr>Weekly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">*Policy<wbr>VMRetention<wbr>Yearly</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Policy<wbr>VMBackup?</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recovery<wbr>Vault<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Policy<wbr>VMRetention<wbr>Daily?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Policy<wbr>VMRetention<wbr>Monthly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Policy<wbr>VMRetention<wbr>Weekly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Policy<wbr>VMRetention<wbr>Yearly?</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmbackup">Dict[Policy<wbr>VMBackup]</a></span>
    </dt>
    <dd>{{% md %}}Configures the Policy backup frequency, times & days as documented in the `backup` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Backup Policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recovery_<wbr>vault_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the policy. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>daily</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentiondaily">Dict[Policy<wbr>VMRetention<wbr>Daily]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>monthly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionmonthly">Dict[Policy<wbr>VMRetention<wbr>Monthly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy monthly retention as documented in the `retention_monthly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>weekly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionweekly">Dict[Policy<wbr>VMRetention<wbr>Weekly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>yearly</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#policyvmretentionyearly">Dict[Policy<wbr>VMRetention<wbr>Yearly]</a></span>
    </dt>
    <dd>{{% md %}}Configures the policy yearly retention as documented in the `retention_yearly` block below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the timezone. Defaults to `UTC`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Policy<wbr>VMBackup</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#PolicyVMBackup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#PolicyVMBackup">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMBackupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMBackupOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Sets the backup frequency. Must be either `Daily` or`Weekly`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time of day to perform the backup in 24hour format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Sets the backup frequency. Must be either `Daily` or`Weekly`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time of day to perform the backup in 24hour format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Sets the backup frequency. Must be either `Daily` or`Weekly`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time of day to perform the backup in 24hour format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Sets the backup frequency. Must be either `Daily` or`Weekly`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time of day to perform the backup in 24hour format.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>VMRetention<wbr>Daily</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#PolicyVMRetentionDaily">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#PolicyVMRetentionDaily">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionDailyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionDailyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>VMRetention<wbr>Monthly</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#PolicyVMRetentionMonthly">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#PolicyVMRetentionMonthly">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionMonthlyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionMonthlyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>VMRetention<wbr>Weekly</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#PolicyVMRetentionWeekly">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#PolicyVMRetentionWeekly">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionWeeklyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionWeeklyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Policy<wbr>VMRetention<wbr>Yearly</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#PolicyVMRetentionYearly">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#PolicyVMRetentionYearly">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionYearlyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/backup?tab=doc#PolicyVMRetentionYearlyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Months</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Months</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>months</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of yearly backups to keep. Must be between `1` and `9999`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>months</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The months of the year to retain backups of. Must be one of `January`, `February`, `March`, `April`, `May`, `June`, `July`, `Augest`, `September`, `October`, `November` and `December`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The weekday backups to retain . Must be one of `Sunday`, `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday` or `Saturday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weeks</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The weeks of the month to retain backups of. Must be one of `First`, `Second`, `Third`, `Fourth`, `Last`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

