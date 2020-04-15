
---
title: "GetAutopilotHealth"
block_external_search_index: true
---



The `consul..getAutopilotHealth` data source returns
[autopilot health information](https://www.consul.io/api/operator/autopilot.html#read-health)
about the current Consul cluster.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as consul from "@pulumi/consul";

const read = pulumi.output(consul.getAutopilotHealth({ async: true }));

export const health = read.healthy;
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-consul/blob/master/website/docs/d/autopilot_health.html.markdown.





## Using GetAutopilotHealth

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getAutopilotHealth<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/consul/#GetAutopilotHealthArgs">GetAutopilotHealthArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/consul/#GetAutopilotHealthResult">GetAutopilotHealthResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_autopilot_health(</span>datacenter=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupAutopilotHealth<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetAutopilotHealthArgs">GetAutopilotHealthArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#LookupAutopilotHealthResult">LookupAutopilotHealthResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetAutopilotHealth </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.GetAutopilotHealthResult.html">GetAutopilotHealthResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Consul/Pulumi.Consul.GetAutopilotHealthArgs.html">GetAutopilotHealthArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The datacenter to use. This overrides the agent's
default datacenter and the datacenter in the provider setup.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The datacenter to use. This overrides the agent's
default datacenter and the datacenter in the provider setup.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The datacenter to use. This overrides the agent's
default datacenter and the datacenter in the provider setup.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The datacenter to use. This overrides the agent's
default datacenter and the datacenter in the provider setup.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetAutopilotHealth Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Failure<wbr>Tolerance</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of redundant healthy servers that could fail
without causing an outage
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

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
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getautopilothealthserver">List&lt;Get<wbr>Autopilot<wbr>Health<wbr>Server&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of server health information. See below for details on the
available information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Failure<wbr>Tolerance</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of redundant healthy servers that could fail
without causing an outage
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

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
        <span>Servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getautopilothealthserver">[]Get<wbr>Autopilot<wbr>Health<wbr>Server</a></span>
    </dt>
    <dd>{{% md %}}A list of server health information. See below for details on the
available information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>failure<wbr>Tolerance</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of redundant healthy servers that could fail
without causing an outage
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

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
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getautopilothealthserver">Get<wbr>Autopilot<wbr>Health<wbr>Server[]</a></span>
    </dt>
    <dd>{{% md %}}A list of server health information. See below for details on the
available information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>failure_<wbr>tolerance</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of redundant healthy servers that could fail
without causing an outage
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

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
        <span>servers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getautopilothealthserver">List[Get<wbr>Autopilot<wbr>Health<wbr>Server]</a></span>
    </dt>
    <dd>{{% md %}}A list of server health information. See below for details on the
available information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>datacenter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Autopilot<wbr>Health<wbr>Server</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/consul/types/output/#GetAutopilotHealthServer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-consul/sdk/go/consul/?tab=doc#GetAutopilotHealthServer">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The address of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Raft ID of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Contact</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time elapsed since the server's last contact with
the leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The index of the server's last committed Raft log entry
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The server's last known Raft leader term
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Leader</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is currently leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The node name of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Serf<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the SerfHealth check of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Stable<wbr>Since</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time this server has been in its current ``Healthy``
state
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consul version of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Voter</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is a voting member of the Raft cluster
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The address of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Raft ID of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Contact</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time elapsed since the server's last contact with
the leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The index of the server's last committed Raft log entry
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Last<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The server's last known Raft leader term
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Leader</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is currently leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The node name of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Serf<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the SerfHealth check of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Stable<wbr>Since</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time this server has been in its current ``Healthy``
state
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consul version of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Voter</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is a voting member of the Raft cluster
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The address of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Raft ID of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Contact</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time elapsed since the server's last contact with
the leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The index of the server's last committed Raft log entry
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The server's last known Raft leader term
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>leader</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the server is currently leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The node name of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>serf<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The status of the SerfHealth check of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>stable<wbr>Since</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time this server has been in its current ``Healthy``
state
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Consul version of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>voter</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the server is a voting member of the Raft cluster
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The address of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>healthy</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is healthy according to the current Autopilot
configuration
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Raft ID of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Contact</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time elapsed since the server's last contact with
the leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The index of the server's last committed Raft log entry
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>last<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The server's last known Raft leader term
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>leader</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is currently leader
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The node name of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>serf<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The status of the SerfHealth check of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>stable<wbr>Since</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time this server has been in its current ``Healthy``
state
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Consul version of the server
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>voter</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the server is a voting member of the Raft cluster
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







