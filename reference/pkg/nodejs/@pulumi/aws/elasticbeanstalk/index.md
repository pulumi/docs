---
title: Module elasticbeanstalk
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Application">class Application</a>
* <a href="#ApplicationVersion">class ApplicationVersion</a>
* <a href="#ConfigurationTemplate">class ConfigurationTemplate</a>
* <a href="#Environment">class Environment</a>
* <a href="#getHostedZone">function getHostedZone</a>
* <a href="#getSolutionStack">function getSolutionStack</a>
* <a href="#ApplicationArgs">interface ApplicationArgs</a>
* <a href="#ApplicationState">interface ApplicationState</a>
* <a href="#ApplicationVersionArgs">interface ApplicationVersionArgs</a>
* <a href="#ApplicationVersionState">interface ApplicationVersionState</a>
* <a href="#ConfigurationTemplateArgs">interface ConfigurationTemplateArgs</a>
* <a href="#ConfigurationTemplateState">interface ConfigurationTemplateState</a>
* <a href="#EnvironmentArgs">interface EnvironmentArgs</a>
* <a href="#EnvironmentState">interface EnvironmentState</a>
* <a href="#GetHostedZoneArgs">interface GetHostedZoneArgs</a>
* <a href="#GetSolutionStackArgs">interface GetSolutionStackArgs</a>
* <a href="#GetSolutionStackResult">interface GetSolutionStackResult</a>

<a href="/elasticbeanstalk/application.ts">elasticbeanstalk/application.ts</a> <a href="/elasticbeanstalk/applicationVersion.ts">elasticbeanstalk/applicationVersion.ts</a> <a href="/elasticbeanstalk/configurationTemplate.ts">elasticbeanstalk/configurationTemplate.ts</a> <a href="/elasticbeanstalk/environment.ts">elasticbeanstalk/environment.ts</a> <a href="/elasticbeanstalk/getHostedZone.ts">elasticbeanstalk/getHostedZone.ts</a> <a href="/elasticbeanstalk/getSolutionStack.ts">elasticbeanstalk/getSolutionStack.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Application">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L14">class Application</a>
</h2>

Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

This resource creates an application that has one configuration template named
`default`, and no application versions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L34">constructor</a>
</h3>

```typescript
new Application(name: string, args?: ApplicationArgs, opts?: pulumi.ResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Application(name: string, state?: ApplicationState, opts?: pulumi.ResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState): Application
```


Get an existing Application resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the application, must be unique within your account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ApplicationVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L27">class ApplicationVersion</a>
</h2>

Provides an Elastic Beanstalk Application Version Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

This resource creates a Beanstalk Application Version that can be deployed to a Beanstalk
Environment.

~> **NOTE on Application Version Resource:**  When using the Application Version resource with multiple
[Elastic Beanstalk Environments](elastic_beanstalk_environment.html) it is possible that an error may be returned
when attempting to delete an Application Version while it is still in use by a different environment.
To work around this you can:
<ol>
<li>Create each environment in a separate AWS account</li>
<li>Create your `aws_elastic_beanstalk_application_version` resources with a unique names in your
Elastic Beanstalk Application. For example &lt;revision&gt;-&lt;environment&gt;.</li>
</ol>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L64">constructor</a>
</h3>

```typescript
new ApplicationVersion(name: string, args: ApplicationVersionArgs, opts?: pulumi.ResourceOptions)
```


Create a ApplicationVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ApplicationVersion(name: string, state?: ApplicationVersionState, opts?: pulumi.ResourceOptions)
```


Create a ApplicationVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L36">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationVersionState): ApplicationVersion
```


Get an existing ApplicationVersion resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L43">property application</a>
</h3>

```typescript
public application: pulumi.Output<Application>;
```


Name of the Beanstalk Application the version is associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L47">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<Bucket | string>;
```


S3 bucket that contains the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L51">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L56">property forceDelete</a>
</h3>

```typescript
public forceDelete: pulumi.Output<boolean | undefined>;
```


On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L60">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


S3 object that is the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L64">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the this Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfigurationTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L11">class ConfigurationTemplate</a>
</h2>

Provides an Elastic Beanstalk Configuration Template, which are associated with
a specific application and are used to deploy different versions of the
application with the same configuration settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L46">constructor</a>
</h3>

```typescript
new ConfigurationTemplate(name: string, args: ConfigurationTemplateArgs, opts?: pulumi.ResourceOptions)
```


Create a ConfigurationTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new ConfigurationTemplate(name: string, state?: ConfigurationTemplateState, opts?: pulumi.ResourceOptions)
```


Create a ConfigurationTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationTemplateState): ConfigurationTemplate
```


Get an existing ConfigurationTemplate resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L27">property application</a>
</h3>

```typescript
public application: pulumi.Output<string>;
```


name of the application to associate with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the Template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L40">property environmentId</a>
</h3>

```typescript
public environmentId: pulumi.Output<string | undefined>;
```


The ID of the environment used with this configuration template
* `setting` – (Optional) Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in [Option Settings](#option-settings)
* `solution_stack_name` – (Optional) A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for this Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L45">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L46">property solutionStackName</a>
</h3>

```typescript
public solutionStackName: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Environment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L17">class Environment</a>
</h2>

Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

Environments are often things such as `development`, `integration`, or
`production`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L122">constructor</a>
</h3>

```typescript
new Environment(name: string, args: EnvironmentArgs, opts?: pulumi.ResourceOptions)
```


Create a Environment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Environment(name: string, state?: EnvironmentState, opts?: pulumi.ResourceOptions)
```


Create a Environment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EnvironmentState): Environment
```


Get an existing Environment resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L35">property allSettings</a>
</h3>

```typescript
public allSettings: pulumi.Output<{ ... }[]>;
```


List of all option settings configured in the Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L40">property application</a>
</h3>

```typescript
public application: pulumi.Output<Application>;
```


Name of the application that contains the version
to be deployed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L41">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L45">property autoscalingGroups</a>
</h3>

```typescript
public autoscalingGroups: pulumi.Output<string[]>;
```


The autoscaling groups used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L49">property cname</a>
</h3>

```typescript
public cname: pulumi.Output<string>;
```


Fully qualified DNS name for the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L54">property cnamePrefix</a>
</h3>

```typescript
public cnamePrefix: pulumi.Output<string>;
```


Prefix to use for the fully qualified DNS name of
the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L58">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the Environment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L62">property instances</a>
</h3>

```typescript
public instances: pulumi.Output<string[]>;
```


Instances used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L66">property launchConfigurations</a>
</h3>

```typescript
public launchConfigurations: pulumi.Output<string[]>;
```


Launch configurations in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L70">property loadBalancers</a>
</h3>

```typescript
public loadBalancers: pulumi.Output<string[]>;
```


Elastic load balancers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L75">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for this Environment. This name is used
in the application URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L76">property pollInterval</a>
</h3>

```typescript
public pollInterval: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L80">property queues</a>
</h3>

```typescript
public queues: pulumi.Output<string[]>;
```


SQS queues in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L84">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }[] | undefined>;
```


Settings specifically set for this Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L85">property solutionStackName</a>
</h3>

```typescript
public solutionStackName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L86">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L91">property templateName</a>
</h3>

```typescript
public templateName: pulumi.Output<string | undefined>;
```


The name of the Elastic Beanstalk Configuration
template to use in deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L101">property tier</a>
</h3>

```typescript
public tier: pulumi.Output<string | undefined>;
```


Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
* `setting` – (Optional) Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in [Option Settings](#option-settings)
* `solution_stack_name` – (Optional) A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L105">property triggers</a>
</h3>

```typescript
public triggers: pulumi.Output<string[]>;
```


Autoscaling triggers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L111">property version</a>
</h3>

```typescript
public version: pulumi.Output<ApplicationVersion>;
```


The name of the Elastic Beanstalk Application Version
to use in deployment.
* `tags` – (Optional) A set of tags to apply to the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L122">property waitForReadyTimeout</a>
</h3>

```typescript
public waitForReadyTimeout: pulumi.Output<string | undefined>;
```


The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
* `poll_interval` – The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff

<h2 class="pdoc-module-header" id="getHostedZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getHostedZone.ts#L9">function getHostedZone</a>
</h2>

```typescript
getHostedZone(args?: GetHostedZoneArgs): Promise<void>
```


Use this data source to get the ID of an [elastic beanstalk hosted zone](http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region).

<h2 class="pdoc-module-header" id="getSolutionStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getSolutionStack.ts#L9">function getSolutionStack</a>
</h2>

```typescript
getSolutionStack(args: GetSolutionStackArgs): Promise<GetSolutionStackResult>
```


Use this data source to get the name of a elastic beanstalk solution stack.

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L78">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L82">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L86">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application, must be unique within your account

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L64">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L68">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/application.ts#L72">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application, must be unique within your account

<h2 class="pdoc-module-header" id="ApplicationVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L142">interface ApplicationVersionArgs</a>
</h2>

The set of arguments for constructing a ApplicationVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L146">property application</a>
</h3>

```typescript
application: pulumi.Input<Application>;
```


Name of the Beanstalk Application the version is associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L150">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<Bucket | string>;
```


S3 bucket that contains the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L154">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L159">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L163">property key</a>
</h3>

```typescript
key: pulumi.Input<string>;
```


S3 object that is the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L167">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the this Application Version.

<h2 class="pdoc-module-header" id="ApplicationVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L111">interface ApplicationVersionState</a>
</h2>

Input properties used for looking up and filtering ApplicationVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L115">property application</a>
</h3>

```typescript
application?: pulumi.Input<Application>;
```


Name of the Beanstalk Application the version is associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L119">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<Bucket | string>;
```


S3 bucket that contains the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L123">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L128">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L132">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


S3 object that is the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/applicationVersion.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the this Application Version.

<h2 class="pdoc-module-header" id="ConfigurationTemplateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L116">interface ConfigurationTemplateArgs</a>
</h2>

The set of arguments for constructing a ConfigurationTemplate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L120">property application</a>
</h3>

```typescript
application: pulumi.Input<string>;
```


name of the application to associate with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L124">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L133">property environmentId</a>
</h3>

```typescript
environmentId?: pulumi.Input<string>;
```


The ID of the environment used with this configuration template
* `setting` – (Optional) Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in [Option Settings](#option-settings)
* `solution_stack_name` – (Optional) A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L138">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L139">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="ConfigurationTemplateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L87">interface ConfigurationTemplateState</a>
</h2>

Input properties used for looking up and filtering ConfigurationTemplate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L91">property application</a>
</h3>

```typescript
application?: pulumi.Input<string>;
```


name of the application to associate with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L104">property environmentId</a>
</h3>

```typescript
environmentId?: pulumi.Input<string>;
```


The ID of the environment used with this configuration template
* `setting` – (Optional) Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in [Option Settings](#option-settings)
* `solution_stack_name` – (Optional) A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L109">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/configurationTemplate.ts#L110">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="EnvironmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L292">interface EnvironmentArgs</a>
</h2>

The set of arguments for constructing a Environment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L297">property application</a>
</h3>

```typescript
application: pulumi.Input<Application>;
```


Name of the application that contains the version
to be deployed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L302">property cnamePrefix</a>
</h3>

```typescript
cnamePrefix?: pulumi.Input<string>;
```


Prefix to use for the fully qualified DNS name of
the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L306">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Environment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L311">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Environment. This name is used
in the application URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L312">property pollInterval</a>
</h3>

```typescript
pollInterval?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L316">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }[]>;
```


Settings specifically set for this Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L317">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L318">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L323">property templateName</a>
</h3>

```typescript
templateName?: pulumi.Input<string>;
```


The name of the Elastic Beanstalk Configuration
template to use in deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L333">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
* `setting` – (Optional) Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in [Option Settings](#option-settings)
* `solution_stack_name` – (Optional) A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L339">property version</a>
</h3>

```typescript
version?: pulumi.Input<ApplicationVersion>;
```


The name of the Elastic Beanstalk Application Version
to use in deployment.
* `tags` – (Optional) A set of tags to apply to the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L350">property waitForReadyTimeout</a>
</h3>

```typescript
waitForReadyTimeout?: pulumi.Input<string>;
```


The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
* `poll_interval` – The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff

<h2 class="pdoc-module-header" id="EnvironmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L193">interface EnvironmentState</a>
</h2>

Input properties used for looking up and filtering Environment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L199">property allSettings</a>
</h3>

```typescript
allSettings?: pulumi.Input<{ ... }[]>;
```


List of all option settings configured in the Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L204">property application</a>
</h3>

```typescript
application?: pulumi.Input<Application>;
```


Name of the application that contains the version
to be deployed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L205">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L209">property autoscalingGroups</a>
</h3>

```typescript
autoscalingGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


The autoscaling groups used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L213">property cname</a>
</h3>

```typescript
cname?: pulumi.Input<string>;
```


Fully qualified DNS name for the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L218">property cnamePrefix</a>
</h3>

```typescript
cnamePrefix?: pulumi.Input<string>;
```


Prefix to use for the fully qualified DNS name of
the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L222">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Environment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L226">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<pulumi.Input<string>[]>;
```


Instances used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L230">property launchConfigurations</a>
</h3>

```typescript
launchConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```


Launch configurations in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L234">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<pulumi.Input<string>[]>;
```


Elastic load balancers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L239">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Environment. This name is used
in the application URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L240">property pollInterval</a>
</h3>

```typescript
pollInterval?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L244">property queues</a>
</h3>

```typescript
queues?: pulumi.Input<pulumi.Input<string>[]>;
```


SQS queues in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L248">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<{ ... }[]>;
```


Settings specifically set for this Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L249">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L250">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L255">property templateName</a>
</h3>

```typescript
templateName?: pulumi.Input<string>;
```


The name of the Elastic Beanstalk Configuration
template to use in deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L265">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
* `setting` – (Optional) Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in [Option Settings](#option-settings)
* `solution_stack_name` – (Optional) A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L269">property triggers</a>
</h3>

```typescript
triggers?: pulumi.Input<pulumi.Input<string>[]>;
```


Autoscaling triggers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L275">property version</a>
</h3>

```typescript
version?: pulumi.Input<ApplicationVersion>;
```


The name of the Elastic Beanstalk Application Version
to use in deployment.
* `tags` – (Optional) A set of tags to apply to the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/environment.ts#L286">property waitForReadyTimeout</a>
</h3>

```typescript
waitForReadyTimeout?: pulumi.Input<string>;
```


The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
* `poll_interval` – The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff

<h2 class="pdoc-module-header" id="GetHostedZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getHostedZone.ts#L19">interface GetHostedZoneArgs</a>
</h2>

A collection of arguments for invoking getHostedZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getHostedZone.ts#L23">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region you'd like the zone for. By default, fetches the current region.

<h2 class="pdoc-module-header" id="GetSolutionStackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getSolutionStack.ts#L19">interface GetSolutionStackArgs</a>
</h2>

A collection of arguments for invoking getSolutionStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getSolutionStack.ts#L24">property mostRecent</a>
</h3>

```typescript
mostRecent?: pulumi.Input<boolean>;
```


If more than one result is returned, use the most
recent solution stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getSolutionStack.ts#L30">property nameRegex</a>
</h3>

```typescript
nameRegex: pulumi.Input<string>;
```


A regex string to apply to the solution stack list returned
by AWS. See [Elastic Beanstalk Supported Platforms][beanstalk-platforms] from
AWS documentation for reference solution stack names.

<h2 class="pdoc-module-header" id="GetSolutionStackResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getSolutionStack.ts#L36">interface GetSolutionStackResult</a>
</h2>

A collection of values returned by getSolutionStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/elasticbeanstalk/getSolutionStack.ts#L40">property name</a>
</h3>

```typescript
name: string;
```


The name of the solution stack.

