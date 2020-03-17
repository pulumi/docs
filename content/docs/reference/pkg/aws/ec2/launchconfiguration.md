
---
title: "LaunchConfiguration"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a resource to create a new launch configuration, used for autoscaling groups.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ubuntu = aws.getAmi({
    filters: [
        {
            name: "name",
            values: ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"],
        },
        {
            name: "virtualization-type",
            values: ["hvm"],
        },
    ],
    mostRecent: true,
    owners: ["099720109477"], // Canonical
});
const asConf = new aws.ec2.LaunchConfiguration("as_conf", {
    imageId: ubuntu.id,
    instanceType: "t2.micro",
});
```

## Using with AutoScaling Groups

Launch Configurations cannot be updated after creation with the Amazon
Web Service API. In order to update a Launch Configuration, this provider will
destroy the existing resource and create a replacement. In order to effectively
use a Launch Configuration resource with an [AutoScaling Group resource][1],
it's recommended to specify `create_before_destroy` in a [lifecycle][2] block.
Either omit the Launch Configuration `name` attribute, or specify a partial name
with `name_prefix`.  Example:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ubuntu = aws.getAmi({
    filters: [
        {
            name: "name",
            values: ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"],
        },
        {
            name: "virtualization-type",
            values: ["hvm"],
        },
    ],
    mostRecent: true,
    owners: ["099720109477"], // Canonical
});
const asConf = new aws.ec2.LaunchConfiguration("as_conf", {
    imageId: ubuntu.id,
    instanceType: "t2.micro",
    namePrefix: "lc-example-",
});
const bar = new aws.autoscaling.Group("bar", {
    launchConfiguration: asConf.name,
    maxSize: 2,
    minSize: 1,
});
```

With this setup this provider generates a unique name for your Launch
Configuration and can then update the AutoScaling Group without conflict before
destroying the previous Launch Configuration.

## Using with Spot Instances

Launch configurations can set the spot instance pricing to be used for the
Auto Scaling Group to reserve instances. Simply specifying the `spot_price`
parameter will set the price on the Launch Configuration which will attempt to
reserve your instances at this price.  See the [AWS Spot Instance
documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
for more information or how to launch [Spot Instances][3] with this provider.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ubuntu = aws.getAmi({
    filters: [
        {
            name: "name",
            values: ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"],
        },
        {
            name: "virtualization-type",
            values: ["hvm"],
        },
    ],
    mostRecent: true,
    owners: ["099720109477"], // Canonical
});
const asConf = new aws.ec2.LaunchConfiguration("as_conf", {
    imageId: ubuntu.id,
    instanceType: "m4.large",
    spotPrice: "0.001",
});
const bar = new aws.autoscaling.Group("bar", {
    launchConfiguration: asConf.name,
});
```

## Block devices

Each of the `*_block_device` attributes controls a portion of the AWS
Launch Configuration's "Block Device Mapping". It's a good idea to familiarize yourself with [AWS's Block Device
Mapping docs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html)
to understand the implications of using these attributes.

The `root_block_device` mapping supports the following:

* `volume_type` - (Optional) The type of volume. Can be `"standard"`, `"gp2"`,
  or `"io1"`. (Default: `"standard"`).
* `volume_size` - (Optional) The size of the volume in gigabytes.
* `iops` - (Optional) The amount of provisioned
  [IOPS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
  This must be set with a `volume_type` of `"io1"`.
* `delete_on_termination` - (Optional) Whether the volume should be destroyed
  on instance termination (Default: `true`).
* `encrypted` - (Optional) Whether the volume should be encrypted or not. (Default: `false`).

Modifying any of the `root_block_device` settings requires resource
replacement.

Each `ebs_block_device` supports the following:

* `device_name` - (Required) The name of the device to mount.
* `snapshot_id` - (Optional) The Snapshot ID to mount.
* `volume_type` - (Optional) The type of volume. Can be `"standard"`, `"gp2"`,
  or `"io1"`. (Default: `"standard"`).
* `volume_size` - (Optional) The size of the volume in gigabytes.
* `iops` - (Optional) The amount of provisioned
  [IOPS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-io-characteristics.html).
  This must be set with a `volume_type` of `"io1"`.
* `delete_on_termination` - (Optional) Whether the volume should be destroyed
  on instance termination (Default: `true`).
* `encrypted` - (Optional) Whether the volume should be encrypted or not. Do not use this option if you are using `snapshot_id` as the encrypted flag will be determined by the snapshot. (Default: `false`).

Modifying any `ebs_block_device` currently requires resource replacement.

Each `ephemeral_block_device` supports the following:

* `device_name` - The name of the block device to mount on the instance.
* `virtual_name` - The [Instance Store Device
  Name](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#InstanceStoreDeviceNames)
  (e.g. `"ephemeral0"`)

Each AWS Instance type has a different set of Instance Store block devices
available for attachment. AWS [publishes a
list](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html#StorageOnInstanceTypes)
of which ephemeral devices are available on each type. The devices are always
identified by the `virtual_name` in the format `"ephemeral{0..N}"`.

> **NOTE:** Changes to `*_block_device` configuration of _existing_ resources
cannot currently be detected by this provider. After updating to block device
configuration, resource recreation can be manually triggered by using the
[`taint` command](https://www.terraform.io/docs/commands/taint.html).

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/launch_configuration.html.markdown.



## Create a LaunchConfiguration Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchConfiguration">LaunchConfiguration</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchConfigurationArgs">LaunchConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">LaunchConfiguration</span><span class="p">(resource_name, opts=None, </span>associate_public_ip_address=None<span class="p">, </span>ebs_block_devices=None<span class="p">, </span>ebs_optimized=None<span class="p">, </span>enable_monitoring=None<span class="p">, </span>ephemeral_block_devices=None<span class="p">, </span>iam_instance_profile=None<span class="p">, </span>image_id=None<span class="p">, </span>instance_type=None<span class="p">, </span>key_name=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>placement_tenancy=None<span class="p">, </span>root_block_device=None<span class="p">, </span>security_groups=None<span class="p">, </span>spot_price=None<span class="p">, </span>user_data=None<span class="p">, </span>user_data_base64=None<span class="p">, </span>vpc_classic_link_id=None<span class="p">, </span>vpc_classic_link_security_groups=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewLaunchConfiguration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationArgs">LaunchConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfiguration">LaunchConfiguration</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfiguration.html">LaunchConfiguration</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationArgs.html">LaunchConfigurationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a LaunchConfiguration resource with the given unique name, arguments, and options.

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
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">[]ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">[]ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">*ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
            <td class="align-top">associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string | Instance<wbr>Profile</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
            <td class="align-top">associate_<wbr>public_<wbr>ip_<wbr>address</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">List[launch_<wbr>configuration_<wbr>ebs_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">List[launch_<wbr>configuration_<wbr>ephemeral_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>block_<wbr>device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">Dict[launch_<wbr>configuration_<wbr>root_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>price</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data_<wbr>base64</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## LaunchConfiguration Output Properties

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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The key name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">[]ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">[]ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The key name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device[]</a></code>
            </td>
            <td class="align-top">{{% md %}} Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The key name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
            <td class="align-top">{{% md %}} The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associate_<wbr>public_<wbr>ip_<wbr>address</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">List[launch_<wbr>configuration_<wbr>ebs_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">List[launch_<wbr>configuration_<wbr>ephemeral_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The key name that should be used for the instance.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>block_<wbr>device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">Dict[launch_<wbr>configuration_<wbr>root_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>price</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data_<wbr>base64</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing LaunchConfiguration Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchConfigurationState">LaunchConfigurationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#LaunchConfiguration">LaunchConfiguration</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>arn=None<span class="p">, </span>associate_public_ip_address=None<span class="p">, </span>ebs_block_devices=None<span class="p">, </span>ebs_optimized=None<span class="p">, </span>enable_monitoring=None<span class="p">, </span>ephemeral_block_devices=None<span class="p">, </span>iam_instance_profile=None<span class="p">, </span>image_id=None<span class="p">, </span>instance_type=None<span class="p">, </span>key_name=None<span class="p">, </span>name=None<span class="p">, </span>name_prefix=None<span class="p">, </span>placement_tenancy=None<span class="p">, </span>root_block_device=None<span class="p">, </span>security_groups=None<span class="p">, </span>spot_price=None<span class="p">, </span>user_data=None<span class="p">, </span>user_data_base64=None<span class="p">, </span>vpc_classic_link_id=None<span class="p">, </span>vpc_classic_link_security_groups=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetLaunchConfiguration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationState">LaunchConfigurationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfiguration">LaunchConfiguration</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfiguration.html">LaunchConfiguration</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationState.html">LaunchConfigurationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing LaunchConfiguration resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">List&lt;Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">Pulumi.<wbr>Aws.<wbr>Ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">[]ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">[]ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Image<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Key<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">*ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Spot<wbr>Price</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">User<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associate<wbr>Public<wbr>Ip<wbr>Address</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs<wbr>Optimized</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable<wbr>Monitoring</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral<wbr>Block<wbr>Devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam<wbr>Instance<wbr>Profile</td>
            <td class="align-top">
                
                <code>string | Instance<wbr>Profile</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement<wbr>Tenancy</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root<wbr>Block<wbr>Device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">ec2.<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot<wbr>Price</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user<wbr>Data<wbr>Base64</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
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
The Amazon Resource Name of the launch configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">associate_<wbr>public_<wbr>ip_<wbr>address</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Associate a public ip address with an instance in a VPC.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationebsblockdevice">List[launch_<wbr>configuration_<wbr>ebs_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Additional EBS block devices to attach to the
instance.  See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ebs_<wbr>optimized</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If true, the launched EC2 instance will be EBS-optimized.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enable_<wbr>monitoring</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables/disables detailed monitoring. This is enabled by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ephemeral_<wbr>block_<wbr>devices</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationephemeralblockdevice">List[launch_<wbr>configuration_<wbr>ephemeral_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize Ephemeral (also known as
&#34;Instance Store&#34;) volumes on the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iam_<wbr>instance_<wbr>profile</td>
            <td class="align-top">
                
                <code>Dict[Any, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name attribute of the IAM instance profile to associate
with launched instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">image_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The EC2 image ID to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The size of instance to launch.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">key_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The key name that should be used for the instance.
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
The name of the launch configuration. If you leave
this blank, this provider will auto-generate a unique name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Creates a unique name beginning with the specified
prefix. Conflicts with `name`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">placement_<wbr>tenancy</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The tenancy of the instance. Valid values are
`&#34;default&#34;` or `&#34;dedicated&#34;`, see [AWS&#39;s Create Launch Configuration](http://docs.aws.amazon.com/AutoScaling/latest/APIReference/API_CreateLaunchConfiguration.html)
for more details
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">root_<wbr>block_<wbr>device</td>
            <td class="align-top">
                
                <code><a href="#launchconfigurationrootblockdevice">Dict[launch_<wbr>configuration_<wbr>root_<wbr>block_<wbr>device]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Customize details about the root block
device of the instance. See Block Devices below for details.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of associated security group IDS.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">spot_<wbr>price</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum price to use for reserving spot instances.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The user data to provide when launching the instance. Do not pass gzip-compressed data via this argument; see `user_data_base64` instead.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">user_<wbr>data_<wbr>base64</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Can be used instead of `user_data` to pass base64-encoded binary data directly. Use this instead of `user_data` whenever the value is not a valid UTF-8 string. For example, gzip-encoded user data must be base64-encoded and passed via this argument to avoid corruption.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of a ClassicLink-enabled VPC. Only applies to EC2-Classic instances. (eg. `vpc-2730681a`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">vpc_<wbr>classic_<wbr>link_<wbr>security_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IDs of one or more security groups for the specified ClassicLink-enabled VPC (eg. `sg-46ae3d11`).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### LaunchConfigurationEbsBlockDevice
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchConfigurationEbsBlockDevice">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchConfigurationEbsBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationEbsBlockDeviceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationEbsBlockDeviceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationEbsBlockDeviceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationEbsBlockDevice.html">output</a> API doc for this type.
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
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
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
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">No<wbr>Device</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
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
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
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
            <td class="align-top">Encrypted</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">No<wbr>Device</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
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
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
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
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">no<wbr>Device</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
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
            <td class="align-top">delete_<wbr>on_<wbr>termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
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
            <td class="align-top">encrypted</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">no_<wbr>device</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">snapshot_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### LaunchConfigurationEphemeralBlockDevice
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchConfigurationEphemeralBlockDevice">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchConfigurationEphemeralBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationEphemeralBlockDeviceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationEphemeralBlockDeviceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationEphemeralBlockDeviceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationEphemeralBlockDevice.html">output</a> API doc for this type.
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





#### LaunchConfigurationRootBlockDevice
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#LaunchConfigurationRootBlockDevice">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#LaunchConfigurationRootBlockDevice">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationRootBlockDeviceArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/ec2?tab=doc#LaunchConfigurationRootBlockDeviceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationRootBlockDeviceArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.LaunchConfigurationRootBlockDevice.html">output</a> API doc for this type.
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
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
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
            <td class="align-top">Delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Iops</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Size</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Volume<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
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
            <td class="align-top">delete<wbr>On<wbr>Termination</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Size</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
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
            <td class="align-top">delete_<wbr>on_<wbr>termination</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">iops</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>size</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">volume_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







