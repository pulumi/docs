
---
title: "ConfigurationAggregator"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages an AWS Config Configuration Aggregator

## Example Usage

### Account Based Aggregation

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const account = new aws.cfg.ConfigurationAggregator("account", {
    accountAggregationSource: {
        accountIds: ["123456789012"],
        regions: ["us-west-2"],
    },
});
```

### Organization Based Aggregation

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const organizationRole = new aws.iam.Role("organization", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "config.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
`,
});
const organizationRolePolicyAttachment = new aws.iam.RolePolicyAttachment("organization", {
    policyArn: "arn:aws:iam::aws:policy/service-role/AWSConfigRoleForOrganizations",
    role: organizationRole.name,
});
const organizationConfigurationAggregator = new aws.cfg.ConfigurationAggregator("organization", {
    organizationAggregationSource: {
        allRegions: true,
        roleArn: organizationRole.arn,
    },
}, {dependsOn: [organizationRolePolicyAttachment]});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/config_configuration_aggregator.html.markdown.



## Create a ConfigurationAggregator Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#ConfigurationAggregator">ConfigurationAggregator</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#ConfigurationAggregatorArgs">ConfigurationAggregatorArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ConfigurationAggregator</span><span class="p">(resource_name, opts=None, </span>account_aggregation_source=None<span class="p">, </span>name=None<span class="p">, </span>organization_aggregation_source=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewConfigurationAggregator<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregatorArgs">ConfigurationAggregatorArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregator">ConfigurationAggregator</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregator.html">ConfigurationAggregator</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregatorArgs.html">ConfigurationAggregatorArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a ConfigurationAggregator resource with the given unique name, arguments, and options.

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
            <td class="align-top">Account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
            <td class="align-top">Account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">*Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">*Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
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
            <td class="align-top">account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
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
            <td class="align-top">account_<wbr>aggregation_<wbr>source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Dict[Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">organization_<wbr>aggregation_<wbr>source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Dict[Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
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
    
    </tbody>
</table>


{{% /lang %}}







## ConfigurationAggregator Output Properties

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
            <td class="align-top">Account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} The account(s) to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the aggregator
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} The organization to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
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
            <td class="align-top">Account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">*Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} The account(s) to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the aggregator
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">*Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} The organization to aggregate config data from as documented below.
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
            <td class="align-top">account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} The account(s) to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the aggregator
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} The organization to aggregate config data from as documented below.
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
            <td class="align-top">account_<wbr>aggregation_<wbr>source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Dict[Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} The account(s) to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the aggregator
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">organization_<wbr>aggregation_<wbr>source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Dict[Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} The organization to aggregate config data from as documented below.
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
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing ConfigurationAggregator Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#ConfigurationAggregatorState">ConfigurationAggregatorState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/cfg/#ConfigurationAggregator">ConfigurationAggregator</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>account_aggregation_source=None<span class="p">, </span>arn=None<span class="p">, </span>name=None<span class="p">, </span>organization_aggregation_source=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetConfigurationAggregator<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregatorState">ConfigurationAggregatorState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregator">ConfigurationAggregator</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregator.html">ConfigurationAggregator</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregatorState.html">ConfigurationAggregatorState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing ConfigurationAggregator resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The ARN of the aggregator
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the resource.
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
            <td class="align-top">Account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">*Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The ARN of the aggregator
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">*Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
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
            <td class="align-top">account<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The ARN of the aggregator
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">organization<wbr>Aggregation<wbr>Source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
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
            <td class="align-top">account_<wbr>aggregation_<wbr>source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatoraccountaggregationsource">Dict[Configuration<wbr>Aggregator<wbr>Account<wbr>Aggregation<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The account(s) to aggregate config data from as documented below.
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
The ARN of the aggregator
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
The name of the configuration aggregator.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">organization_<wbr>aggregation_<wbr>source</td>
            <td class="align-top">
                
                <code><a href="#configurationaggregatororganizationaggregationsource">Dict[Configuration<wbr>Aggregator<wbr>Organization<wbr>Aggregation<wbr>Source]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The organization to aggregate config data from as documented below.
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
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ConfigurationAggregatorAccountAggregationSource
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ConfigurationAggregatorAccountAggregationSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ConfigurationAggregatorAccountAggregationSource">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregatorAccountAggregationSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregatorAccountAggregationSourceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregatorAccountAggregationSourceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregatorAccountAggregationSource.html">output</a> API doc for this type.
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
            <td class="align-top">Account<wbr>Ids</td>
            <td class="align-top">
                
                <code>List<string></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of 12-digit account IDs of the account(s) being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">All<wbr>Regions</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regions</td>
            <td class="align-top">
                
                <code>List<string>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
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
            <td class="align-top">Account<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of 12-digit account IDs of the account(s) being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">All<wbr>Regions</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regions</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
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
            <td class="align-top">account<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of 12-digit account IDs of the account(s) being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">all<wbr>Regions</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regions</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
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
            <td class="align-top">account_<wbr>ids</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of 12-digit account IDs of the account(s) being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">all<wbr>Regions</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regions</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ConfigurationAggregatorOrganizationAggregationSource
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ConfigurationAggregatorOrganizationAggregationSource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ConfigurationAggregatorOrganizationAggregationSource">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregatorOrganizationAggregationSourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/cfg?tab=doc#ConfigurationAggregatorOrganizationAggregationSourceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregatorOrganizationAggregationSourceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Cfg.ConfigurationAggregatorOrganizationAggregationSource.html">output</a> API doc for this type.
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
            <td class="align-top">All<wbr>Regions</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regions</td>
            <td class="align-top">
                
                <code>List<string>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.
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
            <td class="align-top">All<wbr>Regions</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Regions</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.
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
            <td class="align-top">all<wbr>Regions</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regions</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.
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
            <td class="align-top">all<wbr>Regions</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, aggregate existing AWS Config regions and future regions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">regions</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of source regions being aggregated.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ARN of the IAM role used to retrieve AWS Organization details associated with the aggregator account.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







