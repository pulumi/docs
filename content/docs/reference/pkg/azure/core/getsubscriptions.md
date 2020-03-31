
---
title: "GetSubscriptions"
block_external_search_index: true
---

Use this data source to access information about all the Subscriptions currently available.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/subscriptions.html.markdown.





## Using GetSubscriptions

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getSubscriptions<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/core/#GetSubscriptionsArgs">GetSubscriptionsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/core/#GetSubscriptionsResult">GetSubscriptionsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_subscriptions(</span>display_name_contains=None<span class="p">, </span>display_name_prefix=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupSubscriptions<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/core?tab=doc#LookupSubscriptionsArgs">LookupSubscriptionsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/core?tab=doc#LookupSubscriptionsResult">LookupSubscriptionsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetSubscriptions </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Core.GetSubscriptionsResult.html">GetSubscriptionsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Core.Inputs.GetSubscriptionsArgs.html">GetSubscriptionsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">Pulumi.InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name<wbr>Contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive value which must be contained within the `display_name` field, used to filter the results
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive prefix which can be used to filter on the `display_name` field
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name<wbr>Contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A case-insensitive value which must be contained within the `display_name` field, used to filter the results
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A case-insensitive prefix which can be used to filter on the `display_name` field
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name<wbr>Contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive value which must be contained within the `display_name` field, used to filter the results
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A case-insensitive prefix which can be used to filter on the `display_name` field
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name_<wbr>contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A case-insensitive value which must be contained within the `display_name` field, used to filter the results
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A case-insensitive prefix which can be used to filter on the `display_name` field
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetSubscriptions Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Display<wbr>Name<wbr>Contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subscriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsubscriptionssubscription">List&lt;Get<wbr>Subscriptions<wbr>Subscription&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `subscription` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Display<wbr>Name<wbr>Contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subscriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsubscriptionssubscription">[]Get<wbr>Subscriptions<wbr>Subscription</a></span>
    </dt>
    <dd>{{% md %}}One or more `subscription` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>display<wbr>Name<wbr>Contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subscriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsubscriptionssubscription">Get<wbr>Subscriptions<wbr>Subscription[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `subscription` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>display_<wbr>name_<wbr>contains</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subscriptions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getsubscriptionssubscription">List[Get<wbr>Subscriptions<wbr>Subscription]</a></span>
    </dt>
    <dd>{{% md %}}One or more `subscription` blocks as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Subscriptions<wbr>Subscription</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetSubscriptionsSubscription">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/core?tab=doc#GetSubscriptionsSubscription">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location<wbr>Placement<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription location placement ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Quota<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription quota ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spending<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription spending limit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription GUID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Location<wbr>Placement<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription location placement ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Quota<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription quota ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spending<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription spending limit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription GUID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location<wbr>Placement<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription location placement ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>quota<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription quota ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spending<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription spending limit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription GUID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The subscription tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription display name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>location<wbr>Placement<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription location placement ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>quota<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription quota ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spending<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription spending limit.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subscription_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription GUID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The subscription tenant ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







