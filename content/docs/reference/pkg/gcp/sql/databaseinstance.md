
---
title: "DatabaseInstance"
block_external_search_index: true
---



Creates a new Google SQL Database Instance. For more information, see the [official documentation](https://cloud.google.com/sql/),
or the [JSON API](https://cloud.google.com/sql/docs/admin-api/v1beta4/instances).

> **NOTE on `gcp.sql.DatabaseInstance`:** - First-generation instances have been
deprecated and should no longer be created, see [upgrade docs](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for more details.
To upgrade your First-generation instance, update your config that the instance has
* `settings.ip_configuration.ipv4_enabled=true`
* `settings.backup_configuration.enabled=true`
* `settings.backup_configuration.binary_log_enabled=true`.  
Apply the config, then upgrade the instance in the console as described in the documentation.
Once upgraded, update the following attributes in your config to the correct value according to
the above documentation:
* `region`
* `database_version` (if applicable)
* `tier`  
Remove any fields that are not applicable to Second-generation instances:
* `settings.crash_safe_replication`
* `settings.replication_type`
* `settings.authorized_gae_applications`
And change values to appropriate values for Second-generation instances for:
* `activation_policy` ("ON_DEMAND" is no longer an option)
* `pricing_plan` ("PER_USE" is now the only valid option)
Change `settings.backup_configuration.enabled` attribute back to its desired value and apply as necessary.

> **NOTE on `gcp.sql.DatabaseInstance`:** - Second-generation instances include a
default 'root'@'%' user with no password. This user will be deleted by the provider on
instance creation. You should use `gcp.sql.User` to define a custom user with
a restricted host and strong password.

{{% examples %}}
## Example Usage

{{% example %}}
### SQL Second Generation Instance

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const master = new gcp.sql.DatabaseInstance("master", {
    databaseVersion: "POSTGRES_11",
    region: "us-central1",
    settings: {
        // Second-generation instance tiers are based on the machine
        // type. See argument reference below.
        tier: "db-f1-micro",
    },
});
```

{{% /example %}}
{{% /examples %}}



## Create a DatabaseInstance Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/sql/#DatabaseInstance">DatabaseInstance</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/sql/#DatabaseInstanceArgs">DatabaseInstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DatabaseInstance</span><span class="p">(resource_name, opts=None, </span>database_version=None<span class="p">, </span>encryption_key_name=None<span class="p">, </span>master_instance_name=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>replica_configuration=None<span class="p">, </span>root_password=None<span class="p">, </span>settings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDatabaseInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceArgs">DatabaseInstanceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstance">DatabaseInstance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Sql.DatabaseInstance.html">DatabaseInstance</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Sql.DatabaseInstanceArgs.html">DatabaseInstanceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Database<wbr>Instance<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replica<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Database<wbr>Instance<wbr>Replica<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Database<wbr>Instance<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replica<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Database<wbr>Instance<wbr>Replica<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Database<wbr>Instance<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replica<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Database<wbr>Instance<wbr>Replica<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Dict[Database<wbr>Instance<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption_<wbr>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>instance_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replica_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Dict[Database<wbr>Instance<wbr>Replica<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## DatabaseInstance Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Connection<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>First<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">List&lt;Database<wbr>Instance<wbr>Ip<wbr>Address&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Account<wbr>Email<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Connection<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>First<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">[]Database<wbr>Instance<wbr>Ip<wbr>Address</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Server<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Account<wbr>Email<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>connection<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>first<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">Database<wbr>Instance<wbr>Ip<wbr>Address[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Account<wbr>Email<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>connection_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>first_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">List[Database<wbr>Instance<wbr>Ip<wbr>Address]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>private_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>server_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Dict[Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>account_<wbr>email_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing DatabaseInstance Resource

Get an existing DatabaseInstance resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/sql/#DatabaseInstanceState">DatabaseInstanceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/sql/#DatabaseInstance">DatabaseInstance</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>connection_name=None<span class="p">, </span>database_version=None<span class="p">, </span>encryption_key_name=None<span class="p">, </span>first_ip_address=None<span class="p">, </span>ip_addresses=None<span class="p">, </span>master_instance_name=None<span class="p">, </span>name=None<span class="p">, </span>private_ip_address=None<span class="p">, </span>project=None<span class="p">, </span>public_ip_address=None<span class="p">, </span>region=None<span class="p">, </span>replica_configuration=None<span class="p">, </span>root_password=None<span class="p">, </span>self_link=None<span class="p">, </span>server_ca_cert=None<span class="p">, </span>service_account_email_address=None<span class="p">, </span>settings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDatabaseInstance<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceState">DatabaseInstanceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstance">DatabaseInstance</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Sql.DatabaseInstance.html">DatabaseInstance</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Sql.DatabaseInstanceState.html">DatabaseInstanceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Connection<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>First<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">List&lt;Database<wbr>Instance<wbr>Ip<wbr>Address<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replica<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Database<wbr>Instance<wbr>Replica<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Email<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Database<wbr>Instance<wbr>Settings<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Connection<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>First<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">[]Database<wbr>Instance<wbr>Ip<wbr>Address</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Replica<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Database<wbr>Instance<wbr>Replica<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Server<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Email<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Database<wbr>Instance<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>connection<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>first<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">Database<wbr>Instance<wbr>Ip<wbr>Address[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Instance<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replica<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Database<wbr>Instance<wbr>Replica<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root<wbr>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server<wbr>Ca<wbr>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Email<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Database<wbr>Instance<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>connection_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The connection name of the instance to be used in
connection strings. For example, when connecting with [Cloud SQL Proxy](https://cloud.google.com/sql/docs/mysql/connect-admin-proxy).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>database_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The MySQL, PostgreSQL or
SQL Server (beta) version to use. Supported values include `MYSQL_5_6`,
`MYSQL_5_7`, `POSTGRES_9_6`,`POSTGRES_11`, `SQLSERVER_2017_STANDARD`,
`SQLSERVER_2017_ENTERPRISE`, `SQLSERVER_2017_EXPRESS`, `SQLSERVER_2017_WEB`.
[Database Version Policies](https://cloud.google.com/sql/docs/sqlserver/db-versions)
includes an up-to-date reference of supported versions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption_<wbr>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}
The full path to the encryption key used for the CMEK disk encryption.  Setting
up disk encryption currently requires manual steps outside of this provider.
The provided key must be in the same region as the SQL instance.  In order
to use this feature, a special kind of service account must be created and
granted permission on this key.  This step can currently only be done
manually, please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#service-account).
That service account needs the `Cloud KMS > Cloud KMS CryptoKey Encrypter/Decrypter` role on your
key - please see [this step](https://cloud.google.com/sql/docs/mysql/configure-cmek#grantkey).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>first_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The first IPv4 address of any type assigned.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceipaddress">List[Database<wbr>Instance<wbr>Ip<wbr>Address]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master_<wbr>instance_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The name of the instance that will act as
the master in the replication setup. Note, this requires the master to have
`binary_log_enabled` set, as well as existing backups.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The first private (`PRIVATE`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The first public (`PRIMARY`) IPv4 address assigned. 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The region the instance will sit in. Note, Cloud SQL is not
available in all regions - choose from one of the options listed [here](https://cloud.google.com/sql/docs/mysql/instance-locations).
A valid region must be provided to use this resource. If a region is not provided in the resource definition,
the provider region will be used instead, but this will be an apply-time error for instances if the provider
region is not supported with Cloud SQL. If you choose not to provide the `region` argument for this resource,
make sure you understand this.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>replica_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancereplicaconfiguration">Dict[Database<wbr>Instance<wbr>Replica<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}The configuration for replication. The
configuration is detailed below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root_<wbr>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Initial root password. Required for MS SQL Server, ignored by MySQL and PostgreSQL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>server_<wbr>ca_<wbr>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstanceservercacert">Dict[Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account_<wbr>email_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The service account email address assigned to the
instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettings">Dict[Database<wbr>Instance<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}The settings to use for the database. The
configuration is detailed below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Database<wbr>Instance<wbr>Ip<wbr>Address</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceIpAddress">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceIpAddressOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>To<wbr>Retire</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>To<wbr>Retire</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>To<wbr>Retire</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>To<wbr>Retire</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Replica<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceReplicaConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceReplicaConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceReplicaConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceReplicaConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the trusted CA's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's private key. The
corresponding public key in encoded in the `client_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Retry<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of seconds
between connect retries.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dump<wbr>File<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Path to a SQL file in GCS from which slave
instances are created. Format is `gs://bucket/filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failover<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the replica is the failover target.
If the field is set to true the replica will be designated as a failover replica.
If the master instance fails, the replica instance will be promoted as
the new master instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Heartbeat<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Time in ms between replication
heartbeats.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Password for the replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Cipher</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Username for replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verify<wbr>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}True if the master's common name
value is checked during the SSL handshake.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the trusted CA's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's private key. The
corresponding public key in encoded in the `client_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Retry<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of seconds
between connect retries.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dump<wbr>File<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Path to a SQL file in GCS from which slave
instances are created. Format is `gs://bucket/filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failover<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the replica is the failover target.
If the field is set to true the replica will be designated as a failover replica.
If the master instance fails, the replica instance will be promoted as
the new master instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Master<wbr>Heartbeat<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Time in ms between replication
heartbeats.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Password for the replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ssl<wbr>Cipher</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Username for replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verify<wbr>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}True if the master's common name
value is checked during the SSL handshake.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the trusted CA's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's private key. The
corresponding public key in encoded in the `client_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Retry<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of seconds
between connect retries.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dump<wbr>File<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Path to a SQL file in GCS from which slave
instances are created. Format is `gs://bucket/filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failover<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the replica is the failover target.
If the field is set to true the replica will be designated as a failover replica.
If the master instance fails, the replica instance will be promoted as
the new master instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Heartbeat<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Time in ms between replication
heartbeats.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Password for the replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Cipher</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Username for replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verify<wbr>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}True if the master's common name
value is checked during the SSL handshake.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ca<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the trusted CA's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's x509
certificate.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>client<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}PEM representation of the slave's private key. The
corresponding public key in encoded in the `client_certificate`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Retry<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of seconds
between connect retries.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dump<wbr>File<wbr>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Path to a SQL file in GCS from which slave
instances are created. Format is `gs://bucket/filename`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failover<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies if the replica is the failover target.
If the field is set to true the replica will be designated as a failover replica.
If the master instance fails, the replica instance will be promoted as
the new master instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>master<wbr>Heartbeat<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Time in ms between replication
heartbeats.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Password for the replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ssl<wbr>Cipher</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>username</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Username for replication connection.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verify<wbr>Server<wbr>Certificate</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}True if the master's common name
value is checked during the SSL handshake.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Server<wbr>Ca<wbr>Cert</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceServerCaCert">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceServerCaCertOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sha1Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sha1Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>common<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>create<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sha1Fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cert</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>common_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>create_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sha1_<wbr>fingerprint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The machine type to use. See [tiers](https://cloud.google.com/sql/docs/admin-api/v1beta4/tiers)
for more details and supported versions. Postgres supports only shared-core machine types such as `db-f1-micro`,
and custom machine types such as `db-custom-2-13312`. See the [Custom Machine Type Documentation](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) to learn about specifying custom machine types.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Activation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}This specifies when the instance should be
active. Can be either `ALWAYS`, `NEVER` or `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Authorized<wbr>Gae<wbr>Applications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
A list of Google App Engine (GAE) project names that are allowed to access this instance.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}This specifies whether a PostgreSQL instance
should be set up for high availability (`REGIONAL`) or single zone (`ZONAL`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsbackupconfiguration">Database<wbr>Instance<wbr>Settings<wbr>Backup<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Crash<wbr>Safe<wbr>Replication</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Specific to read instances, indicates
when crash-safe replication flags are enabled.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Flags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsdatabaseflag">List&lt;Database<wbr>Instance<wbr>Settings<wbr>Database<wbr>Flag<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Autoresize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Configuration to increase storage size automatically.  Note that future `pulumi apply` calls will attempt to resize the disk to the value specified in `disk_size` - if this is set, do not set `disk_size`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of data disk: PD_SSD or PD_HDD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfiguration">Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingslocationpreference">Database<wbr>Instance<wbr>Settings<wbr>Location<wbr>Preference<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsmaintenancewindow">Database<wbr>Instance<wbr>Settings<wbr>Maintenance<wbr>Window<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pricing<wbr>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Pricing plan for this instance, can only be `PER_USE`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Replication type for this instance, can be one of `ASYNCHRONOUS` or `SYNCHRONOUS`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A set of key/value user label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine type to use. See [tiers](https://cloud.google.com/sql/docs/admin-api/v1beta4/tiers)
for more details and supported versions. Postgres supports only shared-core machine types such as `db-f1-micro`,
and custom machine types such as `db-custom-2-13312`. See the [Custom Machine Type Documentation](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) to learn about specifying custom machine types.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Activation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}This specifies when the instance should be
active. Can be either `ALWAYS`, `NEVER` or `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Authorized<wbr>Gae<wbr>Applications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
A list of Google App Engine (GAE) project names that are allowed to access this instance.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Availability<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}This specifies whether a PostgreSQL instance
should be set up for high availability (`REGIONAL`) or single zone (`ZONAL`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Backup<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsbackupconfiguration">Database<wbr>Instance<wbr>Settings<wbr>Backup<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Crash<wbr>Safe<wbr>Replication</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Specific to read instances, indicates
when crash-safe replication flags are enabled.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Database<wbr>Flags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsdatabaseflag">[]Database<wbr>Instance<wbr>Settings<wbr>Database<wbr>Flag</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Autoresize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Configuration to increase storage size automatically.  Note that future `pulumi apply` calls will attempt to resize the disk to the value specified in `disk_size` - if this is set, do not set `disk_size`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of data disk: PD_SSD or PD_HDD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ip<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfiguration">Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location<wbr>Preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingslocationpreference">Database<wbr>Instance<wbr>Settings<wbr>Location<wbr>Preference</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsmaintenancewindow">Database<wbr>Instance<wbr>Settings<wbr>Maintenance<wbr>Window</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pricing<wbr>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Pricing plan for this instance, can only be `PER_USE`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Replication type for this instance, can be one of `ASYNCHRONOUS` or `SYNCHRONOUS`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value user label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The machine type to use. See [tiers](https://cloud.google.com/sql/docs/admin-api/v1beta4/tiers)
for more details and supported versions. Postgres supports only shared-core machine types such as `db-f1-micro`,
and custom machine types such as `db-custom-2-13312`. See the [Custom Machine Type Documentation](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) to learn about specifying custom machine types.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>activation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}This specifies when the instance should be
active. Can be either `ALWAYS`, `NEVER` or `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>authorized<wbr>Gae<wbr>Applications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
A list of Google App Engine (GAE) project names that are allowed to access this instance.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}This specifies whether a PostgreSQL instance
should be set up for high availability (`REGIONAL`) or single zone (`ZONAL`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsbackupconfiguration">Database<wbr>Instance<wbr>Settings<wbr>Backup<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>crash<wbr>Safe<wbr>Replication</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Specific to read instances, indicates
when crash-safe replication flags are enabled.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Flags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsdatabaseflag">Database<wbr>Instance<wbr>Settings<wbr>Database<wbr>Flag[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Autoresize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Configuration to increase storage size automatically.  Note that future `pulumi apply` calls will attempt to resize the disk to the value specified in `disk_size` - if this is set, do not set `disk_size`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of data disk: PD_SSD or PD_HDD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfiguration">Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location<wbr>Preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingslocationpreference">Database<wbr>Instance<wbr>Settings<wbr>Location<wbr>Preference</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsmaintenancewindow">Database<wbr>Instance<wbr>Settings<wbr>Maintenance<wbr>Window</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pricing<wbr>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Pricing plan for this instance, can only be `PER_USE`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Replication type for this instance, can be one of `ASYNCHRONOUS` or `SYNCHRONOUS`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A set of key/value user label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>tier</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The machine type to use. See [tiers](https://cloud.google.com/sql/docs/admin-api/v1beta4/tiers)
for more details and supported versions. Postgres supports only shared-core machine types such as `db-f1-micro`,
and custom machine types such as `db-custom-2-13312`. See the [Custom Machine Type Documentation](https://cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#create) to learn about specifying custom machine types.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>activation<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}This specifies when the instance should be
active. Can be either `ALWAYS`, `NEVER` or `ON_DEMAND`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>authorized<wbr>Gae<wbr>Applications</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
A list of Google App Engine (GAE) project names that are allowed to access this instance.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>availability<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}This specifies whether a PostgreSQL instance
should be set up for high availability (`REGIONAL`) or single zone (`ZONAL`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>backup<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsbackupconfiguration">Dict[Database<wbr>Instance<wbr>Settings<wbr>Backup<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>crash<wbr>Safe<wbr>Replication</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Specific to read instances, indicates
when crash-safe replication flags are enabled.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>database<wbr>Flags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsdatabaseflag">List[Database<wbr>Instance<wbr>Settings<wbr>Database<wbr>Flag]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Autoresize</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Configuration to increase storage size automatically.  Note that future `pulumi apply` calls will attempt to resize the disk to the value specified in `disk_size` - if this is set, do not set `disk_size`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of data disk, in GB. Size of a running instance cannot be reduced but can be increased.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disk<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of data disk: PD_SSD or PD_HDD.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ip_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfiguration">Dict[Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location<wbr>Preference</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingslocationpreference">Dict[Database<wbr>Instance<wbr>Settings<wbr>Location<wbr>Preference]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>maintenance<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsmaintenancewindow">Dict[Database<wbr>Instance<wbr>Settings<wbr>Maintenance<wbr>Window]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pricing<wbr>Plan</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Pricing plan for this instance, can only be `PER_USE`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>replication<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}This property is only applicable to First Generation instances.
First Generation instances are now deprecated, see [here](https://cloud.google.com/sql/docs/mysql/upgrade-2nd-gen)
for information on how to upgrade to Second Generation instances.
Replication type for this instance, can be one of `ASYNCHRONOUS` or `SYNCHRONOUS`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}This property is only applicable to First Generation instances, and First Generation instances are now deprecated.{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value user label pairs to assign to the instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings<wbr>Backup<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettingsBackupConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettingsBackupConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsBackupConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsBackupConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Binary<wbr>Log<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}True if binary logging is enabled. If
`settings.backup_configuration.enabled` is false, this must be as well.
Cannot be used with Postgres.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}True if backup configuration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}`HH:MM` format time indicating when backup
configuration starts.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Binary<wbr>Log<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}True if binary logging is enabled. If
`settings.backup_configuration.enabled` is false, this must be as well.
Cannot be used with Postgres.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}True if backup configuration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}`HH:MM` format time indicating when backup
configuration starts.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>binary<wbr>Log<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}True if binary logging is enabled. If
`settings.backup_configuration.enabled` is false, this must be as well.
Cannot be used with Postgres.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}True if backup configuration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}`HH:MM` format time indicating when backup
configuration starts.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>binary<wbr>Log<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}True if binary logging is enabled. If
`settings.backup_configuration.enabled` is false, this must be as well.
Cannot be used with Postgres.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}True if backup configuration is enabled.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}`HH:MM` format time indicating when backup
configuration starts.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings<wbr>Database<wbr>Flag</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettingsDatabaseFlag">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettingsDatabaseFlag">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsDatabaseFlagArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsDatabaseFlagOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettingsIpConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettingsIpConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsIpConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsIpConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfigurationauthorizednetwork">List&lt;Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration<wbr>Authorized<wbr>Network<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether this Cloud SQL instance should be assigned
a public IPV4 address. Either `ipv4_enabled` must be enabled or a
`private_network` must be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The VPC network from which the Cloud SQL
instance is accessible for private IP. For example, projects/myProject/global/networks/default.
Specifying a network enables private IP.
Either `ipv4_enabled` must be enabled or a `private_network` must be configured.
This setting can be updated, but it cannot be removed after it is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}True if mysqld should default to `REQUIRE X509`
for users connecting over IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfigurationauthorizednetwork">[]Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration<wbr>Authorized<wbr>Network</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ipv4Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether this Cloud SQL instance should be assigned
a public IPV4 address. Either `ipv4_enabled` must be enabled or a
`private_network` must be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Private<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The VPC network from which the Cloud SQL
instance is accessible for private IP. For example, projects/myProject/global/networks/default.
Specifying a network enables private IP.
Either `ipv4_enabled` must be enabled or a `private_network` must be configured.
This setting can be updated, but it cannot be removed after it is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}True if mysqld should default to `REQUIRE X509`
for users connecting over IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfigurationauthorizednetwork">Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration<wbr>Authorized<wbr>Network[]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether this Cloud SQL instance should be assigned
a public IPV4 address. Either `ipv4_enabled` must be enabled or a
`private_network` must be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The VPC network from which the Cloud SQL
instance is accessible for private IP. For example, projects/myProject/global/networks/default.
Specifying a network enables private IP.
Either `ipv4_enabled` must be enabled or a `private_network` must be configured.
This setting can be updated, but it cannot be removed after it is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}True if mysqld should default to `REQUIRE X509`
for users connecting over IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Networks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#databaseinstancesettingsipconfigurationauthorizednetwork">List[Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration<wbr>Authorized<wbr>Network]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ipv4Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether this Cloud SQL instance should be assigned
a public IPV4 address. Either `ipv4_enabled` must be enabled or a
`private_network` must be configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>private<wbr>Network</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The VPC network from which the Cloud SQL
instance is accessible for private IP. For example, projects/myProject/global/networks/default.
Specifying a network enables private IP.
Either `ipv4_enabled` must be enabled or a `private_network` must be configured.
This setting can be updated, but it cannot be removed after it is set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Ssl</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}True if mysqld should default to `REQUIRE X509`
for users connecting over IP.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings<wbr>Ip<wbr>Configuration<wbr>Authorized<wbr>Network</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettingsIpConfigurationAuthorizedNetwork">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettingsIpConfigurationAuthorizedNetwork">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsIpConfigurationAuthorizedNetworkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A CIDR notation IPv4 or IPv6 address that is allowed to
access this instance. Must be set even if other two attributes are not for
the whitelist to become active.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The [RFC 3339](https://tools.ietf.org/html/rfc3339)
formatted date time string indicating when this whitelist expires.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A name for this whitelist entry.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings<wbr>Location<wbr>Preference</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettingsLocationPreference">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettingsLocationPreference">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsLocationPreferenceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsLocationPreferenceOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Follow<wbr>Gae<wbr>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A GAE application whose zone to remain
in. Must be in the same region as this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The preferred compute engine
[zone](https://cloud.google.com/compute/docs/zones?hl=en).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Follow<wbr>Gae<wbr>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A GAE application whose zone to remain
in. Must be in the same region as this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The preferred compute engine
[zone](https://cloud.google.com/compute/docs/zones?hl=en).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>follow<wbr>Gae<wbr>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A GAE application whose zone to remain
in. Must be in the same region as this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The preferred compute engine
[zone](https://cloud.google.com/compute/docs/zones?hl=en).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>follow<wbr>Gae<wbr>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A GAE application whose zone to remain
in. Must be in the same region as this instance.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The preferred compute engine
[zone](https://cloud.google.com/compute/docs/zones?hl=en).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Database<wbr>Instance<wbr>Settings<wbr>Maintenance<wbr>Window</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatabaseInstanceSettingsMaintenanceWindow">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatabaseInstanceSettingsMaintenanceWindow">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsMaintenanceWindowArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/sql?tab=doc#DatabaseInstanceSettingsMaintenanceWindowOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Day</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Day of week (`1-7`), starting on Monday
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Hour of day (`0-23`), ignored if `day` not set
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Track</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Receive updates earlier (`canary`) or later
(`stable`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Day</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Day of week (`1-7`), starting on Monday
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Hour of day (`0-23`), ignored if `day` not set
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Track</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Receive updates earlier (`canary`) or later
(`stable`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>day</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Day of week (`1-7`), starting on Monday
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Hour of day (`0-23`), ignored if `day` not set
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update<wbr>Track</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Receive updates earlier (`canary`) or later
(`stable`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>day</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Day of week (`1-7`), starting on Monday
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hour</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Hour of day (`0-23`), ignored if `day` not set
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update<wbr>Track</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Receive updates earlier (`canary`) or later
(`stable`)
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

