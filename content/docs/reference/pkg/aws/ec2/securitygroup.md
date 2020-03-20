
---
title: "SecurityGroup"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>




## Create a SecurityGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#SecurityGroup">SecurityGroup</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#SecurityGroupArgs">SecurityGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">SecurityGroup</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>egress=None<span class="p">, </span>ingress=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>revoke_rules_on_delete=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSecurityGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroupArgs">SecurityGroupArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroup">SecurityGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroup.html">SecurityGroup</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroupArgs.html">SecurityGroupArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a SecurityGroup resource with the given unique name, arguments, and options.

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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Security<wbr>Group<wbr>Egress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Security<wbr>Group<wbr>Ingress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">[]Security<wbr>Group<wbr>Egress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">[]Security<wbr>Group<wbr>Ingress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">ec2.<wbr>Security<wbr>Group<wbr>Egress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">ec2.<wbr>Security<wbr>Group<wbr>Ingress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">List[Security<wbr>Group<wbr>Egress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">List[Security<wbr>Group<wbr>Ingress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revoke_<wbr>rules_<wbr>on_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## SecurityGroup Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the security group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Security<wbr>Group<wbr>Egress&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Security<wbr>Group<wbr>Ingress&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group. If omitted, this provider will
assign a random, unique name
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The VPC ID.
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
            <td class="align-top">{{% md %}} The ARN of the security group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">[]Security<wbr>Group<wbr>Egress</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">[]Security<wbr>Group<wbr>Ingress</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group. If omitted, this provider will
assign a random, unique name
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The VPC ID.
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
            <td class="align-top">{{% md %}} The ARN of the security group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">ec2.<wbr>Security<wbr>Group<wbr>Egress[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">ec2.<wbr>Security<wbr>Group<wbr>Ingress[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group. If omitted, this provider will
assign a random, unique name
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The VPC ID.
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
            <td class="align-top">{{% md %}} The ARN of the security group
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">List[Security<wbr>Group<wbr>Egress]</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">List[Security<wbr>Group<wbr>Ingress]</a></code>
            </td>
            <td class="align-top">{{% md %}} Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the security group. If omitted, this provider will
assign a random, unique name
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revoke_<wbr>rules_<wbr>on_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The VPC ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing SecurityGroup Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#SecurityGroupState">SecurityGroupState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#SecurityGroup">SecurityGroup</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>egress=None<span class="p">, </span>ingress=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>owner_id=None<span class="p">, </span>revoke_rules_on_delete=None<span class="p">, </span>tags=None<span class="p">, </span>vpc_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSecurityGroup<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroupState">SecurityGroupState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroup">SecurityGroup</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroup.html">SecurityGroup</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroupState.html">SecurityGroupState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing SecurityGroup resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the security group
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Security<wbr>Group<wbr>Egress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Security<wbr>Group<wbr>Ingress<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
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
The ARN of the security group
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">[]Security<wbr>Group<wbr>Egress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">[]Security<wbr>Group<wbr>Ingress</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
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
The ARN of the security group
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">ec2.<wbr>Security<wbr>Group<wbr>Egress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">ec2.<wbr>Security<wbr>Group<wbr>Ingress[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revoke<wbr>Rules<wbr>On<wbr>Delete</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
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
The ARN of the security group
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">egress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupegress">List[Security<wbr>Group<wbr>Egress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
egress rule. Each egress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ingress</td>
            <td class="align-top">
                
                <code><a href="#securitygroupingress">List[Security<wbr>Group<wbr>Ingress]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be specified multiple times for each
ingress rule. Each ingress block supports fields documented below.
This argument is processed in [attribute-as-blocks mode](https://www.terraform.io/docs/configuration/attr-as-blocks.html).
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
The name of the security group. If omitted, this provider will
assign a random, unique name
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
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The owner ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revoke_<wbr>rules_<wbr>on_<wbr>delete</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instruct this provider to revoke all of the
Security Groups attached ingress and egress rules before deleting the rule
itself. This is normally not needed, however certain AWS services such as
Elastic Map Reduce may automatically add required rules to security groups used
with the service, and those rules may contain a cyclic dependency that prevent
the security groups from being destroyed without removing the dependency first.
Default `false`
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The VPC ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### SecurityGroupEgress
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#SecurityGroupEgress">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#SecurityGroupEgress">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroupEgressArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroupEgressOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroupEgressArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroupEgress.html">output</a> API doc for this type.
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
            <td class="align-top">Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix<wbr>List<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Self</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
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
            <td class="align-top">Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>[]string</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix<wbr>List<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Self</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
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
            <td class="align-top">cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>string[]?</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix<wbr>List<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">self</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
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
            <td class="align-top">cidr_<wbr>blocks</td>
            <td class="align-top">
                
                <code>List[str]</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>blocks</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix_<wbr>list_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">self</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### SecurityGroupIngress
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#SecurityGroupIngress">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#SecurityGroupIngress">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroupIngressArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#SecurityGroupIngressOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroupIngressArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.SecurityGroupIngress.html">output</a> API doc for this type.
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
            <td class="align-top">Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix<wbr>List<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Self</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
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
            <td class="align-top">Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>[]string</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">From<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ipv6Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Prefix<wbr>List<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Self</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">To<wbr>Port</td>
            <td class="align-top">
                
                <code>int</code>
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
            <td class="align-top">cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>string[]?</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6Cidr<wbr>Blocks</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix<wbr>List<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">self</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to<wbr>Port</td>
            <td class="align-top">
                
                <code>number</code>
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
            <td class="align-top">cidr_<wbr>blocks</td>
            <td class="align-top">
                
                <code>List[str]</code>
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
The security group description. Defaults to
&#34;Managed by Pulumi&#34;. Cannot be &#34;&#34;. __NOTE__: This field maps to the AWS
`GroupDescription` attribute, for which there is no Update API. If you&#39;d like
to classify your security groups in a way that can be updated, use `tags`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">from_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ipv6_<wbr>cidr_<wbr>blocks</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">prefix_<wbr>list_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">self</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">to_<wbr>port</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







