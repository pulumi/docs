
---
title: "ConfigurationTemplate"
block_external_search_index: true
---

Provides an Elastic Beanstalk Configuration Template, which are associated with
a specific application and are used to deploy different versions of the
application with the same configuration settings.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const tftest = new aws.elasticbeanstalk.Application("tftest", {
    description: "tf-test-desc",
});
const tfTemplate = new aws.elasticbeanstalk.ConfigurationTemplate("tf_template", {
    application: tftest.name,
    solutionStackName: "64bit Amazon Linux 2015.09 v2.0.8 running Go 1.4",
});
```

## Option Settings

The `setting` field supports the following format:

* `namespace` - unique namespace identifying the option's associated AWS resource
* `name` - name of the configuration option
* `value` - value for the configuration option
* `resource` - (Optional) resource name for [scheduled action](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options-general.html#command-options-general-autoscalingscheduledaction)

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/elastic_beanstalk_configuration_template.html.markdown.



## Create a ConfigurationTemplate Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#ConfigurationTemplate">ConfigurationTemplate</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#ConfigurationTemplateArgs">ConfigurationTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ConfigurationTemplate</span><span class="p">(resource_name, opts=None, </span>application=None<span class="p">, </span>description=None<span class="p">, </span>environment_id=None<span class="p">, </span>name=None<span class="p">, </span>settings=None<span class="p">, </span>solution_stack_name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewConfigurationTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#ConfigurationTemplateArgs">ConfigurationTemplateArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#ConfigurationTemplate">ConfigurationTemplate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.ConfigurationTemplate.html">ConfigurationTemplate</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.ElasticBeanstalk.ConfigurationTemplateArgs.html">ConfigurationTemplateArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">List&lt;Configuration<wbr>Template<wbr>Setting<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">[]Configuration<wbr>Template<wbr>Setting</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">Configuration<wbr>Template<wbr>Setting[]?</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>application</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">List[Configuration<wbr>Template<wbr>Setting]</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>solution_<wbr>stack_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ConfigurationTemplate Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">List&lt;Configuration<wbr>Template<wbr>Setting&gt;</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">[]Configuration<wbr>Template<wbr>Setting</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">Configuration<wbr>Template<wbr>Setting[]</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>application</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>environment_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">List[Configuration<wbr>Template<wbr>Setting]</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>solution_<wbr>stack_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ConfigurationTemplate Resource

Get an existing ConfigurationTemplate resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#ConfigurationTemplateState">ConfigurationTemplateState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/elasticbeanstalk/#ConfigurationTemplate">ConfigurationTemplate</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>application=None<span class="p">, </span>description=None<span class="p">, </span>environment_id=None<span class="p">, </span>name=None<span class="p">, </span>settings=None<span class="p">, </span>solution_stack_name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetConfigurationTemplate<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#ConfigurationTemplateState">ConfigurationTemplateState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#ConfigurationTemplate">ConfigurationTemplate</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.ConfigurationTemplate.html">ConfigurationTemplate</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Elasticbeanstalk.ConfigurationTemplateState.html">ConfigurationTemplateState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">List&lt;Configuration<wbr>Template<wbr>Setting<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Application</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">[]Configuration<wbr>Template<wbr>Setting</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">Configuration<wbr>Template<wbr>Setting[]?</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>solution<wbr>Stack<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>application</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}name of the application to associate with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Short description of the Template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the environment used with this configuration template
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>settings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#configurationtemplatesetting">List[Configuration<wbr>Template<wbr>Setting]</a></span>
    </dt>
    <dd>{{% md %}}Option settings to configure the new Environment. These
override specific values that are set as defaults. The format is detailed
below in Option Settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>solution_<wbr>stack_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A solution stack to base your Template
off of. Example stacks can be found in the [Amazon API documentation][1]
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Configuration<wbr>Template<wbr>Setting</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ConfigurationTemplateSetting">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ConfigurationTemplateSetting">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#ConfigurationTemplateSettingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/elasticbeanstalk?tab=doc#ConfigurationTemplateSettingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
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
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unique name for this Template.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
