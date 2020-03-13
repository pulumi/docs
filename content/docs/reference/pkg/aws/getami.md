
---
title: "GetAmi"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Use this data source to get the ID of a registered AMI for use in other
resources.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = aws.getAmi({
    executableUsers: ["self"],
    filters: [
        {
            name: "name",
            values: ["myami-*"],
        },
        {
            name: "root-device-type",
            values: ["ebs"],
        },
        {
            name: "virtualization-type",
            values: ["hvm"],
        },
    ],
    mostRecent: true,
    nameRegex: "^myami-\\d{3}",
    owners: ["self"],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/ami.html.markdown.





## Using GetAmi

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getAmi<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws//#GetAmiArgs">GetAmiArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws//#GetAmiResult">GetAmiResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_ami(</span>executable_users=None<span class="p">, </span>filters=None<span class="p">, </span>most_recent=None<span class="p">, </span>name_regex=None<span class="p">, </span>owners=None<span class="p">, </span>tags=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupAmi<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetAmiArgs">GetAmiArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#LookupAmiResult">LookupAmiResult</a></span>, error)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetAmiResult.html">Pulumi.Aws.GetAmiResult</a></span>> <span class="p">GetAmi(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetAmiArgs.html">GetAmiArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>



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
            <td class="align-top">Executable<wbr>Users</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Limit search to users with *explicit* launch permission on
the image. Valid items are the numeric account ID or `self`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">List&lt;Pulumi.<wbr>Aws.<wbr>Get<wbr>Ami<wbr>Filter<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Most<wbr>Recent</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If more than one result is returned, use the most
recent AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owners</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
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
            <td class="align-top">Executable<wbr>Users</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Limit search to users with *explicit* launch permission on
the image. Valid items are the numeric account ID or `self`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">[]Get<wbr>Ami<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Most<wbr>Recent</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If more than one result is returned, use the most
recent AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Regex</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owners</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
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
            <td class="align-top">executable<wbr>Users</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Limit search to users with *explicit* launch permission on
the image. Valid items are the numeric account ID or `self`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">Get<wbr>Ami<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">most<wbr>Recent</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If more than one result is returned, use the most
recent AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owners</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
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
            <td class="align-top">executable_<wbr>users</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Limit search to users with *explicit* launch permission on
the image. Valid items are the numeric account ID or `self`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">list[get_<wbr>ami_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
One or more name/value pairs to filter off of. There are
several valid keys, for a full reference, check out
[describe-images in the AWS CLI reference][1].
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">most_<wbr>recent</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If more than one result is returned, use the most
recent AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>regex</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A regex string to apply to the AMI list returned
by AWS. This allows more advanced filtering not supported from the AWS API. This
filtering is done locally on what AWS returns, and could have a performance
impact if the result is large. It is recommended to combine this with other
options to narrow down the list AWS returns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owners</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of AMI owners to limit search. At least 1 value must be specified. Valid values: an AWS account ID, `self` (the current account), or an AWS owner alias (e.g. `amazon`, `aws-marketplace`, `microsoft`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetAmi Result

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
            <td class="align-top">Architecture</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The OS architecture of the AMI (ie: `i386` or `x86_64`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#getamiblockdevicemapping">List&lt;Pulumi.<wbr>Aws.<wbr>Get<wbr>Ami<wbr>Block<wbr>Device<wbr>Mapping&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The block device mappings of the AMI.
* `block_device_mappings.#.device_name` - The physical name of the device.
* `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
will be deleted on termination.
* `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
is encrypted.
* `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
not a provisioned IOPS image, otherwise the supported IOPS count.
* `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
* `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
* `block_device_mappings.#.ebs.volume_type` - The volume type.
* `block_device_mappings.#.no_device` - Suppresses the specified device
included in the block device mapping of the AMI.
* `block_device_mappings.#.virtual_name` - The virtual device name (for
instance stores).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the image was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The description of the AMI that was provided during image
creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Executable<wbr>Users</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">List&lt;Pulumi.<wbr>Aws.<wbr>Get<wbr>Ami<wbr>Filter&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hypervisor</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hypervisor type of the image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AMI. Should be the same as the resource `id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Location</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The location of the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Owner<wbr>Alias</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account alias (for example, `amazon`, `self`) or
the AWS account ID of the AMI owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The kernel associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Most<wbr>Recent</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the image owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owners</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The value is Windows for `Windows` AMIs; otherwise blank.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Codes</td>
            <td class="align-top">
                
                <code><a href="#getamiproductcode">List&lt;Pulumi.<wbr>Aws.<wbr>Get<wbr>Ami<wbr>Product<wbr>Code&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Any product codes associated with the AMI.
* `product_codes.#.product_code_id` - The product code.
* `product_codes.#.product_code_type` - The type of product code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} `true` if the image has public launch permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RAM disk associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The device name of the root device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of root device (ie: `ebs` or `instance-store`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The snapshot id associated with the root device, if any
(only applies to `ebs` root devices).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the AMI. If the state is `available`, the image
is successfully registered and can be used to launch an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State<wbr>Reason</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Describes a state change. Fields are `UNSET` if not available.
* `state_reason.code` - The reason code for the state change.
* `state_reason.message` - The message for the state change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Any tags assigned to the image.
* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of virtualization of the AMI (ie: `hvm` or
`paravirtual`).
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
            <td class="align-top">Architecture</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The OS architecture of the AMI (ie: `i386` or `x86_64`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#getamiblockdevicemapping">[]Get<wbr>Ami<wbr>Block<wbr>Device<wbr>Mapping</a></code>
            </td>
            <td class="align-top">{{% md %}} The block device mappings of the AMI.
* `block_device_mappings.#.device_name` - The physical name of the device.
* `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
will be deleted on termination.
* `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
is encrypted.
* `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
not a provisioned IOPS image, otherwise the supported IOPS count.
* `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
* `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
* `block_device_mappings.#.ebs.volume_type` - The volume type.
* `block_device_mappings.#.no_device` - Suppresses the specified device
included in the block device mapping of the AMI.
* `block_device_mappings.#.virtual_name` - The virtual device name (for
instance stores).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the image was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The description of the AMI that was provided during image
creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Executable<wbr>Users</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">[]Get<wbr>Ami<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hypervisor</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hypervisor type of the image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AMI. Should be the same as the resource `id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Location</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The location of the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Owner<wbr>Alias</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account alias (for example, `amazon`, `self`) or
the AWS account ID of the AMI owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The kernel associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Most<wbr>Recent</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Regex</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the image owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owners</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The value is Windows for `Windows` AMIs; otherwise blank.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Codes</td>
            <td class="align-top">
                
                <code><a href="#getamiproductcode">[]Get<wbr>Ami<wbr>Product<wbr>Code</a></code>
            </td>
            <td class="align-top">{{% md %}} Any product codes associated with the AMI.
* `product_codes.#.product_code_id` - The product code.
* `product_codes.#.product_code_type` - The type of product code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Public</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} `true` if the image has public launch permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RAM disk associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The device name of the root device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Device<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of root device (ie: `ebs` or `instance-store`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The snapshot id associated with the root device, if any
(only applies to `ebs` root devices).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the AMI. If the state is `available`, the image
is successfully registered and can be used to launch an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">State<wbr>Reason</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Describes a state change. Fields are `UNSET` if not available.
* `state_reason.code` - The reason code for the state change.
* `state_reason.message` - The message for the state change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} Any tags assigned to the image.
* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of virtualization of the AMI (ie: `hvm` or
`paravirtual`).
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
            <td class="align-top">architecture</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The OS architecture of the AMI (ie: `i386` or `x86_64`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block<wbr>Device<wbr>Mappings</td>
            <td class="align-top">
                
                <code><a href="#getamiblockdevicemapping">Get<wbr>Ami<wbr>Block<wbr>Device<wbr>Mapping[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The block device mappings of the AMI.
* `block_device_mappings.#.device_name` - The physical name of the device.
* `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
will be deleted on termination.
* `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
is encrypted.
* `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
not a provisioned IOPS image, otherwise the supported IOPS count.
* `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
* `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
* `block_device_mappings.#.ebs.volume_type` - The volume type.
* `block_device_mappings.#.no_device` - Suppresses the specified device
included in the block device mapping of the AMI.
* `block_device_mappings.#.virtual_name` - The virtual device name (for
instance stores).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation<wbr>Date</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the image was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The description of the AMI that was provided during image
creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">executable<wbr>Users</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">Get<wbr>Ami<wbr>Filter[]?</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hypervisor</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The hypervisor type of the image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AMI. Should be the same as the resource `id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Location</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The location of the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Owner<wbr>Alias</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account alias (for example, `amazon`, `self`) or
the AWS account ID of the AMI owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The kernel associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">most<wbr>Recent</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Regex</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the image owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owners</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The value is Windows for `Windows` AMIs; otherwise blank.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product<wbr>Codes</td>
            <td class="align-top">
                
                <code><a href="#getamiproductcode">Get<wbr>Ami<wbr>Product<wbr>Code[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Any product codes associated with the AMI.
* `product_codes.#.product_code_id` - The product code.
* `product_codes.#.product_code_type` - The type of product code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} `true` if the image has public launch permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ramdisk<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The RAM disk associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The device name of the root device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Device<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of root device (ie: `ebs` or `instance-store`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The snapshot id associated with the root device, if any
(only applies to `ebs` root devices).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sriov<wbr>Net<wbr>Support</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the AMI. If the state is `available`, the image
is successfully registered and can be used to launch an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state<wbr>Reason</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} Describes a state change. Fields are `UNSET` if not available.
* `state_reason.code` - The reason code for the state change.
* `state_reason.message` - The message for the state change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} Any tags assigned to the image.
* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtualization<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of virtualization of the AMI (ie: `hvm` or
`paravirtual`).
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
            <td class="align-top">architecture</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The OS architecture of the AMI (ie: `i386` or `x86_64`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">block_<wbr>device_<wbr>mappings</td>
            <td class="align-top">
                
                <code><a href="#getamiblockdevicemapping">list[get_<wbr>ami_<wbr>block_<wbr>device_<wbr>mapping]</a></code>
            </td>
            <td class="align-top">{{% md %}} The block device mappings of the AMI.
* `block_device_mappings.#.device_name` - The physical name of the device.
* `block_device_mappings.#.ebs.delete_on_termination` - `true` if the EBS volume
will be deleted on termination.
* `block_device_mappings.#.ebs.encrypted` - `true` if the EBS volume
is encrypted.
* `block_device_mappings.#.ebs.iops` - `0` if the EBS volume is
not a provisioned IOPS image, otherwise the supported IOPS count.
* `block_device_mappings.#.ebs.snapshot_id` - The ID of the snapshot.
* `block_device_mappings.#.ebs.volume_size` - The size of the volume, in GiB.
* `block_device_mappings.#.ebs.volume_type` - The volume type.
* `block_device_mappings.#.no_device` - Suppresses the specified device
included in the block device mapping of the AMI.
* `block_device_mappings.#.virtual_name` - The virtual device name (for
instance stores).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">creation_<wbr>date</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The date and time the image was created.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The description of the AMI that was provided during image
creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">executable_<wbr>users</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getamifilter">list[get_<wbr>ami_<wbr>filter]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hypervisor</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The hypervisor type of the image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the AMI. Should be the same as the resource `id`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The location of the AMI.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>owner_<wbr>alias</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account alias (for example, `amazon`, `self`) or
the AWS account ID of the AMI owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of image.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kernel_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The kernel associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">most_<wbr>recent</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>regex</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS account ID of the image owner.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owners</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The value is Windows for `Windows` AMIs; otherwise blank.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product_<wbr>codes</td>
            <td class="align-top">
                
                <code><a href="#getamiproductcode">list[get_<wbr>ami_<wbr>product_<wbr>code]</a></code>
            </td>
            <td class="align-top">{{% md %}} Any product codes associated with the AMI.
* `product_codes.#.product_code_id` - The product code.
* `product_codes.#.product_code_type` - The type of product code.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">public</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} `true` if the image has public launch permissions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ramdisk_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The RAM disk associated with the image, if any. Only applicable
for machine images.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The device name of the root device.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>device_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of root device (ie: `ebs` or `instance-store`).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The snapshot id associated with the root device, if any
(only applies to `ebs` root devices).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sriov_<wbr>net_<wbr>support</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether enhanced networking is enabled.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The current state of the AMI. If the state is `available`, the image
is successfully registered and can be used to launch an instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">state_<wbr>reason</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} Describes a state change. Fields are `UNSET` if not available.
* `state_reason.code` - The reason code for the state change.
* `state_reason.message` - The message for the state change.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} Any tags assigned to the image.
* `tags.#.key` - The key name of the tag.
* `tags.#.value` - The value of the tag.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtualization_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of virtualization of the AMI (ie: `hvm` or
`paravirtual`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetAmiBlockDeviceMapping
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetAmiBlockDeviceMapping">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetAmiBlockDeviceMapping">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetAmiBlockDeviceMapping.html">output</a> API doc for this type.
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
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">No<wbr>Device</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">No<wbr>Device</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">device<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">no<wbr>Device</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">device_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">no_<wbr>device</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">virtual_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetAmiFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetAmiFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetAmiFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetAmiFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetAmiFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetAmiFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetAmiFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the AMI that was provided during image creation.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">values</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### GetAmiProductCode
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetAmiProductCode">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/?tab=doc#GetAmiProductCode">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.GetAmiProductCode.html">output</a> API doc for this type.
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
            <td class="align-top">Product<wbr>Code<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Product<wbr>Code<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Product<wbr>Code<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">product<wbr>Code<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product<wbr>Code<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">product_<wbr>code_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">product_<wbr>code_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







