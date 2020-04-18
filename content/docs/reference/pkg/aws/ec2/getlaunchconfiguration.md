
---
title: "GetLaunchConfiguration"
block_external_search_index: true
---



Provides information about a Launch Configuration.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const ubuntu = pulumi.output(aws.ec2.getLaunchConfiguration({
    name: "test-launch-config",
}, { async: true }));
```

{{% /example %}}
{{% /examples %}}





## Using GetLaunchConfiguration

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getLaunchConfiguration<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetLaunchConfigurationArgs">GetLaunchConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/ec2/#GetLaunchConfigurationResult">GetLaunchConfigurationResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_launch_configuration(</span>name=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupLaunchConfiguration<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2?tab=doc#LookupLaunchConfigurationArgs">LookupLaunchConfigurationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2?tab=doc#LookupLaunchConfigurationResult">LookupLaunchConfigurationResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetLaunchConfiguration </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationResult.html">GetLaunchConfigurationResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Ec2.GetLaunchConfigurationArgs.html">GetLaunchConfigurationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The name of the launch configuration.
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
    <dd>{{% md %}}The name of the launch configuration.
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
    <dd>{{% md %}}The name of the launch configuration.
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
    <dd>{{% md %}}The name of the launch configuration.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetLaunchConfiguration Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether a Public IP address is associated with the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationebsblockdevice">List&lt;Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device&gt;</a></span>
    </dt>
    <dd>{{% md %}}The EBS Block Devices attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether Detailed Monitoring is Enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ephemeral<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationephemeralblockdevice">List&lt;Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device&gt;</a></span>
    </dt>
    <dd>{{% md %}}The Ephemeral volumes on the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to associate with launched instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The EC2 Image ID of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Instance Type of the instance to launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Key Name that should be used for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Placement<wbr>Tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenancy of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Root<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationrootblockdevice">List&lt;Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device&gt;</a></span>
    </dt>
    <dd>{{% md %}}The Root Block Device of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of associated Security Group IDS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spot<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Price to use for reserving Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The User Data of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Classic<wbr>Link<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of a ClassicLink-enabled VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether a Public IP address is associated with the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationebsblockdevice">[]Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device</a></span>
    </dt>
    <dd>{{% md %}}The EBS Block Devices attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether Detailed Monitoring is Enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ephemeral<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationephemeralblockdevice">[]Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device</a></span>
    </dt>
    <dd>{{% md %}}The Ephemeral volumes on the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to associate with launched instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The EC2 Image ID of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Instance Type of the instance to launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Key Name that should be used for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Placement<wbr>Tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenancy of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Root<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationrootblockdevice">[]Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</a></span>
    </dt>
    <dd>{{% md %}}The Root Block Device of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of associated Security Group IDS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spot<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Price to use for reserving Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The User Data of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Classic<wbr>Link<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of a ClassicLink-enabled VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether a Public IP address is associated with the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationebsblockdevice">Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device[]</a></span>
    </dt>
    <dd>{{% md %}}The EBS Block Devices attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether Detailed Monitoring is Enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ephemeral<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationephemeralblockdevice">Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device[]</a></span>
    </dt>
    <dd>{{% md %}}The Ephemeral volumes on the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to associate with launched instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The EC2 Image ID of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Instance Type of the instance to launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Key Name that should be used for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>placement<wbr>Tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Tenancy of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>root<wbr>Block<wbr>Devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationrootblockdevice">Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device[]</a></span>
    </dt>
    <dd>{{% md %}}The Root Block Device of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of associated Security Group IDS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spot<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Price to use for reserving Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The User Data of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Classic<wbr>Link<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of a ClassicLink-enabled VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Classic<wbr>Link<wbr>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Amazon Resource Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>associate_<wbr>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether a Public IP address is associated with the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs_<wbr>block_<wbr>devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationebsblockdevice">List[Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device]</a></span>
    </dt>
    <dd>{{% md %}}The EBS Block Devices attached to the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs_<wbr>optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the launched EC2 instance will be EBS-optimized.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether Detailed Monitoring is Enabled.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ephemeral_<wbr>block_<wbr>devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationephemeralblockdevice">List[Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device]</a></span>
    </dt>
    <dd>{{% md %}}The Ephemeral volumes on the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iam_<wbr>instance_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The IAM Instance Profile to associate with launched instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The EC2 Image ID of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>instance_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Instance Type of the instance to launch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Key Name that should be used for the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Name of the launch configuration.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>placement_<wbr>tenancy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Tenancy of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>root_<wbr>block_<wbr>devices</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getlaunchconfigurationrootblockdevice">List[Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device]</a></span>
    </dt>
    <dd>{{% md %}}The Root Block Device of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of associated Security Group IDS.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spot_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Price to use for reserving Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The User Data of the instance.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>classic_<wbr>link_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of a ClassicLink-enabled VPC.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>classic_<wbr>link_<wbr>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}The IDs of one or more Security Groups for the specified ClassicLink-enabled VPC.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Launch<wbr>Configuration<wbr>Ebs<wbr>Block<wbr>Device</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchConfigurationEbsBlockDevice">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2?tab=doc#GetLaunchConfigurationEbsBlockDevice">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Snapshot ID of the mount.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Snapshot ID of the mount.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snapshot<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Snapshot ID of the mount.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>snapshot_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Snapshot ID of the mount.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Configuration<wbr>Ephemeral<wbr>Block<wbr>Device</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchConfigurationEphemeralBlockDevice">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2?tab=doc#GetLaunchConfigurationEphemeralBlockDevice">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Name of the device.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Name of the device.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>device<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Name of the device.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>device_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Name of the device.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>virtual<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Virtual Name of the device.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Get<wbr>Launch<wbr>Configuration<wbr>Root<wbr>Block<wbr>Device</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetLaunchConfigurationRootBlockDevice">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/v2/go/aws/ec2?tab=doc#GetLaunchConfigurationRootBlockDevice">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>delete<wbr>On<wbr>Termination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the EBS Volume will be deleted on instance termination.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>encrypted</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether the volume is Encrypted.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>iops</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The provisioned IOPs of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The Size of the volume.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>volume<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The Type of the volume.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







