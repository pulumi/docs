
---
title: "UptimeCheckConfig"
block_external_search_index: true
---

This message configures which resources and services to monitor for availability.


To get more information about UptimeCheckConfig, see:

* [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.uptimeCheckConfigs)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/monitoring/uptime-checks/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/monitoring_uptime_check_config.html.markdown.



## Create a UptimeCheckConfig Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#UptimeCheckConfig">UptimeCheckConfig</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#UptimeCheckConfigArgs">UptimeCheckConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">UptimeCheckConfig</span><span class="p">(resource_name, opts=None, </span>content_matchers=None<span class="p">, </span>display_name=None<span class="p">, </span>http_check=None<span class="p">, </span>monitored_resource=None<span class="p">, </span>period=None<span class="p">, </span>project=None<span class="p">, </span>resource_group=None<span class="p">, </span>selected_regions=None<span class="p">, </span>tcp_check=None<span class="p">, </span>timeout=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewUptimeCheckConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigArgs">UptimeCheckConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfig">UptimeCheckConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.UptimeCheckConfig.html">UptimeCheckConfig</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.UptimeCheckConfigArgs.html">UptimeCheckConfigArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">List&lt;Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">[]Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">*Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">*Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">*Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">*Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher[]?</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource?</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group?</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">List[Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher]</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Dict[Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitored_<wbr>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Dict[Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource]</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Dict[Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selected_<wbr>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Dict[Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## UptimeCheckConfig Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">List&lt;Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource?</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group?</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uptime<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">[]Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">*Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">*Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">*Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">*Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Uptime<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher[]?</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource?</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group?</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uptime<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>content_<wbr>matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">List[Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher]</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Dict[Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitored_<wbr>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Dict[Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource]</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Dict[Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>selected_<wbr>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tcp_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Dict[Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>uptime_<wbr>check_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing UptimeCheckConfig Resource

Get an existing UptimeCheckConfig resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#UptimeCheckConfigState">UptimeCheckConfigState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#UptimeCheckConfig">UptimeCheckConfig</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>content_matchers=None<span class="p">, </span>display_name=None<span class="p">, </span>http_check=None<span class="p">, </span>monitored_resource=None<span class="p">, </span>name=None<span class="p">, </span>period=None<span class="p">, </span>project=None<span class="p">, </span>resource_group=None<span class="p">, </span>selected_regions=None<span class="p">, </span>tcp_check=None<span class="p">, </span>timeout=None<span class="p">, </span>uptime_check_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetUptimeCheckConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigState">UptimeCheckConfigState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfig">UptimeCheckConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.UptimeCheckConfig.html">UptimeCheckConfig</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.UptimeCheckConfigState.html">UptimeCheckConfigState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">List&lt;Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uptime<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">[]Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">*Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">*Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">*Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">*Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Uptime<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>content<wbr>Matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher[]?</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitored<wbr>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource?</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group?</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selected<wbr>Regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp<wbr>Check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check?</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uptime<wbr>Check<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>content_<wbr>matchers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigcontentmatcher">List[Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher]</a></span>
    </dt>
    <dd>{{% md %}}The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response's content.
This field is optional and should only be specified if a content match is required.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheck">Dict[Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make an HTTP or HTTPS check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitored_<wbr>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigmonitoredresource">Dict[Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource]</a></span>
    </dt>
    <dd>{{% md %}}The monitored resource (https://cloud.google.com/monitoring/api/resources) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigresourcegroup">Dict[Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group]</a></span>
    </dt>
    <dd>{{% md %}}The group resource associated with the configuration.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>selected_<wbr>regions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tcp_<wbr>check</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfigtcpcheck">Dict[Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check]</a></span>
    </dt>
    <dd>{{% md %}}Contains information needed to make a TCP check.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>uptime_<wbr>check_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The id of the uptime check
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Uptime<wbr>Check<wbr>Config<wbr>Content<wbr>Matcher</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#UptimeCheckConfigContentMatcher">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#UptimeCheckConfigContentMatcher">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigContentMatcherArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigContentMatcherOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#UptimeCheckConfigHttpCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#UptimeCheckConfigHttpCheck">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigHttpCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigHttpCheckOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheckauthinfo">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Auth<wbr>Info<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mask<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Validate<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheckauthinfo">*Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Auth<wbr>Info</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mask<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Validate<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheckauthinfo">Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Auth<wbr>Info?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mask<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>validate<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Info</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#uptimecheckconfighttpcheckauthinfo">Dict[Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Auth<wbr>Info]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mask<wbr>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>validate<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Uptime<wbr>Check<wbr>Config<wbr>Http<wbr>Check<wbr>Auth<wbr>Info</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#UptimeCheckConfigHttpCheckAuthInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#UptimeCheckConfigHttpCheckAuthInfo">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigHttpCheckAuthInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigHttpCheckAuthInfoOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Uptime<wbr>Check<wbr>Config<wbr>Monitored<wbr>Resource</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#UptimeCheckConfigMonitoredResource">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#UptimeCheckConfigMonitoredResource">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigMonitoredResourceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigMonitoredResourceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Uptime<wbr>Check<wbr>Config<wbr>Resource<wbr>Group</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#UptimeCheckConfigResourceGroup">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#UptimeCheckConfigResourceGroup">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigResourceGroupArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigResourceGroupOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Uptime<wbr>Check<wbr>Config<wbr>Tcp<wbr>Check</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#UptimeCheckConfigTcpCheck">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#UptimeCheckConfigTcpCheck">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigTcpCheckArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#UptimeCheckConfigTcpCheckOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
