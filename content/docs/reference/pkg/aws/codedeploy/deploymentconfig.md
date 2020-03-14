
---
title: "DeploymentConfig"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a CodeDeploy deployment config for an application

## Example Usage

### Server Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const fooDeploymentConfig = new aws.codedeploy.DeploymentConfig("foo", {
    deploymentConfigName: "test-deployment-config",
    minimumHealthyHosts: {
        type: "HOST_COUNT",
        value: 2,
    },
});
const fooDeploymentGroup = new aws.codedeploy.DeploymentGroup("foo", {
    alarmConfiguration: {
        alarms: ["my-alarm-name"],
        enabled: true,
    },
    appName: aws_codedeploy_app_foo_app.name,
    autoRollbackConfiguration: {
        enabled: true,
        events: ["DEPLOYMENT_FAILURE"],
    },
    deploymentConfigName: fooDeploymentConfig.id,
    deploymentGroupName: "bar",
    ec2TagFilters: [{
        key: "filterkey",
        type: "KEY_AND_VALUE",
        value: "filtervalue",
    }],
    serviceRoleArn: aws_iam_role_foo_role.arn,
    triggerConfigurations: [{
        triggerEvents: ["DeploymentFailure"],
        triggerName: "foo-trigger",
        triggerTargetArn: "foo-topic-arn",
    }],
});
```

### Lambda Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const fooDeploymentConfig = new aws.codedeploy.DeploymentConfig("foo", {
    computePlatform: "Lambda",
    deploymentConfigName: "test-deployment-config",
    trafficRoutingConfig: {
        timeBasedLinear: {
            interval: 10,
            percentage: 10,
        },
        type: "TimeBasedLinear",
    },
});
const fooDeploymentGroup = new aws.codedeploy.DeploymentGroup("foo", {
    alarmConfiguration: {
        alarms: ["my-alarm-name"],
        enabled: true,
    },
    appName: aws_codedeploy_app_foo_app.name,
    autoRollbackConfiguration: {
        enabled: true,
        events: ["DEPLOYMENT_STOP_ON_ALARM"],
    },
    deploymentConfigName: fooDeploymentConfig.id,
    deploymentGroupName: "bar",
    serviceRoleArn: aws_iam_role_foo_role.arn,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/codedeploy_deployment_config.html.markdown.



## Create a DeploymentConfig Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentConfig">DeploymentConfig</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentConfigArgs">DeploymentConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DeploymentConfig</span><span class="p">(resource_name, opts=None, </span>compute_platform=None<span class="p">, </span>deployment_config_name=None<span class="p">, </span>minimum_healthy_hosts=None<span class="p">, </span>traffic_routing_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDeploymentConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigArgs">DeploymentConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfig">DeploymentConfig</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfig.html">DeploymentConfig</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigArgs.html">DeploymentConfigArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a DeploymentConfig resource with the given unique name, arguments, and options.

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
            <td class="align-top">Compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">Compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">compute_<wbr>platform</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>healthy_<wbr>hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">dict{deployment_<wbr>config_<wbr>minimum_<wbr>healthy_<wbr>hosts}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">traffic_<wbr>routing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">dict{deployment_<wbr>config_<wbr>traffic_<wbr>routing_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## DeploymentConfig Output Properties

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
            <td class="align-top">Compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts?</a></code>
            </td>
            <td class="align-top">{{% md %}} A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">Compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts</a></code>
            </td>
            <td class="align-top">{{% md %}} A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts?</a></code>
            </td>
            <td class="align-top">{{% md %}} A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">compute_<wbr>platform</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>healthy_<wbr>hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">dict{deployment_<wbr>config_<wbr>minimum_<wbr>healthy_<wbr>hosts}</a></code>
            </td>
            <td class="align-top">{{% md %}} A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">traffic_<wbr>routing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">dict{deployment_<wbr>config_<wbr>traffic_<wbr>routing_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} A traffic_routing_config block. Traffic Routing Config is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing DeploymentConfig Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentConfigState">DeploymentConfigState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/codedeploy/#DeploymentConfig">DeploymentConfig</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>compute_platform=None<span class="p">, </span>deployment_config_id=None<span class="p">, </span>deployment_config_name=None<span class="p">, </span>minimum_healthy_hosts=None<span class="p">, </span>traffic_routing_config=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDeploymentConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigState">DeploymentConfigState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfig">DeploymentConfig</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfig.html">DeploymentConfig</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigState.html">DeploymentConfigState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing DeploymentConfig resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">Compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">compute<wbr>Platform</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Config<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum<wbr>Healthy<wbr>Hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">codedeploy.<wbr>Deployment<wbr>Config<wbr>Minimum<wbr>Healthy<wbr>Hosts?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">traffic<wbr>Routing<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
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
            <td class="align-top">compute_<wbr>platform</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The compute platform can be `Server`, `Lambda`, or `ECS`. Default is `Server`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The AWS Assigned deployment config id
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>config_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the deployment config.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">minimum_<wbr>healthy_<wbr>hosts</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigminimumhealthyhosts">dict{deployment_<wbr>config_<wbr>minimum_<wbr>healthy_<wbr>hosts}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A minimum_healthy_hosts block. Required for `Server` compute platform. Minimum Healthy Hosts are documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">traffic_<wbr>routing_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfig">dict{deployment_<wbr>config_<wbr>traffic_<wbr>routing_<wbr>config}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A traffic_routing_config block. Traffic Routing Config is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DeploymentConfigMinimumHealthyHosts
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentConfigMinimumHealthyHosts">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentConfigMinimumHealthyHosts">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigMinimumHealthyHostsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigMinimumHealthyHostsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigMinimumHealthyHostsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigMinimumHealthyHosts.html">output</a> API doc for this type.
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
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>int?</code>
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
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>*int</code>
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
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>number?</code>
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
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentConfigTrafficRoutingConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentConfigTrafficRoutingConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentConfigTrafficRoutingConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigTrafficRoutingConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigTrafficRoutingConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigTrafficRoutingConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigTrafficRoutingConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Time<wbr>Based<wbr>Canary</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedcanary">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Time<wbr>Based<wbr>Canary<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Based<wbr>Linear</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedlinear">Pulumi.<wbr>Aws.<wbr>Codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Time<wbr>Based<wbr>Linear<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
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
            <td class="align-top">Time<wbr>Based<wbr>Canary</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedcanary">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Time<wbr>Based<wbr>Canary</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Based<wbr>Linear</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedlinear">*codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Time<wbr>Based<wbr>Linear</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
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
            <td class="align-top">time<wbr>Based<wbr>Canary</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedcanary">codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Time<wbr>Based<wbr>Canary?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time<wbr>Based<wbr>Linear</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedlinear">codedeploy.<wbr>Deployment<wbr>Config<wbr>Traffic<wbr>Routing<wbr>Config<wbr>Time<wbr>Based<wbr>Linear?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
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
            <td class="align-top">time_<wbr>based_<wbr>canary</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedcanary">dict{deployment_<wbr>config_<wbr>traffic_<wbr>routing_<wbr>config_<wbr>time_<wbr>based_<wbr>canary}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time_<wbr>based_<wbr>linear</td>
            <td class="align-top">
                
                <code><a href="#deploymentconfigtrafficroutingconfigtimebasedlinear">dict{deployment_<wbr>config_<wbr>traffic_<wbr>routing_<wbr>config_<wbr>time_<wbr>based_<wbr>linear}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
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





#### DeploymentConfigTrafficRoutingConfigTimeBasedCanary
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentConfigTrafficRoutingConfigTimeBasedCanary">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentConfigTrafficRoutingConfigTimeBasedCanary">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigTrafficRoutingConfigTimeBasedCanaryOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigTrafficRoutingConfigTimeBasedCanaryArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigTrafficRoutingConfigTimeBasedCanary.html">output</a> API doc for this type.
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
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Percentage</td>
            <td class="align-top">
                
                <code>int?</code>
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
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Percentage</td>
            <td class="align-top">
                
                <code>*int</code>
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
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">percentage</td>
            <td class="align-top">
                
                <code>number?</code>
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
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">percentage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DeploymentConfigTrafficRoutingConfigTimeBasedLinear
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DeploymentConfigTrafficRoutingConfigTimeBasedLinear">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DeploymentConfigTrafficRoutingConfigTimeBasedLinear">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/codedeploy?tab=doc#DeploymentConfigTrafficRoutingConfigTimeBasedLinearOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigTrafficRoutingConfigTimeBasedLinearArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Codedeploy.DeploymentConfigTrafficRoutingConfigTimeBasedLinear.html">output</a> API doc for this type.
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
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Percentage</td>
            <td class="align-top">
                
                <code>int?</code>
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
            <td class="align-top">Interval</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Percentage</td>
            <td class="align-top">
                
                <code>*int</code>
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
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">percentage</td>
            <td class="align-top">
                
                <code>number?</code>
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
            <td class="align-top">interval</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">percentage</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







