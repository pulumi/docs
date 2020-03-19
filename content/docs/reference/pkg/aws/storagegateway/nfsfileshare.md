
---
title: "NfsFileShare"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Manages an AWS Storage Gateway NFS File Share.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.storagegateway.NfsFileShare("example", {
    clientLists: ["0.0.0.0/0"],
    gatewayArn: aws_storagegateway_gateway_example.arn,
    locationArn: aws_s3_bucket_example.arn,
    roleArn: aws_iam_role_example.arn,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/storagegateway_nfs_file_share.html.markdown.



## Create a NfsFileShare Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/storagegateway/#NfsFileShare">NfsFileShare</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/storagegateway/#NfsFileShareArgs">NfsFileShareArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NfsFileShare</span><span class="p">(resource_name, opts=None, </span>client_lists=None<span class="p">, </span>default_storage_class=None<span class="p">, </span>gateway_arn=None<span class="p">, </span>guess_mime_type_enabled=None<span class="p">, </span>kms_encrypted=None<span class="p">, </span>kms_key_arn=None<span class="p">, </span>location_arn=None<span class="p">, </span>nfs_file_share_defaults=None<span class="p">, </span>object_acl=None<span class="p">, </span>read_only=None<span class="p">, </span>requester_pays=None<span class="p">, </span>role_arn=None<span class="p">, </span>squash=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNfsFileShare<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/storagegateway?tab=doc#NfsFileShareArgs">NfsFileShareArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/storagegateway?tab=doc#NfsFileShare">NfsFileShare</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Storagegateway.NfsFileShare.html">NfsFileShare</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Storagegateway.NfsFileShareArgs.html">NfsFileShareArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a NfsFileShare resource with the given unique name, arguments, and options.

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
            <td class="align-top">Client<wbr>Lists</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">Pulumi.<wbr>Aws.<wbr>Storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Only</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Squash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
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
Key-value mapping of resource tags
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
            <td class="align-top">Client<wbr>Lists</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">*storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Acl</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Only</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Squash</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
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
Key-value mapping of resource tags
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
            <td class="align-top">client<wbr>Lists</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">squash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
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
Key-value mapping of resource tags
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
            <td class="align-top">client_<wbr>lists</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>storage_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">guess_<wbr>mime_<wbr>type_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nfs_<wbr>file_<wbr>share_<wbr>defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">Dict[Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>acl</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester_<wbr>pays</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">squash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## NfsFileShare Output Properties

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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Lists</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fileshare<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">Pulumi.<wbr>Aws.<wbr>Storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Only</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Squash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Lists</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fileshare<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">*storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Acl</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Only</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Squash</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Lists</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fileshare<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults?</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">squash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
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
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>lists</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>storage_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fileshare_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">guess_<wbr>mime_<wbr>type_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nfs_<wbr>file_<wbr>share_<wbr>defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">Dict[Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults]</a></code>
            </td>
            <td class="align-top">{{% md %}} Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>acl</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester_<wbr>pays</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">squash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing NfsFileShare Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/storagegateway/#NfsFileShareState">NfsFileShareState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/storagegateway/#NfsFileShare">NfsFileShare</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>client_lists=None<span class="p">, </span>default_storage_class=None<span class="p">, </span>fileshare_id=None<span class="p">, </span>gateway_arn=None<span class="p">, </span>guess_mime_type_enabled=None<span class="p">, </span>kms_encrypted=None<span class="p">, </span>kms_key_arn=None<span class="p">, </span>location_arn=None<span class="p">, </span>nfs_file_share_defaults=None<span class="p">, </span>object_acl=None<span class="p">, </span>read_only=None<span class="p">, </span>requester_pays=None<span class="p">, </span>role_arn=None<span class="p">, </span>squash=None<span class="p">, </span>tags=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNfsFileShare<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/storagegateway?tab=doc#NfsFileShareState">NfsFileShareState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/storagegateway?tab=doc#NfsFileShare">NfsFileShare</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Storagegateway.NfsFileShare.html">NfsFileShare</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Storagegateway.NfsFileShareState.html">NfsFileShareState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing NfsFileShare resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Lists</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fileshare<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">Pulumi.<wbr>Aws.<wbr>Storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Only</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Squash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
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
Key-value mapping of resource tags
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
Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Client<wbr>Lists</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Fileshare<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">*storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Object<wbr>Acl</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Only</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Squash</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
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
Key-value mapping of resource tags
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
Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client<wbr>Lists</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default<wbr>Storage<wbr>Class</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fileshare<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">guess<wbr>Mime<wbr>Type<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nfs<wbr>File<wbr>Share<wbr>Defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">storagegateway.<wbr>Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object<wbr>Acl</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Only</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester<wbr>Pays</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">squash</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
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
Key-value mapping of resource tags
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
Amazon Resource Name (ARN) of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">client_<wbr>lists</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of clients that are allowed to access the file gateway. The list must contain either valid IP addresses or valid CIDR blocks. Set to `[&#34;0.0.0.0/0&#34;]` to not limit access. Minimum 1 item. Maximum 100 items.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">default_<wbr>storage_<wbr>class</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default storage class for objects put into an Amazon S3 bucket by the file gateway. Defaults to `S3_STANDARD`. Valid values: `S3_STANDARD`, `S3_STANDARD_IA`, `S3_ONEZONE_IA`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">fileshare_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the NFS File Share.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">gateway_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the file gateway.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">guess_<wbr>mime_<wbr>type_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value that enables guessing of the MIME type for uploaded objects based on file extensions. Defaults to `true`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean value if `true` to use Amazon S3 server side encryption with your own AWS KMS key, or `false` to use a key managed by Amazon S3. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) for KMS key used for Amazon S3 server side encryption. This value can only be set when `kms_encrypted` is true.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the backed storage used for storing file data.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">nfs_<wbr>file_<wbr>share_<wbr>defaults</td>
            <td class="align-top">
                
                <code><a href="#nfsfilesharenfsfilesharedefaults">Dict[Nfs<wbr>File<wbr>Share<wbr>Nfs<wbr>File<wbr>Share<wbr>Defaults]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Nested argument with file share default values. More information below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">object_<wbr>acl</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Access Control List permission for S3 bucket objects. Defaults to `private`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>only</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to indicate write status of file share. File share does not accept writes if `true`. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">requester_<wbr>pays</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean who pays the cost of the request and the data download from the Amazon S3 bucket. Set this value to `true` if you want the requester to pay instead of the bucket owner. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the AWS Identity and Access Management (IAM) role that a file gateway assumes when it accesses the underlying storage.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">squash</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maps a user to anonymous user. Defaults to `RootSquash`. Valid values: `RootSquash` (only root is mapped to anonymous user), `NoSquash` (no one is mapped to anonymous user), `AllSquash` (everyone is mapped to anonymous user)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Key-value mapping of resource tags
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### NfsFileShareNfsFileShareDefaults
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#NfsFileShareNfsFileShareDefaults">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#NfsFileShareNfsFileShareDefaults">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/storagegateway?tab=doc#NfsFileShareNfsFileShareDefaultsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/storagegateway?tab=doc#NfsFileShareNfsFileShareDefaultsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Storagegateway.NfsFileShareNfsFileShareDefaultsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Storagegateway.NfsFileShareNfsFileShareDefaults.html">output</a> API doc for this type.
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
            <td class="align-top">Directory<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix directory mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0777&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">File<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix file mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0666&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Group<wbr>Id</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
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
            <td class="align-top">Directory<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix directory mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0777&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">File<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix file mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0666&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Group<wbr>Id</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
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
            <td class="align-top">directory<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix directory mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0777&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">file<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix file mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0666&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">group<wbr>Id</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
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
            <td class="align-top">directory<wbr>Mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix directory mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0777&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">file<wbr>Mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Unix file mode in the string form &#34;nnnn&#34;. Defaults to `&#34;0666&#34;`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">group<wbr>Id</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default group ID for the file share (unless the files have another group ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The default owner ID for the file share (unless the files have another owner ID specified). Defaults to `65534` (`nfsnobody`). Valid values: `0` through `4294967294`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







