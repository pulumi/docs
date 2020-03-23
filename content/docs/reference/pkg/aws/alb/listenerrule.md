
---
title: "ListenerRule"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Load Balancer Listener Rule resource.

> **Note:** `aws.alb.ListenerRule` is known as `aws.lb.ListenerRule`. The functionality is identical.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const frontEndLoadBalancer = new aws.lb.LoadBalancer("front_end", {});
const frontEndListener = new aws.lb.Listener("front_end", {});
const static = new aws.lb.ListenerRule("static", {
    actions: [{
        targetGroupArn: aws_lb_target_group_static.arn,
        type: "forward",
    }],
    conditions: [
        {
            pathPattern: {
                values: ["/static/*"],
            },
        },
        {
            hostHeader: {
                values: ["example.com"],
            },
        },
    ],
    listenerArn: frontEndListener.arn,
    priority: 100,
});
const hostBasedRouting = new aws.lb.ListenerRule("host_based_routing", {
    actions: [{
        targetGroupArn: aws_lb_target_group_static.arn,
        type: "forward",
    }],
    conditions: [{
        hostHeader: {
            values: ["my-service.*.mydomain.io"],
        },
    }],
    listenerArn: frontEndListener.arn,
    priority: 99,
});
const redirectHttpToHttps = new aws.lb.ListenerRule("redirect_http_to_https", {
    actions: [{
        redirect: {
            port: "443",
            protocol: "HTTPS",
            statusCode: "HTTP_301",
        },
        type: "redirect",
    }],
    conditions: [{
        httpHeader: {
            httpHeaderName: "X-Forwarded-For",
            values: ["192.168.1.*"],
        },
    }],
    listenerArn: frontEndListener.arn,
});
const healthCheck = new aws.lb.ListenerRule("health_check", {
    actions: [{
        fixedResponse: {
            contentType: "text/plain",
            messageBody: "HEALTHY",
            statusCode: "200",
        },
        type: "fixed-response",
    }],
    conditions: [{
        queryStrings: [
            {
                key: "health",
                value: "check",
            },
            {
                value: "bar",
            },
        ],
    }],
    listenerArn: frontEndListener.arn,
});
const pool = new aws.cognito.UserPool("pool", {});
const client = new aws.cognito.UserPoolClient("client", {});
const domain = new aws.cognito.UserPoolDomain("domain", {});
const admin = new aws.lb.ListenerRule("admin", {
    actions: [
        {
            authenticateOidc: {
                authorizationEndpoint: "https://example.com/authorization_endpoint",
                clientId: "client_id",
                clientSecret: "client_secret",
                issuer: "https://example.com",
                tokenEndpoint: "https://example.com/token_endpoint",
                userInfoEndpoint: "https://example.com/user_info_endpoint",
            },
            type: "authenticate-oidc",
        },
        {
            targetGroupArn: aws_lb_target_group_static.arn,
            type: "forward",
        },
    ],
    listenerArn: frontEndListener.arn,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lb_listener_rule.html.markdown.



## Create a ListenerRule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#ListenerRule">ListenerRule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#ListenerRuleArgs">ListenerRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ListenerRule</span><span class="p">(resource_name, opts=None, </span>actions=None<span class="p">, </span>conditions=None<span class="p">, </span>listener_arn=None<span class="p">, </span>priority=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewListenerRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleArgs">ListenerRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRule">ListenerRule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRule.html">ListenerRule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleArgs.html">ListenerRuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a ListenerRule resource with the given unique name, arguments, and options.

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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">List&lt;Listener<wbr>Rule<wbr>Action<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">List&lt;Listener<wbr>Rule<wbr>Condition<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">[]Listener<wbr>Rule<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">[]Listener<wbr>Rule<wbr>Condition</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">Listener<wbr>Rule<wbr>Action[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">Listener<wbr>Rule<wbr>Condition[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">List[Listener<wbr>Rule<wbr>Action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">List[Listener<wbr>Rule<wbr>Condition]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## ListenerRule Output Properties

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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">List&lt;Listener<wbr>Rule<wbr>Action&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">List&lt;Listener<wbr>Rule<wbr>Condition&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">[]Listener<wbr>Rule<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">[]Listener<wbr>Rule<wbr>Condition</a></code>
            </td>
            <td class="align-top">{{% md %}} A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">Listener<wbr>Rule<wbr>Action[]</a></code>
            </td>
            <td class="align-top">{{% md %}} An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">Listener<wbr>Rule<wbr>Condition[]</a></code>
            </td>
            <td class="align-top">{{% md %}} A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">List[Listener<wbr>Rule<wbr>Action]</a></code>
            </td>
            <td class="align-top">{{% md %}} An Action block. Action blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">List[Listener<wbr>Rule<wbr>Condition]</a></code>
            </td>
            <td class="align-top">{{% md %}} A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing ListenerRule Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#ListenerRuleState">ListenerRuleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/alb/#ListenerRule">ListenerRule</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>actions=None<span class="p">, </span>arn=None<span class="p">, </span>conditions=None<span class="p">, </span>listener_arn=None<span class="p">, </span>priority=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetListenerRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleState">ListenerRuleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRule">ListenerRule</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRule.html">ListenerRule</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleState.html">ListenerRuleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing ListenerRule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">List&lt;Listener<wbr>Rule<wbr>Action<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Action block. Action blocks are documented below.
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
The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">List&lt;Listener<wbr>Rule<wbr>Condition<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">Actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">[]Listener<wbr>Rule<wbr>Action</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Action block. Action blocks are documented below.
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
The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">[]Listener<wbr>Rule<wbr>Condition</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Priority</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">Listener<wbr>Rule<wbr>Action[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Action block. Action blocks are documented below.
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
The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">Listener<wbr>Rule<wbr>Condition[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
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
            <td class="align-top">actions</td>
            <td class="align-top">
                
                <code><a href="#listenerruleaction">List[Listener<wbr>Rule<wbr>Action]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
An Action block. Action blocks are documented below.
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
The ARN of the rule (matches `id`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">conditions</td>
            <td class="align-top">
                
                <code><a href="#listenerrulecondition">List[Listener<wbr>Rule<wbr>Condition]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">listener_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the listener to which to attach the rule.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">priority</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can&#39;t have multiple rules with the same priority.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ListenerRuleAction
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleAction">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleAction">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleAction.html">output</a> API doc for this type.
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
            <td class="align-top">Authenticate<wbr>Cognito</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticatecognito">Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Cognito<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using Cognito. Required if `type` is `authenticate-cognito`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authenticate<wbr>Oidc</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticateoidc">Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Oidc<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using OIDC. Required if `type` is `authenticate-oidc`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fixed<wbr>Response</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionfixedresponse">Listener<wbr>Rule<wbr>Action<wbr>Fixed<wbr>Response<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Order</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redirect</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionredirect">Listener<wbr>Rule<wbr>Action<wbr>Redirect<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating a redirect action. Required if `type` is `redirect`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Target Group to which to route traffic. Required if `type` is `forward`.
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
The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
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
            <td class="align-top">Authenticate<wbr>Cognito</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticatecognito">*Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Cognito</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using Cognito. Required if `type` is `authenticate-cognito`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authenticate<wbr>Oidc</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticateoidc">*Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Oidc</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using OIDC. Required if `type` is `authenticate-oidc`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fixed<wbr>Response</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionfixedresponse">*Listener<wbr>Rule<wbr>Action<wbr>Fixed<wbr>Response</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Order</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Redirect</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionredirect">*Listener<wbr>Rule<wbr>Action<wbr>Redirect</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating a redirect action. Required if `type` is `redirect`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Target<wbr>Group<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Target Group to which to route traffic. Required if `type` is `forward`.
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
The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
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
            <td class="align-top">authenticate<wbr>Cognito</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticatecognito">Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Cognito?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using Cognito. Required if `type` is `authenticate-cognito`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authenticate<wbr>Oidc</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticateoidc">Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Oidc?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using OIDC. Required if `type` is `authenticate-oidc`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fixed<wbr>Response</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionfixedresponse">Listener<wbr>Rule<wbr>Action<wbr>Fixed<wbr>Response?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">order</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redirect</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionredirect">Listener<wbr>Rule<wbr>Action<wbr>Redirect?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating a redirect action. Required if `type` is `redirect`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target<wbr>Group<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Target Group to which to route traffic. Required if `type` is `forward`.
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
The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
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
            <td class="align-top">authenticate<wbr>Cognito</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticatecognito">Dict[Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Cognito]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using Cognito. Required if `type` is `authenticate-cognito`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authenticate<wbr>Oidc</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionauthenticateoidc">Dict[Listener<wbr>Rule<wbr>Action<wbr>Authenticate<wbr>Oidc]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an authenticate action using OIDC. Required if `type` is `authenticate-oidc`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fixed<wbr>Response</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionfixedresponse">Dict[Listener<wbr>Rule<wbr>Action<wbr>Fixed<wbr>Response]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating an action that returns a custom HTTP response. Required if `type` is `fixed-response`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">order</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">redirect</td>
            <td class="align-top">
                
                <code><a href="#listenerruleactionredirect">Dict[Listener<wbr>Rule<wbr>Action<wbr>Redirect]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information for creating a redirect action. Required if `type` is `redirect`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">target_<wbr>group_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Target Group to which to route traffic. Required if `type` is `forward`.
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
The type of routing action. Valid values are `forward`, `redirect`, `fixed-response`, `authenticate-cognito` and `authenticate-oidc`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleActionAuthenticateCognito
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleActionAuthenticateCognito">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleActionAuthenticateCognito">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionAuthenticateCognitoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionAuthenticateCognitoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionAuthenticateCognitoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionAuthenticateCognito.html">output</a> API doc for this type.
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
            <td class="align-top">Authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Cognito user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Cognito user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain prefix or fully-qualified domain name of the Cognito user pool.
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
            <td class="align-top">Authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Cognito user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Cognito user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Pool<wbr>Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain prefix or fully-qualified domain name of the Cognito user pool.
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
            <td class="align-top">authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Cognito user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Cognito user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Domain</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain prefix or fully-qualified domain name of the Cognito user pool.
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
            <td class="align-top">authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the Cognito user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Client<wbr>Id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the Cognito user pool client.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Pool<wbr>Domain</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The domain prefix or fully-qualified domain name of the Cognito user pool.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleActionAuthenticateOidc
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleActionAuthenticateOidc">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleActionAuthenticateOidc">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionAuthenticateOidcArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionAuthenticateOidcOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionAuthenticateOidcArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionAuthenticateOidc.html">output</a> API doc for this type.
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
            <td class="align-top">Authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>Dictionary<string, object>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorization<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authorization endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OIDC issuer identifier of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Token<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The token endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Info<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user info endpoint of the IdP.
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
            <td class="align-top">Authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Authorization<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authorization endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OIDC issuer identifier of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">On<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Scope</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Token<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The token endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Info<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user info endpoint of the IdP.
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
            <td class="align-top">authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorization<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authorization endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Secret</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">issuer</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OIDC issuer identifier of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">token<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The token endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Info<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user info endpoint of the IdP.
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
            <td class="align-top">authentication<wbr>Request<wbr>Extra<wbr>Params</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters to include in the redirect request to the authorization endpoint. Max: 10.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">authorization<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The authorization endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client identifier.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>secret</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OAuth 2.0 client secret.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">issuer</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The OIDC issuer identifier of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">on<wbr>Unauthenticated<wbr>Request</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The behavior if the user is not authenticated. Valid values: `deny`, `allow` and `authenticate`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">scope</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The set of user claims to be requested from the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Cookie<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the cookie used to maintain session information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">session<wbr>Timeout</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum duration of the authentication session, in seconds.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">token<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The token endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Info<wbr>Endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The user info endpoint of the IdP.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleActionFixedResponse
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleActionFixedResponse">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleActionFixedResponse">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionFixedResponseArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionFixedResponseOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionFixedResponseArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionFixedResponse.html">output</a> API doc for this type.
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
            <td class="align-top">Content<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Message<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message body.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
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
            <td class="align-top">Content<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Message<wbr>Body</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message body.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
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
            <td class="align-top">content<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">message<wbr>Body</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message body.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
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
            <td class="align-top">content_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The content type. Valid values are `text/plain`, `text/css`, `text/html`, `application/javascript` and `application/json`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">message<wbr>Body</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The message body.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleActionRedirect
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleActionRedirect">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleActionRedirect">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionRedirectArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleActionRedirectOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionRedirectArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleActionRedirect.html">output</a> API doc for this type.
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
            <td class="align-top">Host</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The absolute path, starting with the leading &#34;/&#34;. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading &#34;?&#34;. Defaults to `#{query}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
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
            <td class="align-top">Host</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The absolute path, starting with the leading &#34;/&#34;. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Port</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Protocol</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading &#34;?&#34;. Defaults to `#{query}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
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
            <td class="align-top">host</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The absolute path, starting with the leading &#34;/&#34;. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading &#34;?&#34;. Defaults to `#{query}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
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
            <td class="align-top">host</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The hostname. This component is not percent-encoded. The hostname can contain `#{host}`. Defaults to `#{host}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The absolute path, starting with the leading &#34;/&#34;. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}. Defaults to `/#{path}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">port</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The port. Specify a value from `1` to `65535` or `#{port}`. Defaults to `#{port}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">protocol</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The protocol. Valid values are `HTTP`, `HTTPS`, or `#{protocol}`. Defaults to `#{protocol}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading &#34;?&#34;. Defaults to `#{query}`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP response code. Valid values are `2XX`, `4XX`, or `5XX`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleCondition
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleCondition">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleCondition.html">output</a> API doc for this type.
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
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of condition. Valid values are `host-header` or `path-pattern`. Must also set `values`.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhostheader">Listener<wbr>Rule<wbr>Condition<wbr>Host<wbr>Header<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttpheader">Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Header<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP headers to match. HTTP Header block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Request<wbr>Method</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttprequestmethod">Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Request<wbr>Method<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (\_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path<wbr>Pattern</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionpathpattern">Listener<wbr>Rule<wbr>Condition<wbr>Path<wbr>Pattern<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a `query-string` condition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>Strings</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionquerystring">List&lt;Listener<wbr>Rule<wbr>Condition<wbr>Query<wbr>String<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query strings to match. Query String block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ip</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionsourceip">Listener<wbr>Rule<wbr>Condition<wbr>Source<wbr>Ip<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the `X-Forwarded-For` header, use `http-header` condition instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
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
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of condition. Valid values are `host-header` or `path-pattern`. Must also set `values`.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhostheader">*Listener<wbr>Rule<wbr>Condition<wbr>Host<wbr>Header</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttpheader">*Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Header</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP headers to match. HTTP Header block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Request<wbr>Method</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttprequestmethod">*Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Request<wbr>Method</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (\_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path<wbr>Pattern</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionpathpattern">*Listener<wbr>Rule<wbr>Condition<wbr>Path<wbr>Pattern</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a `query-string` condition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Query<wbr>Strings</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionquerystring">[]Listener<wbr>Rule<wbr>Condition<wbr>Query<wbr>String</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query strings to match. Query String block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Source<wbr>Ip</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionsourceip">*Listener<wbr>Rule<wbr>Condition<wbr>Source<wbr>Ip</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the `X-Forwarded-For` header, use `http-header` condition instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
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
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of condition. Valid values are `host-header` or `path-pattern`. Must also set `values`.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhostheader">Listener<wbr>Rule<wbr>Condition<wbr>Host<wbr>Header?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttpheader">Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Header?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP headers to match. HTTP Header block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Request<wbr>Method</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttprequestmethod">Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Request<wbr>Method?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (\_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path<wbr>Pattern</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionpathpattern">Listener<wbr>Rule<wbr>Condition<wbr>Path<wbr>Pattern?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a `query-string` condition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query<wbr>Strings</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionquerystring">Listener<wbr>Rule<wbr>Condition<wbr>Query<wbr>String[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query strings to match. Query String block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ip</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionsourceip">Listener<wbr>Rule<wbr>Condition<wbr>Source<wbr>Ip?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the `X-Forwarded-For` header, use `http-header` condition instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
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
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of condition. Valid values are `host-header` or `path-pattern`. Must also set `values`.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhostheader">Dict[Listener<wbr>Rule<wbr>Condition<wbr>Host<wbr>Header]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of host header patterns to match. The maximum size of each pattern is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Header</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttpheader">Dict[Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Header]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP headers to match. HTTP Header block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Request<wbr>Method</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionhttprequestmethod">Dict[Listener<wbr>Rule<wbr>Condition<wbr>Http<wbr>Request<wbr>Method]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of HTTP request methods or verbs to match. Maximum size is 40 characters. Only allowed characters are A-Z, hyphen (-) and underscore (\_). Comparison is case sensitive. Wildcards are not supported. Only one needs to match for the condition to be satisfied. AWS recommends that GET and HEAD requests are routed in the same way because the response to a HEAD request may be cached.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path<wbr>Pattern</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionpathpattern">Dict[Listener<wbr>Rule<wbr>Condition<wbr>Path<wbr>Pattern]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of path patterns to match against the request URL. Maximum size of each pattern is 128 characters. Comparison is case sensitive. Wildcard charaters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). Only one pattern needs to match for the condition to be satisfied. Path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use a `query-string` condition.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">query<wbr>Strings</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionquerystring">List[Listener<wbr>Rule<wbr>Condition<wbr>Query<wbr>String]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query strings to match. Query String block fields documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">source<wbr>Ip</td>
            <td class="align-top">
                
                <code><a href="#listenerruleconditionsourceip">Dict[Listener<wbr>Rule<wbr>Condition<wbr>Source<wbr>Ip]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Contains a single `values` item which is a list of source IP CIDR notations to match. You can use both IPv4 and IPv6 addresses. Wildcards are not supported. Condition is satisfied if the source IP address of the request matches one of the CIDR blocks. Condition is not satisfied by the addresses in the `X-Forwarded-For` header, use `http-header` condition instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            use &#39;host_header&#39; or &#39;path_pattern&#39; attribute instead
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleConditionHostHeader
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleConditionHostHeader">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleConditionHostHeader">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionHostHeaderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionHostHeaderOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionHostHeaderArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionHostHeader.html">output</a> API doc for this type.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List<string>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleConditionHttpHeader
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleConditionHttpHeader">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleConditionHttpHeader">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionHttpHeaderArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionHttpHeaderOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionHttpHeaderArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionHttpHeader.html">output</a> API doc for this type.
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
            <td class="align-top">Http<wbr>Header<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a `host-header` condition instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List<string></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">Http<wbr>Header<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a `host-header` condition instead.
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
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">http<wbr>Header<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a `host-header` condition instead.
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
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">http<wbr>Header<wbr>Name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of HTTP header to search. The maximum size is 40 characters. Comparison is case insensitive. Only RFC7240 characters are supported. Wildcards are not supported. You cannot use HTTP header condition to specify the host header, use a `host-header` condition instead.
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
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleConditionHttpRequestMethod
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleConditionHttpRequestMethod">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleConditionHttpRequestMethod">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionHttpRequestMethodArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionHttpRequestMethodOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionHttpRequestMethodArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionHttpRequestMethod.html">output</a> API doc for this type.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List<string></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleConditionPathPattern
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleConditionPathPattern">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleConditionPathPattern">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionPathPatternArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionPathPatternOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionPathPatternArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionPathPattern.html">output</a> API doc for this type.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List<string>?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleConditionQueryString
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleConditionQueryString">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleConditionQueryString">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionQueryStringArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionQueryStringOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionQueryStringArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionQueryString.html">output</a> API doc for this type.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string key pattern to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string value pattern to match.
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
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string key pattern to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string value pattern to match.
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
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Query string key pattern to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string value pattern to match.
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
 (Optional)
Query string key pattern to match.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string value pattern to match.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### ListenerRuleConditionSourceIp
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ListenerRuleConditionSourceIp">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ListenerRuleConditionSourceIp">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionSourceIpArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/alb?tab=doc#ListenerRuleConditionSourceIpOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionSourceIpArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Alb.ListenerRuleConditionSourceIp.html">output</a> API doc for this type.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List<string></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
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
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Query string pairs or values to match. Query String Value blocks documented below. Multiple `values` blocks can be specified, see example above. Maximum size of each string is 128 characters. Comparison is case insensitive. Wildcard characters supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal &#39;\*&#39; or &#39;?&#39; character in a query string, escape the character with a backslash (\\). Only one pair needs to match for the condition to be satisfied.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







