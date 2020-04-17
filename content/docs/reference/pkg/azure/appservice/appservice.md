
---
title: "AppService"
block_external_search_index: true
---



Manages an App Service (within an App Service Plan).

> **Note:** When using Slots - the `app_settings`, `connection_string` and `site_config` blocks on the `azure.appservice.AppService` resource will be overwritten when promoting a Slot using the `azure.appservice.ActiveSlot` resource.

{{% examples %}}
{{% /examples %}}



## Create a AppService Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/appservice/#AppService">AppService</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/appservice/#AppServiceArgs">AppServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AppService</span><span class="p">(resource_name, opts=None, </span>app_service_plan_id=None<span class="p">, </span>app_settings=None<span class="p">, </span>auth_settings=None<span class="p">, </span>backup=None<span class="p">, </span>client_affinity_enabled=None<span class="p">, </span>client_cert_enabled=None<span class="p">, </span>connection_strings=None<span class="p">, </span>enabled=None<span class="p">, </span>https_only=None<span class="p">, </span>identity=None<span class="p">, </span>location=None<span class="p">, </span>logs=None<span class="p">, </span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>site_config=None<span class="p">, </span>storage_accounts=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAppService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceArgs">AppServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppService">AppService</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.AppService.AppService.html">AppService</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.AppService.AppServiceArgs.html">AppServiceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">App<wbr>Service<wbr>Backup<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">List&lt;App<wbr>Service<wbr>Connection<wbr>String<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">App<wbr>Service<wbr>Identity<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">App<wbr>Service<wbr>Logs<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Site<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">App<wbr>Service<wbr>Site<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">List&lt;App<wbr>Service<wbr>Storage<wbr>Account<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">App<wbr>Service<wbr>Auth<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">App<wbr>Service<wbr>Backup</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">[]App<wbr>Service<wbr>Connection<wbr>String</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">App<wbr>Service<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">App<wbr>Service<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Site<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">App<wbr>Service<wbr>Site<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">[]App<wbr>Service<wbr>Storage<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">App<wbr>Service<wbr>Auth<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">App<wbr>Service<wbr>Backup</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">App<wbr>Service<wbr>Connection<wbr>String[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">App<wbr>Service<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">App<wbr>Service<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>site<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">App<wbr>Service<wbr>Site<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">App<wbr>Service<wbr>Storage<wbr>Account[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>app_<wbr>service_<wbr>plan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">Dict[App<wbr>Service<wbr>Auth<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">Dict[App<wbr>Service<wbr>Backup]</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>affinity_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>cert_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">List[App<wbr>Service<wbr>Connection<wbr>String]</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">Dict[App<wbr>Service<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">Dict[App<wbr>Service<wbr>Logs]</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>site_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">Dict[App<wbr>Service<wbr>Site<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">List[App<wbr>Service<wbr>Storage<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AppService Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Default<wbr>Site<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Possible<wbr>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">List&lt;App<wbr>Service<wbr>Site<wbr>Credential&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">List&lt;App<wbr>Service<wbr>Source<wbr>Control&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Default<wbr>Site<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Possible<wbr>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">[]App<wbr>Service<wbr>Site<wbr>Credential</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">[]App<wbr>Service<wbr>Source<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>default<wbr>Site<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>possible<wbr>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">App<wbr>Service<wbr>Site<wbr>Credential[]</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">App<wbr>Service<wbr>Source<wbr>Control[]</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>default_<wbr>site_<wbr>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>outbound_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>possible_<wbr>outbound_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>site_<wbr>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">List[App<wbr>Service<wbr>Site<wbr>Credential]</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">List[App<wbr>Service<wbr>Source<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AppService Resource

Get an existing AppService resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/appservice/#AppServiceState">AppServiceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/appservice/#AppService">AppService</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>app_service_plan_id=None<span class="p">, </span>app_settings=None<span class="p">, </span>auth_settings=None<span class="p">, </span>backup=None<span class="p">, </span>client_affinity_enabled=None<span class="p">, </span>client_cert_enabled=None<span class="p">, </span>connection_strings=None<span class="p">, </span>default_site_hostname=None<span class="p">, </span>enabled=None<span class="p">, </span>https_only=None<span class="p">, </span>identity=None<span class="p">, </span>location=None<span class="p">, </span>logs=None<span class="p">, </span>name=None<span class="p">, </span>outbound_ip_addresses=None<span class="p">, </span>possible_outbound_ip_addresses=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>site_config=None<span class="p">, </span>site_credentials=None<span class="p">, </span>source_controls=None<span class="p">, </span>storage_accounts=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAppService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceState">AppServiceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppService">AppService</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.AppService.AppService.html">AppService</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.AppService.AppServiceState.html">AppServiceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">App<wbr>Service<wbr>Backup<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">List&lt;App<wbr>Service<wbr>Connection<wbr>String<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Site<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">App<wbr>Service<wbr>Identity<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">App<wbr>Service<wbr>Logs<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Possible<wbr>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Site<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">App<wbr>Service<wbr>Site<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">List&lt;App<wbr>Service<wbr>Site<wbr>Credential<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">List&lt;App<wbr>Service<wbr>Source<wbr>Control<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">List&lt;App<wbr>Service<wbr>Storage<wbr>Account<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">App<wbr>Service<wbr>Auth<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">App<wbr>Service<wbr>Backup</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">[]App<wbr>Service<wbr>Connection<wbr>String</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Site<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">App<wbr>Service<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">App<wbr>Service<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Possible<wbr>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Site<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">App<wbr>Service<wbr>Site<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">[]App<wbr>Service<wbr>Site<wbr>Credential</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">[]App<wbr>Service<wbr>Source<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">[]App<wbr>Service<wbr>Storage<wbr>Account</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">App<wbr>Service<wbr>Auth<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">App<wbr>Service<wbr>Backup</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">App<wbr>Service<wbr>Connection<wbr>String[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Site<wbr>Hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">App<wbr>Service<wbr>Identity</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">App<wbr>Service<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>possible<wbr>Outbound<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>site<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">App<wbr>Service<wbr>Site<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">App<wbr>Service<wbr>Site<wbr>Credential[]</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">App<wbr>Service<wbr>Source<wbr>Control[]</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">App<wbr>Service<wbr>Storage<wbr>Account[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>service_<wbr>plan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which to create this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auth_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettings">Dict[App<wbr>Service<wbr>Auth<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}A `auth_settings` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackup">Dict[App<wbr>Service<wbr>Backup]</a></span>
    </dt>
    <dd>{{% md %}}A `backup` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>affinity_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>cert_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceconnectionstring">List[App<wbr>Service<wbr>Connection<wbr>String]</a></span>
    </dt>
    <dd>{{% md %}}One or more `connection_string` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>site_<wbr>hostname</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Default Hostname associated with the App Service - such as `mysite.azurewebsites.net`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceidentity">Dict[App<wbr>Service<wbr>Identity]</a></span>
    </dt>
    <dd>{{% md %}}A Managed Service Identity block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogs">Dict[App<wbr>Service<wbr>Logs]</a></span>
    </dt>
    <dd>{{% md %}}A `logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name of the App Service. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>outbound_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>possible_<wbr>outbound_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A comma separated list of outbound IP addresses - such as `52.23.25.3,52.143.43.12,52.143.43.17` - not all of which are necessarily in use. Superset of `outbound_ip_addresses`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to create the App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>site_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfig">Dict[App<wbr>Service<wbr>Site<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>site_<wbr>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesitecredential">List[App<wbr>Service<wbr>Site<wbr>Credential]</a></span>
    </dt>
    <dd>{{% md %}}A `site_credential` block as defined below, which contains the site-level credentials used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesourcecontrol">List[App<wbr>Service<wbr>Source<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}A `source_control` block as defined below, which contains the Source Control information when `scm_type` is set to `LocalGit`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>accounts</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicestorageaccount">List[App<wbr>Service<wbr>Storage<wbr>Account]</a></span>
    </dt>
    <dd>{{% md %}}One or more `storage_account` blocks as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>App<wbr>Service<wbr>Auth<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceAuthSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceAuthSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Authentication enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsactivedirectory">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Active<wbr>Directory<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Login<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form "key=value".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>External<wbr>Redirect<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}External URLs that can be redirected to as part of logging in or logging out of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The default provider to use when multiple providers have been set up. Possible values are `AzureActiveDirectory`, `Facebook`, `Google`, `MicrosoftAccount` and `Twitter`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Facebook</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsfacebook">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Facebook<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `facebook` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsgoogle">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Google<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `google` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. https://sts.windows.net/{tenant-guid}/.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Microsoft</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsmicrosoft">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Microsoft<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `microsoft` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The runtime version of the Authentication/Authorization module.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Refresh<wbr>Extension<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">double</a></span>
    </dt>
    <dd>{{% md %}}The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Store<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingstwitter">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Twitter<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `twitter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unauthenticated<wbr>Client<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take when an unauthenticated client attempts to access the app. Possible values are `AllowAnonymous` and `RedirectToLoginPage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Authentication enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsactivedirectory">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}A `active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Additional<wbr>Login<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form "key=value".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>External<wbr>Redirect<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}External URLs that can be redirected to as part of logging in or logging out of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The default provider to use when multiple providers have been set up. Possible values are `AzureActiveDirectory`, `Facebook`, `Google`, `MicrosoftAccount` and `Twitter`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Facebook</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsfacebook">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Facebook</a></span>
    </dt>
    <dd>{{% md %}}A `facebook` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsgoogle">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Google</a></span>
    </dt>
    <dd>{{% md %}}A `google` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. https://sts.windows.net/{tenant-guid}/.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Microsoft</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsmicrosoft">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Microsoft</a></span>
    </dt>
    <dd>{{% md %}}A `microsoft` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The runtime version of the Authentication/Authorization module.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Refresh<wbr>Extension<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#number">float64</a></span>
    </dt>
    <dd>{{% md %}}The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token<wbr>Store<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingstwitter">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Twitter</a></span>
    </dt>
    <dd>{{% md %}}A `twitter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unauthenticated<wbr>Client<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take when an unauthenticated client attempts to access the app. Possible values are `AllowAnonymous` and `RedirectToLoginPage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Authentication enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsactivedirectory">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}A `active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Login<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form "key=value".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>External<wbr>Redirect<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}External URLs that can be redirected to as part of logging in or logging out of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The default provider to use when multiple providers have been set up. Possible values are `AzureActiveDirectory`, `Facebook`, `Google`, `MicrosoftAccount` and `Twitter`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>facebook</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsfacebook">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Facebook</a></span>
    </dt>
    <dd>{{% md %}}A `facebook` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsgoogle">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Google</a></span>
    </dt>
    <dd>{{% md %}}A `google` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. https://sts.windows.net/{tenant-guid}/.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>microsoft</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsmicrosoft">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Microsoft</a></span>
    </dt>
    <dd>{{% md %}}A `microsoft` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The runtime version of the Authentication/Authorization module.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Refresh<wbr>Extension<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/number">number</a></span>
    </dt>
    <dd>{{% md %}}The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Store<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingstwitter">App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Twitter</a></span>
    </dt>
    <dd>{{% md %}}A `twitter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unauthenticated<wbr>Client<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The action to take when an unauthenticated client attempts to access the app. Possible values are `AllowAnonymous` and `RedirectToLoginPage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Authentication enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsactivedirectory">Dict[App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}A `active_directory` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>additional<wbr>Login<wbr>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Login parameters to send to the OpenID Connect authorization endpoint when a user logs in. Each parameter must be in the form "key=value".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>External<wbr>Redirect<wbr>Urls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}External URLs that can be redirected to as part of logging in or logging out of the app.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Provider</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The default provider to use when multiple providers have been set up. Possible values are `AzureActiveDirectory`, `Facebook`, `Google`, `MicrosoftAccount` and `Twitter`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>facebook</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsfacebook">Dict[App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Facebook]</a></span>
    </dt>
    <dd>{{% md %}}A `facebook` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsgoogle">Dict[App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Google]</a></span>
    </dt>
    <dd>{{% md %}}A `google` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>issuer</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Issuer URI. When using Azure Active Directory, this value is the URI of the directory tenant, e.g. https://sts.windows.net/{tenant-guid}/.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>microsoft</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingsmicrosoft">Dict[App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Microsoft]</a></span>
    </dt>
    <dd>{{% md %}}A `microsoft` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The runtime version of the Authentication/Authorization module.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Refresh<wbr>Extension<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of hours after session token expiration that a session token can be used to call the token refresh API. Defaults to 72.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token<wbr>Store<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If enabled the module will durably store platform-specific security tokens that are obtained during login flows. Defaults to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>twitter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appserviceauthsettingstwitter">Dict[App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Twitter]</a></span>
    </dt>
    <dd>{{% md %}}A `twitter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unauthenticated<wbr>Client<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The action to take when an unauthenticated client attempts to access the app. Possible values are `AllowAnonymous` and `RedirectToLoginPage`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Active<wbr>Directory</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceAuthSettingsActiveDirectory">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceAuthSettingsActiveDirectory">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsActiveDirectoryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsActiveDirectoryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Allowed audience values to consider when validating JWTs issued by Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allowed<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Allowed audience values to consider when validating JWTs issued by Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Allowed audience values to consider when validating JWTs issued by Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Client ID of this relying party application. Enables OpenIDConnection authentication with Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allowed<wbr>Audiences</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Allowed audience values to consider when validating JWTs issued by Azure Active Directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Client Secret of this relying party application. If no secret is provided, implicit flow will be used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Facebook</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceAuthSettingsFacebook">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceAuthSettingsFacebook">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsFacebookArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsFacebookOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The App ID of the Facebook app used for login
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The App Secret of the Facebook app used for Facebook Login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. https://developers.facebook.com/docs/facebook-login
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The App ID of the Facebook app used for login
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The App Secret of the Facebook app used for Facebook Login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. https://developers.facebook.com/docs/facebook-login
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The App ID of the Facebook app used for login
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The App Secret of the Facebook app used for Facebook Login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. https://developers.facebook.com/docs/facebook-login
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>app_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The App ID of the Facebook app used for login
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>app_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The App Secret of the Facebook app used for Facebook Login.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Facebook Login authentication. https://developers.facebook.com/docs/facebook-login
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Google</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceAuthSettingsGoogle">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceAuthSettingsGoogle">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsGoogleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsGoogleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The OpenID Connect Client ID for the Google web application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The client secret associated with the Google web application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. https://developers.google.com/identity/sign-in/web/
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The OpenID Connect Client ID for the Google web application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The client secret associated with the Google web application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. https://developers.google.com/identity/sign-in/web/
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The OpenID Connect Client ID for the Google web application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The client secret associated with the Google web application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. https://developers.google.com/identity/sign-in/web/
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The OpenID Connect Client ID for the Google web application.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The client secret associated with the Google web application.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Google Sign-In authentication. https://developers.google.com/identity/sign-in/web/
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Microsoft</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceAuthSettingsMicrosoft">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceAuthSettingsMicrosoft">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsMicrosoftArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsMicrosoftOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client ID that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client secret that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. https://msdn.microsoft.com/en-us/library/dn631845.aspx
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client ID that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client secret that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. https://msdn.microsoft.com/en-us/library/dn631845.aspx
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client ID that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client secret that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. https://msdn.microsoft.com/en-us/library/dn631845.aspx
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client ID that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 client secret that was created for the app used for authentication.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Scopes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The OAuth 2.0 scopes that will be requested as part of Microsoft Account authentication. https://msdn.microsoft.com/en-us/library/dn631845.aspx
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Auth<wbr>Settings<wbr>Twitter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceAuthSettingsTwitter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceAuthSettingsTwitter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsTwitterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceAuthSettingsTwitterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Consumer<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Consumer<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Consumer<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Consumer<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>consumer<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>consumer<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>consumer<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>consumer<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Backup</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceBackup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceBackup">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceBackupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceBackupOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name for this Backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackupschedule">App<wbr>Service<wbr>Backup<wbr>Schedule<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `schedule` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The SAS URL to a Storage Container where Backups should be saved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is this Backup enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name for this Backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackupschedule">App<wbr>Service<wbr>Backup<wbr>Schedule</a></span>
    </dt>
    <dd>{{% md %}}A `schedule` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The SAS URL to a Storage Container where Backups should be saved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is this Backup enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name for this Backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackupschedule">App<wbr>Service<wbr>Backup<wbr>Schedule</a></span>
    </dt>
    <dd>{{% md %}}A `schedule` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The SAS URL to a Storage Container where Backups should be saved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is this Backup enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the name for this Backup.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicebackupschedule">Dict[App<wbr>Service<wbr>Backup<wbr>Schedule]</a></span>
    </dt>
    <dd>{{% md %}}A `schedule` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The SAS URL to a Storage Container where Backups should be saved.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is this Backup enabled?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Backup<wbr>Schedule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceBackupSchedule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceBackupSchedule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceBackupScheduleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceBackupScheduleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Frequency<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Sets how often the backup should be executed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Frequency<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Sets the unit of time for how often the backup should be executed. Possible values are `Day` or `Hour`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keep<wbr>At<wbr>Least<wbr>One<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Period<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after which Backups should be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Sets when the schedule should start working.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Frequency<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Sets how often the backup should be executed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Frequency<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Sets the unit of time for how often the backup should be executed. Possible values are `Day` or `Hour`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Keep<wbr>At<wbr>Least<wbr>One<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Period<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after which Backups should be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Sets when the schedule should start working.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>frequency<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Sets how often the backup should be executed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>frequency<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Sets the unit of time for how often the backup should be executed. Possible values are `Day` or `Hour`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keep<wbr>At<wbr>Least<wbr>One<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Period<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after which Backups should be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Sets when the schedule should start working.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>frequency<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Sets how often the backup should be executed.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>frequency<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Sets the unit of time for how often the backup should be executed. Possible values are `Day` or `Hour`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>keep<wbr>At<wbr>Least<wbr>One<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Should at least one backup always be kept in the Storage Account by the Retention Policy, regardless of how old it is?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Period<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Specifies the number of days after which Backups should be deleted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Sets when the schedule should start working.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Connection<wbr>String</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceConnectionString">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceConnectionString">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceConnectionStringArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceConnectionStringOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The value for the Connection String.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The value for the Connection String.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The value for the Connection String.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String. Possible values are `APIHub`, `Custom`, `DocDb`, `EventHub`, `MySQL`, `NotificationHub`, `PostgreSQL`, `RedisCache`, `ServiceBus`, `SQLAzure` and  `SQLServer`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The value for the Connection String.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Identity</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceIdentity">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceIdentity">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceIdentityArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceIdentityOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identity type of the App Service. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), `UserAssigned` where you can specify the Service Principal IDs in the `identity_ids` field, and `SystemAssigned, UserAssigned` which assigns both a system managed identity as well as the specified user assigned identities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specifies a list of user managed identity ids to be assigned. Required if `type` is `UserAssigned`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identity type of the App Service. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), `UserAssigned` where you can specify the Service Principal IDs in the `identity_ids` field, and `SystemAssigned, UserAssigned` which assigns both a system managed identity as well as the specified user assigned identities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Specifies a list of user managed identity ids to be assigned. Required if `type` is `UserAssigned`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identity type of the App Service. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), `UserAssigned` where you can specify the Service Principal IDs in the `identity_ids` field, and `SystemAssigned, UserAssigned` which assigns both a system managed identity as well as the specified user assigned identities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Specifies a list of user managed identity ids to be assigned. Required if `type` is `UserAssigned`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>principal<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Specifies the identity type of the App Service. Possible values are `SystemAssigned` (where Azure will generate a Service Principal for you), `UserAssigned` where you can specify the Service Principal IDs in the `identity_ids` field, and `SystemAssigned, UserAssigned` which assigns both a system managed identity as well as the specified user assigned identities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>identity<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Specifies a list of user managed identity ids to be assigned. Required if `type` is `UserAssigned`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>principal_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Principal ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tenant_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Tenant ID for the Service Principal associated with the Managed Service Identity of this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Logs</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceLogs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceLogs">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogs">App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An `application_logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogs">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An `http_logs` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogs">App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}An `application_logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogs">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}An `http_logs` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogs">App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}An `application_logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogs">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs</a></span>
    </dt>
    <dd>{{% md %}}An `http_logs` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogs">Dict[App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs]</a></span>
    </dt>
    <dd>{{% md %}}An `application_logs` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Logs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogs">Dict[App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs]</a></span>
    </dt>
    <dd>{{% md %}}An `http_logs` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceLogsApplicationLogs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceLogsApplicationLogs">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsApplicationLogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsApplicationLogsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogsazureblobstorage">App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogsazureblobstorage">App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogsazureblobstorage">App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogsapplicationlogsazureblobstorage">Dict[App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage]</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Logs<wbr>Application<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceLogsApplicationLogsAzureBlobStorage">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceLogsApplicationLogsAzureBlobStorage">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsApplicationLogsAzureBlobStorageArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsApplicationLogsAzureBlobStorageOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The level at which to log. Possible values include `Error`, `Warning`, `Information`, `Verbose` and `Off`. **NOTE:** this field is not available for `http_logs`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The level at which to log. Possible values include `Error`, `Warning`, `Information`, `Verbose` and `Off`. **NOTE:** this field is not available for `http_logs`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The level at which to log. Possible values include `Error`, `Warning`, `Information`, `Verbose` and `Off`. **NOTE:** this field is not available for `http_logs`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>level</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The level at which to log. Possible values include `Error`, `Warning`, `Information`, `Verbose` and `Off`. **NOTE:** this field is not available for `http_logs`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>retention_<wbr>in_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceLogsHttpLogs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceLogsHttpLogs">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsHttpLogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsHttpLogsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsazureblobstorage">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsfilesystem">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>File<wbr>System<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `file_system` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsazureblobstorage">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsfilesystem">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>File<wbr>System</a></span>
    </dt>
    <dd>{{% md %}}A `file_system` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsazureblobstorage">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsfilesystem">App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>File<wbr>System</a></span>
    </dt>
    <dd>{{% md %}}A `file_system` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Blob<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsazureblobstorage">Dict[App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage]</a></span>
    </dt>
    <dd>{{% md %}}An `azure_blob_storage` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicelogshttplogsfilesystem">Dict[App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>File<wbr>System]</a></span>
    </dt>
    <dd>{{% md %}}A `file_system` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>Azure<wbr>Blob<wbr>Storage</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceLogsHttpLogsAzureBlobStorage">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceLogsHttpLogsAzureBlobStorage">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsHttpLogsAzureBlobStorageArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsHttpLogsAzureBlobStorageOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>retention_<wbr>in_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>sas<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URL to the storage container, with a Service SAS token appended. **NOTE:** there is currently no means of generating Service SAS tokens with the `azurerm` provider.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Logs<wbr>Http<wbr>Logs<wbr>File<wbr>System</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceLogsHttpLogsFileSystem">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceLogsHttpLogsFileSystem">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsHttpLogsFileSystemArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceLogsHttpLogsFileSystemOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum size in megabytes that http log files can use before being removed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>In<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum size in megabytes that http log files can use before being removed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>retention<wbr>In<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>retention<wbr>In<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum size in megabytes that http log files can use before being removed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>retention_<wbr>in_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of days to retain logs for.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>retention<wbr>In<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum size in megabytes that http log files can use before being removed.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Site<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceSiteConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceSiteConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the app be loaded at all times? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Swap<wbr>Slot<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigcors">App<wbr>Service<wbr>Site<wbr>Config<wbr>Cors<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this App Service. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigiprestriction">List&lt;App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of objects representing ip restrictions as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JAVA`, `JETTY`, and `TOMCAT`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11` and their specific versions - except for Java 11 (e.g. `1.7.0_80`, `1.8.0_181`, `11`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the App Service. Possible options are a Docker container (`DOCKER|<user/image:tag>`), a base-64 encoded Docker Compose file (`COMPOSE|${filebase64("compose.yml")}`) or a base-64 encoded Kubernetes Manifest (`KUBE|${filebase64("kubernetes.yml")}`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP to use in this App Service. Possible values are `5.5`, `5.6`, `7.0`, `7.1`, `7.2`, and `7.3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Python to use in this App Service. Possible values are `2.7` and `3.4`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Should WebSockets be enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Windows Docker container image (`DOCKER|<user/image:tag>`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the app be loaded at all times? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Swap<wbr>Slot<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigcors">App<wbr>Service<wbr>Site<wbr>Config<wbr>Cors</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this App Service. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigiprestriction">[]App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction</a></span>
    </dt>
    <dd>{{% md %}}A list of objects representing ip restrictions as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JAVA`, `JETTY`, and `TOMCAT`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11` and their specific versions - except for Java 11 (e.g. `1.7.0_80`, `1.8.0_181`, `11`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the App Service. Possible options are a Docker container (`DOCKER|<user/image:tag>`), a base-64 encoded Docker Compose file (`COMPOSE|${filebase64("compose.yml")}`) or a base-64 encoded Kubernetes Manifest (`KUBE|${filebase64("kubernetes.yml")}`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP to use in this App Service. Possible values are `5.5`, `5.6`, `7.0`, `7.1`, `7.2`, and `7.3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Python to use in this App Service. Possible values are `2.7` and `3.4`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Should WebSockets be enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Windows Docker container image (`DOCKER|<user/image:tag>`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Should the app be loaded at all times? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Swap<wbr>Slot<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigcors">App<wbr>Service<wbr>Site<wbr>Config<wbr>Cors</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this App Service. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigiprestriction">App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction[]</a></span>
    </dt>
    <dd>{{% md %}}A list of objects representing ip restrictions as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JAVA`, `JETTY`, and `TOMCAT`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11` and their specific versions - except for Java 11 (e.g. `1.7.0_80`, `1.8.0_181`, `11`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the App Service. Possible options are a Docker container (`DOCKER|<user/image:tag>`), a base-64 encoded Docker Compose file (`COMPOSE|${filebase64("compose.yml")}`) or a base-64 encoded Kubernetes Manifest (`KUBE|${filebase64("kubernetes.yml")}`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP to use in this App Service. Possible values are `5.5`, `5.6`, `7.0`, `7.1`, `7.2`, and `7.3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Python to use in this App Service. Possible values are `2.7` and `3.4`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Should WebSockets be enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Windows Docker container image (`DOCKER|<user/image:tag>`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the app be loaded at all times? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch, e.g. `/sbin/myserver -b 0.0.0.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Swap<wbr>Slot<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigcors">Dict[App<wbr>Service<wbr>Site<wbr>Config<wbr>Cors]</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service. Possible values are `v2.0` (which will use the latest version of the .net framework for the .net CLR v2 - currently `.net 3.5`) and `v4.0` (which corresponds to the latest version of the .net CLR v4 - which at the time of writing is `.net 4.7.1`). [For more information on which .net CLR version to use based on the .net framework you're targeting - please see this table](https://en.wikipedia.org/wiki/.NET_Framework_version_history#Overview). Defaults to `v4.0`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this App Service. Possible values include: `AllAllowed`, `FtpsOnly` and `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#appservicesiteconfigiprestriction">List[App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction]</a></span>
    </dt>
    <dd>{{% md %}}A list of objects representing ip restrictions as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Java Container to use. If specified `java_version` and `java_container_version` must also be specified. Possible values are `JAVA`, `JETTY`, and `TOMCAT`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container to use. If specified `java_version` and `java_container` must also be specified.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of Java to use. If specified `java_container` and `java_container_version` must also be specified. Possible values are `1.7`, `1.8` and `11` and their specific versions - except for Java 11 (e.g. `1.7.0_80`, `1.8.0_181`, `11`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the App Service. Possible options are a Docker container (`DOCKER|<user/image:tag>`), a base-64 encoded Docker Compose file (`COMPOSE|${filebase64("compose.yml")}`) or a base-64 encoded Kubernetes Manifest (`KUBE|${filebase64("kubernetes.yml")}`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode. Possible values are `Integrated` and `Classic`. Defaults to `Integrated`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for the app service. Possible values are `1.0`, `1.1`, and `1.2`. Defaults to `1.2` for new app services.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP to use in this App Service. Possible values are `5.5`, `5.6`, `7.0`, `7.1`, `7.2`, and `7.3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of Python to use in this App Service. Possible values are `2.7` and `3.4`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled? Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio should the Remote Debugger be compatible with? Possible values are `VS2012`, `VS2013`, `VS2015` and `VS2017`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service. Defaults to `None`. Possible values are: `BitbucketGit`, `BitbucketHg`, `CodePlexGit`, `CodePlexHg`, `Dropbox`, `ExternalGit`, `ExternalHg`, `GitHub`, `LocalGit`, `None`, `OneDrive`, `Tfs`, `VSO`, and `VSTSRM`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Should the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Should WebSockets be enabled?
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Windows Docker container image (`DOCKER|<user/image:tag>`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Site<wbr>Config<wbr>Cors</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceSiteConfigCors">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceSiteConfigCors">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteConfigCorsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteConfigCorsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Support<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Are credentials supported?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Support<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Are credentials supported?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>support<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Are credentials supported?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of origins which should be able to make cross-origin calls. `*` can be used to allow all calls.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>support<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Are credentials supported?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceSiteConfigIpRestriction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceSiteConfigIpRestriction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteConfigIpRestrictionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteConfigIpRestrictionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Network Subnet ID used for this IP Restriction.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Network Subnet ID used for this IP Restriction.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Network Subnet ID used for this IP Restriction.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction in CIDR notation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Network Subnet ID used for this IP Restriction.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Site<wbr>Credential</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceSiteCredential">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSiteCredentialOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The password associated with the username, which can be used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The username which can be used to publish to this App Service
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The password associated with the username, which can be used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The username which can be used to publish to this App Service
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The password associated with the username, which can be used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The username which can be used to publish to this App Service
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The password associated with the username, which can be used to publish to this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The username which can be used to publish to this App Service
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Source<wbr>Control</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceSourceControl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceSourceControlOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Branch name of the Git repository for this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Repo<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the Git repository for this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Branch name of the Git repository for this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Repo<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the Git repository for this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Branch name of the Git repository for this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>repo<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}URL of the Git repository for this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Branch name of the Git repository for this App Service.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>repo<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}URL of the Git repository for this App Service.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>App<wbr>Service<wbr>Storage<wbr>Account</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#AppServiceStorageAccount">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#AppServiceStorageAccount">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceStorageAccountArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#AppServiceStorageAccountOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The access key for the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account identifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the file share (container name, for Blob storage).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of storage. Possible values are `AzureBlob` and `AzureFiles`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The path to mount the storage within the site's runtime environment.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The access key for the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account identifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the file share (container name, for Blob storage).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of storage. Possible values are `AzureBlob` and `AzureFiles`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to mount the storage within the site's runtime environment.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The access key for the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>account<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account identifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>share<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the file share (container name, for Blob storage).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of storage. Possible values are `AzureBlob` and `AzureFiles`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The path to mount the storage within the site's runtime environment.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The access key for the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>account_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the storage account identifier.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>share_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the file share (container name, for Blob storage).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of storage. Possible values are `AzureBlob` and `AzureFiles`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mount<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The path to mount the storage within the site's runtime environment.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`azurerm` Terraform Provider](https://github.com/terraform-providers/terraform-provider-azurerm).</dd>
</dl>

