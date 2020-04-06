
---
title: "BackupPolicy"
block_external_search_index: true
---



Provides an RDS instance backup policy resource and used to configure instance backup policy.

> **NOTE:** Each DB instance has a backup policy and it will be set default values when destroying the resource.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/db_backup_policy.html.markdown.



## Create a BackupPolicy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#BackupPolicy">BackupPolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#BackupPolicyArgs">BackupPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">BackupPolicy</span><span class="p">(resource_name, opts=None, </span>archive_backup_keep_count=None<span class="p">, </span>archive_backup_keep_policy=None<span class="p">, </span>archive_backup_retention_period=None<span class="p">, </span>backup_periods=None<span class="p">, </span>backup_retention_period=None<span class="p">, </span>backup_time=None<span class="p">, </span>compress_type=None<span class="p">, </span>enable_backup_log=None<span class="p">, </span>high_space_usage_protection=None<span class="p">, </span>instance_id=None<span class="p">, </span>local_log_retention_hours=None<span class="p">, </span>local_log_retention_space=None<span class="p">, </span>log_backup=None<span class="p">, </span>log_backup_frequency=None<span class="p">, </span>log_backup_retention_period=None<span class="p">, </span>log_retention_period=None<span class="p">, </span>preferred_backup_periods=None<span class="p">, </span>preferred_backup_time=None<span class="p">, </span>retention_period=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBackupPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#BackupPolicyArgs">BackupPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#BackupPolicy">BackupPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.BackupPolicy.html">BackupPolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.BackupPolicyArgs.html">BackupPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive_<wbr>backup_<wbr>keep_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive_<wbr>backup_<wbr>keep_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive_<wbr>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup_<wbr>periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>compress_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>backup_<wbr>log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high_<wbr>space_<wbr>usage_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local_<wbr>log_<wbr>retention_<wbr>hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local_<wbr>log_<wbr>retention_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log_<wbr>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>backup_<wbr>frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>backup_<wbr>periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>backup_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}







## BackupPolicy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>High<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>High<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>high<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>archive_<wbr>backup_<wbr>keep_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>archive_<wbr>backup_<wbr>keep_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>archive_<wbr>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>backup_<wbr>periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>backup_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>compress_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>backup_<wbr>log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>high_<wbr>space_<wbr>usage_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local_<wbr>log_<wbr>retention_<wbr>hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>local_<wbr>log_<wbr>retention_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>log_<wbr>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>log_<wbr>backup_<wbr>frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>log_<wbr>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>log_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>preferred_<wbr>backup_<wbr>periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>preferred_<wbr>backup_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}








## Look up an Existing BackupPolicy Resource

Get an existing BackupPolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#BackupPolicyState">BackupPolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/rds/#BackupPolicy">BackupPolicy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>archive_backup_keep_count=None<span class="p">, </span>archive_backup_keep_policy=None<span class="p">, </span>archive_backup_retention_period=None<span class="p">, </span>backup_periods=None<span class="p">, </span>backup_retention_period=None<span class="p">, </span>backup_time=None<span class="p">, </span>compress_type=None<span class="p">, </span>enable_backup_log=None<span class="p">, </span>high_space_usage_protection=None<span class="p">, </span>instance_id=None<span class="p">, </span>local_log_retention_hours=None<span class="p">, </span>local_log_retention_space=None<span class="p">, </span>log_backup=None<span class="p">, </span>log_backup_frequency=None<span class="p">, </span>log_backup_retention_period=None<span class="p">, </span>log_retention_period=None<span class="p">, </span>preferred_backup_periods=None<span class="p">, </span>preferred_backup_time=None<span class="p">, </span>retention_period=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetBackupPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#BackupPolicyState">BackupPolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/rds?tab=doc#BackupPolicy">BackupPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.BackupPolicy.html">BackupPolicy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Rds.BackupPolicyState.html">BackupPolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Backup<wbr>Keep<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Backup<wbr>Keep<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>compress<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Backup<wbr>Log</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Space<wbr>Usage<wbr>Protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Log<wbr>Retention<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local<wbr>Log<wbr>Retention<wbr>Space</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Backup<wbr>Frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log<wbr>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>Backup<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred<wbr>Backup<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>archive_<wbr>backup_<wbr>keep_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep count. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. When `archive_backup_keep_policy` is `ByMonth` Valid values: [1-31]. When `archive_backup_keep_policy` is `ByWeek` Valid values: [1-7].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive_<wbr>backup_<wbr>keep_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance archive backup keep policy. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values are `ByMonth`, `Disable`, `KeepAll`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>archive_<wbr>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance archive backup retention days. Valid when the `enable_backup_log` is `true` and instance is mysql local disk. Valid values: [30-1095], and `archive_backup_retention_period` must larger than `backup_retention_period` 730.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup_<wbr>periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_period&#39; has been deprecated from version 1.69.0. Use `preferred_backup_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance backup retention days. Valid values: [7-730]. Default to 7. But mysql local disk is unlimited.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>backup_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'preferred_backup_time' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;backup_time&#39; has been deprecated from version 1.69.0. Use `preferred_backup_time` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>compress_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The compress type of instance policy. Valid values are `1`, `4`, `8`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>backup_<wbr>log</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to backup instance log. Valid values are `true`, `false`, Default to `true`. Note: The 'Basic Edition' category Rds instance does not support setting log backup. [What is Basic Edition](https://www.alibabacloud.com/help/doc-detail/48980.htm).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high_<wbr>space_<wbr>usage_<wbr>protection</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance high space usage protection policy. Valid when the `enable_backup_log` is `true`. Valid values are `Enable`, `Disable`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>instance_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Id of instance that can run database.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local_<wbr>log_<wbr>retention_<wbr>hours</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention hours. Valid when the `enable_backup_log` is `true`. Valid values: [0-7*24].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>local_<wbr>log_<wbr>retention_<wbr>space</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup local retention space. Valid when the `enable_backup_log` is `true`. Valid values: [5-50].
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log_<wbr>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.68.0, and use field 'enable_backup_log' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_backup&#39; has been deprecated from version 1.68.0. Use `enable_backup_log` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>backup_<wbr>frequency</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Instance log backup frequency. Valid when the instance engine is `SQLServer`. Valid values are `LogInterval`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>log_<wbr>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Instance log backup retention days. Valid when the `enable_backup_log` is `1`. Valid values: [7-730]. Default to 7. It cannot be larger than `backup_retention_period`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>log_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'log_backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;log_retention_period&#39; has been deprecated from version 1.69.0. Use `log_backup_retention_period` instead{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>backup_<wbr>periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}DB Instance backup period. Please set at least two days to ensure backing up at least twice a week. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"].
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>preferred_<wbr>backup_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DB instance backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}It has been deprecated from version 1.69.0, and use field 'backup_retention_period' instead.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Attribute &#39;retention_period&#39; has been deprecated from version 1.69.0. Use `backup_retention_period` instead{{% /md %}}</p></dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

