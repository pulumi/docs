
---
title: "GetAppService"
block_external_search_index: true
---



Use this data source to access information about an existing App Service.

{{% examples %}}
{{% /examples %}}





## Using GetAppService {#using}

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getAppService<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/appservice/#GetAppServiceArgs">GetAppServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/appservice/#GetAppServiceResult">GetAppServiceResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_app_service(</span>name=None<span class="p">, </span>resource_group_name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupAppService<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#LookupAppServiceArgs">LookupAppServiceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#LookupAppServiceResult">LookupAppServiceResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetAppService </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Appservice.GetAppServiceResult.html">GetAppServiceResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.AppService.GetAppServiceArgs.html">GetAppServiceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the App Service exists.
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
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the App Service exists.
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
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the App Service exists.
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
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Name of the Resource Group where the App Service exists.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetAppService Result {#result}

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>App<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings for the App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappserviceconnectionstring">List&lt;Get<wbr>App<wbr>Service<wbr>Connection<wbr>String&gt;</a></span>
    </dt>
    <dd>{{% md %}}An `connection_string` block as defined below.
{{% /md %}}</dd>

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
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
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
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Site<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfig">List&lt;Get<wbr>App<wbr>Service<wbr>Site<wbr>Config&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesitecredential">List&lt;Get<wbr>App<wbr>Service<wbr>Site<wbr>Credential&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesourcecontrol">List&lt;Get<wbr>App<wbr>Service<wbr>Source<wbr>Control&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>App<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>App<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings for the App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappserviceconnectionstring">[]Get<wbr>App<wbr>Service<wbr>Connection<wbr>String</a></span>
    </dt>
    <dd>{{% md %}}An `connection_string` block as defined below.
{{% /md %}}</dd>

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
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
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
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Site<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfig">[]Get<wbr>App<wbr>Service<wbr>Site<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesitecredential">[]Get<wbr>App<wbr>Service<wbr>Site<wbr>Credential</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesourcecontrol">[]Get<wbr>App<wbr>Service<wbr>Source<wbr>Control</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>app<wbr>Service<wbr>Plan<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>app<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings for the App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Affinity<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client<wbr>Cert<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>Strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappserviceconnectionstring">Get<wbr>App<wbr>Service<wbr>Connection<wbr>String[]</a></span>
    </dt>
    <dd>{{% md %}}An `connection_string` block as defined below.
{{% /md %}}</dd>

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
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https<wbr>Only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
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
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>site<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfig">Get<wbr>App<wbr>Service<wbr>Site<wbr>Config[]</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>site<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesitecredential">Get<wbr>App<wbr>Service<wbr>Site<wbr>Credential[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesourcecontrol">Get<wbr>App<wbr>Service<wbr>Source<wbr>Control[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
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

    <dt class="property-"
            title="">
        <span>app_<wbr>service_<wbr>plan_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the App Service Plan within which the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>app_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A key-value pair of App Settings for the App Service.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>affinity_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service send session affinity cookies, which route client requests in the same session to the same instance?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>client_<wbr>cert_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service require client certificates for incoming requests?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>strings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappserviceconnectionstring">List[Get<wbr>App<wbr>Service<wbr>Connection<wbr>String]</a></span>
    </dt>
    <dd>{{% md %}}An `connection_string` block as defined below.
{{% /md %}}</dd>

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
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the App Service Enabled?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https_<wbr>only</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Can the App Service only be accessed via HTTPS?
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Azure location where the App Service exists.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the Connection String.
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
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>site_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfig">List[Get<wbr>App<wbr>Service<wbr>Site<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A `site_config` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>site_<wbr>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesitecredential">List[Get<wbr>App<wbr>Service<wbr>Site<wbr>Credential]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>controls</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesourcecontrol">List[Get<wbr>App<wbr>Service<wbr>Source<wbr>Control]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types


<h4 id="getappserviceconnectionstring">Get<wbr>App<wbr>Service<wbr>Connection<wbr>String</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAppServiceConnectionString">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#GetAppServiceConnectionString">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String.
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
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String.
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
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String.
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
    <dd>{{% md %}}The name of the App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of the Connection String.
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





<h4 id="getappservicesiteconfig">Get<wbr>App<wbr>Service<wbr>Site<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAppServiceSiteConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#GetAppServiceSiteConfig">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the app be loaded at all times?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigcor">List&lt;Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Cor<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigiprestriction">List&lt;Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_restriction` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Java in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Python used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled in this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio is the Remote Debugger compatible with?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Are WebSockets enabled for this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Windows Container Docker Image for the AppService.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the app be loaded at all times?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>App<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigcor">[]Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Cor</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigiprestriction">[]Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_restriction` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Java in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Python used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled in this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio is the Remote Debugger compatible with?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Are WebSockets enabled for this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Windows Container Docker Image for the AppService.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is the app be loaded at all times?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigcor">Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Cor[]</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigiprestriction">Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction[]</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_restriction` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Java in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The version of Python used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled in this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio is the Remote Debugger compatible with?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Are WebSockets enabled for this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Windows Container Docker Image for the AppService.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>always<wbr>On</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is the app be loaded at all times?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>app<wbr>Command<wbr>Line</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}App command line to launch.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>cors</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigcor">List[Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Cor]</a></span>
    </dt>
    <dd>{{% md %}}A `cors` block as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Documents</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The ordering of default documents to load, if an address isn't specified.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>dotnet<wbr>Framework<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of the .net framework's CLR used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ftps<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}State of FTP / FTPS service for this AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http2Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is HTTP2 Enabled on this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Restrictions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getappservicesiteconfigiprestriction">List[Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction]</a></span>
    </dt>
    <dd>{{% md %}}One or more `ip_restriction` blocks as defined above.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>java<wbr>Container</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>java<wbr>Container<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of the Java Container in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>java<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of Java in use.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>linux<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Linux App Framework and version for the AppService.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>local<wbr>Mysql<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is "MySQL In App" Enabled? This runs a local MySQL instance with your app and shares resources from the App Service plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>managed<wbr>Pipeline<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Managed Pipeline Mode used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>min<wbr>Tls<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The minimum supported TLS version for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>php<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of PHP used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>python<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The version of Python used in this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote<wbr>Debugging<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Is Remote Debugging Enabled in this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>remote<wbr>Debugging<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Which version of Visual Studio is the Remote Debugger compatible with?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scm<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of Source Control enabled for this App Service.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>use32Bit<wbr>Worker<wbr>Process</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Does the App Service run in 32 bit mode, rather than 64 bit mode?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>websockets<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Are WebSockets enabled for this App Service?
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>windows<wbr>Fx<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Windows Container Docker Image for the AppService.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getappservicesiteconfigcor">Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Cor</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAppServiceSiteConfigCor">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#GetAppServiceSiteConfigCor">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Allowed<wbr>Origins</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of origins which are able to make cross-origin calls.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
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
    <dd>{{% md %}}A list of origins which are able to make cross-origin calls.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
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
    <dd>{{% md %}}A list of origins which are able to make cross-origin calls.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
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
    <dd>{{% md %}}A list of origins which are able to make cross-origin calls.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>support<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Are credentials supported?
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getappservicesiteconfigiprestriction">Get<wbr>App<wbr>Service<wbr>Site<wbr>Config<wbr>Ip<wbr>Restriction</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAppServiceSiteConfigIpRestriction">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#GetAppServiceSiteConfigIpRestriction">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
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
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
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
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
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
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IP Address used for this IP Restriction.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Network<wbr>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getappservicesitecredential">Get<wbr>App<wbr>Service<wbr>Site<wbr>Credential</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAppServiceSiteCredential">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#GetAppServiceSiteCredential">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
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
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
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
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
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
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4 id="getappservicesourcecontrol">Get<wbr>App<wbr>Service<wbr>Source<wbr>Control</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#GetAppServiceSourceControl">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/v3/go/azure/appservice?tab=doc#GetAppServiceSourceControl">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Repo<wbr>Url</span>
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
        <span>Branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Repo<wbr>Url</span>
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
        <span>branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>repo<wbr>Url</span>
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
        <span>branch</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>repo<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}







