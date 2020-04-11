
---
title: "Fleet"
block_external_search_index: true
---



Provides a Gamelift Fleet resource.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.gamelift.Fleet("example", {
    buildId: aws_gamelift_build_example.id,
    ec2InstanceType: "t2.micro",
    fleetType: "ON_DEMAND",
    runtimeConfiguration: {
        serverProcesses: [{
            concurrentExecutions: 1,
            launchPath: "C:\\game\\GomokuServer.exe",
        }],
    },
});
```

{{% /example %}}
{{% /examples %}}



## Create a Fleet Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/gamelift/#Fleet">Fleet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/gamelift/#FleetArgs">FleetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Fleet</span><span class="p">(resource_name, opts=None, </span>build_id=None<span class="p">, </span>description=None<span class="p">, </span>ec2_inbound_permissions=None<span class="p">, </span>ec2_instance_type=None<span class="p">, </span>fleet_type=None<span class="p">, </span>instance_role_arn=None<span class="p">, </span>metric_groups=None<span class="p">, </span>name=None<span class="p">, </span>new_game_session_protection_policy=None<span class="p">, </span>resource_creation_limit_policy=None<span class="p">, </span>runtime_configuration=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFleet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetArgs">FleetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#Fleet">Fleet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Gamelift.Fleet.html">Fleet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GameLift.FleetArgs.html">FleetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">List&lt;Fleet<wbr>Ec2Inbound<wbr>Permission<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>New<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Fleet<wbr>Runtime<wbr>Configuration<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">[]Fleet<wbr>Ec2Inbound<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>New<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">*Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">*Fleet<wbr>Runtime<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">Fleet<wbr>Ec2Inbound<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>new<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Fleet<wbr>Runtime<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>build_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ec2_<wbr>inbound_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">List[Fleet<wbr>Ec2Inbound<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ec2_<wbr>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fleet_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>new_<wbr>game_<wbr>session_<wbr>protection_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>creation_<wbr>limit_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Dict[Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Dict[Fleet<wbr>Runtime<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Fleet Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">List&lt;Fleet<wbr>Ec2Inbound<wbr>Permission&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>New<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Operating<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Fleet<wbr>Runtime<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">[]Fleet<wbr>Ec2Inbound<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>New<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Operating<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">*Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">*Fleet<wbr>Runtime<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">Fleet<wbr>Ec2Inbound<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>new<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>operating<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Fleet<wbr>Runtime<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>build_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ec2_<wbr>inbound_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">List[Fleet<wbr>Ec2Inbound<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ec2_<wbr>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fleet_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log_<wbr>paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metric_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>new_<wbr>game_<wbr>session_<wbr>protection_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>operating_<wbr>system</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>creation_<wbr>limit_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Dict[Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Dict[Fleet<wbr>Runtime<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Fleet Resource

Get an existing Fleet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/gamelift/#FleetState">FleetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/gamelift/#Fleet">Fleet</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>build_id=None<span class="p">, </span>description=None<span class="p">, </span>ec2_inbound_permissions=None<span class="p">, </span>ec2_instance_type=None<span class="p">, </span>fleet_type=None<span class="p">, </span>instance_role_arn=None<span class="p">, </span>log_paths=None<span class="p">, </span>metric_groups=None<span class="p">, </span>name=None<span class="p">, </span>new_game_session_protection_policy=None<span class="p">, </span>operating_system=None<span class="p">, </span>resource_creation_limit_policy=None<span class="p">, </span>runtime_configuration=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFleet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetState">FleetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#Fleet">Fleet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Gamelift.Fleet.html">Fleet</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Gamelift.FleetState.html">FleetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">List&lt;Fleet<wbr>Ec2Inbound<wbr>Permission<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>New<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operating<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Fleet<wbr>Runtime<wbr>Configuration<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">[]Fleet<wbr>Ec2Inbound<wbr>Permission</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>New<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Operating<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">*Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">*Fleet<wbr>Runtime<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>build<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ec2Inbound<wbr>Permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">Fleet<wbr>Ec2Inbound<wbr>Permission[]?</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ec2Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fleet<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>new<wbr>Game<wbr>Session<wbr>Protection<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operating<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Creation<wbr>Limit<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Fleet<wbr>Runtime<wbr>Configuration?</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Fleet ARN.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>build_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the Gamelift Build to be deployed on the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Human-readable description of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ec2_<wbr>inbound_<wbr>permissions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetec2inboundpermission">List[Fleet<wbr>Ec2Inbound<wbr>Permission]</a></span>
    </dt>
    <dd>{{% md %}}Range of IP addresses and port settings that permit inbound traffic to access server processes running on the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ec2_<wbr>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of an EC2 instance type. e.g. `t2.micro`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fleet_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Type of fleet. This value must be `ON_DEMAND` or `SPOT`. Defaults to `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ARN of an IAM role that instances in the fleet can assume.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>paths</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>metric_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of names of metric groups to add this fleet to. A metric group tracks metrics across all fleets in the group. Defaults to `default`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the fleet.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>new_<wbr>game_<wbr>session_<wbr>protection_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Game session protection policy to apply to all instances in this fleet. e.g. `FullProtection`. Defaults to `NoProtection`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>operating_<wbr>system</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Operating system of the fleet's computing resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>creation_<wbr>limit_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetresourcecreationlimitpolicy">Dict[Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Policy that limits the number of game sessions an individual player can create over a span of time for this fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfiguration">Dict[Fleet<wbr>Runtime<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Instructions for launching server processes on each instance in the fleet. See below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Fleet<wbr>Ec2Inbound<wbr>Permission</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetEc2InboundPermission">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetEc2InboundPermission">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetEc2InboundPermissionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetEc2InboundPermissionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Starting value for a range of allowed port numbers.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range of allowed IP addresses expressed in CIDR notation. e.g. `000.000.000.000/[subnet mask]` or `0.0.0.0/[subnet mask]`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Network communication protocol used by the fleet. e.g. `TCP` or `UDP`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than `from_port`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>From<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Starting value for a range of allowed port numbers.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range of allowed IP addresses expressed in CIDR notation. e.g. `000.000.000.000/[subnet mask]` or `0.0.0.0/[subnet mask]`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Network communication protocol used by the fleet. e.g. `TCP` or `UDP`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>To<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than `from_port`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>from<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Starting value for a range of allowed port numbers.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Range of allowed IP addresses expressed in CIDR notation. e.g. `000.000.000.000/[subnet mask]` or `0.0.0.0/[subnet mask]`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Network communication protocol used by the fleet. e.g. `TCP` or `UDP`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>to<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than `from_port`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>from_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting value for a range of allowed port numbers.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ip<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Range of allowed IP addresses expressed in CIDR notation. e.g. `000.000.000.000/[subnet mask]` or `0.0.0.0/[subnet mask]`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>protocol</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Network communication protocol used by the fleet. e.g. `TCP` or `UDP`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>to_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be higher than `from_port`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Resource<wbr>Creation<wbr>Limit<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetResourceCreationLimitPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetResourceCreationLimitPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetResourceCreationLimitPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetResourceCreationLimitPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>New<wbr>Game<wbr>Sessions<wbr>Per<wbr>Creator</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions that an individual can create during the policy period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Period<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Time span used in evaluating the resource creation limit policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>New<wbr>Game<wbr>Sessions<wbr>Per<wbr>Creator</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions that an individual can create during the policy period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Policy<wbr>Period<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Time span used in evaluating the resource creation limit policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>new<wbr>Game<wbr>Sessions<wbr>Per<wbr>Creator</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions that an individual can create during the policy period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy<wbr>Period<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Time span used in evaluating the resource creation limit policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>new<wbr>Game<wbr>Sessions<wbr>Per<wbr>Creator</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions that an individual can create during the policy period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>policy<wbr>Period<wbr>In<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Time span used in evaluating the resource creation limit policy.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Runtime<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetRuntimeConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetRuntimeConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetRuntimeConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetRuntimeConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Game<wbr>Session<wbr>Activation<wbr>Timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum amount of time (in seconds) that a game session can remain in status `ACTIVATING`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Concurrent<wbr>Game<wbr>Session<wbr>Activations</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions with status `ACTIVATING` to allow on an instance simultaneously. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Processes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfigurationserverprocess">List&lt;Fleet<wbr>Runtime<wbr>Configuration<wbr>Server<wbr>Process<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Game<wbr>Session<wbr>Activation<wbr>Timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum amount of time (in seconds) that a game session can remain in status `ACTIVATING`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Concurrent<wbr>Game<wbr>Session<wbr>Activations</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions with status `ACTIVATING` to allow on an instance simultaneously. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Processes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfigurationserverprocess">[]Fleet<wbr>Runtime<wbr>Configuration<wbr>Server<wbr>Process</a></span>
    </dt>
    <dd>{{% md %}}Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>game<wbr>Session<wbr>Activation<wbr>Timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum amount of time (in seconds) that a game session can remain in status `ACTIVATING`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Concurrent<wbr>Game<wbr>Session<wbr>Activations</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions with status `ACTIVATING` to allow on an instance simultaneously. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Processes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfigurationserverprocess">Fleet<wbr>Runtime<wbr>Configuration<wbr>Server<wbr>Process[]?</a></span>
    </dt>
    <dd>{{% md %}}Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>game<wbr>Session<wbr>Activation<wbr>Timeout<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum amount of time (in seconds) that a game session can remain in status `ACTIVATING`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Concurrent<wbr>Game<wbr>Session<wbr>Activations</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum number of game sessions with status `ACTIVATING` to allow on an instance simultaneously. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Processes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetruntimeconfigurationserverprocess">List[Fleet<wbr>Runtime<wbr>Configuration<wbr>Server<wbr>Process]</a></span>
    </dt>
    <dd>{{% md %}}Collection of server process configurations that describe which server processes to run on each instance in a fleet. See below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Runtime<wbr>Configuration<wbr>Server<wbr>Process</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetRuntimeConfigurationServerProcess">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetRuntimeConfigurationServerProcess">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetRuntimeConfigurationServerProcessArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/gamelift?tab=doc#FleetRuntimeConfigurationServerProcessOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of server processes using this configuration to run concurrently on an instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances `C:\game`, and for Linux instances `/local/game`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional list of parameters to pass to the server executable on launch.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Number of server processes using this configuration to run concurrently on an instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances `C:\game`, and for Linux instances `/local/game`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Optional list of parameters to pass to the server executable on launch.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Number of server processes using this configuration to run concurrently on an instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>launch<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances `C:\game`, and for Linux instances `/local/game`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Optional list of parameters to pass to the server executable on launch.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>concurrent<wbr>Executions</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of server processes using this configuration to run concurrently on an instance.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>launch<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Location of the server executable in a game build. All game builds are installed on instances at the root : for Windows instances `C:\game`, and for Linux instances `/local/game`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Optional list of parameters to pass to the server executable on launch.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).</dd>
</dl>

