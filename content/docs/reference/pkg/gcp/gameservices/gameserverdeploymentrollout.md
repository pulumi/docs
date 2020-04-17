
---
title: "GameServerDeploymentRollout"
block_external_search_index: true
---



This represents the rollout state. This is part of the game server
deployment.

To get more information about GameServerDeploymentRollout, see:

* [API documentation](https://cloud.google.com/game-servers/docs/reference/rest/v1beta/GameServerDeploymentRollout)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/game-servers/docs)



## Create a GameServerDeploymentRollout Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/gameservices/#GameServerDeploymentRollout">GameServerDeploymentRollout</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/gameservices/#GameServerDeploymentRolloutArgs">GameServerDeploymentRolloutArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">GameServerDeploymentRollout</span><span class="p">(resource_name, opts=None, </span>default_game_server_config=None<span class="p">, </span>deployment_id=None<span class="p">, </span>game_server_config_overrides=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewGameServerDeploymentRollout<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRolloutArgs">GameServerDeploymentRolloutArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRollout">GameServerDeploymentRollout</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.GameServices.GameServerDeploymentRollout.html">GameServerDeploymentRollout</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.GameServices.GameServerDeploymentRolloutArgs.html">GameServerDeploymentRolloutArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Default<wbr>Game<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Deployment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Game<wbr>Server<wbr>Config<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">List&lt;Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Game<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Deployment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Game<wbr>Server<wbr>Config<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">[]Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Game<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>deployment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>game<wbr>Server<wbr>Config<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override[]</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default_<wbr>game_<wbr>server_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>deployment_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>game_<wbr>server_<wbr>config_<wbr>overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">List[Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override]</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## GameServerDeploymentRollout Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing GameServerDeploymentRollout Resource

Get an existing GameServerDeploymentRollout resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/gameservices/#GameServerDeploymentRolloutState">GameServerDeploymentRolloutState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/gameservices/#GameServerDeploymentRollout">GameServerDeploymentRollout</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>default_game_server_config=None<span class="p">, </span>deployment_id=None<span class="p">, </span>game_server_config_overrides=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetGameServerDeploymentRollout<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRolloutState">GameServerDeploymentRolloutState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRollout">GameServerDeploymentRollout</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.GameServices.GameServerDeploymentRollout.html">GameServerDeploymentRollout</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.GameServices.GameServerDeploymentRolloutState.html">GameServerDeploymentRolloutState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Default<wbr>Game<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deployment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Game<wbr>Server<wbr>Config<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">List&lt;Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Game<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Deployment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Game<wbr>Server<wbr>Config<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">[]Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Game<wbr>Server<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deployment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>game<wbr>Server<wbr>Config<wbr>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override[]</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>game_<wbr>server_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}This field points to the game server config that is applied by default to all realms and clusters. For example,
'projects/my-project/locations/global/gameServerDeployments/my-game/configs/my-config'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>deployment_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The deployment to rollout the new config to. Only 1 rollout must be associated with each deployment.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>game_<wbr>server_<wbr>config_<wbr>overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverride">List[Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override]</a></span>
    </dt>
    <dd>{{% md %}}The game_server_config_overrides contains the per game server config overrides. The overrides are processed in the order
they are listed. As soon as a match is found for a cluster, the rest of the list is not processed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The resource id of the game server deployment eg:
'projects/my-project/locations/global/gameServerDeployments/my-deployment/rollout'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#GameServerDeploymentRolloutGameServerConfigOverride">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GameServerDeploymentRolloutGameServerConfigOverride">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRolloutGameServerConfigOverrideArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRolloutGameServerConfigOverrideOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realms<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverriderealmsselector">Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Realms<wbr>Selector<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Realms<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverriderealmsselector">Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Realms<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realms<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverriderealmsselector">Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Realms<wbr>Selector</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>config<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>realms<wbr>Selector</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#gameserverdeploymentrolloutgameserverconfigoverriderealmsselector">Dict[Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Realms<wbr>Selector]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Game<wbr>Server<wbr>Deployment<wbr>Rollout<wbr>Game<wbr>Server<wbr>Config<wbr>Override<wbr>Realms<wbr>Selector</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelector">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelector">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/gameservices?tab=doc#GameServerDeploymentRolloutGameServerConfigOverrideRealmsSelectorOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Realms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Realms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>realms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>realms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

