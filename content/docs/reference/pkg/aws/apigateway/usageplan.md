
---
title: "UsagePlan"
block_external_search_index: true
---

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

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlan">UsagePlan</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlanArgs">UsagePlanArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">UsagePlan</span><span class="p">(resource_name, opts=None, </span>api_stages=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>product_code=None<span class="p">, </span>quota_settings=None<span class="p">, </span>tags=None<span class="p">, </span>throttle_settings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewUsagePlan<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanArgs">UsagePlanArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlan">UsagePlan</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlan.html">UsagePlan</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.ApiGateway.UsagePlanArgs.html">UsagePlanArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">List&lt;Usage<wbr>Plan<wbr>Api<wbr>Stage<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Usage<wbr>Plan<wbr>Quota<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Usage<wbr>Plan<wbr>Throttle<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">[]Usage<wbr>Plan<wbr>Api<wbr>Stage</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">*Usage<wbr>Plan<wbr>Quota<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">*Usage<wbr>Plan<wbr>Throttle<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">Usage<wbr>Plan<wbr>Api<wbr>Stage[]?</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">List[Usage<wbr>Plan<wbr>Api<wbr>Stage]</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quota_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Dict[Usage<wbr>Plan<wbr>Quota<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throttle_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Dict[Usage<wbr>Plan<wbr>Throttle<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## UsagePlan Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">List&lt;Usage<wbr>Plan<wbr>Api<wbr>Stage&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">[]Usage<wbr>Plan<wbr>Api<wbr>Stage</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">*Usage<wbr>Plan<wbr>Quota<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">*Usage<wbr>Plan<wbr>Throttle<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">Usage<wbr>Plan<wbr>Api<wbr>Stage[]?</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api_<wbr>stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">List[Usage<wbr>Plan<wbr>Api<wbr>Stage]</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>product_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>quota_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Dict[Usage<wbr>Plan<wbr>Quota<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>throttle_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Dict[Usage<wbr>Plan<wbr>Throttle<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing UsagePlan Resource

Get an existing UsagePlan resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlanState">UsagePlanState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#UsagePlan">UsagePlan</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_stages=None<span class="p">, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>product_code=None<span class="p">, </span>quota_settings=None<span class="p">, </span>tags=None<span class="p">, </span>throttle_settings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetUsagePlan<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanState">UsagePlanState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlan">UsagePlan</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlan.html">UsagePlan</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.UsagePlanState.html">UsagePlanState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">List&lt;Usage<wbr>Plan<wbr>Api<wbr>Stage<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Usage<wbr>Plan<wbr>Quota<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Usage<wbr>Plan<wbr>Throttle<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">[]Usage<wbr>Plan<wbr>Api<wbr>Stage</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">*Usage<wbr>Plan<wbr>Quota<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">*Usage<wbr>Plan<wbr>Throttle<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">Usage<wbr>Plan<wbr>Api<wbr>Stage[]?</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quota<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Usage<wbr>Plan<wbr>Quota<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throttle<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Usage<wbr>Plan<wbr>Throttle<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>stages</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanapistage">List[Usage<wbr>Plan<wbr>Api<wbr>Stage]</a></span>
    </dt>
    <dd>{{% md %}}The associated API stages of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name (ARN)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description of a usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The AWS Markeplace product identifier to associate with the usage plan as a SaaS product on AWS Marketplace.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quota_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanquotasettings">Dict[Usage<wbr>Plan<wbr>Quota<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The quota settings of the usage plan.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Key-value mapping of resource tags
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throttle_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#usageplanthrottlesettings">Dict[Usage<wbr>Plan<wbr>Throttle<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The throttling limits of the usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Usage<wbr>Plan<wbr>Api<wbr>Stage</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UsagePlanApiStage">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UsagePlanApiStage">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanApiStageArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanApiStageOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}API Id of the associated API stage in a usage plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Stage</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}API stage name of the associated API stage in a usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}API Id of the associated API stage in a usage plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Stage</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}API stage name of the associated API stage in a usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}API Id of the associated API stage in a usage plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>stage</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}API stage name of the associated API stage in a usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>api_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}API Id of the associated API stage in a usage plan.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>stage</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}API stage name of the associated API stage in a usage plan.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Usage<wbr>Plan<wbr>Quota<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UsagePlanQuotaSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UsagePlanQuotaSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanQuotaSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanQuotaSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of requests that can be made in a given time period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of requests subtracted from the given limit in the initial time period.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The maximum number of requests that can be made in a given time period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Offset</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of requests subtracted from the given limit in the initial time period.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum number of requests that can be made in a given time period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>offset</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of requests subtracted from the given limit in the initial time period.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum number of requests that can be made in a given time period.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>offset</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of requests subtracted from the given limit in the initial time period.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time period in which the limit applies. Valid values are "DAY", "WEEK" or "MONTH".
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Usage<wbr>Plan<wbr>Throttle<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#UsagePlanThrottleSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#UsagePlanThrottleSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanThrottleSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#UsagePlanThrottleSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Burst<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rate<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The API request steady-state rate limit.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Burst<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rate<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The API request steady-state rate limit.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>burst<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rate<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The API request steady-state rate limit.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>burst<wbr>Limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The API request burst limit, the maximum rate limit over a time ranging from one to a few seconds, depending upon whether the underlying token bucket is at its full capacity.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rate_<wbr>limit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The API request steady-state rate limit.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
