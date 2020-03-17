
---
title: "FileSystem"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an Elastic File System (EFS) resource.

## Example Usage

### EFS File System w/ tags

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const foo = new aws.efs.FileSystem("foo", {
    tags: {
        Name: "MyProduct",
    },
});
```

### Using lifecycle policy

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const fooWithLifecylePolicy = new aws.efs.FileSystem("foo_with_lifecyle_policy", {
    lifecyclePolicy: {
        transitionToIa: "AFTER_30_DAYS",
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/efs_file_system.html.markdown.



## Create a FileSystem Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/efs/#FileSystem">FileSystem</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/efs/#FileSystemArgs">FileSystemArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">FileSystem</span><span class="p">(resource_name, opts=None, </span>creation_token=None<span class="p">, </span>encrypted=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>lifecycle_policy=None<span class="p">, </span>performance_mode=None<span class="p">, </span>provisioned_throughput_in_mibps=None<span class="p">, </span>tags=None<span class="p">, </span>throughput_mode=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFileSystem<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/efs?tab=doc#FileSystemArgs">FileSystemArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/efs?tab=doc#FileSystem">FileSystem</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Efs.FileSystem.html">FileSystem</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Efs.FileSystemArgs.html">FileSystemArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a FileSystem resource with the given unique name, arguments, and options.

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
            <td class="align-top">Creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">Pulumi.<wbr>Aws.<wbr>Efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
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
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">Creation<wbr>Token</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">*efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
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
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
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
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">creation_<wbr>token</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">Dict[file_<wbr>system_<wbr>lifecycle_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provisioned_<wbr>throughput_<wbr>in_<wbr>mibps</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throughput_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## FileSystem Output Properties

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">Pulumi.<wbr>Aws.<wbr>Efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">*efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation_<wbr>token</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">Dict[file_<wbr>system_<wbr>lifecycle_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provisioned_<wbr>throughput_<wbr>in_<wbr>mibps</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throughput_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing FileSystem Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/efs/#FileSystemState">FileSystemState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/efs/#FileSystem">FileSystem</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>creation_token=None<span class="p">, </span>dns_name=None<span class="p">, </span>encrypted=None<span class="p">, </span>kms_key_id=None<span class="p">, </span>lifecycle_policy=None<span class="p">, </span>performance_mode=None<span class="p">, </span>provisioned_throughput_in_mibps=None<span class="p">, </span>tags=None<span class="p">, </span>throughput_mode=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFileSystem<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/efs?tab=doc#FileSystemState">FileSystemState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/efs?tab=doc#FileSystem">FileSystem</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Efs.FileSystem.html">FileSystem</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Efs.FileSystemState.html">FileSystemState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing FileSystem resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">Pulumi.<wbr>Aws.<wbr>Efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>double?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
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
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Token</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dns<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">*efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>*float64</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
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
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation<wbr>Token</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle<wbr>Policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">efs.<wbr>File<wbr>System<wbr>Lifecycle<wbr>Policy?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provisioned<wbr>Throughput<wbr>In<wbr>Mibps</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
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
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throughput<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name of the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation_<wbr>token</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name (a maximum of 64 characters are allowed)
used as reference when creating the Elastic File System to ensure idempotent file
system creation. By default generated by this provider. See [Elastic File System]
(http://docs.aws.amazon.com/efs/latest/ug/) user guide for more information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dns_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS name for the filesystem per [documented convention](http://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-dns-name.html).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the disk will be encrypted.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN for the KMS encryption key. When specifying kms_key_id, encrypted needs to be set to true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lifecycle_<wbr>policy</td>
            <td class="align-top">
                
                <code><a href="#filesystemlifecyclepolicy">Dict[file_<wbr>system_<wbr>lifecycle_<wbr>policy]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A file system [lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/API_LifecyclePolicy.html) object (documented below).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">performance_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The file system performance mode. Can be either `&#34;generalPurpose&#34;` or `&#34;maxIO&#34;` (Default: `&#34;generalPurpose&#34;`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">provisioned_<wbr>throughput_<wbr>in_<wbr>mibps</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The throughput, measured in MiB/s, that you want to provision for the file system. Only applicable with `throughput_mode` set to `provisioned`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of tags to assign to the file system.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">throughput_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Throughput mode for the file system. Defaults to `bursting`. Valid values: `bursting`, `provisioned`. When using `provisioned`, also set `provisioned_throughput_in_mibps`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### FileSystemLifecyclePolicy
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#FileSystemLifecyclePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#FileSystemLifecyclePolicy">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/efs?tab=doc#FileSystemLifecyclePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/efs?tab=doc#FileSystemLifecyclePolicyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Efs.FileSystemLifecyclePolicyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Efs.FileSystemLifecyclePolicy.html">output</a> API doc for this type.
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
            <td class="align-top">Transition<wbr>To<wbr>Ia</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
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
            <td class="align-top">Transition<wbr>To<wbr>Ia</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
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
            <td class="align-top">transition<wbr>To<wbr>Ia</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
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
            <td class="align-top">transition_<wbr>to_<wbr>ia</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







