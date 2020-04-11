
---
title: "Ocean"
block_external_search_index: true
---



Provides a Spotinst Ocean AWS resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as spotinst from "@pulumi/spotinst";

const example = new spotinst.aws.Ocean("example", {
    associatePublicIpAddress: true,
    // --- AUTOSCALER -----------------
    autoscaler: {
        autoHeadroomPercentage: 50,
        autoscaleCooldown: 300,
        autoscaleDown: {
            evaluationPeriods: 300,
        },
        autoscaleHeadroom: {
            cpuPerUnit: 1024,
            gpuPerUnit: 1,
            memoryPerUnit: 512,
            numOfUnits: 2,
        },
        autoscaleIsAutoConfig: false,
        autoscaleIsEnabled: false,
        resourceLimits: {
            maxMemoryGib: 20,
            maxVcpu: 1024,
        },
    },
    controllerId: "fakeClusterId",
    desiredCapacity: 2,
    drainingTimeout: 120,
    // --- STRATEGY --------------------
    fallbackToOndemand: true,
    gracePeriod: 600,
    iamInstanceProfile: "iam-profile",
    // --- LAUNCH CONFIGURATION --------------
    imageId: "ami-123456",
    keyName: "fake key",
    loadBalancers: [
        {
            arn: "arn:aws:elasticloadbalancing:us-west-2:fake-arn",
            type: "TARGET_GROUP",
        },
        {
            name: "AntonK",
            type: "CLASSIC",
        },
    ],
    maxSize: 2,
    minSize: 1,
    region: "us-west-2",
    rootVolumeSize: 20,
    securityGroups: ["sg-987654321"],
    subnetIds: ["subnet-123456789"],
    userData: "echo hello world",
    utilizeReservedInstances: false,
    whitelists: [
        "t1.micro",
        "m1.small",
    ],
});
```

## Update Policy

* `update_policy` - (Optional)
    * `should_roll` - (Required) Enables the roll.
    * `roll_config` - (Required) While used, you can control whether the group should perform a deployment after an update to the configuration.
        * `batch_size_percentage` - (Required) Sets the percentage of the instances to deploy in each batch.

```typescript
import * as pulumi from "@pulumi/pulumi";
```

<a id="scheduled-task"></a>
## scheduled task

* `scheduled_task` - (Optional) Set scheduling object.
    * `shutdown_hours` - (Optional) Set shutdown hours for cluster object.
        * `is_enabled` - (Optional)  Flag to enable / disable the shutdown hours.
                                     Example: True
        * `time_windows` - (Required) Set time windows for shutdown hours. specify a list of 'timeWindows' with at least one time window Each string is in the format of - ddd:hh:mm-ddd:hh:mm ddd = day of week = Sun | Mon | Tue | Wed | Thu | Fri | Sat hh = hour 24 = 0 -23 mm = minute = 0 - 59. Time windows should not overlap. required on cluster.scheduling.isEnabled = True. API Times are in UTC
                                      Example: Fri:15:30-Wed:14:30
    * `tasks` - (Optional) The scheduling tasks for the cluster.
        * `is_enabled` - (Required)  Describes whether the task is enabled. When true the task should run when false it should not run. Required for cluster.scheduling.tasks object.
        * `cron_expression` - (Required) A valid cron expression. For example : " * * * * * ".The cron is running in UTC time zone and is in Unix cron format Cron Expression Validator Script. Only one of ‘frequency’ or ‘cronExpression’ should be used at a time. Required for cluster.scheduling.tasks object
                                         Example: 0 1 * * *
        * `task_type` - (Required) Valid values: "clusterRoll". Required for cluster.scheduling.tasks object
                                   Example: clusterRoll
             
```typescript
import * as pulumi from "@pulumi/pulumi";
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-spotinst/blob/master/website/docs/r/ocean_aws.html.markdown.



## Create a Ocean Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/aws/#Ocean">Ocean</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/aws/#OceanArgs">OceanArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Ocean</span><span class="p">(resource_name, opts=None, </span>associate_public_ip_address=None<span class="p">, </span>autoscaler=None<span class="p">, </span>blacklists=None<span class="p">, </span>controller_id=None<span class="p">, </span>desired_capacity=None<span class="p">, </span>draining_timeout=None<span class="p">, </span>ebs_optimized=None<span class="p">, </span>fallback_to_ondemand=None<span class="p">, </span>grace_period=None<span class="p">, </span>iam_instance_profile=None<span class="p">, </span>image_id=None<span class="p">, </span>key_name=None<span class="p">, </span>load_balancers=None<span class="p">, </span>max_size=None<span class="p">, </span>min_size=None<span class="p">, </span>monitoring=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>root_volume_size=None<span class="p">, </span>scheduled_tasks=None<span class="p">, </span>security_groups=None<span class="p">, </span>spot_percentage=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>update_policy=None<span class="p">, </span>user_data=None<span class="p">, </span>utilize_reserved_instances=None<span class="p">, </span>whitelists=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewOcean<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanArgs">OceanArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#Ocean">Ocean</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Aws.Ocean.html">Ocean</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Aws.OceanArgs.html">OceanArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Ocean<wbr>Autoscaler<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">List&lt;Ocean<wbr>Load<wbr>Balancer<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">List&lt;Ocean<wbr>Scheduled<wbr>Task<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">List&lt;Ocean<wbr>Tag<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Ocean<wbr>Update<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">*Ocean<wbr>Autoscaler</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">[]Ocean<wbr>Load<wbr>Balancer</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">[]Ocean<wbr>Scheduled<wbr>Task</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">[]Ocean<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">*Ocean<wbr>Update<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Ocean<wbr>Autoscaler?</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">Ocean<wbr>Load<wbr>Balancer[]?</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">Ocean<wbr>Scheduled<wbr>Task[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">Ocean<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Ocean<wbr>Update<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>associate_<wbr>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Dict[Ocean<wbr>Autoscaler]</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>draining_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ebs_<wbr>optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback_<wbr>to_<wbr>ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grace_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iam_<wbr>instance_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load_<wbr>balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">List[Ocean<wbr>Load<wbr>Balancer]</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root_<wbr>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled_<wbr>tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">List[Ocean<wbr>Scheduled<wbr>Task]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot_<wbr>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">List[Ocean<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Dict[Ocean<wbr>Update<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>utilize_<wbr>reserved_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Ocean Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Ocean<wbr>Autoscaler?</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">List&lt;Ocean<wbr>Load<wbr>Balancer&gt;?</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">List&lt;Ocean<wbr>Scheduled<wbr>Task&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">List&lt;Ocean<wbr>Tag&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Ocean<wbr>Update<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">*Ocean<wbr>Autoscaler</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">[]Ocean<wbr>Load<wbr>Balancer</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">[]Ocean<wbr>Scheduled<wbr>Task</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">[]Ocean<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">*Ocean<wbr>Update<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Ocean<wbr>Autoscaler?</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">Ocean<wbr>Load<wbr>Balancer[]?</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">Ocean<wbr>Scheduled<wbr>Task[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">Ocean<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Ocean<wbr>Update<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>associate_<wbr>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Dict[Ocean<wbr>Autoscaler]</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>controller_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>desired_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>draining_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ebs_<wbr>optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>fallback_<wbr>to_<wbr>ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>grace_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>iam_<wbr>instance_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>load_<wbr>balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">List[Ocean<wbr>Load<wbr>Balancer]</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>min_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>root_<wbr>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduled_<wbr>tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">List[Ocean<wbr>Scheduled<wbr>Task]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>spot_<wbr>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">List[Ocean<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>update_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Dict[Ocean<wbr>Update<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>user_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>utilize_<wbr>reserved_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Ocean Resource

Get an existing Ocean resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/aws/#OceanState">OceanState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/spotinst/aws/#Ocean">Ocean</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>associate_public_ip_address=None<span class="p">, </span>autoscaler=None<span class="p">, </span>blacklists=None<span class="p">, </span>controller_id=None<span class="p">, </span>desired_capacity=None<span class="p">, </span>draining_timeout=None<span class="p">, </span>ebs_optimized=None<span class="p">, </span>fallback_to_ondemand=None<span class="p">, </span>grace_period=None<span class="p">, </span>iam_instance_profile=None<span class="p">, </span>image_id=None<span class="p">, </span>key_name=None<span class="p">, </span>load_balancers=None<span class="p">, </span>max_size=None<span class="p">, </span>min_size=None<span class="p">, </span>monitoring=None<span class="p">, </span>name=None<span class="p">, </span>region=None<span class="p">, </span>root_volume_size=None<span class="p">, </span>scheduled_tasks=None<span class="p">, </span>security_groups=None<span class="p">, </span>spot_percentage=None<span class="p">, </span>subnet_ids=None<span class="p">, </span>tags=None<span class="p">, </span>update_policy=None<span class="p">, </span>user_data=None<span class="p">, </span>utilize_reserved_instances=None<span class="p">, </span>whitelists=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetOcean<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanState">OceanState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#Ocean">Ocean</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Aws.Ocean.html">Ocean</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Spotinst/Pulumi.Spotinst.Aws.OceanState.html">OceanState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Ocean<wbr>Autoscaler<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">List&lt;Ocean<wbr>Load<wbr>Balancer<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">List&lt;Ocean<wbr>Scheduled<wbr>Task<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">List&lt;Ocean<wbr>Tag<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Ocean<wbr>Update<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">*Ocean<wbr>Autoscaler</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">[]Ocean<wbr>Load<wbr>Balancer</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">[]Ocean<wbr>Scheduled<wbr>Task</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">[]Ocean<wbr>Tag</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">*Ocean<wbr>Update<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>associate<wbr>Public<wbr>Ip<wbr>Address</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Ocean<wbr>Autoscaler?</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired<wbr>Capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>draining<wbr>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ebs<wbr>Optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback<wbr>To<wbr>Ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grace<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iam<wbr>Instance<wbr>Profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load<wbr>Balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">Ocean<wbr>Load<wbr>Balancer[]?</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root<wbr>Volume<wbr>Size</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled<wbr>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">Ocean<wbr>Scheduled<wbr>Task[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security<wbr>Groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet<wbr>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">Ocean<wbr>Tag[]?</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Ocean<wbr>Update<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>utilize<wbr>Reserved<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>associate_<wbr>public_<wbr>ip_<wbr>address</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Configure public IP address allocation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscaler</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscaler">Dict[Ocean<wbr>Autoscaler]</a></span>
    </dt>
    <dd>{{% md %}}Describes the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>blacklists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Instance types not allowed in the Ocean cluster. Cannot be configured if `whitelist` is configured.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>controller_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ocean cluster identifier. Example: `ocean.k8s`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>desired_<wbr>capacity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of instances to launch and maintain in the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>draining_<wbr>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time in seconds, the instance is allowed to run while detached from the ELB. This is to allow the instance time to be drained from incoming TCP connections before terminating it, during a scale down operation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ebs_<wbr>optimized</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable EBS optimized for cluster. Flag will enable optimized capacity for high bandwidth connectivity to the EB service for non EBS optimized instance types. For instances that are EBS optimized this flag will be ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>fallback_<wbr>to_<wbr>ondemand</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If not Spot instance markets are available, enable Ocean to launch On-Demand instances instead.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>grace_<wbr>period</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The amount of time, in seconds, after the instance has launched to start checking its health.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>iam_<wbr>instance_<wbr>profile</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The instance profile iam role.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>image_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}ID of the image used to launch the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The key pair to attach the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>load_<wbr>balancers</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanloadbalancer">List[Ocean<wbr>Load<wbr>Balancer]</a></span>
    </dt>
    <dd>{{% md %}}- Array of load balancer objects to add to ocean cluster
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The upper limit of instances the cluster can scale up to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The lower limit of instances the cluster can scale down to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>monitoring</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable detailed monitoring for cluster. Flag will enable Cloud Watch detailed detailed monitoring (one minute increments). Note: there are additional hourly costs for this service based on the region used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The region the cluster will run in.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>root_<wbr>volume_<wbr>size</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The size (in Gb) to allocate for the root volume. Minimum `20`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled_<wbr>tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtask">List[Ocean<wbr>Scheduled<wbr>Task]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>security_<wbr>groups</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}One or more security group ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>spot_<wbr>percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subnet_<wbr>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A comma-separated list of subnet identifiers for the Ocean cluster. Subnet IDs should be configured with auto assign public ip.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceantag">List[Ocean<wbr>Tag]</a></span>
    </dt>
    <dd>{{% md %}}Optionally adds tags to instances launched in an Ocean cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>update_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicy">Dict[Ocean<wbr>Update<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Base64-encoded MIME user data to make available to the instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>utilize_<wbr>reserved_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If Reserved instances exist, OCean will utilize them before launching Spot instances.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>whitelists</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Instance types allowed in the Ocean cluster. Cannot be configured if `blacklist` is configured.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Ocean<wbr>Autoscaler</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanAutoscaler">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanAutoscaler">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Headroom<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Set the auto headroom percentage (a number in the range [0, 200]) which controls the percentage of headroom from the cluster. Relevant only when `isAutoConfig` toggled on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Cooldown period between scaling actions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Down</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaledown">Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Down<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Auto Scaling scale down operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Headroom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaleheadroom">Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Headroom<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Is<wbr>Auto<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Automatically configure and optimize headroom resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Enable the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerresourcelimits">Ocean<wbr>Autoscaler<wbr>Resource<wbr>Limits<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Optionally set upper and lower bounds on the resource usage of the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Headroom<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Set the auto headroom percentage (a number in the range [0, 200]) which controls the percentage of headroom from the cluster. Relevant only when `isAutoConfig` toggled on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Cooldown period between scaling actions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Down</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaledown">*Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Down</a></span>
    </dt>
    <dd>{{% md %}}Auto Scaling scale down operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Headroom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaleheadroom">*Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Headroom</a></span>
    </dt>
    <dd>{{% md %}}Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Is<wbr>Auto<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Automatically configure and optimize headroom resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Autoscale<wbr>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Enable the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerresourcelimits">*Ocean<wbr>Autoscaler<wbr>Resource<wbr>Limits</a></span>
    </dt>
    <dd>{{% md %}}Optionally set upper and lower bounds on the resource usage of the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Headroom<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Set the auto headroom percentage (a number in the range [0, 200]) which controls the percentage of headroom from the cluster. Relevant only when `isAutoConfig` toggled on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Cooldown period between scaling actions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Down</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaledown">Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Down?</a></span>
    </dt>
    <dd>{{% md %}}Auto Scaling scale down operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Headroom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaleheadroom">Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Headroom?</a></span>
    </dt>
    <dd>{{% md %}}Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Is<wbr>Auto<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Automatically configure and optimize headroom resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Enable the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerresourcelimits">Ocean<wbr>Autoscaler<wbr>Resource<wbr>Limits?</a></span>
    </dt>
    <dd>{{% md %}}Optionally set upper and lower bounds on the resource usage of the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Headroom<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Set the auto headroom percentage (a number in the range [0, 200]) which controls the percentage of headroom from the cluster. Relevant only when `isAutoConfig` toggled on.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Cooldown</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Cooldown period between scaling actions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Down</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaledown">Dict[Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Down]</a></span>
    </dt>
    <dd>{{% md %}}Auto Scaling scale down operations.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Headroom</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerautoscaleheadroom">Dict[Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Headroom]</a></span>
    </dt>
    <dd>{{% md %}}Spare resource capacity management enabling fast assignment of Pods without waiting for new resources to launch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Is<wbr>Auto<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Automatically configure and optimize headroom resources.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>autoscale<wbr>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Enable the Ocean Kubernetes autoscaler.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Limits</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanautoscalerresourcelimits">Dict[Ocean<wbr>Autoscaler<wbr>Resource<wbr>Limits]</a></span>
    </dt>
    <dd>{{% md %}}Optionally set upper and lower bounds on the resource usage of the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Down</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanAutoscalerAutoscaleDown">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanAutoscalerAutoscaleDown">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerAutoscaleDownArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerAutoscaleDownOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Evaluation<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of evaluation periods that should accumulate before a scale down action takes place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Scale<wbr>Down<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Would represent the maximum % to scale-down. Number between 1-100.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Evaluation<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of evaluation periods that should accumulate before a scale down action takes place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Scale<wbr>Down<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Would represent the maximum % to scale-down. Number between 1-100.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>evaluation<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of evaluation periods that should accumulate before a scale down action takes place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Scale<wbr>Down<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Would represent the maximum % to scale-down. Number between 1-100.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>evaluation<wbr>Periods</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of evaluation periods that should accumulate before a scale down action takes place.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Scale<wbr>Down<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Would represent the maximum % to scale-down. Number between 1-100.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Autoscaler<wbr>Autoscale<wbr>Headroom</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanAutoscalerAutoscaleHeadroom">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanAutoscalerAutoscaleHeadroom">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerAutoscaleHeadroomArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerAutoscaleHeadroomOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of GPUS to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Optionally configure the amount of memory (MB) to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Of<wbr>Units</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Cpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of GPUS to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Memory<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Optionally configure the amount of memory (MB) to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Of<wbr>Units</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of GPUS to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Optionally configure the amount of memory (MB) to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Of<wbr>Units</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>cpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of CPUs to allocate the headroom. CPUs are denoted in millicores, where 1000 millicores = 1 vCPU.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gpu<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optionally configure the number of GPUS to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>memory<wbr>Per<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Optionally configure the amount of memory (MB) to allocate the headroom.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Of<wbr>Units</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of units to retain as headroom, where each unit has the defined headroom CPU and memory.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Autoscaler<wbr>Resource<wbr>Limits</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanAutoscalerResourceLimits">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanAutoscalerResourceLimits">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerResourceLimitsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanAutoscalerResourceLimitsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Memory<wbr>Gib</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum memory in GiB units that can be allocated to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Vcpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The maximum cpu in vCPU units that can be allocated to the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Memory<wbr>Gib</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum memory in GiB units that can be allocated to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Vcpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The maximum cpu in vCPU units that can be allocated to the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Memory<wbr>Gib</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum memory in GiB units that can be allocated to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Vcpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum cpu in vCPU units that can be allocated to the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Memory<wbr>Gib</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum memory in GiB units that can be allocated to the cluster.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Vcpu</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum cpu in vCPU units that can be allocated to the cluster.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Load<wbr>Balancer</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanLoadBalancer">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanLoadBalancer">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanLoadBalancerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanLoadBalancerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to TARGET_GROUP
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Can be set to CLASSIC or TARGET_GROUP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to TARGET_GROUP
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Can be set to CLASSIC or TARGET_GROUP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to TARGET_GROUP
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Can be set to CLASSIC or TARGET_GROUP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if type is set to TARGET_GROUP
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required if type is set to CLASSIC
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Can be set to CLASSIC or TARGET_GROUP
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Scheduled<wbr>Task</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanScheduledTask">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanScheduledTask">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanScheduledTaskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanScheduledTaskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Shutdown<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtaskshutdownhours">Ocean<wbr>Scheduled<wbr>Task<wbr>Shutdown<wbr>Hours<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtasktask">List&lt;Ocean<wbr>Scheduled<wbr>Task<wbr>Task<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Shutdown<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtaskshutdownhours">*Ocean<wbr>Scheduled<wbr>Task<wbr>Shutdown<wbr>Hours</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtasktask">[]Ocean<wbr>Scheduled<wbr>Task<wbr>Task</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>shutdown<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtaskshutdownhours">Ocean<wbr>Scheduled<wbr>Task<wbr>Shutdown<wbr>Hours?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtasktask">Ocean<wbr>Scheduled<wbr>Task<wbr>Task[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>shutdown<wbr>Hours</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtaskshutdownhours">Dict[Ocean<wbr>Scheduled<wbr>Task<wbr>Shutdown<wbr>Hours]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tasks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanscheduledtasktask">List[Ocean<wbr>Scheduled<wbr>Task<wbr>Task]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Scheduled<wbr>Task<wbr>Shutdown<wbr>Hours</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanScheduledTaskShutdownHours">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanScheduledTaskShutdownHours">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanScheduledTaskShutdownHoursArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanScheduledTaskShutdownHoursOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Windows</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Windows</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Windows</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Windows</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Scheduled<wbr>Task<wbr>Task</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanScheduledTaskTask">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanScheduledTaskTask">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanScheduledTaskTaskArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanScheduledTaskTaskOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cron<wbr>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Task<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Cron<wbr>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Task<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cron<wbr>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>task<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>cron<wbr>Expression</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>is<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>task<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Tag</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanTag">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanTag">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanTagArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanTagOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tag value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>key</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The tag key.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The tag value.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Update<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanUpdatePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanUpdatePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanUpdatePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanUpdatePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Roll<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicyrollconfig">Ocean<wbr>Update<wbr>Policy<wbr>Roll<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Should<wbr>Roll</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Roll<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicyrollconfig">*Ocean<wbr>Update<wbr>Policy<wbr>Roll<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Should<wbr>Roll</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>roll<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicyrollconfig">Ocean<wbr>Update<wbr>Policy<wbr>Roll<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>should<wbr>Roll</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>roll<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#oceanupdatepolicyrollconfig">Dict[Ocean<wbr>Update<wbr>Policy<wbr>Roll<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>should<wbr>Roll</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Ocean<wbr>Update<wbr>Policy<wbr>Roll<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/input/#OceanUpdatePolicyRollConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/spotinst/types/output/#OceanUpdatePolicyRollConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanUpdatePolicyRollConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-spotinst/sdk/go/spotinst/aws?tab=doc#OceanUpdatePolicyRollConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Batch<wbr>Size<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Batch<wbr>Size<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>batch<wbr>Size<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>batch<wbr>Size<wbr>Percentage</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-spotinst">https://github.com/pulumi/pulumi-spotinst</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

