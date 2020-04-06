
---
title: "CloudCredential"
block_external_search_index: true
---



Provides a Rancher v2 Cloud Credential resource. This can be used to create Cloud Credential for Rancher v2.2.x and retrieve their information.

amazonec2, azure, digitalocean, openstack and vsphere credentials config are supported for Cloud Credential.

> This content is derived from https://github.com/terraform-providers/terraform-provider-rancher2/blob/master/website/docs/r/cloudCredential.html.markdown.



## Create a CloudCredential Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#CloudCredential">CloudCredential</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#CloudCredentialArgs">CloudCredentialArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">CloudCredential</span><span class="p">(resource_name, opts=None, </span>amazonec2_credential_config=None<span class="p">, </span>annotations=None<span class="p">, </span>azure_credential_config=None<span class="p">, </span>description=None<span class="p">, </span>digitalocean_credential_config=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>openstack_credential_config=None<span class="p">, </span>vsphere_credential_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCloudCredential<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialArgs">CloudCredentialArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredential">CloudCredential</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..CloudCredential.html">CloudCredential</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2.CloudCredentialArgs.html">CloudCredentialArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">*Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">*Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">*Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">*Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">*Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>amazonec2_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Dict[Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Dict[Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>digitalocean_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Dict[Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openstack_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Dict[Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Dict[Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## CloudCredential Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">*Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">*Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">*Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">*Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">*Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>amazonec2_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Dict[Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>azure_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Dict[Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>digitalocean_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Dict[Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>openstack_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Dict[Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vsphere_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Dict[Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing CloudCredential Resource

Get an existing CloudCredential resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#CloudCredentialState">CloudCredentialState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rancher2/#CloudCredential">CloudCredential</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>amazonec2_credential_config=None<span class="p">, </span>annotations=None<span class="p">, </span>azure_credential_config=None<span class="p">, </span>description=None<span class="p">, </span>digitalocean_credential_config=None<span class="p">, </span>driver=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>openstack_credential_config=None<span class="p">, </span>vsphere_credential_config=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCloudCredential<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialState">CloudCredentialState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredential">CloudCredential</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..CloudCredential.html">CloudCredential</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rancher2/Pulumi.Rancher2..CloudCredentialState.html">CloudCredentialState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">*Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">*Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">*Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">*Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">*Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>amazonec2Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>digitalocean<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openstack<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere<wbr>Credential<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>amazonec2_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialamazonec2credentialconfig">Dict[Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}AWS config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>annotations</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Annotations for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>azure_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialazurecredentialconfig">Dict[Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Azure config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description for the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>digitalocean_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialdigitaloceancredentialconfig">Dict[Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}DigitalOcean config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>driver</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}(Computed) The driver of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Labels for Cloud Credential object (map)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the Cloud Credential (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>openstack_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialopenstackcredentialconfig">Dict[Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}OpenStack config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vsphere_<wbr>credential_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#cloudcredentialvspherecredentialconfig">Dict[Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}vSphere config for the Cloud Credential (list maxitems:1)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Cloud<wbr>Credential<wbr>Amazonec2Credential<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#CloudCredentialAmazonec2CredentialConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#CloudCredentialAmazonec2CredentialConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialAmazonec2CredentialConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialAmazonec2CredentialConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS access key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secret<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS secret key (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS access key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Secret<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS secret key (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS access key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secret<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS secret key (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AWS access key (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>secret_<wbr>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AWS secret key (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cloud<wbr>Credential<wbr>Azure<wbr>Credential<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#CloudCredentialAzureCredentialConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#CloudCredentialAzureCredentialConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialAzureCredentialConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialAzureCredentialConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account ID (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Subscription ID (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account ID (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Subscription ID (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account ID (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client<wbr>Secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Azure Subscription ID (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account ID (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>client_<wbr>secret</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Azure Service Principal Account password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subscription<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Azure Subscription ID (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cloud<wbr>Credential<wbr>Digitalocean<wbr>Credential<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#CloudCredentialDigitaloceanCredentialConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#CloudCredentialDigitaloceanCredentialConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialDigitaloceanCredentialConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialDigitaloceanCredentialConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DigitalOcean access token (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Access<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DigitalOcean access token (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DigitalOcean access token (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>access<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DigitalOcean access token (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cloud<wbr>Credential<wbr>Openstack<wbr>Credential<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#CloudCredentialOpenstackCredentialConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#CloudCredentialOpenstackCredentialConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialOpenstackCredentialConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialOpenstackCredentialConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Cloud<wbr>Credential<wbr>Vsphere<wbr>Credential<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/input/#CloudCredentialVsphereCredentialConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rancher2/types/output/#CloudCredentialVsphereCredentialConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialVsphereCredentialConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rancher2/sdk/go/rancher2/?tab=doc#CloudCredentialVsphereCredentialConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere username (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vcenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere IP/hostname for vCenter (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vcenter<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}vSphere Port for vCenter. Default `443` (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere username (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vcenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere IP/hostname for vCenter (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vcenter<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}vSphere Port for vCenter. Default `443` (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere username (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vcenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}vSphere IP/hostname for vCenter (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vcenter<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}vSphere Port for vCenter. Default `443` (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}vSphere password (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}vSphere username (string)
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vcenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}vSphere IP/hostname for vCenter (string)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vcenter<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}vSphere Port for vCenter. Default `443` (string)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-rancher2">https://github.com/pulumi/pulumi-rancher2</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

