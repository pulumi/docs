
---
title: "Cluster"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an ElastiCache Cluster resource, which manages a Memcached cluster or Redis instance.
For working with Redis (Cluster Mode Enabled) replication groups, see the
[`aws.elasticache.ReplicationGroup` resource](https://www.terraform.io/docs/providers/aws/r/elasticache_replication_group.html).

> **Note:** When you change an attribute, such as `node_type`, by default
it is applied in the next maintenance window. Because of this, this provider may report
a difference in its planning phase because the actual modification has not yet taken
place. You can use the `apply_immediately` flag to instruct the service to apply the
change immediately. Using `apply_immediately` can result in a brief downtime as the server reboots.
See the AWS Docs on [Modifying an ElastiCache Cache Cluster][2] for more information.

## Example Usage

### Memcached Cluster

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.elasticache.Cluster("example", {
    engine: "memcached",
    nodeType: "cache.m4.large",
    numCacheNodes: 2,
    parameterGroupName: "default.memcached1.4",
    port: 11211,
});
```

### Redis Instance

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.elasticache.Cluster("example", {
    engine: "redis",
    engineVersion: "3.2.10",
    nodeType: "cache.m4.large",
    numCacheNodes: 1,
    parameterGroupName: "default.redis3.2",
    port: 6379,
});
```

### Redis Cluster Mode Disabled Read Replica Instance

These inherit their settings from the replication group.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const replica = new aws.elasticache.Cluster("replica", {
    replicationGroupId: aws_elasticache_replication_group_example.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elasticache_cluster.html.markdown.



## Create a Cluster Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticache/#Cluster">Cluster</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticache/#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Cluster</span><span class="p">(resource_name, opts=None, </span>apply_immediately=None<span class="p">, </span>availability_zone=None<span class="p">, </span>az_mode=None<span class="p">, </span>cluster_id=None<span class="p">, </span>engine=None<span class="p">, </span>engine_version=None<span class="p">, </span>maintenance_window=None<span class="p">, </span>node_type=None<span class="p">, </span>notification_topic_arn=None<span class="p">, </span>num_cache_nodes=None<span class="p">, </span>parameter_group_name=None<span class="p">, </span>port=None<span class="p">, </span>preferred_availability_zones=None<span class="p">, </span>replication_group_id=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>security_group_names=None<span class="p">, </span>snapshot_arns=None<span class="p">, </span>snapshot_name=None<span class="p">, </span>snapshot_retention_limit=None<span class="p">, </span>snapshot_window=None<span class="p">, </span>subnet_group_name=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticache?tab=doc#ClusterArgs">ClusterArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticache?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticache.Cluster.html">Cluster</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticache.ClusterArgs.html">ClusterArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Az<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">az_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">num_<wbr>cache_<wbr>nodes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>retention_<wbr>limit</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticache.<wbr>Cluster<wbr>Cache<wbr>Node&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">[]Cluster<wbr>Cache<wbr>Node</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">elasticache.<wbr>Cluster<wbr>Cache<wbr>Node[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Address</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification<wbr>Topic<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Group<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">availability_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">az_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache_<wbr>nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">List[Cluster<wbr>Cache<wbr>Node]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>address</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Group identifier. ElastiCache converts
this name to lowercase
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration_<wbr>endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} (Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">node_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The compute and memory capacity of the nodes. See
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">notification_<wbr>topic_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} An Amazon Resource Name (ARN) of an
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">num_<wbr>cache_<wbr>nodes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameter_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the parameter group to associate
with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} One or more VPC security groups associated
with the cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>group_<wbr>names</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>retention_<wbr>limit</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>group_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the subnet group to be used
for the cache cluster.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
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

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticache/#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticache/#Cluster">Cluster</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>apply_immediately=None<span class="p">, </span>arn=None<span class="p">, </span>availability_zone=None<span class="p">, </span>az_mode=None<span class="p">, </span>cache_nodes=None<span class="p">, </span>cluster_address=None<span class="p">, </span>cluster_id=None<span class="p">, </span>configuration_endpoint=None<span class="p">, </span>engine=None<span class="p">, </span>engine_version=None<span class="p">, </span>maintenance_window=None<span class="p">, </span>node_type=None<span class="p">, </span>notification_topic_arn=None<span class="p">, </span>num_cache_nodes=None<span class="p">, </span>parameter_group_name=None<span class="p">, </span>port=None<span class="p">, </span>preferred_availability_zones=None<span class="p">, </span>replication_group_id=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>security_group_names=None<span class="p">, </span>snapshot_arns=None<span class="p">, </span>snapshot_name=None<span class="p">, </span>snapshot_retention_limit=None<span class="p">, </span>snapshot_window=None<span class="p">, </span>subnet_group_name=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetCluster<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticache?tab=doc#ClusterState">ClusterState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticache?tab=doc#Cluster">Cluster</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticache.Cluster.html">Cluster</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticache.ClusterState.html">ClusterState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticache.<wbr>Cluster<wbr>Cache<wbr>Node<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
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
(Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
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
(Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Az<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">[]Cluster<wbr>Cache<wbr>Node</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
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
(Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
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
(Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">az<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">elasticache.<wbr>Cluster<wbr>Cache<wbr>Node[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
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
(Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
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
(Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">num<wbr>Cache<wbr>Nodes</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred<wbr>Availability<wbr>Zones</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication<wbr>Group<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Arns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Retention<wbr>Limit</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Window</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any database modifications
are applied immediately, or during the next maintenance window. Default is
`false`. See [Amazon ElastiCache Documentation for more information.][1]
(Available since v0.6.0)
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">az_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether the nodes in this Memcached node group are created in a single Availability Zone or created across multiple Availability Zones in the cluster&#39;s region. Valid values for this parameter are `single-az` or `cross-az`, default is `single-az`. If you want to choose `cross-az`, `num_cache_nodes` must be greater than `1`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cache_<wbr>nodes</td>
            <td class="align-top">
                
                <code><a href="#clustercachenode">List[Cluster<wbr>Cache<wbr>Node]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of node objects including `id`, `address`, `port` and `availability_zone`.
Referenceable e.g. as `${aws_elasticache_cluster.bar.cache_nodes.0.address}`
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
(Memcached only) The DNS name of the cache cluster without the port appended.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cluster_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Group identifier. ElastiCache converts
this name to lowercase
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
(Memcached only) The configuration endpoint to allow host discovery.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the cache engine to be used for this cache cluster.
Valid values for this parameter are `memcached` or `redis`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Version number of the cache engine to be used.
See [Describe Cache Engine Versions](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-cache-engine-versions.html)
in the AWS Documentation center for supported versions
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
Specifies the weekly time range for when maintenance
on the cache cluster is performed. The format is `ddd:hh24:mi-ddd:hh24:mi` (24H Clock UTC).
The minimum maintenance window is a 60 minute period. Example: `sun:05:00-sun:09:00`
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
[Available Cache Node Types](https://aws.amazon.com/elasticache/details#Available_Cache_Node_Types) for
supported node types
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
SNS topic to send ElastiCache notifications to. Example:
`arn:aws:sns:us-east-1:012345678999:my_sns_topic`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">num_<wbr>cache_<wbr>nodes</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The initial number of cache nodes that the
cache cluster will have. For Redis, this value must be 1. For Memcache, this
value must be between 1 and 20. If this number is reduced on subsequent runs,
the highest numbered nodes will be removed.
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
with this cache cluster
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">preferred_<wbr>availability_<wbr>zones</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Availability Zones in which cache nodes are created. If you are creating your cluster in an Amazon VPC you can only locate nodes in Availability Zones that are associated with the subnets in the selected subnet group. The number of Availability Zones listed must equal the value of `num_cache_nodes`. If you want all the nodes in the same Availability Zone, use `availability_zone` instead, or repeat the Availability Zone multiple times in the list. Default: System chosen Availability Zones. Detecting drift of existing node availability zone is not currently supported. Updating this argument by itself to migrate existing node availability zones is not currently supported and will show a perpetual difference.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">replication_<wbr>group_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the replication group to which this cluster should belong. If this parameter is specified, the cluster is added to the specified replication group as a read replica; otherwise, the cluster is a standalone primary that is not part of any replication group.
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
with the cache cluster
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
List of security group
names to associate with this cache cluster
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>arns</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A single-element string list containing an
Amazon Resource Name (ARN) of a Redis RDB snapshot file stored in Amazon S3.
Example: `arn:aws:s3:::my_bucket/snapshot1.rdb`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of a snapshot from which to restore data into the new node group.  Changing the `snapshot_name` forces a new resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>retention_<wbr>limit</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of days for which ElastiCache will
retain automatic cache cluster snapshots before deleting them. For example, if you set
SnapshotRetentionLimit to 5, then a snapshot that was taken today will be retained for 5 days
before being deleted. If the value of SnapshotRetentionLimit is set to zero (0), backups are turned off.
Please note that setting a `snapshot_retention_limit` is not supported on cache.t1.micro or cache.t2.* cache nodes
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>window</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The daily time range (in UTC) during which ElastiCache will
begin taking a daily snapshot of your cache cluster. Example: 05:00-09:00
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
Name of the subnet group to be used
for the cache cluster.
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
A mapping of tags to assign to the resource
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ClusterCacheNode
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ClusterCacheNode">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticache?tab=doc#ClusterCacheNodeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticache.ClusterCacheNode.html">output</a> API doc for this type.
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
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
The Availability Zone for the cache cluster. If you want to create cache nodes in multi-az, use `preferred_availability_zones` instead. Default: System chosen Availability Zone.
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
The port number on which each of the cache nodes will accept connections. For Memcache the default is 11211, and for Redis the default port is 6379. Cannot be provided with `replication_group_id`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







