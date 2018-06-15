---
title: Module mq
---

<a href="../index.html">@pulumi/aws</a> &gt; mq

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Broker">class Broker</a>
* <a href="#Configuration">class Configuration</a>
* <a href="#getBroker">function getBroker</a>
* <a href="#BrokerArgs">interface BrokerArgs</a>
* <a href="#BrokerState">interface BrokerState</a>
* <a href="#ConfigurationArgs">interface ConfigurationArgs</a>
* <a href="#ConfigurationState">interface ConfigurationState</a>
* <a href="#GetBrokerArgs">interface GetBrokerArgs</a>
* <a href="#GetBrokerResult">interface GetBrokerResult</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts">mq/broker.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts">mq/configuration.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts">mq/getBroker.ts</a> 


<h2 class="pdoc-module-header" id="Broker">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L24">class Broker</a>
</h2>

Provides an MQ Broker Resource. This resources also manages users for the broker.

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

Changes to an MQ Broker can occur when you change a
parameter, such as `configuration` or `user`, and are reflected in the next maintenance
window. Because of this, Terraform may report a difference in its planning
phase because a modification has not yet taken place. You can use the
`apply_immediately` flag to instruct the service to apply the change immediately
(see documentation below).

~> **Note:** using `apply_immediately` can result in a
brief downtime as the broker reboots.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L104">constructor</a>
</h3>

```typescript
new Broker(name: string, args: BrokerArgs, opts?: pulumi.ResourceOptions)
```


Create a Broker resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L33">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BrokerState): Broker
```


Get an existing Broker resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L41">property applyImmediately</a>
</h3>

```typescript
public applyImmediately: pulumi.Output<boolean | undefined>;
```


Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L45">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L49">property autoMinorVersionUpgrade</a>
</h3>

```typescript
public autoMinorVersionUpgrade: pulumi.Output<boolean | undefined>;
```


Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L53">property brokerName</a>
</h3>

```typescript
public brokerName: pulumi.Output<string>;
```


The name of the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L57">property configuration</a>
</h3>

```typescript
public configuration: pulumi.Output<{ ... }>;
```


Configuration of the broker. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L61">property deploymentMode</a>
</h3>

```typescript
public deploymentMode: pulumi.Output<string | undefined>;
```


The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L65">property engineType</a>
</h3>

```typescript
public engineType: pulumi.Output<string>;
```


The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L69">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The version of the broker engine. Currently, Amazon MQ supports only `5.15.0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L73">property hostInstanceType</a>
</h3>

```typescript
public hostInstanceType: pulumi.Output<string>;
```


The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L84">property instances</a>
</h3>

```typescript
public instances: pulumi.Output<{ ... }[]>;
```


A list of information about allocated brokers (both active & standby).
* `instances.0.console_url` - The URL of the broker's [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.endpoints` - The broker's wire-level protocol endpoints in the following order & format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L88">property maintenanceWindowStartTime</a>
</h3>

```typescript
public maintenanceWindowStartTime: pulumi.Output<{ ... }>;
```


Maintenance window start time. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L92">property publiclyAccessible</a>
</h3>

```typescript
public publiclyAccessible: pulumi.Output<boolean | undefined>;
```


Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L96">property securityGroups</a>
</h3>

```typescript
public securityGroups: pulumi.Output<string[]>;
```


The list of security group IDs assigned to the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L100">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string[]>;
```


The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L104">property users</a>
</h3>

```typescript
public users: pulumi.Output<{ ... }[]>;
```


The list of all ActiveMQ usernames for the specified broker. See below.

<h2 class="pdoc-module-header" id="Configuration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L11">class Configuration</a>
</h2>

Provides an MQ Configuration Resource.

For more information on Amazon MQ, see [Amazon MQ documentation](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L53">constructor</a>
</h3>

```typescript
new Configuration(name: string, args: ConfigurationArgs, opts?: pulumi.ResourceOptions)
```


Create a Configuration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationState): Configuration
```


Get an existing Configuration resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L33">property data</a>
</h3>

```typescript
public data: pulumi.Output<string>;
```


The broker configuration in XML format.
See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
for supported parameters and format of the XML.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L41">property engineType</a>
</h3>

```typescript
public engineType: pulumi.Output<string>;
```


The type of broker engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L45">property engineVersion</a>
</h3>

```typescript
public engineVersion: pulumi.Output<string>;
```


The version of the broker engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L49">property latestRevision</a>
</h3>

```typescript
public latestRevision: pulumi.Output<number>;
```


The latest revision of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the configuration

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getBroker">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L9">function getBroker</a>
</h2>

```typescript
getBroker(args?: GetBrokerArgs): Promise<GetBrokerResult>
```


Provides information about a MQ Broker.

<h2 class="pdoc-module-header" id="BrokerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L250">interface BrokerArgs</a>
</h2>

The set of arguments for constructing a Broker resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L255">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L259">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L263">property brokerName</a>
</h3>

```typescript
brokerName: pulumi.Input<string>;
```


The name of the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L267">property configuration</a>
</h3>

```typescript
configuration?: pulumi.Input<{ ... }>;
```


Configuration of the broker. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L271">property deploymentMode</a>
</h3>

```typescript
deploymentMode?: pulumi.Input<string>;
```


The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L275">property engineType</a>
</h3>

```typescript
engineType: pulumi.Input<string>;
```


The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L279">property engineVersion</a>
</h3>

```typescript
engineVersion: pulumi.Input<string>;
```


The version of the broker engine. Currently, Amazon MQ supports only `5.15.0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L283">property hostInstanceType</a>
</h3>

```typescript
hostInstanceType: pulumi.Input<string>;
```


The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L287">property maintenanceWindowStartTime</a>
</h3>

```typescript
maintenanceWindowStartTime?: pulumi.Input<{ ... }>;
```


Maintenance window start time. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L291">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L295">property securityGroups</a>
</h3>

```typescript
securityGroups: pulumi.Input<pulumi.Input<string>[]>;
```


The list of security group IDs assigned to the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L299">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L303">property users</a>
</h3>

```typescript
users: pulumi.Input<{ ... }[]>;
```


The list of all ActiveMQ usernames for the specified broker. See below.

<h2 class="pdoc-module-header" id="BrokerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L176">interface BrokerState</a>
</h2>

Input properties used for looking up and filtering Broker resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L181">property applyImmediately</a>
</h3>

```typescript
applyImmediately?: pulumi.Input<boolean>;
```


Specifies whether any broker modifications
are applied immediately, or during the next maintenance window. Default is `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L185">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L189">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade?: pulumi.Input<boolean>;
```


Enables automatic upgrades to new minor versions for brokers, as Apache releases the versions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L193">property brokerName</a>
</h3>

```typescript
brokerName?: pulumi.Input<string>;
```


The name of the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L197">property configuration</a>
</h3>

```typescript
configuration?: pulumi.Input<{ ... }>;
```


Configuration of the broker. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L201">property deploymentMode</a>
</h3>

```typescript
deploymentMode?: pulumi.Input<string>;
```


The deployment mode of the broker. Supported: `SINGLE_INSTANCE` and `ACTIVE_STANDBY_MULTI_AZ`. Defaults to `SINGLE_INSTANCE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L205">property engineType</a>
</h3>

```typescript
engineType?: pulumi.Input<string>;
```


The type of broker engine. Currently, Amazon MQ supports only `ActiveMQ`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L209">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The version of the broker engine. Currently, Amazon MQ supports only `5.15.0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L213">property hostInstanceType</a>
</h3>

```typescript
hostInstanceType?: pulumi.Input<string>;
```


The broker's instance type. e.g. `mq.t2.micro` or `mq.m4.large`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L224">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<{ ... }[]>;
```


A list of information about allocated brokers (both active & standby).
* `instances.0.console_url` - The URL of the broker's [ActiveMQ Web Console](http://activemq.apache.org/web-console.html).
* `instances.0.endpoints` - The broker's wire-level protocol endpoints in the following order & format referenceable e.g. as `instances.0.endpoints.0` (SSL):
* `ssl://broker-id.mq.us-west-2.amazonaws.com:61617`
* `amqp+ssl://broker-id.mq.us-west-2.amazonaws.com:5671`
* `stomp+ssl://broker-id.mq.us-west-2.amazonaws.com:61614`
* `mqtt+ssl://broker-id.mq.us-west-2.amazonaws.com:8883`
* `wss://broker-id.mq.us-west-2.amazonaws.com:61619`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L228">property maintenanceWindowStartTime</a>
</h3>

```typescript
maintenanceWindowStartTime?: pulumi.Input<{ ... }>;
```


Maintenance window start time. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L232">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible?: pulumi.Input<boolean>;
```


Whether to enable connections from applications outside of the VPC that hosts the broker's subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L236">property securityGroups</a>
</h3>

```typescript
securityGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of security group IDs assigned to the broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L240">property subnetIds</a>
</h3>

```typescript
subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of subnet IDs in which to launch the broker. A `SINGLE_INSTANCE` deployment requires one subnet. An `ACTIVE_STANDBY_MULTI_AZ` deployment requires two subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/broker.ts#L244">property users</a>
</h3>

```typescript
users?: pulumi.Input<{ ... }[]>;
```


The list of all ActiveMQ usernames for the specified broker. See below.

<h2 class="pdoc-module-header" id="ConfigurationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L136">interface ConfigurationArgs</a>
</h2>

The set of arguments for constructing a Configuration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L142">property data</a>
</h3>

```typescript
data: pulumi.Input<string>;
```


The broker configuration in XML format.
See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
for supported parameters and format of the XML.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L146">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L150">property engineType</a>
</h3>

```typescript
engineType: pulumi.Input<string>;
```


The type of broker engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L154">property engineVersion</a>
</h3>

```typescript
engineVersion: pulumi.Input<string>;
```


The version of the broker engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the configuration

<h2 class="pdoc-module-header" id="ConfigurationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L100">interface ConfigurationState</a>
</h2>

Input properties used for looking up and filtering Configuration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L104">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L110">property data</a>
</h3>

```typescript
data?: pulumi.Input<string>;
```


The broker configuration in XML format.
See [official docs](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/amazon-mq-broker-configuration-parameters.html)
for supported parameters and format of the XML.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L114">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L118">property engineType</a>
</h3>

```typescript
engineType?: pulumi.Input<string>;
```


The type of broker engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L122">property engineVersion</a>
</h3>

```typescript
engineVersion?: pulumi.Input<string>;
```


The version of the broker engine.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L126">property latestRevision</a>
</h3>

```typescript
latestRevision?: pulumi.Input<number>;
```


The latest revision of the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/configuration.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the configuration

<h2 class="pdoc-module-header" id="GetBrokerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L20">interface GetBrokerArgs</a>
</h2>

A collection of arguments for invoking getBroker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L24">property brokerId</a>
</h3>

```typescript
brokerId?: pulumi.Input<string>;
```


The unique id of the mq broker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L28">property brokerName</a>
</h3>

```typescript
brokerName?: pulumi.Input<string>;
```


The unique name of the mq broker.

<h2 class="pdoc-module-header" id="GetBrokerResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L34">interface GetBrokerResult</a>
</h2>

A collection of values returned by getBroker.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L35">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L36">property autoMinorVersionUpgrade</a>
</h3>

```typescript
autoMinorVersionUpgrade: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L37">property brokerId</a>
</h3>

```typescript
brokerId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L38">property brokerName</a>
</h3>

```typescript
brokerName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L39">property configuration</a>
</h3>

```typescript
configuration: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L40">property deploymentMode</a>
</h3>

```typescript
deploymentMode: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L41">property engineType</a>
</h3>

```typescript
engineType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L42">property engineVersion</a>
</h3>

```typescript
engineVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L43">property hostInstanceType</a>
</h3>

```typescript
hostInstanceType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L44">property instances</a>
</h3>

```typescript
instances: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L45">property maintenanceWindowStartTime</a>
</h3>

```typescript
maintenanceWindowStartTime: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L46">property publiclyAccessible</a>
</h3>

```typescript
publiclyAccessible: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L47">property securityGroups</a>
</h3>

```typescript
securityGroups: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L48">property subnetIds</a>
</h3>

```typescript
subnetIds: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/mq/getBroker.ts#L49">property users</a>
</h3>

```typescript
users: { ... }[];
```

