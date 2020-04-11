
---
title: "AutoscaleSetting"
block_external_search_index: true
---



Manages a AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.

## Example Usage (repeating on weekends)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure";

const exampleResourceGroup = new azure.core.ResourceGroup("example", {
    location: "West US",
});
const exampleScaleSet = new azure.compute.ScaleSet("example", {});
const exampleAutoscaleSetting = new azure.monitoring.AutoscaleSetting("example", {
    location: exampleResourceGroup.location,
    notification: {
        email: {
            customEmails: ["admin@contoso.com"],
            sendToSubscriptionAdministrator: true,
            sendToSubscriptionCoAdministrator: true,
        },
    },
    profiles: [{
        capacity: {
            default: 1,
            maximum: 10,
            minimum: 1,
        },
        name: "Weekends",
        recurrence: {
            days: [
                "Saturday",
                "Sunday",
            ],
            frequency: "Week",
            hours: 12,
            minutes: 0,
            timezone: "Pacific Standard Time",
        },
        rules: [
            {
                metricTrigger: {
                    metricName: "Percentage CPU",
                    metricResourceId: exampleScaleSet.id,
                    operator: "GreaterThan",
                    statistic: "Average",
                    threshold: 90,
                    timeAggregation: "Average",
                    timeGrain: "PT1M",
                    timeWindow: "PT5M",
                },
                scaleAction: {
                    cooldown: "PT1M",
                    direction: "Increase",
                    type: "ChangeCount",
                    value: 2,
                },
            },
            {
                metricTrigger: {
                    metricName: "Percentage CPU",
                    metricResourceId: exampleScaleSet.id,
                    operator: "LessThan",
                    statistic: "Average",
                    threshold: 10,
                    timeAggregation: "Average",
                    timeGrain: "PT1M",
                    timeWindow: "PT5M",
                },
                scaleAction: {
                    cooldown: "PT1M",
                    direction: "Decrease",
                    type: "ChangeCount",
                    value: 2,
                },
            },
        ],
    }],
    resourceGroupName: exampleResourceGroup.name,
    targetResourceId: exampleScaleSet.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown.



## Create a AutoscaleSetting Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/monitoring/#AutoscaleSetting">AutoscaleSetting</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/monitoring/#AutoscaleSettingArgs">AutoscaleSettingArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AutoscaleSetting</span><span class="p">(resource_name, opts=None, </span>enabled=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>notification=None<span class="p">, </span>profiles=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>tags=None<span class="p">, </span>target_resource_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAutoscaleSetting<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingArgs">AutoscaleSettingArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSetting">AutoscaleSetting</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Monitoring.AutoscaleSetting.html">AutoscaleSetting</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Monitoring.AutoscaleSettingArgs.html">AutoscaleSettingArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Autoscale<wbr>Setting<wbr>Notification<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">List&lt;Autoscale<wbr>Setting<wbr>Profile<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">*Autoscale<wbr>Setting<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">[]Autoscale<wbr>Setting<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Autoscale<wbr>Setting<wbr>Notification?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">Autoscale<wbr>Setting<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Dict[Autoscale<wbr>Setting<wbr>Notification]</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">List[Autoscale<wbr>Setting<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target_<wbr>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AutoscaleSetting Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Autoscale<wbr>Setting<wbr>Notification?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">List&lt;Autoscale<wbr>Setting<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>Target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">*Autoscale<wbr>Setting<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">[]Autoscale<wbr>Setting<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>Target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Autoscale<wbr>Setting<wbr>Notification?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">Autoscale<wbr>Setting<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Dict[Autoscale<wbr>Setting<wbr>Notification]</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">List[Autoscale<wbr>Setting<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>target_<wbr>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AutoscaleSetting Resource

Get an existing AutoscaleSetting resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/monitoring/#AutoscaleSettingState">AutoscaleSettingState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/monitoring/#AutoscaleSetting">AutoscaleSetting</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>enabled=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>notification=None<span class="p">, </span>profiles=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>tags=None<span class="p">, </span>target_resource_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAutoscaleSetting<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingState">AutoscaleSettingState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSetting">AutoscaleSetting</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Monitoring.AutoscaleSetting.html">AutoscaleSetting</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Monitoring.AutoscaleSettingState.html">AutoscaleSettingState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Autoscale<wbr>Setting<wbr>Notification<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">List&lt;Autoscale<wbr>Setting<wbr>Profile<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>Target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">*Autoscale<wbr>Setting<wbr>Notification</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">[]Autoscale<wbr>Setting<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>Target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Autoscale<wbr>Setting<wbr>Notification?</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">Autoscale<wbr>Setting<wbr>Profile[]?</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>target<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the AutoScale Setting. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotification">Dict[Autoscale<wbr>Setting<wbr>Notification]</a></span>
    </dt>
    <dd>{{% md %}}Specifies a `notification` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofile">List[Autoscale<wbr>Setting<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}Specifies one or more (up to 20) `profile` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.
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
        <span>target_<wbr>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the resource ID of the resource that the autoscale setting should be added to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Autoscale<wbr>Setting<wbr>Notification</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingNotification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingNotification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingNotificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingNotificationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationemail">Autoscale<wbr>Setting<wbr>Notification<wbr>Email<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `email` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Webhooks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationwebhook">List&lt;Autoscale<wbr>Setting<wbr>Notification<wbr>Webhook<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more `webhook` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationemail">*Autoscale<wbr>Setting<wbr>Notification<wbr>Email</a></span>
    </dt>
    <dd>{{% md %}}A `email` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Webhooks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationwebhook">[]Autoscale<wbr>Setting<wbr>Notification<wbr>Webhook</a></span>
    </dt>
    <dd>{{% md %}}One or more `webhook` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationemail">Autoscale<wbr>Setting<wbr>Notification<wbr>Email?</a></span>
    </dt>
    <dd>{{% md %}}A `email` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>webhooks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationwebhook">Autoscale<wbr>Setting<wbr>Notification<wbr>Webhook[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more `webhook` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationemail">Dict[Autoscale<wbr>Setting<wbr>Notification<wbr>Email]</a></span>
    </dt>
    <dd>{{% md %}}A `email` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>webhooks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingnotificationwebhook">List[Autoscale<wbr>Setting<wbr>Notification<wbr>Webhook]</a></span>
    </dt>
    <dd>{{% md %}}One or more `webhook` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Notification<wbr>Email</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingNotificationEmail">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingNotificationEmail">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingNotificationEmailArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingNotificationEmailOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Emails</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Specifies a list of custom email addresses to which the email notifications will be sent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Send<wbr>To<wbr>Subscription<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription administrator? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Send<wbr>To<wbr>Subscription<wbr>Co<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription co-administrator? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Emails</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Specifies a list of custom email addresses to which the email notifications will be sent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Send<wbr>To<wbr>Subscription<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription administrator? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Send<wbr>To<wbr>Subscription<wbr>Co<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription co-administrator? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Emails</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Specifies a list of custom email addresses to which the email notifications will be sent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>send<wbr>To<wbr>Subscription<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription administrator? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>send<wbr>To<wbr>Subscription<wbr>Co<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription co-administrator? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Emails</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Specifies a list of custom email addresses to which the email notifications will be sent.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>send<wbr>To<wbr>Subscription<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription administrator? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>send<wbr>To<wbr>Subscription<wbr>Co<wbr>Administrator</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Should email notifications be sent to the subscription co-administrator? Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Notification<wbr>Webhook</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingNotificationWebhook">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingNotificationWebhook">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingNotificationWebhookArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingNotificationWebhookOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A map of settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The HTTPS URI which should receive scale notifications.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A map of settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The HTTPS URI which should receive scale notifications.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A map of settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The HTTPS URI which should receive scale notifications.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>properties</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A map of settings.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service_<wbr>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The HTTPS URI which should receive scale notifications.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilecapacity">Autoscale<wbr>Setting<wbr>Profile<wbr>Capacity<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `capacity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fixed<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilefixeddate">Autoscale<wbr>Setting<wbr>Profile<wbr>Fixed<wbr>Date<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `fixed_date` block as defined below. This cannot be specified if a `recurrence` block is specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerecurrence">Autoscale<wbr>Setting<wbr>Profile<wbr>Recurrence<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `recurrence` block as defined below. This cannot be specified if a `fixed_date` block is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerule">List&lt;Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}One or more (up to 10) `rule` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilecapacity">Autoscale<wbr>Setting<wbr>Profile<wbr>Capacity</a></span>
    </dt>
    <dd>{{% md %}}A `capacity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fixed<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilefixeddate">*Autoscale<wbr>Setting<wbr>Profile<wbr>Fixed<wbr>Date</a></span>
    </dt>
    <dd>{{% md %}}A `fixed_date` block as defined below. This cannot be specified if a `recurrence` block is specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerecurrence">*Autoscale<wbr>Setting<wbr>Profile<wbr>Recurrence</a></span>
    </dt>
    <dd>{{% md %}}A `recurrence` block as defined below. This cannot be specified if a `fixed_date` block is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerule">[]Autoscale<wbr>Setting<wbr>Profile<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}One or more (up to 10) `rule` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilecapacity">Autoscale<wbr>Setting<wbr>Profile<wbr>Capacity</a></span>
    </dt>
    <dd>{{% md %}}A `capacity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fixed<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilefixeddate">Autoscale<wbr>Setting<wbr>Profile<wbr>Fixed<wbr>Date?</a></span>
    </dt>
    <dd>{{% md %}}A `fixed_date` block as defined below. This cannot be specified if a `recurrence` block is specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerecurrence">Autoscale<wbr>Setting<wbr>Profile<wbr>Recurrence?</a></span>
    </dt>
    <dd>{{% md %}}A `recurrence` block as defined below. This cannot be specified if a `fixed_date` block is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerule">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}One or more (up to 10) `rule` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilecapacity">Dict[Autoscale<wbr>Setting<wbr>Profile<wbr>Capacity]</a></span>
    </dt>
    <dd>{{% md %}}A `capacity` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fixed<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilefixeddate">Dict[Autoscale<wbr>Setting<wbr>Profile<wbr>Fixed<wbr>Date]</a></span>
    </dt>
    <dd>{{% md %}}A `fixed_date` block as defined below. This cannot be specified if a `recurrence` block is specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the profile.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerecurrence">Dict[Autoscale<wbr>Setting<wbr>Profile<wbr>Recurrence]</a></span>
    </dt>
    <dd>{{% md %}}A `recurrence` block as defined below. This cannot be specified if a `fixed_date` block is specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerule">List[Autoscale<wbr>Setting<wbr>Profile<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}One or more (up to 10) `rule` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile<wbr>Capacity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfileCapacity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfileCapacity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileCapacityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileCapacityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of instances that are available for scaling if metrics are not available for evaluation. The default is only used if the current instance count is lower than the default. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>maximum</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>minimum</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum number of instances for this resource. Valid values are between `0` and `1000`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile<wbr>Fixed<wbr>Date</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfileFixedDate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfileFixedDate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileFixedDateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileFixedDateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the end date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the start date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Time Zone of the `start` and `end` times. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the end date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the start date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Time Zone of the `start` and `end` times. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the end date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the start date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Time Zone of the `start` and `end` times. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the end date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the start date for the profile, formatted as an RFC3339 date string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Time Zone of the `start` and `end` times. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile<wbr>Recurrence</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfileRecurrence">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfileRecurrence">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRecurrenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRecurrenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of days that this profile takes effect on. Possible values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` and `Sunday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from `0` to `23`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Time Zone used for the `hours` field. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of days that this profile takes effect on. Possible values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` and `Sunday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from `0` to `23`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Time Zone used for the `hours` field. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of days that this profile takes effect on. Possible values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` and `Sunday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from `0` to `23`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Time Zone used for the `hours` field. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of days that this profile takes effect on. Possible values include `Monday`, `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday` and `Sunday`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A list containing a single item, which specifies the Hour interval at which this recurrence should be triggered (in 24-hour time). Possible values are from `0` to `23`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A list containing a single item which specifies the Minute interval at which this recurrence should be triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Time Zone used for the `hours` field. A list of [possible values can be found here](https://msdn.microsoft.com/en-us/library/azure/dn931928.aspx). Defaults to `UTC`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfileRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfileRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Metric<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulemetrictrigger">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Metric<wbr>Trigger<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `metric_trigger` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scale<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulescaleaction">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Scale<wbr>Action<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `scale_action` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Metric<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulemetrictrigger">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Metric<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A `metric_trigger` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scale<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulescaleaction">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Scale<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}A `scale_action` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>metric<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulemetrictrigger">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Metric<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A `metric_trigger` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scale<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulescaleaction">Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Scale<wbr>Action</a></span>
    </dt>
    <dd>{{% md %}}A `scale_action` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>metric<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulemetrictrigger">Dict[Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Metric<wbr>Trigger]</a></span>
    </dt>
    <dd>{{% md %}}A `metric_trigger` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scale<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#autoscalesettingprofilerulescaleaction">Dict[Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Scale<wbr>Action]</a></span>
    </dt>
    <dd>{{% md %}}A `scale_action` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Metric<wbr>Trigger</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfileRuleMetricTrigger">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfileRuleMetricTrigger">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRuleMetricTriggerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRuleMetricTriggerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the metric that defines what the rule monitors, such as `Percentage CPU` for `Virtual Machine Scale Sets` and `CpuPercentage` for `App Service Plan`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Metric<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Resource which the Rule monitors.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the operator used to compare the metric data and threshold. Possible values are: `Equals`, `NotEquals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Statistic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how the metrics from multiple instances are combined. Possible values are `Average`, `Min` and `Max`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}Specifies the threshold of the metric that triggers the scale action.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Aggregation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how the data that's collected should be combined over time. Possible values include `Average`, `Count`, `Maximum`, `Minimum`, `Last` and `Total`. Defaults to `Average`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Grain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the metric that defines what the rule monitors, such as `Percentage CPU` for `Virtual Machine Scale Sets` and `CpuPercentage` for `App Service Plan`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Metric<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Resource which the Rule monitors.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the operator used to compare the metric data and threshold. Possible values are: `Equals`, `NotEquals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Statistic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how the metrics from multiple instances are combined. Possible values are `Average`, `Min` and `Max`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}Specifies the threshold of the metric that triggers the scale action.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Aggregation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how the data that's collected should be combined over time. Possible values include `Average`, `Count`, `Maximum`, `Minimum`, `Last` and `Total`. Defaults to `Average`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Grain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the metric that defines what the rule monitors, such as `Percentage CPU` for `Virtual Machine Scale Sets` and `CpuPercentage` for `App Service Plan`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>metric<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the Resource which the Rule monitors.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the operator used to compare the metric data and threshold. Possible values are: `Equals`, `NotEquals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>statistic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how the metrics from multiple instances are combined. Possible values are `Average`, `Min` and `Max`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the threshold of the metric that triggers the scale action.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Aggregation</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how the data that's collected should be combined over time. Possible values include `Average`, `Count`, `Maximum`, `Minimum`, `Last` and `Total`. Defaults to `Average`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Grain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>metric<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the metric that defines what the rule monitors, such as `Percentage CPU` for `Virtual Machine Scale Sets` and `CpuPercentage` for `App Service Plan`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>metric<wbr>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the Resource which the Rule monitors.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operator</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the operator used to compare the metric data and threshold. Possible values are: `Equals`, `NotEquals`, `GreaterThan`, `GreaterThanOrEqual`, `LessThan`, `LessThanOrEqual`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>statistic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how the metrics from multiple instances are combined. Possible values are `Average`, `Min` and `Max`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the threshold of the metric that triggers the scale action.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Aggregation</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how the data that's collected should be combined over time. Possible values include `Average`, `Count`, `Maximum`, `Minimum`, `Last` and `Total`. Defaults to `Average`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Grain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the granularity of metrics that the rule monitors, which must be one of the pre-defined values returned from the metric definitions for the metric. This value must be between 1 minute and 12 hours an be formatted as an ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the time range for which data is collected, which must be greater than the delay in metric collection (which varies from resource to resource). This value must be between 5 minutes and 12 hours and be formatted as an ISO 8601 string.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Autoscale<wbr>Setting<wbr>Profile<wbr>Rule<wbr>Scale<wbr>Action</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AutoscaleSettingProfileRuleScaleAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AutoscaleSettingProfileRuleScaleAction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRuleScaleActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/monitoring?tab=doc#AutoscaleSettingProfileRuleScaleActionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Direction</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scale direction. Possible values are `Increase` and `Decrease`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of action that should occur. Possible values are `ChangeCount`, `ExactCount` and `PercentChangeCount`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances involved in the scaling action. Defaults to `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Direction</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scale direction. Possible values are `Increase` and `Decrease`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of action that should occur. Possible values are `ChangeCount`, `ExactCount` and `PercentChangeCount`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances involved in the scaling action. Defaults to `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>direction</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The scale direction. Possible values are `Increase` and `Decrease`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of action that should occur. Possible values are `ChangeCount`, `ExactCount` and `PercentChangeCount`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of instances involved in the scaling action. Defaults to `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The amount of time to wait since the last scaling action before this action occurs. Must be between 1 minute and 1 week and formatted as a ISO 8601 string.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>direction</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The scale direction. Possible values are `Increase` and `Decrease`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of action that should occur. Possible values are `ChangeCount`, `ExactCount` and `PercentChangeCount`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of instances involved in the scaling action. Defaults to `1`.
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

