
---
title: "UsagePlan"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an API Gateway Usage Plan.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const myapi = new aws.apigateway.RestApi("myapi", {});
const dev = new aws.apigateway.Deployment("dev", {
    restApi: myapi.id,
    stageName: "dev",
});
const prod = new aws.apigateway.Deployment("prod", {
    restApi: myapi.id,
    stageName: "prod",
});
const myUsagePlan = new aws.apigateway.UsagePlan("MyUsagePlan", {
    apiStages: [
        {
            apiId: myapi.id,
            stage: dev.stageName,
        },
        {
            apiId: myapi.id,
            stage: prod.stageName,
        },
    ],
    description: "my description",
    productCode: "MYCODE",
    quotaSettings: {
        limit: 20,
        offset: 2,
        period: "WEEK",
    },
    throttleSettings: {
        burstLimit: 5,
        rateLimit: 10,
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_usage_plan.html.markdown.



## Create a UsagePlan Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlan">UsagePlan</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlanArgs">UsagePlanArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">UsagePlan</span><span class="p">(resource_name, opts=None, </span>api_stages=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>product_code=None<span class="p">, </span>quota_settings=None<span class="p">, </span>tags=None<span class="p">, </span>throttle_settings=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewUsagePlan<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanArgs">UsagePlanArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlan">UsagePlan</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlan.html">UsagePlan</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanArgs.html">UsagePlanArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a UsagePlan resource with the given unique name, arguments, and options.

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
            <td class="align-top">Api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">List&lt;Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">Throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
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
            <td class="align-top">Api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">[]apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">*apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">Throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">*apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
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
            <td class="align-top">api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
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
            <td class="align-top">api_<wbr>stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">List[usage_<wbr>plan_<wbr>api_<wbr>stage]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quota_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">Dict[usage_<wbr>plan_<wbr>quota_<wbr>settings]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throttle_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">Dict[usage_<wbr>plan_<wbr>throttle_<wbr>settings]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## UsagePlan Output Properties

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
            <td class="align-top">Api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">List&lt;Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} The associated API stages of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">Throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} The throttling limits of the usage plan.
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
            <td class="align-top">Api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">[]apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage</a></code>
            </td>
            <td class="align-top">{{% md %}} The associated API stages of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The description of a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">*apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings</a></code>
            </td>
            <td class="align-top">{{% md %}} The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">Throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">*apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings</a></code>
            </td>
            <td class="align-top">{{% md %}} The throttling limits of the usage plan.
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
            <td class="align-top">api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} The associated API stages of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The description of a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} The throttling limits of the usage plan.
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
            <td class="align-top">api_<wbr>stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">List[usage_<wbr>plan_<wbr>api_<wbr>stage]</a></code>
            </td>
            <td class="align-top">{{% md %}} The associated API stages of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The description of a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quota_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">Dict[usage_<wbr>plan_<wbr>quota_<wbr>settings]</a></code>
            </td>
            <td class="align-top">{{% md %}} The quota settings of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throttle_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">Dict[usage_<wbr>plan_<wbr>throttle_<wbr>settings]</a></code>
            </td>
            <td class="align-top">{{% md %}} The throttling limits of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing UsagePlan Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlanState">UsagePlanState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlan">UsagePlan</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_stages=None<span class="p">, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>product_code=None<span class="p">, </span>quota_settings=None<span class="p">, </span>tags=None<span class="p">, </span>throttle_settings=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetUsagePlan<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanState">UsagePlanState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlan">UsagePlan</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlan.html">UsagePlan</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanState.html">UsagePlanState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing UsagePlan resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">List&lt;Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
Amazon Resource Name (ARN)
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">Throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
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
            <td class="align-top">Api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">[]apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
Amazon Resource Name (ARN)
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">*apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">Throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">*apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
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
            <td class="align-top">api<wbr>Stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">apigateway.<wbr>Usage<wbr>Plan<wbr>Api<wbr>Stage[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
Amazon Resource Name (ARN)
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quota<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">apigateway.<wbr>Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
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
    
        <tr>
            <td class="align-top">throttle<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">apigateway.<wbr>Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
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
            <td class="align-top">api_<wbr>stages</td>
            <td class="align-top">
                
                <code><a href="#usageplanapistage">List[usage_<wbr>plan_<wbr>api_<wbr>stage]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The associated API stages of the usage plan.
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
Amazon Resource Name (ARN)
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
The description of a usage plan.
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
The name of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">quota_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanquotasettings">Dict[usage_<wbr>plan_<wbr>quota_<wbr>settings]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The quota settings of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throttle_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#usageplanthrottlesettings">Dict[usage_<wbr>plan_<wbr>throttle_<wbr>settings]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throttling limits of the usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### UsagePlanApiStage
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UsagePlanApiStage">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UsagePlanApiStage">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanApiStageArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanApiStageOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanApiStageArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanApiStage.html">output</a> API doc for this type.
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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API Id of the associated API stage in a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stage</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API stage name of the associated API stage in a usage plan.
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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API Id of the associated API stage in a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stage</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API stage name of the associated API stage in a usage plan.
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
            <td class="align-top">api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API Id of the associated API stage in a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stage</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API stage name of the associated API stage in a usage plan.
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
            <td class="align-top">api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API Id of the associated API stage in a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stage</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
API stage name of the associated API stage in a usage plan.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UsagePlanQuotaSettings
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UsagePlanQuotaSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UsagePlanQuotaSettings">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanQuotaSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanQuotaSettingsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanQuotaSettingsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanQuotaSettings.html">output</a> API doc for this type.
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
            <td class="align-top">Limit</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of requests that can be made in a given time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Offset</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of requests subtracted from the given limit in the initial time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Period</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time period in which the limit applies. Valid values are &#34;DAY&#34;, &#34;WEEK&#34; or &#34;MONTH&#34;.
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
            <td class="align-top">Limit</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of requests that can be made in a given time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Offset</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of requests subtracted from the given limit in the initial time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Period</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time period in which the limit applies. Valid values are &#34;DAY&#34;, &#34;WEEK&#34; or &#34;MONTH&#34;.
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
            <td class="align-top">limit</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of requests that can be made in a given time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">offset</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of requests subtracted from the given limit in the initial time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">period</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time period in which the limit applies. Valid values are &#34;DAY&#34;, &#34;WEEK&#34; or &#34;MONTH&#34;.
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
            <td class="align-top">limit</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The maximum number of requests that can be made in a given time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">offset</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of requests subtracted from the given limit in the initial time period.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">period</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time period in which the limit applies. Valid values are &#34;DAY&#34;, &#34;WEEK&#34; or &#34;MONTH&#34;.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### UsagePlanThrottleSettings
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UsagePlanThrottleSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UsagePlanThrottleSettings">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanThrottleSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanThrottleSettingsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanThrottleSettingsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanThrottleSettings.html">output</a> API doc for this type.
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
            <td class="align-top">Burst<wbr>Limit</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rate<wbr>Limit</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request steady-state rate limit.
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
            <td class="align-top">Burst<wbr>Limit</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rate<wbr>Limit</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request steady-state rate limit.
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
            <td class="align-top">burst<wbr>Limit</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rate<wbr>Limit</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request steady-state rate limit.
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
            <td class="align-top">burst_<wbr>limit</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rate_<wbr>limit</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API request steady-state rate limit.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







