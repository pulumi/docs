---
title: Module codedeploy
---

<a href="../index.html">@pulumi/aws</a> &gt; codedeploy

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Application">class Application</a>
* <a href="#DeploymentConfig">class DeploymentConfig</a>
* <a href="#DeploymentGroup">class DeploymentGroup</a>
* <a href="#ApplicationArgs">interface ApplicationArgs</a>
* <a href="#ApplicationState">interface ApplicationState</a>
* <a href="#DeploymentConfigArgs">interface DeploymentConfigArgs</a>
* <a href="#DeploymentConfigState">interface DeploymentConfigState</a>
* <a href="#DeploymentGroupArgs">interface DeploymentGroupArgs</a>
* <a href="#DeploymentGroupState">interface DeploymentGroupState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts">codedeploy/application.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts">codedeploy/deploymentConfig.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts">codedeploy/deploymentGroup.ts</a> 


<h2 class="pdoc-module-header" id="Application">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L10">class Application</a>
</h2>

Provides a CodeDeploy application to be used as a basis for deployments

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L31">constructor</a>
</h3>

```typescript
new Application(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L26">property computePlatform</a>
</h3>

```typescript
public computePlatform: pulumi.Output<string | undefined>;
```


The compute platform can either be `Server` or `Lambda`. Default is `Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L31">property uniqueId</a>
</h3>

```typescript
public uniqueId: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DeploymentConfig">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L10">class DeploymentConfig</a>
</h2>

Provides a CodeDeploy deployment config for an application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L34">constructor</a>
</h3>

```typescript
new DeploymentConfig(name: string, args: DeploymentConfigArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DeploymentConfig resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentConfigState): DeploymentConfig
```


Get an existing DeploymentConfig resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L26">property deploymentConfigId</a>
</h3>

```typescript
public deploymentConfigId: pulumi.Output<string>;
```


The AWS Assigned deployment config id

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L30">property deploymentConfigName</a>
</h3>

```typescript
public deploymentConfigName: pulumi.Output<string>;
```


The name of the deployment config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L34">property minimumHealthyHosts</a>
</h3>

```typescript
public minimumHealthyHosts: pulumi.Output<{ ... }>;
```


A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DeploymentGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L10">class DeploymentGroup</a>
</h2>

Provides a CodeDeploy Deployment Group for a CodeDeploy Application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L78">constructor</a>
</h3>

```typescript
new DeploymentGroup(name: string, args: DeploymentGroupArgs, opts?: pulumi.CustomResourceOptions)
```


Create a DeploymentGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentGroupState): DeploymentGroup
```


Get an existing DeploymentGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L26">property alarmConfiguration</a>
</h3>

```typescript
public alarmConfiguration: pulumi.Output<{ ... } | undefined>;
```


Information about alarms associated with the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L30">property appName</a>
</h3>

```typescript
public appName: pulumi.Output<string>;
```


The name of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L34">property autoRollbackConfiguration</a>
</h3>

```typescript
public autoRollbackConfiguration: pulumi.Output<{ ... } | undefined>;
```


The automatic rollback configuration associated with the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L38">property autoscalingGroups</a>
</h3>

```typescript
public autoscalingGroups: pulumi.Output<string[] | undefined>;
```


Autoscaling groups associated with the deployment group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L42">property blueGreenDeploymentConfig</a>
</h3>

```typescript
public blueGreenDeploymentConfig: pulumi.Output<{ ... }>;
```


Information about blue/green deployment options for a deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L46">property deploymentConfigName</a>
</h3>

```typescript
public deploymentConfigName: pulumi.Output<string | undefined>;
```


The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L50">property deploymentGroupName</a>
</h3>

```typescript
public deploymentGroupName: pulumi.Output<string>;
```


The name of the deployment group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L54">property deploymentStyle</a>
</h3>

```typescript
public deploymentStyle: pulumi.Output<{ ... }>;
```


Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L58">property ec2TagFilters</a>
</h3>

```typescript
public ec2TagFilters: pulumi.Output<{ ... }[] | undefined>;
```


Tag filters associated with the deployment group. See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L62">property ec2TagSets</a>
</h3>

```typescript
public ec2TagSets: pulumi.Output<{ ... }[] | undefined>;
```


Sets of Tag filters associated with the deployment group, which are referred to as *tag groups* in the document.  See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L66">property loadBalancerInfo</a>
</h3>

```typescript
public loadBalancerInfo: pulumi.Output<{ ... }>;
```


Information about the load balancer to use in a blue/green deployment (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L70">property onPremisesInstanceTagFilters</a>
</h3>

```typescript
public onPremisesInstanceTagFilters: pulumi.Output<{ ... }[] | undefined>;
```


On premise tag filters associated with the group. See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L74">property serviceRoleArn</a>
</h3>

```typescript
public serviceRoleArn: pulumi.Output<string>;
```


The service role ARN that allows deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L78">property triggerConfigurations</a>
</h3>

```typescript
public triggerConfigurations: pulumi.Output<{ ... }[] | undefined>;
```


Trigger Configurations for the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L76">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L80">property computePlatform</a>
</h3>

```typescript
computePlatform?: pulumi.Input<string>;
```


The compute platform can either be `Server` or `Lambda`. Default is `Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L84">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L85">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L61">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L65">property computePlatform</a>
</h3>

```typescript
computePlatform?: pulumi.Input<string>;
```


The compute platform can either be `Server` or `Lambda`. Default is `Server`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L69">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/application.ts#L70">property uniqueId</a>
</h3>

```typescript
uniqueId?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="DeploymentConfigArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L88">interface DeploymentConfigArgs</a>
</h2>

The set of arguments for constructing a DeploymentConfig resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L92">property deploymentConfigName</a>
</h3>

```typescript
deploymentConfigName: pulumi.Input<string>;
```


The name of the deployment config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L96">property minimumHealthyHosts</a>
</h3>

```typescript
minimumHealthyHosts: pulumi.Input<{ ... }>;
```


A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.

<h2 class="pdoc-module-header" id="DeploymentConfigState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L70">interface DeploymentConfigState</a>
</h2>

Input properties used for looking up and filtering DeploymentConfig resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L74">property deploymentConfigId</a>
</h3>

```typescript
deploymentConfigId?: pulumi.Input<string>;
```


The AWS Assigned deployment config id

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L78">property deploymentConfigName</a>
</h3>

```typescript
deploymentConfigName?: pulumi.Input<string>;
```


The name of the deployment config.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentConfig.ts#L82">property minimumHealthyHosts</a>
</h3>

```typescript
minimumHealthyHosts?: pulumi.Input<{ ... }>;
```


A minimum_healthy_hosts block. Minimum Healthy Hosts are documented below.

<h2 class="pdoc-module-header" id="DeploymentGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L201">interface DeploymentGroupArgs</a>
</h2>

The set of arguments for constructing a DeploymentGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L205">property alarmConfiguration</a>
</h3>

```typescript
alarmConfiguration?: pulumi.Input<{ ... }>;
```


Information about alarms associated with the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L209">property appName</a>
</h3>

```typescript
appName: pulumi.Input<string>;
```


The name of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L213">property autoRollbackConfiguration</a>
</h3>

```typescript
autoRollbackConfiguration?: pulumi.Input<{ ... }>;
```


The automatic rollback configuration associated with the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L217">property autoscalingGroups</a>
</h3>

```typescript
autoscalingGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


Autoscaling groups associated with the deployment group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L221">property blueGreenDeploymentConfig</a>
</h3>

```typescript
blueGreenDeploymentConfig?: pulumi.Input<{ ... }>;
```


Information about blue/green deployment options for a deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L225">property deploymentConfigName</a>
</h3>

```typescript
deploymentConfigName?: pulumi.Input<string>;
```


The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L229">property deploymentGroupName</a>
</h3>

```typescript
deploymentGroupName: pulumi.Input<string>;
```


The name of the deployment group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L233">property deploymentStyle</a>
</h3>

```typescript
deploymentStyle?: pulumi.Input<{ ... }>;
```


Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L237">property ec2TagFilters</a>
</h3>

```typescript
ec2TagFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Tag filters associated with the deployment group. See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L241">property ec2TagSets</a>
</h3>

```typescript
ec2TagSets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Sets of Tag filters associated with the deployment group, which are referred to as *tag groups* in the document.  See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L245">property loadBalancerInfo</a>
</h3>

```typescript
loadBalancerInfo?: pulumi.Input<{ ... }>;
```


Information about the load balancer to use in a blue/green deployment (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L249">property onPremisesInstanceTagFilters</a>
</h3>

```typescript
onPremisesInstanceTagFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


On premise tag filters associated with the group. See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L253">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn: pulumi.Input<string>;
```


The service role ARN that allows deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L257">property triggerConfigurations</a>
</h3>

```typescript
triggerConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Trigger Configurations for the deployment group (documented below).

<h2 class="pdoc-module-header" id="DeploymentGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L139">interface DeploymentGroupState</a>
</h2>

Input properties used for looking up and filtering DeploymentGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L143">property alarmConfiguration</a>
</h3>

```typescript
alarmConfiguration?: pulumi.Input<{ ... }>;
```


Information about alarms associated with the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L147">property appName</a>
</h3>

```typescript
appName?: pulumi.Input<string>;
```


The name of the application.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L151">property autoRollbackConfiguration</a>
</h3>

```typescript
autoRollbackConfiguration?: pulumi.Input<{ ... }>;
```


The automatic rollback configuration associated with the deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L155">property autoscalingGroups</a>
</h3>

```typescript
autoscalingGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


Autoscaling groups associated with the deployment group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L159">property blueGreenDeploymentConfig</a>
</h3>

```typescript
blueGreenDeploymentConfig?: pulumi.Input<{ ... }>;
```


Information about blue/green deployment options for a deployment group (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L163">property deploymentConfigName</a>
</h3>

```typescript
deploymentConfigName?: pulumi.Input<string>;
```


The name of the group's deployment config. The default is "CodeDeployDefault.OneAtATime".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L167">property deploymentGroupName</a>
</h3>

```typescript
deploymentGroupName?: pulumi.Input<string>;
```


The name of the deployment group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L171">property deploymentStyle</a>
</h3>

```typescript
deploymentStyle?: pulumi.Input<{ ... }>;
```


Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L175">property ec2TagFilters</a>
</h3>

```typescript
ec2TagFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Tag filters associated with the deployment group. See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L179">property ec2TagSets</a>
</h3>

```typescript
ec2TagSets?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Sets of Tag filters associated with the deployment group, which are referred to as *tag groups* in the document.  See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L183">property loadBalancerInfo</a>
</h3>

```typescript
loadBalancerInfo?: pulumi.Input<{ ... }>;
```


Information about the load balancer to use in a blue/green deployment (documented below).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L187">property onPremisesInstanceTagFilters</a>
</h3>

```typescript
onPremisesInstanceTagFilters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


On premise tag filters associated with the group. See the AWS docs for details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L191">property serviceRoleArn</a>
</h3>

```typescript
serviceRoleArn?: pulumi.Input<string>;
```


The service role ARN that allows deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codedeploy/deploymentGroup.ts#L195">property triggerConfigurations</a>
</h3>

```typescript
triggerConfigurations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Trigger Configurations for the deployment group (documented below).

