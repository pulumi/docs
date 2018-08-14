---
title: Module opsworks
---

<a href="../index.html">@pulumi/aws</a> &gt; opsworks

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Application">class Application</a>
* <a href="#CustomLayer">class CustomLayer</a>
* <a href="#GangliaLayer">class GangliaLayer</a>
* <a href="#HaproxyLayer">class HaproxyLayer</a>
* <a href="#Instance">class Instance</a>
* <a href="#JavaAppLayer">class JavaAppLayer</a>
* <a href="#MemcachedLayer">class MemcachedLayer</a>
* <a href="#MysqlLayer">class MysqlLayer</a>
* <a href="#NodejsAppLayer">class NodejsAppLayer</a>
* <a href="#Permission">class Permission</a>
* <a href="#PhpAppLayer">class PhpAppLayer</a>
* <a href="#RailsAppLayer">class RailsAppLayer</a>
* <a href="#RdsDbInstance">class RdsDbInstance</a>
* <a href="#Stack">class Stack</a>
* <a href="#StaticWebLayer">class StaticWebLayer</a>
* <a href="#UserProfile">class UserProfile</a>
* <a href="#ApplicationArgs">interface ApplicationArgs</a>
* <a href="#ApplicationState">interface ApplicationState</a>
* <a href="#CustomLayerArgs">interface CustomLayerArgs</a>
* <a href="#CustomLayerState">interface CustomLayerState</a>
* <a href="#GangliaLayerArgs">interface GangliaLayerArgs</a>
* <a href="#GangliaLayerState">interface GangliaLayerState</a>
* <a href="#HaproxyLayerArgs">interface HaproxyLayerArgs</a>
* <a href="#HaproxyLayerState">interface HaproxyLayerState</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#JavaAppLayerArgs">interface JavaAppLayerArgs</a>
* <a href="#JavaAppLayerState">interface JavaAppLayerState</a>
* <a href="#MemcachedLayerArgs">interface MemcachedLayerArgs</a>
* <a href="#MemcachedLayerState">interface MemcachedLayerState</a>
* <a href="#MysqlLayerArgs">interface MysqlLayerArgs</a>
* <a href="#MysqlLayerState">interface MysqlLayerState</a>
* <a href="#NodejsAppLayerArgs">interface NodejsAppLayerArgs</a>
* <a href="#NodejsAppLayerState">interface NodejsAppLayerState</a>
* <a href="#PermissionArgs">interface PermissionArgs</a>
* <a href="#PermissionState">interface PermissionState</a>
* <a href="#PhpAppLayerArgs">interface PhpAppLayerArgs</a>
* <a href="#PhpAppLayerState">interface PhpAppLayerState</a>
* <a href="#RailsAppLayerArgs">interface RailsAppLayerArgs</a>
* <a href="#RailsAppLayerState">interface RailsAppLayerState</a>
* <a href="#RdsDbInstanceArgs">interface RdsDbInstanceArgs</a>
* <a href="#RdsDbInstanceState">interface RdsDbInstanceState</a>
* <a href="#StackArgs">interface StackArgs</a>
* <a href="#StackState">interface StackState</a>
* <a href="#StaticWebLayerArgs">interface StaticWebLayerArgs</a>
* <a href="#StaticWebLayerState">interface StaticWebLayerState</a>
* <a href="#UserProfileArgs">interface UserProfileArgs</a>
* <a href="#UserProfileState">interface UserProfileState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts">opsworks/application.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts">opsworks/customLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts">opsworks/gangliaLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts">opsworks/haproxyLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts">opsworks/instance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts">opsworks/javaAppLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts">opsworks/memcachedLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts">opsworks/mysqlLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts">opsworks/nodejsAppLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts">opsworks/permission.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts">opsworks/phpAppLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts">opsworks/railsAppLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts">opsworks/rdsDbInstance.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts">opsworks/stack.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts">opsworks/staticWebLayer.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts">opsworks/userProfile.ts</a> 


<h2 class="pdoc-module-header" id="Application">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L9">class Application</a>
</h2>

Provides an OpsWorks application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L89">constructor</a>
</h3>

```typescript
new Application(name: string, args: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState): Application
```


Get an existing Application resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L25">property appSources</a>
</h3>

```typescript
public appSources: pulumi.Output<{ ... }[]>;
```


SCM configuration of the app as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L29">property autoBundleOnDeploy</a>
</h3>

```typescript
public autoBundleOnDeploy: pulumi.Output<string | undefined>;
```


Run bundle install when deploying for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L33">property awsFlowRubySettings</a>
</h3>

```typescript
public awsFlowRubySettings: pulumi.Output<string | undefined>;
```


Specify activity and workflow workers for your app using the aws-flow gem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L37">property dataSourceArn</a>
</h3>

```typescript
public dataSourceArn: pulumi.Output<string | undefined>;
```


The data source's ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L41">property dataSourceDatabaseName</a>
</h3>

```typescript
public dataSourceDatabaseName: pulumi.Output<string | undefined>;
```


The database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L45">property dataSourceType</a>
</h3>

```typescript
public dataSourceType: pulumi.Output<string | undefined>;
```


The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L49">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L53">property documentRoot</a>
</h3>

```typescript
public documentRoot: pulumi.Output<string | undefined>;
```


Subfolder for the document root for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L57">property domains</a>
</h3>

```typescript
public domains: pulumi.Output<string[] | undefined>;
```


A list of virtual host alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L61">property enableSsl</a>
</h3>

```typescript
public enableSsl: pulumi.Output<boolean | undefined>;
```


Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L65">property environments</a>
</h3>

```typescript
public environments: pulumi.Output<{ ... }[] | undefined>;
```


Object to define environment variables.  Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L69">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L73">property railsEnv</a>
</h3>

```typescript
public railsEnv: pulumi.Output<string | undefined>;
```


The name of the Rails environment for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L77">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L81">property sslConfigurations</a>
</h3>

```typescript
public sslConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


The SSL configuration of the app. Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L85">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the application will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L89">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of source to use. For example, "archive".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CustomLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L9">class CustomLayer</a>
</h2>

Provides an OpsWorks custom layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L90">constructor</a>
</h3>

```typescript
new CustomLayer(name: string, args: CustomLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CustomLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CustomLayerState): CustomLayer
```


Get an existing CustomLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L25">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L29">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L33">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L34">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L35">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L39">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L43">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L47">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L48">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L49">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L50">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L54">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L58">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L62">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L66">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L70">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L78">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L82">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L86">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L90">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="GangliaLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L9">class GangliaLayer</a>
</h2>

Provides an OpsWorks Ganglia layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L98">constructor</a>
</h3>

```typescript
new GangliaLayer(name: string, args: GangliaLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GangliaLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GangliaLayerState): GangliaLayer
```


Get an existing GangliaLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L25">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L29">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L33">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L34">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L35">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L39">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L43">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L47">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L48">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L49">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L50">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L54">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L58">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L62">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L66">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L70">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L78">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The password to use for Ganglia.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L82">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L86">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L90">property url</a>
</h3>

```typescript
public url: pulumi.Output<string | undefined>;
```


The URL path to use for Ganglia. Defaults to "/ganglia".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L94">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L98">property username</a>
</h3>

```typescript
public username: pulumi.Output<string | undefined>;
```


The username to use for Ganglia. Defaults to "opsworks".

<h2 class="pdoc-module-header" id="HaproxyLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L9">class HaproxyLayer</a>
</h2>

Provides an OpsWorks haproxy layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L110">constructor</a>
</h3>

```typescript
new HaproxyLayer(name: string, args: HaproxyLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HaproxyLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: HaproxyLayerState): HaproxyLayer
```


Get an existing HaproxyLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L25">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L29">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L33">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L34">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L35">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L39">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L43">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L47">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L48">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L49">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L50">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L54">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L58">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L62">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L66">property healthcheckMethod</a>
</h3>

```typescript
public healthcheckMethod: pulumi.Output<string | undefined>;
```


HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L70">property healthcheckUrl</a>
</h3>

```typescript
public healthcheckUrl: pulumi.Output<string | undefined>;
```


URL path to use for instance healthchecks. Defaults to "/".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L74">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L78">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L82">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L86">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L90">property statsEnabled</a>
</h3>

```typescript
public statsEnabled: pulumi.Output<boolean | undefined>;
```


Whether to enable HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L94">property statsPassword</a>
</h3>

```typescript
public statsPassword: pulumi.Output<string>;
```


The password to use for HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L98">property statsUrl</a>
</h3>

```typescript
public statsUrl: pulumi.Output<string | undefined>;
```


The HAProxy stats URL. Defaults to "/haproxy?stats".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L102">property statsUser</a>
</h3>

```typescript
public statsUser: pulumi.Output<string | undefined>;
```


The username for HAProxy stats. Defaults to "opsworks".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L106">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L110">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L9">class Instance</a>
</h2>

Provides an OpsWorks instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L155">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L25">property agentVersion</a>
</h3>

```typescript
public agentVersion: pulumi.Output<string | undefined>;
```


The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L29">property amiId</a>
</h3>

```typescript
public amiId: pulumi.Output<string>;
```


The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L33">property architecture</a>
</h3>

```typescript
public architecture: pulumi.Output<string | undefined>;
```


Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L37">property autoScalingType</a>
</h3>

```typescript
public autoScalingType: pulumi.Output<string | undefined>;
```


Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L42">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


Name of the availability zone where instances will be created
by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L43">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L44">property deleteEbs</a>
</h3>

```typescript
public deleteEbs: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L45">property deleteEip</a>
</h3>

```typescript
public deleteEip: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L50">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Additional EBS block devices to attach to the
instance.  See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L54">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean | undefined>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L58">property ec2InstanceId</a>
</h3>

```typescript
public ec2InstanceId: pulumi.Output<string>;
```


EC2 instance ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L59">property ecsClusterArn</a>
</h3>

```typescript
public ecsClusterArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L60">property elasticIp</a>
</h3>

```typescript
public elasticIp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L65">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L69">property hostname</a>
</h3>

```typescript
public hostname: pulumi.Output<string>;
```


The instance's host name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L70">property infrastructureClass</a>
</h3>

```typescript
public infrastructureClass: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L74">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L75">property instanceProfileArn</a>
</h3>

```typescript
public instanceProfileArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L79">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string | undefined>;
```


The type of instance to start

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L80">property lastServiceErrorId</a>
</h3>

```typescript
public lastServiceErrorId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L84">property layerIds</a>
</h3>

```typescript
public layerIds: pulumi.Output<string[]>;
```


The ids of the layers the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L88">property os</a>
</h3>

```typescript
public os: pulumi.Output<string>;
```


Name of operating system that will be installed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L89">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L95">property privateDns</a>
</h3>

```typescript
public privateDns: pulumi.Output<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L99">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```


The private IP address assigned to the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L104">property publicDns</a>
</h3>

```typescript
public publicDns: pulumi.Output<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L108">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L109">property registeredBy</a>
</h3>

```typescript
public registeredBy: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L110">property reportedAgentVersion</a>
</h3>

```typescript
public reportedAgentVersion: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L111">property reportedOsFamily</a>
</h3>

```typescript
public reportedOsFamily: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L112">property reportedOsName</a>
</h3>

```typescript
public reportedOsName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L113">property reportedOsVersion</a>
</h3>

```typescript
public reportedOsVersion: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L118">property rootBlockDevices</a>
</h3>

```typescript
public rootBlockDevices: pulumi.Output<{ ... }[]>;
```


Customize details about the root block
device of the instance. See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L122">property rootDeviceType</a>
</h3>

```typescript
public rootDeviceType: pulumi.Output<string>;
```


Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L123">property rootDeviceVolumeId</a>
</h3>

```typescript
public rootDeviceVolumeId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L127">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L128">property sshHostDsaKeyFingerprint</a>
</h3>

```typescript
public sshHostDsaKeyFingerprint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L129">property sshHostRsaKeyFingerprint</a>
</h3>

```typescript
public sshHostRsaKeyFingerprint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L133">property sshKeyName</a>
</h3>

```typescript
public sshKeyName: pulumi.Output<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L137">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L141">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


The desired state of the instance.  Can be either `"running"` or `"stopped"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L142">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L146">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L150">property tenancy</a>
</h3>

```typescript
public tenancy: pulumi.Output<string>;
```


Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L155">property virtualizationType</a>
</h3>

```typescript
public virtualizationType: pulumi.Output<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

<h2 class="pdoc-module-header" id="JavaAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L9">class JavaAppLayer</a>
</h2>

Provides an OpsWorks Java application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L106">constructor</a>
</h3>

```typescript
new JavaAppLayer(name: string, args: JavaAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a JavaAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JavaAppLayerState): JavaAppLayer
```


Get an existing JavaAppLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L25">property appServer</a>
</h3>

```typescript
public appServer: pulumi.Output<string | undefined>;
```


Keyword for the application container to use. Defaults to "tomcat".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L29">property appServerVersion</a>
</h3>

```typescript
public appServerVersion: pulumi.Output<string | undefined>;
```


Version of the selected application container to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L33">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L37">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L41">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L42">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L43">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L47">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L51">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L55">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L56">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L57">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L58">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L62">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L66">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L70">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L74">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L78">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L82">property jvmOptions</a>
</h3>

```typescript
public jvmOptions: pulumi.Output<string | undefined>;
```


Options to set for the JVM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L86">property jvmType</a>
</h3>

```typescript
public jvmType: pulumi.Output<string | undefined>;
```


Keyword for the type of JVM to use. Defaults to `openjdk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L90">property jvmVersion</a>
</h3>

```typescript
public jvmVersion: pulumi.Output<string | undefined>;
```


Version of JVM to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L94">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L98">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L102">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L106">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MemcachedLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L9">class MemcachedLayer</a>
</h2>

Provides an OpsWorks memcached layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L90">constructor</a>
</h3>

```typescript
new MemcachedLayer(name: string, args: MemcachedLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MemcachedLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MemcachedLayerState): MemcachedLayer
```


Get an existing MemcachedLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L25">property allocatedMemory</a>
</h3>

```typescript
public allocatedMemory: pulumi.Output<number | undefined>;
```


Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L29">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L33">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L37">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L38">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L39">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L43">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L47">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L51">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L52">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L53">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L54">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L58">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L62">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L66">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L70">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L74">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L78">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L82">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L86">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L90">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MysqlLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L12">class MysqlLayer</a>
</h2>

Provides an OpsWorks MySQL layer resource.

~> **Note:** All arguments including the root password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L97">constructor</a>
</h3>

```typescript
new MysqlLayer(name: string, args: MysqlLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MysqlLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MysqlLayerState): MysqlLayer
```


Get an existing MysqlLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L28">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L32">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L36">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L37">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L38">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L42">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L46">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L50">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L51">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L52">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L53">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L57">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L61">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L65">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L69">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L73">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L77">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L81">property rootPassword</a>
</h3>

```typescript
public rootPassword: pulumi.Output<string | undefined>;
```


Root password to use for MySQL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L85">property rootPasswordOnAllInstances</a>
</h3>

```typescript
public rootPasswordOnAllInstances: pulumi.Output<boolean | undefined>;
```


Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L89">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L93">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L97">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="NodejsAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L9">class NodejsAppLayer</a>
</h2>

Provides an OpsWorks NodeJS application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L90">constructor</a>
</h3>

```typescript
new NodejsAppLayer(name: string, args: NodejsAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NodejsAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NodejsAppLayerState): NodejsAppLayer
```


Get an existing NodejsAppLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L25">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L29">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L33">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L34">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L35">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L39">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L43">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L47">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L48">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L49">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L50">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L54">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L58">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L62">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L66">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L70">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L78">property nodejsVersion</a>
</h3>

```typescript
public nodejsVersion: pulumi.Output<string | undefined>;
```


The version of NodeJS to use. Defaults to "0.10.38".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L82">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L86">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L90">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="Permission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L9">class Permission</a>
</h2>

Provides an OpsWorks permission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L41">constructor</a>
</h3>

```typescript
new Permission(name: string, args: PermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Permission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PermissionState): Permission
```


Get an existing Permission resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L25">property allowSsh</a>
</h3>

```typescript
public allowSsh: pulumi.Output<boolean>;
```


Whether the user is allowed to use SSH to communicate with the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L29">property allowSudo</a>
</h3>

```typescript
public allowSudo: pulumi.Output<boolean>;
```


Whether the user is allowed to use sudo to elevate privileges

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L33">property level</a>
</h3>

```typescript
public level: pulumi.Output<string>;
```


The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L37">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The stack to set the permissions for

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L41">property userArn</a>
</h3>

```typescript
public userArn: pulumi.Output<string>;
```


The user's IAM ARN to set permissions for

<h2 class="pdoc-module-header" id="PhpAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L9">class PhpAppLayer</a>
</h2>

Provides an OpsWorks PHP application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L86">constructor</a>
</h3>

```typescript
new PhpAppLayer(name: string, args: PhpAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PhpAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PhpAppLayerState): PhpAppLayer
```


Get an existing PhpAppLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L25">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L29">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L33">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L34">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L35">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L39">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L43">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L47">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L48">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L49">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L50">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L54">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L58">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L62">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L66">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L70">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L74">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L78">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L82">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L86">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RailsAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L9">class RailsAppLayer</a>
</h2>

Provides an OpsWorks Ruby on Rails application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L110">constructor</a>
</h3>

```typescript
new RailsAppLayer(name: string, args: RailsAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RailsAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RailsAppLayerState): RailsAppLayer
```


Get an existing RailsAppLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L25">property appServer</a>
</h3>

```typescript
public appServer: pulumi.Output<string | undefined>;
```


Keyword for the app server to use. Defaults to "apache_passenger".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L29">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L33">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L37">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L41">property bundlerVersion</a>
</h3>

```typescript
public bundlerVersion: pulumi.Output<string | undefined>;
```


When OpsWorks is managing Bundler, which version to use. Defaults to "1.5.3".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L42">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L43">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L47">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L51">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L55">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L56">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L57">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L58">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L62">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L66">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L70">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L74">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L78">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L82">property manageBundler</a>
</h3>

```typescript
public manageBundler: pulumi.Output<boolean | undefined>;
```


Whether OpsWorks should manage bundler. On by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L86">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L90">property passengerVersion</a>
</h3>

```typescript
public passengerVersion: pulumi.Output<string | undefined>;
```


The version of Passenger to use. Defaults to "4.0.46".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L94">property rubyVersion</a>
</h3>

```typescript
public rubyVersion: pulumi.Output<string | undefined>;
```


The version of Ruby to use. Defaults to "2.0.0".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L98">property rubygemsVersion</a>
</h3>

```typescript
public rubygemsVersion: pulumi.Output<string | undefined>;
```


The version of RubyGems to use. Defaults to "2.2.2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L102">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L106">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L110">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RdsDbInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L12">class RdsDbInstance</a>
</h2>

Provides an OpsWorks RDS DB Instance resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L40">constructor</a>
</h3>

```typescript
new RdsDbInstance(name: string, args: RdsDbInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RdsDbInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RdsDbInstanceState): RdsDbInstance
```


Get an existing RdsDbInstance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L28">property dbPassword</a>
</h3>

```typescript
public dbPassword: pulumi.Output<string>;
```


A db password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L32">property dbUser</a>
</h3>

```typescript
public dbUser: pulumi.Output<string>;
```


A db username

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L36">property rdsDbInstanceArn</a>
</h3>

```typescript
public rdsDbInstanceArn: pulumi.Output<string>;
```


The db instance to register for this stack. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L40">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The stack to register a db inatance for. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Stack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L11">class Stack</a>
</h2>

Provides an OpsWorks stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L120">constructor</a>
</h3>

```typescript
new Stack(name: string, args: StackArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Stack resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StackState): Stack
```


Get an existing Stack resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L27">property agentVersion</a>
</h3>

```typescript
public agentVersion: pulumi.Output<string>;
```


If set to `"LATEST"`, OpsWorks will automatically install the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L32">property berkshelfVersion</a>
</h3>

```typescript
public berkshelfVersion: pulumi.Output<string | undefined>;
```


If `manage_berkshelf` is enabled, the version of Berkshelf to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L36">property color</a>
</h3>

```typescript
public color: pulumi.Output<string | undefined>;
```


Color to paint next to the stack's resources in the OpsWorks console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L40">property configurationManagerName</a>
</h3>

```typescript
public configurationManagerName: pulumi.Output<string | undefined>;
```


Name of the configuration manager to use. Defaults to "Chef".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L44">property configurationManagerVersion</a>
</h3>

```typescript
public configurationManagerVersion: pulumi.Output<string | undefined>;
```


Version of the configuration manager to use. Defaults to "11.4".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L49">property customCookbooksSources</a>
</h3>

```typescript
public customCookbooksSources: pulumi.Output<{ ... }[]>;
```


When `use_custom_cookbooks` is set, provide this sub-object as
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L53">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the entire stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L58">property defaultAvailabilityZone</a>
</h3>

```typescript
public defaultAvailabilityZone: pulumi.Output<string>;
```


Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L63">property defaultInstanceProfileArn</a>
</h3>

```typescript
public defaultInstanceProfileArn: pulumi.Output<string>;
```


The ARN of an IAM Instance Profile that created instances
will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L67">property defaultOs</a>
</h3>

```typescript
public defaultOs: pulumi.Output<string | undefined>;
```


Name of OS that will be installed on instances by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L71">property defaultRootDeviceType</a>
</h3>

```typescript
public defaultRootDeviceType: pulumi.Output<string | undefined>;
```


Name of the type of root device instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L75">property defaultSshKeyName</a>
</h3>

```typescript
public defaultSshKeyName: pulumi.Output<string | undefined>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L80">property defaultSubnetId</a>
</h3>

```typescript
public defaultSubnetId: pulumi.Output<string>;
```


Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L85">property hostnameTheme</a>
</h3>

```typescript
public hostnameTheme: pulumi.Output<string | undefined>;
```


Keyword representing the naming scheme that will be used for instance hostnames
within this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L89">property manageBerkshelf</a>
</h3>

```typescript
public manageBerkshelf: pulumi.Output<boolean | undefined>;
```


Boolean value controlling whether Opsworks will run Berkshelf for this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L93">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L97">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The name of the region where the stack will exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L101">property serviceRoleArn</a>
</h3>

```typescript
public serviceRoleArn: pulumi.Output<string>;
```


The ARN of an IAM role that the OpsWorks service will act as.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L102">property stackEndpoint</a>
</h3>

```typescript
public stackEndpoint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L106">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L111">property useCustomCookbooks</a>
</h3>

```typescript
public useCustomCookbooks: pulumi.Output<boolean | undefined>;
```


Boolean value controlling whether the custom cookbook settings are
enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L116">property useOpsworksSecurityGroups</a>
</h3>

```typescript
public useOpsworksSecurityGroups: pulumi.Output<boolean | undefined>;
```


Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L120">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The id of the VPC that this stack belongs to.

<h2 class="pdoc-module-header" id="StaticWebLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L9">class StaticWebLayer</a>
</h2>

Provides an OpsWorks static web server layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L83">constructor</a>
</h3>

```typescript
new StaticWebLayer(name: string, args: StaticWebLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StaticWebLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StaticWebLayerState): StaticWebLayer
```


Get an existing StaticWebLayer resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L25">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L29">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L33">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L34">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L35">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L39">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L40">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L44">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L45">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L46">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L47">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L51">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L55">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L59">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L63">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L67">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L71">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L75">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L79">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L83">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="UserProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L9">class UserProfile</a>
</h2>

Provides an OpsWorks User Profile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L37">constructor</a>
</h3>

```typescript
new UserProfile(name: string, args: UserProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserProfile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: UserProfileState): UserProfile
```


Get an existing UserProfile resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L25">property allowSelfManagement</a>
</h3>

```typescript
public allowSelfManagement: pulumi.Output<boolean | undefined>;
```


Whether users can specify their own SSH public key through the My Settings page

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L29">property sshPublicKey</a>
</h3>

```typescript
public sshPublicKey: pulumi.Output<string | undefined>;
```


The users public key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L33">property sshUsername</a>
</h3>

```typescript
public sshUsername: pulumi.Output<string>;
```


The ssh username, with witch this user wants to log in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L37">property userArn</a>
</h3>

```typescript
public userArn: pulumi.Output<string>;
```


The user's IAM ARN

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L227">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L231">property appSources</a>
</h3>

```typescript
appSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


SCM configuration of the app as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L235">property autoBundleOnDeploy</a>
</h3>

```typescript
autoBundleOnDeploy?: pulumi.Input<string>;
```


Run bundle install when deploying for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L239">property awsFlowRubySettings</a>
</h3>

```typescript
awsFlowRubySettings?: pulumi.Input<string>;
```


Specify activity and workflow workers for your app using the aws-flow gem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L243">property dataSourceArn</a>
</h3>

```typescript
dataSourceArn?: pulumi.Input<string>;
```


The data source's ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L247">property dataSourceDatabaseName</a>
</h3>

```typescript
dataSourceDatabaseName?: pulumi.Input<string>;
```


The database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L251">property dataSourceType</a>
</h3>

```typescript
dataSourceType?: pulumi.Input<string>;
```


The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L255">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L259">property documentRoot</a>
</h3>

```typescript
documentRoot?: pulumi.Input<string>;
```


Subfolder for the document root for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L263">property domains</a>
</h3>

```typescript
domains?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual host alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L267">property enableSsl</a>
</h3>

```typescript
enableSsl?: pulumi.Input<boolean>;
```


Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L271">property environments</a>
</h3>

```typescript
environments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Object to define environment variables.  Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L275">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L279">property railsEnv</a>
</h3>

```typescript
railsEnv?: pulumi.Input<string>;
```


The name of the Rails environment for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L283">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L287">property sslConfigurations</a>
</h3>

```typescript
sslConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The SSL configuration of the app. Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L291">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the application will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L295">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of source to use. For example, "archive".

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L153">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L157">property appSources</a>
</h3>

```typescript
appSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


SCM configuration of the app as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L161">property autoBundleOnDeploy</a>
</h3>

```typescript
autoBundleOnDeploy?: pulumi.Input<string>;
```


Run bundle install when deploying for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L165">property awsFlowRubySettings</a>
</h3>

```typescript
awsFlowRubySettings?: pulumi.Input<string>;
```


Specify activity and workflow workers for your app using the aws-flow gem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L169">property dataSourceArn</a>
</h3>

```typescript
dataSourceArn?: pulumi.Input<string>;
```


The data source's ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L173">property dataSourceDatabaseName</a>
</h3>

```typescript
dataSourceDatabaseName?: pulumi.Input<string>;
```


The database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L177">property dataSourceType</a>
</h3>

```typescript
dataSourceType?: pulumi.Input<string>;
```


The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L181">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L185">property documentRoot</a>
</h3>

```typescript
documentRoot?: pulumi.Input<string>;
```


Subfolder for the document root for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L189">property domains</a>
</h3>

```typescript
domains?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual host alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L193">property enableSsl</a>
</h3>

```typescript
enableSsl?: pulumi.Input<boolean>;
```


Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L197">property environments</a>
</h3>

```typescript
environments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Object to define environment variables.  Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L201">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L205">property railsEnv</a>
</h3>

```typescript
railsEnv?: pulumi.Input<string>;
```


The name of the Rails environment for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L209">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L213">property sslConfigurations</a>
</h3>

```typescript
sslConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The SSL configuration of the app. Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L217">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the application will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L221">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of source to use. For example, "archive".

<h2 class="pdoc-module-header" id="CustomLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L237">interface CustomLayerArgs</a>
</h2>

The set of arguments for constructing a CustomLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L241">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L245">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L249">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L250">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L251">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L255">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L259">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L263">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L264">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L265">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L266">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L270">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L274">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L278">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L282">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L286">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L290">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L294">property shortName</a>
</h3>

```typescript
shortName: pulumi.Input<string>;
```


A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L298">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L302">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L306">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="CustomLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L162">interface CustomLayerState</a>
</h2>

Input properties used for looking up and filtering CustomLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L166">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L170">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L174">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L175">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L176">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L180">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L184">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L188">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L189">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L190">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L191">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L195">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L199">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L203">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L207">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L211">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L215">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L219">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L223">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L227">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L231">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="GangliaLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L257">interface GangliaLayerArgs</a>
</h2>

The set of arguments for constructing a GangliaLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L261">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L265">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L269">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L270">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L271">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L275">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L279">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L283">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L284">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L285">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L286">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L290">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L294">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L298">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L302">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L306">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L310">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L314">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The password to use for Ganglia.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L318">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L322">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L326">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL path to use for Ganglia. Defaults to "/ganglia".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L330">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L334">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The username to use for Ganglia. Defaults to "opsworks".

<h2 class="pdoc-module-header" id="GangliaLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L174">interface GangliaLayerState</a>
</h2>

Input properties used for looking up and filtering GangliaLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L178">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L182">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L186">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L187">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L188">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L192">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L196">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L200">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L201">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L202">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L203">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L207">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L211">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L215">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L219">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L223">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L227">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L231">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password to use for Ganglia.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L235">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L239">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L243">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL path to use for Ganglia. Defaults to "/ganglia".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L247">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L251">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The username to use for Ganglia. Defaults to "opsworks".

<h2 class="pdoc-module-header" id="HaproxyLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L287">interface HaproxyLayerArgs</a>
</h2>

The set of arguments for constructing a HaproxyLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L291">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L295">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L299">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L300">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L301">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L305">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L309">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L313">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L314">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L315">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L316">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L320">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L324">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L328">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L332">property healthcheckMethod</a>
</h3>

```typescript
healthcheckMethod?: pulumi.Input<string>;
```


HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L336">property healthcheckUrl</a>
</h3>

```typescript
healthcheckUrl?: pulumi.Input<string>;
```


URL path to use for instance healthchecks. Defaults to "/".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L340">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L344">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L348">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L352">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L356">property statsEnabled</a>
</h3>

```typescript
statsEnabled?: pulumi.Input<boolean>;
```


Whether to enable HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L360">property statsPassword</a>
</h3>

```typescript
statsPassword: pulumi.Input<string>;
```


The password to use for HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L364">property statsUrl</a>
</h3>

```typescript
statsUrl?: pulumi.Input<string>;
```


The HAProxy stats URL. Defaults to "/haproxy?stats".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L368">property statsUser</a>
</h3>

```typescript
statsUser?: pulumi.Input<string>;
```


The username for HAProxy stats. Defaults to "opsworks".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L372">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L376">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="HaproxyLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L192">interface HaproxyLayerState</a>
</h2>

Input properties used for looking up and filtering HaproxyLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L196">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L200">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L204">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L205">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L206">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L210">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L214">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L218">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L219">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L220">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L221">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L225">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L229">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L233">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L237">property healthcheckMethod</a>
</h3>

```typescript
healthcheckMethod?: pulumi.Input<string>;
```


HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L241">property healthcheckUrl</a>
</h3>

```typescript
healthcheckUrl?: pulumi.Input<string>;
```


URL path to use for instance healthchecks. Defaults to "/".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L245">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L249">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L253">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L257">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L261">property statsEnabled</a>
</h3>

```typescript
statsEnabled?: pulumi.Input<boolean>;
```


Whether to enable HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L265">property statsPassword</a>
</h3>

```typescript
statsPassword?: pulumi.Input<string>;
```


The password to use for HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L269">property statsUrl</a>
</h3>

```typescript
statsUrl?: pulumi.Input<string>;
```


The HAProxy stats URL. Defaults to "/haproxy?stats".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L273">property statsUser</a>
</h3>

```typescript
statsUser?: pulumi.Input<string>;
```


The username for HAProxy stats. Defaults to "opsworks".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L277">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L281">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L415">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L419">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L423">property amiId</a>
</h3>

```typescript
amiId?: pulumi.Input<string>;
```


The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L427">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L431">property autoScalingType</a>
</h3>

```typescript
autoScalingType?: pulumi.Input<string>;
```


Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L436">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L437">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L438">property deleteEbs</a>
</h3>

```typescript
deleteEbs?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L439">property deleteEip</a>
</h3>

```typescript
deleteEip?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L444">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L448">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L449">property ecsClusterArn</a>
</h3>

```typescript
ecsClusterArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L450">property elasticIp</a>
</h3>

```typescript
elasticIp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L455">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L459">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The instance's host name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L460">property infrastructureClass</a>
</h3>

```typescript
infrastructureClass?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L464">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L465">property instanceProfileArn</a>
</h3>

```typescript
instanceProfileArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L469">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of instance to start

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L470">property lastServiceErrorId</a>
</h3>

```typescript
lastServiceErrorId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L474">property layerIds</a>
</h3>

```typescript
layerIds: pulumi.Input<pulumi.Input<string>[]>;
```


The ids of the layers the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L478">property os</a>
</h3>

```typescript
os?: pulumi.Input<string>;
```


Name of operating system that will be installed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L479">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L485">property privateDns</a>
</h3>

```typescript
privateDns?: pulumi.Input<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L489">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


The private IP address assigned to the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L494">property publicDns</a>
</h3>

```typescript
publicDns?: pulumi.Input<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L498">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L499">property registeredBy</a>
</h3>

```typescript
registeredBy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L500">property reportedAgentVersion</a>
</h3>

```typescript
reportedAgentVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L501">property reportedOsFamily</a>
</h3>

```typescript
reportedOsFamily?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L502">property reportedOsName</a>
</h3>

```typescript
reportedOsName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L503">property reportedOsVersion</a>
</h3>

```typescript
reportedOsVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L508">property rootBlockDevices</a>
</h3>

```typescript
rootBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize details about the root block
device of the instance. See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L512">property rootDeviceType</a>
</h3>

```typescript
rootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L513">property rootDeviceVolumeId</a>
</h3>

```typescript
rootDeviceVolumeId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L517">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L518">property sshHostDsaKeyFingerprint</a>
</h3>

```typescript
sshHostDsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L519">property sshHostRsaKeyFingerprint</a>
</h3>

```typescript
sshHostRsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L523">property sshKeyName</a>
</h3>

```typescript
sshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L527">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L531">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The desired state of the instance.  Can be either `"running"` or `"stopped"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L532">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L536">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L540">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L545">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L275">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L279">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L283">property amiId</a>
</h3>

```typescript
amiId?: pulumi.Input<string>;
```


The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L287">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L291">property autoScalingType</a>
</h3>

```typescript
autoScalingType?: pulumi.Input<string>;
```


Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L296">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L297">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L298">property deleteEbs</a>
</h3>

```typescript
deleteEbs?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L299">property deleteEip</a>
</h3>

```typescript
deleteEip?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L304">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L308">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L312">property ec2InstanceId</a>
</h3>

```typescript
ec2InstanceId?: pulumi.Input<string>;
```


EC2 instance ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L313">property ecsClusterArn</a>
</h3>

```typescript
ecsClusterArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L314">property elasticIp</a>
</h3>

```typescript
elasticIp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L319">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L323">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The instance's host name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L324">property infrastructureClass</a>
</h3>

```typescript
infrastructureClass?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L328">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L329">property instanceProfileArn</a>
</h3>

```typescript
instanceProfileArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L333">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of instance to start

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L334">property lastServiceErrorId</a>
</h3>

```typescript
lastServiceErrorId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L338">property layerIds</a>
</h3>

```typescript
layerIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The ids of the layers the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L342">property os</a>
</h3>

```typescript
os?: pulumi.Input<string>;
```


Name of operating system that will be installed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L343">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L349">property privateDns</a>
</h3>

```typescript
privateDns?: pulumi.Input<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L353">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


The private IP address assigned to the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L358">property publicDns</a>
</h3>

```typescript
publicDns?: pulumi.Input<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L362">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L363">property registeredBy</a>
</h3>

```typescript
registeredBy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L364">property reportedAgentVersion</a>
</h3>

```typescript
reportedAgentVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L365">property reportedOsFamily</a>
</h3>

```typescript
reportedOsFamily?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L366">property reportedOsName</a>
</h3>

```typescript
reportedOsName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L367">property reportedOsVersion</a>
</h3>

```typescript
reportedOsVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L372">property rootBlockDevices</a>
</h3>

```typescript
rootBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize details about the root block
device of the instance. See [Block Devices](#block-devices) below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L376">property rootDeviceType</a>
</h3>

```typescript
rootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L377">property rootDeviceVolumeId</a>
</h3>

```typescript
rootDeviceVolumeId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L381">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L382">property sshHostDsaKeyFingerprint</a>
</h3>

```typescript
sshHostDsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L383">property sshHostRsaKeyFingerprint</a>
</h3>

```typescript
sshHostRsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L387">property sshKeyName</a>
</h3>

```typescript
sshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L391">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L395">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The desired state of the instance.  Can be either `"running"` or `"stopped"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L396">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L400">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L404">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L409">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

<h2 class="pdoc-module-header" id="JavaAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L274">interface JavaAppLayerArgs</a>
</h2>

The set of arguments for constructing a JavaAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L278">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the application container to use. Defaults to "tomcat".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L282">property appServerVersion</a>
</h3>

```typescript
appServerVersion?: pulumi.Input<string>;
```


Version of the selected application container to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L286">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L290">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L294">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L295">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L296">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L300">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L304">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L308">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L309">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L310">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L311">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L315">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L319">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L323">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L327">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L331">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L335">property jvmOptions</a>
</h3>

```typescript
jvmOptions?: pulumi.Input<string>;
```


Options to set for the JVM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L339">property jvmType</a>
</h3>

```typescript
jvmType?: pulumi.Input<string>;
```


Keyword for the type of JVM to use. Defaults to `openjdk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L343">property jvmVersion</a>
</h3>

```typescript
jvmVersion?: pulumi.Input<string>;
```


Version of JVM to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L347">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L351">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L355">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L359">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="JavaAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L183">interface JavaAppLayerState</a>
</h2>

Input properties used for looking up and filtering JavaAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L187">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the application container to use. Defaults to "tomcat".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L191">property appServerVersion</a>
</h3>

```typescript
appServerVersion?: pulumi.Input<string>;
```


Version of the selected application container to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L195">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L199">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L203">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L204">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L205">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L209">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L213">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L217">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L218">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L219">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L220">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L224">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L228">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L232">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L236">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L240">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L244">property jvmOptions</a>
</h3>

```typescript
jvmOptions?: pulumi.Input<string>;
```


Options to set for the JVM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L248">property jvmType</a>
</h3>

```typescript
jvmType?: pulumi.Input<string>;
```


Keyword for the type of JVM to use. Defaults to `openjdk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L252">property jvmVersion</a>
</h3>

```typescript
jvmVersion?: pulumi.Input<string>;
```


Version of JVM to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L256">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L260">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L264">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L268">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MemcachedLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L234">interface MemcachedLayerArgs</a>
</h2>

The set of arguments for constructing a MemcachedLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L238">property allocatedMemory</a>
</h3>

```typescript
allocatedMemory?: pulumi.Input<number>;
```


Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L242">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L246">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L250">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L251">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L252">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L256">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L260">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L264">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L265">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L266">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L267">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L271">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L275">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L279">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L283">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L287">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L291">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L295">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L299">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L303">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MemcachedLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L159">interface MemcachedLayerState</a>
</h2>

Input properties used for looking up and filtering MemcachedLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L163">property allocatedMemory</a>
</h3>

```typescript
allocatedMemory?: pulumi.Input<number>;
```


Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L167">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L171">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L175">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L176">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L177">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L181">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L185">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L189">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L190">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L191">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L192">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L196">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L200">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L204">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L208">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L212">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L220">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L224">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L228">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MysqlLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L247">interface MysqlLayerArgs</a>
</h2>

The set of arguments for constructing a MysqlLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L251">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L255">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L259">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L260">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L261">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L265">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L269">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L273">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L274">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L275">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L276">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L280">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L284">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L288">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L292">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L296">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L300">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L304">property rootPassword</a>
</h3>

```typescript
rootPassword?: pulumi.Input<string>;
```


Root password to use for MySQL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L308">property rootPasswordOnAllInstances</a>
</h3>

```typescript
rootPasswordOnAllInstances?: pulumi.Input<boolean>;
```


Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L312">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L316">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L320">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MysqlLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L168">interface MysqlLayerState</a>
</h2>

Input properties used for looking up and filtering MysqlLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L172">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L176">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L180">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L181">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L182">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L186">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L190">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L194">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L195">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L196">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L197">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L201">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L205">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L209">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L213">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L217">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L221">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L225">property rootPassword</a>
</h3>

```typescript
rootPassword?: pulumi.Input<string>;
```


Root password to use for MySQL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L229">property rootPasswordOnAllInstances</a>
</h3>

```typescript
rootPasswordOnAllInstances?: pulumi.Input<boolean>;
```


Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L233">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L237">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L241">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="NodejsAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L234">interface NodejsAppLayerArgs</a>
</h2>

The set of arguments for constructing a NodejsAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L238">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L242">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L246">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L247">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L248">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L252">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L256">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L260">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L261">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L262">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L263">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L267">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L271">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L275">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L279">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L283">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L287">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L291">property nodejsVersion</a>
</h3>

```typescript
nodejsVersion?: pulumi.Input<string>;
```


The version of NodeJS to use. Defaults to "0.10.38".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L295">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L299">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L303">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="NodejsAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L159">interface NodejsAppLayerState</a>
</h2>

Input properties used for looking up and filtering NodejsAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L163">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L167">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L171">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L172">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L173">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L177">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L181">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L185">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L186">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L187">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L188">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L192">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L196">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L200">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L204">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L208">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L212">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L216">property nodejsVersion</a>
</h3>

```typescript
nodejsVersion?: pulumi.Input<string>;
```


The version of NodeJS to use. Defaults to "0.10.38".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L220">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L224">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L228">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="PermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L104">interface PermissionArgs</a>
</h2>

The set of arguments for constructing a Permission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L108">property allowSsh</a>
</h3>

```typescript
allowSsh?: pulumi.Input<boolean>;
```


Whether the user is allowed to use SSH to communicate with the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L112">property allowSudo</a>
</h3>

```typescript
allowSudo?: pulumi.Input<boolean>;
```


Whether the user is allowed to use sudo to elevate privileges

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L116">property level</a>
</h3>

```typescript
level?: pulumi.Input<string>;
```


The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L120">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The stack to set the permissions for

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L124">property userArn</a>
</h3>

```typescript
userArn: pulumi.Input<string>;
```


The user's IAM ARN to set permissions for

<h2 class="pdoc-module-header" id="PermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L78">interface PermissionState</a>
</h2>

Input properties used for looking up and filtering Permission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L82">property allowSsh</a>
</h3>

```typescript
allowSsh?: pulumi.Input<boolean>;
```


Whether the user is allowed to use SSH to communicate with the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L86">property allowSudo</a>
</h3>

```typescript
allowSudo?: pulumi.Input<boolean>;
```


Whether the user is allowed to use sudo to elevate privileges

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L90">property level</a>
</h3>

```typescript
level?: pulumi.Input<string>;
```


The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L94">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The stack to set the permissions for

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L98">property userArn</a>
</h3>

```typescript
userArn?: pulumi.Input<string>;
```


The user's IAM ARN to set permissions for

<h2 class="pdoc-module-header" id="PhpAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L224">interface PhpAppLayerArgs</a>
</h2>

The set of arguments for constructing a PhpAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L228">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L232">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L236">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L237">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L238">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L242">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L246">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L250">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L251">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L252">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L253">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L257">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L261">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L265">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L269">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L273">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L277">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L281">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L285">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L289">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="PhpAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L153">interface PhpAppLayerState</a>
</h2>

Input properties used for looking up and filtering PhpAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L157">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L161">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L165">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L166">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L167">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L171">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L175">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L179">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L180">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L181">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L182">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L186">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L190">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L194">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L198">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L202">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L206">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L210">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L214">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L218">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RailsAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L284">interface RailsAppLayerArgs</a>
</h2>

The set of arguments for constructing a RailsAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L288">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the app server to use. Defaults to "apache_passenger".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L292">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L296">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L300">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L304">property bundlerVersion</a>
</h3>

```typescript
bundlerVersion?: pulumi.Input<string>;
```


When OpsWorks is managing Bundler, which version to use. Defaults to "1.5.3".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L305">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L306">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L310">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L314">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L318">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L319">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L320">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L321">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L325">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L329">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L333">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L337">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L341">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L345">property manageBundler</a>
</h3>

```typescript
manageBundler?: pulumi.Input<boolean>;
```


Whether OpsWorks should manage bundler. On by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L349">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L353">property passengerVersion</a>
</h3>

```typescript
passengerVersion?: pulumi.Input<string>;
```


The version of Passenger to use. Defaults to "4.0.46".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L357">property rubyVersion</a>
</h3>

```typescript
rubyVersion?: pulumi.Input<string>;
```


The version of Ruby to use. Defaults to "2.0.0".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L361">property rubygemsVersion</a>
</h3>

```typescript
rubygemsVersion?: pulumi.Input<string>;
```


The version of RubyGems to use. Defaults to "2.2.2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L365">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L369">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L373">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RailsAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L189">interface RailsAppLayerState</a>
</h2>

Input properties used for looking up and filtering RailsAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L193">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the app server to use. Defaults to "apache_passenger".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L197">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L201">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L205">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L209">property bundlerVersion</a>
</h3>

```typescript
bundlerVersion?: pulumi.Input<string>;
```


When OpsWorks is managing Bundler, which version to use. Defaults to "1.5.3".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L210">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L211">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L215">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L219">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L223">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L224">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L225">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L226">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L230">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L234">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L238">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L242">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L246">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L250">property manageBundler</a>
</h3>

```typescript
manageBundler?: pulumi.Input<boolean>;
```


Whether OpsWorks should manage bundler. On by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L254">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L258">property passengerVersion</a>
</h3>

```typescript
passengerVersion?: pulumi.Input<string>;
```


The version of Passenger to use. Defaults to "4.0.46".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L262">property rubyVersion</a>
</h3>

```typescript
rubyVersion?: pulumi.Input<string>;
```


The version of Ruby to use. Defaults to "2.0.0".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L266">property rubygemsVersion</a>
</h3>

```typescript
rubygemsVersion?: pulumi.Input<string>;
```


The version of RubyGems to use. Defaults to "2.2.2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L270">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L274">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L278">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RdsDbInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L106">interface RdsDbInstanceArgs</a>
</h2>

The set of arguments for constructing a RdsDbInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L110">property dbPassword</a>
</h3>

```typescript
dbPassword: pulumi.Input<string>;
```


A db password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L114">property dbUser</a>
</h3>

```typescript
dbUser: pulumi.Input<string>;
```


A db username

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L118">property rdsDbInstanceArn</a>
</h3>

```typescript
rdsDbInstanceArn: pulumi.Input<string>;
```


The db instance to register for this stack. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L122">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The stack to register a db inatance for. Changing this will force a new resource.

<h2 class="pdoc-module-header" id="RdsDbInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L84">interface RdsDbInstanceState</a>
</h2>

Input properties used for looking up and filtering RdsDbInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L88">property dbPassword</a>
</h3>

```typescript
dbPassword?: pulumi.Input<string>;
```


A db password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L92">property dbUser</a>
</h3>

```typescript
dbUser?: pulumi.Input<string>;
```


A db username

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L96">property rdsDbInstanceArn</a>
</h3>

```typescript
rdsDbInstanceArn?: pulumi.Input<string>;
```


The db instance to register for this stack. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L100">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The stack to register a db inatance for. Changing this will force a new resource.

<h2 class="pdoc-module-header" id="StackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L304">interface StackArgs</a>
</h2>

The set of arguments for constructing a Stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L308">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


If set to `"LATEST"`, OpsWorks will automatically install the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L312">property berkshelfVersion</a>
</h3>

```typescript
berkshelfVersion?: pulumi.Input<string>;
```


If `manage_berkshelf` is enabled, the version of Berkshelf to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L316">property color</a>
</h3>

```typescript
color?: pulumi.Input<string>;
```


Color to paint next to the stack's resources in the OpsWorks console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L320">property configurationManagerName</a>
</h3>

```typescript
configurationManagerName?: pulumi.Input<string>;
```


Name of the configuration manager to use. Defaults to "Chef".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L324">property configurationManagerVersion</a>
</h3>

```typescript
configurationManagerVersion?: pulumi.Input<string>;
```


Version of the configuration manager to use. Defaults to "11.4".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L329">property customCookbooksSources</a>
</h3>

```typescript
customCookbooksSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


When `use_custom_cookbooks` is set, provide this sub-object as
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L333">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the entire stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L338">property defaultAvailabilityZone</a>
</h3>

```typescript
defaultAvailabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L343">property defaultInstanceProfileArn</a>
</h3>

```typescript
defaultInstanceProfileArn: pulumi.Input<string>;
```


The ARN of an IAM Instance Profile that created instances
will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L347">property defaultOs</a>
</h3>

```typescript
defaultOs?: pulumi.Input<string>;
```


Name of OS that will be installed on instances by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L351">property defaultRootDeviceType</a>
</h3>

```typescript
defaultRootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L355">property defaultSshKeyName</a>
</h3>

```typescript
defaultSshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L360">property defaultSubnetId</a>
</h3>

```typescript
defaultSubnetId?: pulumi.Input<string>;
```


Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L365">property hostnameTheme</a>
</h3>

```typescript
hostnameTheme?: pulumi.Input<string>;
```


Keyword representing the naming scheme that will be used for instance hostnames
within this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L369">property manageBerkshelf</a>
</h3>

```typescript
manageBerkshelf?: pulumi.Input<boolean>;
```


Boolean value controlling whether Opsworks will run Berkshelf for this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L373">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L377">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The name of the region where the stack will exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L381">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn: pulumi.Input<string>;
```


The ARN of an IAM role that the OpsWorks service will act as.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L385">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L390">property useCustomCookbooks</a>
</h3>

```typescript
useCustomCookbooks?: pulumi.Input<boolean>;
```


Boolean value controlling whether the custom cookbook settings are
enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L395">property useOpsworksSecurityGroups</a>
</h3>

```typescript
useOpsworksSecurityGroups?: pulumi.Input<boolean>;
```


Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L399">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The id of the VPC that this stack belongs to.

<h2 class="pdoc-module-header" id="StackState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L201">interface StackState</a>
</h2>

Input properties used for looking up and filtering Stack resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L205">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


If set to `"LATEST"`, OpsWorks will automatically install the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L206">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L210">property berkshelfVersion</a>
</h3>

```typescript
berkshelfVersion?: pulumi.Input<string>;
```


If `manage_berkshelf` is enabled, the version of Berkshelf to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L214">property color</a>
</h3>

```typescript
color?: pulumi.Input<string>;
```


Color to paint next to the stack's resources in the OpsWorks console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L218">property configurationManagerName</a>
</h3>

```typescript
configurationManagerName?: pulumi.Input<string>;
```


Name of the configuration manager to use. Defaults to "Chef".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L222">property configurationManagerVersion</a>
</h3>

```typescript
configurationManagerVersion?: pulumi.Input<string>;
```


Version of the configuration manager to use. Defaults to "11.4".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L227">property customCookbooksSources</a>
</h3>

```typescript
customCookbooksSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


When `use_custom_cookbooks` is set, provide this sub-object as
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L231">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the entire stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L236">property defaultAvailabilityZone</a>
</h3>

```typescript
defaultAvailabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L241">property defaultInstanceProfileArn</a>
</h3>

```typescript
defaultInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM Instance Profile that created instances
will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L245">property defaultOs</a>
</h3>

```typescript
defaultOs?: pulumi.Input<string>;
```


Name of OS that will be installed on instances by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L249">property defaultRootDeviceType</a>
</h3>

```typescript
defaultRootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L253">property defaultSshKeyName</a>
</h3>

```typescript
defaultSshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L258">property defaultSubnetId</a>
</h3>

```typescript
defaultSubnetId?: pulumi.Input<string>;
```


Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L263">property hostnameTheme</a>
</h3>

```typescript
hostnameTheme?: pulumi.Input<string>;
```


Keyword representing the naming scheme that will be used for instance hostnames
within this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L267">property manageBerkshelf</a>
</h3>

```typescript
manageBerkshelf?: pulumi.Input<boolean>;
```


Boolean value controlling whether Opsworks will run Berkshelf for this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L271">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L275">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The name of the region where the stack will exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L279">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that the OpsWorks service will act as.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L280">property stackEndpoint</a>
</h3>

```typescript
stackEndpoint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L284">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L289">property useCustomCookbooks</a>
</h3>

```typescript
useCustomCookbooks?: pulumi.Input<boolean>;
```


Boolean value controlling whether the custom cookbook settings are
enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L294">property useOpsworksSecurityGroups</a>
</h3>

```typescript
useOpsworksSecurityGroups?: pulumi.Input<boolean>;
```


Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L298">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The id of the VPC that this stack belongs to.

<h2 class="pdoc-module-header" id="StaticWebLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L218">interface StaticWebLayerArgs</a>
</h2>

The set of arguments for constructing a StaticWebLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L222">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L226">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L230">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L231">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L232">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L236">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L237">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L241">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L242">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L243">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L244">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L248">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L252">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L256">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L260">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L264">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L268">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L272">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L276">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L280">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="StaticWebLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L150">interface StaticWebLayerState</a>
</h2>

Input properties used for looking up and filtering StaticWebLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L154">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L158">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L162">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L163">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L164">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L168">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L169">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L173">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L174">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L175">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L176">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L180">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L184">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L188">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L192">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L196">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L200">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L204">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L208">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L212">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="UserProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L97">interface UserProfileArgs</a>
</h2>

The set of arguments for constructing a UserProfile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L101">property allowSelfManagement</a>
</h3>

```typescript
allowSelfManagement?: pulumi.Input<boolean>;
```


Whether users can specify their own SSH public key through the My Settings page

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L105">property sshPublicKey</a>
</h3>

```typescript
sshPublicKey?: pulumi.Input<string>;
```


The users public key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L109">property sshUsername</a>
</h3>

```typescript
sshUsername: pulumi.Input<string>;
```


The ssh username, with witch this user wants to log in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L113">property userArn</a>
</h3>

```typescript
userArn: pulumi.Input<string>;
```


The user's IAM ARN

<h2 class="pdoc-module-header" id="UserProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L75">interface UserProfileState</a>
</h2>

Input properties used for looking up and filtering UserProfile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L79">property allowSelfManagement</a>
</h3>

```typescript
allowSelfManagement?: pulumi.Input<boolean>;
```


Whether users can specify their own SSH public key through the My Settings page

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L83">property sshPublicKey</a>
</h3>

```typescript
sshPublicKey?: pulumi.Input<string>;
```


The users public key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L87">property sshUsername</a>
</h3>

```typescript
sshUsername?: pulumi.Input<string>;
```


The ssh username, with witch this user wants to log in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L91">property userArn</a>
</h3>

```typescript
userArn?: pulumi.Input<string>;
```


The user's IAM ARN

