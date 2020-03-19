
---
title: "Environment"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an Elastic Beanstalk Environment Resource. Elastic Beanstalk allows
you to deploy and manage applications in the AWS cloud without worrying about
the infrastructure that runs those applications.

Environments are often things such as `development`, `integration`, or
`production`.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const tftest = new aws.elasticbeanstalk.Application("tftest", {
    description: "tf-test-desc",
});
const tfenvtest = new aws.elasticbeanstalk.Environment("tfenvtest", {
    application: tftest.name,
    solutionStackName: "64bit Amazon Linux 2015.03 v2.0.3 running Go 1.4",
});
```

## Option Settings

Some options can be stack-specific, check [AWS Docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html)
for supported options and examples.

The `setting` and `all_settings` mappings support the following format:

* `namespace` - unique namespace identifying the option's associated AWS resource
* `name` - name of the configuration option
* `value` - value for the configuration option
* `resource` - (Optional) resource name for [scheduled action](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction)

### Example With Options

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const tftest = new aws.elasticbeanstalk.Application("tftest", {
    description: "tf-test-desc",
});
const tfenvtest = new aws.elasticbeanstalk.Environment("tfenvtest", {
    application: tftest.name,
    settings: [
        {
            name: "VPCId",
            namespace: "aws:ec2:vpc",
            value: "vpc-xxxxxxxx",
        },
        {
            name: "Subnets",
            namespace: "aws:ec2:vpc",
            value: "subnet-xxxxxxxx",
        },
    ],
    solutionStackName: "64bit Amazon Linux 2015.03 v2.0.3 running Go 1.4",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_environment.html.markdown.



## Create a Environment Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#Environment">Environment</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#EnvironmentArgs">EnvironmentArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Environment</span><span class="p">(resource_name, opts=None, </span>application=None<span class="p">, </span>cname_prefix=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>platform_arn=None<span class="p">, </span>poll_interval=None<span class="p">, </span>settings=None<span class="p">, </span>solution_stack_name=None<span class="p">, </span>tags=None<span class="p">, </span>template_name=None<span class="p">, </span>tier=None<span class="p">, </span>version=None<span class="p">, </span>wait_for_ready_timeout=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewEnvironment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#EnvironmentArgs">EnvironmentArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#Environment">Environment</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.Environment.html">Environment</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.EnvironmentArgs.html">EnvironmentArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Environment resource with the given unique name, arguments, and options.

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
            <td class="align-top">Application</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticbeanstalk.<wbr>Environment<wbr>Setting<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
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
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">Application</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">[]elasticbeanstalk.<wbr>Environment<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
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
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Template<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">application</td>
            <td class="align-top">
                
                <code>string | Application</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">elasticbeanstalk.<wbr>Environment<wbr>Setting[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
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
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>Application<wbr>Version?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">application</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">poll_<wbr>interval</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">List[Environment<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">solution_<wbr>stack_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">template_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>ready_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Environment Output Properties

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
            <td class="align-top">All<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticbeanstalk.<wbr>Environment<wbr>All<wbr>Setting&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Application</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configurations</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticbeanstalk.<wbr>Environment<wbr>Setting&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Triggers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">All<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">[]elasticbeanstalk.<wbr>Environment<wbr>All<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Application</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configurations</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">[]elasticbeanstalk.<wbr>Environment<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Template<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Triggers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">all<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">elasticbeanstalk.<wbr>Environment<wbr>All<wbr>Setting[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">application</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Url</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Configurations</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">elasticbeanstalk.<wbr>Environment<wbr>Setting[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">triggers</td>
            <td class="align-top">
                
                <code>string[]</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>Application<wbr>Version</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">all_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">List[Environment<wbr>All<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">application</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the application that contains the version
to be deployed
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>configurations</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">poll_<wbr>interval</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">List[Environment<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">solution_<wbr>stack_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">template_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">triggers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>ready_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Environment Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#EnvironmentState">EnvironmentState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#Environment">Environment</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>all_settings=None<span class="p">, </span>application=None<span class="p">, </span>arn=None<span class="p">, </span>autoscaling_groups=None<span class="p">, </span>cname=None<span class="p">, </span>cname_prefix=None<span class="p">, </span>description=None<span class="p">, </span>endpoint_url=None<span class="p">, </span>instances=None<span class="p">, </span>launch_configurations=None<span class="p">, </span>load_balancers=None<span class="p">, </span>name=None<span class="p">, </span>platform_arn=None<span class="p">, </span>poll_interval=None<span class="p">, </span>queues=None<span class="p">, </span>settings=None<span class="p">, </span>solution_stack_name=None<span class="p">, </span>tags=None<span class="p">, </span>template_name=None<span class="p">, </span>tier=None<span class="p">, </span>triggers=None<span class="p">, </span>version=None<span class="p">, </span>wait_for_ready_timeout=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetEnvironment<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#EnvironmentState">EnvironmentState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#Environment">Environment</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.Environment.html">Environment</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.EnvironmentState.html">EnvironmentState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Environment resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">All<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticbeanstalk.<wbr>Environment<wbr>All<wbr>Setting<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Application</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the application that contains the version
to be deployed
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configurations</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">List&lt;Pulumi.<wbr>Aws.<wbr>Elasticbeanstalk.<wbr>Environment<wbr>Setting<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
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
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Triggers</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">All<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">[]elasticbeanstalk.<wbr>Environment<wbr>All<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Application</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the application that contains the version
to be deployed
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Endpoint<wbr>Url</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Instances</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Launch<wbr>Configurations</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Queues</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">[]elasticbeanstalk.<wbr>Environment<wbr>Setting</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
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
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Template<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tier</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Triggers</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Version</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">all<wbr>Settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">elasticbeanstalk.<wbr>Environment<wbr>All<wbr>Setting[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">application</td>
            <td class="align-top">
                
                <code>string | Application</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the application that contains the version
to be deployed
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling<wbr>Groups</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname<wbr>Prefix</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint<wbr>Url</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch<wbr>Configurations</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load<wbr>Balancers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">poll<wbr>Interval</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">elasticbeanstalk.<wbr>Environment<wbr>Setting[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">solution<wbr>Stack<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
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
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">template<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tier</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">triggers</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>Application<wbr>Version?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait<wbr>For<wbr>Ready<wbr>Timeout</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
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
            <td class="align-top">all_<wbr>settings</td>
            <td class="align-top">
                
                <code><a href="#environmentallsetting">List[Environment<wbr>All<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of all option settings configured in this Environment. These
are a combination of default settings and their overrides from `setting` in
the configuration.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">application</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the application that contains the version
to be deployed
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
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">autoscaling_<wbr>groups</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The autoscaling groups used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Fully qualified DNS name for this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">cname_<wbr>prefix</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Prefix to use for the fully qualified DNS name of
the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Short description of the Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">endpoint_<wbr>url</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL to the Load Balancer for this Environment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">instances</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Instances used by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">launch_<wbr>configurations</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Launch configurations in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">load_<wbr>balancers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic load balancers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">platform_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The [ARN][2] of the Elastic Beanstalk [Platform][3]
to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">poll_<wbr>interval</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The time between polling the AWS API to
check if changes have been applied. Use this to adjust the rate of API calls
for any `create` or `update` action. Minimum `10s`, maximum `180s`. Omit this to
use the default behavior, which is an exponential backoff
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">queues</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
SQS queues in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">settings</td>
            <td class="align-top">
                
                <code><a href="#environmentsetting">List[Environment<wbr>Setting]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">solution_<wbr>stack_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A solution stack to base your environment
off of. Example stacks can be found in the [Amazon API documentation][1]
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A set of tags to apply to the Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">template_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Configuration
template to use in deployment
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tier</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Elastic Beanstalk Environment tier. Valid values are `Worker`
or `WebServer`. If tier is left blank `WebServer` will be used.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">triggers</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Autoscaling triggers in use by this Environment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">version</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the Elastic Beanstalk Application Version
to use in deployment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">wait_<wbr>for_<wbr>ready_<wbr>timeout</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The maximum
[duration](https://golang.org/pkg/time/#ParseDuration) that this provider should
wait for an Elastic Beanstalk Environment to be in a ready state before timing
out.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### EnvironmentAllSetting
{{% lang nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EnvironmentAllSetting">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#EnvironmentAllSettingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the   <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.EnvironmentAllSetting.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource</td>
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource</td>
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource</td>
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource</td>
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
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### EnvironmentSetting
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#EnvironmentSetting">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#EnvironmentSetting">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#EnvironmentSettingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#EnvironmentSettingOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.EnvironmentSettingArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.EnvironmentSetting.html">output</a> API doc for this type.
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource</td>
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource</td>
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource</td>
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
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
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A unique name for this Environment. This name is used
in the application URL
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">namespace</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource</td>
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
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







