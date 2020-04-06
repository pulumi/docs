
---
title: "RouterInterface"
block_external_search_index: true
---






## Create a RouterInterface Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#RouterInterface">RouterInterface</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#RouterInterfaceArgs">RouterInterfaceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">RouterInterface</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>health_check_source_ip=None<span class="p">, </span>health_check_target_ip=None<span class="p">, </span>instance_charge_type=None<span class="p">, </span>name=None<span class="p">, </span>opposite_access_point_id=None<span class="p">, </span>opposite_region=None<span class="p">, </span>period=None<span class="p">, </span>role=None<span class="p">, </span>router_id=None<span class="p">, </span>router_type=None<span class="p">, </span>specification=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewRouterInterface<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#RouterInterfaceArgs">RouterInterfaceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#RouterInterface">RouterInterface</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.RouterInterface.html">RouterInterface</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.RouterInterfaceArgs.html">RouterInterfaceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>Opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>check_<wbr>source_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>check_<wbr>target_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite_<wbr>access_<wbr>point_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-required"
            title="Required">
        <span>opposite_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## RouterInterface Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>access_<wbr>point_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health_<wbr>check_<wbr>source_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>health_<wbr>check_<wbr>target_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite_<wbr>access_<wbr>point_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite_<wbr>interface_<wbr>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>opposite_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite_<wbr>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>opposite_<wbr>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing RouterInterface Resource

Get an existing RouterInterface resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#RouterInterfaceState">RouterInterfaceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/vpc/#RouterInterface">RouterInterface</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>access_point_id=None<span class="p">, </span>description=None<span class="p">, </span>health_check_source_ip=None<span class="p">, </span>health_check_target_ip=None<span class="p">, </span>instance_charge_type=None<span class="p">, </span>name=None<span class="p">, </span>opposite_access_point_id=None<span class="p">, </span>opposite_interface_id=None<span class="p">, </span>opposite_interface_owner_id=None<span class="p">, </span>opposite_region=None<span class="p">, </span>opposite_router_id=None<span class="p">, </span>opposite_router_type=None<span class="p">, </span>period=None<span class="p">, </span>role=None<span class="p">, </span>router_id=None<span class="p">, </span>router_type=None<span class="p">, </span>specification=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetRouterInterface<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#RouterInterfaceState">RouterInterfaceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/vpc?tab=doc#RouterInterface">RouterInterface</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.RouterInterface.html">RouterInterface</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Vpc.RouterInterfaceState.html">RouterInterfaceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Check<wbr>Source<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health<wbr>Check<wbr>Target<wbr>Ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite<wbr>Access<wbr>Point<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite<wbr>Interface<wbr>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>opposite<wbr>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite<wbr>Router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite<wbr>Router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>access_<wbr>point_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the router interface. It can be 2-256 characters long or left blank. It cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>check_<wbr>source_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Source IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_target_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>health_<wbr>check_<wbr>target_<wbr>ip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used as the Packet Target IP of health check for disaster recovery or ECMP. It is only valid when `router_type` is `VBR`. The IP must be an unused IP in the local VPC. It and `health_check_source_ip` must be specified at the same time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The billing method of the router interface. Valid values are "PrePaid" and "PostPaid". Default to "PostPaid". Router Interface doesn't support "PrePaid" when region and opposite_region are the same.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the router interface. Length must be 2-80 characters long. Only Chinese characters, English letters, numbers, period (.), underline (_), or dash (-) are permitted.
If it is not specified, the default value is interface ID. The name cannot start with http:// and https://.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite_<wbr>access_<wbr>point_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_access_point_id&#39; has been deprecated from version 1.11.0.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite_<wbr>interface_<wbr>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_interface_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_interface_owner_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_interface_owner_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>opposite_<wbr>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Region of peer side.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite_<wbr>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection's 'opposite_router_id' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_id&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_id&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>opposite_<wbr>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.11.0. resource alicloud_router_interface_connection's 'opposite_router_type' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;opposite_router_type&#39; has been deprecated from version 1.11.0. Use resource alicloud_router_interface_connection&#39;s &#39;opposite_router_type&#39; instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy the resource, in month. It is valid when `instance_charge_type` is `PrePaid`. Default to 1. Valid values: [1-9, 12, 24, 36]. At present, the provider does not support modify "period" and you can do that via web console.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The role the router interface plays. Optional value: `InitiatingSide`, `AcceptingSide`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Router ID.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>router_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Router Type. Optional value: VRouter, VBR. Accepting side router interface type only be VRouter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specification of router interfaces. It is valid when `role` is `InitiatingSide`. Accepting side's role is default to set as 'Negative'. For more about the specification, refer to [Router interface specification](https://www.alibabacloud.com/help/doc-detail/36037.htm).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

