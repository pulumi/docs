
---
title: "Cluster"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a DAX Cluster resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const bar = new aws.dax.Cluster("bar", {
    clusterName: "cluster-example",
    iamRoleArn: aws_iam_role_example.arn,
    nodeType: "dax.r4.large",
    replicationFactor: 1,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dax_cluster.html.markdown.



## Create a Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/dax/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/dax/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>availability_zones=None<span class="p">, </span>cluster_name=None<span class="p">, </span>description=None<span class="p">, </span>iam_role_arn=None<span class="p">, </span>maintenance_window=None<span class="p">, </span>node_type=None<span class="p">, </span>notification_topic_arn=None<span class="p">, </span>parameter_group_name=None<span class="p">, </span>replication_factor=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>server_side_encryption=None<span class="p">, </span>subnet_group_name=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.ClusterArgs.html">ClusterArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Cluster resource with the given unique name, arguments, and options.

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
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
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
Group identifier. DAX converts this name to
lowercase
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">Pulumi.<wbr>Aws.<wbr>Dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
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
A mapping of tags to assign to the resource
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
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
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
Group identifier. DAX converts this name to
lowercase
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">*dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
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
A mapping of tags to assign to the resource
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
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
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
Group identifier. DAX converts this name to
lowercase
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
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
A mapping of tags to assign to the resource
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
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
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
Group identifier. DAX converts this name to
lowercase
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>factor</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">Dict[cluster_<wbr>server_<wbr>side_<wbr>encryption]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Cluster Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the DAX cluster without the port appended
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">List&lt;Pulumi.<wbr>Aws.<wbr>Dax.<wbr>Cluster<wbr>Node&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">Pulumi.<wbr>Aws.<wbr>Dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used for the
cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
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
            <td class="align-top">{{% md %}} The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the DAX cluster without the port appended
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">[]dax.<wbr>Cluster<wbr>Node</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">*dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used for the
cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
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
            <td class="align-top">{{% md %}} The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the DAX cluster without the port appended
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">dax.<wbr>Cluster<wbr>Node[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used for the
cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
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
            <td class="align-top">{{% md %}} The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name of the DAX cluster without the port appended
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">List[cluster_<wbr>node]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>factor</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">Dict[cluster_<wbr>server_<wbr>side_<wbr>encryption]</a></code>
            </td>
            <td class="align-top">{{% md %}} Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used for the
cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/dax/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/dax/#Cluster">Cluster</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>availability_zones=None<span class="p">, </span>cluster_address=None<span class="p">, </span>cluster_name=None<span class="p">, </span>configuration_endpoint=None<span class="p">, </span>description=None<span class="p">, </span>iam_role_arn=None<span class="p">, </span>maintenance_window=None<span class="p">, </span>node_type=None<span class="p">, </span>nodes=None<span class="p">, </span>notification_topic_arn=None<span class="p">, </span>parameter_group_name=None<span class="p">, </span>port=None<span class="p">, </span>replication_factor=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>server_side_encryption=None<span class="p">, </span>subnet_group_name=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Cluster resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the DAX cluster without the port appended
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
Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">List&lt;Pulumi.<wbr>Aws.<wbr>Dax.<wbr>Cluster<wbr>Node<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">Pulumi.<wbr>Aws.<wbr>Dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
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
A mapping of tags to assign to the resource
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
The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the DAX cluster without the port appended
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
Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">[]dax.<wbr>Cluster<wbr>Node</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">*dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
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
A mapping of tags to assign to the resource
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
The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the DAX cluster without the port appended
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
Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">dax.<wbr>Cluster<wbr>Node[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Factor</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">dax.<wbr>Cluster<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
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
A mapping of tags to assign to the resource
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
The ARN of the DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of Availability Zones in which the
nodes will be created
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name of the DAX cluster without the port appended
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
Group identifier. DAX converts this name to
lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The configuration endpoint for this DAX cluster,
consisting of a DNS name and a port number
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
Description for the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid Amazon Resource Name (ARN) that identifies
an IAM role. At runtime, DAX will assume this role and use the role&#39;s
permissions to access DynamoDB on your behalf
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies the weekly time range for when
maintenance on the cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi`
(24H Clock UTC). The minimum maintenance window is a 60 minute period. Example:
`sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute and memory capacity of the nodes. See
[Nodes][1] for supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nodes</td>
            <td class="align-top">
                
                <code><a href="#clusternode">List[cluster_<wbr>node]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and
`availability_zone`. Referenceable e.g. as
`${aws_dax_cluster.test.nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Amazon Resource Name (ARN) of an
SNS topic to send DAX notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the parameter group to associate
with this DAX cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>factor</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of nodes in the DAX cluster. A
replication factor of 1 will create a single-node cluster, without any read
replicas
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more VPC security groups associated
with the cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#clusterserversideencryption">Dict[cluster_<wbr>server_<wbr>side_<wbr>encryption]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encrypt at rest options
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the subnet group to be used for the
cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ClusterNode
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterNode">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#ClusterNodeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.ClusterNode.html">output</a> API doc for this type.
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
            <td class="align-top">Address</td>
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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
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
            <td class="align-top">Address</td>
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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
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
            <td class="align-top">address</td>
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
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
            <td class="align-top">address</td>
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port used by the configuration endpoint
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ClusterServerSideEncryption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ClusterServerSideEncryption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterServerSideEncryption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#ClusterServerSideEncryptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dax?tab=doc#ClusterServerSideEncryptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.ClusterServerSideEncryptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dax.ClusterServerSideEncryption.html">output</a> API doc for this type.
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
Whether to enable encryption at rest. Defaults to `false`.
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
Whether to enable encryption at rest. Defaults to `false`.
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
Whether to enable encryption at rest. Defaults to `false`.
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
Whether to enable encryption at rest. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







