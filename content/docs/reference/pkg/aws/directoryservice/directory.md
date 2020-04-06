
---
title: "Directory"
block_external_search_index: true
---



Provides a Simple or Managed Microsoft directory in AWS Directory Service.

> **Note:** All arguments including the password and customer username will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

{{% examples %}}
## Example Usage

{{% example %}}
### SimpleAD

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
const foo = new aws.ec2.Subnet("foo", {
    availabilityZone: "us-west-2a",
    cidrBlock: "10.0.1.0/24",
    vpcId: main.id,
});
const barSubnet = new aws.ec2.Subnet("bar", {
    availabilityZone: "us-west-2b",
    cidrBlock: "10.0.2.0/24",
    vpcId: main.id,
});
const barDirectory = new aws.directoryservice.Directory("bar", {
    password: "SuperSecretPassw0rd",
    size: "Small",
    tags: {
        Project: "foo",
    },
    vpcSettings: {
        subnetIds: [
            foo.id,
            barSubnet.id,
        ],
        vpcId: main.id,
    },
});
```

{{% /example %}}
{{% example %}}
### Microsoft Active Directory (MicrosoftAD)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
const foo = new aws.ec2.Subnet("foo", {
    availabilityZone: "us-west-2a",
    cidrBlock: "10.0.1.0/24",
    vpcId: main.id,
});
const barSubnet = new aws.ec2.Subnet("bar", {
    availabilityZone: "us-west-2b",
    cidrBlock: "10.0.2.0/24",
    vpcId: main.id,
});
const barDirectory = new aws.directoryservice.Directory("bar", {
    edition: "Standard",
    password: "SuperSecretPassw0rd",
    tags: {
        Project: "foo",
    },
    type: "MicrosoftAD",
    vpcSettings: {
        subnetIds: [
            foo.id,
            barSubnet.id,
        ],
        vpcId: main.id,
    },
});
```

{{% /example %}}
{{% example %}}
### Microsoft Active Directory Connector (ADConnector)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const main = new aws.ec2.Vpc("main", {
    cidrBlock: "10.0.0.0/16",
});
const foo = new aws.ec2.Subnet("foo", {
    availabilityZone: "us-west-2a",
    cidrBlock: "10.0.1.0/24",
    vpcId: main.id,
});
const bar = new aws.ec2.Subnet("bar", {
    availabilityZone: "us-west-2b",
    cidrBlock: "10.0.2.0/24",
    vpcId: main.id,
});
const connector = new aws.directoryservice.Directory("connector", {
    connectSettings: {
        customerDnsIps: ["A.B.C.D"],
        customerUsername: "Admin",
        subnetIds: [
            foo.id,
            bar.id,
        ],
        vpcId: main.id,
    },
    password: "SuperSecretPassw0rd",
    size: "Small",
    type: "ADConnector",
});
```

{{% /example %}}
{{% /examples %}}



## Create a Directory Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directoryservice/#Directory">Directory</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directoryservice/#DirectoryArgs">DirectoryArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Directory</span><span class="p">(resource_name, opts=None, </span>alias=None<span class="p">, </span>connect_settings=None<span class="p">, </span>description=None<span class="p">, </span>edition=None<span class="p">, </span>enable_sso=None<span class="p">, </span>name=None<span class="p">, </span>password=None<span class="p">, </span>short_name=None<span class="p">, </span>size=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>vpc_settings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDirectory<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#DirectoryArgs">DirectoryArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#Directory">Directory</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directoryservice.Directory.html">Directory</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.DirectoryService.DirectoryArgs.html">DirectoryArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Directory<wbr>Connect<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Directory<wbr>Vpc<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">*Directory<wbr>Connect<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">*Directory<wbr>Vpc<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Directory<wbr>Connect<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Directory<wbr>Vpc<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Dict[Directory<wbr>Connect<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>short_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Dict[Directory<wbr>Vpc<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Directory Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Directory<wbr>Connect<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Directory<wbr>Vpc<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Access<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">*Directory<wbr>Connect<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dns<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">*Directory<wbr>Vpc<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Directory<wbr>Connect<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Directory<wbr>Vpc<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>access_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>connect_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Dict[Directory<wbr>Connect<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dns_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>short_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Dict[Directory<wbr>Vpc<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Directory Resource

Get an existing Directory resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directoryservice/#DirectoryState">DirectoryState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/directoryservice/#Directory">Directory</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>access_url=None<span class="p">, </span>alias=None<span class="p">, </span>connect_settings=None<span class="p">, </span>description=None<span class="p">, </span>dns_ip_addresses=None<span class="p">, </span>edition=None<span class="p">, </span>enable_sso=None<span class="p">, </span>name=None<span class="p">, </span>password=None<span class="p">, </span>security_group_id=None<span class="p">, </span>short_name=None<span class="p">, </span>size=None<span class="p">, </span>tags=None<span class="p">, </span>type=None<span class="p">, </span>vpc_settings=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDirectory<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#DirectoryState">DirectoryState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#Directory">Directory</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directoryservice.Directory.html">Directory</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Directoryservice.DirectoryState.html">DirectoryState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Access<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Directory<wbr>Connect<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Directory<wbr>Vpc<wbr>Settings<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Access<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">*Directory<wbr>Connect<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dns<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">*Directory<wbr>Vpc<wbr>Settings</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Directory<wbr>Connect<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns<wbr>Ip<wbr>Addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Group<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>short<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Directory<wbr>Vpc<wbr>Settings?</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>access_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The access URL for the directory, such as `http://alias.awsapps.com`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>alias</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The alias for the directory (must be unique amongst all aliases in AWS). Required for `enable_sso`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>connect_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryconnectsettings">Dict[Directory<wbr>Connect<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}Connector related information about the directory. Fields documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A textual description for the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dns_<wbr>ip_<wbr>addresses</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of IP addresses of the DNS servers for the directory or connector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>edition</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The MicrosoftAD edition (`Standard` or `Enterprise`). Defaults to `Enterprise` (applies to MicrosoftAD type only).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>sso</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to enable single-sign on for the directory. Requires `alias`. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The fully qualified name for the directory, such as `corp.example.com`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The password for the directory administrator or connector user.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>group_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the security group created by the directory.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>short_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The short name of the directory, such as `CORP`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The size of the directory (`Small` or `Large` are accepted values).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A mapping of tags to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The directory type (`SimpleAD`, `ADConnector` or `MicrosoftAD` are accepted values). Defaults to `SimpleAD`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#directoryvpcsettings">Dict[Directory<wbr>Vpc<wbr>Settings]</a></span>
    </dt>
    <dd>{{% md %}}VPC related information about the directory. Fields documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Directory<wbr>Connect<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DirectoryConnectSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DirectoryConnectSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#DirectoryConnectSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#DirectoryConnectSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Customer<wbr>Dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The DNS IP addresses of the domain to connect to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Customer<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username corresponding to the password provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Customer<wbr>Dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The DNS IP addresses of the domain to connect to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Customer<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username corresponding to the password provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>customer<wbr>Dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The DNS IP addresses of the domain to connect to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>customer<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The username corresponding to the password provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>customer<wbr>Dns<wbr>Ips</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The DNS IP addresses of the domain to connect to.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>customer<wbr>Username</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The username corresponding to the password provided.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Directory<wbr>Vpc<wbr>Settings</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DirectoryVpcSettings">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DirectoryVpcSettings">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#DirectoryVpcSettingsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/directoryservice?tab=doc#DirectoryVpcSettingsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The identifiers of the subnets for the directory servers (2 subnets in 2 different AZs).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>vpc_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identifier of the VPC that the directory is in.
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

