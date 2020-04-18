
---
title: "Queue"
block_external_search_index: true
---



The ``rabbitmq..Queue`` resource creates and manages a queue.

## Example Usage

### Basic Example

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as rabbitmq from "@pulumi/rabbitmq";

const testVHost = new rabbitmq.VHost("test", {});
const guest = new rabbitmq.Permissions("guest", {
    permissions: {
        configure: ".*",
        read: ".*",
        write: ".*",
    },
    user: "guest",
    vhost: testVHost.name,
});
const testQueue = new rabbitmq.Queue("test", {
    settings: {
        autoDelete: true,
        durable: false,
    },
    vhost: guest.vhost,
});
```

### Example With JSON Arguments

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as rabbitmq from "@pulumi/rabbitmq";

const config = new pulumi.Config();
const arguments = config.get("arguments") || `{
  "x-message-ttl": 5000
}
`;

const testVHost = new rabbitmq.VHost("test", {});
const guest = new rabbitmq.Permissions("guest", {
    permissions: {
        configure: ".*",
        read: ".*",
        write: ".*",
    },
    user: "guest",
    vhost: testVHost.name,
});
const testQueue = new rabbitmq.Queue("test", {
    settings: {
        argumentsJson: arguments,
        autoDelete: true,
        durable: false,
    },
    vhost: guest.vhost,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-rabbitmq/blob/master/website/docs/r/queue.html.markdown.



## Create a Queue Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rabbitmq/#Queue">Queue</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rabbitmq/#QueueArgs">QueueArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Queue</span><span class="p">(resource_name, opts=None, </span>name=None<span class="p">, </span>settings=None<span class="p">, </span>vhost=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewQueue<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq/?tab=doc#QueueArgs">QueueArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq/?tab=doc#Queue">Queue</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rabbitmq/Pulumi.Rabbitmq..Queue.html">Queue</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rabbitmq/Pulumi.Rabbitmq.QueueArgs.html">QueueArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Dict[Queue<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Queue Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Dict[Queue<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Queue Resource

Get an existing Queue resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rabbitmq/#QueueState">QueueState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/rabbitmq/#Queue">Queue</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>name=None<span class="p">, </span>settings=None<span class="p">, </span>vhost=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetQueue<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq/?tab=doc#QueueState">QueueState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq/?tab=doc#Queue">Queue</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rabbitmq/Pulumi.Rabbitmq..Queue.html">Queue</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Rabbitmq/Pulumi.Rabbitmq..QueueState.html">QueueState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">*Queue<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Queue<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the queue.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#queuesettings">Dict[Queue<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The settings of the queue. The structure is
described below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vhost</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The vhost to create the resource in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Queue<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/rabbitmq/types/input/#QueueSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/rabbitmq/types/output/#QueueSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq/?tab=doc#QueueSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-rabbitmq/sdk/go/rabbitmq/?tab=doc#QueueSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arguments</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Additional key/value settings for the queue.
All values will be sent to RabbitMQ as a string. If you require non-string
values, use `arguments_json`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arguments<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A nested JSON string which contains additional
settings for the queue. This is useful for when the arguments contain
non-string values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the queue will self-delete when all
consumers have unsubscribed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Durable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the queue survives server restarts.
Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arguments</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Additional key/value settings for the queue.
All values will be sent to RabbitMQ as a string. If you require non-string
values, use `arguments_json`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arguments<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A nested JSON string which contains additional
settings for the queue. This is useful for when the arguments contain
non-string values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the queue will self-delete when all
consumers have unsubscribed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Durable</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the queue survives server restarts.
Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arguments</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Additional key/value settings for the queue.
All values will be sent to RabbitMQ as a string. If you require non-string
values, use `arguments_json`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arguments<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A nested JSON string which contains additional
settings for the queue. This is useful for when the arguments contain
non-string values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the queue will self-delete when all
consumers have unsubscribed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>durable</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the queue survives server restarts.
Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arguments</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Additional key/value settings for the queue.
All values will be sent to RabbitMQ as a string. If you require non-string
values, use `arguments_json`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arguments<wbr>Json</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A nested JSON string which contains additional
settings for the queue. This is useful for when the arguments contain
non-string values.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the queue will self-delete when all
consumers have unsubscribed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>durable</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the queue survives server restarts.
Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-rabbitmq">https://github.com/pulumi/pulumi-rabbitmq</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

