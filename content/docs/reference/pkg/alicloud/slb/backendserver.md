
---
title: "BackendServer"
block_external_search_index: true
---



Add a group of backend servers (ECS or ENI instance) to the Server Load Balancer or remove them from it.

> **NOTE:** Available in 1.53.0+

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as alicloud from "@pulumi/alicloud";

const config = new pulumi.Config();
const name = config.get("name") || "slbbackendservertest";

const defaultZones = pulumi.output(alicloud.getZones({
    availableDiskCategory: "cloud_efficiency",
    availableResourceCreation: "VSwitch",
}, { async: true }));
const defaultInstanceTypes = defaultZones.apply(defaultZones => alicloud.ecs.getInstanceTypes({
    availabilityZone: defaultZones.zones[0].id,
    cpuCoreCount: 1,
    memorySize: 2,
}, { async: true }));
const defaultImages = pulumi.output(alicloud.ecs.getImages({
    mostRecent: true,
    nameRegex: "^ubuntu_18.*64",
    owners: "system",
}, { async: true }));
const defaultNetwork = new alicloud.vpc.Network("default", {
    cidrBlock: "172.16.0.0/16",
});
const defaultSwitch = new alicloud.vpc.Switch("default", {
    availabilityZone: defaultZones.zones[0].id,
    cidrBlock: "172.16.0.0/16",
    vpcId: defaultNetwork.id,
});
const defaultSecurityGroup = new alicloud.ecs.SecurityGroup("default", {
    vpcId: defaultNetwork.id,
});
const defaultInstance: alicloud.ecs.Instance[] = [];
for (let i = 0; i < 2; i++) {
    defaultInstance.push(new alicloud.ecs.Instance(`default-${i}`, {
        availabilityZone: defaultZones.zones[0].id,
        imageId: defaultImages.images[0].id,
        instanceChargeType: "PostPaid",
        instanceName: name,
        instanceType: defaultInstanceTypes.instanceTypes[0].id,
        internetChargeType: "PayByTraffic",
        internetMaxBandwidthOut: 10,
        securityGroups: defaultSecurityGroup.id,
        systemDiskCategory: "cloud_efficiency",
        vswitchId: defaultSwitch.id,
    }));
}
const defaultLoadBalancer = new alicloud.slb.LoadBalancer("default", {
    vswitchId: defaultSwitch.id,
});
const defaultBackendServer = new alicloud.slb.BackendServer("default", {
    backendServers: [
        {
            serverId: defaultInstance[0].id,
            weight: 100,
        },
        {
            serverId: defaultInstance[1].id,
            weight: 100,
        },
    ],
    loadBalancerId: defaultLoadBalancer.id,
});
```

## Block servers

The servers mapping supports the following:

* `server_id` - (Required) A list backend server ID (ECS instance ID).
* `weight` - (Optional) Weight of the backend server. Valid value range: [0-100]. 
* `type` - (Optional) Type of the backend server. Valid value ecs, eni. Default to eni.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/slb_backend_server.html.markdown.



## Create a BackendServer Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#BackendServer">BackendServer</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#BackendServerArgs">BackendServerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BackendServer</span><span class="p">(resource_name, opts=None, </span>backend_servers=None<span class="p">, </span>delete_protection_validation=None<span class="p">, </span>load_balancer_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBackendServer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#BackendServerArgs">BackendServerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#BackendServer">BackendServer</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.BackendServer.html">BackendServer</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.BackendServerArgs.html">BackendServerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">List&lt;Backend<wbr>Server<wbr>Backend<wbr>Server<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">[]Backend<wbr>Server<wbr>Backend<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">Backend<wbr>Server<wbr>Backend<wbr>Server[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend_<wbr>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">List[Backend<wbr>Server<wbr>Backend<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>protection_<wbr>validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## BackendServer Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">List&lt;Backend<wbr>Server<wbr>Backend<wbr>Server&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">[]Backend<wbr>Server<wbr>Backend<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">Backend<wbr>Server<wbr>Backend<wbr>Server[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>backend_<wbr>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">List[Backend<wbr>Server<wbr>Backend<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>delete_<wbr>protection_<wbr>validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing BackendServer Resource

Get an existing BackendServer resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#BackendServerState">BackendServerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/slb/#BackendServer">BackendServer</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>backend_servers=None<span class="p">, </span>delete_protection_validation=None<span class="p">, </span>load_balancer_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBackendServer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#BackendServerState">BackendServerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#BackendServer">BackendServer</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.BackendServer.html">BackendServer</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Slb.BackendServerState.html">BackendServerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">List&lt;Backend<wbr>Server<wbr>Backend<wbr>Server<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">[]Backend<wbr>Server<wbr>Backend<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend<wbr>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">Backend<wbr>Server<wbr>Backend<wbr>Server[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Protection<wbr>Validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancer<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>backend_<wbr>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#backendserverbackendserver">List[Backend<wbr>Server<wbr>Backend<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of instances to added backend server in the SLB. It contains three sub-fields as `Block server` follows.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>protection_<wbr>validation</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load_<wbr>balancer_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the load balancer.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Backend<wbr>Server<wbr>Backend<wbr>Server</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#BackendServerBackendServer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#BackendServerBackendServer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#BackendServerBackendServerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/slb?tab=doc#BackendServerBackendServerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>server<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>weight</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

