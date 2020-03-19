
---
title: "LaunchTemplate"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an EC2 launch template resource. Can be used to create instances or auto scaling groups.

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_template.html.markdown.



## Create a LaunchTemplate Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchTemplate">LaunchTemplate</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchTemplateArgs">LaunchTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">LaunchTemplate</span><span class="p">(resource_name, opts=None, </span>block_device_mappings=None<span class="p">, </span>capacity_reservation_specification=None<span class="p">, </span>cpu_options=None<span class="p">, </span>credit_specification=None<span class="p">, </span>description=None<span class="p">, </span>disable_api_termination=None<span class="p">, </span>ebs_optimized=None<span class="p">, </span>elastic_gpu_specifications=None<span class="p">, </span>elastic_inference_accelerator=None<span class="p">, </span>iam_instance_profile=None<span class="p">, </span>image_id=None<span class="p">, </span>instance_initiated_shutdown_behavior=None<span class="p">, </span>instance_market_options=None<span class="p">, </span>instance_type=None<span class="p">, </span>kernel_id=None<span class="p">, </span>key_name=None<span class="p">, </span>license_specifications=None<span class="p">, </span>monitoring=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>placement=None<span class="p">, </span>ram_disk_id=None<span class="p">, </span>security_group_names=None<span class="p">, </span>tag_specifications=None<span class="p">, </span>tags=None<span class="p">, </span>user_data=None<span class="p">, </span>vpc_security_group_ids=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLaunchTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateArgs">LaunchTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplate">LaunchTemplate</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplate.html">LaunchTemplate</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateArgs.html">LaunchTemplateArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a LaunchTemplate resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Monitoring<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Placement<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">[]ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">*ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">*ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">[]ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">*ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">*ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">[]ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">*ec2.<wbr>Launch<wbr>Template<wbr>Monitoring</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">[]ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">*ec2.<wbr>Launch<wbr>Template<wbr>Placement</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">[]ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">ec2.<wbr>Launch<wbr>Template<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">ec2.<wbr>Launch<wbr>Template<wbr>Placement?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block_<wbr>device_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">List[Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity_<wbr>reservation_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">Dict[Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">Dict[Launch<wbr>Template<wbr>Cpu<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credit_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">Dict[Launch<wbr>Template<wbr>Credit<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable_<wbr>api_<wbr>termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>gpu_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">List[Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>inference_<wbr>accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">Dict[Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">Dict[Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>initiated_<wbr>shutdown_<wbr>behavior</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>market_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">Dict[Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">List[Launch<wbr>Template<wbr>License<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">Dict[Launch<wbr>Template<wbr>Monitoring]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">List[Launch<wbr>Template<wbr>Network<wbr>Interface]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">Dict[Launch<wbr>Template<wbr>Placement]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ram_<wbr>disk_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">List[Launch<wbr>Template<wbr>Tag<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## LaunchTemplate Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Version</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile?</a></code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latest<wbr>Version</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Placement?</a></code>
            </td>
            <td class="align-top">{{% md %}} The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">[]ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">*ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">*ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Version</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">[]ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">*ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">*ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile</a></code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latest<wbr>Version</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">[]ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">*ec2.<wbr>Launch<wbr>Template<wbr>Monitoring</a></code>
            </td>
            <td class="align-top">{{% md %}} The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">[]ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">*ec2.<wbr>Launch<wbr>Template<wbr>Placement</a></code>
            </td>
            <td class="align-top">{{% md %}} The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">[]ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Version</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile?</a></code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latest<wbr>Version</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">ec2.<wbr>Launch<wbr>Template<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">ec2.<wbr>Launch<wbr>Template<wbr>Placement?</a></code>
            </td>
            <td class="align-top">{{% md %}} The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>device_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">List[Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity_<wbr>reservation_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">Dict[Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">Dict[Launch<wbr>Template<wbr>Cpu<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credit_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">Dict[Launch<wbr>Template<wbr>Credit<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>version</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable_<wbr>api_<wbr>termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>gpu_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">List[Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>inference_<wbr>accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">Dict[Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">Dict[Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile]</a></code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>initiated_<wbr>shutdown_<wbr>behavior</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>market_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">Dict[Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latest_<wbr>version</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">List[Launch<wbr>Template<wbr>License<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">Dict[Launch<wbr>Template<wbr>Monitoring]</a></code>
            </td>
            <td class="align-top">{{% md %}} The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">List[Launch<wbr>Template<wbr>Network<wbr>Interface]</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">Dict[Launch<wbr>Template<wbr>Placement]</a></code>
            </td>
            <td class="align-top">{{% md %}} The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ram_<wbr>disk_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">List[Launch<wbr>Template<wbr>Tag<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing LaunchTemplate Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchTemplateState">LaunchTemplateState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchTemplate">LaunchTemplate</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>block_device_mappings=None<span class="p">, </span>capacity_reservation_specification=None<span class="p">, </span>cpu_options=None<span class="p">, </span>credit_specification=None<span class="p">, </span>default_version=None<span class="p">, </span>description=None<span class="p">, </span>disable_api_termination=None<span class="p">, </span>ebs_optimized=None<span class="p">, </span>elastic_gpu_specifications=None<span class="p">, </span>elastic_inference_accelerator=None<span class="p">, </span>iam_instance_profile=None<span class="p">, </span>image_id=None<span class="p">, </span>instance_initiated_shutdown_behavior=None<span class="p">, </span>instance_market_options=None<span class="p">, </span>instance_type=None<span class="p">, </span>kernel_id=None<span class="p">, </span>key_name=None<span class="p">, </span>latest_version=None<span class="p">, </span>license_specifications=None<span class="p">, </span>monitoring=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>network_interfaces=None<span class="p">, </span>placement=None<span class="p">, </span>ram_disk_id=None<span class="p">, </span>security_group_names=None<span class="p">, </span>tag_specifications=None<span class="p">, </span>tags=None<span class="p">, </span>user_data=None<span class="p">, </span>vpc_security_group_ids=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetLaunchTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateState">LaunchTemplateState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplate">LaunchTemplate</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplate.html">LaunchTemplate</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateState.html">LaunchTemplateState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing LaunchTemplate resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Version</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latest<wbr>Version</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Monitoring<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Placement<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">[]ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">*ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">*ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Version</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">[]ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">*ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">*ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Latest<wbr>Version</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">License<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">[]ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">*ec2.<wbr>Launch<wbr>Template<wbr>Monitoring</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">[]ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">*ec2.<wbr>Launch<wbr>Template<wbr>Placement</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">[]ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">ec2.<wbr>Launch<wbr>Template<wbr>Cpu<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credit<wbr>Specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">ec2.<wbr>Launch<wbr>Template<wbr>Credit<wbr>Specification?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Version</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable<wbr>Api<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Gpu<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Inference<wbr>Accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">ec2.<wbr>Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">ec2.<wbr>Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Initiated<wbr>Shutdown<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Market<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latest<wbr>Version</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">ec2.<wbr>Launch<wbr>Template<wbr>License<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">ec2.<wbr>Launch<wbr>Template<wbr>Monitoring?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">ec2.<wbr>Launch<wbr>Template<wbr>Network<wbr>Interface[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">ec2.<wbr>Launch<wbr>Template<wbr>Placement?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ram<wbr>Disk<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag<wbr>Specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">ec2.<wbr>Launch<wbr>Template<wbr>Tag<wbr>Specification[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>device_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemapping">List[Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specify volumes to attach to the instance besides the volumes specified by the AMI.
See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity_<wbr>reservation_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecification">Dict[Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Targeting for EC2 capacity reservations. See Capacity Reservation Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cpu_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecpuoptions">Dict[Launch<wbr>Template<wbr>Cpu<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The CPU options for the instance. See CPU Options below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">credit_<wbr>specification</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecreditspecification">Dict[Launch<wbr>Template<wbr>Credit<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize the credit specification of the instance. See Credit
Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>version</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disable_<wbr>api_<wbr>termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, enables [EC2 Instance
Termination Protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#Using_ChangingDisableAPITermination)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If `true`, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>gpu_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticgpuspecification">List[Launch<wbr>Template<wbr>Elastic<wbr>Gpu<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The elastic GPU to attach to the instance. See Elastic GPU
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>inference_<wbr>accelerator</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateelasticinferenceaccelerator">Dict[Launch<wbr>Template<wbr>Elastic<wbr>Inference<wbr>Accelerator]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing an Elastic Inference Accelerator to attach to the instance. See Elastic Inference Accelerator below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateiaminstanceprofile">Dict[Launch<wbr>Template<wbr>Iam<wbr>Instance<wbr>Profile]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM Instance Profile to launch the instance with. See Instance Profile
below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AMI from which to launch the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>initiated_<wbr>shutdown_<wbr>behavior</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Shutdown behavior for the instance. Can be `stop` or `terminate`.
(Default: `stop`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>market_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptions">Dict[Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The market (purchasing) option for the instance. See Market Options
below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The kernel ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name to use for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">latest_<wbr>version</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The latest version of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">license_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatelicensespecification">List[Launch<wbr>Template<wbr>License<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of license specifications to associate with. See License Specification below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">monitoring</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatemonitoring">Dict[Launch<wbr>Template<wbr>Monitoring]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The monitoring option for the instance. See Monitoring below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>interfaces</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatenetworkinterface">List[Launch<wbr>Template<wbr>Network<wbr>Interface]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize network interfaces to be attached at instance boot time. See Network
Interfaces below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateplacement">Dict[Launch<wbr>Template<wbr>Placement]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The placement of the instance. See Placement below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ram_<wbr>disk_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the RAM disk.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group names to associate with. If you are creating Instances in a VPC, use
`vpc_security_group_ids` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tag_<wbr>specifications</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatetagspecification">List[Launch<wbr>Template<wbr>Tag<wbr>Specification]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tags to apply to the resources during launch. See Tag Specifications below for more details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Base64-encoded user data to provide when launching the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of security group IDs to associate with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### LaunchTemplateBlockDeviceMapping
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateBlockDeviceMapping">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateBlockDeviceMapping">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateBlockDeviceMappingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateBlockDeviceMappingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateBlockDeviceMappingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateBlockDeviceMapping.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the device to mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemappingebs">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Ebs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configure EBS volume properties.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">No<wbr>Device</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Suppresses the specified device included in the AMI&#39;s block device mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Instance Store Device
Name](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
(e.g. `&#34;ephemeral0&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the device to mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemappingebs">*ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Ebs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configure EBS volume properties.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">No<wbr>Device</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Suppresses the specified device included in the AMI&#39;s block device mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Instance Store Device
Name](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
(e.g. `&#34;ephemeral0&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">device<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the device to mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemappingebs">ec2.<wbr>Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Ebs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configure EBS volume properties.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">no<wbr>Device</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Suppresses the specified device included in the AMI&#39;s block device mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Instance Store Device
Name](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
(e.g. `&#34;ephemeral0&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the device to mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateblockdevicemappingebs">Dict[Launch<wbr>Template<wbr>Block<wbr>Device<wbr>Mapping<wbr>Ebs]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configure EBS volume properties.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">no<wbr>Device</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Suppresses the specified device included in the AMI&#39;s block device mapping.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [Instance Store Device
Name](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
(e.g. `&#34;ephemeral0&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateBlockDeviceMappingEbs
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateBlockDeviceMappingEbs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateBlockDeviceMappingEbs">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateBlockDeviceMappingEbsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateBlockDeviceMappingEbsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateBlockDeviceMappingEbsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateBlockDeviceMappingEbs.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateCapacityReservationSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateCapacityReservationSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateCapacityReservationSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCapacityReservationSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCapacityReservationSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCapacityReservationSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCapacityReservationSpecification.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Preference</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecificationcapacityreservationtarget">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification<wbr>Capacity<wbr>Reservation<wbr>Target<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Preference</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecificationcapacityreservationtarget">*ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification<wbr>Capacity<wbr>Reservation<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Preference</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecificationcapacityreservationtarget">ec2.<wbr>Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification<wbr>Capacity<wbr>Reservation<wbr>Target?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Preference</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Target</td>
            <td class="align-top">
                
                <code><a href="#launchtemplatecapacityreservationspecificationcapacityreservationtarget">Dict[Launch<wbr>Template<wbr>Capacity<wbr>Reservation<wbr>Specification<wbr>Capacity<wbr>Reservation<wbr>Target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCapacityReservationSpecificationCapacityReservationTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCapacityReservationSpecificationCapacityReservationTarget.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Capacity<wbr>Reservation<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">capacity<wbr>Reservation<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateCpuOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateCpuOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateCpuOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCpuOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCpuOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCpuOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCpuOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Core<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Threads<wbr>Per<wbr>Core</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Core<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Threads<wbr>Per<wbr>Core</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">core<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">threads<wbr>Per<wbr>Core</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">core<wbr>Count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">threads<wbr>Per<wbr>Core</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateCreditSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateCreditSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateCreditSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCreditSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateCreditSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCreditSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateCreditSpecification.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cpu<wbr>Credits</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Cpu<wbr>Credits</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cpu<wbr>Credits</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">cpu<wbr>Credits</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateElasticGpuSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateElasticGpuSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateElasticGpuSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateElasticGpuSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateElasticGpuSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateElasticGpuSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateElasticGpuSpecification.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateElasticInferenceAccelerator
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateElasticInferenceAccelerator">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateElasticInferenceAccelerator">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateElasticInferenceAcceleratorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateElasticInferenceAcceleratorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateElasticInferenceAcceleratorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateElasticInferenceAccelerator.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Accelerator type.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateIamInstanceProfile
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateIamInstanceProfile">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateIamInstanceProfile">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateIamInstanceProfileArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateIamInstanceProfileOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateIamInstanceProfileArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateIamInstanceProfile.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the launch template. If you leave this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateInstanceMarketOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateInstanceMarketOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateInstanceMarketOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateInstanceMarketOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateInstanceMarketOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateInstanceMarketOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateInstanceMarketOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Market<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptionsspotoptions">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options<wbr>Spot<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Market<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptionsspotoptions">*ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options<wbr>Spot<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">market<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptionsspotoptions">ec2.<wbr>Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options<wbr>Spot<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">market<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#launchtemplateinstancemarketoptionsspotoptions">Dict[Launch<wbr>Template<wbr>Instance<wbr>Market<wbr>Options<wbr>Spot<wbr>Options]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateInstanceMarketOptionsSpotOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateInstanceMarketOptionsSpotOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateInstanceMarketOptionsSpotOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateInstanceMarketOptionsSpotOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateInstanceMarketOptionsSpotOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateInstanceMarketOptionsSpotOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateInstanceMarketOptionsSpotOptions.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Duration<wbr>Minutes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Interruption<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Valid<wbr>Until</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Block<wbr>Duration<wbr>Minutes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Interruption<wbr>Behavior</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Price</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Valid<wbr>Until</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block<wbr>Duration<wbr>Minutes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Interruption<wbr>Behavior</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">valid<wbr>Until</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">block_<wbr>duration_<wbr>minutes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Interruption<wbr>Behavior</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Price</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">valid_<wbr>until</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateLicenseSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateLicenseSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateLicenseSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateLicenseSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateLicenseSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateLicenseSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateLicenseSpecification.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">License<wbr>Configuration<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">License<wbr>Configuration<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">license<wbr>Configuration<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">license_<wbr>configuration_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateMonitoring
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateMonitoring">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateMonitoring">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateMonitoringArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateMonitoringOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateMonitoringArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateMonitoring.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateNetworkInterface
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateNetworkInterface">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateNetworkInterface">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateNetworkInterfaceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateNetworkInterfaceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateNetworkInterfaceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateNetworkInterface.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Index</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv4Address<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv4Addresses</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Address<wbr>Count</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Addresses</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interface<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Private<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Index</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv4Address<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv4Addresses</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Address<wbr>Count</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Addresses</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Interface<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Private<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Index</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv4Address<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv4Addresses</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Address<wbr>Count</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Addresses</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Interface<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">private<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">associate_<wbr>public_<wbr>ip_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device_<wbr>index</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv4Address<wbr>Count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv4Addresses</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>address_<wbr>count</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>addresses</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>interface_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">private_<wbr>ip_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplatePlacement
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplatePlacement">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplatePlacement">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplatePlacementArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplatePlacementOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplatePlacementArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplatePlacement.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spread<wbr>Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Affinity</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spread<wbr>Domain</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">affinity</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spread<wbr>Domain</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">affinity</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spread<wbr>Domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchTemplateTagSpecification
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchTemplateTagSpecification">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchTemplateTagSpecification">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateTagSpecificationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchTemplateTagSpecificationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateTagSpecificationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchTemplateTagSpecification.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">resource_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the launch template.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







