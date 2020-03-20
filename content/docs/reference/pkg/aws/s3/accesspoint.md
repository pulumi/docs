
---
title: "AccessPoint"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>




## Create a AccessPoint Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#AccessPoint">AccessPoint</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#AccessPointArgs">AccessPointArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AccessPoint</span><span class="p">(resource_name, opts=None, </span>account_id=None<span class="p">, </span>bucket=None<span class="p">, </span>name=None<span class="p">, </span>policy=None<span class="p">, </span>public_access_block_configuration=None<span class="p">, </span>vpc_configuration=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAccessPoint<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPointArgs">AccessPointArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPoint">AccessPoint</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPoint.html">AccessPoint</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPointArgs.html">AccessPointArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a AccessPoint resource with the given unique name, arguments, and options.

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
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Access<wbr>Point<wbr>Vpc<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">*Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">*Access<wbr>Point<wbr>Vpc<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">s3.<wbr>Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">s3.<wbr>Access<wbr>Point<wbr>Vpc<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public_<wbr>access_<wbr>block_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">Dict[Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">Dict[Access<wbr>Point<wbr>Vpc<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## AccessPoint Output Properties

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
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Has<wbr>Public<wbr>Access<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Origin</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Access<wbr>Point<wbr>Vpc<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Has<wbr>Public<wbr>Access<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Origin</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">*Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">*Access<wbr>Point<wbr>Vpc<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">account<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">has<wbr>Public<wbr>Access<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Origin</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">s3.<wbr>Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">s3.<wbr>Access<wbr>Point<wbr>Vpc<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">has_<wbr>public_<wbr>access_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>origin</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public_<wbr>access_<wbr>block_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">Dict[Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">Dict[Access<wbr>Point<wbr>Vpc<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing AccessPoint Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#AccessPointState">AccessPointState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/s3/#AccessPoint">AccessPoint</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>account_id=None<span class="p">, </span>arn=None<span class="p">, </span>bucket=None<span class="p">, </span>domain_name=None<span class="p">, </span>has_public_access_policy=None<span class="p">, </span>name=None<span class="p">, </span>network_origin=None<span class="p">, </span>policy=None<span class="p">, </span>public_access_block_configuration=None<span class="p">, </span>vpc_configuration=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAccessPoint<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPointState">AccessPointState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPoint">AccessPoint</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPoint.html">AccessPoint</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPointState.html">AccessPointState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing AccessPoint resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Has<wbr>Public<wbr>Access<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Origin</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">Pulumi.<wbr>Aws.<wbr>S3.<wbr>Access<wbr>Point<wbr>Vpc<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">Account<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Bucket</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Domain<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Has<wbr>Public<wbr>Access<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Network<wbr>Origin</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Policy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">*Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">*Access<wbr>Point<wbr>Vpc<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">account<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">has<wbr>Public<wbr>Access<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network<wbr>Origin</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public<wbr>Access<wbr>Block<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">s3.<wbr>Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">s3.<wbr>Access<wbr>Point<wbr>Vpc<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
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
            <td class="align-top">account_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of the S3 Access Point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">bucket</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the bucket that you want to associate this access point with.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">domain_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DNS domain name of the S3 Access Point in the format _`name`_-_`account_id`_.s3-accesspoint._region_.amazonaws.com.
Note: S3 access points only support secure access by HTTPS. HTTP isn&#39;t supported.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">has_<wbr>public_<wbr>access_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point currently has a policy that allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name you want to assign to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">network_<wbr>origin</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether this access point allows access from the public Internet. Values are `VPC` (the access point doesn&#39;t allow access from the public Internet) and `Internet` (the access point allows access from the public Internet, subject to the access point and bucket access policies).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">policy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A valid JSON document that specifies the policy that you want to apply to this access point.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public_<wbr>access_<wbr>block_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointpublicaccessblockconfiguration">Dict[Access<wbr>Point<wbr>Public<wbr>Access<wbr>Block<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to manage the `PublicAccessBlock` configuration that you want to apply to this Amazon S3 bucket. You can enable the configuration options in any combination. Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>configuration</td>
            <td class="align-top">
                
                <code><a href="#accesspointvpcconfiguration">Dict[Access<wbr>Point<wbr>Vpc<wbr>Configuration]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block to restrict access to this access point to requests from the specified Virtual Private Cloud (VPC). Detailed below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### AccessPointPublicAccessBlockConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AccessPointPublicAccessBlockConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AccessPointPublicAccessBlockConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPointPublicAccessBlockConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPointPublicAccessBlockConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPointPublicAccessBlockConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPointPublicAccessBlockConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
* PUT Object calls fail if the request includes a public ACL.
* PUT Bucket calls fail if the request includes a public ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore all public ACLs on buckets in this account and any objects that they contain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access buckets with public policies.
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
            <td class="align-top">Block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
* PUT Object calls fail if the request includes a public ACL.
* PUT Bucket calls fail if the request includes a public ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore all public ACLs on buckets in this account and any objects that they contain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access buckets with public policies.
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
            <td class="align-top">block<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
* PUT Object calls fail if the request includes a public ACL.
* PUT Bucket calls fail if the request includes a public ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Public<wbr>Policy</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore<wbr>Public<wbr>Acls</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore all public ACLs on buckets in this account and any objects that they contain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict<wbr>Public<wbr>Buckets</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access buckets with public policies.
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
            <td class="align-top">block_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing policies or ACLs. When set to `true` causes the following behavior:
* PUT Bucket acl and PUT Object acl calls fail if the specified ACL is public.
* PUT Object calls fail if the request includes a public ACL.
* PUT Bucket calls fail if the request includes a public ACL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>public_<wbr>policy</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should block public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect existing bucket policies. When set to `true` causes Amazon S3 to:
* Reject calls to PUT Bucket policy if the specified bucket policy allows public access.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ignore_<wbr>public_<wbr>acls</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should ignore public ACLs for buckets in this account. Defaults to `true`. Enabling this setting does not affect the persistence of any existing ACLs and doesn&#39;t prevent new public ACLs from being set. When set to `true` causes Amazon S3 to:
* Ignore all public ACLs on buckets in this account and any objects that they contain.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">restrict_<wbr>public_<wbr>buckets</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether Amazon S3 should restrict public bucket policies for buckets in this account. Defaults to `true`. Enabling this setting does not affect previously stored bucket policies, except that public and cross-account access within any public bucket policy, including non-public delegation to specific accounts, is blocked. When set to `true`:
* Only the bucket owner and AWS Services can access buckets with public policies.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### AccessPointVpcConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#AccessPointVpcConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#AccessPointVpcConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPointVpcConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/s3?tab=doc#AccessPointVpcConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPointVpcConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.S3.AccessPointVpcConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This access point will only allow connections from the specified VPC ID.
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
            <td class="align-top">Vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This access point will only allow connections from the specified VPC ID.
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
            <td class="align-top">vpc<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This access point will only allow connections from the specified VPC ID.
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
            <td class="align-top">vpc_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
This access point will only allow connections from the specified VPC ID.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







