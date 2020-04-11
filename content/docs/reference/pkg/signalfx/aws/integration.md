
---
title: "Integration"
block_external_search_index: true
---



SignalFx AWS CloudWatch integrations. For help with this integration see [Monitoring Amazon Web Services](https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#monitor-amazon-web-services).

> **NOTE** When managing integrations you'll need to use an admin token to authenticate the SignalFx provider.

> **WARNING** This resource implements a part of a workflow. You must use it with one of either `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.

## Service Names

Fields that expect an AWS service/namespace will work with one of: "AWS/ApiGateway" "AWS/AppStream" "AWS/AutoScaling" "AWS/Billing" "AWS/CloudFront" "AWS/CloudSearch" "AWS/Events" "AWS/Logs" "AWS/Connect" "AWS/DMS" "AWS/DX" "AWS/DynamoDB" "AWS/EC2" "AWS/EC2Spot" "AWS/ECS" "AWS/ElasticBeanstalk" "AWS/EBS" "AWS/EFS" "AWS/ELB" "AWS/ApplicationELB" "AWS/NetworkELB" "AWS/ElasticTranscoder" "AWS/ElastiCache" "AWS/ES" "AWS/ElasticMapReduce" "AWS/GameLift" "AWS/Inspector" "AWS/IoT" "AWS/KMS" "AWS/KinesisAnalytics" "AWS/Firehose" "AWS/Kinesis" "AWS/KinesisVideo" "AWS/Lambda" "AWS/Lex" "AWS/ML" "AWS/OpsWorks" "AWS/Polly" "AWS/Redshift" "AWS/RDS" "AWS/Route53" "AWS/SageMaker" "AWS/DDoSProtection" "AWS/SES" "AWS/SNS" "AWS/SQS" "AWS/S3" "AWS/SWF" "AWS/States" "AWS/StorageGateway" "AWS/Translate" "AWS/NATGateway" "AWS/VPN" "WAF" "AWS/WorkSpaces".

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_integration.html.markdown.



## Create a Integration Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/aws/#Integration">Integration</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/aws/#IntegrationArgs">IntegrationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Integration</span><span class="p">(resource_name, opts=None, </span>custom_cloudwatch_namespaces=None<span class="p">, </span>custom_namespace_sync_rules=None<span class="p">, </span>enable_aws_usage=None<span class="p">, </span>enabled=None<span class="p">, </span>external_id=None<span class="p">, </span>import_cloud_watch=None<span class="p">, </span>integration_id=None<span class="p">, </span>key=None<span class="p">, </span>namespace_sync_rules=None<span class="p">, </span>poll_rate=None<span class="p">, </span>regions=None<span class="p">, </span>role_arn=None<span class="p">, </span>services=None<span class="p">, </span>token=None<span class="p">, </span>use_get_metric_data_method=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewIntegration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#IntegrationArgs">IntegrationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#Integration">Integration</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.Aws.Integration.html">Integration</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.Aws.IntegrationArgs.html">IntegrationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">List&lt;Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">List&lt;Integration<wbr>Namespace<wbr>Sync<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">[]Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">[]Integration<wbr>Namespace<wbr>Sync<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">Integration<wbr>Namespace<wbr>Sync<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>cloudwatch_<wbr>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>namespace_<wbr>sync_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">List[Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>aws_<wbr>usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import_<wbr>cloud_<wbr>watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>integration_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace_<wbr>sync_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">List[Integration<wbr>Namespace<wbr>Sync<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poll_<wbr>rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>get_<wbr>metric_<wbr>data_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Integration Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">List&lt;Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">List&lt;Integration<wbr>Namespace<wbr>Sync<wbr>Rule&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">[]Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>External<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">[]Integration<wbr>Namespace<wbr>Sync<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">Integration<wbr>Namespace<wbr>Sync<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>custom_<wbr>cloudwatch_<wbr>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>namespace_<wbr>sync_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">List[Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>aws_<wbr>usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>external_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>import_<wbr>cloud_<wbr>watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>integration_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace_<wbr>sync_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">List[Integration<wbr>Namespace<wbr>Sync<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>poll_<wbr>rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>use_<wbr>get_<wbr>metric_<wbr>data_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Integration Resource

Get an existing Integration resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/aws/#IntegrationState">IntegrationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/aws/#Integration">Integration</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>custom_cloudwatch_namespaces=None<span class="p">, </span>custom_namespace_sync_rules=None<span class="p">, </span>enable_aws_usage=None<span class="p">, </span>enabled=None<span class="p">, </span>external_id=None<span class="p">, </span>import_cloud_watch=None<span class="p">, </span>integration_id=None<span class="p">, </span>key=None<span class="p">, </span>namespace_sync_rules=None<span class="p">, </span>poll_rate=None<span class="p">, </span>regions=None<span class="p">, </span>role_arn=None<span class="p">, </span>services=None<span class="p">, </span>token=None<span class="p">, </span>use_get_metric_data_method=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetIntegration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#IntegrationState">IntegrationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#Integration">Integration</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.Aws.Integration.html">Integration</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.Aws.IntegrationState.html">IntegrationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">List&lt;Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">List&lt;Integration<wbr>Namespace<wbr>Sync<wbr>Rule<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">[]Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">[]Integration<wbr>Namespace<wbr>Sync<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Services</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Cloudwatch<wbr>Namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Aws<wbr>Usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import<wbr>Cloud<wbr>Watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>integration<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace<wbr>Sync<wbr>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">Integration<wbr>Namespace<wbr>Sync<wbr>Rule[]?</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poll<wbr>Rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Get<wbr>Metric<wbr>Data<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>cloudwatch_<wbr>namespaces</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>namespace_<wbr>sync_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationcustomnamespacesyncrule">List[Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the `custom_cloudwatch_namespaces` property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>aws_<wbr>usage</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If `true`, SignalFx imports the metrics.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the integration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The `external_id` property from one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>import_<wbr>cloud_<wbr>watch</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>integration_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of one of a `signalfx.aws.ExternalIntegration` or `signalfx.aws.TokenIntegration`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If you specify `auth_method = \"SecurityToken\"` in your request to create an AWS integration object, use this property to specify the key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace_<wbr>sync_<wbr>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#integrationnamespacesyncrule">List[Integration<wbr>Namespace<wbr>Sync<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the `services` property. If you don't specify either property, SignalFx syncs all data in all AWS namespaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>poll_<wbr>rate</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}AWS poll rate (in seconds). One of `60` or `300`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of AWS regions that SignalFx should monitor.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Role ARN that you add to an existing AWS integration object. **Note**: Ensure you use the `arn` property of your role, not the id!
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>services</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with `namespace_sync_rule`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>token</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Used with `signalfx_aws_token_integration`. Use this property to specify the token.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use_<wbr>get_<wbr>metric_<wbr>data_<wbr>method</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the use of Amazon's `GetMetricData` for collecting metrics. Note that this requires the inclusion of the `"cloudwatch:GetMetricData"` permission.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Integration<wbr>Custom<wbr>Namespace<wbr>Sync<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#IntegrationCustomNamespaceSyncRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#IntegrationCustomNamespaceSyncRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#IntegrationCustomNamespaceSyncRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#IntegrationCustomNamespaceSyncRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Integration<wbr>Namespace<wbr>Sync<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#IntegrationNamespaceSyncRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#IntegrationNamespaceSyncRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#IntegrationNamespaceSyncRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/aws?tab=doc#IntegrationNamespaceSyncRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn't match the filter. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of `"Include"` or `"Exclude"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow `filter()` function; it can be any valid SignalFlow filter expression.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-signalfx">https://github.com/pulumi/pulumi-signalfx</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

