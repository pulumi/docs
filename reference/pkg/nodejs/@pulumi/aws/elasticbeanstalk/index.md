---
title: Module elasticbeanstalk
---

<a href="../index.html">@pulumi/aws</a> &gt; elasticbeanstalk

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
* <a href="#GetHostedZoneResult">interface GetHostedZoneResult</a>
* <a href="#GetSolutionStackArgs">interface GetSolutionStackArgs</a>
* <a href="#GetSolutionStackResult">interface GetSolutionStackResult</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts">elasticbeanstalk/application.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts">elasticbeanstalk/applicationVersion.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts">elasticbeanstalk/configurationTemplate.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts">elasticbeanstalk/environment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getHostedZone.ts">elasticbeanstalk/getHostedZone.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts">elasticbeanstalk/getSolutionStack.ts</a> 


<h2 class="pdoc-module-header" id="Application">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L15">class Application</a>
</h2>

Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

This resource creates an application that has one configuration template named
`default`, and no application versions

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L36">constructor</a>
</h3>

```typescript
new Application(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Application resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L24">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L28">property appversionLifecycle</a>
</h3>

```typescript
public appversionLifecycle: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the application, must be unique within your account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ApplicationVersion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L28">class ApplicationVersion</a>
</h2>

Provides an Elastic Beanstalk Application Version Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

This resource creates a Beanstalk Application Version that can be deployed to a Beanstalk
Environment.

~> **NOTE on Application Version Resource:**  When using the Application Version resource with multiple
Elastic Beanstalk Environments it is possible that an error may be returned
when attempting to delete an Application Version while it is still in use by a different environment.
To work around this you can:
<ol>
<li>Create each environment in a separate AWS account</li>
<li>Create your `aws_elastic_beanstalk_application_version` resources with a unique names in your
Elastic Beanstalk Application. For example &lt;revision&gt;-&lt;environment&gt;.</li>
</ol>

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L65">constructor</a>
</h3>

```typescript
new ApplicationVersion(name: string, args: ApplicationVersionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ApplicationVersion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L37">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationVersionState): ApplicationVersion
```


Get an existing ApplicationVersion resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L44">property application</a>
</h3>

```typescript
public application: pulumi.Output<Application>;
```


Name of the Beanstalk Application the version is associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L48">property bucket</a>
</h3>

```typescript
public bucket: pulumi.Output<string>;
```


S3 bucket that contains the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L52">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L57">property forceDelete</a>
</h3>

```typescript
public forceDelete: pulumi.Output<boolean | undefined>;
```


On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L61">property key</a>
</h3>

```typescript
public key: pulumi.Output<string>;
```


S3 object that is the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L65">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the this Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ConfigurationTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L12">class ConfigurationTemplate</a>
</h2>

Provides an Elastic Beanstalk Configuration Template, which are associated with
a specific application and are used to deploy different versions of the
application with the same configuration settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L51">constructor</a>
</h3>

```typescript
new ConfigurationTemplate(name: string, args: ConfigurationTemplateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ConfigurationTemplate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConfigurationTemplateState): ConfigurationTemplate
```


Get an existing ConfigurationTemplate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L28">property application</a>
</h3>

```typescript
public application: pulumi.Output<string>;
```


name of the application to associate with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the Template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L36">property environmentId</a>
</h3>

```typescript
public environmentId: pulumi.Output<string | undefined>;
```


The ID of the environment used with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for this Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L46">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }[]>;
```


Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L51">property solutionStackName</a>
</h3>

```typescript
public solutionStackName: pulumi.Output<string | undefined>;
```


A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Environment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L19">class Environment</a>
</h2>

Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

Environments are often things such as `development`, `integration`, or
`production`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L129">constructor</a>
</h3>

```typescript
new Environment(name: string, args: EnvironmentArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Environment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L28">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EnvironmentState): Environment
```


Get an existing Environment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L37">property allSettings</a>
</h3>

```typescript
public allSettings: pulumi.Output<{ ... }[]>;
```


List of all option settings configured in the Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L42">property application</a>
</h3>

```typescript
public application: pulumi.Output<Application>;
```


Name of the application that contains the version
to be deployed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L43">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L47">property autoscalingGroups</a>
</h3>

```typescript
public autoscalingGroups: pulumi.Output<string[]>;
```


The autoscaling groups used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L51">property cname</a>
</h3>

```typescript
public cname: pulumi.Output<string>;
```


Fully qualified DNS name for the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L56">property cnamePrefix</a>
</h3>

```typescript
public cnamePrefix: pulumi.Output<string>;
```


Prefix to use for the fully qualified DNS name of
the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L60">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Short description of the Environment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L64">property instances</a>
</h3>

```typescript
public instances: pulumi.Output<string[]>;
```


Instances used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L68">property launchConfigurations</a>
</h3>

```typescript
public launchConfigurations: pulumi.Output<string[]>;
```


Launch configurations in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L72">property loadBalancers</a>
</h3>

```typescript
public loadBalancers: pulumi.Output<string[]>;
```


Elastic load balancers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L77">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for this Environment. This name is used
in the application URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L84">property pollInterval</a>
</h3>

```typescript
public pollInterval: pulumi.Output<string | undefined>;
```


The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L88">property queues</a>
</h3>

```typescript
public queues: pulumi.Output<string[]>;
```


SQS queues in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L94">property settings</a>
</h3>

```typescript
public settings: pulumi.Output<{ ... }[] | undefined>;
```


Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L99">property solutionStackName</a>
</h3>

```typescript
public solutionStackName: pulumi.Output<string>;
```


A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L103">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A set of tags to apply to the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L108">property templateName</a>
</h3>

```typescript
public templateName: pulumi.Output<string | undefined>;
```


The name of the Elastic Beanstalk Configuration
template to use in deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L113">property tier</a>
</h3>

```typescript
public tier: pulumi.Output<string | undefined>;
```


Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L117">property triggers</a>
</h3>

```typescript
public triggers: pulumi.Output<string[]>;
```


Autoscaling triggers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L122">property version</a>
</h3>

```typescript
public version: pulumi.Output<ApplicationVersion>;
```


The name of the Elastic Beanstalk Application Version
to use in deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L129">property waitForReadyTimeout</a>
</h3>

```typescript
public waitForReadyTimeout: pulumi.Output<string | undefined>;
```


The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.

<h2 class="pdoc-module-header" id="getHostedZone">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getHostedZone.ts#L10">function getHostedZone</a>
</h2>

```typescript
getHostedZone(args?: GetHostedZoneArgs, opts?: pulumi.InvokeOptions): Promise<GetHostedZoneResult>
```


Use this data source to get the ID of an [elastic beanstalk hosted zone](http://docs.aws.amazon.com/general/latest/gr/rande.html#elasticbeanstalk_region).

<h2 class="pdoc-module-header" id="getSolutionStack">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L10">function getSolutionStack</a>
</h2>

```typescript
getSolutionStack(args: GetSolutionStackArgs, opts?: pulumi.InvokeOptions): Promise<GetSolutionStackResult>
```


Use this data source to get the name of a elastic beanstalk solution stack.

<h2 class="pdoc-module-header" id="ApplicationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L81">interface ApplicationArgs</a>
</h2>

The set of arguments for constructing a Application resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L82">property appversionLifecycle</a>
</h3>

```typescript
appversionLifecycle?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L86">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L90">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application, must be unique within your account

<h2 class="pdoc-module-header" id="ApplicationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L66">interface ApplicationState</a>
</h2>

Input properties used for looking up and filtering Application resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L67">property appversionLifecycle</a>
</h3>

```typescript
appversionLifecycle?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L71">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the application

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/application.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the application, must be unique within your account

<h2 class="pdoc-module-header" id="ApplicationVersionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L141">interface ApplicationVersionArgs</a>
</h2>

The set of arguments for constructing a ApplicationVersion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L145">property application</a>
</h3>

```typescript
application: pulumi.Input<Application>;
```


Name of the Beanstalk Application the version is associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L149">property bucket</a>
</h3>

```typescript
bucket: pulumi.Input<string | Bucket>;
```


S3 bucket that contains the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L153">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L158">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L162">property key</a>
</h3>

```typescript
key: pulumi.Input<string>;
```


S3 object that is the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L166">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the this Application Version.

<h2 class="pdoc-module-header" id="ApplicationVersionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L110">interface ApplicationVersionState</a>
</h2>

Input properties used for looking up and filtering ApplicationVersion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L114">property application</a>
</h3>

```typescript
application?: pulumi.Input<Application>;
```


Name of the Beanstalk Application the version is associated with.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L118">property bucket</a>
</h3>

```typescript
bucket?: pulumi.Input<string | Bucket>;
```


S3 bucket that contains the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L122">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Application Version.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L127">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


On delete, force an Application Version to be deleted when it may be in use
by multiple Elastic Beanstalk Environments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L131">property key</a>
</h3>

```typescript
key?: pulumi.Input<string>;
```


S3 object that is the Application Version source bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/applicationVersion.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the this Application Version.

<h2 class="pdoc-module-header" id="ConfigurationTemplateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L123">interface ConfigurationTemplateArgs</a>
</h2>

The set of arguments for constructing a ConfigurationTemplate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L127">property application</a>
</h3>

```typescript
application: pulumi.Input<string>;
```


name of the application to associate with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L131">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L135">property environmentId</a>
</h3>

```typescript
environmentId?: pulumi.Input<string>;
```


The ID of the environment used with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L145">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L150">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```


A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]

<h2 class="pdoc-module-header" id="ConfigurationTemplateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L90">interface ConfigurationTemplateState</a>
</h2>

Input properties used for looking up and filtering ConfigurationTemplate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L94">property application</a>
</h3>

```typescript
application?: pulumi.Input<string>;
```


name of the application to associate with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L102">property environmentId</a>
</h3>

```typescript
environmentId?: pulumi.Input<string>;
```


The ID of the environment used with this configuration template

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L112">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/configurationTemplate.ts#L117">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```


A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]

<h2 class="pdoc-module-header" id="EnvironmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L302">interface EnvironmentArgs</a>
</h2>

The set of arguments for constructing a Environment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L307">property application</a>
</h3>

```typescript
application: pulumi.Input<Application>;
```


Name of the application that contains the version
to be deployed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L312">property cnamePrefix</a>
</h3>

```typescript
cnamePrefix?: pulumi.Input<string>;
```


Prefix to use for the fully qualified DNS name of
the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L316">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Environment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L321">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Environment. This name is used
in the application URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L328">property pollInterval</a>
</h3>

```typescript
pollInterval?: pulumi.Input<string>;
```


The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L334">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L339">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```


A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L343">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A set of tags to apply to the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L348">property templateName</a>
</h3>

```typescript
templateName?: pulumi.Input<string>;
```


The name of the Elastic Beanstalk Configuration
template to use in deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L353">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L358">property version</a>
</h3>

```typescript
version?: pulumi.Input<ApplicationVersion>;
```


The name of the Elastic Beanstalk Application Version
to use in deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L365">property waitForReadyTimeout</a>
</h3>

```typescript
waitForReadyTimeout?: pulumi.Input<string>;
```


The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.

<h2 class="pdoc-module-header" id="EnvironmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L198">interface EnvironmentState</a>
</h2>

Input properties used for looking up and filtering Environment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L204">property allSettings</a>
</h3>

```typescript
allSettings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of all option settings configured in the Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L209">property application</a>
</h3>

```typescript
application?: pulumi.Input<Application>;
```


Name of the application that contains the version
to be deployed

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L210">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L214">property autoscalingGroups</a>
</h3>

```typescript
autoscalingGroups?: pulumi.Input<pulumi.Input<string>[]>;
```


The autoscaling groups used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L218">property cname</a>
</h3>

```typescript
cname?: pulumi.Input<string>;
```


Fully qualified DNS name for the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L223">property cnamePrefix</a>
</h3>

```typescript
cnamePrefix?: pulumi.Input<string>;
```


Prefix to use for the fully qualified DNS name of
the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L227">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Short description of the Environment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L231">property instances</a>
</h3>

```typescript
instances?: pulumi.Input<pulumi.Input<string>[]>;
```


Instances used by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L235">property launchConfigurations</a>
</h3>

```typescript
launchConfigurations?: pulumi.Input<pulumi.Input<string>[]>;
```


Launch configurations in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L239">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<pulumi.Input<string>[]>;
```


Elastic load balancers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L244">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for this Environment. This name is used
in the application URL

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L251">property pollInterval</a>
</h3>

```typescript
pollInterval?: pulumi.Input<string>;
```


The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L255">property queues</a>
</h3>

```typescript
queues?: pulumi.Input<pulumi.Input<string>[]>;
```


SQS queues in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L261">property settings</a>
</h3>

```typescript
settings?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L266">property solutionStackName</a>
</h3>

```typescript
solutionStackName?: pulumi.Input<string>;
```


A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L270">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A set of tags to apply to the Environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L275">property templateName</a>
</h3>

```typescript
templateName?: pulumi.Input<string>;
```


The name of the Elastic Beanstalk Configuration
template to use in deployment

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L280">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L284">property triggers</a>
</h3>

```typescript
triggers?: pulumi.Input<pulumi.Input<string>[]>;
```


Autoscaling triggers in use by this environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L289">property version</a>
</h3>

```typescript
version?: pulumi.Input<ApplicationVersion>;
```


The name of the Elastic Beanstalk Application Version
to use in deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/environment.ts#L296">property waitForReadyTimeout</a>
</h3>

```typescript
waitForReadyTimeout?: pulumi.Input<string>;
```


The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that Terraform should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.

<h2 class="pdoc-module-header" id="GetHostedZoneArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getHostedZone.ts#L20">interface GetHostedZoneArgs</a>
</h2>

A collection of arguments for invoking getHostedZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getHostedZone.ts#L24">property region</a>
</h3>

```typescript
region?: string;
```


The region you'd like the zone for. By default, fetches the current region.

<h2 class="pdoc-module-header" id="GetHostedZoneResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getHostedZone.ts#L30">interface GetHostedZoneResult</a>
</h2>

A collection of values returned by getHostedZone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getHostedZone.ts#L34">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h2 class="pdoc-module-header" id="GetSolutionStackArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L20">interface GetSolutionStackArgs</a>
</h2>

A collection of arguments for invoking getSolutionStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L25">property mostRecent</a>
</h3>

```typescript
mostRecent?: boolean;
```


If more than one result is returned, use the most
recent solution stack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L31">property nameRegex</a>
</h3>

```typescript
nameRegex: string;
```


A regex string to apply to the solution stack list returned
by AWS. See [Elastic Beanstalk Supported Platforms][beanstalk-platforms] from
AWS documentation for reference solution stack names.

<h2 class="pdoc-module-header" id="GetSolutionStackResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L37">interface GetSolutionStackResult</a>
</h2>

A collection of values returned by getSolutionStack.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L45">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/elasticbeanstalk/getSolutionStack.ts#L41">property name</a>
</h3>

```typescript
name: string;
```


The name of the solution stack.

