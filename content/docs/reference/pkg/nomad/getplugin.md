
---
title: "getPlugin"
title_tag: "nomad.getPlugin"
meta_desc: "Documentation for the nomad.getPlugin function with examples, input properties, output properties, and supporting types."
---



<!-- WARNING: this file was generated by Pulumi Docs Generator. -->
<!-- Do not edit by hand unless you're certain you know what you are doing! -->

Lookup a plugin by ID. The aim of this datasource is to determine whether
a particular plugin exists on the cluster, to find information on the health
and availability of the plugin, and to optionally wait for the plugin
before performing actions the require an available plugin controller.

If a plugin with the specified ID does not exist and the datasource is not
configured to wait, it will result in an error. For simple existence checks,
use the `nomad.getPlugins` listing datasource.


{{% examples %}}

## Example Usage

{{< chooser language "typescript,python,go,csharp" / >}}





{{< example csharp >}}

```csharp
using Pulumi;
using Nomad = Pulumi.Nomad;

class MyStack : Stack
{
    public MyStack()
    {
        var ebs = Output.Create(Nomad.GetPlugin.InvokeAsync(new Nomad.GetPluginArgs
        {
            PluginId = "aws-ebs0",
            WaitForHealthy = true,
        }));
    }

}
```


{{< /example >}}


{{< example go >}}

```go
package main

import (
	"github.com/pulumi/pulumi-nomad/sdk/go/nomad"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		opt0 := true
		_, err := nomad.GetPlugin(ctx, &nomad.GetPluginArgs{
			PluginId:       "aws-ebs0",
			WaitForHealthy: &opt0,
		}, nil)
		if err != nil {
			return err
		}
		return nil
	})
}
```


{{< /example >}}


{{< example python >}}

```python
import pulumi
import pulumi_nomad as nomad

ebs = nomad.get_plugin(plugin_id="aws-ebs0",
    wait_for_healthy=True)
```


{{< /example >}}


{{< example typescript >}}


```typescript
import * as pulumi from "@pulumi/pulumi";
import * as nomad from "@pulumi/nomad";

const ebs = pulumi.output(nomad.getPlugin({
    pluginId: "aws-ebs0",
    waitForHealthy: true,
}));
```


{{< /example >}}





{{% /examples %}}




## Using getPlugin {#using}

{{< chooser language "typescript,python,go,csharp" / >}}


{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getPlugin<span class="p">(</span><span class="nx">args</span><span class="p">:</span> <span class="nx">GetPluginArgs</span><span class="p">,</span> <span class="nx">opts</span><span class="p">?:</span> <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="#result">GetPluginResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span>get_plugin(</span><span class="nx">plugin_id</span><span class="p">:</span> <span class="nx">Optional[str]</span> = None<span class="p">,</span>
               <span class="nx">wait_for_healthy</span><span class="p">:</span> <span class="nx">Optional[bool]</span> = None<span class="p">,</span>
               <span class="nx">wait_for_registration</span><span class="p">:</span> <span class="nx">Optional[bool]</span> = None<span class="p">,</span>
               <span class="nx">opts</span><span class="p">:</span> <span class="nx"><a href="/docs/reference/pkg/python/pulumi/#pulumi.InvokeOptions">Optional[InvokeOptions]</a></span> = None<span class="p">) -&gt;</span> GetPluginResult</code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetPlugin<span class="p">(</span><span class="nx">ctx</span><span class="p"> *</span><span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">,</span> <span class="nx">args</span><span class="p"> *</span><span class="nx">GetPluginArgs</span><span class="p">,</span> <span class="nx">opts</span><span class="p"> ...</span><span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="#result">GetPluginResult</a></span>, error)</span></code></pre></div>

> Note: This function is named `GetPlugin` in the Go SDK.

{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetPlugin </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="#result">GetPluginResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx">GetPluginArgs</span><span class="p"> </span><span class="nx">args<span class="p">,</span> <span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span><span class="p">? </span><span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:


{{% choosable language csharp %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="pluginid_csharp">
<a href="#pluginid_csharp" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="waitforhealthy_csharp">
<a href="#waitforhealthy_csharp" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="waitforregistration_csharp">
<a href="#waitforregistration_csharp" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="pluginid_go">
<a href="#pluginid_go" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="waitforhealthy_go">
<a href="#waitforhealthy_go" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="waitforregistration_go">
<a href="#waitforregistration_go" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language nodejs %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="pluginid_nodejs">
<a href="#pluginid_nodejs" style="color: inherit; text-decoration: inherit;">plugin<wbr>Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="waitforhealthy_nodejs">
<a href="#waitforhealthy_nodejs" style="color: inherit; text-decoration: inherit;">wait<wbr>For<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="waitforregistration_nodejs">
<a href="#waitforregistration_nodejs" style="color: inherit; text-decoration: inherit;">wait<wbr>For<wbr>Registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="plugin_id_python">
<a href="#plugin_id_python" style="color: inherit; text-decoration: inherit;">plugin_<wbr>id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="wait_for_healthy_python">
<a href="#wait_for_healthy_python" style="color: inherit; text-decoration: inherit;">wait_<wbr>for_<wbr>healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-optional"
            title="Optional">
        <span id="wait_for_registration_python">
<a href="#wait_for_registration_python" style="color: inherit; text-decoration: inherit;">wait_<wbr>for_<wbr>registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}




## getPlugin Result {#result}

The following output properties are available:



{{% choosable language csharp %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="controllerrequired_csharp">
<a href="#controllerrequired_csharp" style="color: inherit; text-decoration: inherit;">Controller<wbr>Required</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllersexpected_csharp">
<a href="#controllersexpected_csharp" style="color: inherit; text-decoration: inherit;">Controllers<wbr>Expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllershealthy_csharp">
<a href="#controllershealthy_csharp" style="color: inherit; text-decoration: inherit;">Controllers<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_csharp">
<a href="#id_csharp" style="color: inherit; text-decoration: inherit;">Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodes_csharp">
<a href="#nodes_csharp" style="color: inherit; text-decoration: inherit;">Nodes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpluginnode">List&lt;Get<wbr>Plugin<wbr>Node&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodesexpected_csharp">
<a href="#nodesexpected_csharp" style="color: inherit; text-decoration: inherit;">Nodes<wbr>Expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodeshealthy_csharp">
<a href="#nodeshealthy_csharp" style="color: inherit; text-decoration: inherit;">Nodes<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginid_csharp">
<a href="#pluginid_csharp" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginprovider_csharp">
<a href="#pluginprovider_csharp" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Provider</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginproviderversion_csharp">
<a href="#pluginproviderversion_csharp" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Provider<wbr>Version</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="waitforhealthy_csharp">
<a href="#waitforhealthy_csharp" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="waitforregistration_csharp">
<a href="#waitforregistration_csharp" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="controllerrequired_go">
<a href="#controllerrequired_go" style="color: inherit; text-decoration: inherit;">Controller<wbr>Required</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllersexpected_go">
<a href="#controllersexpected_go" style="color: inherit; text-decoration: inherit;">Controllers<wbr>Expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllershealthy_go">
<a href="#controllershealthy_go" style="color: inherit; text-decoration: inherit;">Controllers<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_go">
<a href="#id_go" style="color: inherit; text-decoration: inherit;">Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodes_go">
<a href="#nodes_go" style="color: inherit; text-decoration: inherit;">Nodes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpluginnode">[]Get<wbr>Plugin<wbr>Node</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodesexpected_go">
<a href="#nodesexpected_go" style="color: inherit; text-decoration: inherit;">Nodes<wbr>Expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodeshealthy_go">
<a href="#nodeshealthy_go" style="color: inherit; text-decoration: inherit;">Nodes<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginid_go">
<a href="#pluginid_go" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginprovider_go">
<a href="#pluginprovider_go" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Provider</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginproviderversion_go">
<a href="#pluginproviderversion_go" style="color: inherit; text-decoration: inherit;">Plugin<wbr>Provider<wbr>Version</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="waitforhealthy_go">
<a href="#waitforhealthy_go" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="waitforregistration_go">
<a href="#waitforregistration_go" style="color: inherit; text-decoration: inherit;">Wait<wbr>For<wbr>Registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language nodejs %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="controllerrequired_nodejs">
<a href="#controllerrequired_nodejs" style="color: inherit; text-decoration: inherit;">controller<wbr>Required</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllersexpected_nodejs">
<a href="#controllersexpected_nodejs" style="color: inherit; text-decoration: inherit;">controllers<wbr>Expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllershealthy_nodejs">
<a href="#controllershealthy_nodejs" style="color: inherit; text-decoration: inherit;">controllers<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_nodejs">
<a href="#id_nodejs" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodes_nodejs">
<a href="#nodes_nodejs" style="color: inherit; text-decoration: inherit;">nodes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpluginnode">Get<wbr>Plugin<wbr>Node[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodesexpected_nodejs">
<a href="#nodesexpected_nodejs" style="color: inherit; text-decoration: inherit;">nodes<wbr>Expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodeshealthy_nodejs">
<a href="#nodeshealthy_nodejs" style="color: inherit; text-decoration: inherit;">nodes<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginid_nodejs">
<a href="#pluginid_nodejs" style="color: inherit; text-decoration: inherit;">plugin<wbr>Id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginprovider_nodejs">
<a href="#pluginprovider_nodejs" style="color: inherit; text-decoration: inherit;">plugin<wbr>Provider</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="pluginproviderversion_nodejs">
<a href="#pluginproviderversion_nodejs" style="color: inherit; text-decoration: inherit;">plugin<wbr>Provider<wbr>Version</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="waitforhealthy_nodejs">
<a href="#waitforhealthy_nodejs" style="color: inherit; text-decoration: inherit;">wait<wbr>For<wbr>Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="waitforregistration_nodejs">
<a href="#waitforregistration_nodejs" style="color: inherit; text-decoration: inherit;">wait<wbr>For<wbr>Registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties"><dt class="property-"
            title="">
        <span id="controller_required_python">
<a href="#controller_required_python" style="color: inherit; text-decoration: inherit;">controller_<wbr>required</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllers_expected_python">
<a href="#controllers_expected_python" style="color: inherit; text-decoration: inherit;">controllers_<wbr>expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="controllers_healthy_python">
<a href="#controllers_healthy_python" style="color: inherit; text-decoration: inherit;">controllers_<wbr>healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="id_python">
<a href="#id_python" style="color: inherit; text-decoration: inherit;">id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The provider-assigned unique ID for this managed resource.
{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodes_python">
<a href="#nodes_python" style="color: inherit; text-decoration: inherit;">nodes</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getpluginnode">Sequence[Get<wbr>Plugin<wbr>Node]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodes_expected_python">
<a href="#nodes_expected_python" style="color: inherit; text-decoration: inherit;">nodes_<wbr>expected</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="nodes_healthy_python">
<a href="#nodes_healthy_python" style="color: inherit; text-decoration: inherit;">nodes_<wbr>healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="plugin_id_python">
<a href="#plugin_id_python" style="color: inherit; text-decoration: inherit;">plugin_<wbr>id</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="plugin_provider_python">
<a href="#plugin_provider_python" style="color: inherit; text-decoration: inherit;">plugin_<wbr>provider</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="plugin_provider_version_python">
<a href="#plugin_provider_version_python" style="color: inherit; text-decoration: inherit;">plugin_<wbr>provider_<wbr>version</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="wait_for_healthy_python">
<a href="#wait_for_healthy_python" style="color: inherit; text-decoration: inherit;">wait_<wbr>for_<wbr>healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-"
            title="">
        <span id="wait_for_registration_python">
<a href="#wait_for_registration_python" style="color: inherit; text-decoration: inherit;">wait_<wbr>for_<wbr>registration</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}




## Supporting Types


<h4 id="getpluginnode">Get<wbr>Plugin<wbr>Node</h4>



{{% choosable language csharp %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="healthy_csharp">
<a href="#healthy_csharp" style="color: inherit; text-decoration: inherit;">Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="healthydescription_csharp">
<a href="#healthydescription_csharp" style="color: inherit; text-decoration: inherit;">Healthy<wbr>Description</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="name_csharp">
<a href="#name_csharp" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language go %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="healthy_go">
<a href="#healthy_go" style="color: inherit; text-decoration: inherit;">Healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="healthydescription_go">
<a href="#healthydescription_go" style="color: inherit; text-decoration: inherit;">Healthy<wbr>Description</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="name_go">
<a href="#name_go" style="color: inherit; text-decoration: inherit;">Name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language nodejs %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="healthy_nodejs">
<a href="#healthy_nodejs" style="color: inherit; text-decoration: inherit;">healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="healthydescription_nodejs">
<a href="#healthydescription_nodejs" style="color: inherit; text-decoration: inherit;">healthy<wbr>Description</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="name_nodejs">
<a href="#name_nodejs" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties"><dt class="property-required"
            title="Required">
        <span id="healthy_python">
<a href="#healthy_python" style="color: inherit; text-decoration: inherit;">healthy</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="healthy_description_python">
<a href="#healthy_description_python" style="color: inherit; text-decoration: inherit;">healthy_<wbr>description</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd><dt class="property-required"
            title="Required">
        <span id="name_python">
<a href="#name_python" style="color: inherit; text-decoration: inherit;">name</a>
</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd></dl>
{{% /choosable %}}





<h2 id="package-details">Package Details</h2>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-nomad">https://github.com/pulumi/pulumi-nomad</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
	<dt>Notes</dt>
	<dd>{{% md %}}This Pulumi package is based on the [`nomad` Terraform Provider](https://github.com/hashicorp/terraform-provider-nomad).{{% /md %}}</dd>
</dl>

