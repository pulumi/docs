
---
title: "MaintenanceWindowTarget"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an SSM Maintenance Window Target resource

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const window = new aws.ssm.MaintenanceWindow("window", {
    cutoff: 1,
    duration: 3,
    schedule: "cron(0 16 ? * TUE *)",
});
const target1 = new aws.ssm.MaintenanceWindowTarget("target1", {
    description: "This is a maintenance window target",
    resourceType: "INSTANCE",
    targets: [{
        key: "tag:Name",
        values: ["acceptance_test"],
    }],
    windowId: window.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/ssm_maintenance_window_target.html.markdown.



## Create a MaintenanceWindowTarget Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTarget">MaintenanceWindowTarget</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTargetArgs">MaintenanceWindowTargetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">MaintenanceWindowTarget</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>owner_information=None<span class="p">, </span>resource_type=None<span class="p">, </span>targets=None<span class="p">, </span>window_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMaintenanceWindowTarget<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTargetArgs">MaintenanceWindowTargetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTarget">MaintenanceWindowTarget</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTarget.html">MaintenanceWindowTarget</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTargetArgs.html">MaintenanceWindowTargetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a MaintenanceWindowTarget resource with the given unique name, arguments, and options.

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Information</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the target with.
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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Information</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the target with.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Information</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the target with.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>information</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">List[Maintenance<wbr>Window<wbr>Target<wbr>Target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The Id of the maintenance window to register the target with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## MaintenanceWindowTarget Output Properties

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Information</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the target with.
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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The description of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Information</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the target with.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Information</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the target with.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The description of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>information</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">List[Maintenance<wbr>Window<wbr>Target<wbr>Target]</a></code>
            </td>
            <td class="align-top">{{% md %}} The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Id of the maintenance window to register the target with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing MaintenanceWindowTarget Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTargetState">MaintenanceWindowTargetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ssm/#MaintenanceWindowTarget">MaintenanceWindowTarget</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>owner_information=None<span class="p">, </span>resource_type=None<span class="p">, </span>targets=None<span class="p">, </span>window_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMaintenanceWindowTarget<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTargetState">MaintenanceWindowTargetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTarget">MaintenanceWindowTarget</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTarget.html">MaintenanceWindowTarget</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTargetState.html">MaintenanceWindowTargetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing MaintenanceWindowTarget resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Information</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">List&lt;Pulumi.<wbr>Aws.<wbr>Ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the target with.
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
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Information</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">[]ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Window<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the target with.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Information</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">ssm.<wbr>Maintenance<wbr>Window<wbr>Target<wbr>Target[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the target with.
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
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The description of the maintenance window target.
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
The name of the maintenance window target.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>information</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">targets</td>
            <td class="align-top">
                
                <code><a href="#maintenancewindowtargettarget">List[Maintenance<wbr>Window<wbr>Target<wbr>Target]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The targets (either instances or tags). Instances are specified using Key=InstanceIds,Values=InstanceId1,InstanceId2. Tags are specified using Key=tag name,Values=tag value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">window_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Id of the maintenance window to register the target with.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### MaintenanceWindowTargetTarget
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MaintenanceWindowTargetTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MaintenanceWindowTargetTarget">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTargetTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ssm?tab=doc#MaintenanceWindowTargetTargetOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTargetTargetArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ssm.MaintenanceWindowTargetTarget.html">output</a> API doc for this type.
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
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
            <td class="align-top">Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
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
            <td class="align-top">key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







