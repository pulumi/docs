
---
title: "GetLaunchTemplate"
block_external_search_index: true
---



Provides information about a Launch Template.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const defaultLaunchTemplate = pulumi.output(aws.ec2.getLaunchTemplate({
    name: "my-launch-template",
}, { async: true }));
```

{{% /example %}}
{{% example %}}
### Filter

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const test = pulumi.output(aws.ec2.getLaunchTemplate({
    filter: [{
        name: "launch-template-name",
        values: ["some-template"],
    }],
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetLaunchTemplate

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getLaunchTemplate<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetLaunchTemplateArgs">GetLaunchTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetLaunchTemplateResult">GetLaunchTemplateResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_launch_template(</span>filters=None<span class="p">, </span>name=None<span class="p">, </span>tags=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupLaunchTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LookupLaunchTemplateArgs">LookupLaunchTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LookupLaunchTemplateResult">LookupLaunchTemplateResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetLaunchTemplate </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchTemplateResult.html">GetLaunchTemplateResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchTemplateArgs.html">GetLaunchTemplateArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">List&lt;Get<wbr>Launch<wbr>Template<wbr>Filter<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block(s) for filtering. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">[]Get<wbr>Launch<wbr>Template<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}Configuration block(s) for filtering. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">Get<wbr>Launch<wbr>Template<wbr>Filter[]?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block(s) for filtering. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">List[Get<wbr>Launch<wbr>Template<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}Configuration block(s) for filtering. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetLaunchTemplate Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Block<wbr>Device<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemapping">List&lt;Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specify volumes to attach to the instance besides the volumes specified by the AMI.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credit<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatecreditspecification">List&lt;Get<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification&gt;</a></span>
    </dt>
    <dd>{{% md %}}Customize the credit specification of the instance. See Credit
Specification below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The default version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disable<wbr>Api<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If `true`, the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Elastic<wbr>Gpu<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateelasticgpuspecification">List&lt;Get<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification&gt;</a></span>
    </dt>
    <dd>{{% md %}}The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">List&lt;Get<wbr>Launch<wbr>Template<wbr>Filter&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hibernation<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatehibernationoption">List&lt;Get<wbr>Launch<wbr>Template<wbr>Hibernation<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}The hibernation options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iam<wbr>Instance<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateiaminstanceprofile">List&lt;Get<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile&gt;</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
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
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The AMI from which to launch the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Market<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoption">List&lt;Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}The market (purchasing) option for the instance.
below for details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kernel<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The kernel ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The key name to use for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Latest<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The latest version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemetadataoption">List&lt;Get<wbr>Launch<wbr>Template<wbr>Metadata<wbr>Option&gt;</a></span>
    </dt>
    <dd>{{% md %}}The metadata options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitorings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemonitoring">List&lt;Get<wbr>Launch<wbr>Template<wbr>Monitoring&gt;</a></span>
    </dt>
    <dd>{{% md %}}The monitoring option for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatenetworkinterface">List&lt;Get<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface&gt;</a></span>
    </dt>
    <dd>{{% md %}}Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Placements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateplacement">List&lt;Get<wbr>Launch<wbr>Template<wbr>Placement&gt;</a></span>
    </dt>
    <dd>{{% md %}}The placement of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ram<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the RAM disk.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tag<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatetagspecification">List&lt;Get<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification&gt;</a></span>
    </dt>
    <dd>{{% md %}}The tags to apply to the resources during launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}(Optional) A mapping of tags to assign to the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Base64-encoded user data to provide when launching the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of security group IDs to associate with.
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
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Block<wbr>Device<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemapping">[]Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping</a></span>
    </dt>
    <dd>{{% md %}}Specify volumes to attach to the instance besides the volumes specified by the AMI.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Credit<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatecreditspecification">[]Get<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}Customize the credit specification of the instance. See Credit
Specification below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The default version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disable<wbr>Api<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If `true`, the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Elastic<wbr>Gpu<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateelasticgpuspecification">[]Get<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">[]Get<wbr>Launch<wbr>Template<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hibernation<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatehibernationoption">[]Get<wbr>Launch<wbr>Template<wbr>Hibernation<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}The hibernation options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iam<wbr>Instance<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateiaminstanceprofile">[]Get<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
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
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The AMI from which to launch the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Market<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoption">[]Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}The market (purchasing) option for the instance.
below for details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kernel<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The kernel ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The key name to use for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Latest<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The latest version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Metadata<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemetadataoption">[]Get<wbr>Launch<wbr>Template<wbr>Metadata<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}The metadata options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitorings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemonitoring">[]Get<wbr>Launch<wbr>Template<wbr>Monitoring</a></span>
    </dt>
    <dd>{{% md %}}The monitoring option for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatenetworkinterface">[]Get<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface</a></span>
    </dt>
    <dd>{{% md %}}Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Placements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateplacement">[]Get<wbr>Launch<wbr>Template<wbr>Placement</a></span>
    </dt>
    <dd>{{% md %}}The placement of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ram<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the RAM disk.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tag<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatetagspecification">[]Get<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification</a></span>
    </dt>
    <dd>{{% md %}}The tags to apply to the resources during launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}(Optional) A mapping of tags to assign to the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Base64-encoded user data to provide when launching the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of security group IDs to associate with.
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
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>block<wbr>Device<wbr>Mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemapping">Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping[]</a></span>
    </dt>
    <dd>{{% md %}}Specify volumes to attach to the instance besides the volumes specified by the AMI.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credit<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatecreditspecification">Get<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification[]</a></span>
    </dt>
    <dd>{{% md %}}Customize the credit specification of the instance. See Credit
Specification below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The default version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disable<wbr>Api<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If `true`, the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>elastic<wbr>Gpu<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateelasticgpuspecification">Get<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification[]</a></span>
    </dt>
    <dd>{{% md %}}The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">Get<wbr>Launch<wbr>Template<wbr>Filter[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hibernation<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatehibernationoption">Get<wbr>Launch<wbr>Template<wbr>Hibernation<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}The hibernation options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iam<wbr>Instance<wbr>Profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateiaminstanceprofile">Get<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile[]</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
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
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The AMI from which to launch the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Market<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoption">Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}The market (purchasing) option for the instance.
below for details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kernel<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The kernel ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The key name to use for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>latest<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The latest version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemetadataoption">Get<wbr>Launch<wbr>Template<wbr>Metadata<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}The metadata options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitorings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemonitoring">Get<wbr>Launch<wbr>Template<wbr>Monitoring[]</a></span>
    </dt>
    <dd>{{% md %}}The monitoring option for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatenetworkinterface">Get<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface[]</a></span>
    </dt>
    <dd>{{% md %}}Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>placements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateplacement">Get<wbr>Launch<wbr>Template<wbr>Placement[]</a></span>
    </dt>
    <dd>{{% md %}}The placement of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ram<wbr>Disk<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the RAM disk.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Group<wbr>Names</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tag<wbr>Specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatetagspecification">Get<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification[]</a></span>
    </dt>
    <dd>{{% md %}}The tags to apply to the resources during launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}(Optional) A mapping of tags to assign to the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Base64-encoded user data to provide when launching the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of security group IDs to associate with.
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
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>block_<wbr>device_<wbr>mappings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemapping">List[Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping]</a></span>
    </dt>
    <dd>{{% md %}}Specify volumes to attach to the instance besides the volumes specified by the AMI.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>credit_<wbr>specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatecreditspecification">List[Get<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}Customize the credit specification of the instance. See Credit
Specification below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The default version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disable_<wbr>api_<wbr>termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs_<wbr>optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If `true`, the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>elastic_<wbr>gpu_<wbr>specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateelasticgpuspecification">List[Get<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatefilter">List[Get<wbr>Launch<wbr>Template<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hibernation_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatehibernationoption">List[Get<wbr>Launch<wbr>Template<wbr>Hibernation<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}The hibernation options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iam_<wbr>instance_<wbr>profiles</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateiaminstanceprofile">List[Get<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile]</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
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
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AMI from which to launch the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>initiated_<wbr>shutdown_<wbr>behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>market_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoption">List[Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}The market (purchasing) option for the instance.
below for details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kernel_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The kernel ID.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key name to use for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>latest_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The latest version of the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>metadata_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemetadataoption">List[Get<wbr>Launch<wbr>Template<wbr>Metadata<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}The metadata options for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitorings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatemonitoring">List[Get<wbr>Launch<wbr>Template<wbr>Monitoring]</a></span>
    </dt>
    <dd>{{% md %}}The monitoring option for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interfaces</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatenetworkinterface">List[Get<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface]</a></span>
    </dt>
    <dd>{{% md %}}Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>placements</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateplacement">List[Get<wbr>Launch<wbr>Template<wbr>Placement]</a></span>
    </dt>
    <dd>{{% md %}}The placement of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ram_<wbr>disk_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the RAM disk.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>group_<wbr>names</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tag_<wbr>specifications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplatetagspecification">List[Get<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification]</a></span>
    </dt>
    <dd>{{% md %}}The tags to apply to the resources during launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}(Optional) A mapping of tags to assign to the launch template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Base64-encoded user data to provide when launching the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of security group IDs to associate with.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateBlockDeviceMapping">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateBlockDeviceMapping">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ebs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemappingeb">List&lt;Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Eb<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>No<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ebs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemappingeb">[]Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Eb</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>No<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ebs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemappingeb">Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Eb[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>no<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ebs</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateblockdevicemappingeb">List[Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Eb]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>no<wbr>Device</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Eb</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateBlockDeviceMappingEb">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateBlockDeviceMappingEb">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateCreditSpecification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateCreditSpecification">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cpu<wbr>Credits</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cpu<wbr>Credits</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cpu<wbr>Credits</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cpu<wbr>Credits</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateElasticGpuSpecification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateElasticGpuSpecification">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetLaunchTemplateFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateFilter">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>values</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Set of values that are accepted for the given filter field. Results will be selected if any given value matches.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Hibernation<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateHibernationOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateHibernationOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Configured</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Configured</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>configured</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>configured</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateIamInstanceProfile">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateIamInstanceProfile">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN) of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the filter field. Valid values can be found in the [EC2 DescribeLaunchTemplates API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateInstanceMarketOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateInstanceMarketOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Market<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoptionspotoption">List&lt;Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option<wbr>Spot<wbr>Option<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Market<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoptionspotoption">[]Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option<wbr>Spot<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>market<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spot<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoptionspotoption">Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option<wbr>Spot<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>market<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spot_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchtemplateinstancemarketoptionspotoption">List[Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option<wbr>Spot<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Option<wbr>Spot<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateInstanceMarketOptionSpotOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateInstanceMarketOptionSpotOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Block<wbr>Duration<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spot<wbr>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Valid<wbr>Until</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Block<wbr>Duration<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spot<wbr>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Valid<wbr>Until</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>block<wbr>Duration<wbr>Minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spot<wbr>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>valid<wbr>Until</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>block_<wbr>duration_<wbr>minutes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Interruption<wbr>Behavior</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spot<wbr>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>valid_<wbr>until</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Metadata<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateMetadataOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateMetadataOption">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The state of the metadata service: `enabled`, `disabled`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Put<wbr>Response<wbr>Hop<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The desired HTTP PUT response hop limit for instance metadata requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If session tokens are required: `optional`, `required`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The state of the metadata service: `enabled`, `disabled`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Put<wbr>Response<wbr>Hop<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The desired HTTP PUT response hop limit for instance metadata requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Http<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If session tokens are required: `optional`, `required`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The state of the metadata service: `enabled`, `disabled`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Put<wbr>Response<wbr>Hop<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The desired HTTP PUT response hop limit for instance metadata requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If session tokens are required: `optional`, `required`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The state of the metadata service: `enabled`, `disabled`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Put<wbr>Response<wbr>Hop<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The desired HTTP PUT response hop limit for instance metadata requests.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>http<wbr>Tokens</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If session tokens are required: `optional`, `required`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Monitoring</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateMonitoring">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateMonitoring">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateNetworkInterface">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv4Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv4Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv6Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv6Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv4Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv4Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv6Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Ipv6Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Network<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>device<wbr>Index</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv4Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv4Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv6Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv6Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network<wbr>Interface<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>associate_<wbr>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the launch template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>device_<wbr>index</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv4Address<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv4Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv6_<wbr>address_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>ipv6_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>network_<wbr>interface_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>private_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Placement</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplatePlacement">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplatePlacement">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spread<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Spread<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spread<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>affinity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>availability_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>host_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>spread<wbr>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchTemplateTagSpecification">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchTemplateTagSpecification">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags, each pair of which must exactly match a pair on the desired Launch Template.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







