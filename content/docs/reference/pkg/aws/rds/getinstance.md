
---
title: "GetInstance"
block_external_search_index: true
---

Use this data source to get information about an RDS instance

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const database = pulumi.output(aws.rds.getInstance({
    dbInstanceIdentifier: "my-test-database",
}, { async: true }));
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/db_instance.html.markdown.





## Using GetInstance

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getInstance<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/rds/#GetInstanceArgs">GetInstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/rds/#GetInstanceResult">GetInstanceResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_instance(</span>db_instance_identifier=None<span class="p">, </span>tags=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#LookupInstanceArgs">LookupInstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/rds?tab=doc#LookupInstanceResult">LookupInstanceResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetInstance </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.GetInstanceResult.html">GetInstanceResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Rds.GetInstanceArgs.html">GetInstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Instance<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the RDS instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Db<wbr>Instance<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the RDS instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>db<wbr>Instance<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the RDS instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>db_<wbr>instance_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the RDS instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetInstance Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The hostname of the RDS instance. See also `endpoint` and `port`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allocated<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the allocated storage size specified in gigabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Minor<wbr>Version<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that minor version patches are applied automatically.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Availability Zone the DB instance is located in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days for which automatic DB snapshots are retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ca<wbr>Cert<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the identifier of the CA certificate for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Cluster<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the name of the compute and memory capacity class of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the port that the DB instance listens on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Parameter<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Provides the list of DB parameter groups applied to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Provides List of DB security groups associated to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Subnet<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the subnet group associated with the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}List of log types to export to cloudwatch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The connection endpoint in `address:port` format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Provides the name of the database engine to be used for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates the database engine version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hosted<wbr>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the Provisioned IOPS (I/O operations per second) value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>License<wbr>Model</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}License model information for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the master username for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multi<wbr>Az</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the DB instance is a Multi-AZ deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Option<wbr>Group<wbr>Memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Provides the list of option group memberships for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The database port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Backup<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the daily time range during which automated backups are created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the weekly time range during which system maintenance can occur in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publicly<wbr>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies the accessibility options for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Replicate<wbr>Source<wbr>Db</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the source DB that this is a replica of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RDS Resource ID of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the DB instance is encrypted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage type associated with DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time zone of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Provides a list of VPC security group elements that the DB instance belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The hostname of the RDS instance. See also `endpoint` and `port`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Allocated<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the allocated storage size specified in gigabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Auto<wbr>Minor<wbr>Version<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that minor version patches are applied automatically.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Availability Zone the DB instance is located in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days for which automatic DB snapshots are retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ca<wbr>Cert<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the identifier of the CA certificate for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Cluster<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the name of the compute and memory capacity class of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Instance<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the port that the DB instance listens on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Parameter<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Provides the list of DB parameter groups applied to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Provides List of DB security groups associated to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Db<wbr>Subnet<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the subnet group associated with the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of log types to export to cloudwatch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The connection endpoint in `address:port` format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Provides the name of the database engine to be used for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates the database engine version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hosted<wbr>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the Provisioned IOPS (I/O operations per second) value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>License<wbr>Model</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}License model information for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Master<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the master username for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Multi<wbr>Az</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the DB instance is a Multi-AZ deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Option<wbr>Group<wbr>Memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Provides the list of option group memberships for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The database port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Backup<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the daily time range during which automated backups are created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Preferred<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the weekly time range during which system maintenance can occur in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Publicly<wbr>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies the accessibility options for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Replicate<wbr>Source<wbr>Db</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the source DB that this is a replica of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RDS Resource ID of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the DB instance is encrypted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage type associated with DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time zone of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Provides a list of VPC security group elements that the DB instance belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The hostname of the RDS instance. See also `endpoint` and `port`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allocated<wbr>Storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the allocated storage size specified in gigabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto<wbr>Minor<wbr>Version<wbr>Upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Indicates that minor version patches are applied automatically.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Availability Zone the DB instance is located in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backup<wbr>Retention<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days for which automatic DB snapshots are retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ca<wbr>Cert<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the identifier of the CA certificate for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Cluster<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Instance<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Instance<wbr>Class</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the name of the compute and memory capacity class of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Instance<wbr>Identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Instance<wbr>Port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the port that the DB instance listens on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Parameter<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Provides the list of DB parameter groups applied to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Provides List of DB security groups associated to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db<wbr>Subnet<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the subnet group associated with the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled<wbr>Cloudwatch<wbr>Logs<wbr>Exports</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of log types to export to cloudwatch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The connection endpoint in `address:port` format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Provides the name of the database engine to be used for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Indicates the database engine version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hosted<wbr>Zone<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the Provisioned IOPS (I/O operations per second) value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>license<wbr>Model</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}License model information for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Contains the master username for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multi<wbr>Az</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Specifies if the DB instance is a Multi-AZ deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>option<wbr>Group<wbr>Memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Provides the list of option group memberships for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The database port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>preferred<wbr>Backup<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the daily time range during which automated backups are created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>preferred<wbr>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the weekly time range during which system maintenance can occur in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publicly<wbr>Accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Specifies the accessibility options for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>replicate<wbr>Source<wbr>Db</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the source DB that this is a replica of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The RDS Resource ID of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Specifies whether the DB instance is encrypted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the storage type associated with DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time zone of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Provides a list of VPC security group elements that the DB instance belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The hostname of the RDS instance. See also `endpoint` and `port`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>allocated_<wbr>storage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the allocated storage size specified in gigabytes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>auto_<wbr>minor_<wbr>version_<wbr>upgrade</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates that minor version patches are applied automatically.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>availability_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Availability Zone the DB instance is located in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>backup_<wbr>retention_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the number of days for which automatic DB snapshots are retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ca_<wbr>cert_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the identifier of the CA certificate for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>cluster_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If the DB instance is a member of a DB cluster, contains the name of the DB cluster that the DB instance is a member of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>instance_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name (ARN) for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>instance_<wbr>class</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Contains the name of the compute and memory capacity class of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>instance_<wbr>identifier</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>instance_<wbr>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the port that the DB instance listens on.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Contains the name of the initial database of this instance that was provided at create time, if one was specified when the DB instance was created. This same name is returned for the life of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>parameter_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Provides the list of DB parameter groups applied to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Provides List of DB security groups associated to this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>db_<wbr>subnet_<wbr>group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the subnet group associated with the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled_<wbr>cloudwatch_<wbr>logs_<wbr>exports</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of log types to export to cloudwatch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The connection endpoint in `address:port` format.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Provides the name of the database engine to be used for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>engine_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Indicates the database engine version.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hosted_<wbr>zone_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The canonical hosted zone ID of the DB instance (to be used in a Route 53 Alias record).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the Provisioned IOPS (I/O operations per second) value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If StorageEncrypted is true, the KMS key identifier for the encrypted DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>license_<wbr>model</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}License model information for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>master_<wbr>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Contains the master username for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN for the IAM role that permits RDS to send Enhanced Monitoring metrics to CloudWatch Logs.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>multi_<wbr>az</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if the DB instance is a Multi-AZ deployment.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>option_<wbr>group_<wbr>memberships</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Provides the list of option group memberships for this DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>port</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The database port.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>preferred_<wbr>backup_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the daily time range during which automated backups are created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>preferred_<wbr>maintenance_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the weekly time range during which system maintenance can occur in UTC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>publicly_<wbr>accessible</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies the accessibility options for the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>replicate_<wbr>source_<wbr>db</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier of the source DB that this is a replica of.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The RDS Resource ID of this instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether the DB instance is encrypted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the storage type associated with DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time zone of the DB instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Provides a list of VPC security group elements that the DB instance belongs to.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







