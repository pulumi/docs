
---
title: "Registry"
block_external_search_index: true
---

 Creates a device registry in Google's Cloud IoT Core platform. For more information see
[the official documentation](https://cloud.google.com/iot/docs/) and
[API](https://cloud.google.com/iot/docs/reference/cloudiot/rest/v1/projects.locations.registries).

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudiot_registry.html.markdown.



## Create a Registry Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#Registry">Registry</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#RegistryArgs">RegistryArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Registry</span><span class="p">(resource_name, opts=None, </span>credentials=None<span class="p">, </span>event_notification_configs=None<span class="p">, </span>http_config=None<span class="p">, </span>log_level=None<span class="p">, </span>mqtt_config=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>state_notification_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRegistry<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryArgs">RegistryArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#Registry">Registry</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.Registry.html">Registry</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.Inputs.RegistryArgs.html">RegistryArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">List&lt;Registry<wbr>Credential<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">List&lt;Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Registry<wbr>State<wbr>Notification<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">[]Registry<wbr>Credential</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">[]Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">*Registry<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">*Registry<wbr>Mqtt<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">*Registry<wbr>State<wbr>Notification<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">Registry<wbr>Credential[]?</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item[]?</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Registry<wbr>State<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">List[Registry<wbr>Credential]</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>notification_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">List[Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item]</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Dict[Registry<wbr>Http<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mqtt_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Dict[Registry<wbr>Mqtt<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state_<wbr>notification_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Dict[Registry<wbr>State<wbr>Notification<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Registry Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">List&lt;Registry<wbr>Credential&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">List&lt;Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Registry<wbr>State<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">[]Registry<wbr>Credential</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">[]Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>State<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">*Registry<wbr>State<wbr>Notification<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">Registry<wbr>Credential[]?</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item[]</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Registry<wbr>State<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">List[Registry<wbr>Credential]</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event_<wbr>notification_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">List[Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item]</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Dict[Registry<wbr>Http<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>mqtt_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Dict[Registry<wbr>Mqtt<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>state_<wbr>notification_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Dict[Registry<wbr>State<wbr>Notification<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Registry Resource

Get an existing Registry resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#RegistryState">RegistryState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/kms/#Registry">Registry</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>credentials=None<span class="p">, </span>event_notification_configs=None<span class="p">, </span>http_config=None<span class="p">, </span>log_level=None<span class="p">, </span>mqtt_config=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>state_notification_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRegistry<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryState">RegistryState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#Registry">Registry</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.Registry.html">Registry</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Kms.RegistryState.html">RegistryState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">List&lt;Registry<wbr>Credential<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">List&lt;Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Registry<wbr>State<wbr>Notification<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">[]Registry<wbr>Credential</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">[]Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">*Registry<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">*Registry<wbr>Mqtt<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>State<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">*Registry<wbr>State<wbr>Notification<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">Registry<wbr>Credential[]?</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Notification<wbr>Configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item[]?</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Registry<wbr>Http<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Level</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mqtt<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Registry<wbr>Mqtt<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state<wbr>Notification<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Registry<wbr>State<wbr>Notification<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredential">List[Registry<wbr>Credential]</a></span>
    </dt>
    <dd>{{% md %}}List of public key certificates to authenticate devices. Structure is documented below. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>notification_<wbr>configs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryeventnotificationconfigitem">List[Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item]</a></span>
    </dt>
    <dd>{{% md %}}List of configurations for event notification, such as
PubSub topics to publish device events to. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registryhttpconfig">Dict[Registry<wbr>Http<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate HTTP. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>level</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mqtt_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrymqttconfig">Dict[Registry<wbr>Mqtt<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Activate or deactivate MQTT. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The project in which the resource belongs. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Region in which the created address should reside. If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>state_<wbr>notification_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrystatenotificationconfig">Dict[Registry<wbr>State<wbr>Notification<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}A PubSub topic to publish device state updates. Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Registry<wbr>Credential</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RegistryCredential">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RegistryCredential">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryCredentialArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryCredentialOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredentialpublickeycertificate">Registry<wbr>Credential<wbr>Public<wbr>Key<wbr>Certificate<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The certificate format and data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Public<wbr>Key<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredentialpublickeycertificate">Registry<wbr>Credential<wbr>Public<wbr>Key<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}The certificate format and data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Key<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredentialpublickeycertificate">Registry<wbr>Credential<wbr>Public<wbr>Key<wbr>Certificate</a></span>
    </dt>
    <dd>{{% md %}}The certificate format and data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>public<wbr>Key<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#registrycredentialpublickeycertificate">Dict[Registry<wbr>Credential<wbr>Public<wbr>Key<wbr>Certificate]</a></span>
    </dt>
    <dd>{{% md %}}The certificate format and data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Registry<wbr>Credential<wbr>Public<wbr>Key<wbr>Certificate</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RegistryCredentialPublicKeyCertificate">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RegistryCredentialPublicKeyCertificate">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryCredentialPublicKeyCertificateArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryCredentialPublicKeyCertificateOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certificate data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows only  `X509_CERTIFICATE_PEM`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certificate data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows only  `X509_CERTIFICATE_PEM`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The certificate data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows only  `X509_CERTIFICATE_PEM`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The certificate data.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field allows only  `X509_CERTIFICATE_PEM`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Registry<wbr>Event<wbr>Notification<wbr>Config<wbr>Item</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RegistryEventNotificationConfigItem">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RegistryEventNotificationConfigItem">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryEventNotificationConfigItemArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryEventNotificationConfigItemOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Pubsub<wbr>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subfolder<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If the subfolder name matches this string
exactly, this configuration will be used. The string must not include the
leading '/' character. If empty, all strings are matched. Empty value can
only be used for the last `event_notification_configs` item.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Pubsub<wbr>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subfolder<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If the subfolder name matches this string
exactly, this configuration will be used. The string must not include the
leading '/' character. If empty, all strings are matched. Empty value can
only be used for the last `event_notification_configs` item.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>pubsub<wbr>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subfolder<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If the subfolder name matches this string
exactly, this configuration will be used. The string must not include the
leading '/' character. If empty, all strings are matched. Empty value can
only be used for the last `event_notification_configs` item.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>pubsub_<wbr>topic_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subfolder<wbr>Matches</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If the subfolder name matches this string
exactly, this configuration will be used. The string must not include the
leading '/' character. If empty, all strings are matched. Empty value can
only be used for the last `event_notification_configs` item.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Registry<wbr>Http<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RegistryHttpConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RegistryHttpConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryHttpConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryHttpConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Enabled<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows `HTTP_ENABLED` or `HTTP_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Enabled<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows `HTTP_ENABLED` or `HTTP_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Enabled<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows `HTTP_ENABLED` or `HTTP_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>http_<wbr>enabled_<wbr>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field allows `HTTP_ENABLED` or `HTTP_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Registry<wbr>Mqtt<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RegistryMqttConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RegistryMqttConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryMqttConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryMqttConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Mqtt<wbr>Enabled<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows `MQTT_ENABLED` or `MQTT_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Mqtt<wbr>Enabled<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows `MQTT_ENABLED` or `MQTT_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>mqtt<wbr>Enabled<wbr>State</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field allows `MQTT_ENABLED` or `MQTT_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>mqtt_<wbr>enabled_<wbr>state</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field allows `MQTT_ENABLED` or `MQTT_DISABLED`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Registry<wbr>State<wbr>Notification<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#RegistryStateNotificationConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#RegistryStateNotificationConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryStateNotificationConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/kms?tab=doc#RegistryStateNotificationConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Pubsub<wbr>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Pubsub<wbr>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>pubsub<wbr>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>pubsub_<wbr>topic_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}PubSub topic name to publish device state updates.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







