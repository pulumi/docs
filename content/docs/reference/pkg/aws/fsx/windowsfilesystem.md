
---
title: "WindowsFileSystem"
block_external_search_index: true
---



Manages a FSx Windows File System. See the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html) for more information.

> **NOTE:** Either the `active_directory_id` argument or `self_managed_active_directory` configuration block must be specified.

{{% examples %}}
## Example Usage

{{% example %}}
### Using AWS Directory Service

Additional information for using AWS Directory Service with Windows File Systems can be found in the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsx-aws-managed-ad.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.fsx.WindowsFileSystem("example", {
    activeDirectoryId: aws_directory_service_directory_example.id,
    kmsKeyId: aws_kms_key_example.arn,
    storageCapacity: 300,
    subnetIds: aws_subnet_example.id,
    throughputCapacity: 1024,
});
```

{{% /example %}}
{{% example %}}
### Using a Self-Managed Microsoft Active Directory

Additional information for using AWS Directory Service with Windows File Systems can be found in the [FSx Windows Guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/self-managed-AD.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.fsx.WindowsFileSystem("example", {
    kmsKeyId: aws_kms_key_example.arn,
    selfManagedActiveDirectory: {
        dnsIps: [
            "10.0.0.111",
            "10.0.0.222",
        ],
        domainName: "corp.example.com",
        password: "avoid-plaintext-passwords",
        username: "Admin",
    },
    storageCapacity: 300,
    subnetIds: aws_subnet_example.id,
    throughputCapacity: 1024,
});
```

{{% /example %}}
{{% /examples %}}



## Create a WindowsFileSystem Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/fsx/#WindowsFileSystem">WindowsFileSystem</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/fsx/#WindowsFileSystemArgs">WindowsFileSystemArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">WindowsFileSystem</span><span class="p">(resource_name, opts=None, </span>active_directory_id=None<span class="p">, </span>automatic_backup_retention_days=None<span class="p">, </span>copy_tags_to_backups=None<span class="p">, </span>daily_automatic_backup_start_time=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>self_managed_active_directory=None<span class="p">, </span>skip_final_backup=None<span class="p">, </span>storage_capacity=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>throughput_capacity=None<span class="p">, </span>weekly_maintenance_start_time=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewWindowsFileSystem<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/fsx?tab=doc#WindowsFileSystemArgs">WindowsFileSystemArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/fsx?tab=doc#WindowsFileSystem">WindowsFileSystem</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Fsx.WindowsFileSystem.html">WindowsFileSystem</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Fsx.WindowsFileSystemArgs.html">WindowsFileSystemArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">*Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>directory_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic_<wbr>backup_<wbr>retention_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy_<wbr>tags_<wbr>to_<wbr>backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>daily_<wbr>automatic_<wbr>backup_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>managed_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Dict[Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip_<wbr>final_<wbr>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>throughput_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weekly_<wbr>maintenance_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## WindowsFileSystem Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">*Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>active_<wbr>directory_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>automatic_<wbr>backup_<wbr>retention_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>copy_<wbr>tags_<wbr>to_<wbr>backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>daily_<wbr>automatic_<wbr>backup_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>network_<wbr>interface_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>managed_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Dict[Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>skip_<wbr>final_<wbr>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>throughput_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>weekly_<wbr>maintenance_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing WindowsFileSystem Resource

Get an existing WindowsFileSystem resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/fsx/#WindowsFileSystemState">WindowsFileSystemState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/fsx/#WindowsFileSystem">WindowsFileSystem</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>active_directory_id=None<span class="p">, </span>arn=None<span class="p">, </span>automatic_backup_retention_days=None<span class="p">, </span>copy_tags_to_backups=None<span class="p">, </span>daily_automatic_backup_start_time=None<span class="p">, </span>dns_name=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>network_interface_ids=None<span class="p">, </span>owner_id=None<span class="p">, </span>security_group_ids=None<span class="p">, </span>self_managed_active_directory=None<span class="p">, </span>skip_final_backup=None<span class="p">, </span>storage_capacity=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>throughput_capacity=None<span class="p">, </span>vpc_id=None<span class="p">, </span>weekly_maintenance_start_time=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetWindowsFileSystem<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/fsx?tab=doc#WindowsFileSystemState">WindowsFileSystemState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/fsx?tab=doc#WindowsFileSystem">WindowsFileSystem</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Fsx.WindowsFileSystem.html">WindowsFileSystem</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Fsx.WindowsFileSystemState.html">WindowsFileSystemState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">*Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active<wbr>Directory<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic<wbr>Backup<wbr>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy<wbr>Tags<wbr>To<wbr>Backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>daily<wbr>Automatic<wbr>Backup<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms<wbr>Key<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network<wbr>Interface<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Group<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Managed<wbr>Active<wbr>Directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory?</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Final<wbr>Backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throughput<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weekly<wbr>Maintenance<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>active_<wbr>directory_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID for an existing Microsoft Active Directory instance that the file system should join when it's created. Cannot be specified with `self_managed_active_directory`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Amazon Resource Name of the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>automatic_<wbr>backup_<wbr>retention_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of days to retain automatic backups. Minimum of `0` and maximum of `35`. Defaults to `7`. Set to `0` to disable.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>copy_<wbr>tags_<wbr>to_<wbr>backups</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}A boolean flag indicating whether tags on the file system should be copied to backups. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>daily_<wbr>automatic_<wbr>backup_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The preferred time (in `HH:MM` format) to take daily automatic backups, in the UTC time zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}DNS name for the file system, e.g. `fs-12345678.corp.example.com` (domain name matching the Active Directory domain name)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kms_<wbr>key_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ARN for the KMS Key to encrypt the file system at rest. Defaults to an AWS managed KMS Key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>network_<wbr>interface_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Set of Elastic Network Interface identifiers from which the file system is accessible.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>owner_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AWS account identifier that created the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>group_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the security groups that apply to the specified network interfaces created for file system access. These security groups will apply to all network interfaces.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>managed_<wbr>active_<wbr>directory</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#windowsfilesystemselfmanagedactivedirectory">Dict[Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory]</a></span>
    </dt>
    <dd>{{% md %}}Configuration block that Amazon FSx uses to join the Windows File Server instance to your self-managed (including on-premises) Microsoft Active Directory (AD) directory. Cannot be specified with `active_directory_id`. Detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip_<wbr>final_<wbr>backup</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When enabled, will skip the default final backup taken when the file system is deleted. This configuration must be applied separately before attempting to delete the resource to have the desired behavior. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Storage capacity (GiB) of the file system. Minimum of 32 and maximum of 65536.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A list of IDs for the subnets that the file system will be accessible from. File systems support only one subnet. The file server is also launched in that subnet's Availability Zone.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>throughput_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Throughput (megabytes per second) of the file system in power of 2 increments. Minimum of `8` and maximum of `2048`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Identifier of the Virtual Private Cloud for the file system.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>weekly_<wbr>maintenance_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The preferred start time (in `d:HH:MM` format) to perform weekly maintenance, in the UTC time zone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Windows<wbr>File<wbr>System<wbr>Self<wbr>Managed<wbr>Active<wbr>Directory</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#WindowsFileSystemSelfManagedActiveDirectory">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#WindowsFileSystemSelfManagedActiveDirectory">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/fsx?tab=doc#WindowsFileSystemSelfManagedActiveDirectoryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/fsx?tab=doc#WindowsFileSystemSelfManagedActiveDirectoryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>System<wbr>Administrators<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organizational<wbr>Unit<wbr>Distinguished<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>File<wbr>System<wbr>Administrators<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Organizational<wbr>Unit<wbr>Distinguished<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>System<wbr>Administrators<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organizational<wbr>Unit<wbr>Distinguished<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dns_<wbr>ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of up to two IP addresses of DNS servers or domain controllers in the self-managed AD directory. The IP addresses need to be either in the same VPC CIDR range as the file system or in the private IP version 4 (IPv4) address ranges as specified in [RFC 1918](https://tools.ietf.org/html/rfc1918).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>domain_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified domain name of the self-managed AD directory. For example, `corp.example.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>file<wbr>System<wbr>Administrators<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the domain group whose members are granted administrative privileges for the file system. Administrative privileges include taking ownership of files and folders, and setting audit controls (audit ACLs) on files and folders. The group that you specify must already exist in your domain. Defaults to `Domain Admins`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>organizational<wbr>Unit<wbr>Distinguished<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified distinguished name of the organizational unit within your self-managed AD directory that the Windows File Server instance will join. For example, `OU=FSx,DC=yourdomain,DC=corp,DC=com`. Only accepts OU as the direct parent of the file system. If none is provided, the FSx file system is created in the default location of your self-managed AD directory. To learn more, see [RFC 2253](https://tools.ietf.org/html/rfc2253).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user name for the service account on your self-managed AD domain that Amazon FSx will use to join to your AD domain.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).</dd>
</dl>

