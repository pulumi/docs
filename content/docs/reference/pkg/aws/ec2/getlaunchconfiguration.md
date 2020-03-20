
---
title: "GetLaunchConfiguration"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides information about a Launch Configuration.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ubuntu = aws.ec2.getLaunchConfiguration({
    name: "test-launch-config",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/launch_configuration.html.markdown.





## Using GetLaunchConfiguration

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getLaunchConfiguration<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetLaunchConfigurationArgs">GetLaunchConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetLaunchConfigurationResult">GetLaunchConfigurationResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_launch_configuration(</span>name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupLaunchConfiguration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LookupLaunchConfigurationArgs">LookupLaunchConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LookupLaunchConfigurationResult">LookupLaunchConfigurationResult</a></span>, error)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationResult.html">Pulumi.Aws.Ec2.GetLaunchConfigurationResult</a></span>> <span class="p">GetLaunchConfiguration(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationArgs.html">GetLaunchConfigurationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>



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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the launch configuration.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the launch configuration.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the launch configuration.
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetLaunchConfiguration Result

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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether a Public IP address is associated with the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The EBS Block Devices attached to the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Detailed Monitoring is Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The Ephemeral volumes on the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to associate with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 Image ID of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Instance Type of the instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Key Name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Tenancy of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationrootblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The Root Block Device of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated Security Group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Price to use for reserving Spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The User Data of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether a Public IP address is associated with the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationebsblockdevice">[]Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} The EBS Block Devices attached to the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Detailed Monitoring is Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationephemeralblockdevice">[]Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} The Ephemeral volumes on the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to associate with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 Image ID of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Instance Type of the instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Key Name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Tenancy of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationrootblockdevice">[]Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} The Root Block Device of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated Security Group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Price to use for reserving Spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The User Data of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether a Public IP address is associated with the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationebsblockdevice">ec2.<wbr>Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The EBS Block Devices attached to the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Whether Detailed Monitoring is Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationephemeralblockdevice">ec2.<wbr>Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Ephemeral volumes on the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to associate with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 Image ID of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Instance Type of the instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Key Name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Tenancy of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationrootblockdevice">ec2.<wbr>Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Root Block Device of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated Security Group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Price to use for reserving Spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The User Data of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associate_<wbr>public_<wbr>ip_<wbr>address</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether a Public IP address is associated with the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationebsblockdevice">List[Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} The EBS Block Devices attached to the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether Detailed Monitoring is Enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationephemeralblockdevice">List[Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Ephemeral volumes on the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IAM Instance Profile to associate with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 Image ID of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Instance Type of the instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Key Name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Tenancy of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#getlaunchconfigurationrootblockdevice">List[Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device]</a></code>
            </td>
            <td class="align-top">{{% md %}} The Root Block Device of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated Security Group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>price</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Price to use for reserving Spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The User Data of the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetLaunchConfigurationEbsBlockDevice
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchConfigurationEbsBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchConfigurationEbsBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationEbsBlockDevice.html">output</a> API doc for this type.
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
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Snapshot ID of the mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
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
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Snapshot ID of the mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
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
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Snapshot ID of the mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
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
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Snapshot ID of the mount.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetLaunchConfigurationEphemeralBlockDevice
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchConfigurationEphemeralBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchConfigurationEphemeralBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationEphemeralBlockDevice.html">output</a> API doc for this type.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Virtual Name of the device.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Virtual Name of the device.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Virtual Name of the device.
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
 (Required)
The Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Virtual Name of the device.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetLaunchConfigurationRootBlockDevice
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchConfigurationRootBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#GetLaunchConfigurationRootBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationRootBlockDevice.html">output</a> API doc for this type.
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
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
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
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
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
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
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
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the EBS Volume will be deleted on instance termination.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether the volume is Encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The provisioned IOPs of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Size of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Type of the volume.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







