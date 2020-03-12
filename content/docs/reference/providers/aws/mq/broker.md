
---
title: "Broker"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides an MQ Broker Resource. This resources also manages users for the broker.

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

Changes to an MQ Broker can occur when you change a
parameter, such as `configuration` or `user`, and are reflected in the next maintenance
window. Because of this, this provider may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

> **Note:** using `apply_immediately` can result in a
brief downtime as the broker reboots.

> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.mq.Broker("example", {
    brokerName: "example",
    configuration: {
        id: aws_mq_configuration_test.id,
        revision: aws_mq_configuration_test.latestRevision,
    },
    engineType: "ActiveMQ",
    engineVersion: "5.15.0",
    hostInstanceType: "mq.t2.micro",
    securityGroups: [aws_security_group_test.id],
    users: [{
        password: "MindTheGap",
        username: "ExampleUser",
    }],
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/mq_broker.html.markdown.



## Create a Broker Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/mq/#Broker">Broker</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/mq/#BrokerArgs">BrokerArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def Broker(resource_name, id, opts=None, apply_<wbr>immediately=None, auto_<wbr>minor_<wbr>version_<wbr>upgrade=None, broker_<wbr>name=None, configuration=None, deployment_<wbr>mode=None, encryption_<wbr>options=None, engine_<wbr>type=None, engine_<wbr>version=None, host_<wbr>instance_<wbr>type=None, logs=None, maintenance_<wbr>window_<wbr>start_<wbr>time=None, publicly_<wbr>accessible=None, security_<wbr>groups=None, subnet_<wbr>ids=None, tags=None, users=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewBroker<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerArgs">BrokerArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#Broker">Broker</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.Broker.html">Broker</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerArgs.html">BrokerArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Broker resource with the given unique name, arguments, and options.

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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Encryption<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Logs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">List&lt;Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>User<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">*mq.<wbr>Broker<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">*mq.<wbr>Broker<wbr>Encryption<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">*mq.<wbr>Broker<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">*mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">[]mq.<wbr>Broker<wbr>User</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">mq.<wbr>Broker<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">mq.<wbr>Broker<wbr>Encryption<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">mq.<wbr>Broker<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">mq.<wbr>Broker<wbr>User[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>minor_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">dict{broker_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">dict{broker_<wbr>encryption_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">dict{broker_<wbr>logs}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window_<wbr>start_<wbr>time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">dict{broker_<wbr>maintenance_<wbr>window_<wbr>start_<wbr>time}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly_<wbr>accessible</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">list[broker_<wbr>user]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The list of all ActiveMQ usernames for the specified broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Broker Output Properties

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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Encryption<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">List&lt;Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Instance&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">List&lt;Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>User&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">mq.<wbr>Broker<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">*mq.<wbr>Broker<wbr>Encryption<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">[]mq.<wbr>Broker<wbr>Instance</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">*mq.<wbr>Broker<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">[]mq.<wbr>Broker<wbr>User</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">mq.<wbr>Broker<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">mq.<wbr>Broker<wbr>Encryption<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">mq.<wbr>Broker<wbr>Instance[]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">mq.<wbr>Broker<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">mq.<wbr>Broker<wbr>User[]</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>minor_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">dict{broker_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">dict{broker_<wbr>encryption_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">list[broker_<wbr>instance]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">dict{broker_<wbr>logs}</a></code>
            </td>
            <td class="align-top">{{% md %}} Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window_<wbr>start_<wbr>time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">dict{broker_<wbr>maintenance_<wbr>window_<wbr>start_<wbr>time}</a></code>
            </td>
            <td class="align-top">{{% md %}} Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly_<wbr>accessible</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">list[broker_<wbr>user]</a></code>
            </td>
            <td class="align-top">{{% md %}} The list of all ActiveMQ usernames for the specified broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Broker Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BrokerState, opts?: pulumi.CustomResourceOptions): Broker;
```

```python
def get(resource_name, id, opts=None, apply_<wbr>immediately=None, arn=None, auto_<wbr>minor_<wbr>version_<wbr>upgrade=None, broker_<wbr>name=None, configuration=None, deployment_<wbr>mode=None, encryption_<wbr>options=None, engine_<wbr>type=None, engine_<wbr>version=None, host_<wbr>instance_<wbr>type=None, instances=None, logs=None, maintenance_<wbr>window_<wbr>start_<wbr>time=None, publicly_<wbr>accessible=None, security_<wbr>groups=None, subnet_<wbr>ids=None, tags=None, users=None)
```

```go
func GetBroker(ctx *pulumi.Context, name string, id pulumi.IDInput, state *BrokerState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Broker Get(string name, Input<string> id, BrokerState? state = null, CustomResourceOptions? options = null);
```

Get an existing Broker resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
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
The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Configuration<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Encryption<wbr>Options<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">List&lt;Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Instance<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Logs<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
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
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">List&lt;Pulumi.<wbr>Aws.<wbr>Mq.<wbr>Broker<wbr>User<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">Apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
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
The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Broker<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">*mq.<wbr>Broker<wbr>Configuration</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">*mq.<wbr>Broker<wbr>Encryption<wbr>Options</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Engine<wbr>Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">[]mq.<wbr>Broker<wbr>Instance</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">*mq.<wbr>Broker<wbr>Logs</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">*mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
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
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">[]mq.<wbr>Broker<wbr>User</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">apply<wbr>Immediately</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
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
The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto<wbr>Minor<wbr>Version<wbr>Upgrade</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">mq.<wbr>Broker<wbr>Configuration?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption<wbr>Options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">mq.<wbr>Broker<wbr>Encryption<wbr>Options?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine<wbr>Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host<wbr>Instance<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">mq.<wbr>Broker<wbr>Instance[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">mq.<wbr>Broker<wbr>Logs?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance<wbr>Window<wbr>Start<wbr>Time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">mq.<wbr>Broker<wbr>Maintenance<wbr>Window<wbr>Start<wbr>Time?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly<wbr>Accessible</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
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
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Ids</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">mq.<wbr>Broker<wbr>User[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of all ActiveMQ usernames for the specified broker. See below.
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
            <td class="align-top">apply_<wbr>immediately</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.
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
The ARN of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">auto_<wbr>minor_<wbr>version_<wbr>upgrade</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">broker_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">configuration</td>
            <td class="align-top">
                
                <code><a href="#brokerconfiguration">dict{broker_<wbr>configuration}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">deployment_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">encryption_<wbr>options</td>
            <td class="align-top">
                
                <code><a href="#brokerencryptionoptions">dict{broker_<wbr>encryption_<wbr>options}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Configuration block containing encryption options. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">engine_<wbr>version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The version of the broker engine. See the [AmazonMQ Broker Engine docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/broker-engine.html) for supported versions.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">host_<wbr>instance_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The broker&#39;s instance type. e.g. `mq.t2.micro` or `mq.m4.large`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code><a href="#brokerinstance">list[broker_<wbr>instance]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of information about allocated brokers (both active &amp; standby).
* `instances.0.console_url` - The URL of the broker&#39;s [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.ip_address` - The IP Address of the broker.
* `instances.0.endpoints` - The broker&#39;s wire-level protocol endpoints in the following order &amp; format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt&#43;ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">logs</td>
            <td class="align-top">
                
                <code><a href="#brokerlogs">dict{broker_<wbr>logs}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Logging configuration of the broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">maintenance_<wbr>window_<wbr>start_<wbr>time</td>
            <td class="align-top">
                
                <code><a href="#brokermaintenancewindowstarttime">dict{broker_<wbr>maintenance_<wbr>window_<wbr>start_<wbr>time}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Maintenance window start time. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">publicly_<wbr>accessible</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable connections from applications outside of the VPC that hosts the broker&#39;s subnets.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security_<wbr>groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of security group IDs assigned to the broker.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>ids</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.
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
A mapping of tags to assign to the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">users</td>
            <td class="align-top">
                
                <code><a href="#brokeruser">list[broker_<wbr>user]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of all ActiveMQ usernames for the specified broker. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### BrokerConfiguration
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BrokerConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BrokerConfiguration">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerConfigurationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerConfigurationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerConfiguration.html">output</a> API doc for this type.
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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Configuration ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Revision of the Configuration.
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
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Configuration ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Revision</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Revision of the Configuration.
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Configuration ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Revision of the Configuration.
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
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The Configuration ID.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">revision</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Revision of the Configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BrokerEncryptionOptions
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BrokerEncryptionOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BrokerEncryptionOptions">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerEncryptionOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerEncryptionOptionsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerEncryptionOptionsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerEncryptionOptions.html">output</a> API doc for this type.
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
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting `use_aws_owned_key` to `false`. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Aws<wbr>Owned<wbr>Key</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to `true`. Setting to `false` without configuring `kms_key_id` will create an AWS managed Customer Master Key (CMK) aliased to `aws/mq` in your account.
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
            <td class="align-top">Kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting `use_aws_owned_key` to `false`. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Aws<wbr>Owned<wbr>Key</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to `true`. Setting to `false` without configuring `kms_key_id` will create an AWS managed Customer Master Key (CMK) aliased to `aws/mq` in your account.
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
            <td class="align-top">kms<wbr>Key<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting `use_aws_owned_key` to `false`. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Aws<wbr>Owned<wbr>Key</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to `true`. Setting to `false` without configuring `kms_key_id` will create an AWS managed Customer Master Key (CMK) aliased to `aws/mq` in your account.
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
            <td class="align-top">kms_<wbr>key_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Resource Name (ARN) of Key Management Service (KMS) Customer Master Key (CMK) to use for encryption at rest. Requires setting `use_aws_owned_key` to `false`. To perform drift detection when AWS managed CMKs or customer managed CMKs are in use, this value must be configured.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use_<wbr>aws_<wbr>owned_<wbr>key</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Boolean to enable an AWS owned Key Management Service (KMS) Customer Master Key (CMK) that is not in your account. Defaults to `true`. Setting to `false` without configuring `kms_key_id` will create an AWS managed Customer Master Key (CMK) aliased to `aws/mq` in your account.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BrokerInstance
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BrokerInstance">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerInstanceOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerInstance.html">output</a> API doc for this type.
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
            <td class="align-top">Console<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoints</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ip<wbr>Address</td>
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
            <td class="align-top">Console<wbr>Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoints</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ip<wbr>Address</td>
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
            <td class="align-top">console<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoints</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ip<wbr>Address</td>
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
            <td class="align-top">console_<wbr>url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoints</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ip_<wbr>address</td>
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





#### BrokerLogs
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BrokerLogs">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BrokerLogs">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerLogsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerLogsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerLogsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerLogs.html">output</a> API doc for this type.
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
            <td class="align-top">Audit</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">General</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables general logging via CloudWatch. Defaults to `false`.
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
            <td class="align-top">Audit</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">General</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables general logging via CloudWatch. Defaults to `false`.
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
            <td class="align-top">audit</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">general</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables general logging via CloudWatch. Defaults to `false`.
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
            <td class="align-top">audit</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables audit logging. User management action made using JMX or the ActiveMQ Web Console is logged. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">general</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Enables general logging via CloudWatch. Defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BrokerMaintenanceWindowStartTime
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BrokerMaintenanceWindowStartTime">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BrokerMaintenanceWindowStartTime">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerMaintenanceWindowStartTimeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerMaintenanceWindowStartTimeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerMaintenanceWindowStartTimeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerMaintenanceWindowStartTime.html">output</a> API doc for this type.
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
            <td class="align-top">Day<wbr>Of<wbr>Week</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The day of the week. e.g. `MONDAY`, `TUESDAY`, or `WEDNESDAY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Of<wbr>Day</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time, in 24-hour format. e.g. `02:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. `CET`
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
            <td class="align-top">Day<wbr>Of<wbr>Week</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The day of the week. e.g. `MONDAY`, `TUESDAY`, or `WEDNESDAY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Of<wbr>Day</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time, in 24-hour format. e.g. `02:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Time<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. `CET`
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
            <td class="align-top">day<wbr>Of<wbr>Week</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The day of the week. e.g. `MONDAY`, `TUESDAY`, or `WEDNESDAY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time<wbr>Of<wbr>Day</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time, in 24-hour format. e.g. `02:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time<wbr>Zone</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. `CET`
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
            <td class="align-top">day_<wbr>of_<wbr>week</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The day of the week. e.g. `MONDAY`, `TUESDAY`, or `WEDNESDAY`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time_<wbr>of_<wbr>day</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time, in 24-hour format. e.g. `02:00`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">time_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The time zone, UTC by default, in either the Country/City format, or the UTC offset format. e.g. `CET`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### BrokerUser
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#BrokerUser">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#BrokerUser">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerUserArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/mq?tab=doc#BrokerUserOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerUserArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Mq.BrokerUser.html">output</a> API doc for this type.
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
            <td class="align-top">Console<wbr>Access</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable access to the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) for the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of groups (20 maximum) to which the ActiveMQ user belongs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username of the user.
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
            <td class="align-top">Console<wbr>Access</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable access to the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) for the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of groups (20 maximum) to which the ActiveMQ user belongs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Password</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username of the user.
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
            <td class="align-top">console<wbr>Access</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable access to the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) for the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of groups (20 maximum) to which the ActiveMQ user belongs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username of the user.
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
            <td class="align-top">console_<wbr>access</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable access to the [ActiveMQ Web Console](http://activemq.apache.org/web-console.html) for the user.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">groups</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The list of groups (20 maximum) to which the ActiveMQ user belongs.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">password</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The password of the user. It must be 12 to 250 characters long, at least 4 unique characters, and must not contain commas.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">username</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The username of the user.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







