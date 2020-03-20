
---
title: "NodeGroup"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages an EKS Node Group, which can provision and optionally update an Auto Scaling Group of Kubernetes worker nodes compatible with EKS. Additional documentation about this functionality can be found in the [EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html).

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/eks_node_group.html.markdown.



## Create a NodeGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/eks/#NodeGroup">NodeGroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/eks/#NodeGroupArgs">NodeGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NodeGroup</span><span class="p">(resource_name, opts=None, </span>ami_type=None<span class="p">, </span>cluster_name=None<span class="p">, </span>disk_size=None<span class="p">, </span>instance_types=None<span class="p">, </span>labels=None<span class="p">, </span>node_group_name=None<span class="p">, </span>node_role_arn=None<span class="p">, </span>release_version=None<span class="p">, </span>remote_access=None<span class="p">, </span>scaling_config=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNodeGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupArgs">NodeGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroup">NodeGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroup.html">NodeGroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupArgs.html">NodeGroupArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a NodeGroup resource with the given unique name, arguments, and options.

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
            <td class="align-top">Ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disk<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Release<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Remote<wbr>Access<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Scaling<wbr>Config<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
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
            <td class="align-top">Ami<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disk<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Types</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Release<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">*Node<wbr>Group<wbr>Remote<wbr>Access</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Node<wbr>Group<wbr>Scaling<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
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
            <td class="align-top">ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disk<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">release<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">eks.<wbr>Node<wbr>Group<wbr>Remote<wbr>Access?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">eks.<wbr>Node<wbr>Group<wbr>Scaling<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
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
            <td class="align-top">ami_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disk_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>types</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">release_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote_<wbr>access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">Dict[Node<wbr>Group<wbr>Remote<wbr>Access]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Dict[Node<wbr>Group<wbr>Scaling<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
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







## NodeGroup Output Properties

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
            <td class="align-top">Ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disk<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Release<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Remote<wbr>Access?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">List&lt;Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Resource&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Scaling<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disk<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Release<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">*Node<wbr>Group<wbr>Remote<wbr>Access</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">[]Node<wbr>Group<wbr>Resource</a></code>
            </td>
            <td class="align-top">{{% md %}} List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Node<wbr>Group<wbr>Scaling<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disk<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">release<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">eks.<wbr>Node<wbr>Group<wbr>Remote<wbr>Access?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">eks.<wbr>Node<wbr>Group<wbr>Resource[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">eks.<wbr>Node<wbr>Group<wbr>Scaling<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">ami_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disk_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>types</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">release_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote_<wbr>access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">Dict[Node<wbr>Group<wbr>Remote<wbr>Access]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">List[Node<wbr>Group<wbr>Resource]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Dict[Node<wbr>Group<wbr>Scaling<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing NodeGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/eks/#NodeGroupState">NodeGroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/eks/#NodeGroup">NodeGroup</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>ami_type=None<span class="p">, </span>arn=None<span class="p">, </span>cluster_name=None<span class="p">, </span>disk_size=None<span class="p">, </span>instance_types=None<span class="p">, </span>labels=None<span class="p">, </span>node_group_name=None<span class="p">, </span>node_role_arn=None<span class="p">, </span>release_version=None<span class="p">, </span>remote_access=None<span class="p">, </span>resources=None<span class="p">, </span>scaling_config=None<span class="p">, </span>status=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>version=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNodeGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupState">NodeGroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroup">NodeGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroup.html">NodeGroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupState.html">NodeGroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing NodeGroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disk<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Release<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Remote<wbr>Access<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">List&lt;Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Resource<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Scaling<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
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
            <td class="align-top">Ami<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Disk<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Types</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Labels</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Release<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">*Node<wbr>Group<wbr>Remote<wbr>Access</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">[]Node<wbr>Group<wbr>Resource</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">*Node<wbr>Group<wbr>Scaling<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
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
            <td class="align-top">ami<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disk<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Types</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">release<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote<wbr>Access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">eks.<wbr>Node<wbr>Group<wbr>Remote<wbr>Access?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">eks.<wbr>Node<wbr>Group<wbr>Resource[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">eks.<wbr>Node<wbr>Group<wbr>Scaling<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
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
            <td class="align-top">ami_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">disk_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>types</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">labels</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of Kubernetes labels. Only labels that are applied with the EKS API are managed by this argument. Other Kubernetes labels applied to the EKS Node Group will not be managed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the IAM Role that provides permissions for the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">release_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AMI version of the EKS Node Group. Defaults to latest version for Kubernetes version.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote_<wbr>access</td>
            <td class="align-top">
                
                <code><a href="#nodegroupremoteaccess">Dict[Node<wbr>Group<wbr>Remote<wbr>Access]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with remote access settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resources</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresource">List[Node<wbr>Group<wbr>Resource]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about underlying resources.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scaling_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#nodegroupscalingconfig">Dict[Node<wbr>Group<wbr>Scaling<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with scaling settings. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Status of the EKS Node Group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifiers of EC2 Subnets to associate with the EKS Node Group. These subnets must have the following resource tag: `kubernetes.io/cluster/CLUSTER_NAME` (where `CLUSTER_NAME` is replaced with the name of the EKS Cluster).
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
Key-value mapping of resource tags.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
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










## Supporting Types

#### NodeGroupRemoteAccess
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#NodeGroupRemoteAccess">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NodeGroupRemoteAccess">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupRemoteAccessArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupRemoteAccessOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupRemoteAccessArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupRemoteAccess.html">output</a> API doc for this type.
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
            <td class="align-top">Ec2Ssh<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify `source_security_group_ids` when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify `ec2_ssh_key`, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
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
            <td class="align-top">Ec2Ssh<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify `source_security_group_ids` when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify `ec2_ssh_key`, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
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
            <td class="align-top">ec2Ssh<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify `source_security_group_ids` when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify `ec2_ssh_key`, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
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
            <td class="align-top">ec2Ssh<wbr>Key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
EC2 Key Pair name that provides access for SSH communication with the worker nodes in the EKS Node Group. If you specify this configuration, but do not specify `source_security_group_ids` when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set of EC2 Security Group IDs to allow SSH access (port 22) from on the worker nodes. If you specify `ec2_ssh_key`, but do not specify this configuration when you create an EKS Node Group, port 22 on the worker nodes is opened to the Internet (0.0.0.0/0).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### NodeGroupResource
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NodeGroupResource">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupResourceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupResource.html">output</a> API doc for this type.
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
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresourceautoscalinggroup">List&lt;Pulumi.<wbr>Aws.<wbr>Eks.<wbr>Node<wbr>Group<wbr>Resource<wbr>Autoscaling<wbr>Group<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about AutoScaling Groups.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the remote access EC2 Security Group.
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
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresourceautoscalinggroup">[]Node<wbr>Group<wbr>Resource<wbr>Autoscaling<wbr>Group</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about AutoScaling Groups.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Remote<wbr>Access<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the remote access EC2 Security Group.
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
            <td class="align-top">autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresourceautoscalinggroup">eks.<wbr>Node<wbr>Group<wbr>Resource<wbr>Autoscaling<wbr>Group[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about AutoScaling Groups.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote<wbr>Access<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the remote access EC2 Security Group.
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
            <td class="align-top">autoscaling_<wbr>groups</td>
            <td class="align-top">
                
                <code><a href="#nodegroupresourceautoscalinggroup">List[Node<wbr>Group<wbr>Resource<wbr>Autoscaling<wbr>Group]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of objects containing information about AutoScaling Groups.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">remote<wbr>Access<wbr>Security<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Identifier of the remote access EC2 Security Group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### NodeGroupResourceAutoscalingGroup
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NodeGroupResourceAutoscalingGroup">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupResourceAutoscalingGroupOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupResourceAutoscalingGroup.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the AutoScaling Group.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the AutoScaling Group.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the AutoScaling Group.
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
 (Optional)
Name of the AutoScaling Group.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### NodeGroupScalingConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#NodeGroupScalingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NodeGroupScalingConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupScalingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/eks?tab=doc#NodeGroupScalingConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupScalingConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Eks.NodeGroupScalingConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Desired<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Desired number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Maximum number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Minimum number of worker nodes.
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
            <td class="align-top">Desired<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Desired number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Max<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Maximum number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Min<wbr>Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Minimum number of worker nodes.
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
            <td class="align-top">desired<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Desired number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Maximum number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min<wbr>Size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Minimum number of worker nodes.
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
            <td class="align-top">desired<wbr>Size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Desired number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">max_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Maximum number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">min_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Minimum number of worker nodes.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







