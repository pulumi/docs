
---
title: "Fleet"
block_external_search_index: true
---

Provides a resource to manage EC2 Fleets.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.ec2.Fleet("example", {
    launchTemplateConfig: {
        launchTemplateSpecification: {
            launchTemplateId: aws_launch_template_example.id,
            version: aws_launch_template_example.latestVersion,
        },
    },
    targetCapacitySpecification: {
        defaultTargetCapacityType: "spot",
        totalTargetCapacity: 5,
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ec2_fleet.html.markdown.



## Create a Fleet Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#Fleet">Fleet</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#FleetArgs">FleetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Fleet</span><span class="p">(resource_name, opts=None, </span>excess_capacity_termination_policy=None<span class="p">, </span>launch_template_config=None<span class="p">, </span>on_demand_options=None<span class="p">, </span>replace_unhealthy_instances=None<span class="p">, </span>spot_options=None<span class="p">, </span>tags=None<span class="p">, </span>target_capacity_specification=None<span class="p">, </span>terminate_instances=None<span class="p">, </span>terminate_instances_with_expiration=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFleet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetArgs">FleetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#Fleet">Fleet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.Fleet.html">Fleet</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.Inputs.FleetArgs.html">FleetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Fleet<wbr>On<wbr>Demand<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Fleet<wbr>Spot<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">*Fleet<wbr>On<wbr>Demand<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">*Fleet<wbr>Spot<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Fleet<wbr>On<wbr>Demand<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Fleet<wbr>Spot<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>excess_<wbr>capacity_<wbr>termination_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>launch_<wbr>template_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Dict[Fleet<wbr>Launch<wbr>Template<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on_<wbr>demand_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Dict[Fleet<wbr>On<wbr>Demand<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replace_<wbr>unhealthy_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Dict[Fleet<wbr>Spot<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target_<wbr>capacity_<wbr>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Dict[Fleet<wbr>Target<wbr>Capacity<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate_<wbr>instances_<wbr>with_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Fleet Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>On<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Fleet<wbr>On<wbr>Demand<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Fleet<wbr>Spot<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>On<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">*Fleet<wbr>On<wbr>Demand<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">*Fleet<wbr>Spot<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>on<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Fleet<wbr>On<wbr>Demand<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Fleet<wbr>Spot<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>excess_<wbr>capacity_<wbr>termination_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>launch_<wbr>template_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Dict[Fleet<wbr>Launch<wbr>Template<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>on_<wbr>demand_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Dict[Fleet<wbr>On<wbr>Demand<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>replace_<wbr>unhealthy_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spot_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Dict[Fleet<wbr>Spot<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>target_<wbr>capacity_<wbr>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Dict[Fleet<wbr>Target<wbr>Capacity<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>terminate_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>terminate_<wbr>instances_<wbr>with_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Fleet Resource

Get an existing Fleet resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#FleetState">FleetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#Fleet">Fleet</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>excess_capacity_termination_policy=None<span class="p">, </span>launch_template_config=None<span class="p">, </span>on_demand_options=None<span class="p">, </span>replace_unhealthy_instances=None<span class="p">, </span>spot_options=None<span class="p">, </span>tags=None<span class="p">, </span>target_capacity_specification=None<span class="p">, </span>terminate_instances=None<span class="p">, </span>terminate_instances_with_expiration=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFleet<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetState">FleetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#Fleet">Fleet</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.Fleet.html">Fleet</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.FleetState.html">FleetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Fleet<wbr>On<wbr>Demand<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Fleet<wbr>Spot<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">*Fleet<wbr>Launch<wbr>Template<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">*Fleet<wbr>On<wbr>Demand<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">*Fleet<wbr>Spot<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">*Fleet<wbr>Target<wbr>Capacity<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>excess<wbr>Capacity<wbr>Termination<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Template<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Fleet<wbr>Launch<wbr>Template<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Demand<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Fleet<wbr>On<wbr>Demand<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replace<wbr>Unhealthy<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Fleet<wbr>Spot<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target<wbr>Capacity<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Fleet<wbr>Target<wbr>Capacity<wbr>Specification?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate<wbr>Instances<wbr>With<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>excess_<wbr>capacity_<wbr>termination_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated if the total target capacity of the EC2 Fleet is decreased below the current size of the EC2. Valid values: `no-termination`, `termination`. Defaults to `termination`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch_<wbr>template_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfig">Dict[Fleet<wbr>Launch<wbr>Template<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on_<wbr>demand_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetondemandoptions">Dict[Fleet<wbr>On<wbr>Demand<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing On-Demand configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replace_<wbr>unhealthy_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether EC2 Fleet should replace unhealthy instances. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetspotoptions">Dict[Fleet<wbr>Spot<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing Spot configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Map of Fleet tags. To tag instances at launch, specify the tags in the Launch Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>target_<wbr>capacity_<wbr>specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleettargetcapacityspecification">Dict[Fleet<wbr>Target<wbr>Capacity<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing target capacity configurations. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to terminate instances for an EC2 Fleet if it is deleted successfully. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>terminate_<wbr>instances_<wbr>with_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether running instances should be terminated when the EC2 Fleet expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of request. Indicates whether the EC2 Fleet only requests the target capacity, or also attempts to maintain it. Valid values: `maintain`, `request`. Defaults to `maintain`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Fleet<wbr>Launch<wbr>Template<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetLaunchTemplateConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetLaunchTemplateConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetLaunchTemplateConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetLaunchTemplateConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Template<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfiglaunchtemplatespecification">Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Launch<wbr>Template<wbr>Specification<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template to use. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfigoverride">List&lt;Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Override<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument(s) containing parameters to override the same parameters in the Launch Template. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Template<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfiglaunchtemplatespecification">Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Launch<wbr>Template<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template to use. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfigoverride">[]Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Override</a></span>
    </dt>
    <dd>{{% md %}}Nested argument(s) containing parameters to override the same parameters in the Launch Template. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>launch<wbr>Template<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfiglaunchtemplatespecification">Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Launch<wbr>Template<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template to use. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfigoverride">Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Override[]?</a></span>
    </dt>
    <dd>{{% md %}}Nested argument(s) containing parameters to override the same parameters in the Launch Template. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>launch<wbr>Template<wbr>Specification</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfiglaunchtemplatespecification">Dict[Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Launch<wbr>Template<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument containing EC2 Launch Template to use. Defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>overrides</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#fleetlaunchtemplateconfigoverride">List[Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Override]</a></span>
    </dt>
    <dd>{{% md %}}Nested argument(s) containing parameters to override the same parameters in the Launch Template. Defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Launch<wbr>Template<wbr>Specification</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetLaunchTemplateConfigLaunchTemplateSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetLaunchTemplateConfigLaunchTemplateSpecification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetLaunchTemplateConfigLaunchTemplateSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetLaunchTemplateConfigLaunchTemplateSpecificationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Template<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the launch template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Version number of the launch template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Template<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the launch template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Version number of the launch template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Template<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the launch template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Version number of the launch template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Template<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the launch template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Template<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Version number of the launch template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Launch<wbr>Template<wbr>Config<wbr>Override</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetLaunchTemplateConfigOverride">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetLaunchTemplateConfigOverride">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetLaunchTemplateConfigOverrideArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetLaunchTemplateConfigOverrideOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Availability Zone in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maximum price per unit hour that you are willing to pay for a Spot Instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}Priority for the launch template override. If `on_demand_options` `allocation_strategy` is set to `prioritized`, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. Valid values are whole numbers starting at 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the subnet in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}Number of units provided by the specified instance type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Availability Zone in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Maximum price per unit hour that you are willing to pay for a Spot Instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}Priority for the launch template override. If `on_demand_options` `allocation_strategy` is set to `prioritized`, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. Valid values are whole numbers starting at 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the subnet in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weighted<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}Number of units provided by the specified instance type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Availability Zone in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maximum price per unit hour that you are willing to pay for a Spot Instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Priority for the launch template override. If `on_demand_options` `allocation_strategy` is set to `prioritized`, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. Valid values are whole numbers starting at 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the subnet in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of units provided by the specified instance type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>availability_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Availability Zone in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance type.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maximum price per unit hour that you are willing to pay for a Spot Instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>priority</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Priority for the launch template override. If `on_demand_options` `allocation_strategy` is set to `prioritized`, EC2 Fleet uses priority to determine which launch template override to use first in fulfilling On-Demand capacity. The highest priority is launched first. The lower the number, the higher the priority. If no number is set, the launch template override has the lowest priority. Valid values are whole numbers starting at 0.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the subnet in which to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weighted<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of units provided by the specified instance type.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>On<wbr>Demand<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetOnDemandOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetOnDemandOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetOnDemandOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetOnDemandOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allocation<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allocation_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Spot<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetSpotOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetSpotOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetSpotOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetSpotOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Behavior when a Spot Instance is interrupted. Valid values: `hibernate`, `stop`, `terminate`. Default: `terminate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Pools<wbr>To<wbr>Use<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot `allocation_strategy` is set to `lowestPrice`. Default: `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Allocation<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Behavior when a Spot Instance is interrupted. Valid values: `hibernate`, `stop`, `terminate`. Default: `terminate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Pools<wbr>To<wbr>Use<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot `allocation_strategy` is set to `lowestPrice`. Default: `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allocation<wbr>Strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Behavior when a Spot Instance is interrupted. Valid values: `hibernate`, `stop`, `terminate`. Default: `terminate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Pools<wbr>To<wbr>Use<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot `allocation_strategy` is set to `lowestPrice`. Default: `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>allocation_<wbr>strategy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How to allocate the target capacity across the Spot pools. Valid values: `diversified`, `lowestPrice`. Default: `lowestPrice`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Behavior when a Spot Instance is interrupted. Valid values: `hibernate`, `stop`, `terminate`. Default: `terminate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>pools_<wbr>to_<wbr>use_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Number of Spot pools across which to allocate your target Spot capacity. Valid only when Spot `allocation_strategy` is set to `lowestPrice`. Default: `1`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Fleet<wbr>Target<wbr>Capacity<wbr>Specification</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FleetTargetCapacitySpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FleetTargetCapacitySpecification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetTargetCapacitySpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#FleetTargetCapacitySpecificationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Target<wbr>Capacity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Default target capacity type. Valid values: `on-demand`, `spot`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Demand<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of On-Demand units to request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of Spot units to request.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Total<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of units to request, filled using `default_target_capacity_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Default<wbr>Target<wbr>Capacity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Default target capacity type. Valid values: `on-demand`, `spot`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Demand<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of On-Demand units to request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of Spot units to request.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Total<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of units to request, filled using `default_target_capacity_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Target<wbr>Capacity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Default target capacity type. Valid values: `on-demand`, `spot`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Demand<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of On-Demand units to request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of Spot units to request.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>total<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of units to request, filled using `default_target_capacity_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>default<wbr>Target<wbr>Capacity<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Default target capacity type. Valid values: `on-demand`, `spot`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Demand<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of On-Demand units to request.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of Spot units to request.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>total<wbr>Target<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of units to request, filled using `default_target_capacity_type`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







