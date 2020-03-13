
---
title: "WebAcl"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a WAF Web ACL Resource

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ipset = new aws.waf.IpSet("ipset", {
    ipSetDescriptors: [{
        type: "IPV4",
        value: "192.0.7.0/24",
    }],
});
const wafrule = new aws.waf.Rule("wafrule", {
    metricName: "tfWAFRule",
    predicates: [{
        dataId: ipset.id,
        negated: false,
        type: "IPMatch",
    }],
}, {dependsOn: [ipset]});
const wafAcl = new aws.waf.WebAcl("waf_acl", {
    defaultAction: {
        type: "ALLOW",
    },
    metricName: "tfWebACL",
    rules: [{
        action: {
            type: "BLOCK",
        },
        priority: 1,
        ruleId: wafrule.id,
        type: "REGULAR",
    }],
}, {dependsOn: [ipset, wafrule]});
```

### Logging

> *NOTE:* The Kinesis Firehose Delivery Stream name must begin with `aws-waf-logs-` and be located in `us-east-1` region. See the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) for more information about enabling WAF logging.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.waf.WebAcl("example", {
    // ... other configuration ...
    loggingConfiguration: {
        logDestination: aws_kinesis_firehose_delivery_stream_example.arn,
        redactedFields: {
            fieldToMatches: [
                {
                    type: "URI",
                },
                {
                    data: "referer",
                    type: "HEADER",
                },
            ],
        },
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/waf_web_acl.html.markdown.



## Create a WebAcl Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/waf/#WebAcl">WebAcl</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/waf/#WebAclArgs">WebAclArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">WebAcl</span><span class="p">(resource_name, id, opts=None, </span>default_action=None<span class="p">, </span>logging_configuration=None<span class="p">, </span>metric_name=None<span class="p">, </span>name=None<span class="p">, </span>rules=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewWebAcl<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclArgs">WebAclArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAcl">WebAcl</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAcl.html">WebAcl</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclArgs.html">WebAclArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a WebAcl resource with the given unique name, arguments, and options.

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
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">List&lt;Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
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
Key-value mapping of resource tags
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
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">*waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">[]waf.<wbr>Web<wbr>Acl<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
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
Key-value mapping of resource tags
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
            <td class="align-top">default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">waf.<wbr>Web<wbr>Acl<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
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
Key-value mapping of resource tags
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
            <td class="align-top">default_<wbr>action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">dict{web_<wbr>acl_<wbr>default_<wbr>action}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">dict{web_<wbr>acl_<wbr>logging_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">list[web_<wbr>acl_<wbr>rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## WebAcl Output Properties

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
            <td class="align-top">{{% md %}} The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description for the Amazon CloudWatch metric of this web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">List&lt;Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Rule&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">*waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description for the Amazon CloudWatch metric of this web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">[]waf.<wbr>Web<wbr>Acl<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description for the Amazon CloudWatch metric of this web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">waf.<wbr>Web<wbr>Acl<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">dict{web_<wbr>acl_<wbr>default_<wbr>action}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">dict{web_<wbr>acl_<wbr>logging_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name or description for the Amazon CloudWatch metric of this web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">list[web_<wbr>acl_<wbr>rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing WebAcl Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebAclState, opts?: pulumi.CustomResourceOptions): WebAcl;
```

```python
def get(resource_name, id, opts=None, arn=None, default_<wbr>action=None, logging_<wbr>configuration=None, metric_<wbr>name=None, name=None, rules=None, tags=None)
```

```go
func GetWebAcl(ctx *pulumi.Context, name string, id pulumi.IDInput, state *WebAclState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static WebAcl Get(string name, Input<string> id, WebAclState? state = null, CustomResourceOptions? options = null);
```

Get an existing WebAcl resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">List&lt;Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
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
Key-value mapping of resource tags
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
The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">*waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">*waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Metric<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">[]waf.<wbr>Web<wbr>Acl<wbr>Rule</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
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
Key-value mapping of resource tags
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
The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">waf.<wbr>Web<wbr>Acl<wbr>Default<wbr>Action?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">waf.<wbr>Web<wbr>Acl<wbr>Rule[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
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
Key-value mapping of resource tags
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
The ARN of the WAF WebACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>action</td>
            <td class="align-top">
                
                <code><a href="#webacldefaultaction">dict{web_<wbr>acl_<wbr>default_<wbr>action}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block with action that you want AWS WAF to take when a request doesn&#39;t match the criteria in any of the rules that are associated with the web ACL. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logging_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfiguration">dict{web_<wbr>acl_<wbr>logging_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to enable WAF logging. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">metric_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name or description for the Amazon CloudWatch metric of this web ACL.
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
The name or description of the web ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rules</td>
            <td class="align-top">
                
                <code><a href="#webaclrule">list[web_<wbr>acl_<wbr>rule]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration blocks containing rules to associate with the web ACL and the settings for each rule. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### WebAclDefaultAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclDefaultAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclDefaultAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclDefaultActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclDefaultActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclDefaultActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclDefaultAction.html">output</a> API doc for this type.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WebAclLoggingConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclLoggingConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclLoggingConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclLoggingConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclLoggingConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclLoggingConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclLoggingConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Log<wbr>Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redacted<wbr>Fields</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfields">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Redacted<wbr>Fields<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing parts of the request that you want redacted from the logs. Detailed below.
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
            <td class="align-top">Log<wbr>Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redacted<wbr>Fields</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfields">*waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Redacted<wbr>Fields</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing parts of the request that you want redacted from the logs. Detailed below.
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
            <td class="align-top">log<wbr>Destination</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redacted<wbr>Fields</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfields">waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Redacted<wbr>Fields?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing parts of the request that you want redacted from the logs. Detailed below.
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
            <td class="align-top">log_<wbr>destination</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of Kinesis Firehose Delivery Stream
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redacted_<wbr>fields</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfields">dict{web_<wbr>acl_<wbr>logging_<wbr>configuration_<wbr>redacted_<wbr>fields}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing parts of the request that you want redacted from the logs. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WebAclLoggingConfigurationRedactedFields
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclLoggingConfigurationRedactedFields">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclLoggingConfigurationRedactedFields">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclLoggingConfigurationRedactedFieldsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclLoggingConfigurationRedactedFieldsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclLoggingConfigurationRedactedFieldsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclLoggingConfigurationRedactedFields.html">output</a> API doc for this type.
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
            <td class="align-top">Field<wbr>To<wbr>Matches</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfieldsfieldtomatch">List&lt;Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Redacted<wbr>Fields<wbr>Field<wbr>To<wbr>Match<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of configuration blocks for fields to redact. Detailed below.
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
            <td class="align-top">Field<wbr>To<wbr>Matches</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfieldsfieldtomatch">[]waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Redacted<wbr>Fields<wbr>Field<wbr>To<wbr>Match</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of configuration blocks for fields to redact. Detailed below.
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
            <td class="align-top">field<wbr>To<wbr>Matches</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfieldsfieldtomatch">waf.<wbr>Web<wbr>Acl<wbr>Logging<wbr>Configuration<wbr>Redacted<wbr>Fields<wbr>Field<wbr>To<wbr>Match[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of configuration blocks for fields to redact. Detailed below.
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
            <td class="align-top">field_<wbr>to_<wbr>matches</td>
            <td class="align-top">
                
                <code><a href="#webaclloggingconfigurationredactedfieldsfieldtomatch">list[web_<wbr>acl_<wbr>logging_<wbr>configuration_<wbr>redacted_<wbr>fields_<wbr>field_<wbr>to_<wbr>match]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Set of configuration blocks for fields to redact. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WebAclLoggingConfigurationRedactedFieldsFieldToMatch
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclLoggingConfigurationRedactedFieldsFieldToMatch">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclLoggingConfigurationRedactedFieldsFieldToMatch">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclLoggingConfigurationRedactedFieldsFieldToMatchOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclLoggingConfigurationRedactedFieldsFieldToMatchArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclLoggingConfigurationRedactedFieldsFieldToMatch.html">output</a> API doc for this type.
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
            <td class="align-top">Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
            <td class="align-top">Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
            <td class="align-top">data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
            <td class="align-top">data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When the value of `type` is `HEADER`, enter the name of the header that you want the WAF to search, for example, `User-Agent` or `Referer`. If the value of `type` is any other value, omit `data`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WebAclRule
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclRule">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclRuleOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclRuleArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclRule.html">output</a> API doc for this type.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleaction">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Action<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleoverrideaction">Pulumi.<wbr>Aws.<wbr>Waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Override<wbr>Action<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the associated WAF (Global) rule (e.g. [`aws.waf.Rule`](https://www.terraform.io/docs/providers/aws/r/waf_rule.html)). WAF (Regional) rules cannot be used.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
            <td class="align-top">Action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleaction">*waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Override<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleoverrideaction">*waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Override<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the associated WAF (Global) rule (e.g. [`aws.waf.Rule`](https://www.terraform.io/docs/providers/aws/r/waf_rule.html)). WAF (Regional) rules cannot be used.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleaction">waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Action?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override<wbr>Action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleoverrideaction">waf.<wbr>Web<wbr>Acl<wbr>Rule<wbr>Override<wbr>Action?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the associated WAF (Global) rule (e.g. [`aws.waf.Rule`](https://www.terraform.io/docs/providers/aws/r/waf_rule.html)). WAF (Regional) rules cannot be used.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
            <td class="align-top">action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleaction">dict{web_<wbr>acl_<wbr>rule_<wbr>action}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The action that CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Not used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">override_<wbr>action</td>
            <td class="align-top">
                
                <code><a href="#webaclruleoverrideaction">dict{web_<wbr>acl_<wbr>rule_<wbr>override_<wbr>action}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Override the action that a group requests CloudFront or AWS WAF takes when a web request matches the conditions in the rule. Only used if `type` is `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Specifies the order in which the rules in a WebACL are evaluated.
Rules with a lower value are evaluated before rules with a higher value.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rule_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
ID of the associated WAF (Global) rule (e.g. [`aws.waf.Rule`](https://www.terraform.io/docs/providers/aws/r/waf_rule.html)). WAF (Regional) rules cannot be used.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WebAclRuleAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclRuleAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclRuleAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclRuleActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclRuleActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclRuleActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclRuleAction.html">output</a> API doc for this type.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### WebAclRuleOverrideAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WebAclRuleOverrideAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WebAclRuleOverrideAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclRuleOverrideActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/waf?tab=doc#WebAclRuleOverrideActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclRuleOverrideActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Waf.WebAclRuleOverrideAction.html">output</a> API doc for this type.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
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
The rule type, either `REGULAR`, as defined by [Rule](http://docs.aws.amazon.com/waf/latest/APIReference/API_Rule.html), `RATE_BASED`, as defined by [RateBasedRule](http://docs.aws.amazon.com/waf/latest/APIReference/API_RateBasedRule.html), or `GROUP`, as defined by [RuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_RuleGroup.html). The default is REGULAR. If you add a RATE_BASED rule, you need to set `type` as `RATE_BASED`. If you add a GROUP rule, you need to set `type` as `GROUP`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







