
---
title: "MysqlLayer"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an OpsWorks MySQL layer resource.

> **Note:** All arguments including the root password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const db = new aws.opsworks.MysqlLayer("db", {
    stackId: aws_opsworks_stack_main.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/opsworks_mysql_layer.html.markdown.



## Create a MysqlLayer Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/opsworks/#MysqlLayer">MysqlLayer</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/opsworks/#MysqlLayerArgs">MysqlLayerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">MysqlLayer</span><span class="p">(resource_name, opts=None, </span>auto_assign_elastic_ips=None<span class="p">, </span>auto_assign_public_ips=None<span class="p">, </span>auto_healing=None<span class="p">, </span>custom_configure_recipes=None<span class="p">, </span>custom_deploy_recipes=None<span class="p">, </span>custom_instance_profile_arn=None<span class="p">, </span>custom_json=None<span class="p">, </span>custom_security_group_ids=None<span class="p">, </span>custom_setup_recipes=None<span class="p">, </span>custom_shutdown_recipes=None<span class="p">, </span>custom_undeploy_recipes=None<span class="p">, </span>drain_elb_on_shutdown=None<span class="p">, </span>ebs_volumes=None<span class="p">, </span>elastic_load_balancer=None<span class="p">, </span>install_updates_on_boot=None<span class="p">, </span>instance_shutdown_timeout=None<span class="p">, </span>name=None<span class="p">, </span>root_password=None<span class="p">, </span>root_password_on_all_instances=None<span class="p">, </span>stack_id=None<span class="p">, </span>system_packages=None<span class="p">, </span>use_ebs_optimized_instances=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMysqlLayer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/opsworks?tab=doc#MysqlLayerArgs">MysqlLayerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/opsworks?tab=doc#MysqlLayer">MysqlLayer</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Opsworks.MysqlLayer.html">MysqlLayer</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Opsworks.MysqlLayerArgs.html">MysqlLayerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a MysqlLayer resource with the given unique name, arguments, and options.

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
            <td class="align-top">Auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">List&lt;Pulumi.<wbr>Aws.<wbr>Opsworks.<wbr>Mysql<wbr>Layer<wbr>Ebs<wbr>Volume<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">System<wbr>Packages</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
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
            <td class="align-top">Auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">[]Mysql<wbr>Layer<wbr>Ebs<wbr>Volume</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">System<wbr>Packages</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
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
            <td class="align-top">auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">opsworks.<wbr>Mysql<wbr>Layer<wbr>Ebs<wbr>Volume[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">system<wbr>Packages</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
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
            <td class="align-top">auto_<wbr>assign_<wbr>elastic_<wbr>ips</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>assign_<wbr>public_<wbr>ips</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>healing</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>configure_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>deploy_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>instance_<wbr>profile_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>setup_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>shutdown_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>undeploy_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">drain_<wbr>elb_<wbr>on_<wbr>shutdown</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">List[Mysql<wbr>Layer<wbr>Ebs<wbr>Volume]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>load_<wbr>balancer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">install_<wbr>updates_<wbr>on_<wbr>boot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>shutdown_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>password_<wbr>on_<wbr>all_<wbr>instances</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stack_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">system_<wbr>packages</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use_<wbr>ebs_<wbr>optimized_<wbr>instances</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## MysqlLayer Output Properties

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
            <td class="align-top">Auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">List&lt;Pulumi.<wbr>Aws.<wbr>Opsworks.<wbr>Mysql<wbr>Layer<wbr>Ebs<wbr>Volume&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">System<wbr>Packages</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to use EBS-optimized instances.
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
            <td class="align-top">Auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">[]Mysql<wbr>Layer<wbr>Ebs<wbr>Volume</a></code>
            </td>
            <td class="align-top">{{% md %}} `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">System<wbr>Packages</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to use EBS-optimized instances.
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
            <td class="align-top">auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">opsworks.<wbr>Mysql<wbr>Layer<wbr>Ebs<wbr>Volume[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">system<wbr>Packages</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to use EBS-optimized instances.
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
            <td class="align-top">auto_<wbr>assign_<wbr>elastic_<wbr>ips</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>assign_<wbr>public_<wbr>ips</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>healing</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>configure_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>deploy_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>instance_<wbr>profile_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>setup_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>shutdown_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>undeploy_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">drain_<wbr>elb_<wbr>on_<wbr>shutdown</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">List[Mysql<wbr>Layer<wbr>Ebs<wbr>Volume]</a></code>
            </td>
            <td class="align-top">{{% md %}} `ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>load_<wbr>balancer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">install_<wbr>updates_<wbr>on_<wbr>boot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>shutdown_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>password_<wbr>on_<wbr>all_<wbr>instances</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stack_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">system_<wbr>packages</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use_<wbr>ebs_<wbr>optimized_<wbr>instances</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to use EBS-optimized instances.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing MysqlLayer Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/opsworks/#MysqlLayerState">MysqlLayerState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/opsworks/#MysqlLayer">MysqlLayer</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>auto_assign_elastic_ips=None<span class="p">, </span>auto_assign_public_ips=None<span class="p">, </span>auto_healing=None<span class="p">, </span>custom_configure_recipes=None<span class="p">, </span>custom_deploy_recipes=None<span class="p">, </span>custom_instance_profile_arn=None<span class="p">, </span>custom_json=None<span class="p">, </span>custom_security_group_ids=None<span class="p">, </span>custom_setup_recipes=None<span class="p">, </span>custom_shutdown_recipes=None<span class="p">, </span>custom_undeploy_recipes=None<span class="p">, </span>drain_elb_on_shutdown=None<span class="p">, </span>ebs_volumes=None<span class="p">, </span>elastic_load_balancer=None<span class="p">, </span>install_updates_on_boot=None<span class="p">, </span>instance_shutdown_timeout=None<span class="p">, </span>name=None<span class="p">, </span>root_password=None<span class="p">, </span>root_password_on_all_instances=None<span class="p">, </span>stack_id=None<span class="p">, </span>system_packages=None<span class="p">, </span>use_ebs_optimized_instances=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMysqlLayer<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/opsworks?tab=doc#MysqlLayerState">MysqlLayerState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/opsworks?tab=doc#MysqlLayer">MysqlLayer</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Opsworks.MysqlLayer.html">MysqlLayer</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Opsworks.MysqlLayerState.html">MysqlLayerState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing MysqlLayer resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">List&lt;Pulumi.<wbr>Aws.<wbr>Opsworks.<wbr>Mysql<wbr>Layer<wbr>Ebs<wbr>Volume<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">System<wbr>Packages</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
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
            <td class="align-top">Auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Json</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">[]Mysql<wbr>Layer<wbr>Ebs<wbr>Volume</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stack<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">System<wbr>Packages</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
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
            <td class="align-top">auto<wbr>Assign<wbr>Elastic<wbr>Ips</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Assign<wbr>Public<wbr>Ips</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Healing</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Configure<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Deploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Instance<wbr>Profile<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Json</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Security<wbr>Group<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Setup<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Shutdown<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom<wbr>Undeploy<wbr>Recipes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">drain<wbr>Elb<wbr>On<wbr>Shutdown</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">opsworks.<wbr>Mysql<wbr>Layer<wbr>Ebs<wbr>Volume[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic<wbr>Load<wbr>Balancer</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">install<wbr>Updates<wbr>On<wbr>Boot</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Shutdown<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Password</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Password<wbr>On<wbr>All<wbr>Instances</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stack<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">system<wbr>Packages</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Ebs<wbr>Optimized<wbr>Instances</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
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
            <td class="align-top">auto_<wbr>assign_<wbr>elastic_<wbr>ips</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to automatically assign an elastic IP address to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>assign_<wbr>public_<wbr>ips</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>healing</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable auto-healing for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>configure_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>deploy_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>instance_<wbr>profile_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of an IAM profile that will be used for the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>json</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Custom JSON attributes to apply to the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>security_<wbr>group_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Ids for a set of security groups to apply to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>setup_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>shutdown_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">custom_<wbr>undeploy_<wbr>recipes</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">drain_<wbr>elb_<wbr>on_<wbr>shutdown</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable Elastic Load Balancing connection draining.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>volumes</td>
            <td class="align-top">
                
                <code><a href="#mysqllayerebsvolume">List[Mysql<wbr>Layer<wbr>Ebs<wbr>Volume]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elastic_<wbr>load_<wbr>balancer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of an Elastic Load Balancer to attach to this layer
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">install_<wbr>updates_<wbr>on_<wbr>boot</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to install OS and package updates on each instance when it boots.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>shutdown_<wbr>timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.
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
A human-readable name for the layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Root password to use for MySQL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>password_<wbr>on_<wbr>all_<wbr>instances</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to set the root user password to all instances in the stack so they can access the instances in this layer.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stack_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The id of the stack the layer will belong to.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">system_<wbr>packages</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Names of a set of system packages to install on the layer&#39;s instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use_<wbr>ebs_<wbr>optimized_<wbr>instances</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to use EBS-optimized instances.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### MysqlLayerEbsVolume
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#MysqlLayerEbsVolume">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#MysqlLayerEbsVolume">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/opsworks?tab=doc#MysqlLayerEbsVolumeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/opsworks?tab=doc#MysqlLayerEbsVolumeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Opsworks.MysqlLayerEbsVolumeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Opsworks.MysqlLayerEbsVolume.html">output</a> API doc for this type.
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
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
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
            <td class="align-top">Mount<wbr>Point</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Disks</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Raid<wbr>Level</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
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
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
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
            <td class="align-top">Mount<wbr>Point</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Disks</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Raid<wbr>Level</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Size</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
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
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
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
            <td class="align-top">mount<wbr>Point</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Of<wbr>Disks</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">raid<wbr>Level</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">size</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
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
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
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
            <td class="align-top">mount<wbr>Point</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Of<wbr>Disks</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">raid<wbr>Level</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
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







