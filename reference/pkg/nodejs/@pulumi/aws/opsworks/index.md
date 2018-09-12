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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L10">class Application</a>
</h2>

Provides an OpsWorks application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L90">constructor</a>
</h3>

```typescript
new Application(name: string, args: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L26">property appSources</a>
</h3>

```typescript
public appSources: pulumi.Output<{ ... }[]>;
```


SCM configuration of the app as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L30">property autoBundleOnDeploy</a>
</h3>

```typescript
public autoBundleOnDeploy: pulumi.Output<string | undefined>;
```


Run bundle install when deploying for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L34">property awsFlowRubySettings</a>
</h3>

```typescript
public awsFlowRubySettings: pulumi.Output<string | undefined>;
```


Specify activity and workflow workers for your app using the aws-flow gem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L38">property dataSourceArn</a>
</h3>

```typescript
public dataSourceArn: pulumi.Output<string | undefined>;
```


The data source's ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L42">property dataSourceDatabaseName</a>
</h3>

```typescript
public dataSourceDatabaseName: pulumi.Output<string | undefined>;
```


The database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L46">property dataSourceType</a>
</h3>

```typescript
public dataSourceType: pulumi.Output<string | undefined>;
```


The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L50">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L54">property documentRoot</a>
</h3>

```typescript
public documentRoot: pulumi.Output<string | undefined>;
```


Subfolder for the document root for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L58">property domains</a>
</h3>

```typescript
public domains: pulumi.Output<string[] | undefined>;
```


A list of virtual host alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L62">property enableSsl</a>
</h3>

```typescript
public enableSsl: pulumi.Output<boolean | undefined>;
```


Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L66">property environments</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L70">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L74">property railsEnv</a>
</h3>

```typescript
public railsEnv: pulumi.Output<string | undefined>;
```


The name of the Rails environment for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L78">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L82">property sslConfigurations</a>
</h3>

```typescript
public sslConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


The SSL configuration of the app. Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L86">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the application will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L90">property type</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L10">class CustomLayer</a>
</h2>

Provides an OpsWorks custom layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L91">constructor</a>
</h3>

```typescript
new CustomLayer(name: string, args: CustomLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CustomLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L26">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L30">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L34">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L35">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L36">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L40">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L44">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L48">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L49">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L50">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L51">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L55">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L59">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L63">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L67">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L71">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L79">property shortName</a>
</h3>

```typescript
public shortName: pulumi.Output<string>;
```


A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L83">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L87">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L91">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="GangliaLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L10">class GangliaLayer</a>
</h2>

Provides an OpsWorks Ganglia layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L99">constructor</a>
</h3>

```typescript
new GangliaLayer(name: string, args: GangliaLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GangliaLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L26">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L30">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L34">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L35">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L36">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L40">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L44">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L48">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L49">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L50">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L51">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L55">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L59">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L63">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L67">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L71">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L79">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The password to use for Ganglia.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L83">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L87">property systemPackages</a>
</h3>

```typescript
public systemPackages: pulumi.Output<string[] | undefined>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L91">property url</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L95">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L99">property username</a>
</h3>

```typescript
public username: pulumi.Output<string | undefined>;
```


The username to use for Ganglia. Defaults to "opsworks".

<h2 class="pdoc-module-header" id="HaproxyLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L10">class HaproxyLayer</a>
</h2>

Provides an OpsWorks haproxy layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L111">constructor</a>
</h3>

```typescript
new HaproxyLayer(name: string, args: HaproxyLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a HaproxyLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L26">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L30">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L34">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L35">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L36">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L40">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L44">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L48">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L49">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L50">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L51">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L55">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L59">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L63">property elasticLoadBalancer</a>
</h3>

```typescript
public elasticLoadBalancer: pulumi.Output<string | undefined>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L67">property healthcheckMethod</a>
</h3>

```typescript
public healthcheckMethod: pulumi.Output<string | undefined>;
```


HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L71">property healthcheckUrl</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L75">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L79">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L83">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L87">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L91">property statsEnabled</a>
</h3>

```typescript
public statsEnabled: pulumi.Output<boolean | undefined>;
```


Whether to enable HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L95">property statsPassword</a>
</h3>

```typescript
public statsPassword: pulumi.Output<string>;
```


The password to use for HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L99">property statsUrl</a>
</h3>

```typescript
public statsUrl: pulumi.Output<string | undefined>;
```


The HAProxy stats URL. Defaults to "/haproxy?stats".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L103">property statsUser</a>
</h3>

```typescript
public statsUser: pulumi.Output<string | undefined>;
```


The username for HAProxy stats. Defaults to "opsworks".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L107">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L111">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L10">class Instance</a>
</h2>

Provides an OpsWorks instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L156">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L26">property agentVersion</a>
</h3>

```typescript
public agentVersion: pulumi.Output<string | undefined>;
```


The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L30">property amiId</a>
</h3>

```typescript
public amiId: pulumi.Output<string>;
```


The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L34">property architecture</a>
</h3>

```typescript
public architecture: pulumi.Output<string | undefined>;
```


Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L38">property autoScalingType</a>
</h3>

```typescript
public autoScalingType: pulumi.Output<string | undefined>;
```


Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L43">property availabilityZone</a>
</h3>

```typescript
public availabilityZone: pulumi.Output<string>;
```


Name of the availability zone where instances will be created
by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L44">property createdAt</a>
</h3>

```typescript
public createdAt: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L45">property deleteEbs</a>
</h3>

```typescript
public deleteEbs: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L46">property deleteEip</a>
</h3>

```typescript
public deleteEip: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L51">property ebsBlockDevices</a>
</h3>

```typescript
public ebsBlockDevices: pulumi.Output<{ ... }[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L55">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean | undefined>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L59">property ec2InstanceId</a>
</h3>

```typescript
public ec2InstanceId: pulumi.Output<string>;
```


EC2 instance ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L60">property ecsClusterArn</a>
</h3>

```typescript
public ecsClusterArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L61">property elasticIp</a>
</h3>

```typescript
public elasticIp: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L66">property ephemeralBlockDevices</a>
</h3>

```typescript
public ephemeralBlockDevices: pulumi.Output<{ ... }[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L70">property hostname</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L71">property infrastructureClass</a>
</h3>

```typescript
public infrastructureClass: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L75">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L76">property instanceProfileArn</a>
</h3>

```typescript
public instanceProfileArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L80">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string | undefined>;
```


The type of instance to start

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L81">property lastServiceErrorId</a>
</h3>

```typescript
public lastServiceErrorId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L85">property layerIds</a>
</h3>

```typescript
public layerIds: pulumi.Output<string[]>;
```


The ids of the layers the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L89">property os</a>
</h3>

```typescript
public os: pulumi.Output<string>;
```


Name of operating system that will be installed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L90">property platform</a>
</h3>

```typescript
public platform: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L96">property privateDns</a>
</h3>

```typescript
public privateDns: pulumi.Output<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L100">property privateIp</a>
</h3>

```typescript
public privateIp: pulumi.Output<string>;
```


The private IP address assigned to the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L105">property publicDns</a>
</h3>

```typescript
public publicDns: pulumi.Output<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L109">property publicIp</a>
</h3>

```typescript
public publicIp: pulumi.Output<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L110">property registeredBy</a>
</h3>

```typescript
public registeredBy: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L111">property reportedAgentVersion</a>
</h3>

```typescript
public reportedAgentVersion: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L112">property reportedOsFamily</a>
</h3>

```typescript
public reportedOsFamily: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L113">property reportedOsName</a>
</h3>

```typescript
public reportedOsName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L114">property reportedOsVersion</a>
</h3>

```typescript
public reportedOsVersion: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L119">property rootBlockDevices</a>
</h3>

```typescript
public rootBlockDevices: pulumi.Output<{ ... }[]>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L123">property rootDeviceType</a>
</h3>

```typescript
public rootDeviceType: pulumi.Output<string>;
```


Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L124">property rootDeviceVolumeId</a>
</h3>

```typescript
public rootDeviceVolumeId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L128">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string[]>;
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L129">property sshHostDsaKeyFingerprint</a>
</h3>

```typescript
public sshHostDsaKeyFingerprint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L130">property sshHostRsaKeyFingerprint</a>
</h3>

```typescript
public sshHostRsaKeyFingerprint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L134">property sshKeyName</a>
</h3>

```typescript
public sshKeyName: pulumi.Output<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L138">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L142">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


The desired state of the instance.  Can be either `"running"` or `"stopped"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L143">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L147">property subnetId</a>
</h3>

```typescript
public subnetId: pulumi.Output<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L151">property tenancy</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L156">property virtualizationType</a>
</h3>

```typescript
public virtualizationType: pulumi.Output<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

<h2 class="pdoc-module-header" id="JavaAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L10">class JavaAppLayer</a>
</h2>

Provides an OpsWorks Java application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L107">constructor</a>
</h3>

```typescript
new JavaAppLayer(name: string, args: JavaAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a JavaAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L26">property appServer</a>
</h3>

```typescript
public appServer: pulumi.Output<string | undefined>;
```


Keyword for the application container to use. Defaults to "tomcat".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L30">property appServerVersion</a>
</h3>

```typescript
public appServerVersion: pulumi.Output<string | undefined>;
```


Version of the selected application container to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L34">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L38">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L42">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L43">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L44">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L48">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L52">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L56">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L57">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L58">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L59">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L63">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L67">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L71">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L75">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L79">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L83">property jvmOptions</a>
</h3>

```typescript
public jvmOptions: pulumi.Output<string | undefined>;
```


Options to set for the JVM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L87">property jvmType</a>
</h3>

```typescript
public jvmType: pulumi.Output<string | undefined>;
```


Keyword for the type of JVM to use. Defaults to `openjdk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L91">property jvmVersion</a>
</h3>

```typescript
public jvmVersion: pulumi.Output<string | undefined>;
```


Version of JVM to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L95">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L99">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L103">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L107">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MemcachedLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L10">class MemcachedLayer</a>
</h2>

Provides an OpsWorks memcached layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L91">constructor</a>
</h3>

```typescript
new MemcachedLayer(name: string, args: MemcachedLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MemcachedLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L26">property allocatedMemory</a>
</h3>

```typescript
public allocatedMemory: pulumi.Output<number | undefined>;
```


Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L30">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L34">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L38">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L39">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L40">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L44">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L48">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L52">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L53">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L54">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L55">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L59">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L63">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L67">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L71">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L75">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L79">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L83">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L87">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L91">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MysqlLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L13">class MysqlLayer</a>
</h2>

Provides an OpsWorks MySQL layer resource.

~> **Note:** All arguments including the root password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L98">constructor</a>
</h3>

```typescript
new MysqlLayer(name: string, args: MysqlLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a MysqlLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L22">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L29">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L33">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L37">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L38">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L39">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L43">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L47">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L51">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L52">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L53">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L54">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L58">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L62">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L66">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L70">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L74">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L78">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L82">property rootPassword</a>
</h3>

```typescript
public rootPassword: pulumi.Output<string | undefined>;
```


Root password to use for MySQL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L86">property rootPasswordOnAllInstances</a>
</h3>

```typescript
public rootPasswordOnAllInstances: pulumi.Output<boolean | undefined>;
```


Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L90">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L94">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L98">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="NodejsAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L10">class NodejsAppLayer</a>
</h2>

Provides an OpsWorks NodeJS application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L91">constructor</a>
</h3>

```typescript
new NodejsAppLayer(name: string, args: NodejsAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a NodejsAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L26">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L30">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L34">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L35">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L36">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L40">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L44">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L48">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L49">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L50">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L51">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L55">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L59">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L63">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L67">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L71">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L79">property nodejsVersion</a>
</h3>

```typescript
public nodejsVersion: pulumi.Output<string | undefined>;
```


The version of NodeJS to use. Defaults to "0.10.38".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L83">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L87">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L91">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="Permission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L10">class Permission</a>
</h2>

Provides an OpsWorks permission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L42">constructor</a>
</h3>

```typescript
new Permission(name: string, args: PermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Permission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L26">property allowSsh</a>
</h3>

```typescript
public allowSsh: pulumi.Output<boolean>;
```


Whether the user is allowed to use SSH to communicate with the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L30">property allowSudo</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L34">property level</a>
</h3>

```typescript
public level: pulumi.Output<string>;
```


The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L38">property stackId</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L42">property userArn</a>
</h3>

```typescript
public userArn: pulumi.Output<string>;
```


The user's IAM ARN to set permissions for

<h2 class="pdoc-module-header" id="PhpAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L10">class PhpAppLayer</a>
</h2>

Provides an OpsWorks PHP application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L87">constructor</a>
</h3>

```typescript
new PhpAppLayer(name: string, args: PhpAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a PhpAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L26">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L30">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L34">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L35">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L36">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L40">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L44">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L48">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L49">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L50">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L51">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L55">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L59">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L63">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L67">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L71">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L79">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L83">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L87">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RailsAppLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L10">class RailsAppLayer</a>
</h2>

Provides an OpsWorks Ruby on Rails application layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L111">constructor</a>
</h3>

```typescript
new RailsAppLayer(name: string, args: RailsAppLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RailsAppLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L26">property appServer</a>
</h3>

```typescript
public appServer: pulumi.Output<string | undefined>;
```


Keyword for the app server to use. Defaults to "apache_passenger".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L30">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L34">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L38">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L42">property bundlerVersion</a>
</h3>

```typescript
public bundlerVersion: pulumi.Output<string | undefined>;
```


When OpsWorks is managing Bundler, which version to use. Defaults to "1.5.3".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L43">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L44">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L48">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L52">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L56">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L57">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L58">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L59">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L63">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L67">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L71">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L75">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L79">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L83">property manageBundler</a>
</h3>

```typescript
public manageBundler: pulumi.Output<boolean | undefined>;
```


Whether OpsWorks should manage bundler. On by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L87">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L91">property passengerVersion</a>
</h3>

```typescript
public passengerVersion: pulumi.Output<string | undefined>;
```


The version of Passenger to use. Defaults to "4.0.46".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L95">property rubyVersion</a>
</h3>

```typescript
public rubyVersion: pulumi.Output<string | undefined>;
```


The version of Ruby to use. Defaults to "2.0.0".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L99">property rubygemsVersion</a>
</h3>

```typescript
public rubygemsVersion: pulumi.Output<string | undefined>;
```


The version of RubyGems to use. Defaults to "2.2.2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L103">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L107">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L111">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RdsDbInstance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L13">class RdsDbInstance</a>
</h2>

Provides an OpsWorks RDS DB Instance resource.

~> **Note:** All arguments including the username and password will be stored in the raw state as plain-text.
[Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L41">constructor</a>
</h3>

```typescript
new RdsDbInstance(name: string, args: RdsDbInstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RdsDbInstance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L22">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L29">property dbPassword</a>
</h3>

```typescript
public dbPassword: pulumi.Output<string>;
```


A db password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L33">property dbUser</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L37">property rdsDbInstanceArn</a>
</h3>

```typescript
public rdsDbInstanceArn: pulumi.Output<string>;
```


The db instance to register for this stack. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L41">property stackId</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L12">class Stack</a>
</h2>

Provides an OpsWorks stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L121">constructor</a>
</h3>

```typescript
new Stack(name: string, args: StackArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Stack resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L21">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L28">property agentVersion</a>
</h3>

```typescript
public agentVersion: pulumi.Output<string>;
```


If set to `"LATEST"`, OpsWorks will automatically install the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L33">property berkshelfVersion</a>
</h3>

```typescript
public berkshelfVersion: pulumi.Output<string | undefined>;
```


If `manage_berkshelf` is enabled, the version of Berkshelf to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L37">property color</a>
</h3>

```typescript
public color: pulumi.Output<string | undefined>;
```


Color to paint next to the stack's resources in the OpsWorks console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L41">property configurationManagerName</a>
</h3>

```typescript
public configurationManagerName: pulumi.Output<string | undefined>;
```


Name of the configuration manager to use. Defaults to "Chef".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L45">property configurationManagerVersion</a>
</h3>

```typescript
public configurationManagerVersion: pulumi.Output<string | undefined>;
```


Version of the configuration manager to use. Defaults to "11.4".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L50">property customCookbooksSources</a>
</h3>

```typescript
public customCookbooksSources: pulumi.Output<{ ... }[]>;
```


When `use_custom_cookbooks` is set, provide this sub-object as
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L54">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```


Custom JSON attributes to apply to the entire stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L59">property defaultAvailabilityZone</a>
</h3>

```typescript
public defaultAvailabilityZone: pulumi.Output<string>;
```


Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L64">property defaultInstanceProfileArn</a>
</h3>

```typescript
public defaultInstanceProfileArn: pulumi.Output<string>;
```


The ARN of an IAM Instance Profile that created instances
will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L68">property defaultOs</a>
</h3>

```typescript
public defaultOs: pulumi.Output<string | undefined>;
```


Name of OS that will be installed on instances by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L72">property defaultRootDeviceType</a>
</h3>

```typescript
public defaultRootDeviceType: pulumi.Output<string | undefined>;
```


Name of the type of root device instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L76">property defaultSshKeyName</a>
</h3>

```typescript
public defaultSshKeyName: pulumi.Output<string | undefined>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L81">property defaultSubnetId</a>
</h3>

```typescript
public defaultSubnetId: pulumi.Output<string>;
```


Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L86">property hostnameTheme</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L90">property manageBerkshelf</a>
</h3>

```typescript
public manageBerkshelf: pulumi.Output<boolean | undefined>;
```


Boolean value controlling whether Opsworks will run Berkshelf for this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L94">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L98">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The name of the region where the stack will exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L102">property serviceRoleArn</a>
</h3>

```typescript
public serviceRoleArn: pulumi.Output<string>;
```


The ARN of an IAM role that the OpsWorks service will act as.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L103">property stackEndpoint</a>
</h3>

```typescript
public stackEndpoint: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L107">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L112">property useCustomCookbooks</a>
</h3>

```typescript
public useCustomCookbooks: pulumi.Output<boolean | undefined>;
```


Boolean value controlling whether the custom cookbook settings are
enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L117">property useOpsworksSecurityGroups</a>
</h3>

```typescript
public useOpsworksSecurityGroups: pulumi.Output<boolean | undefined>;
```


Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L121">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The id of the VPC that this stack belongs to.

<h2 class="pdoc-module-header" id="StaticWebLayer">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L10">class StaticWebLayer</a>
</h2>

Provides an OpsWorks static web server layer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L84">constructor</a>
</h3>

```typescript
new StaticWebLayer(name: string, args: StaticWebLayerArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StaticWebLayer resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L26">property autoAssignElasticIps</a>
</h3>

```typescript
public autoAssignElasticIps: pulumi.Output<boolean | undefined>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L30">property autoAssignPublicIps</a>
</h3>

```typescript
public autoAssignPublicIps: pulumi.Output<boolean | undefined>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L34">property autoHealing</a>
</h3>

```typescript
public autoHealing: pulumi.Output<boolean | undefined>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L35">property customConfigureRecipes</a>
</h3>

```typescript
public customConfigureRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L36">property customDeployRecipes</a>
</h3>

```typescript
public customDeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L40">property customInstanceProfileArn</a>
</h3>

```typescript
public customInstanceProfileArn: pulumi.Output<string | undefined>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L41">property customJson</a>
</h3>

```typescript
public customJson: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L45">property customSecurityGroupIds</a>
</h3>

```typescript
public customSecurityGroupIds: pulumi.Output<string[] | undefined>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L46">property customSetupRecipes</a>
</h3>

```typescript
public customSetupRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L47">property customShutdownRecipes</a>
</h3>

```typescript
public customShutdownRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L48">property customUndeployRecipes</a>
</h3>

```typescript
public customUndeployRecipes: pulumi.Output<string[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L52">property drainElbOnShutdown</a>
</h3>

```typescript
public drainElbOnShutdown: pulumi.Output<boolean | undefined>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L56">property ebsVolumes</a>
</h3>

```typescript
public ebsVolumes: pulumi.Output<{ ... }[] | undefined>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L60">property elasticLoadBalancer</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L64">property installUpdatesOnBoot</a>
</h3>

```typescript
public installUpdatesOnBoot: pulumi.Output<boolean | undefined>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L68">property instanceShutdownTimeout</a>
</h3>

```typescript
public instanceShutdownTimeout: pulumi.Output<number | undefined>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L72">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L76">property stackId</a>
</h3>

```typescript
public stackId: pulumi.Output<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L80">property systemPackages</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L84">property useEbsOptimizedInstances</a>
</h3>

```typescript
public useEbsOptimizedInstances: pulumi.Output<boolean | undefined>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="UserProfile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L10">class UserProfile</a>
</h2>

Provides an OpsWorks User Profile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L38">constructor</a>
</h3>

```typescript
new UserProfile(name: string, args: UserProfileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a UserProfile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L26">property allowSelfManagement</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L30">property sshPublicKey</a>
</h3>

```typescript
public sshPublicKey: pulumi.Output<string | undefined>;
```


The users public key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L34">property sshUsername</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L38">property userArn</a>
</h3>

```typescript
public userArn: pulumi.Output<string>;
```


The user's IAM ARN

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L228">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L232">property appSources</a>
</h3>

```typescript
appSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


SCM configuration of the app as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L236">property autoBundleOnDeploy</a>
</h3>

```typescript
autoBundleOnDeploy?: pulumi.Input<string>;
```


Run bundle install when deploying for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L240">property awsFlowRubySettings</a>
</h3>

```typescript
awsFlowRubySettings?: pulumi.Input<string>;
```


Specify activity and workflow workers for your app using the aws-flow gem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L244">property dataSourceArn</a>
</h3>

```typescript
dataSourceArn?: pulumi.Input<string>;
```


The data source's ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L248">property dataSourceDatabaseName</a>
</h3>

```typescript
dataSourceDatabaseName?: pulumi.Input<string>;
```


The database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L252">property dataSourceType</a>
</h3>

```typescript
dataSourceType?: pulumi.Input<string>;
```


The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L256">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L260">property documentRoot</a>
</h3>

```typescript
documentRoot?: pulumi.Input<string>;
```


Subfolder for the document root for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L264">property domains</a>
</h3>

```typescript
domains?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual host alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L268">property enableSsl</a>
</h3>

```typescript
enableSsl?: pulumi.Input<boolean>;
```


Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L272">property environments</a>
</h3>

```typescript
environments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Object to define environment variables.  Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L276">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L280">property railsEnv</a>
</h3>

```typescript
railsEnv?: pulumi.Input<string>;
```


The name of the Rails environment for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L284">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L288">property sslConfigurations</a>
</h3>

```typescript
sslConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The SSL configuration of the app. Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L292">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the application will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L296">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of source to use. For example, "archive".

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L154">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L158">property appSources</a>
</h3>

```typescript
appSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


SCM configuration of the app as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L162">property autoBundleOnDeploy</a>
</h3>

```typescript
autoBundleOnDeploy?: pulumi.Input<string>;
```


Run bundle install when deploying for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L166">property awsFlowRubySettings</a>
</h3>

```typescript
awsFlowRubySettings?: pulumi.Input<string>;
```


Specify activity and workflow workers for your app using the aws-flow gem.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L170">property dataSourceArn</a>
</h3>

```typescript
dataSourceArn?: pulumi.Input<string>;
```


The data source's ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L174">property dataSourceDatabaseName</a>
</h3>

```typescript
dataSourceDatabaseName?: pulumi.Input<string>;
```


The database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L178">property dataSourceType</a>
</h3>

```typescript
dataSourceType?: pulumi.Input<string>;
```


The data source's type one of `AutoSelectOpsworksMysqlInstance`, `OpsworksMysqlInstance`, or `RdsDbInstance`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L182">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the app.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L186">property documentRoot</a>
</h3>

```typescript
documentRoot?: pulumi.Input<string>;
```


Subfolder for the document root for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L190">property domains</a>
</h3>

```typescript
domains?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of virtual host alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L194">property enableSsl</a>
</h3>

```typescript
enableSsl?: pulumi.Input<boolean>;
```


Whether to enable SSL for the app. This must be set in order to let `ssl_configuration.private_key`, `ssl_configuration.certificate` and `ssl_configuration.chain` take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L198">property environments</a>
</h3>

```typescript
environments?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Object to define environment variables.  Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L202">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L206">property railsEnv</a>
</h3>

```typescript
railsEnv?: pulumi.Input<string>;
```


The name of the Rails environment for application of type `rails`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L210">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


A short, machine-readable name for the application. This can only be defined on resource creation and ignored on resource update.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L214">property sslConfigurations</a>
</h3>

```typescript
sslConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


The SSL configuration of the app. Object is described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L218">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the application will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/application.ts#L222">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of source to use. For example, "archive".

<h2 class="pdoc-module-header" id="CustomLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L238">interface CustomLayerArgs</a>
</h2>

The set of arguments for constructing a CustomLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L242">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L246">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L250">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L251">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L252">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L256">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L260">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L264">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L265">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L266">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L267">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L271">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L275">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L279">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L283">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L287">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L291">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L295">property shortName</a>
</h3>

```typescript
shortName: pulumi.Input<string>;
```


A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L299">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L303">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L307">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="CustomLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L163">interface CustomLayerState</a>
</h2>

Input properties used for looking up and filtering CustomLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L167">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L171">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L175">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L176">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L177">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L181">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L185">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L189">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L190">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L191">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L192">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L196">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L200">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L204">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L208">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L212">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L216">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L220">property shortName</a>
</h3>

```typescript
shortName?: pulumi.Input<string>;
```


A short, machine-readable name for the layer, which will be used to identify it in the Chef node JSON.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L224">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L228">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/customLayer.ts#L232">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="GangliaLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L258">interface GangliaLayerArgs</a>
</h2>

The set of arguments for constructing a GangliaLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L262">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L266">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L270">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L271">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L272">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L276">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L280">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L284">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L285">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L286">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L287">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L291">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L295">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L299">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L303">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L307">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L311">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L315">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The password to use for Ganglia.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L319">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L323">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L327">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL path to use for Ganglia. Defaults to "/ganglia".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L331">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L335">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The username to use for Ganglia. Defaults to "opsworks".

<h2 class="pdoc-module-header" id="GangliaLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L175">interface GangliaLayerState</a>
</h2>

Input properties used for looking up and filtering GangliaLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L179">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L183">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L187">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L188">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L189">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L193">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L197">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L201">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L202">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L203">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L204">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L208">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L212">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L216">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L220">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L224">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L228">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L232">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password to use for Ganglia.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L236">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L240">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L244">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The URL path to use for Ganglia. Defaults to "/ganglia".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L248">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/gangliaLayer.ts#L252">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The username to use for Ganglia. Defaults to "opsworks".

<h2 class="pdoc-module-header" id="HaproxyLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L288">interface HaproxyLayerArgs</a>
</h2>

The set of arguments for constructing a HaproxyLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L292">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L296">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L300">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L301">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L302">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L306">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L310">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L314">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L315">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L316">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L317">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L321">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L325">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L329">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L333">property healthcheckMethod</a>
</h3>

```typescript
healthcheckMethod?: pulumi.Input<string>;
```


HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L337">property healthcheckUrl</a>
</h3>

```typescript
healthcheckUrl?: pulumi.Input<string>;
```


URL path to use for instance healthchecks. Defaults to "/".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L341">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L345">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L349">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L353">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L357">property statsEnabled</a>
</h3>

```typescript
statsEnabled?: pulumi.Input<boolean>;
```


Whether to enable HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L361">property statsPassword</a>
</h3>

```typescript
statsPassword: pulumi.Input<string>;
```


The password to use for HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L365">property statsUrl</a>
</h3>

```typescript
statsUrl?: pulumi.Input<string>;
```


The HAProxy stats URL. Defaults to "/haproxy?stats".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L369">property statsUser</a>
</h3>

```typescript
statsUser?: pulumi.Input<string>;
```


The username for HAProxy stats. Defaults to "opsworks".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L373">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L377">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="HaproxyLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L193">interface HaproxyLayerState</a>
</h2>

Input properties used for looking up and filtering HaproxyLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L197">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L201">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L205">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L206">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L207">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L211">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L215">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L219">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L220">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L221">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L222">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L226">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L230">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L234">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L238">property healthcheckMethod</a>
</h3>

```typescript
healthcheckMethod?: pulumi.Input<string>;
```


HTTP method to use for instance healthchecks. Defaults to "OPTIONS".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L242">property healthcheckUrl</a>
</h3>

```typescript
healthcheckUrl?: pulumi.Input<string>;
```


URL path to use for instance healthchecks. Defaults to "/".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L246">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L250">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L254">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L258">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L262">property statsEnabled</a>
</h3>

```typescript
statsEnabled?: pulumi.Input<boolean>;
```


Whether to enable HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L266">property statsPassword</a>
</h3>

```typescript
statsPassword?: pulumi.Input<string>;
```


The password to use for HAProxy stats.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L270">property statsUrl</a>
</h3>

```typescript
statsUrl?: pulumi.Input<string>;
```


The HAProxy stats URL. Defaults to "/haproxy?stats".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L274">property statsUser</a>
</h3>

```typescript
statsUser?: pulumi.Input<string>;
```


The username for HAProxy stats. Defaults to "opsworks".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L278">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/haproxyLayer.ts#L282">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L416">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L420">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L424">property amiId</a>
</h3>

```typescript
amiId?: pulumi.Input<string>;
```


The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L428">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L432">property autoScalingType</a>
</h3>

```typescript
autoScalingType?: pulumi.Input<string>;
```


Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L437">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L438">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L439">property deleteEbs</a>
</h3>

```typescript
deleteEbs?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L440">property deleteEip</a>
</h3>

```typescript
deleteEip?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L445">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L449">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L450">property ecsClusterArn</a>
</h3>

```typescript
ecsClusterArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L451">property elasticIp</a>
</h3>

```typescript
elasticIp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L456">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L460">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The instance's host name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L461">property infrastructureClass</a>
</h3>

```typescript
infrastructureClass?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L465">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L466">property instanceProfileArn</a>
</h3>

```typescript
instanceProfileArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L470">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of instance to start

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L471">property lastServiceErrorId</a>
</h3>

```typescript
lastServiceErrorId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L475">property layerIds</a>
</h3>

```typescript
layerIds: pulumi.Input<pulumi.Input<string>[]>;
```


The ids of the layers the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L479">property os</a>
</h3>

```typescript
os?: pulumi.Input<string>;
```


Name of operating system that will be installed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L480">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L486">property privateDns</a>
</h3>

```typescript
privateDns?: pulumi.Input<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L490">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


The private IP address assigned to the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L495">property publicDns</a>
</h3>

```typescript
publicDns?: pulumi.Input<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L499">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L500">property registeredBy</a>
</h3>

```typescript
registeredBy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L501">property reportedAgentVersion</a>
</h3>

```typescript
reportedAgentVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L502">property reportedOsFamily</a>
</h3>

```typescript
reportedOsFamily?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L503">property reportedOsName</a>
</h3>

```typescript
reportedOsName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L504">property reportedOsVersion</a>
</h3>

```typescript
reportedOsVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L509">property rootBlockDevices</a>
</h3>

```typescript
rootBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L513">property rootDeviceType</a>
</h3>

```typescript
rootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L514">property rootDeviceVolumeId</a>
</h3>

```typescript
rootDeviceVolumeId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L518">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L519">property sshHostDsaKeyFingerprint</a>
</h3>

```typescript
sshHostDsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L520">property sshHostRsaKeyFingerprint</a>
</h3>

```typescript
sshHostRsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L524">property sshKeyName</a>
</h3>

```typescript
sshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L528">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L532">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The desired state of the instance.  Can be either `"running"` or `"stopped"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L533">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L537">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L541">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L546">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L276">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L280">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


The AWS OpsWorks agent to install.  Defaults to `"INHERIT"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L284">property amiId</a>
</h3>

```typescript
amiId?: pulumi.Input<string>;
```


The AMI to use for the instance.  If an AMI is specified, `os` must be `"Custom"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L288">property architecture</a>
</h3>

```typescript
architecture?: pulumi.Input<string>;
```


Machine architecture for created instances.  Can be either `"x86_64"` (the default) or `"i386"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L292">property autoScalingType</a>
</h3>

```typescript
autoScalingType?: pulumi.Input<string>;
```


Creates load-based or time-based instances.  If set, can be either: `"load"` or `"timer"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L297">property availabilityZone</a>
</h3>

```typescript
availabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L298">property createdAt</a>
</h3>

```typescript
createdAt?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L299">property deleteEbs</a>
</h3>

```typescript
deleteEbs?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L300">property deleteEip</a>
</h3>

```typescript
deleteEip?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L305">property ebsBlockDevices</a>
</h3>

```typescript
ebsBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Additional EBS block devices to attach to the
instance.  See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L309">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


If true, the launched EC2 instance will be EBS-optimized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L313">property ec2InstanceId</a>
</h3>

```typescript
ec2InstanceId?: pulumi.Input<string>;
```


EC2 instance ID

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L314">property ecsClusterArn</a>
</h3>

```typescript
ecsClusterArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L315">property elasticIp</a>
</h3>

```typescript
elasticIp?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L320">property ephemeralBlockDevices</a>
</h3>

```typescript
ephemeralBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize Ephemeral (also known as
"Instance Store") volumes on the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L324">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The instance's host name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L325">property infrastructureClass</a>
</h3>

```typescript
infrastructureClass?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L329">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Controls where to install OS and package updates when the instance boots.  Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L330">property instanceProfileArn</a>
</h3>

```typescript
instanceProfileArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L334">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The type of instance to start

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L335">property lastServiceErrorId</a>
</h3>

```typescript
lastServiceErrorId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L339">property layerIds</a>
</h3>

```typescript
layerIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The ids of the layers the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L343">property os</a>
</h3>

```typescript
os?: pulumi.Input<string>;
```


Name of operating system that will be installed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L344">property platform</a>
</h3>

```typescript
platform?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L350">property privateDns</a>
</h3>

```typescript
privateDns?: pulumi.Input<string>;
```


The private DNS name assigned to the instance. Can only be
used inside the Amazon EC2, and only available if you've enabled DNS hostnames
for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L354">property privateIp</a>
</h3>

```typescript
privateIp?: pulumi.Input<string>;
```


The private IP address assigned to the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L359">property publicDns</a>
</h3>

```typescript
publicDns?: pulumi.Input<string>;
```


The public DNS name assigned to the instance. For EC2-VPC, this
is only available if you've enabled DNS hostnames for your VPC

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L363">property publicIp</a>
</h3>

```typescript
publicIp?: pulumi.Input<string>;
```


The public IP address assigned to the instance, if applicable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L364">property registeredBy</a>
</h3>

```typescript
registeredBy?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L365">property reportedAgentVersion</a>
</h3>

```typescript
reportedAgentVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L366">property reportedOsFamily</a>
</h3>

```typescript
reportedOsFamily?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L367">property reportedOsName</a>
</h3>

```typescript
reportedOsName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L368">property reportedOsVersion</a>
</h3>

```typescript
reportedOsVersion?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L373">property rootBlockDevices</a>
</h3>

```typescript
rootBlockDevices?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Customize details about the root block
device of the instance. See Block Devices below for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L377">property rootDeviceType</a>
</h3>

```typescript
rootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.  Can be either `"ebs"` or `"instance-store"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L378">property rootDeviceVolumeId</a>
</h3>

```typescript
rootDeviceVolumeId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L382">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


The associated security groups.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L383">property sshHostDsaKeyFingerprint</a>
</h3>

```typescript
sshHostDsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L384">property sshHostRsaKeyFingerprint</a>
</h3>

```typescript
sshHostRsaKeyFingerprint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L388">property sshKeyName</a>
</h3>

```typescript
sshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L392">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the instance will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L396">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The desired state of the instance.  Can be either `"running"` or `"stopped"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L397">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L401">property subnetId</a>
</h3>

```typescript
subnetId?: pulumi.Input<string>;
```


Subnet ID to attach to

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L405">property tenancy</a>
</h3>

```typescript
tenancy?: pulumi.Input<string>;
```


Instance tenancy to use. Can be one of `"default"`, `"dedicated"` or `"host"`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/instance.ts#L410">property virtualizationType</a>
</h3>

```typescript
virtualizationType?: pulumi.Input<string>;
```


Keyword to choose what virtualization mode created instances
will use. Can be either `"paravirtual"` or `"hvm"`.

<h2 class="pdoc-module-header" id="JavaAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L275">interface JavaAppLayerArgs</a>
</h2>

The set of arguments for constructing a JavaAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L279">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the application container to use. Defaults to "tomcat".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L283">property appServerVersion</a>
</h3>

```typescript
appServerVersion?: pulumi.Input<string>;
```


Version of the selected application container to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L287">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L291">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L295">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L296">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L297">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L301">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L305">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L309">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L310">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L311">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L312">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L316">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L320">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L324">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L328">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L332">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L336">property jvmOptions</a>
</h3>

```typescript
jvmOptions?: pulumi.Input<string>;
```


Options to set for the JVM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L340">property jvmType</a>
</h3>

```typescript
jvmType?: pulumi.Input<string>;
```


Keyword for the type of JVM to use. Defaults to `openjdk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L344">property jvmVersion</a>
</h3>

```typescript
jvmVersion?: pulumi.Input<string>;
```


Version of JVM to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L348">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L352">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L356">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L360">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="JavaAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L184">interface JavaAppLayerState</a>
</h2>

Input properties used for looking up and filtering JavaAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L188">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the application container to use. Defaults to "tomcat".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L192">property appServerVersion</a>
</h3>

```typescript
appServerVersion?: pulumi.Input<string>;
```


Version of the selected application container to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L196">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L200">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L204">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L205">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L206">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L210">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L214">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L218">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L219">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L220">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L221">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L225">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L229">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L233">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L237">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L241">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L245">property jvmOptions</a>
</h3>

```typescript
jvmOptions?: pulumi.Input<string>;
```


Options to set for the JVM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L249">property jvmType</a>
</h3>

```typescript
jvmType?: pulumi.Input<string>;
```


Keyword for the type of JVM to use. Defaults to `openjdk`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L253">property jvmVersion</a>
</h3>

```typescript
jvmVersion?: pulumi.Input<string>;
```


Version of JVM to use. Defaults to "7".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L257">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L261">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L265">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/javaAppLayer.ts#L269">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MemcachedLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L235">interface MemcachedLayerArgs</a>
</h2>

The set of arguments for constructing a MemcachedLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L239">property allocatedMemory</a>
</h3>

```typescript
allocatedMemory?: pulumi.Input<number>;
```


Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L243">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L247">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L251">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L252">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L253">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L257">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L261">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L265">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L266">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L267">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L268">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L272">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L276">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L280">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L284">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L288">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L292">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L296">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L300">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L304">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MemcachedLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L160">interface MemcachedLayerState</a>
</h2>

Input properties used for looking up and filtering MemcachedLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L164">property allocatedMemory</a>
</h3>

```typescript
allocatedMemory?: pulumi.Input<number>;
```


Amount of memory to allocate for the cache on each instance, in megabytes. Defaults to 512MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L168">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L172">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L176">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L177">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L178">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L182">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L186">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L190">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L191">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L192">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L193">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L197">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L201">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L205">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L209">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L213">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L217">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L221">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L225">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/memcachedLayer.ts#L229">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MysqlLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L248">interface MysqlLayerArgs</a>
</h2>

The set of arguments for constructing a MysqlLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L252">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L256">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L260">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L261">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L262">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L266">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L270">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L274">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L275">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L276">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L277">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L281">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L285">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L289">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L293">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L297">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L301">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L305">property rootPassword</a>
</h3>

```typescript
rootPassword?: pulumi.Input<string>;
```


Root password to use for MySQL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L309">property rootPasswordOnAllInstances</a>
</h3>

```typescript
rootPasswordOnAllInstances?: pulumi.Input<boolean>;
```


Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L313">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L317">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L321">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="MysqlLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L169">interface MysqlLayerState</a>
</h2>

Input properties used for looking up and filtering MysqlLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L173">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L177">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L181">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L182">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L183">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L187">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L191">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L195">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L196">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L197">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L198">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L202">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L206">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L210">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L214">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L218">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L222">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L226">property rootPassword</a>
</h3>

```typescript
rootPassword?: pulumi.Input<string>;
```


Root password to use for MySQL.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L230">property rootPasswordOnAllInstances</a>
</h3>

```typescript
rootPasswordOnAllInstances?: pulumi.Input<boolean>;
```


Whether to set the root user password to all instances in the stack so they can access the instances in this layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L234">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L238">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/mysqlLayer.ts#L242">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="NodejsAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L235">interface NodejsAppLayerArgs</a>
</h2>

The set of arguments for constructing a NodejsAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L239">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L243">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L247">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L248">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L249">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L253">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L257">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L261">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L262">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L263">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L264">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L268">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L272">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L276">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L280">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L284">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L288">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L292">property nodejsVersion</a>
</h3>

```typescript
nodejsVersion?: pulumi.Input<string>;
```


The version of NodeJS to use. Defaults to "0.10.38".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L296">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L300">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L304">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="NodejsAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L160">interface NodejsAppLayerState</a>
</h2>

Input properties used for looking up and filtering NodejsAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L164">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L168">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L172">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L173">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L174">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L178">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L182">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L186">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L187">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L188">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L189">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L193">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L197">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L201">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L205">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L209">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L213">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L217">property nodejsVersion</a>
</h3>

```typescript
nodejsVersion?: pulumi.Input<string>;
```


The version of NodeJS to use. Defaults to "0.10.38".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L221">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L225">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/nodejsAppLayer.ts#L229">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="PermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L105">interface PermissionArgs</a>
</h2>

The set of arguments for constructing a Permission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L109">property allowSsh</a>
</h3>

```typescript
allowSsh?: pulumi.Input<boolean>;
```


Whether the user is allowed to use SSH to communicate with the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L113">property allowSudo</a>
</h3>

```typescript
allowSudo?: pulumi.Input<boolean>;
```


Whether the user is allowed to use sudo to elevate privileges

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L117">property level</a>
</h3>

```typescript
level?: pulumi.Input<string>;
```


The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L121">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The stack to set the permissions for

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L125">property userArn</a>
</h3>

```typescript
userArn: pulumi.Input<string>;
```


The user's IAM ARN to set permissions for

<h2 class="pdoc-module-header" id="PermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L79">interface PermissionState</a>
</h2>

Input properties used for looking up and filtering Permission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L83">property allowSsh</a>
</h3>

```typescript
allowSsh?: pulumi.Input<boolean>;
```


Whether the user is allowed to use SSH to communicate with the instance

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L87">property allowSudo</a>
</h3>

```typescript
allowSudo?: pulumi.Input<boolean>;
```


Whether the user is allowed to use sudo to elevate privileges

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L91">property level</a>
</h3>

```typescript
level?: pulumi.Input<string>;
```


The users permission level. Mus be one of `deny`, `show`, `deploy`, `manage`, `iam_only`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L95">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The stack to set the permissions for

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/permission.ts#L99">property userArn</a>
</h3>

```typescript
userArn?: pulumi.Input<string>;
```


The user's IAM ARN to set permissions for

<h2 class="pdoc-module-header" id="PhpAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L225">interface PhpAppLayerArgs</a>
</h2>

The set of arguments for constructing a PhpAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L229">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L233">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L237">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L238">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L239">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L243">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L247">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L251">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L252">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L253">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L254">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L258">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L262">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L266">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L270">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L274">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L278">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L282">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L286">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L290">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="PhpAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L154">interface PhpAppLayerState</a>
</h2>

Input properties used for looking up and filtering PhpAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L158">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L162">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L166">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L167">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L168">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L172">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L176">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L180">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L181">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L182">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L183">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L187">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L191">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L195">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L199">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L203">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L207">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L211">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L215">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/phpAppLayer.ts#L219">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RailsAppLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L285">interface RailsAppLayerArgs</a>
</h2>

The set of arguments for constructing a RailsAppLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L289">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the app server to use. Defaults to "apache_passenger".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L293">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L297">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L301">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L305">property bundlerVersion</a>
</h3>

```typescript
bundlerVersion?: pulumi.Input<string>;
```


When OpsWorks is managing Bundler, which version to use. Defaults to "1.5.3".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L306">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L307">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L311">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L315">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L319">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L320">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L321">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L322">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L326">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L330">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L334">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L338">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L342">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L346">property manageBundler</a>
</h3>

```typescript
manageBundler?: pulumi.Input<boolean>;
```


Whether OpsWorks should manage bundler. On by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L350">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L354">property passengerVersion</a>
</h3>

```typescript
passengerVersion?: pulumi.Input<string>;
```


The version of Passenger to use. Defaults to "4.0.46".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L358">property rubyVersion</a>
</h3>

```typescript
rubyVersion?: pulumi.Input<string>;
```


The version of Ruby to use. Defaults to "2.0.0".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L362">property rubygemsVersion</a>
</h3>

```typescript
rubygemsVersion?: pulumi.Input<string>;
```


The version of RubyGems to use. Defaults to "2.2.2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L366">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L370">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L374">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RailsAppLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L190">interface RailsAppLayerState</a>
</h2>

Input properties used for looking up and filtering RailsAppLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L194">property appServer</a>
</h3>

```typescript
appServer?: pulumi.Input<string>;
```


Keyword for the app server to use. Defaults to "apache_passenger".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L198">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L202">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L206">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L210">property bundlerVersion</a>
</h3>

```typescript
bundlerVersion?: pulumi.Input<string>;
```


When OpsWorks is managing Bundler, which version to use. Defaults to "1.5.3".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L211">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L212">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L216">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L220">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L224">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L225">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L226">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L227">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L231">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L235">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L239">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L243">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L247">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L251">property manageBundler</a>
</h3>

```typescript
manageBundler?: pulumi.Input<boolean>;
```


Whether OpsWorks should manage bundler. On by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L255">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L259">property passengerVersion</a>
</h3>

```typescript
passengerVersion?: pulumi.Input<string>;
```


The version of Passenger to use. Defaults to "4.0.46".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L263">property rubyVersion</a>
</h3>

```typescript
rubyVersion?: pulumi.Input<string>;
```


The version of Ruby to use. Defaults to "2.0.0".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L267">property rubygemsVersion</a>
</h3>

```typescript
rubygemsVersion?: pulumi.Input<string>;
```


The version of RubyGems to use. Defaults to "2.2.2".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L271">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L275">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/railsAppLayer.ts#L279">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="RdsDbInstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L107">interface RdsDbInstanceArgs</a>
</h2>

The set of arguments for constructing a RdsDbInstance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L111">property dbPassword</a>
</h3>

```typescript
dbPassword: pulumi.Input<string>;
```


A db password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L115">property dbUser</a>
</h3>

```typescript
dbUser: pulumi.Input<string>;
```


A db username

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L119">property rdsDbInstanceArn</a>
</h3>

```typescript
rdsDbInstanceArn: pulumi.Input<string>;
```


The db instance to register for this stack. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L123">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The stack to register a db inatance for. Changing this will force a new resource.

<h2 class="pdoc-module-header" id="RdsDbInstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L85">interface RdsDbInstanceState</a>
</h2>

Input properties used for looking up and filtering RdsDbInstance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L89">property dbPassword</a>
</h3>

```typescript
dbPassword?: pulumi.Input<string>;
```


A db password

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L93">property dbUser</a>
</h3>

```typescript
dbUser?: pulumi.Input<string>;
```


A db username

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L97">property rdsDbInstanceArn</a>
</h3>

```typescript
rdsDbInstanceArn?: pulumi.Input<string>;
```


The db instance to register for this stack. Changing this will force a new resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/rdsDbInstance.ts#L101">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The stack to register a db inatance for. Changing this will force a new resource.

<h2 class="pdoc-module-header" id="StackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L305">interface StackArgs</a>
</h2>

The set of arguments for constructing a Stack resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L309">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


If set to `"LATEST"`, OpsWorks will automatically install the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L313">property berkshelfVersion</a>
</h3>

```typescript
berkshelfVersion?: pulumi.Input<string>;
```


If `manage_berkshelf` is enabled, the version of Berkshelf to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L317">property color</a>
</h3>

```typescript
color?: pulumi.Input<string>;
```


Color to paint next to the stack's resources in the OpsWorks console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L321">property configurationManagerName</a>
</h3>

```typescript
configurationManagerName?: pulumi.Input<string>;
```


Name of the configuration manager to use. Defaults to "Chef".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L325">property configurationManagerVersion</a>
</h3>

```typescript
configurationManagerVersion?: pulumi.Input<string>;
```


Version of the configuration manager to use. Defaults to "11.4".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L330">property customCookbooksSources</a>
</h3>

```typescript
customCookbooksSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


When `use_custom_cookbooks` is set, provide this sub-object as
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L334">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the entire stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L339">property defaultAvailabilityZone</a>
</h3>

```typescript
defaultAvailabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L344">property defaultInstanceProfileArn</a>
</h3>

```typescript
defaultInstanceProfileArn: pulumi.Input<string>;
```


The ARN of an IAM Instance Profile that created instances
will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L348">property defaultOs</a>
</h3>

```typescript
defaultOs?: pulumi.Input<string>;
```


Name of OS that will be installed on instances by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L352">property defaultRootDeviceType</a>
</h3>

```typescript
defaultRootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L356">property defaultSshKeyName</a>
</h3>

```typescript
defaultSshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L361">property defaultSubnetId</a>
</h3>

```typescript
defaultSubnetId?: pulumi.Input<string>;
```


Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L366">property hostnameTheme</a>
</h3>

```typescript
hostnameTheme?: pulumi.Input<string>;
```


Keyword representing the naming scheme that will be used for instance hostnames
within this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L370">property manageBerkshelf</a>
</h3>

```typescript
manageBerkshelf?: pulumi.Input<boolean>;
```


Boolean value controlling whether Opsworks will run Berkshelf for this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L374">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L378">property region</a>
</h3>

```typescript
region: pulumi.Input<string>;
```


The name of the region where the stack will exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L382">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn: pulumi.Input<string>;
```


The ARN of an IAM role that the OpsWorks service will act as.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L386">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L391">property useCustomCookbooks</a>
</h3>

```typescript
useCustomCookbooks?: pulumi.Input<boolean>;
```


Boolean value controlling whether the custom cookbook settings are
enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L396">property useOpsworksSecurityGroups</a>
</h3>

```typescript
useOpsworksSecurityGroups?: pulumi.Input<boolean>;
```


Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L400">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The id of the VPC that this stack belongs to.

<h2 class="pdoc-module-header" id="StackState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L202">interface StackState</a>
</h2>

Input properties used for looking up and filtering Stack resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L206">property agentVersion</a>
</h3>

```typescript
agentVersion?: pulumi.Input<string>;
```


If set to `"LATEST"`, OpsWorks will automatically install the latest version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L207">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L211">property berkshelfVersion</a>
</h3>

```typescript
berkshelfVersion?: pulumi.Input<string>;
```


If `manage_berkshelf` is enabled, the version of Berkshelf to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L215">property color</a>
</h3>

```typescript
color?: pulumi.Input<string>;
```


Color to paint next to the stack's resources in the OpsWorks console.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L219">property configurationManagerName</a>
</h3>

```typescript
configurationManagerName?: pulumi.Input<string>;
```


Name of the configuration manager to use. Defaults to "Chef".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L223">property configurationManagerVersion</a>
</h3>

```typescript
configurationManagerVersion?: pulumi.Input<string>;
```


Version of the configuration manager to use. Defaults to "11.4".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L228">property customCookbooksSources</a>
</h3>

```typescript
customCookbooksSources?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


When `use_custom_cookbooks` is set, provide this sub-object as
described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L232">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```


Custom JSON attributes to apply to the entire stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L237">property defaultAvailabilityZone</a>
</h3>

```typescript
defaultAvailabilityZone?: pulumi.Input<string>;
```


Name of the availability zone where instances will be created
by default. This is required unless you set `vpc_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L242">property defaultInstanceProfileArn</a>
</h3>

```typescript
defaultInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM Instance Profile that created instances
will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L246">property defaultOs</a>
</h3>

```typescript
defaultOs?: pulumi.Input<string>;
```


Name of OS that will be installed on instances by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L250">property defaultRootDeviceType</a>
</h3>

```typescript
defaultRootDeviceType?: pulumi.Input<string>;
```


Name of the type of root device instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L254">property defaultSshKeyName</a>
</h3>

```typescript
defaultSshKeyName?: pulumi.Input<string>;
```


Name of the SSH keypair that instances will have by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L259">property defaultSubnetId</a>
</h3>

```typescript
defaultSubnetId?: pulumi.Input<string>;
```


Id of the subnet in which instances will be created by default. Mandatory
if `vpc_id` is set, and forbidden if it isn't.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L264">property hostnameTheme</a>
</h3>

```typescript
hostnameTheme?: pulumi.Input<string>;
```


Keyword representing the naming scheme that will be used for instance hostnames
within this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L268">property manageBerkshelf</a>
</h3>

```typescript
manageBerkshelf?: pulumi.Input<boolean>;
```


Boolean value controlling whether Opsworks will run Berkshelf for this stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L272">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L276">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The name of the region where the stack will exist.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L280">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that the OpsWorks service will act as.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L281">property stackEndpoint</a>
</h3>

```typescript
stackEndpoint?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L285">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L290">property useCustomCookbooks</a>
</h3>

```typescript
useCustomCookbooks?: pulumi.Input<boolean>;
```


Boolean value controlling whether the custom cookbook settings are
enabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L295">property useOpsworksSecurityGroups</a>
</h3>

```typescript
useOpsworksSecurityGroups?: pulumi.Input<boolean>;
```


Boolean value controlling whether the standard OpsWorks
security groups apply to created instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/stack.ts#L299">property vpcId</a>
</h3>

```typescript
vpcId?: pulumi.Input<string>;
```


The id of the VPC that this stack belongs to.

<h2 class="pdoc-module-header" id="StaticWebLayerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L219">interface StaticWebLayerArgs</a>
</h2>

The set of arguments for constructing a StaticWebLayer resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L223">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L227">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L231">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L232">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L233">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L237">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L238">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L242">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L243">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L244">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L245">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L249">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L253">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L257">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L261">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L265">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L269">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L273">property stackId</a>
</h3>

```typescript
stackId: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L277">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L281">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="StaticWebLayerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L151">interface StaticWebLayerState</a>
</h2>

Input properties used for looking up and filtering StaticWebLayer resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L155">property autoAssignElasticIps</a>
</h3>

```typescript
autoAssignElasticIps?: pulumi.Input<boolean>;
```


Whether to automatically assign an elastic IP address to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L159">property autoAssignPublicIps</a>
</h3>

```typescript
autoAssignPublicIps?: pulumi.Input<boolean>;
```


For stacks belonging to a VPC, whether to automatically assign a public IP address to each of the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L163">property autoHealing</a>
</h3>

```typescript
autoHealing?: pulumi.Input<boolean>;
```


Whether to enable auto-healing for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L164">property customConfigureRecipes</a>
</h3>

```typescript
customConfigureRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L165">property customDeployRecipes</a>
</h3>

```typescript
customDeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L169">property customInstanceProfileArn</a>
</h3>

```typescript
customInstanceProfileArn?: pulumi.Input<string>;
```


The ARN of an IAM profile that will be used for the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L170">property customJson</a>
</h3>

```typescript
customJson?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L174">property customSecurityGroupIds</a>
</h3>

```typescript
customSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
```


Ids for a set of security groups to apply to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L175">property customSetupRecipes</a>
</h3>

```typescript
customSetupRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L176">property customShutdownRecipes</a>
</h3>

```typescript
customShutdownRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L177">property customUndeployRecipes</a>
</h3>

```typescript
customUndeployRecipes?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L181">property drainElbOnShutdown</a>
</h3>

```typescript
drainElbOnShutdown?: pulumi.Input<boolean>;
```


Whether to enable Elastic Load Balancing connection draining.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L185">property ebsVolumes</a>
</h3>

```typescript
ebsVolumes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


`ebs_volume` blocks, as described below, will each create an EBS volume and connect it to the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L189">property elasticLoadBalancer</a>
</h3>

```typescript
elasticLoadBalancer?: pulumi.Input<string>;
```


Name of an Elastic Load Balancer to attach to this layer

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L193">property installUpdatesOnBoot</a>
</h3>

```typescript
installUpdatesOnBoot?: pulumi.Input<boolean>;
```


Whether to install OS and package updates on each instance when it boots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L197">property instanceShutdownTimeout</a>
</h3>

```typescript
instanceShutdownTimeout?: pulumi.Input<number>;
```


The time, in seconds, that OpsWorks will wait for Chef to complete after triggering the Shutdown event.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L201">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A human-readable name for the layer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L205">property stackId</a>
</h3>

```typescript
stackId?: pulumi.Input<string>;
```


The id of the stack the layer will belong to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L209">property systemPackages</a>
</h3>

```typescript
systemPackages?: pulumi.Input<pulumi.Input<string>[]>;
```


Names of a set of system packages to install on the layer's instances.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/staticWebLayer.ts#L213">property useEbsOptimizedInstances</a>
</h3>

```typescript
useEbsOptimizedInstances?: pulumi.Input<boolean>;
```


Whether to use EBS-optimized instances.

<h2 class="pdoc-module-header" id="UserProfileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L98">interface UserProfileArgs</a>
</h2>

The set of arguments for constructing a UserProfile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L102">property allowSelfManagement</a>
</h3>

```typescript
allowSelfManagement?: pulumi.Input<boolean>;
```


Whether users can specify their own SSH public key through the My Settings page

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L106">property sshPublicKey</a>
</h3>

```typescript
sshPublicKey?: pulumi.Input<string>;
```


The users public key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L110">property sshUsername</a>
</h3>

```typescript
sshUsername: pulumi.Input<string>;
```


The ssh username, with witch this user wants to log in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L114">property userArn</a>
</h3>

```typescript
userArn: pulumi.Input<string>;
```


The user's IAM ARN

<h2 class="pdoc-module-header" id="UserProfileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L76">interface UserProfileState</a>
</h2>

Input properties used for looking up and filtering UserProfile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L80">property allowSelfManagement</a>
</h3>

```typescript
allowSelfManagement?: pulumi.Input<boolean>;
```


Whether users can specify their own SSH public key through the My Settings page

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L84">property sshPublicKey</a>
</h3>

```typescript
sshPublicKey?: pulumi.Input<string>;
```


The users public key

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L88">property sshUsername</a>
</h3>

```typescript
sshUsername?: pulumi.Input<string>;
```


The ssh username, with witch this user wants to log in

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/opsworks/userProfile.ts#L92">property userArn</a>
</h3>

```typescript
userArn?: pulumi.Input<string>;
```


The user's IAM ARN

