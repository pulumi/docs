
---
title: "Instance"
block_external_search_index: true
---



Provides an RDS instance resource. A DB instance is an isolated database
environment in the cloud. A DB instance can contain multiple user-created
databases.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/db_instance.html.markdown.



## Create a Instance Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#Instance">Instance</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Instance</span><span class="p">(resource_name, opts=None, </span>auto_renew=None<span class="p">, </span>auto_renew_period=None<span class="p">, </span>auto_upgrade_minor_version=None<span class="p">, </span>db_instance_storage_type=None<span class="p">, </span>engine=None<span class="p">, </span>engine_version=None<span class="p">, </span>force_restart=None<span class="p">, </span>instance_charge_type=None<span class="p">, </span>instance_name=None<span class="p">, </span>instance_storage=None<span class="p">, </span>instance_type=None<span class="p">, </span>maintain_time=None<span class="p">, </span>monitoring_period=None<span class="p">, </span>parameters=None<span class="p">, </span>period=None<span class="p">, </span>security_group_id=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>security_ip_mode=None<span class="p">, </span>security_ips=None<span class="p">, </span>sql_collector_config_value=None<span class="p">, </span>sql_collector_status=None<span class="p">, </span>tags=None<span class="p">, </span>vswitch_id=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#InstanceArgs">InstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.Instance.html">Instance</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.InstanceArgs.html">InstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">List&lt;Instance<wbr>Parameter<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">[]Instance<wbr>Parameter</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">Instance<wbr>Parameter[]?</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>renew_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>upgrade_<wbr>minor_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>instance_<wbr>storage_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>engine_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">List[Instance<wbr>Parameter]</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>ip_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql_<wbr>collector_<wbr>config_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql_<wbr>collector_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Instance Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">List&lt;Instance<wbr>Parameter&gt;</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">[]Instance<wbr>Parameter</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">Instance<wbr>Parameter[]</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auto_<wbr>renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto_<wbr>renew_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto_<wbr>upgrade_<wbr>minor_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connection_<wbr>string</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>instance_<wbr>storage_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>force_<wbr>restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>maintain_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">List[Instance<wbr>Parameter]</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>ip_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sql_<wbr>collector_<wbr>config_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sql_<wbr>collector_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Instance Resource

Get an existing Instance resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#Instance">Instance</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>auto_renew=None<span class="p">, </span>auto_renew_period=None<span class="p">, </span>auto_upgrade_minor_version=None<span class="p">, </span>connection_string=None<span class="p">, </span>db_instance_storage_type=None<span class="p">, </span>engine=None<span class="p">, </span>engine_version=None<span class="p">, </span>force_restart=None<span class="p">, </span>instance_charge_type=None<span class="p">, </span>instance_name=None<span class="p">, </span>instance_storage=None<span class="p">, </span>instance_type=None<span class="p">, </span>maintain_time=None<span class="p">, </span>monitoring_period=None<span class="p">, </span>parameters=None<span class="p">, </span>period=None<span class="p">, </span>port=None<span class="p">, </span>security_group_id=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>security_ip_mode=None<span class="p">, </span>security_ips=None<span class="p">, </span>sql_collector_config_value=None<span class="p">, </span>sql_collector_status=None<span class="p">, </span>tags=None<span class="p">, </span>vswitch_id=None<span class="p">, </span>zone_id=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#InstanceState">InstanceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#Instance">Instance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.Instance.html">Instance</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.InstanceState.html">InstanceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">List&lt;Instance<wbr>Parameter<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">[]Instance<wbr>Parameter</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Renew<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Upgrade<wbr>Minor<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>String</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db<wbr>Instance<wbr>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force<wbr>Restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Charge<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">Instance<wbr>Parameter[]?</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Ip<wbr>Mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql<wbr>Collector<wbr>Config<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql<wbr>Collector<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>renew</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to renewal a DB instance automatically or not. It is valid when instance_charge_type is `PrePaid`. Default to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>renew_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Auto-renewal period of an instance, in the unit of the month. It is valid when instance_charge_type is `PrePaid`. Valid value:[1~12], Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>upgrade_<wbr>minor_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The upgrade method to use. Valid values:
- Auto: Instances are automatically upgraded to a higher minor version.
- Manual: Instances are forcibly upgraded to a higher minor version when the current version is unpublished.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>string</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}RDS database connection string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>db_<wbr>instance_<wbr>storage_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The storage type of the instance. Valid values:
- local_ssd: specifies to use local SSDs. This value is recommended.
- cloud_ssd: specifies to use standard SSDs.
- cloud_essd: specifies to use enhanced SSDs (ESSDs).
- cloud_essd2: specifies to use enhanced SSDs (ESSDs).
- cloud_essd3: specifies to use enhanced SSDs (ESSDs).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database type. Value options: MySQL, SQLServer, PostgreSQL, and PPAS.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>engine_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Database version. Value options can refer to the latest docs [CreateDBInstance](https://www.alibabacloud.com/help/doc-detail/26228.htm) `EngineVersion`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>force_<wbr>restart</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set it to true to make some parameter efficient when modifying them. Default to false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>charge_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `Prepaid`, `Postpaid`, Default to `Postpaid`. Currently, the resource only supports PostPaid to PrePaid.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of DB instance. It a string of 2 to 256 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}User-defined DB instance storage space. Value range:
- [5, 2000] for MySQL/PostgreSQL/PPAS HA dual node edition;
- [20,1000] for MySQL 5.7 basic single node edition;
- [10, 2000] for SQL Server 2008R2;
- [20,2000] for SQL Server 2012 basic single node edition
Increase progressively at a rate of 5 GB. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
Note: There is extra 5 GB storage for SQL Server Instance and it is not in specified `instance_storage`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DB Instance type. For details, see [Instance type table](https://www.alibabacloud.com/help/doc-detail/26312.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintain_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Maintainable time period format of the instance: HH:MMZ-HH:MMZ (UTC time)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The monitoring frequency in seconds. Valid values are 5, 60, 300. Defaults to 300. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#instanceparameter">List[Instance<wbr>Parameter]</a></span>
    </dt>
    <dd>{{% md %}}Set of parameters needs to be set after DB instance was launched. Available parameters can refer to the latest docs [View database parameter templates](https://www.alibabacloud.com/help/doc-detail/26284.htm) .
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The duration that you will buy DB instance (in month). It is valid when instance_charge_type is `PrePaid`. Valid values: [1~9], 12, 24, 36. Default to 1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}RDS database connection port.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from 1.69.0 and use `security_group_ids` instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute `security_group_id` has been deprecated from 1.69.0 and use `security_group_ids` instead.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}, Available in 1.69.0+) The list IDs to join ECS Security Group. At most supports three security groups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>ip_<wbr>mode</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `normal`, `safety`, Default to `normal`. support `safety` switch to high security access mode 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of IP addresses allowed to access all databases of an instance. The list contains up to 1,000 IP addresses, separated by commas. Supported formats include 0.0.0.0/0, 10.23.12.24 (IP), and 10.23.12.24/24 (Classless Inter-Domain Routing (CIDR) mode. /24 represents the length of the prefix in an IP address. The range of the prefix length is [1,32]).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql_<wbr>collector_<wbr>config_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The sql collector keep time of the instance. Valid values are `1`, `30`, `180`, `365`, `1095`, `1825`, `1` is the initial value, and can't change it to `1`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sql_<wbr>collector_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The sql collector status of the instance. Valid values are `Enabled`, `Disabled`, Default to `Disabled`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
- Key: It can be up to 64 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It cannot be a null string.
- Value: It can be up to 128 characters in length. It cannot begin with "aliyun", "acs:", "http://", or "https://". It can be a null string.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vswitch_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The virtual switch ID to launch DB instances in one VPC.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Zone to launch the DB instance. From version 1.8.1, it supports multiple zone.
If it is a multi-zone and `vswitch_id` is specified, the vswitch must in the one of them.
The multiple zone ID can be retrieved by setting `multi` to "true" in the data source `alicloud..getZones`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Instance<wbr>Parameter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/input/#InstanceParameter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#InstanceParameter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#InstanceParameterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#InstanceParameterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

